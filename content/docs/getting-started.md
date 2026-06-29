+++
title    = "Getting Started"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Install and run Omnideck in under five minutes."
order = 1
+++

Omnideck runs inside a container managed by the `omnideck` CLI. You need a container engine (Docker or Podman) and either a cloud LLM API key or a local Ollama install.

## Prerequisites

- **Container engine:** Docker 20.10+ or Podman 4.0+
- **LLM provider:** an API key for OpenAI, Anthropic, OpenRouter, or any OpenAI-compatible endpoint — or [Ollama](https://ollama.com/) for local models
- **RAM:** 4 GB minimum (8 GB recommended for local models)

## Install the CLI

The `omnideck` CLI wraps your container engine with a guided installer and simple management commands. Download the binary for your platform:

**Linux** (and Windows via WSL2):

```bash
curl -L https://github.com/omnideck-dev/cli/releases/latest/download/omnideck-linux-amd64 \
  -o omnideck && chmod +x omnideck && sudo mv omnideck /usr/local/bin/
```

**macOS (Apple Silicon):**

```bash
curl -L https://github.com/omnideck-dev/cli/releases/latest/download/omnideck-darwin-arm64 \
  -o omnideck && chmod +x omnideck && sudo mv omnideck /usr/local/bin/
```

For Intel Macs or ARM Linux, grab the `darwin-amd64` or `linux-arm64` build from the [releases page](https://github.com/omnideck-dev/cli/releases/latest).

Verify it's on your path:

```bash
omnideck --version
```

## Install Omnideck

```bash
omnideck install
```

The install wizard:

1. Detects your container engine (Docker or Podman)
2. Checks whether Ollama is reachable on the host
3. Suggests container memory limits sized for your system
4. Pulls the container image and starts the container

When the wizard finishes, open **[http://localhost:2337](http://localhost:2337)** in your browser.

## First-run setup

A setup wizard runs in the UI the first time you open it. It guides you through:

1. **Adding an LLM provider** — cloud (OpenAI, Anthropic, OpenRouter, or any OpenAI-compatible endpoint) or local Ollama
2. **Picking your main model** — used for chat, context compaction, and conversation titles
3. **Picking an optional vision model** — for tasks that involve image input

Cloud providers list available models automatically. Ollama lists whatever you've already pulled.

That's it — you're running.

## Managing Omnideck

Everything is driven through the CLI:

```bash
omnideck status      # container state, data dirs, Ollama reachability, and web UI port
omnideck stop        # gracefully stop the container
omnideck start       # start it back up
omnideck restart     # stop then start
omnideck update      # pull the latest image and recreate the container
omnideck logs -f     # tail container logs
omnideck doctor      # run health checks and print a pass/warn/fail report
omnideck uninstall   # remove the container (optionally back up and delete data)
```

Your data lives in `~/Omnideck` and survives restarts and upgrades. Conversations, memory, agent profiles, goals, and generated files are all preserved when you `update`.

## Next steps

- [CLI Reference](/docs/cli-reference.html) — full command and flag reference
- [Local Models](/docs/local-models.html) — run Omnideck fully offline with Ollama
- [Integrations](/docs/integrations.html) — connect Gmail, Calendar, and Drive
- [Agents](/docs/agents.html) — create and customize agent profiles
- [Autonomous Tasks](/docs/tasks.html) — schedule background goals

<div class="callout" data-tone="info">
<strong>Privacy:</strong> Omnideck never makes outbound connections to Omnideck servers. Everything runs on your machine. Your data stays in <code>~/Omnideck</code>.
</div>
