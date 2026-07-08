#!/usr/bin/env python3
"""
Sync blog tags from post front matter.

Scans content/blog/*.md, collects all tags and their counts, then:
  - Updates data/tags.toml (adds new tags, refreshes counts, preserves custom slugs)
  - Creates any missing content/blog/tags/<slug>.md pages
  - Warns about tags in tags.toml that no post uses

Usage:
    python3 sync-tags.py
    ./sync-tags.py   (if executable)
"""

import re
import os
import glob
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR  = os.path.join(ROOT, "content", "blog")
TAGS_DIR  = os.path.join(ROOT, "content", "blog", "tags")
TAGS_TOML = os.path.join(ROOT, "data", "tags.toml")


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def extract_tags(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"^\+\+\+\s*\n(.*?)\n\+\+\+", content, re.DOTALL)
    if not m:
        return []
    fm = m.group(1)
    tm = re.search(r"^tags\s*=\s*\[(.*?)\]", fm, re.MULTILINE | re.DOTALL)
    if not tm:
        return []
    return re.findall(r'"([^"]+)"', tm.group(1))


def load_tags_toml():
    """Return dict of name -> {slug, count} from existing tags.toml."""
    result = {}
    if not os.path.exists(TAGS_TOML):
        return result
    with open(TAGS_TOML, encoding="utf-8") as f:
        content = f.read()
    for block in re.split(r"\[\[tags\]\]", content)[1:]:
        nm = re.search(r'name\s*=\s*"([^"]+)"', block)
        sm = re.search(r'slug\s*=\s*"([^"]+)"', block)
        cm = re.search(r"count\s*=\s*(\d+)", block)
        if nm:
            name = nm.group(1)
            result[name] = {
                "slug":  sm.group(1) if sm else slugify(name),
                "count": int(cm.group(1)) if cm else 0,
            }
    return result


def write_tags_toml(tags):
    """Write tags.toml only if content has changed. Returns True if file was written."""
    lines = []
    for name in sorted(tags):
        t = tags[name]
        lines += [
            "[[tags]]",
            f'name  = "{name}"',
            f'slug  = "{t["slug"]}"',
            f'count = {t["count"]}',
            "",
        ]
    new_content = "\n".join(lines)
    if os.path.exists(TAGS_TOML):
        with open(TAGS_TOML, encoding="utf-8") as f:
            if f.read() == new_content:
                return False
    with open(TAGS_TOML, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


TAG_PAGE = """\
+++
title    = "{name}"
date     = {today}
draft    = false
template = "templates/types/tag.html"

[extra]
tag_index    = true
description = "Blog posts tagged with {name}"
+++
"""


def ensure_tag_page(name, slug):
    os.makedirs(TAGS_DIR, exist_ok=True)
    path = os.path.join(TAGS_DIR, f"{slug}.md")
    if os.path.exists(path):
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAG_PAGE.format(name=name, today=date.today().isoformat()))
    return True


def main():
    # Collect tags from blog posts, excluding tag pages
    post_files = [
        p for p in glob.glob(os.path.join(BLOG_DIR, "*.md"))
        if os.path.basename(p) != "index.md"
    ]

    counts = {}
    for path in post_files:
        for tag in extract_tags(path):
            counts[tag] = counts.get(tag, 0) + 1

    if not counts:
        print("No tags found in blog posts.")
        sys.exit(0)

    existing = load_tags_toml()

    # Build updated tag map: preserve custom slugs for known tags
    updated = {}
    new_tags = []
    for name, count in counts.items():
        slug = existing[name]["slug"] if name in existing else slugify(name)
        updated[name] = {"slug": slug, "count": count}
        if name not in existing:
            new_tags.append(name)

    toml_changed = write_tags_toml(updated)
    if toml_changed:
        print(f"data/tags.toml updated  ({len(updated)} tag(s))")

    # Create missing tag pages
    created = []
    for name, entry in updated.items():
        if ensure_tag_page(name, entry["slug"]):
            created.append(name)

    if new_tags:
        print(f"New tags:               {', '.join(sorted(new_tags))}")
    if created:
        print(f"Tag pages created:      {', '.join(sorted(created))}")

    # Warn about orphans (in toml but not in any post)
    orphans = [n for n in existing if n not in updated]
    if orphans:
        print(f"Unused tags (not in any post): {', '.join(sorted(orphans))}")
        print("  → Remove them from data/tags.toml and delete their tag pages manually if no longer needed.")

    if not toml_changed and not new_tags and not created and not orphans:
        pass  # true no-op: no output, no file changes


if __name__ == "__main__":
    main()
