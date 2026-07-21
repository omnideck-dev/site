+++
title    = "Omnideck weekly update: July 13-19, 2026"
date     = 2026-07-20
draft    = false
tags     = ["Changelog"]
template = "templates/types/blog.html"

[extra]
description    = "20 PRs merged across two repos this week. Custom Apps gets a real runtime, browser tools get more careful about what they click and see, and CI finally covers them."
author         = "Ron Northcutt"
featured_image = "/images/weekly-update.png"
+++

Twenty PRs this week, all in omnideck and site. Fewer than last week's 25, but the biggest one had been sitting on the list for a while: Custom Apps got its first real runtime! 

Browser tools took the rest of the attention, mostly in the form of fixing edge cases that only show up once real pages start throwing a weird DOM at the agent. The site kept its own pace too, with a guides section, a mobile fix, and two more blog posts live.

---

## Custom Apps gets a runtime

![Custom apps in Omnideck](/images/update/26-07-20-custom-apps.jpg)

The Custom Apps feature we mentioned last week now has an actual runtime and workspace behind it (#122). This is the piece that turns "custom apps" from an idea on the roadmap into something an agent can run. 

The core idea is that you can instruct Omnideck on how to build, manage, and update your custom software, and run it from your instance! This makes the AI Workbench even more useful.

### Example 1 : IDE App

![IDE App](/images/update/26-07-20-ide-app.jpg)

You can already write code and edit files in Omnideck, but its not the best experience. As a test, Larry spent an hour having Omnideck build an IDE app from scratch. This is surprising usefula, and gives us a great path forward to making Omnideck even more useful. Of course, you could also just ask Omnideck to install something like [Code OSS](https://github.com/code-oss-dev/code) or another tool. 

### Example 2 : Omnideck Projects

![Project App](/images/update/26-07-20-project-app.jpg)

This is another experiment. We've talked for a while about creating a workspace/project feature in Omnideck, but we are always trying to balance the utility we provide with flexibility. Opinions are helpful, but they can also constrain.

So, Larry created a pretty nifty Projects tool that lets you organize your conversations, artifacts, files, etc. into a project that you can manage. It also has a feature for managing and cleaning up your files. This is more of an experimental POC, but it does have value!

### Alpha testers

![Enable custom apps](/images/update/26-07-20-app-enable.jpg)

This is currently in alpha, so it is not enabled by default. You can turn on the custom apps feature if you want to try it out, but there may be breaking changes in the future. That shouldn't be a problem because Omnideck can just adjust your custom apps to adapt, but this is more for advanced users.

Just go to `Settings -> System -> Enable Custom Apps` to turn it on. You can also see Larry's [sample repo of apps](https://github.com/lefoulkrod/omnideck-custom-apps) above for an example AND a skill you can import to help create your own apps.

---

## Browser tools get more careful

Last week's browsing agent work was about resilience. This week was about correctness.

`browse_page` now returns a fallback instead of failing outright when a snapshot can't be taken (#184), so a bad page no longer stalls the whole run. Controls sitting inside ARIA wrappers are exposed properly now (#181), which matters for any site that leans on accessibility markup for its interactive elements. When a click opens a new tab, the agent lands on that tab instead of continuing to act on the old one (#175). And the logic that decides what counts as an "interactive descendant" got fixed (#170), which cleans up a class of false positives where the agent thought something was clickable when it wasn't.

None of these are visible features. They're the difference between an agent that *mostly* works and one that reliably works.

---

## Testing catches up to the browser tools

With that much surface area in the browsing agent, it needed real test coverage, and it got some. Browser tests now run in CI (#179) instead of relying on manual checks, and they run in parallel (#182) so the suite doesn't slow everything else down. A stale shadow ref collision bug also got fixed in agent infrastructure (#183), the kind of thing that's much easier to catch with tests running on every PR than by hand.

---

## One more fix, locked in with tests

The modal-in-collapsed-wrapper bug from a couple weeks back got pinned down for good, with regression tests added alongside the fix (#155). Once something like this has a test guarding it, it stays fixed.

---

## Site picked up a guides section

The Omnideck site added a guides section to the docs, including the first walkthrough for a [Slack integration](https://www.omnideck.dev/guides/slack-integration.html) (#64). The site is also properly mobile responsive now (#63), the blog listing sorts by date correctly (#61), and there's an updated [arbor (static site generator)](https://github.com/rlnorthcutt/arbor) binary available (#62).

Two more posts went up: one on [OpenRouter's free models](https://www.omnideck.dev/blog/using-openrouter-free-models.html) (#60) and Omnideck's (the AI) first blog post on [how it uses its browser tools to find bugs in its browser tools](https://www.omnideck.dev/blog/self-testing-ai-browser-tools.html) (#59). Small housekeeping rounded out the rest: a todo file for tracking future work (#56), a community link in the nav (#55), a changelog page (#54), and screenshots added to last week's update (#57, #58).

---

Join us on [Slack](https://omnideckcommunity.slack.com/archives/C0BGWDQN2TY/p1783946625666379) if you want to keep up to date and help guide the future of the project.