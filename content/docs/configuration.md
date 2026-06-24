+++
title    = "Configuration"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Configure LLM providers, execution policy, and shared file access."
order = 2
+++

Omnideck stores its configuration in `~/.omnideck/config.toml`. You can edit this file directly or use the settings panel in the UI.

## LLM Providers

Add provider credentials under `[[providers]]`. Credentials are stored in an encrypted local vault — the agent never receives your raw API keys.

```toml
[[providers]]
name   = "anthropic"
type   = "anthropic"
key_env = "ANTHROPIC_API_KEY"

[[providers]]
name   = "openai"
type   = "openai"
key_env = "OPENAI_API_KEY"

[[providers]]
name   = "local-ollama"
type   = "ollama"
base_url = "http://localhost:11434"
```

## Execution Policy

Control what the agent is allowed to run. Policies are evaluated before every bash command.

```toml
[execution]
allow_bash         = true
allowed_commands   = ["python", "node", "git", "curl", "ls", "cat", "grep"]
blocked_patterns   = ["rm -rf /", "curl.*169.254"]
max_runtime_secs   = 120
```

## Shared File Space

Define the directory tree the agent can read and write. Paths outside this boundary are inaccessible.

```toml
[filesystem]
shared_path = "~/omnideck-workspace"
```

## Telegram Notifications

Enable notifications for autonomous task completions.

```toml
[notifications]
telegram_bot_token = "..."
telegram_chat_id   = "..."
```

<div class="callout" data-tone="warn">
<strong>Security note:</strong> Never commit your config file to a public repository. Use environment variables for all secrets.
</div>
