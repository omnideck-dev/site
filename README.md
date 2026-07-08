# Omnideck Site — Content Guide

This is the public site for Omnideck. Content is written in Markdown with TOML front matter. No build tools or Node.js required.

## Previewing the site

From the repo root:

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
| `tags` | no | Array of strings |
| `template` | yes | Always `"templates/types/blog.html"` for blog posts |
| `description` | no | Used in meta tags and the blog listing |
| `author` | no | Shown below the title |
| `featured_image` | no | Path relative to `static/` — place images in `static/images/`. Displayed full-width above the post and used for social link previews. |

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

## Images

Place images in `static/images/` and reference them with `/images/filename.jpg`. They will be copied to the build output as-is.

For blog post hero images, use the `featured_image` field in front matter. The image will appear full-width above the post title and will be included in social preview meta tags.

---

## Drafts

Set `draft = true` in any file's front matter to exclude it from the live site. Drafts are visible during local preview by default.
