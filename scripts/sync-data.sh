#!/usr/bin/env bash
# Regenerates release, tag, and homepage data used by the static site.
# Run manually, from the pre-commit hook, or from CI before building.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 sync-tags.py
bash scripts/update-latest-post.sh
python3 scripts/sync-desktop-release.py
