+++
title    = "omnideck weekly update: October 26 - November 1, 2026"
date     = 2026-11-02
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "4 changes across two repos. Background work keeps running when you switch chats, and start or restart no longer claims success before the app is actually ready."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

Four changes across omnideck and cli this week. They share a theme: things that said they were done when they were not.

---

## Background work keeps running when you switch chats

Previously, starting a new conversation or jumping to another one could interrupt work already going. Now conversations keep running in the background. The sidebar shows which ones are active and marks finished background work as done until you open it and look.

Reloading a workspace with an unsent chat behaves now too. It restores the empty chat directly instead of loading a conversation that was never saved, and it no longer throws an error over the tabs and settings.

This one changes how you use the product more than the changelog line suggests. Start something long, go do something else, come back to a result instead of a restart.

---

## Start and restart tell the truth

`omnideck start` and `omnideck restart` used to report success and leave you waiting for an app that was not up yet. They now wait for the app to respond before saying anything. There is also a new `omnideck wait` command that checks readiness without changing an installation, which is what you want in a script or a health check.

The desktop app shares those readiness checks with the bundled CLI, and its recovery screen has a Copy diagnostics button, so a support conversation can start with real information instead of a description of a blank window.

---

If you script against the CLI, `omnideck wait` is worth a look. If you have been bitten by a restart that reported success too early, that one is fixed. [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379) if anything still misbehaves.
