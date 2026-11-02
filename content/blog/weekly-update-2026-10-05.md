+++
title    = "omnideck weekly update: September 28 - October 4, 2026"
date     = 2026-10-05
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "11 changes across three repos. The desktop app got steadier on Windows and Linux, the site picked up install fingerprints and a new blog post, and CLI now hands browser sign-in the right address."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

Eleven changes across omnideck, cli, and site. Desktop took most of the engineering time. The site took most of the visible changes, though "visible" is doing some work in that sentence.

---

## Desktop got steadier on the platforms that were rough

Linux AppImages were built with outdated packaging tooling, which meant the interface could fail to open on newer Linux systems. That is fixed.

On Windows there were two separate problems. Opening omnideck repeatedly could trigger invalid sign-in attempts from the embedded browser, and host routing plus browser sign-in callbacks were broken until the bundled CLI moved to v0.11.0-beta.6. Both are fixed now.

Upgrades also behave better. If you already have a newer container installed, a desktop upgrade preserves it instead of reverting to an older one. New installs use container 0.5.2.

---

## CLI supplies the right address for sign-in callbacks

Browser sign-in flows need to know the host-local address to call back to. The CLI now supplies it to application builds that can use it. This is the other half of the desktop fix above. Invisible when it works, maddening when it does not.

---

## The site got install fingerprints and a new showcase

The install guide now includes the AI model setup step, which had been easy to miss, and shows download fingerprints so you can verify what you downloaded.

There is a new blog post on visual desktop control experiments, where the agent uses real mouse actions to work through complete desktop workflows instead of a scripted path. And there is a Utah trip showcase with runnable demo apps: a park-pass planner and an expense splitter. Both are small, both are the sort of thing you can copy and change.

Two smaller site fixes: blog articles no longer overflow on mobile screens, and the homepage shows the latest releases in publication order with current download links.

---

## Chat and smaller fixes

Chat message links now use the brand accent color in dark mode, which matters more than it sounds when the default link blue disappears into a dark background.

---

If you run the desktop app on Linux or Windows, this is a good week to upgrade. If you hit something in the install guide that does not match what you see, [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379) is the place.
