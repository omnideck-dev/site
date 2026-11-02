+++
title    = "omnideck weekly update: October 12-25, 2026"
date     = 2026-10-26
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "4 changes across one repo. Saved conversations load with far less data, browser tools stopped misreading page content, and runtime dependencies got a security pass."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

Four changes this stretch, all in omnideck. Nothing landed the week of October 12, so this post covers it together with the week after. Fewer changes than usual. Two of them matter more than the count suggests.

---

## Saved conversations use a lot less data

Opening a saved conversation was transferring an unused duplicate of its history. That is gone, and saved conversations now load with compressed responses as well. The complete history still arrives. There is just less of it moving over the wire.

If you work with long chats, or your connection is not great, this is the change you will feel. Everything else in this post is invisible by comparison.

---

## Browser tools stopped misreading page content

A long list of corrections landed together. Page reads no longer pick up glossary text from other pages, which was producing content that looked plausible and was not from the page you asked about. Inline words at the edge of the viewport stay intact instead of getting clipped. Background controls stay hidden behind scroll-locked modals.

Popup responses use the main document now, scrolling aims within the visible part of embedded pages, and scroll limits persist between tool calls while staying independent per tab. PerimeterX and DataDome challenge pages show an actionable notice instead of looking like a broken page, which saves you from debugging a bot check as if it were our bug.

---

## Runtime dependencies got a security pass

Networking, encryption, certificate trust, and web-content processing dependencies were updated to address high and critical advisories. Distrusted certificates are now rejected, and a few denial-of-service gaps in the desktop build are closed.

This is maintenance rather than a feature. It is also the sort of maintenance that is easy to defer and expensive to defer too long.

---

If you have been bitten by a slow-loading long conversation, that one is fixed. [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379) if anything still misbehaves.
