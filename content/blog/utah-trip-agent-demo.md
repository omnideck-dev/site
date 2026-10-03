+++
title    = "AI Agents on Your Computer Planned Our Utah Trip"
date     = 2026-10-03
draft    = false
tags     = ["ai-agents", "open-source", "demo"]
template = "templates/types/blog.html"

[extra]
description    = "omnideck is a free desktop app that puts AI agents to work on your computer. We asked it to help plan a Utah parks trip. Its agents read the official fee pages, built two apps you can try, and painted a sticker in GIMP as an experiment."
author         = "Larry Foulkrod"
featured_image = "/images/utah-trip/featured.png"
+++

omnideck is a free, open source desktop app that puts AI agents to work on your own computer. The agents can browse the web, build small apps, and check their own work. To show what that looks like, we asked omnideck to help plan a weekend in Utah's national parks. Four friends, three requests, and each one ends with something you can keep. This post shows the results, links two of them so you can try them, and explains how the demo was made.

<iframe width="560" height="315" src="https://www.youtube.com/embed/kzp_lSqwxaA" title="omnideck demo: research, build an app, and paint in GIMP" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## How this demo was made

Before the results, here is what you are looking at.

- **The model's replies were written in advance.** We ran omnideck with a scripted model so the demo is repeatable, the same way every time. The agent's words in the chat were planned.
- **Every tool action ran for real.** The browsers really opened nps.gov. Three sub-agents really ran at the same time. The app file was really written, and the agent really typed into it. GIMP really painted the sticker.
- **This is not a model benchmark.** It shows what omnideck's tools do when an agent uses them. It says nothing about how well any particular model would plan the same trip.
- **The GIMP part is experimental.** Desktop control ran on a development build. It is not in the current beta. More on that below.

## 1. Research: is the annual park pass worth it?

The request: have three specialists check each park's official fee page at the same time, then build a planner.

omnideck started three sub-agents, one per park. Each opened its park's fees page on nps.gov in its own browser and read the private vehicle fee.

![The omnideck chat showing three specialist agents, Zion Scout, Bryce Canyon Scout, and Arches Scout, running at the same time.](/images/utah-trip/scouts-spawned.jpg)

![The Zion National Park fees page on nps.gov, open in the Zion scout's browser, with the Private Vehicle $35.00 entry highlighted.](/images/utah-trip/zion-fee-page.jpg)

The fees, checked October 2, 2026, for a private vehicle and US residents:

| Park | Private vehicle |
|---|---|
| Zion | $35 |
| Bryce Canyon | $35 |
| Arches | $30 |
| America the Beautiful annual pass | $80 |

The parent agent turned those numbers into a planner. Then it opened the planner in its own browser and clicked through it, removing Arches and putting it back, to check that the answer changed.

![The park pass planner. Zion and Bryce Canyon are selected and Arches is not. The verdict reads: Pay at the gate. Save $10.](/images/utah-trip/planner-verdict.jpg)

All three parks cost $100 at the gate, so the pass saves $20. Skip Arches and the gate is $10 cheaper. **[Try the planner yourself](/demos/utah-trip/utah-park-planner.html).** It is the exact file the agent made. Fees change, so check nps.gov before you travel.

## 2. Build: who owes whom?

The request: a trip expense splitter for four people, one file we can share, settling up in the fewest payments.

omnideck wrote the app as a single HTML file. Then it opened the file in its own browser and tested it like a user would. It typed in an $80 park pass, chose Sam as the payer, clicked Add, and read the settle-up to confirm the math.

![The agent's browser filling in the expense form: Park pass, $80.](/images/utah-trip/agent-tests-app.jpg)

In the video, a person then adds dinner, $96 paid by Leo, and the balances update. Four people and four expenses settle in three payments.

![The settle-up after dinner is added: Sam pays Leo $68.50, Sam pays Maya $23.00, Priya pays Maya $5.50.](/images/utah-trip/settle-up.jpg)

**[Try the expense splitter](/demos/utah-trip/trip-splitter.html).** "Fewest payments" is exact. The app searches for the largest number of groups whose balances cancel out, and each group settles separately.

## 3. Experiment: painting a sticker in GIMP

The request: paint a sticker for the group chat in GIMP and let me watch.

The agent opened GIMP on its own Linux desktop. It filled in the sky and mesas with GIMP's scripting. Then it painted the arch, its highlight, its shadow, and a trail with real mouse strokes, and exported a transparent PNG.

![The arch half painted in GIMP, with the brush cursor mid-stroke.](/images/utah-trip/gimp-experimental.jpg)

![The finished sticker: a red-rock arch at sunset with UTAH and ROAD TRIP 2026.](/demos/utah-trip/utah-trip-sticker.png)

**This part is experimental and is not in the current omnideck beta.** It ran on a development build of desktop control, including a drag tool that has not shipped. Treat it as a preview of work in progress.

## What you can do with omnideck today

The research and build parts use tools in the current public beta: browser control, sub-agents working in parallel, and writing and testing files. omnideck is:

- free and open source under Apache 2
- a desktop app for macOS, Windows 11, and Linux, plus a CLI
- able to use cloud and local models side by side
- free to use with no omnideck account

[Install omnideck](/install.html) and try one of these requests on your own machine. If you build something with it, or it breaks, tell us in the [community Slack](/community.html).
