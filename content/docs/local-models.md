+++
title    = "Local Models with Ollama"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Run Omnideck fully offline using local models via Ollama."
order = 6
+++

If you'd rather run models locally than send data to a cloud provider, Omnideck supports [Ollama](https://ollama.com/) for fully local inference. Install Ollama on your host, pull the models you want, and Omnideck lists them automatically in the setup wizard.

## Install Ollama

Download and install Ollama from [ollama.com](https://ollama.com/). After installing, pull the models you want to use:

```bash
ollama pull kimi-k2.5      # main model (chat, compaction, titles)
ollama pull qwen3.5        # vision model (optional — for image input)
```

Verify Ollama is running and your models are available:

```bash
ollama list
```

## Recommended models

| Role | Suggested model | Notes |
|---|---|---|
| Main | `kimi-k2.5` | Used for chat, context compaction, and conversation title generation |
| Vision | `qwen3.5` | Must support image input — or use your main model if it does |

The main model handles everything by default. A separate vision model is only needed if you want a model specifically optimized for image input.

## Connect Omnideck to Ollama

During `omnideck install`, the wizard checks whether Ollama is reachable on the host and warns if it isn't. If Ollama is running, select it as your provider in the setup wizard — Omnideck will list the models you've pulled.

If Omnideck is already running, go to **Settings → Providers** in the web UI and add Ollama as a provider. The list of available models updates automatically from your local Ollama install.

## macOS and Docker Desktop

On macOS with Docker Desktop, Ollama must be bound to `0.0.0.0` (not just `127.0.0.1`, which is the default) so the container can reach it on the host. Set this before starting Ollama:

```bash
export OLLAMA_HOST=0.0.0.0
ollama serve
```

Or set it permanently in your shell profile. `omnideck doctor` will report whether Ollama is reachable from inside the container.

## Ollama cloud variants

Ollama can also broker cloud-hosted model variants alongside your local models, so they appear the same way in Omnideck. After `ollama login`, pull a cloud variant:

```bash
ollama pull kimi-k2.5:cloud
```

Cloud variants skip your local GPU but still need to be pulled so Ollama exposes them. This is useful if you want a unified provider interface that can mix local and cloud models.

## Troubleshooting

**"Ollama connection refused" in `omnideck doctor`**

Only matters if you're using local models. Make sure:
1. Ollama is running (`ollama serve`)
2. On macOS / Docker Desktop, `OLLAMA_HOST=0.0.0.0` is set (see above)
3. On Linux with Podman, the firewall isn't blocking the host network bridge

**Models don't appear in the setup wizard**

The wizard lists models already pulled in Ollama. Pull your desired models first (`ollama pull <model>`), then reopen Settings in the Omnideck UI.
