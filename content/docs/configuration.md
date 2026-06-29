+++
title    = "Configuration"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Configure LLM providers, memory limits, and manage multiple Omnideck instances."
order = 2
+++

Omnideck has two layers of configuration: the CLI config (managed by the `omnideck` CLI on your host) and the in-app settings (managed through the web UI at `http://localhost:2337`).

## CLI configuration

The CLI stores a config file per instance at:

```
~/.config/omnideck-cli/instances/<container-name>.yaml
```

A typical config looks like this:

```yaml
container_name: omnideck
shared_dir: /home/user/Omnideck
state_dir: /home/user/Omnideck/.state
memory: 3g
shm_size: 1536m
web_ui_port: "2337"
engine: docker
image: ghcr.io/omnideck-dev/omnideck:main
installed_at: 2025-01-15T10:30:00Z
```

You can inspect or update config values using the CLI:

```bash
omnideck config show                   # pretty-print the saved config
omnideck config set memory 4g          # change the memory limit
omnideck config set web_ui_port 2338   # change the port
omnideck config path                   # print the config file path
```

Changes to `memory` or `web_ui_port` take effect on the next `omnideck restart`.

## Memory limits

The install wizard suggests a memory limit based on your system RAM (roughly 20% of host RAM, between 1 GB and 8 GB). You can adjust this at any time:

```bash
omnideck config set memory 6g
omnideck restart
```

## LLM providers

LLM providers and API keys are configured through the **Settings → Providers** tab in the web UI, not in the CLI config file. The app stores credentials in an encrypted local vault inside the container — your API keys are never written to the CLI config file.

Supported providers:
- **Anthropic** (Claude models)
- **OpenAI** (GPT models)
- **OpenRouter** (multi-provider routing)
- **Any OpenAI-compatible endpoint** (custom or self-hosted)
- **Ollama** (local models — see [Local Models](/docs/local-models.html))

## Shared file directory

The `shared_dir` in the CLI config is mounted into the container and visible as `~/Omnideck` both on your host and inside the container. This is where the agent reads and writes files, and where conversations and memory are stored. You set this during `omnideck install` and it persists across updates.

The `state_dir` (a hidden `.state` subdirectory inside `shared_dir`) holds persistent container state — you won't normally need to interact with it directly.

## Multiple instances

You can run more than one Omnideck container on different ports. When Omnideck is already installed, `omnideck install` asks whether to update the existing instance or install a new one. New instances get a unique container name (`omnideck2`, `omnideck3`, …), separate data directories, and an incremented port.

To manage a specific instance by name:

```bash
omnideck --name omnideck2 status
omnideck --name omnideck2 stop
omnideck --name omnideck2 uninstall
```

When more than one instance exists, commands that need an instance show a picker if `--name` is not given.

<div class="callout" data-tone="warn">
<strong>Security note:</strong> The CLI config file does not contain API keys or credentials — those live in the encrypted vault inside the container. Do not share your <code>~/Omnideck/.state</code> directory, as it contains the vault master key.
</div>
