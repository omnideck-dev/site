+++
title= "How Omnideck Got Started"
date= 2026-07-04
tags= ["origin-story", "open-source", "local-ai", "freedom-first"]
draft= false

[extra]
author= "Larry Foulkrod"
description= "The origin story of Omnideck: from a summer experiment with local LLMs to an open-source AI agent workbench built on freedom-first principles."
featured_image = "/images/omnideck_hero_banner.png"
+++

It's weird to look back and realize that Omnideck (a tool I now depend on every single day, sometimes against my better judgment) originated as a glorified science experiment. A year ago, it didn't even have a "proper" name. I called it `computron_9000`, a half-baked project I assembled in the summer of 2025 to experiment with local LLMs. Back then, the idea of running language models on your own hardware was still new enough that you had to kludge together your own tools if you wanted to do anything useful. Open-source harnesses like OpenClaw weren't really a thing yet, so if you wanted to experiment, you were on your own, armed with nothing but Google searches and stubbornness.

I was just curious. As a software developer, I've always been the type to poke at new tech until it either breaks or starts working well enough to be useful. Local LLMs were no different. I wanted to see what they could do, how they could fit into my workflow, and (let's be honest) whether they were just hype or something truly worth paying attention to. So, I built a basic harness to talk to them. It wasn't pretty, but it worked, which in software is basically the same thing as pretty.

## From Toy to Tool

At first, `computron_9000` was little more than a command-line script with delusions of grandeur. But the more I used it, the more I recognized I needed something better. I needed a way to keep my experiments isolated from the rest of my system, so I containerized it, mostly so a bad prompt couldn't take down my whole machine. I wanted a UI, so I leaned on my React experience and built one. It was still rough around the edges, but it was *mine* — a tool that evolved alongside my needs, and occasionally against my will.

Then came the browser.

I do a lot of research, both for work and for personal projects. At the time, I was juggling tabs, notes, and half-baked ideas across a dozen different tools, and it was driving me nuts. I wanted a way to let the AI see what I was seeing, to interact with the web the way I did. So, I started tinkering with vision models, feeding them screenshots of my browser, and teaching them to "read" what was on the page. It was clunky at first but it worked. Suddenly, I had a tool that could not only talk to me but understand the context of what I was working on, which was more than I could say for some of my friends.

## The Multi-Agent Rabbit Hole

Once the browser integration started functioning, I hit another obstacle: I needed *multiple* AI agents, each with their own settings, tools, and personalities. Maybe one agent was great at research but terrible at coding, while another could write scripts but got lost in long documents. Sound familiar? It's basically every team I've ever worked on. I didn't want to switch between them manually. I wanted them to work together, like a team, except one that might actually listen.

So I constructed a multi-agent system. It was messy, over-engineered, and probably unnecessary for 90% of what I was doing at the time. But it was *fun*. I added tools for the agents to use: file creation, script execution, browser control, even a way to spin up other agents on the fly. It was like building a tiny, digital Swiss Army knife, if a Swiss Army knife occasionally forgot what it was doing halfway through a task. Some tools were useful immediately; others sat unused for months until I stumbled into a problem they were perfect for, at which point I felt like a genius instead of someone who'd just been hoarding features.

## Enter Ron: The First User (and First Pain in My Neck)

By early 2026, `computron_9000` had grown from a weekend project into something I actually relied on. I'd been talking about it with my old friend Ron Northcutt, a developer and technical marketer who's seen more than his fair share of half-baked tools, and isn't shy about telling you so. After a few weeks of hounding him, I finally convinced him to try it out.

Ron's first reaction? *"This is cool, but how the hell do I install it?"*

Fair. I'd been running it locally for so long that I'd forgotten how much of a pain it was to set up. So, Ron did what any self-respecting developer would do when handed a mess: he built a CLI tool to make installation and upgrades easier, presumably so he'd never have to ask me for help again. Then he started using it. Then he started breaking it. Then he started filing tickets, suggesting improvements, and sending me PRs at ungodly hours, as if sleep were optional for both of us.

