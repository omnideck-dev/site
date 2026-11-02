+++
title    = "omnideck weekly update: September 14-27, 2026"
date     = 2026-09-28
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "16 changes across two repos. Browser tools got much better at reading real pages, integration access became an explicit per-tool allowlist, and the interface got a refresh along with phone-sized screens."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

Sixteen changes across omnideck and site this stretch. The week of September 14 was quiet enough that it did not earn its own post, so it rides along with the week after it.

The bulk of the work is browser tools finally handling modern web pages, integrations losing their all-or-nothing shape, and an interface pass that had been on the list for a while.

---

## Browser tools got much better at reading real pages

Eight of the sixteen changes were in browser tooling, and they share a theme. Real websites are messier than the ones we tested against, and this batch is mostly about closing that gap.

Image-only links and buttons now take their names from the image alt text, so they can be identified and clicked instead of showing up as anonymous blobs. Dropdown selection goes straight to the option you asked for, and no longer reports a false failure when choosing that option happens to navigate the page. Reading or saving a page now picks up web-component shadow content, including nested components and slotted text, which is where a growing share of modern interfaces keep their actual content. It also stops including inert template content, so you get what is on the page rather than unexpanded placeholders.

Two of the fixes are about timing. Browser tools look again at embedded content after the page finishes loading, so a slow iframe no longer hides its controls. And when something fails, the error now carries the underlying browser or vision-provider message. "Click failed" becomes something you can act on.

Saved browser profiles also preserve binary data through export and restore now, and retrying a failed session keeps the profile you picked instead of dropping back to the default.

---

## Integration access is per-tool now

Before this change, connecting an integration meant the agent could use all of it. Now access is an explicit allowlist, tool by tool, with a new modal flow for setting it up. Existing connections migrate automatically, so nobody has to redo their setup.

On screen it is one more modal. Underneath it means a connection is no longer all or nothing. Connect a service with forty operations, want three of them, and you can now say exactly that.

---

## The interface got a refresh

The chat, sidebar, and composer all got a visual pass: a friendlier typeface, softer corners, a lighter sidebar. Small stuff individually. Together it reads as a different product.

omnideck also works on phone-sized screens now, and can be installed to a home screen or app launcher as a standalone window. Both desktop panes stay reachable on a small screen and keyboard focus lands where it should. Desktop is still where the full experience lives. This is about checking on something from a phone, not moving the work there.

---

## Agent infrastructure and docs

Oversized tool output is now written to a file with a preview instead of flooding the conversation, and searches that hang get terminated rather than running until something else gives up.

There is also a small one from the carryover week: a blank `custom.css` is created automatically and loaded after the core styles. Drop your own CSS in there and it survives updates, no core file editing required.

On the site, there is a new "Using omnideck at Work" guide aimed at the IT and security review questions teams ask before adopting anything. The Slack integration guide got corrected step references and an optional section on giving the bot a personality, which is more fun than it sounds.

---

If you have been holding off on browser-heavy work because pages kept getting misread, this is the batch to retry. Tell us what still breaks in [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379).
