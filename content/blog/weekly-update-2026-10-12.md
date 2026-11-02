+++
title    = "omnideck weekly update: October 5-11, 2026"
date     = 2026-10-12
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "11 changes across three repos. Browser tools handle hostile pages and keyboard paste, the site got a new brand icon set and a real theme switcher, and the install guides caught up with the releases."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

Eleven changes across omnideck, cli, and site. Most of the site work is the kind of thing you only notice when it is wrong: icons, theme switching, install steps that had drifted from what actually ships.

---

## Browser tools handle more of the awkward cases

Two fixes, both about pages that fight back. Browser tools can now read and interact with pages that disable JavaScript eval, which is a common hardening move on sites that do not want automation. Keyboard paste works with Ctrl/Cmd+V as well, so pasting into a field no longer needs a workaround.

Snapshots also preserve sticky controls and editable text now, and hidden dialogs or consent bars no longer make a page look unavailable when it is fine underneath. If you have seen a snapshot come back mostly empty on a site with a cookie banner, that was this.

Worth saying plainly: browser automation is where we get the most bug reports and where the gap between "works in testing" and "works on the real web" is widest. Two fixes a week is the honest rate.

---

## The site got a new look and a better theme switcher

App and desktop icons are refreshed to the new omnideck mark, and the site now uses the same brand icon set with a CSS restyle to match the product interface.

Theme switching moved to the dark-mode-toggle web component. It remembers your choice, applies it before the page paints so there is no white flash on load, and follows your system setting by default. The old switcher was homegrown and it showed.

---

## Install guides caught up with the releases

The desktop installation guide was rewritten for desktop beta.14 and CLI beta.8. Windows install instructions now match the route we actually tested on video rather than the route that used to work. WSL initialization timeout recovery and the macOS approval prompts are both spelled out, since those are the two places people get stuck and conclude the install is broken. Setup and recovery steps match the released versions again, and integration setup reflects the per-tool access model from the week before.

---

## CLI and smaller fixes

Windows users now get a clear explanation when WSL container limits prevent startup, instead of a failure that looks like a bug in omnideck. The CLI reference had a callout spacing problem, which is the least exciting sentence in this post.

---

If you install on Windows or macOS and something in the guide does not match what you see, that is worth reporting. The guides are only as good as the last person who followed them on a clean machine. [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379) is the place.
