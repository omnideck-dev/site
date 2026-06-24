# STYLE.md — Ivy + Lattice Reference

This file is the canonical style reference for the Omnideck site. Before writing any custom CSS, check here. Most layout and styling needs are already covered by Ivy and Lattice.

**CSS load order:**

```html
<link rel="stylesheet" href="/css/ivy.css" />
<link rel="stylesheet" href="/css/ivy.extra.css" />
<link rel="stylesheet" href="/css/lattice.full.min.css" />
<link rel="stylesheet" href="/css/site.css" />
```

---

## Table of Contents

1. [Ivy — Design Tokens](#1-ivy--design-tokens)
2. [Ivy — Core (Classless Baseline)](#2-ivy--core-classless-baseline)
3. [Ivy Extra — Buttons](#3-ivy-extra--buttons)
4. [Ivy Extra — Cards & Callouts](#4-ivy-extra--cards--callouts)
5. [Ivy Extra — Interactive Patterns](#5-ivy-extra--interactive-patterns)
6. [Ivy Extra — Tables](#6-ivy-extra--tables)
7. [Ivy Extra — Forms](#7-ivy-extra--forms)
8. [Ivy Extra — Badges & Status](#8-ivy-extra--badges--status)
9. [Lattice — Page Shell](#9-lattice--page-shell)
10. [Lattice — Component Grids](#10-lattice--component-grids)
11. [Lattice — Unequal Spans](#11-lattice--unequal-spans)
12. [Lattice — Spacing Scale](#12-lattice--spacing-scale)
13. [Lattice — Display & Flexbox](#13-lattice--display--flexbox)
14. [Lattice — Grid Flow & Placement](#14-lattice--grid-flow--placement)
15. [Lattice — Positioning & Overflow](#15-lattice--positioning--overflow)
16. [Lattice — Accessibility Utilities](#16-lattice--accessibility-utilities)
17. [Lattice — Breakpoints](#17-lattice--breakpoints)
18. [Token Overrides in site.css](#18-token-overrides-in-sitecss)
19. [Common Page Recipes](#19-common-page-recipes)

---

## 1. Ivy — Design Tokens

Ivy uses a two-tier token system. Each color has a `-light` and `-dark` variant. The applied token (e.g. `--color-bg`) is set automatically based on the active theme.

**Always override the `-light` / `-dark` variants, never the applied token directly.**

### Color tokens

```css
/* Background & text */
--color-bg-light / --color-bg-dark
--color-text-light / --color-text-dark
--color-muted-light / --color-muted-dark

/* Links */
--color-link-light / --color-link-dark

/* Primary action color */
--color-primary-light / --color-primary-dark
--color-primary-text-light / --color-primary-text-dark

/* Secondary action color */
--color-secondary-light / --color-secondary-dark
--color-secondary-text-light / --color-secondary-text-dark

/* Borders & surfaces */
--color-border-light / --color-border-dark
--color-surface-light / --color-surface-dark
```

### Semantic state colors

```css
--info     /* informational */
--success  /* positive/complete */
--warn     /* caution */
--danger   /* error/destructive */
```

These are used by callouts (`data-tone="info|success|warn|danger"`) and can be referenced in custom CSS.

### Typography tokens

```css
--font-sans   /* sans-serif stack */
--font-mono   /* monospace stack */
--base-size   /* root font size */
--lh          /* line height */
--measure     /* max line length (e.g. 72ch) */
```

### Spacing & shape tokens

```css
--m           /* base unit: 1rem */
--space-xs    /* 0.5rem */
--space-sm    /* 0.75rem */
--space-xl    /* 2rem */
--radius      /* border-radius */
--fs-sm       /* small font size: 0.875rem */
```

### Lattice layout tokens

```css
--lat-container-width   /* max content width (default: 1024px) */
--lat-col-count         /* grid track count minus 1 (default: 11) */
--lat-space             /* component rhythm unit (default: 1rem) */
--lat-gap-x             /* horizontal gap (default: 1rem) */
--lat-gap-y             /* vertical gap (default: 1rem) */
```

---

## 2. Ivy — Core (Classless Baseline)

No classes needed. Ivy styles semantic HTML elements directly.

### Typography

Ivy applies fluid type scale, readable line heights, and vertical rhythm automatically to:

```html
<h1> through <h6>   <!-- fluid heading sizes -->
<p>                 <!-- body text with measure constraint -->
<strong>, <em>      <!-- bold and italic -->
<small>             <!-- de-emphasized text -->
<blockquote>        <!-- indented, styled quote block -->
<cite>              <!-- citation text -->
<mark>              <!-- highlighted text -->
<s>                 <!-- strikethrough -->
<sub>, <sup>        <!-- subscript, superscript -->
<abbr title="...">  <!-- underlined abbreviation with tooltip -->
```

### Code

```html
<code>inline code</code>
<pre><code>
  multi-line
  code block
</code></pre>
<kbd>Ctrl+C</kbd>   <!-- keyboard shortcut display -->
<samp>output</samp> <!-- program output -->
<var>variable</var>
```

### Links

```html
<a href="...">link</a>   <!-- styled with --color-link, hover/focus states included -->
```

### Lists

```html
<ul>
  <li>unordered item</li>
</ul>

<ol>
  <li>ordered item</li>
</ol>

<dl>
  <dt>term</dt>
  <dd>definition</dd>
</dl>
```

### Media

Ivy makes all media responsive by default:

```html
<img src="..." alt="..." />              <!-- max-width: 100%, responsive -->
<figure>
  <img src="..." alt="..." />
  <figcaption>Caption text</figcaption>
</figure>
<video controls src="..."></video>       <!-- responsive -->
<iframe src="..."></iframe>              <!-- responsive -->
<svg>...</svg>                           <!-- responsive -->
```

### Tables

```html
<table>
  <thead>
    <tr><th>Column A</th><th>Column B</th></tr>
  </thead>
  <tbody>
    <tr><td>Value</td><td>Value</td></tr>
  </tbody>
  <tfoot>
    <tr><td colspan="2">Footer</td></tr>
  </tfoot>
</table>
```

Full-width, with cell padding and borders applied automatically.

### Forms (Core)

Core gives minimal, clean defaults — no heavy theming.

```html
<form>
  <p>
    <label>
      Email
      <input type="email" placeholder="you@example.com" />
    </label>
  </p>
  <p>
    <label>
      Message
      <textarea rows="4"></textarea>
    </label>
  </p>
  <p>
    <label>
      <select>
        <option>Option A</option>
        <option>Option B</option>
      </select>
    </label>
  </p>
  <p><button type="submit">Submit</button></p>
</form>
```

### Horizontal rule

```html
<hr />   <!-- styled separator -->
```

### Accessibility helpers (Core)

```html
<span class="sr-only">Screen reader only text</span>
```

Ivy also applies `:focus-visible` outlines, `prefers-reduced-motion` (all transitions disabled), forced-colors safety, and print styles automatically.

---

## 3. Ivy Extra — Buttons

Requires `ivy.extra.css`. Use `data-variant` and `data-size` attributes on `<button>` or `<a role="button">`.

### Variants

```html
<button data-variant="primary">Primary</button>
<button data-variant="secondary">Secondary</button>
<button data-variant="outline">Outline</button>
<button data-variant="ghost">Ghost</button>
<button data-variant="outline-secondary">Outline Secondary</button>
<button data-variant="ghost-secondary">Ghost Secondary</button>
```

### Sizes

```html
<button data-variant="primary" data-size="sm">Small</button>
<button data-variant="primary">Default</button>
<button data-variant="primary" data-size="lg">Large</button>
```

### Link as button

```html
<a role="button" data-variant="primary" href="/get-started">Get Started</a>
<a role="button" data-variant="outline" href="/docs">Read the Docs</a>
```

### Button group

```html
<div class="button-group">
  <button data-variant="outline">Option A</button>
  <button data-variant="outline">Option B</button>
  <button data-variant="outline">Option C</button>
</div>
```

---

## 4. Ivy Extra — Cards & Callouts

### Card

```html
<div class="card">
  <header>
    <h3>Card Title</h3>
  </header>
  <p>Card body content goes here.</p>
  <footer>
    <button data-variant="primary">Action</button>
  </footer>
</div>
```

Card header and footer are optional. Cards work well inside `.grid` containers.

### Callout

```html
<div class="callout" data-tone="info">
  <strong>Note:</strong> Something worth knowing.
</div>

<div class="callout" data-tone="success">
  <strong>Done:</strong> Your changes were saved.
</div>

<div class="callout" data-tone="warn">
  <strong>Warning:</strong> This action cannot be undone.
</div>

<div class="callout" data-tone="danger">
  <strong>Error:</strong> Something went wrong.
</div>
```

Omit `data-tone` for a neutral/default callout.

---

## 5. Ivy Extra — Interactive Patterns

### Details / Summary (accordion)

No JavaScript required.

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content revealed on expand.</p>
</details>
```

### Tooltip

```html
<button data-tooltip="Copied!" aria-label="Copy to clipboard">Copy</button>
<button data-tooltip="Opens in new tab" data-placement="right">Link</button>
```

`data-placement` accepts: `top` (default), `right`, `bottom`, `left`.

### Dialog / Modal

Requires minimal JS to open/close (Ivy styles the element; open/close is native `<dialog>` API).

```html
<button id="open-dialog">Open</button>

<dialog id="my-dialog">
  <article>
    <header>
      <h3>Dialog Title</h3>
    </header>
    <p>Dialog content goes here.</p>
    <footer>
      <button data-variant="primary" id="close-dialog">Close</button>
    </footer>
  </article>
</dialog>

<script>
  document.getElementById('open-dialog').addEventListener('click', () => {
    document.getElementById('my-dialog').showModal();
  });
  document.getElementById('close-dialog').addEventListener('click', () => {
    document.getElementById('my-dialog').close();
  });
</script>
```

### Progress bar

```html
<progress value="60" max="100">60%</progress>
<progress><!-- indeterminate spinner --></progress>
```

---

## 6. Ivy Extra — Tables

### Striped rows

```html
<table data-striped>
  <thead><tr><th>Name</th><th>Value</th></tr></thead>
  <tbody>
    <tr><td>Alpha</td><td>1</td></tr>
    <tr><td>Beta</td><td>2</td></tr>
  </tbody>
</table>
```

### Responsive stacking (mobile)

On narrow viewports, each row collapses to a labeled list. Requires `data-label` on each `<td>`.

```html
<table data-stack>
  <thead><tr><th>Name</th><th>Role</th><th>Status</th></tr></thead>
  <tbody>
    <tr>
      <td data-label="Name">Alice</td>
      <td data-label="Role">Engineer</td>
      <td data-label="Status">Active</td>
    </tr>
  </tbody>
</table>
```

Combine both: `<table data-striped data-stack>`.

---

## 7. Ivy Extra — Forms

Extra adds accent-color, polished focus states, and opt-in components.

### Switch (toggle)

```html
<label>
  <input type="checkbox" role="switch" />
  Enable feature
</label>
```

### Range input

```html
<label>
  Volume
  <input type="range" min="0" max="100" value="50" />
</label>
```

### File input

```html
<label>
  Upload file
  <input type="file" />
</label>
```

---

## 8. Ivy Extra — Badges & Status

### Badge (notification count)

```html
<span aria-label="Notifications" data-badge="4">Notifications</span>
<span aria-label="Messages" data-badge="12">Messages</span>
```

### Busy / loading spinner

```html
<div aria-busy="true" style="min-height: 3rem;"></div>
```

Use `aria-busy="true"` on any container to show a loading state. Remove the attribute when loading is complete.

---

## 9. Lattice — Page Shell

Lattice uses a single `.lattice` class on `<body>` to establish the page shell. Direct children of `.lattice` are either contained or full-bleed.

```html
<body class="lattice">
  <header class="full-width">
    <!-- full-bleed: stretches edge to edge -->
  </header>

  <main class="container">
    <!-- contained: centered at --lat-container-width with fluid gutters -->
  </main>

  <footer class="full-width">
    <!-- full-bleed footer -->
  </footer>
</body>
```

**Rules:**
- `.lattice` goes on `<body>` once per page.
- Direct children are either `.container` (default, contained) or `.full-width` (full-bleed).
- Gutters include `env(safe-area-inset-*)` for notched devices automatically.

---

## 10. Lattice — Component Grids

Use `.grid` inside `.container` sections for component-level layouts.

### Equal columns

Set the column count on the **container**. Items fill columns automatically.

```html
<!-- 2 equal columns at md+, stacked on mobile -->
<div class="grid md-col-2 gap-3">
  <div>Column A</div>
  <div>Column B</div>
</div>

<!-- 3 equal columns at md+, stacked on mobile -->
<div class="grid md-col-3 gap-3">
  <article>Card A</article>
  <article>Card B</article>
  <article>Card C</article>
</div>

<!-- 4 equal columns at lg+, 2 columns at md, stacked on mobile -->
<div class="grid md-col-2 lg-col-4 gap-3">
  <div>A</div><div>B</div><div>C</div><div>D</div>
</div>
```

Valid column counts: `1, 2, 3, 4, 6, 12`.

Breakpoint prefixes: `sm-col-*`, `md-col-*`, `lg-col-*`, `xl-col-*`, `xxl-col-*`.

### Auto-flow grid (no explicit count)

```html
<!-- Defaults to 12 equal tracks — items flow into them -->
<div class="grid gap-3">
  <div class="md-span-6">Half</div>
  <div class="md-span-6">Half</div>
</div>
```

---

## 11. Lattice — Unequal Spans

Set `.span-*` on **items** inside `.grid` for non-uniform column widths. Span values are out of 12.

Requires `lattice.extra.css` or `lattice.full.css`.

```html
<!-- 1/3 + 2/3 -->
<div class="grid gap-3">
  <aside class="md-span-4">Sidebar</aside>
  <section class="md-span-8">Main content</section>
</div>

<!-- 1/4 + 3/4 -->
<div class="grid gap-3">
  <aside class="md-span-3">Narrow sidebar</aside>
  <section class="md-span-9">Wide content</section>
</div>

<!-- 2/3 + 1/3 -->
<div class="grid gap-3">
  <section class="md-span-8">Primary</section>
  <aside class="md-span-4">Secondary</aside>
</div>

<!-- Offset: centered column -->
<div class="grid gap-3">
  <div class="md-span-6" style="grid-column-start: 4;">Centered 6-wide</div>
</div>
```

All span classes support responsive prefixes:
`span-*`, `sm-span-*`, `md-span-*`, `lg-span-*`, `xl-span-*`, `xxl-span-*`

---

## 12. Lattice — Spacing Scale

Applies padding and margin using a 0–5 scale based on `--lat-space` (1rem).

### Padding

```html
<div class="p-0">   <!-- 0 -->
<div class="p-1">   <!-- 0.25rem -->
<div class="p-2">   <!-- 0.5rem -->
<div class="p-3">   <!-- 1rem -->
<div class="p-4">   <!-- 1.5rem -->
<div class="p-5">   <!-- 2rem -->
```

**Directional padding:**

```html
<div class="pt-3">  <!-- padding-top -->
<div class="pb-3">  <!-- padding-bottom -->
<div class="pl-3">  <!-- padding-left -->
<div class="pr-3">  <!-- padding-right -->
<div class="px-3">  <!-- padding-left + padding-right -->
<div class="py-3">  <!-- padding-top + padding-bottom -->
```

### Margin

Same scale and directional pattern:

```html
<div class="m-3">
<div class="mt-3">
<div class="mb-3">
<div class="ml-3">
<div class="mr-3">
<div class="mx-3">   <!-- horizontal: auto-centering works here -->
<div class="my-3">   <!-- vertical -->
<div class="mx-auto"> <!-- center block element -->
```

### Gap (for grids and flex)

```html
<div class="grid md-col-3 gap-0">  <!-- no gap -->
<div class="grid md-col-3 gap-1">
<div class="grid md-col-3 gap-2">
<div class="grid md-col-3 gap-3">  <!-- 1rem — most common -->
<div class="grid md-col-3 gap-4">
<div class="grid md-col-3 gap-5">
```

All spacing classes support responsive prefixes:
`md-p-3`, `lg-px-4`, `xl-my-5`, etc.

---

## 13. Lattice — Display & Flexbox

### Display

```html
<div class="d-none">           <!-- display: none -->
<div class="d-block">          <!-- display: block -->
<div class="d-inline">         <!-- display: inline -->
<div class="d-inline-block">   <!-- display: inline-block -->
<div class="d-flex">           <!-- display: flex -->
<div class="d-grid">           <!-- display: grid -->
```

Responsive display (show/hide at breakpoints):

```html
<div class="d-none md-d-block">   <!-- hidden on mobile, block at md+ -->
<div class="d-block lg-d-none">   <!-- visible until lg, then hidden -->
<div class="d-none lg-d-flex">    <!-- flex only at lg+ -->
```

### Flexbox

```html
<!-- Direction -->
<div class="d-flex flex-row">     <!-- row (default) -->
<div class="d-flex flex-col">     <!-- column -->

<!-- Justify content -->
<div class="d-flex justify-start">
<div class="d-flex justify-center">
<div class="d-flex justify-end">
<div class="d-flex justify-between">
<div class="d-flex justify-around">
<div class="d-flex justify-evenly">

<!-- Align items -->
<div class="d-flex items-start">
<div class="d-flex items-center">
<div class="d-flex items-end">
<div class="d-flex items-stretch">
<div class="d-flex items-baseline">

<!-- Wrap -->
<div class="d-flex flex-wrap">
<div class="d-flex flex-nowrap">

<!-- Common combos -->
<div class="d-flex items-center justify-between gap-3">
<div class="d-flex items-center gap-2">
<nav class="d-flex items-center gap-3 flex-wrap">
```

### Order

```html
<div class="order-1">
<div class="order-2">
<div class="order-3">
```

---

## 14. Lattice — Grid Flow & Placement

```html
<!-- Grid auto-flow direction -->
<div class="grid flow-row">      <!-- fill rows (default) -->
<div class="grid flow-col">      <!-- fill columns -->
<div class="grid flow-dense">    <!-- fill gaps aggressively -->

<!-- Place all items -->
<div class="grid place-items-center">
<div class="grid place-items-start">
<div class="grid place-items-end">
<div class="grid place-items-stretch">

<!-- Place content (whole grid track) -->
<div class="grid place-content-center">
<div class="grid place-content-start">
<div class="grid place-content-end">
<div class="grid place-content-between">

<!-- Place a single item (on the item, not container) -->
<div class="place-self-center">
<div class="place-self-start">
<div class="place-self-end">
<div class="place-self-stretch">
```

---

## 15. Lattice — Positioning & Overflow

### Position

```html
<div class="relative">    <!-- position: relative -->
<div class="absolute">    <!-- position: absolute -->
<div class="fixed">       <!-- position: fixed -->
<div class="sticky">      <!-- position: sticky -->
<div class="static">      <!-- position: static -->
```

### Inset

```html
<div class="inset-0">    <!-- top/right/bottom/left: 0 -->
```

### Z-index

```html
<div class="z-10">
<div class="z-20">
<div class="z-30">
```

### Overflow

```html
<div class="overflow-auto">
<div class="overflow-hidden">
<div class="overflow-scroll">
<div class="overflow-visible">
```

### Aspect ratio

```html
<div class="aspect-video">    <!-- 16/9 -->
<div class="aspect-square">   <!-- 1/1 -->
```

---

## 16. Lattice — Accessibility Utilities

```html
<!-- Visually hidden but announced by screen readers -->
<span class="sr-only">Skip to main content</span>
<span class="visually-hidden">Page 2 of 5</span>

<!-- Visually hidden until focused (skip links) -->
<a class="sr-only-focusable" href="#main">Skip to content</a>
```

---

## 17. Lattice — Breakpoints

All layout, spacing, display, and flex classes support responsive prefixes using min-width logic (mobile-first).

| Prefix | Min-width | ~Device |
|---|---|---|
| (none) | 0 | All / mobile |
| `sm-` | 40rem (640px) | Large phone / small tablet |
| `md-` | 48rem (768px) | Tablet |
| `lg-` | 64rem (1024px) | Desktop |
| `xl-` | 80rem (1280px) | Large desktop |
| `xxl-` | 96rem (1536px) | Wide screen |

Pattern: `{breakpoint}-{class}`

```html
<!-- Stack on mobile, 3 cols at md, 4 cols at lg -->
<div class="grid md-col-3 lg-col-4 gap-3">

<!-- Hidden on mobile, flex row at lg -->
<nav class="d-none lg-d-flex items-center gap-3">

<!-- Full padding at lg, less on mobile -->
<section class="py-3 lg-py-5">

<!-- Span changes at breakpoints -->
<aside class="span-12 md-span-4 lg-span-3">
```

---

## 18. Token Overrides in site.css

`site.css` is the only place custom CSS lives. Use it to set project tokens and handle gaps the stack genuinely cannot cover.

### Correct pattern

```css
/* site.css */

:root {
  /* Primary color — Omnideck indigo/violet palette */
  --color-primary-light: #6366f1;
  --color-primary-dark:  #818cf8;
  --color-primary-text-light: #ffffff;
  --color-primary-text-dark:  #0f172a;

  /* Secondary */
  --color-secondary-light: #7c3aed;
  --color-secondary-dark:  #a78bfa;
  --color-secondary-text-light: #ffffff;
  --color-secondary-text-dark:  #0f172a;

  /* Typography */
  --font-sans: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", monospace;
  --measure: 68ch;

  /* Layout */
  --lat-container-width: 1100px;
  --radius: 0.5rem;
}
```

### What belongs in site.css

- Token overrides (colors, fonts, container width, radius)
- Styles for custom components that Ivy/Lattice have no equivalent for
- Section-specific layout that can't be expressed with utility classes alone

### What does NOT belong in site.css

- Custom flexbox or grid rules when a Lattice class exists
- Element styling that Ivy already handles (heading sizes, link colors, code blocks)
- Spacing rules when a Lattice spacing class works
- Vendor prefixes that Ivy/Lattice already include

---

## 19. Common Page Recipes

### Full-bleed hero, contained body

```html
<body class="lattice">
  <header class="full-width">
    <div class="container py-5">
      <h1>Omnideck</h1>
      <p>Open-source AI agent infrastructure.</p>
      <a role="button" data-variant="primary" href="/docs">Get Started</a>
      <a role="button" data-variant="outline" href="https://github.com/..." >View on GitHub</a>
    </div>
  </header>

  <main class="container py-4">
    <!-- page content -->
  </main>

  <footer class="full-width py-4">
    <div class="container">
      <!-- footer content -->
    </div>
  </footer>
</body>
```

### Feature grid (3-up cards)

```html
<section class="py-5">
  <h2>Why Omnideck</h2>
  <div class="grid md-col-3 gap-3 mt-3">
    {% for f in Data.features.items %}
    <div class="card">
      <header><h3>{{ f.title }}</h3></header>
      <p>{{ f.desc }}</p>
    </div>
    {% endfor %}
  </div>
</section>
```

### Docs layout (sidebar + content)

```html
<div class="grid gap-4 mt-4">
  <aside class="md-span-3">
    {% include "templates/partials/sidebar.html" %}
  </aside>
  <article class="md-span-9">
    <h1>{{ Page.Title }}</h1>
    {{ Page.HTMLContent|safe }}
  </article>
</div>
```

### Blog post list with teasers

```html
<div class="grid gap-3">
  {% for item in Items %}
  <article>
    <h2><a href="{{ item.URL }}">{{ item.Title }}</a></h2>
    <time>{{ item.Date|godate:"January 2, 2006" }}</time>
    <p>{{ item.Meta.Fields.description }}</p>
  </article>
  {% endfor %}
</div>

{% if Pager %}
<nav class="d-flex justify-between mt-4" aria-label="Pagination">
  {% if Pager.HasPrev %}<a href="{{ Pager.PrevURL }}">← Newer</a>{% endif %}
  {% if Pager.HasNext %}<a href="{{ Pager.NextURL }}">Older →</a>{% endif %}
</nav>
{% endif %}
```

### Sticky site header

```html
<header class="full-width sticky" style="top: 0; z-index: 100;">
  <div class="container d-flex items-center justify-between py-2">
    <a href="/" class="site-logo">Omnideck</a>
    <nav class="d-none md-d-flex items-center gap-3">
      {% for item in Data.nav.items %}
      <a href="{{ item.url }}">{{ item.label }}</a>
      {% endfor %}
    </nav>
  </div>
</header>
```

### Two-column CTA section

```html
<section class="full-width py-5">
  <div class="container d-flex flex-col md-d-flex items-center justify-between gap-4">
    <div>
      <h2>Ready to build?</h2>
      <p>Run your first agent in minutes.</p>
    </div>
    <div class="d-flex gap-2">
      <a role="button" data-variant="primary" href="/docs/getting-started">Get Started</a>
      <a role="button" data-variant="outline" href="https://github.com/...">GitHub</a>
    </div>
  </div>
</section>
```

### Info callout in docs content

```html
<div class="callout" data-tone="info">
  <strong>Note:</strong> This feature requires Omnideck 0.4 or later.
</div>
```

### Show/hide on mobile

```html
<!-- Mobile nav toggle button: visible only on mobile -->
<button class="d-flex md-d-none" aria-label="Open menu">Menu</button>

<!-- Desktop nav: hidden on mobile, flex at md+ -->
<nav class="d-none md-d-flex items-center gap-3">...</nav>
```
