+++
title    = "Running Omnideck on Free Models: What Actually Works"
date     = 2026-07-15
draft    = false
tags     = ["Cost Optimization", "OpenRouter"]
template = "templates/types/blog.html"

[extra]
description    = "OpenRouter's free tier isn't unlimited, and the model that routes you around that fact comes with a real tradeoff. Here's what free actually costs, and how Omnideck runs a set of dedicated free agents for the busywork that never needed a paid model."
author         = "Ron Northcutt"
featured_image = "/images/openrouter-free-models.png"
+++

I've been testing whether Omnideck can lean on OpenRouter's free models instead of paying for every request, and that turned into a [reference gist](https://bit.ly/openrouter-free) covering every free model on the platform right now. That came from a demo video showing the setup in action (see below). Before getting into how it works inside Omnideck, it's worth being clear about what "free" actually means on OpenRouter, because it's not what most people assume.

*Watch the demo*

<iframe width="560" height="315" src="https://www.youtube.com/embed/1R61g29fnhk?si=Ib5CMp_u3UfzyznJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## TL;DR

- OpenRouter's free tier isn't unlimited. No credits gets you 50 requests a day. Put in $10, even if you never spend it, and that jumps to 1,000 a day.
- 50 requests a day runs out fast if you're running an agent loop. 1,000 a day is genuinely workable for background tasks.
- `openrouter/free` routes you to whatever free model is best or available, no config needed. Convenient, but you give up model choice.
- Six models are getting deprecated between July 19 and 21, 2026, including two of the strongest ones (Qwen3 Coder, Tencent Hy3). Don't build on those this week.
- Rate limits are per-account, not per-model or per-key. You can't route around them.
- The move for Omnideck: either one generic free agent on the router, or a few free agents pinned to specific models for jobs like vision or title generation, plus an escalation path to a real model when a task actually needs it.

## The two tiers of "free"

OpenRouter's free models aren't free in the open-source sense. They're rate-limited demo access, and the limit depends on whether you've ever put money into your account.

If you've never bought credits, you get 20 requests per minute and 50 requests per day. That's it. Fifty requests a day is fine for poking around or testing a prompt, but it falls apart fast if you're running anything with a loop, a retry, or more than one agent talking to itself.

Put $10 into your account, even if you never spend it on anything, and your daily cap jumps to 1,000 requests. Same 20 requests per minute. The $10 doesn't buy you tokens for the free models specifically, it buys you a better rate limit. That's a strange mechanic once you notice it: you're not paying for usage, you're paying for permission to use more of something that's still labeled free.

A few details make this messier:

- The limits are account-wide, not per-model. Spinning up more API keys doesn't help you.
- If your balance goes negative for any reason, you can start seeing 402 errors on free models too.
- Paid versions of these same models don't have a platform-level request cap at all.

So the real tiers are: broke and capped at 50 requests a day, or $10 in and capped at 1,000. Neither one is "unlimited," and neither one is what most people picture when a model is marketed as free.

There's also a shortcut worth knowing about: `openrouter/free`. It's not a model, it's a router that picks whichever free model is best or most available at the time of your request. Point your agent at it once and you never have to touch the config again, even as models get deprecated or new ones show up. The tradeoff is control. You don't get to pick the model, so you can't tune for a specific context window, a coding-tuned variant, or a model that handles vision. For anything where the model choice actually matters, picking one directly still makes more sense.

## What this looks like in practice

Fifty requests a day sounds like a lot until you count what a single agentic task actually costs. A multi-step agent that plans, calls a tool, checks the result, and retries once can burn through 10 to 15 requests before it's done with one task. At that rate, the no-credit tier gives you maybe three or four real tasks a day before you're locked out until midnight UTC.

The 1,000/day tier is a different story. That's enough headroom for genuine daily use: testing prompts, running a small agent loop, handling routine tasks without babysitting a counter. It's still not something you'd build a product around, since a single user hammering an endpoint could eat the daily limit in an afternoon. But for a background agent inside something like Omnideck, one that only wakes up for small, low-stakes jobs, 1,000 requests a day is workable.

The practical move is obvious once you see the numbers: put $10 in, even if you have no plan to spend it, and your free tier becomes 20x more usable.

## Caveats worth knowing before you build on this

A few things I'd flag before anyone wires these into a real workflow:

**Deprecation is coming for six models in the next week.** Tencent Hy3, Qwen3 Coder, Dolphin Mistral Venice, Llama 3.3 70B, Llama 3.2 3B, and Hermes 3 405B all get pulled between July 19 and 21, 2026. Two of those, Qwen3 Coder and Tencent Hy3, are genuinely strong models people are actively using for coding and reasoning work. If you've hardcoded a model string into a script or agent config, this is the week it breaks.

**Rate limits aren't per-model, they're per-account.** You can't route around the cap by juggling different free models or generating extra API keys. OpenRouter tracks total request volume across everything.

**The music models aren't actually free.** Lyria 3 Pro and Lyria 3 Clip show $0 token pricing, which makes them look like they belong on the free list, but they charge per generation ($0.08 a song, $0.04 per 30-second clip). Easy to miss if you're skimming.

**Content moderation is the exception, not the rule.** Cohere's North Mini Code is the only model on the free list with moderation built in. Everything else, including Venice Dolphin Mistral, is running with no guardrails at the model level, which is worth knowing if you're exposing any of this to other users.

**Free doesn't mean stable.** These are demo-tier slots subsidized by OpenRouter and the model providers. Context windows, output caps, and availability can shift without much warning, the deprecation wave happening this month is proof of that.

## What actually works in Omnideck

Omnideck already runs a mix of local models and API-backed ones depending on the task. There's a clear slot for one or more low-priority agents, explicitly scoped to run on OpenRouter's free tier and handle the small, frequent, low-stakes jobs that don't deserve a paid API call. The question is whether that's one agent on the free router, or a few agents each pinned to a model suited to their job.

Think of it as the equivalent of a junior team member you hand busywork to: summarizing a log file, drafting a quick commit message, checking whether a blog post has any obvious typos, tagging content, doing a first-pass classification before a stronger model reviews it. None of that needs Claude or GPT-4 class reasoning. It needs "good enough, fast, and doesn't cost anything."

A few design notes on how it's set up:

- **Route by task type, not by default.** The free agent should be the first stop for anything low-stakes and short, with an explicit escalation path to a real model when the task calls for it. Not a fallback used only when other models fail.
- **`openrouter/free` is the lazy option, and that's not an insult.** For a single generic free agent handling miscellaneous busywork, pointing it at the router and forgetting about it is a reasonable call. It's set-and-forget: no config to update when a model gets deprecated, no monitoring which free models are still around.
- **But a few specialized agents beat one generic router.** Rather than one agent on `openrouter/free`, it's worth running a handful of free agents, each pinned to a model suited to a specific job. A vision-capable model like Nemotron Nano 12B VL for image tagging or screenshot review. A fast, cheap model for title generation, tagging, or summarization where you don't need reasoning depth. This costs you the "set it and forget it" simplicity, since you have to swap the pinned model when one gets deprecated, but you get consistent, predictable output per task instead of whatever the router happened to hand you that call.
- **Pick a model that won't disappear next week.** Given the deprecation list, Qwen3 Next 80B or one of the Nemotron Nano models makes more sense as a pinned default than anything flagged for July.
- **Treat it as disposable.** No moderation, no guaranteed uptime, no long-term model stability. The free agents should never touch anything where output quality or availability actually matters. They're there to save API spend on the stuff nobody would miss if it failed.

At the end of the day, it's not about running Omnideck for free, but routing the 80% of requests that were never worth paying for onto a tier that costs nothing. 