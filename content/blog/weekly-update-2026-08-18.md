+++
title    = "Omnideck weekly update: August 9-15, 2026"
date     = 2026-08-16
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "44 PRs merged across three repos this week. The desktop app climbed from alpha.9 to beta.8, the VM testing lab grew into real infrastructure, and agent runs can now pick up where they left off."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

44 PRs this week, another record, across omnideck, cli, and site. The desktop app did most of the moving. It went from alpha.9 to beta.8 in seven days, because the release process and the testing behind it have both become so solid. 

---

## The desktop app climbs from alpha to beta

Desktop setup got another round of improvements ahead of alpha.9, followed by a Tauri host refactor for alpha.10 and then alpha.11 itself. The original Electron app was always considered a POC, with Tauri as a goal for performance and size. This formed the new baseline, and we instantly aimed for a full multi-platform target.

From there the pace picked up: macOS signing got fixed on the way to beta.1, native downloads were fixed for beta.4, and native parity issues were resolved for beta.5. Beta release qualification got hardened, the AppImage setup environment was fixed for beta.6, and beta.7 shipped with a guided macOS installer. Beta.8 landed with native desktop zoom.

Nine releases in one week... thats alot. But, its also part of the process of creating and testing multiple build targets across every major OS.

---

## Bug fixes and hardening along the way

A release cadence like that is the result of finding and fixing real bugs. The macOS runtime memory contract was corrected, and desktop runtime conflicts were repaired. Windows desktop release automation got hardened, and the release policy now accepts Windows line endings rather than tripping on them. Transient native packaging failures retry automatically now instead of failing outright, and dropdown styling is standardized across WebViews. The Tauri host modules also got split apart, which should make the next round of desktop work easier to reason about.

---

## The VM lab grew into real infrastructure

The only way to scale this up with with a more robust testing setup that can actually catch problems before users do, and that's where a big chunk of this week went. Desktop VM end-to-end coverage is automated, a faster VM golden checkpoint is in use, and published desktop release qualification runs automatically now. VM testing got expanded and hardened generally, and Custom Apps are now tested inside packaged desktop VMs. Desktop VM end-to-end testing is centralized, there's a dedicated macOS ARM64 lab lane, and macOS VM parity got expanded further. Hermetic routine execution has its own end-to-end test, and the macOS Downloads consent flow is covered too.

That's eleven separate pieces of testing infrastructure in a single week, most of it invisible unless something breaks. We also put this in a public repo, and have backlog items to make it more generic so other people can use it too. Part of building world class open source software is sharing the tools we need to develop. Stay tuned for more on this later!

---

## CLI keeps in step

The CLI serves as the management engine for the desktop app, so improvements there are often tied into the CLI too. Native runtime setup reporting is clearer, and there's now disposable VM end-to-end coverage for the CLI itself. Competing Podman machines on macOS no longer conflict, and CLI setup and diagnostics got refactored for clarity. The TUI picked up the Omnideck dark theme, and a standalone VM lab controller is in place. CLI VM end-to-end tests are deterministic and cacheable now, removal confirmation input is visible where it used to be hidden, and macOS CLI dashboard polling is stable. The self-hosted hardware workflow was removed, dashboard polling no longer flashes the terminal title, and there's a macOS ARM64 lab lane for the CLI too.

All of these investments are aimed at helping us continue to evolve and accelerate while also reducing the risk of regressions and excess technical debt. We are building this for the long term.

---

## Agent runs can pick up where they left off

Active agent runs are resumable now. If a run gets interrupted, it doesn't have to start over. We are still tracking and working on a list of these quality of life improvements, and will continue to roll them out even as we invest in other areas.

---

## Code quality and site

The tested runtime is pinned, and native IPC headers are preserved through that process. Agent lint and type checks run faster now. On the site, last week's update went up. Still working on updating the site look/feel and making the messaging clearer for users. More on that next weel.

---

If you're on the desktop beta, this is the week the release process caught up to the app. [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379) is still the place to tell us what's still rough.