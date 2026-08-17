#!/usr/bin/env bash
# Regenerates data/tags.toml, tag pages, and data/homepage.toml from blog post frontmatter.
# Run manually, from the pre-commit hook, or from CI before building.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 sync-tags.py
bash scripts/update-latest-post.sh
