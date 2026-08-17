+++
title    = "Local Models with Ollama"
date     = 2026-08-16
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Connect omnideck to models served locally by Ollama."
order = 6
+++

omnideck can use [Ollama](https://ollama.com/) to run model inference on your computer instead of sending prompts to a hosted model provider. Ollama runs outside the omnideck container and exposes the models you have installed through its local API.

Local inference does not make every omnideck feature offline. Browser research, cloud integrations, and Ollama cloud models still use the network.

## Install Ollama

[Download and install Ollama](https://ollama.com/download). Then pull a model. For example, `qwen3.5` supports tool use and image input:

```bash
ollama pull qwen3.5
```

List the models installed on this Ollama server:

```bash
ollama ls
```

## Choose a model

The [Ollama model library](https://ollama.com/library) shows each model's capabilities, variants, and download size. For omnideck:

- choose a model with **Tools** support for agents that need to use omnideck tools
- choose a size that fits your available memory or VRAM
- choose a model with **Vision** support if it should interpret images and screenshots

The same model can be used for ordinary agent work, vision, compaction, and conversation titles when it supports the required capabilities. You can also select different models for those roles.

## Connect omnideck to Ollama

During first-time workbench setup, choose **Ollama (local)**. omnideck normally fills the container-safe Ollama URL detected during installation. Click **Connect**, then choose a main model from the models returned by that Ollama server. The optional vision step only lists models Ollama reports as supporting image input.

If setup is already complete, open **Settings → Providers**, click **Add**, choose **Ollama**, and confirm the detected base URL with **Test & add**. Choose the provider and model for an individual agent under **Agents**. The system-wide vision and compaction models are under **Settings → System**.

## Connection check

omnideck reaches Ollama from inside its Podman container, so the URL used inside omnideck is not normally `http://localhost:11434`. The desktop app and CLI pass the correct host address into the container. CLI users can run `omnideck doctor` to test that connection.

On Windows, Ollama may be reachable on Windows but not from the Podman machine. If the container check fails, guided setup provides these steps:

1. Quit Ollama from the notification area.
2. Open **Edit environment variables for your account**.
3. Add a user variable named `OLLAMA_HOST` with the value `0.0.0.0:11434`.
4. Open Ollama again.

This setting can expose Ollama to other computers if Windows Firewall permits it. Do not allow Ollama through the firewall on public networks.

## Ollama cloud models

Ollama can expose cloud models through the same local API. Sign in and run or pull a model whose tag ends in `:cloud`; for example:

```bash
ollama signin
ollama run kimi-k2.5:cloud
```

These models do not run locally and require an Ollama account and network connection. After the cloud model appears in `ollama ls`, omnideck can list it with the other models exposed by that Ollama server.

## Troubleshooting

**"Ollama connection refused" in `omnideck doctor`**

Only matters if you're using local models. Make sure:
1. Ollama is running (`ollama serve`)
2. `omnideck doctor` can reach Ollama from inside the container
3. On Windows, follow the `OLLAMA_HOST` guidance above if the container check fails
4. A firewall is not blocking the Podman host connection

**Models do not appear in omnideck**

Run `ollama ls` to confirm they are installed on the same Ollama server. Pull the model if needed, then test the Ollama connection under **Settings → Providers**. omnideck caches Ollama's model details briefly, so reopen the model picker after the connection succeeds.
