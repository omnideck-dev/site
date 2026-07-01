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

<ol class="gs-steps">
  <li><a href="#step-1-install-the-cli">Install the CLI</a> — Homebrew (recommended) or binary download</li>
  <li><a href="#step-2-install-omnideck">Install Omnideck</a> — the setup wizard handles the rest</li>
  <li><a href="#step-3-open-the-tool">Open the tool</a> — connect your LLM and start working</li>
</ol>

## Prerequisites

- **Container engine:** Docker 20.10+ or Podman 4.0+
- **LLM provider:** an API key for OpenAI, Anthropic, OpenRouter, or any OpenAI-compatible endpoint — or [Ollama](https://ollama.com/) for local models
- **RAM:** 4 GB minimum (8 GB recommended for local models)

## Step 1: Install the CLI

The `omnideck` CLI wraps your container engine with a guided installer and simple management commands.

### Homebrew (macOS and Linux)

The recommended way to install on macOS or Linux:

```bash
brew tap omnideck-dev/omnideck
brew trust omnideck-dev/omnideck
brew install omnideck
```

Or as a single command:

```bash
brew tap omnideck-dev/omnideck && brew trust omnideck-dev/omnideck && brew install omnideck
```

The `brew trust` step is required once by Homebrew's third-party tap security policy.

To upgrade later:

```bash
brew upgrade omnideck
```

### Download a binary

Grab the binary for your OS from the [releases page](https://github.com/omnideck-dev/cli/releases):

| Platform | File | SHA-256 |
|---|---|---|
| macOS (Apple Silicon) | `omnideck-darwin-arm64.tar.gz` | `c93e4f17…9d7af8` |
| macOS (Intel) | `omnideck-darwin-amd64.tar.gz` | `07b70880…e06728` |
| Linux (x86-64) | `omnideck-linux-amd64.tar.gz` | `e550a2fa…ed30d9` |
| Linux (ARM64) | `omnideck-linux-arm64.tar.gz` | `63d2057b…00032d` |
| Windows (x86-64) | `omnideck-windows-amd64.zip` | `b1dd6da9…c249366` |

Extract the archive and move the binary to a directory on your `PATH`. On Linux or macOS:

```bash
tar -xzf omnideck-linux-amd64.tar.gz
chmod +x omnideck
sudo mv omnideck /usr/local/bin/
```

### Verify the install

```bash
omnideck --version
```

## Step 2: Install Omnideck

```bash
omnideck install
```

The install wizard:

1. Detects your container engine (Docker or Podman)
2. Checks whether Ollama is reachable on the host
3. Suggests container memory limits sized for your system
4. Pulls the container image and starts the container

When the wizard finishes, open **[http://localhost:2337](http://localhost:2337)** in your browser.

## Step 3: Open the tool

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
