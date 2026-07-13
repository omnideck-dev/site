#!/usr/bin/env bash
# Scans content/blog/ for the most recent published post and writes data/homepage.toml.
# Run standalone or via the Claude Code PostToolUse hook.

set -euo pipefail

BLOG_DIR="content/blog"
OUT="data/homepage.toml"

latest_file=""
latest_date=""

for f in "$BLOG_DIR"/*.md; do
  [[ -f "$f" ]] || continue
  [[ "$(basename "$f")" == "index.md" ]] && continue
  grep -q 'tag_index' "$f" 2>/dev/null && continue
  grep -q '^draft *= *true' "$f" 2>/dev/null && continue

  file_date=$(grep '^date' "$f" | head -1 | sed 's/date[[:space:]]*=[[:space:]]*//' | tr -d '"' | xargs)
  [[ -z "$file_date" ]] && continue

  if [[ -z "$latest_date" || "$file_date" > "$latest_date" ]]; then
    latest_date="$file_date"
    latest_file="$f"
  fi
done

if [[ -z "$latest_file" ]]; then
  echo "update-latest-post: no published blog posts found" >&2
  exit 0
fi

title=$(grep '^title' "$latest_file" | head -1 \
  | sed 's/title[[:space:]]*=[[:space:]]*//' | tr -d '"' | xargs)

display_date=$(python3 -c "
from datetime import datetime
d = datetime.strptime('$latest_date', '%Y-%m-%d')
print(f'{d.strftime(\"%B\")} {d.day}, {d.year}')
" 2>/dev/null || echo "$latest_date")

slug=$(basename "$latest_file" .md)
url="/blog/${slug}.html"

cat > "$OUT" <<TOML
[latest_post]
title = "$title"
date  = "$display_date"
url   = "$url"
TOML

echo "update-latest-post: $title ($display_date)"
