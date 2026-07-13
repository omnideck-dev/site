+++
title    = "Omnideck weekly update: July 6-12, 2026"
date     = 2026-07-13
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "25 PRs merged across four repos this week. Conversation folders and archiving, portable agent profile packs, multi-file chat attachments, and a more resilient browsing agent."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

This was a big week. 25 PRs merged across four repos: omnideck, cli, site, and homebrew-tap. Three repos (omnideck, site, cli) all shipped user-facing improvements this week, and a fourth (homebrew-tap) kept distribution current. Conversation management and chat UX got the most attention, browser tools got more resilient rather than more feature-rich, and the housekeeping work (refactors, docs, license) happened alongside the features instead of piling up as debt. 

For a detailed list, checkout the [`#project-updates` channel on Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379).

We are currently looking at some more educational content and a focus on a backlog of smaller improvements and refeinements. There are a few UX changes coming, and we are discussing the new "custom apps" feature. Join us on Slack to tell us what you think.

## Browser tools got smarter and more resilient

The browsing agent picked up three real upgrades. `read_page` now returns the whole page instead of forcing you to guess at chunking, with navigation by chunk and query layered on top (#148). The DOM walk in `browse_page` stopped pruning subtrees just because they're off-viewport (#149), so the agent can see content that isn't currently on screen. We also added a `curl_cffi` fetch fallback for sites that throw up anti-bot interstitials (#132). The agent doesn't just stall out when a site gets defensive.

## Agent profiles are portable now

You can export and import agent profiles and skills as packs (#137). This is the foundation for sharing agent configs between people or environments instead of rebuilding them by hand every time. A follow-up fix made sure that when a pack is exported with skills off, the imported agent has no skills (#150). No silent leakage of capability you didn't intend to share.

## Chat got real multi-file support

Multiple file attachments in chat are in (#139), along with a unified chip UI for those attachments and a cleaner composer experience overall (#145). We also turned the preview source view into a proper editable, saveable code editor (#138), so you're not stuck looking at read-only output when you want to tweak something quickly.

## Chat history finally has structure

This was the week conversation management grew up. Archiving landed (#161), then folder organization (#164), then a round of polish on top: header cleanup, unpin-on-move behavior, archived counts, and flat search across folders (#168). We also split the ConversationsPanel into focused modules as part of that polish pass (#169), which should make this area easier to extend going forward.

## Steady UI cleanup

A few smaller refactors kept the codebase honest: `formatAgentName` moved into `utils/agentUtils.js` (#160), a new `formatTokens` utility landed with test coverage (#162), and token size formatting now drops the decimal places (#163). Not flashy, but this is the kind of housekeeping that keeps the bigger features easy to build on.

## CLI dashboard upgrade

The CLI got a TUI dashboard upgrade, better logging, and some config changes (#11). More visibility into what's happening under the hood without leaving the terminal.

## Site work picked up too

The Omnideck site now supports blog hero images (#47) and tags (#48). Larry's first blog post went up (#49), along with fixes to make `og:image` work for social previews (#50, #52, #53) and an update to the origin story post (#51). If you've shared an Omnideck link on X or LinkedIn recently, this is why the preview image finally looks right.

## Docs and distribution

The README and license got updated to Apache 2 (#144), making the open-source terms official. The Homebrew tap moved up to v0.8.0 (#4), so anyone installing via Homebrew gets the latest build.



