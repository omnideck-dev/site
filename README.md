# Omnideck Site — Content Guide

This is the public site for Omnideck. Content is written in Markdown with TOML front matter. No build tools or Node.js required.

## First-time setup

Clone the repo, then activate the git hook that keeps tags in sync automatically:

```bash
git config core.hooksPath .githooks
```

That's it. No npm install, no build step.

---

## Previewing the site

```bash
./arbor preview
```

Opens a live-reloading dev server at `http://localhost:8080`. Changes to content, templates, and CSS are picked up automatically.

---

## Content types

### Blog posts

**Location:** `content/blog/<slug>.md`

```toml
+++
title    = "Your Post Title"
date     = 2026-01-15
draft    = false
tags     = ["Tag One", "Tag Two"]
template = "templates/types/blog.html"

[extra]
description    = "One or two sentences shown in previews and meta tags."
author         = "Your Name"
featured_image = "/images/your-image.jpg"
+++

Your content here...
```

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Displayed as the page `<h1>` |
| `date` | yes | Format: `YYYY-MM-DD` |
| `draft` | yes | Set `true` to hide from the live site |
| `tags` | no | Array of strings — see [Tags](#tags) below |
| `template` | yes | Always `"templates/types/blog.html"` for blog posts |
| `description` | no | Used in meta tags and the blog listing |
| `author` | no | Shown below the title |
| `featured_image` | no | Path under `static/images/` — e.g. `/images/my-photo.jpg`. Shown full-width above the title and used for social link previews. |

To create a new post stub:

```bash
./arbor new blog my-post-slug
```

---

### Docs pages

**Location:** `content/docs/<slug>.md`

```toml
+++
title    = "Page Title"
date     = 2026-01-15
draft    = false
template = "templates/types/docs.html"

[extra]
description = "One sentence shown in meta tags."
order       = 3
+++

Your content here...
```

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Displayed as the page `<h1>` and in the sidebar |
| `date` | yes | Format: `YYYY-MM-DD` |
| `draft` | yes | Set `true` to hide from the live site |
| `template` | yes | Always `"templates/types/docs.html"` |
| `description` | no | Used in meta tags |
| `order` | no | Integer — controls sort order in the sidebar nav |

---

### General pages

**Location:** `content/<slug>.md`

```toml
+++
title    = "Page Title"
date     = 2026-01-15
draft    = false
template = "templates/types/page.html"

[extra]
description = "One sentence shown in meta tags."
+++

Your content here...
```

---

## Tags

Tags appear as chips on blog posts and cards. Each tag has its own listing page linked from a sidebar on the blog.

**Tags are managed automatically.** Just add them to a post's front matter:

```toml
tags = ["AI", "Open Source", "New Tag"]
```

When you commit, the pre-commit hook runs `sync-tags.py`, which:
- Updates `data/tags.toml` with current counts
- Creates any missing `content/blog/tags/<slug>.md` pages
- Stages those changes so they're included in your commit

You never need to touch `data/tags.toml` or the tag pages directly.

If you want to run it manually outside of a commit:

```bash
./sync-tags.py
```

The script is a no-op if nothing has changed — safe to run anytime.

---

## Images

Place images in `static/images/` and reference them as `/images/filename.jpg`.

For blog post hero images, set `featured_image` in the front matter. The image appears full-width above the post title and is included in Open Graph meta tags for social previews.

---

## Drafts

Set `draft = true` in any file's front matter to exclude it from the live site. Drafts are visible during local preview by default.
