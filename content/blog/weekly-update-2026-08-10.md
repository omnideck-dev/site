+++
title    = "omnideck weekly update: August 2-9, 2026"
date     = 2026-08-10
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "33 PRs merged across four repos this week. The desktop app left Electron behind for Tauri, CLI and runtime setup converged on a single Podman path, and release engineering got real teeth."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

33 PRs this week, the biggest week yet, spread across omnideck, desktop, cli, and roadmap. Most of it traces back to one decision: moving the desktop app off Electron and onto Tauri. That single change touched setup, CI, release process, and testing.

---

## The desktop app leaves Electron for Tauri (beta)

![Desktop beta App](/images/update/26-08-10-desktop-beta.png)

The desktop host is now built on Tauri instead of Electron. It's a rewrite of the foundation the whole desktop app sits on. The weeks since have gone into making that foundation solid: a refactor of the Tauri host ahead of alpha.10, desktop setup improvements for alpha.9, and an alpha.6 release before that.

The desktop app now uses the shared CLI for its own runtime management instead of duplicating that logic. That means you can use the desktop app, the CLI, or both... it doesn't matter. Your decks are visible and reporting accurately regardless of how you choose to manage them!s

Desktop releases are also decoupled from container releases, so one doesn't have to wait on the other. The product name is lowercase "omnideck" everywhere now too.

On the desktop repo itself, initial setup work landed, along with GitHub Actions CI using tag-triggered, review-gated releases. CI was split into a reusable test workflow, and the README got restructured. A version bump to 0.5.0-alpha.2 came with a tighter release version check, plus a release-artifact contract check and a ported hardware smoke script.

A few things broke along the way, which is normal for a migration this size. A blank screen issue on AppImage builds needed two separate fixes before it held.

---

## CLI and runtime setup converge on one path

Setup used to have more than one way to get a runtime working. Now it doesn't. Setup is unified on the shared Podman runtime, and the plumbing behind Podman-only setup got simplified. Native runtime setup reporting is clearer, and there's now disposable VM end-to-end coverage for the CLI. omnideck now stays up to date and visible from the command line tool itself, and CLI 0.1.0 shipped.

One more fix worth calling out: container removal that gets interrupted, and the name conflicts that used to follow, now recover cleanly.

---

## Release engineering got real teeth

Testing and release process stopped being an afterthought. Automated desktop VM end-to-end coverage landed, alongside a proper desktop testing and release structure. Setup UX principles moved next to the tests they govern.

On the CLI side, release contract gates went in, and the testing policy is now authoritative rather than advisory. The first-run test lines up with automatic setup, and cross-platform stable upgrade tests are documented. Evidence-backed direct stable promotion is now allowed, with reproducible release environments across supported platforms.

---

## UI and docs

System settings are grouped now. Model pickers stay visible instead of getting buried in a menu. On the documentation side, a capabilities doc and an RFC/meta writeup for the pack system upgrade are in, and the roadmap repo picked up a new script.

---

If you're running the desktop alpha, the Tauri move is the thing to watch for. Report anything that feels different in [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379).
