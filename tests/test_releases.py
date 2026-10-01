import copy
import importlib.util
import json
import pathlib
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


sync = module('sync', 'sync-releases.py')
desktop = sync.desktop
verify = module('verify', 'verify-site.py')
import release_data


def release(tag, date, assets=None, draft=False, body='A published improvement.'):
    return {'tag_name': tag, 'published_at': date, 'draft': draft,
            'prerelease': 'beta' in tag, 'assets': assets or [], 'body': body,
            'html_url': f'https://github.com/omnideck-dev/omnideck/releases/tag/{tag}'}


def installers():
    suffixes = ['_aarch64.dmg', '_x64.dmg', '_x64-setup.exe', '_arm64-setup.exe',
                '_amd64.AppImage', '_aarch64.AppImage', '_amd64.deb', '_arm64.deb',
                '.x86_64.rpm', '.aarch64.rpm']
    result = []
    for suffix in suffixes:
        name = 'omnideck_0.1.0-beta.11' + suffix
        for filename in [name, name + '.sha256']:
            result.append({'name': filename, 'size': 1000,
                           'browser_download_url': f'https://github.com/download/{filename}'})
    return result


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.desktop = release('v0.1.0-beta.11', '2026-08-19T14:50:15Z', installers())
        self.app = release('app-v0.5.2', '2026-09-27T23:24:01Z')
        self.cli = release('v0.11.0-beta.6', '2026-09-29T01:55:17Z')

    def test_runtime_and_drafts_do_not_replace_desktop(self):
        draft = release('v0.2.0', '2026-10-01T00:00:00Z', installers(), draft=True)
        self.assertEqual(desktop.newest_published_release([self.app, draft, self.desktop]), self.desktop)

    def test_newest_desktop_with_missing_assets_fails_instead_of_reverting(self):
        newer = release('v0.2.0', '2026-10-01T00:00:00Z', installers()[:-2])
        with self.assertRaisesRegex(RuntimeError, 'linux_arm64_rpm'):
            desktop.sync([newer, self.desktop])

    def test_missing_checksum_fails(self):
        self.desktop['assets'] = [asset for asset in installers() if not asset['name'].endswith('_x64.dmg.sha256')]
        with self.assertRaisesRegex(RuntimeError, 'macos_x64'):
            desktop.sync([self.desktop])

    def test_api_failure_does_not_report_success_with_checked_in_data(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / 'desktop_release.toml'
            path.write_text('old data')
            with patch.object(desktop, 'OUTPUT', path), patch.object(desktop, 'fetch_releases', side_effect=OSError('offline')):
                with self.assertRaises(OSError):
                    desktop.main()
            self.assertEqual(path.read_text(), 'old data')

    def test_all_streams_sorted_by_publication_with_preview_labels(self):
        entries = sync.feed([self.desktop, self.app], [self.cli])
        self.assertEqual([item['kind'] for item in entries], ['CLI', 'App / runtime', 'Desktop installer'])
        self.assertEqual(entries[0]['channel'], 'Preview')
        self.assertEqual(entries[1]['channel'], 'Stable')
        self.assertEqual(entries[1]['title'], 'App / runtime 0.5.2')
        data = tomllib.loads(sync.render(entries))
        self.assertEqual(data['latest'], entries[0])
        self.assertEqual(data['items'], entries)

    def test_drafts_and_unknown_tags_excluded(self):
        draft = copy.deepcopy(self.app)
        draft['draft'] = True
        self.assertEqual(sync.feed([draft, release('container-x', '2026-10-01T00:00:00Z')], [self.cli])[0]['kind'], 'CLI')

    def test_note_excerpt_is_plain_prose_and_bounded(self):
        text = sync.summary('# Title\n\n## Added\n\n- Use [MCP](https://example.com) with `tools`. ' + 'Words ' * 80)
        self.assertTrue(text.startswith('Use MCP with tools.'))
        self.assertLessEqual(len(text), 240)
        entries = sync.feed([release('app-v0.1.0', '2026-09-01T00:00:00Z', body='Quotes " and \\ and <script>.')], [])
        self.assertEqual(tomllib.loads(sync.render(entries))['latest']['summary'], entries[0]['summary'])
        self.assertEqual(sync.summary('**Full Changelog**: https://github.com/compare/old...new'), '')

    def test_pagination_and_publication_order(self):
        class Response:
            def __init__(self, releases, link=''):
                self.payload = json.dumps(releases).encode()
                self.headers = {'Link': link}
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def read(self):
                return self.payload
        with patch.object(release_data.urllib.request, 'urlopen', side_effect=[
            Response([self.desktop], '<https://api.github.com/next>; rel="next"'),
            Response([self.app])]) as fetch:
            result = release_data.fetch_releases('omnideck-dev/omnideck')
        self.assertEqual(fetch.call_count, 2)
        self.assertEqual(release_data.published_releases(result)[0], self.app)


class VerificationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = pathlib.Path(self.directory.name)
        self.expected = {'releases': [{'tag': 'app-v0.5.2', 'url': 'https://github.com/notes'}],
                         'desktop_tag': 'v0.1.0-beta.11', 'desktop_url': 'https://github.com/desktop',
                         'downloads': {'mac': {'filename': 'mac.dmg', 'url': 'https://github.com/mac.dmg',
                                               'checksum_url': 'https://github.com/mac.dmg.sha256'}}}
        (self.root / 'releases.json').write_text(json.dumps(self.expected))
        for name in ['index.html', 'whats-new.html']:
            (self.root / name).write_text('<aside data-release-tag="app-v0.5.2"><a href="https://github.com/notes">Notes</a></aside>')
        (self.root / 'install.html').write_text('<aside data-release-tag="v0.1.0-beta.11"><a href="https://github.com/mac.dmg">Download</a></aside>')

    def test_valid_build(self):
        verify.check_pages(str(self.root), self.expected)

    def test_stale_manifest(self):
        (self.root / 'releases.json').write_text('{}')
        with self.assertRaisesRegex(RuntimeError, 'manifest'):
            verify.check_pages(str(self.root), self.expected)

    def test_stale_homepage_despite_fresh_manifest(self):
        (self.root / 'index.html').write_text('Latest blog August 16')
        with self.assertRaisesRegex(RuntimeError, 'Homepage'):
            verify.check_pages(str(self.root), self.expected)

    def test_missing_feed_entry(self):
        (self.root / 'whats-new.html').write_text('No releases')
        with self.assertRaisesRegex(RuntimeError, "What's new"):
            verify.check_pages(str(self.root), self.expected)

    def test_stale_install_page(self):
        (self.root / 'install.html').write_text('<aside data-release-tag="old">')
        with self.assertRaisesRegex(RuntimeError, 'desktop release'):
            verify.check_pages(str(self.root), self.expected)

    def test_missing_download(self):
        (self.root / 'install.html').write_text('<aside data-release-tag="v0.1.0-beta.11">')
        with self.assertRaisesRegex(RuntimeError, 'missing download'):
            verify.check_pages(str(self.root), self.expected)

    def test_network_verification_uses_head_for_packages_and_checksums(self):
        class Response:
            status = 200
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
        with patch.object(verify.urllib.request, 'urlopen', return_value=Response()) as fetch:
            verify.check_downloads(self.expected)
        self.assertEqual({call.args[0].get_method() for call in fetch.call_args_list}, {'HEAD'})
        self.assertIn('https://github.com/mac.dmg.sha256', {call.args[0].full_url for call in fetch.call_args_list})

    def test_broken_package_link_fails(self):
        with patch.object(verify.urllib.request, 'urlopen', side_effect=OSError('404 Not Found')):
            with self.assertRaises(OSError):
                verify.check_downloads(self.expected)


if __name__ == '__main__':
    unittest.main()
