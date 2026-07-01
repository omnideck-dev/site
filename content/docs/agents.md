+++
title    = "Agents"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Create and configure agent profiles — each with its own model, system prompt, and tool access."
order = 3
+++

An agent profile is a named configuration that defines how a particular agent thinks and what it can do. Omnideck ships with a default profile. You can create as many profiles as you like and switch between them at any point in a conversation.

## Creating a profile

Go to **Settings → Profiles** in the web UI and click **New Profile**. Fill in:

- **Name** — a descriptive label (e.g. "Research Agent", "Code Agent")
- **Model** — which LLM provider and model to use for this agent
- **System prompt** — the agent's core instructions, persona, and constraints
- **Tools** — which capabilities the agent has access to
- **Inference parameters** — temperature, top-p, and other model settings

## Tool access

Tool access is scoped per agent profile. A research agent might have full web and memory access but no bash. A DevOps agent might have bash and filesystem but no browser.

| Tool | Description |
|---|---|
| Browser automation | Full browser control — clicking, typing, scrolling, and screenshotting |
| Web search | Search the web (via configured search provider) |
| Code execution | Write and run Python, install packages, build projects |
| Filesystem | Read and write files in the shared workspace (`~/Omnideck`) |
| Memory | Read and write persistent facts across conversations |
| Integrations | Access Gmail and iCloud (requires configured integrations) |

Restricting tools improves focus and reduces the chance of unintended side effects. A dedicated research agent doesn't need bash.

## Context management

As a conversation grows, Omnideck tracks token usage and compacts older messages when a configurable threshold is reached. Compaction summarizes older turns and replaces them with a compact summary, preserving recent context verbatim. This keeps conversations going indefinitely without hitting model context limits.

The compaction model is configured in **Settings → Providers** — you can use a smaller, cheaper model for compaction and a larger one for actual work.

## Sub-agents

Agents can spawn sub-agents for delegated, parallel work. The parent agent describes a goal, the sub-agent runs it, and results are passed back. This enables multi-step workflows where different agents handle different parts of a task.

Sub-agent activity is visible in the **Agent Network** view — each running sub-agent appears as a node with its own activity stream, active tool, and context usage.

Sub-agent spawning is enabled or disabled per agent profile in Settings.

## Switching agents mid-conversation

Use the profile selector at the top of the chat panel to switch to a different profile. The conversation history is preserved; the new agent's system prompt takes effect from the next turn.

## Starter prompts

Each profile can define a set of starter prompts — suggested first messages displayed when you open a new conversation with that profile. Configure these in **Settings → Profiles** to help collaborators or your future self get started quickly.
