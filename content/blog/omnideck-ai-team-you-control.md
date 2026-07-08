+++
title    = "Omnideck: an AI team you actually control"
date     = 2026-07-04
draft    = false
tags     = ["AI", "Open Source", "Privacy", "Automation", "Multi-Agent Systems"]
template = "templates/types/blog.html"

[extra]
description    = "Omnideck is an open-source, local-first, multi-agent AI system you run yourself. No telemetry, no locked-in models, no gatekeepers. Here's what it is and how to get started."
author         = "Ron Northcutt"
featured_image = "/images/agent-list.png"
+++

<div class="callout info"><strong>TL;DR:</strong> Omnideck is an open-source, local-first, multi-agent AI workbench with a real UI, not just a terminal. You need a container engine (Docker or Podman), an LLM source (a local Ollama install or a cloud API key), and about five minutes. <br><br>Install with Homebrew on Mac or Linux, or grab a binary. The setup wizard does the rest. Full steps are in the <a href="https://www.omnideck.dev/docs/getting-started.html">getting started guide</a>.
</div>

Everyone's talking about agentic AI right now, about handing off real work to a team of agents instead of babysitting one chatbot. But if you've actually tried to set that up yourself, you know it's a mess. You're stitching together frameworks, wiring up orchestration logic, and reading documentation that assumes you already have a PhD in the subject. It's powerful in theory and fiddly in practice, and that gap is exactly what got us going.

We built Omnideck to close that gap. It's a multi-agent AI system that runs on your own machine, works with whatever model you want, and never phones home with your data. No orchestration code to write, no framework to wire up by hand. You open a browser tab, and your AI team is already there, ready to work. It's still early, and we wanted to share it while your feedback can still shape where it goes.

## What Omnideck actually is

Omnideck is a team of AI agents you manage from a clean, local web UI, no terminal required. Each agent has its own skills, its own personality, and its own set of tools, so instead of one general-purpose assistant trying to do everything reasonably well, you get specialists. One writes code. One does research. One drafts your emails or pulls files from Gmail and Drive. You bring them in as you need them.

A few things make it different from the AI chat tool you're already using:

- **It's UI-based.** You click through setup, manage agents, and run tasks in a browser at `localhost:2337`. If you can use a web app, you can use Omnideck.
- **Agents are customizable.** Adjust skills, tools, and behavior per agent instead of getting one general-purpose assistant that's mediocre at everything.
- **You can hot-swap agents.** Switch to a different one mid-task without losing your place in the conversation.
- **Manager agents can spawn sub-agents.** A big task gets broken down and delegated automatically, the way a lead hands pieces of a project to the right people on their team.
- **It runs in a container.** Omnideck can't touch the rest of your system. Your API keys and credentials sit in a broker vault, and agents can use the tools without ever seeing the keys themselves.
- **There's no telemetry.** We don't collect usage data, and nothing leaves your machine except what you choose to send to your LLM provider.
- **It's model-agnostic.** Run it fully offline with Ollama, or point it at OpenAI, Anthropic, OpenRouter, or any OpenAI-compatible API. Your choice, and you can change your mind later.

## A day with it

Say your company is about to release a new feature, and before you write about it, you want to know how the competition stacks up: their strengths, their weaknesses, and the sharpest way to describe the difference in a post you're planning to share online.

You start a conversation and hand the general agent a link to your company's release notes, along with what you're trying to accomplish. It reads the notes first, so it actually understands what shipped. Then it looks up who your competitors are and spins up a handful of research agents, one per competitor. Each one runs its own browser session, out on the web digging up what it can find. You can watch them work in real time if you want. As they finish, each research agent summarizes what it found and reports back to the main conversation.

The general agent pulls it all together into a short report you can actually use: what each competitor does well, where they fall short, and where your feature has an edge. From there, you can switch to a tech agent to fact-check the details and confirm nothing got garbled along the way. Once you trust the research, you switch again, this time to a creative agent you've customized to write social posts in your voice. You draft a rough paragraph or two yourself, hand it over, and ask for a review. It suggests edits, you push back on some and take others, and you go back and forth until it reads the way you want. When it's ready, you copy it out and post it.

Start to finish, that's one conversation, four specialized agents, and work that would otherwise mean hours of open tabs, half-finished notes, and a draft you never quite got around to polishing.

## Where this came from

Larry started Omnideck as an experiment in the summer of 2025, poking at what a local, container-isolated multi-agent setup could look like. I joined in early 2026 to help push it from proof-of-concept into something other people could actually install and use.

Between the two of us, we use Omnideck every day now, for research, drafting, and the kind of work that's easy but slow: the stuff that used to mean five browser tabs and three different tools open at once. Once it started saving us real time, it seemed pointless to keep it to ourselves.

It's still in beta. There are rough edges and gaps we're actively closing. But we'd rather ship it now and let real use shape the roadmap than sit on it until it's "done." A lot of what makes Omnideck useful came from someone hitting a wall and telling us about it, and that only happens once people are actually using it.

Larry's got more on the technical origin story and what the early experiments looked like. That's the next post.

## What's coming next

A few things on the near-term roadmap:

- **More integrations.** If there's a service you want Omnideck talking to, tell us.
- **Deeper agent customization.** The agent profile system is getting more knobs, so you can dial in exactly how each agent behaves.
- **Team features.** Sharing agent setups and workflows across a team, not just running solo.
- **Performance work.** Faster, leaner, more efficient, on an ongoing basis.

We're building this in the open, so the roadmap bends toward what people actually ask for. If you hit a wall or want something it doesn't do yet, that feedback goes somewhere.

## What this is really about

Omnideck augments your judgment and your voice, it doesn't replace them. You end up with your own small team of helpers that can handle the things that are easy but time-consuming, like digging through the web for competitor research, or the things that are specialized, like editing copy into a consistent style. That frees you up for the part that actually needs you: synthesizing the research, drafting the post, deciding what's worth saying, and polishing the result until it's right. And it does all of that in a fraction of the time it would take you to do it alone.

## Get started

Install takes about five minutes:

1. **Install the CLI.** Homebrew is the easiest path on macOS or Linux (`brew install omnideck-dev/tap/omnideck`), or download a binary for your platform.
2. **Run `omnideck install`.** The wizard detects Docker or Podman, checks for Ollama, and pulls the container image.
3. **Open `localhost:2337`.** A setup wizard walks you through connecting an LLM provider and picking your models.

That's it. Your data lives in `~/Omnideck` and survives updates.

Full instructions, prerequisites, and CLI reference are in the [getting started docs](https://www.omnideck.dev/docs/getting-started.html). The [GitHub repo](https://github.com/omnideck-dev/omnideck) has the source, and it's Apache 2 licensed, so you can look under the hood or fork it outright.

Try it, break it, tell us what's missing. That's how this gets better.