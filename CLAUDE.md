# CLAUDE.md — Omnideck Static Site

This file defines the conventions, tooling, and constraints for building the Omnideck project site. It is hosted on GitHub Pages and built with Arbor, a convention-driven static site generator.

---

## Project Overview

**Omnideck** is an open-source infrastructure substrate for AI agents. The site is its public-facing home: documentation, landing page, and community entry point.

- **Output target:** GitHub Pages (`public/` → `gh-pages` branch)
- **Generator:** Arbor (binary available at `./arbor` in repo root)
- **CSS stack:** Ivy (classless baseline) + Lattice (layout utilities) + minimal custom CSS
- **Goal:** Fast, lean, semantic HTML. No frameworks. No build complexity beyond Arbor itself.

---

## Tooling

### Arbor

The `arbor` binary is committed to the repo root. Use it for all site operations.

```bash
./arbor build          # production build → public/
./arbor preview        # dev server with live reload at localhost:8080
./arbor build --force  # full rebuild, ignore cache
./arbor check          # validate config, templates, content without building
./arbor new blog <slug> # create a new blog post stub
```

Arbor uses Pongo2 (Jinja2/Django-compatible) for templates. All template logic lives in `templates/`.

### CSS Stack

**Do not introduce npm, PostCSS, Sass, or a separate build step for CSS.** All styles are plain CSS files in `static/css/`.

Load order in the base layout:

```html
<link rel="stylesheet" href="/css/ivy.css" />
<link rel="stylesheet" href="/css/ivy.extra.css" />
<link rel="stylesheet" href="/css/lattice.min.css" />
<link rel="stylesheet" href="/css/site.css" />
```

- `ivy.css` — classless baseline (typography, links, code, tables, forms)
- `ivy.extra.css` — opt-in patterns (buttons, cards, callouts, tooltips, dialogs)
- `lattice.min.css` — layout utilities (grid, flex, positioning, spacing)
- `site.css` — project-specific overrides and custom tokens only

**Minimize `site.css`.** Before writing custom CSS, check whether Ivy tokens, Ivy extra patterns, or Lattice utilities already cover the need. Custom CSS should handle only what the stack genuinely cannot.

---

## CSS Conventions

### Token overrides

Override Ivy tokens in `site.css` using the `-light` / `-dark` variant pattern. Never override the applied tokens (`--color-bg`, `--color-primary`, etc.) directly in `:root`.

```css
:root {
  --color-primary-light: #6366f1;   /* indigo */
  --color-primary-dark:  #818cf8;
  --color-primary-text-light: #ffffff;
  --color-primary-text-dark:  #0f172a;
  --font-sans: "Inter", system-ui, sans-serif;
  --lat-container-width: 1100px;
}
```

### Ivy button/card patterns

Use Ivy's data-attribute API for interactive elements. Prefer these over custom classes:

```html
<button data-variant="primary">Get Started</button>
<button data-variant="outline" data-size="sm">Learn More</button>
<div class="card"> … </div>
<div class="callout" data-tone="info"> … </div>
```

### Lattice layout

Use Lattice utility classes for all layout work. Do not write custom flexbox or grid rules unless Lattice has no equivalent.

Common patterns:

```html
<div class="container">          <!-- centered max-width wrapper -->
<div class="grid cols-3">        <!-- 3-column grid -->
<div class="flex gap-md">        <!-- flex row with gap -->
<div class="stack gap-lg">       <!-- vertical stack -->
<section class="py-xl">          <!-- vertical padding -->
```

---

## HTML Conventions

- Use semantic elements: `<main>`, `<section>`, `<article>`, `<nav>`, `<header>`, `<footer>`, `<aside>`.
- One `<h1>` per page. Heading hierarchy must be correct and sequential.
- No `<div>` where a semantic element exists.
- No inline styles. No style attributes on elements.
- Images must have meaningful `alt` text. Decorative images use `alt=""`.
- Keep markup flat. Avoid deep nesting.

---

## Project Structure

