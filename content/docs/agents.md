+++
title    = "Agents"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Create and configure agent profiles — each with its own model, prompt, tools, and memory."
order = 3
+++

An agent profile is a named configuration that defines how a particular agent thinks and what it can do. You can have as many profiles as you like and switch between them at any point in a conversation.

## Creating a profile

From the UI sidebar, click **New Agent** and fill in:

- **Name** — a descriptive label (e.g. "Research Agent", "Code Agent")
- **Model** — which LLM provider and model to use
- **System prompt** — the agent's core instructions and persona
- **Tools** — which capabilities the agent has access to

Or create a profile in `~/.omnideck/agents/`:

```toml
# ~/.omnideck/agents/research.toml
name   = "Research Agent"
model  = "claude-sonnet-4-6"
provider = "anthropic"

system_prompt = """
You are a thorough research assistant. Your job is to gather, verify, and summarize information from the web. Always cite sources. Prefer primary sources over summaries.
"""

[tools]
web_browse  = true
web_search  = true
memory      = true
filesystem  = false
bash        = false
```

## Per-agent tool access

Tool access is scoped per agent. A research agent might have full web and memory access but no bash. A DevOps agent might have bash and filesystem but no browser.

| Tool | Description |
|---|---|
| `web_browse` | Full Playwright browser automation |
| `web_search` | Web search (via configured provider) |
| `memory` | Read and write persistent keyed facts |
| `filesystem` | Access the shared file space |
| `bash` | Run shell commands (subject to execution policy) |
| `mcp` | Connect to configured MCP servers |

## Context management

When a conversation approaches the model's context limit, Omnideck can run an automatic compaction pass. Configure this per agent:

```toml
[context]
compaction = true
compaction_model   = "gpt-4o-mini"
compaction_provider = "openai"
```

## Sub-agents

Agents can spawn sub-agents for delegated, parallel work. Use the `spawn_agent` tool in a conversation — the parent agent defines the goal, the sub-agent runs it, and results are passed back.

Sub-agent spawning is opt-in per profile:

```toml
[tools]
spawn_agents = true
max_subagents = 3
```

## Switching agents mid-conversation

Click the agent selector at the top of any conversation to switch to a different profile. The conversation history is preserved; the new agent's system prompt takes effect from the next turn.
