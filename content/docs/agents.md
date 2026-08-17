+++
title    = "Agents"
date     = 2026-08-16
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Create agents with their own model, instructions, skills, and autonomy settings."
order = 3
+++

Agents are reusable configurations for different kinds of work. Each one can use its own model, instructions, skills, and inference settings. omnideck includes four agents to start with, and you can create more.

## The agents included with omnideck

| Agent | Starting point |
|---|---|
| **General** | Adapts to the job, loads skills when needed, and can delegate larger work to other agents |
| **Code Expert** | Programming, debugging, and code review with the **coder** skill |
| **Research Agent** | Research and analysis with the **browser** and **coder** skills |
| **Creative Writer** | Brainstorming and writing with more creative inference settings |

These are editable starting points. The model selected during initial setup is applied to all four.

## Create or edit an agent

Open **Agents** in the sidebar, then select an existing agent or click **New agent**. An agent can define:

- **Identity** — name, description, icon, and whether the agent is enabled
- **Provider and model** — the model used when this agent handles a turn or a routine task
- **System prompt** — its role, instructions, and boundaries
- **Skills** — bundles of tools and guidance available to the agent
- **Autonomy** — whether it may spawn other agents or load more skills during a conversation
- **Inference settings** — presets or advanced model-specific controls such as temperature, context window, thinking, and compaction threshold

You can also duplicate, import, and export agents. An agent assigned to a routine cannot be deleted until the routine no longer uses it.

## Skills

Skills bundle tools with the instructions for using them. omnideck includes four skills:

| Skill | Tool categories | What it does |
|---|---|---|
| **assistant** | Memory, Email, Calendar, Drive, Contacts, HTTP | Use persistent memory and services you have connected |
| **browser** | Browser, Web Fetch | Navigate and interact with websites, capture screenshots, and read known URLs as text |
| **coder** | Coding | Read and edit files, search code, run commands, and install packages |
| **routine_planner** | Planning | Create, inspect, and run routines made of one or more agent tasks |

Assign skills in the agent editor. If **Allow loading skills mid-conversation** is enabled, an agent can also load an available skill when a job requires it.

Connected-service tools only appear when the corresponding integration is available. The **assistant** skill grants access to those email, calendar, drive, contacts, and HTTP tool categories; it does not create the connection itself.

## Context management

As a conversation grows, omnideck tracks context usage and can compact older turns into a summary when the agent's configured threshold is reached. Recent context remains available while the summary carries forward the important earlier information.

Set the threshold in the agent's advanced inference settings. Choose the model used for compaction in **Settings → System**.

## Sub-agents

When **Allow spawning agents** is enabled, an agent can delegate self-contained parts of a job to other agents. Each delegated agent uses the selected profile and works in its own context.

Open **Agent Network** from the conversation to see the delegation graph, running/completed/error counts, and the activity for an individual agent. Browser or terminal workspaces opened by an agent can also be opened from its activity when available.

## Switch agents in a conversation

Use the agent selector at the top of the conversation. The selected agent handles the next message; the existing conversation remains in place.
