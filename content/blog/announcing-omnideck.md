+++
title  = "Announcing Omnideck"
date   = 2025-06-01
draft  = false
template = "templates/types/blog.html"

[extra]
description = "A local-first AI agent workbench that runs on your machine, supports any LLM, and never phones home."
author = "Ron Northcutt"
+++

Today we're open-sourcing Omnideck — a self-hosted AI agent workbench that runs on your desktop or home server.

## Why we built it

The current generation of cloud AI agents is powerful but comes with a fundamental compromise: your conversations, files, and credentials flow through servers you don't control, you're locked to one model per tool, and running a local model like Llama or Mistral means piecing together brittle tooling.

Omnideck fixes this by giving you a full agent workbench that runs locally, supports any LLM, and keeps all your data on your machine.

## What's in the first release

- **Multi-agent profiles** — build a team of specialized agents, each with its own model, system prompt, and tool access
- **Real browser automation** — headed browser with both structural and visual navigation
- **Code execution** — write and run code with full output streaming
- **Persistent memory** — keyed facts that survive session resets
- **Autonomous tasks** — cron-scheduled goals with notification on completion
- **Gmail and iCloud integration** — read, search, and send email from inside the agent

## What's next

We're working on:

- MCP server support — connect any Model Context Protocol server
- Google Calendar and Drive integration
- Windows and ARM support
- Visual workflow builder for task chains
- Plugin API for custom tools
- Expanded model provider support

## Get started

**Linux** (and Windows via WSL2):

```bash
curl -L https://github.com/omnideck-dev/cli/releases/latest/download/omnideck-linux-amd64 \
  -o omnideck && chmod +x omnideck && sudo mv omnideck /usr/local/bin/
omnideck install
```

**macOS (Apple Silicon):**

```bash
curl -L https://github.com/omnideck-dev/cli/releases/latest/download/omnideck-darwin-arm64 \
  -o omnideck && chmod +x omnideck && sudo mv omnideck /usr/local/bin/
omnideck install
```

Then open `http://localhost:2337` and follow the setup wizard.

Feedback and contributions are welcome on [GitHub](https://github.com/omnideck-dev/omnideck).