We fell into a rhythm: I'd build something new, Ron would try to use it, and we'd spend evenings debating what worked, what didn't, and why. It wasn't always pretty. There were arguments about design choices, late-night debugging sessions, and more than a few "why the hell did you do it that way?" moments, but it was productive. Ron brought a fresh perspective, and his feedback pushed me to make the tool more robust, more intuitive, and (most importantly) more useful for someone who wasn't me.

## From `computron_9000` to Omnideck

By mid-2026, `computron_9000` had outgrown its joke of a name. It wasn't a toy anymore. It was a tool we both relied on and something that had quietly become a part of our daily workflows. We used it for research, planning projects, organizing data, even testing new models. It was flexible enough to adapt to whatever we threw at it, but opinionated enough to keep us from drowning in options, which is more than I can say for most of the AI tooling landscape.

We realized two things:

1) This thing was *good*. Not "good for a side project" good, but legitimately useful.
2) If it was useful for us, it might be useful for other people too, assuming they could get past the name.

So we decided to spin it off as a proper open-source project. We rebranded it since `computron_9000` was fun, but it wasn't going to convince anyone we were serious, and "Omnideck" actually sounded like a tool. Then, we started sketching out a roadmap. But we didn't want to build *just another AI tool*. The market was already flooded with options, and most of them fell into one of two traps:

* **Too open**: Your system becomes a playground with no guardrails, and you spend more time configuring it than actually using it.
* **Too closed**: You're locked into a vendor's ecosystem, with no control over your data or how the tool evolves.

We wanted something different: a tool constructed for *real* work, with privacy, freedom, and user choice at its core. No vendor lock-in. No features bolted on as an afterthought. No telemetry, because frankly nobody needs a play-by-play of our prompt history. Your data remains on your hardware unless you deliberately choose otherwise. Your credentials are encrypted at rest in a vault the agent process can't directly access, because we've read enough headlines to know better.

We also made a deliberate choice to be desktop-first. The full workbench experience (multiple agents, sub-agent monitoring, scheduled tasks, integration management) is constructed for a real screen and a real keyboard. We'd rather perfect that experience than ship something half-baked and call it "mobile-first innovation."

And because we believe freedom should extend to the license itself, Omnideck is open source under Apache 2.0.

## What We're Building (and Why It Matters)

Our roadmap isn't based on what other AI tools are doing. It's based on what we've needed over the past year of using Omnideck every day. Things like:

* **Research**: Whether it's for work or planning a trip, we needed a way to gather, organize, and synthesize information without jumping between a dozen tabs and tools.
* **Planning**: Projects, features, even personal goals — we wanted a tool that could help us break them down, track progress, and adapt as things changed, ideally without a whiteboard involved.
* **Automation**: Scheduled tasks, routines, and integrations with other systems. Why do the same thing manually when an agent can handle it for you and only occasionally get it wrong?
* **Data Organization**: From notes to code snippets to random ideas, we needed a way to keep everything accessible and searchable, instead of scattered across seventeen text files named "notes_final_v2."
* **Model Testing**: We're developers. We like to tinker. We wanted a way to test new models, compare them, and see how they fit into our workflows, without rewriting half our stack every time someone released a new one.

Most importantly, we wanted a tool that *respects its users*. That means no creepy data collection, no forced upgrades, and no "take it or leave it" design choices. Omnideck is built to be yours and to adapt to how you work, not the other way around.

## What's Next?

We're excited to share Omnideck with the world, but we're also realistic. This is a side project — a labor of love built in the margins of our lives, mostly late at night, fueled by stubbornness and questionable amounts of coffee. We're not a big company with a marketing budget or a team of full-time developers. What we do have is a year of late nights, trial and error, and a tool that's been battle-tested in the real world by exactly the two people most likely to break it.

We don't know what the future holds for Omnideck. But we do know this: we're building something we're proud of, something that's made our lives easier, and something we think could help others too, assuming they can handle a little chaos.

If you're tired of AI tools that feel like they were designed by committee (or worse, by a sales team) give Omnideck a try. Kick the tires. Break it. Tell us what works and what doesn't. Better yet, contribute. We're just getting started, and we'd love for you to be part of the journey.

After all, that's how this whole thing started: with a couple of developers, a lot of curiosity, and a willingness to build something better, one late-night argument at a time.

