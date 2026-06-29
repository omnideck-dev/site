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

Go to **Goals** in the sidebar and click **New Goal**. Configure:

- **Name** — human-readable label
- **Agent** — which agent profile to use
- **Goal** — the instruction the agent receives at the start of each run
- **Schedule** — cron expression, one-off datetime, or manual only

Example goal:

```
Search for the top 5 AI news stories from the last 24 hours.
Summarize each in 2-3 sentences.
Write the digest to ~/Omnideck/digests/{date}.md
```

## Scheduling

Omnideck supports standard cron expressions:

| Expression | Meaning |
|---|---|
| `@daily` | Once a day at midnight |
| `@hourly` | Once an hour |
| `0 9 * * 1` | Every Monday at 09:00 |
| `0 */4 * * *` | Every 4 hours |

Leave the schedule blank to create a manual-only task you trigger yourself.

## Task history

Every run is recorded: start time, end time, status, the agent's full output, and any files written. Drill into a run in the **Goals** view to see the agent's full activity log — thinking, tool calls, and output — exactly as you'd see it in a live conversation.

## Output files

Files the agent writes to `~/Omnideck` during a task run are available on your host filesystem immediately. They also appear in the file preview panel if the task is open in the UI.

<div class="callout" data-tone="info">
<strong>Crash safety:</strong> If Omnideck restarts while a task is running, the task is automatically reset to pending on the next start. It will run again at its next scheduled time.
</div>

## Stopping a running task

Open the task in the **Goals** view and click **Stop**. The agent receives a stop signal and wraps up gracefully — it finishes its current step and then exits cleanly rather than being killed mid-tool-call.