```
.
├── arbor                  # Arbor binary (committed)
├── config.toml            # Site config
├── content/
│   ├── docs/              # Documentation pages (type: docs)
│   ├── blog/              # Blog/changelog posts (type: blog)
│   └── about.md           # Top-level pages (type: page)
├── templates/
│   ├── layouts/
│   │   └── base.html      # Root HTML wrapper — loads CSS, sets meta
│   ├── types/
│   │   ├── page.html      # Generic page template
│   │   ├── docs.html      # Docs page with sidebar
│   │   ├── docs-list.html # Docs index listing
│   │   ├── blog.html      # Blog post template
│   │   └── blog-list.html # Blog listing with pagination
│   ├── displays/
│   │   ├── card.html      # Feature/doc card display
│   │   └── teaser.html    # Blog post teaser
│   └── partials/
│       ├── header.html    # Site nav
│       ├── footer.html    # Footer
│       └── sidebar.html   # Docs sidebar nav
├── data/
│   ├── nav.toml           # Primary navigation links
│   ├── features.toml      # Feature grid content (homepage)
│   └── docs-nav.toml      # Sidebar nav for docs section
├── static/
│   └── css/
│       ├── ivy.css
│       ├── ivy.extra.css
│       ├── lattice.min.css
│       └── site.css       # Custom tokens and overrides only
└── public/                # Build output (git-ignored)
```

---

## Templates

### Base layout

`templates/layouts/base.html` is the root wrapper. It must include:

- `<meta charset>`, `<meta viewport>`, `<meta description>`
- CSS load order (Ivy → Ivy Extra → Lattice → site.css)
- `{% block title %}`, `{% block head %}`, `{% block body %}`
- Header partial and footer partial

### Template variables

Every template has access to:

| Variable | Description |
|---|---|
| `Site.Config` | Values from `config.toml` |
| `Site.Index` | All content items |
| `Page` | Current page (`Page.Title`, `Page.HTMLContent`, `Page.Meta.Fields.*`) |
| `Items` | All items of the current content type |
| `Data` | All `data/*.toml` files by filename |
| `Pager` | Pagination state (listing pages only) |

### Rendering HTML content

Always pipe `HTMLContent` through the `safe` filter:

```html
{{ Page.HTMLContent|safe }}
```

### Date formatting

```html
{{ Page.Date|godate:"January 2, 2006" }}
```

### Custom front matter fields

Defined under `[extra]` in content front matter, accessed as:

```html
{{ Page.Meta.Fields.hero_subtitle }}
```

---

## Content Front Matter

```toml
+++
title    = "Getting Started"
date     = 2025-06-01
draft    = false

[extra]
description = "Install and run Omnideck in under five minutes."
order       = 1   # used for docs sidebar ordering
+++
```

Draft files are excluded from production builds. Set `draft_mode = true` in `config.toml` to include them locally.

---

## config.toml

```toml
[site]
title    = "Omnideck"
base_url = "https://omnideck.dev"
language = "en"
page_size = 10

[build]
draft_mode = false
output_dir = "public"

[author]
name  = "Ron Northcutt"
email = "ron@omnideck.dev"
```

---

## Data Files

Use TOML data files in `data/` for any content that drives template loops (nav links, features, doc sections). This keeps templates logic-free and content editable without touching HTML.

Example: `data/features.toml`

```toml
[[items]]
title = "Isolated by Default"
desc  = "Every agent runs in a Firecracker microVM. Zero shared state."
icon  = "shield"

[[items]]
title = "Durable Workflows"
desc  = "Powered by Restate. Agents survive restarts, retries, and failures."
icon  = "refresh"
```

Template usage:

```html
{% for f in Data.features.items %}
<div class="card">
  <h3>{{ f.title }}</h3>
  <p>{{ f.desc }}</p>
</div>
{% endfor %}
```

---

## Performance Rules

- No JavaScript unless strictly necessary. The dark-mode toggle web component is the only permitted JS by default.
- No web fonts loaded from external CDNs. Use `system-ui` or self-host.
- Images must be appropriately sized. Use `<picture>` with `srcset` for responsive images where needed.
- No tracking scripts, analytics embeds, or third-party resources in the default build.

---

## What Not to Do

- Do not use Tailwind, Bootstrap, or any other CSS framework.
- Do not write custom layout CSS when a Lattice class exists.
- Do not style elements with classes when Ivy already styles the semantic element.
- Do not commit `public/` to the main branch.
- Do not introduce a Node.js build step or `package.json` for CSS/JS.
- Do not use `<div>` wrappers for presentational grouping when a semantic element fits.
- Do not add JavaScript for anything Ivy/CSS handles natively (tooltips, details, switches).
