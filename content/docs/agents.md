+++
title    = "Agents"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Create and configure agent profiles — each with its own model, system prompt, and skills."
order = 3
+++

An agent profile is a named configuration that defines how a particular agent thinks and what it can do. Omnideck ships with four default profiles. You can create as many profiles as you like and switch between them at any point in a conversation.

## Creating a profile

Go to **Settings → Profiles** in the web UI and click **New Profile**. Fill in:

- **Name** — a descriptive label (e.g. "Research Agent", "Code Agent")
- **Model** — which LLM provider and model to use for this agent
- **System prompt** — the agent's core instructions, persona, and constraints
- **Skills** — which skill bundles the agent loads (each skill grants a set of tool categories)
- **Inference parameters** — temperature, top-p, and other model settings

## Skills

Agents don't toggle individual tools. Instead, you assign **skills** — curated bundles of tool categories. Each skill loads a specific set of capabilities. Omnideck ships with four built-in skills:

| Skill | Tool categories | What it does |
|---|---|---|
| **assistant** | Memory, Email, Calendar, Drive, Contacts, HTTP / API | Persistent memory across conversations and access to connected integrations |
| **browser** | Web Browsing, Web Fetch | Full browser automation — navigate, click, type, scroll, fill forms, and take screenshots. Also fetches pages as clean text without a browser. |
| **coder** | Coding & Files | Read, write, edit, and patch files. Run bash commands, install packages, search codebases. |
| **goal_planner** | Goal Planning | Create and manage autonomous goals with scheduled tasks that run in the background. |

You can mix and match skills per profile. A research agent might load **browser** and **assistant** but not **coder**. A DevOps agent might load **coder** and **assistant** but not **browser**. Restricting skills improves focus and reduces the chance of unintended side effects.

Tool categories from integrations — Email, Calendar, Drive, Contacts, and HTTP / API — become available automatically when you connect an integration and load the **assistant** skill.

## Context management

As a conversation grows, Omnideck tracks token usage and compacts older messages when a configurable threshold is reached. Compaction summarizes older turns and replaces them with a compact summary, preserving recent context verbatim. This keeps conversations going indefinitely without hitting model context limits.

The compaction model is configured in **Settings → Providers** — you can use a smaller, cheaper model for compaction and a larger one for actual work.

## Sub-agents

Agents can spawn sub-agents for delegated, parallel work. The parent agent describes a goal, the sub-agent runs it, and results are passed back. This enables multi-step workflows where different agents handle different parts of a task.

Sub-agent activity is visible in the **Agent Network** view — each running sub-agent appears as a node with its own activity stream, active tool, and context usage.

Sub-agent spawning is enabled or disabled per agent profile in Settings.

## Switching agents mid-conversation

Use the profile selector at the top of the chat panel to switch to a different profile. The conversation history is preserved; the new agent's system prompt takes effect from the next turn.
