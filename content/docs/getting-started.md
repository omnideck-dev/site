+++
title    = "Getting Started"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Install and run Omnideck in under five minutes."
order = 1
+++

Omnideck runs inside a container managed by the `omnideck` CLI. You'll need Docker or Podman installed on your machine.

## Prerequisites

- Docker 24+ or Podman 4+
- 4 GB RAM minimum (8 GB recommended for local models)
- At least one LLM API key, or a running Ollama instance

## Install the CLI

```bash
curl -fsSL https://omnideck.dev/install.sh | sh
```

Or download the binary directly from the [releases page](https://github.com/omnideck/omnideck/releases).

## Start Omnideck

```bash
omnideck start
```

The first run pulls the container image and launches the setup wizard. The wizard will guide you through:

1. Choosing your container runtime (Docker or Podman)
2. Adding your first LLM provider
3. Creating your first agent profile
4. Setting a shared file directory

## Access the UI

Once started, Omnideck is available at `http://localhost:3000` in your browser.

## Next steps

- [Configuration](/docs/configuration.html) — tune your providers, models, and execution policy
- [Agents](/docs/agents.html) — create and configure agent profiles
- [Autonomous Tasks](/docs/tasks.html) — schedule background goals

<div class="callout" data-tone="info">
<strong>Note:</strong> Omnideck never makes outbound connections to Omnideck servers. Your data stays on your machine.
</div>
