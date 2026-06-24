+++
title    = "Autonomous Tasks"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Schedule goals that run in the background and notify you on completion."
order = 4
+++

The task engine lets you define goals that Omnideck runs autonomously — on a schedule, at a specific time, or triggered manually. Tasks use the same agent loop and tool access as interactive conversations.

## Creating a task

From the UI, go to **Tasks → New Task** and configure:

- **Name** — human-readable label
- **Agent** — which agent profile to use
- **Goal** — the instruction the agent receives at the start of each run
- **Schedule** — cron expression, one-off datetime, or manual only

Or define tasks in `~/.omnideck/tasks/`:

```toml
# ~/.omnideck/tasks/daily-digest.toml
name     = "Daily Digest"
agent    = "research"
schedule = "0 8 * * *"   # 08:00 UTC every day
timezone = "America/New_York"

goal = """
Search for the top 5 AI news stories from the last 24 hours.
Summarize each in 2-3 sentences.
Write the digest to /workspace/digests/{date}.md
"""
```

## Scheduling

Omnideck supports standard cron expressions plus human-friendly shortcuts:

| Expression | Meaning |
|---|---|
| `@daily` | Once a day at midnight |
| `@hourly` | Once an hour |
| `0 9 * * 1` | Every Monday at 09:00 |
| `0 */4 * * *` | Every 4 hours |

## Notifications

When a task completes or fails, Omnideck sends a notification with a summary and any output files attached. Configure your notification channel in [Configuration](/docs/configuration.html).

## Task history

Every run is recorded: start time, end time, status, the agent's full output, and any files written. View run history in the UI under **Tasks → History**.

<div class="callout" data-tone="info">
<strong>Crash safety:</strong> If Omnideck restarts while a task is running, the task is automatically reset to "pending" on the next start. It will run again at its next scheduled time.
</div>

## Concurrent limits

Control how many tasks can run at the same time:

```toml
[tasks]
max_concurrent = 3
```

If more tasks are scheduled than the limit allows, they queue and run as slots open up.
