"""Shared GitHub release fetching and ordering for the static site."""

import datetime as dt
import json
import os
import urllib.request


APP_REPOSITORY = os.environ.get("OMNIDECK_DESKTOP_RELEASE_REPO", "omnideck-dev/omnideck")
CLI_REPOSITORY = os.environ.get("OMNIDECK_CLI_RELEASE_REPO", "omnideck-dev/cli")


def fetch_releases(repository):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "omnideck-site-release-sync",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{repository}/releases?per_page=100"
    releases = []
    while url:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            releases.extend(json.load(response))
            # GitHub orders by creation, which can differ from publication.
            url = next((part.split(";")[0].strip()[1:-1]
                        for part in response.headers.get("Link", "").split(",")
                        if 'rel="next"' in part), None)
    return releases


def publication_time(release):
    return dt.datetime.fromisoformat(release["published_at"].replace("Z", "+00:00"))


def published_releases(releases):
    return sorted((release for release in releases
                   if not release.get("draft") and release.get("published_at")),
                  key=publication_time, reverse=True)


def desktop_releases(releases):
    # app-v* records describe the runtime, not installable desktop packages.
    return [release for release in published_releases(releases)
            if release["tag_name"].startswith("v")]


def write_atomic(path, content):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)
