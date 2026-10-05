#!/usr/bin/env python3
"""Check built or deployed pages against the exact release snapshot used to build."""

import argparse
from html.parser import HTMLParser
import json
import pathlib
import sys
import time
import urllib.request


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = set()
        self.links = set()
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("data-release-tag"):
            self.tags.add(attrs["data-release-tag"])
        if tag == "a" and attrs.get("href"):
            self.links.add(attrs["href"])


def read(root, path):
    if root.startswith(("https://", "http://")):
        request = urllib.request.Request(f"{root.rstrip('/')}/{path}?release-check={time.time_ns()}",
                                         headers={"User-Agent": "omnideck-site-verification", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")
    return (pathlib.Path(root) / path).read_text(encoding="utf-8")


def check_pages(root, expected):
    actual = json.loads(read(root, "releases.json"))
    if actual != expected:
        raise RuntimeError("Site release manifest does not match the current GitHub release snapshot")
    latest = expected["releases"][0]
    home = Page(read(root, "index.html"))
    if latest["tag"] not in home.tags or latest["url"] not in home.links:
        raise RuntimeError(f"Homepage is missing latest release {latest['tag']}")
    feed = Page(read(root, "whats-new.html"))
    for release in expected["releases"]:
        if release["tag"] not in feed.tags or release["url"] not in feed.links:
            raise RuntimeError(f"What's new is missing release {release['tag']}")
    install_html = read(root, "install.html")
    install = Page(install_html)
    if expected["desktop_tag"] not in install.tags:
        raise RuntimeError(f"Install page is missing desktop release {expected['desktop_tag']}")
    for asset in expected["downloads"].values():
        if not asset["url"] or asset["url"] not in install.links:
            raise RuntimeError(f"Install page is missing download {asset['filename']}")
        if not asset["checksum_url"]:
            raise RuntimeError(f"Download has no checksum: {asset['filename']}")
        if not asset.get("sha256") or asset["sha256"] not in install_html:
            raise RuntimeError(f"Install page is missing the SHA-256 fingerprint for {asset['filename']}")


def check_downloads(expected):
    urls = {asset[key] for asset in expected["downloads"].values() for key in ("url", "checksum_url")}
    urls.add(expected["desktop_url"])
    urls.update(release["url"] for release in expected["releases"])
    for url in sorted(urls):
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "omnideck-site-verification"})
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(f"Release link returned {response.status}: {url}")
    print(f"Verified {len(urls)} release, package, and checksum links")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", help="Build output directory or deployed website URL")
    parser.add_argument("--expected", default="static/releases.json")
    parser.add_argument("--attempts", type=int, default=1, help="Retries for Pages deployment propagation")
    parser.add_argument("--check-downloads", action="store_true")
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error("--attempts must be at least 1")
    expected = json.loads(pathlib.Path(args.expected).read_text(encoding="utf-8"))
    for attempt in range(args.attempts):
        try:
            check_pages(args.root, expected)
            break
        except (OSError, ValueError, RuntimeError) as error:
            if attempt == args.attempts - 1:
                raise
            print(f"Waiting for site deployment ({attempt + 1}/{args.attempts}): {error}", flush=True)
            time.sleep(15)
    if args.check_downloads:
        check_downloads(expected)
    print(f"Verified {args.root}: latest {expected['releases'][0]['tag']}, desktop {expected['desktop_tag']}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Site verification failed: {error}", file=sys.stderr)
        sys.exit(1)
