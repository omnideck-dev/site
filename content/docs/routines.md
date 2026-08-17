+++
title    = "Routines"
date     = 2026-08-16
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Create repeatable work that one or more agents can run now or on a schedule."
order = 4
+++

A routine is repeatable work carried out by one or more agents. It can run once as soon as it is created, run again whenever you choose, or recur on a schedule.

## Create a routine

Create routines by describing them to an agent in a conversation. The **General** agent can load the **routine_planner** skill when needed; you can also assign that skill to another agent.

Open **Routines** in the sidebar to see starter ideas, or start a new conversation and ask for what you want directly:

```text
Create a routine that every weekday at 8:00 AM America/Chicago
reviews my unread email and today's calendar, then writes a short
morning brief.
```

The agent turns the request into a routine with at least one task. Each task has its own instruction and agent. Tasks run in sequence by default, or the agent can make independent tasks run in parallel.

## Scheduling

Scheduled routines use a standard five-field cron expression and an IANA timezone such as `America/Chicago` or `UTC`.

| Expression | Meaning |
|---|---|
| `0 8 * * 1-5` | Weekdays at 08:00 |
| `0 * * * *` | At the start of every hour |
| `0 9 * * 1` | Every Monday at 09:00 |
| `0 */4 * * *` | Every 4 hours |

If you create a routine without a schedule, omnideck queues its first run immediately. It remains in **Routines**, where you can run it again with **Run now**.

## Review and manage routines

The Routines list shows each routine's status, schedule, and most recent run. Open one to:

- **Pause** or **Resume** its future scheduled runs
- **Run now** without waiting for its next scheduled time
- inspect **Recent Runs**, including status, duration, task completion, and each task's output
- inspect **Tasks**, including the assigned agent, dependencies, and retry limit
- delete a run or the entire routine

Pausing a routine prevents future scheduled runs. It does not cancel a run already in progress.

<div class="callout" data-tone="info">
<strong>Routines survive restarts.</strong> If omnideck restarts while a task is marked as running, that task is returned to pending so the runner can pick it up again.
</div>
