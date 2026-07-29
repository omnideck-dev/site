+++
title    = "Omnideck weekly update: July 20-26, 2026"
date     = 2026-07-27
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "15 PRs merged across four repos this week. The desktop app has an alpha, container setup got a lot more forgiving, and CLI releases are locked down."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

15 PRs this week across omnideck, cli, site, and homebrew-tap. Fewer PRs than the last two weeks, but the work behind them was heavier: most of it went into making Omnideck easier to actually get running, on Windows, macOS, and now as a standalone desktop app.

---

## The desktop app has an alpha

![Desktop Alpha App](/images/update/26-07-26-desktop-alpha.png)

We shipped an early alpha of the Omnideck desktop app (#224). It installs its own dependencies and runs as a self-contained app instead of something you set up by hand. Right now it's limited to a single deck install. That's on purpose. This alpha exists to work out the install and recovery process before we open it up to multiple decks, not to be feature-complete on day one.

Alongside it, the Electron runtime image is now pinned by digest instead of a floating tag (#223), so the desktop app builds on something that can't shift under you between releases.

Please note that this is VERY experimental, probably will break, and we will almost certainly refactor/rebuild it. BUT - its very cool and we are looking for good feedback. 

---

### Silliness

And sorry folks - the little "Agent Dash" game in the setup screen is not sticking around. Sometimes Larry likes to do silly things... like use the powerful new Apps feature to make a tamagotchi environment. If you'd like to try that out, ask him on [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379).

---

## Container setup is a lot more forgiving

If you've tried to get Omnideck running in a container and hit a wall, this week's work was aimed at you. Windows runtime setup no longer gets stuck retrying against a stale selection (#20). The same class of retry bug got fixed on macOS (#23). Stale Podman credential settings are handled properly now instead of failing silently (#25), and a failed container engine gives you a real error to act on instead of a dead end (#24). The setup guidance itself is clearer too (#21).

None of this is new features. It's the difference between Omnideck working the first time you try it and giving up on the second retry.

---

## Removing an instance is even cleaner now

Earlier, when removing a deck instance, there were cases where some things might need a manual removal. Instance management got a proper safe-removal workflow (#22), so tearing down a deck instance no longer risks leaving orphaned state behind.

---

## Release and repo security got hardened

The CLI release process and repository went through a security hardening pass (#17), and Omnideck v0.1.0-alpha.3 shipped with bounded logs (#221). Container log growth is capped now too (#26). A long-running instance won't quietly fill a disk anymore.

---

## Smaller fixes

Chat scrolling has more reliable controls, and dev sync was hardened along with it (#222). On the distribution side, the Homebrew formula moved up to Omnideck 0.9.0 (#5), and formula verification runs faster (#6). The site also picked up last week's update post (#65).

---

Come tell us how the desktop alpha installs on your machine in [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379). That feedback is exactly what this alpha is for.