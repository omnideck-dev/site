+++
title    = "CLI Reference"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Complete reference for the omnideck CLI — commands, flags, and configuration."
order = 5
+++

The `omnideck` CLI installs, manages, and monitors your Omnideck container. It wraps Docker or Podman with a guided installer and simple management commands.

## Commands

| Command | Description |
|---|---|
| `install` | Interactive TUI wizard — install or update an existing instance |
| `update` | Pull the latest image and recreate the container |
| `start` | Start a stopped container |
| `stop` | Gracefully stop the running container |
| `restart` | Stop then start |
| `status` | Print a status table (container, data dirs, Ollama, web UI port) |
| `logs` | Tail container logs |
| `doctor` | Run parallel health checks and print a pass/warn/fail report |
| `config show` | Pretty-print the saved config |
| `config set <key> <value>` | Update a single config key |
| `config path` | Print the config file path |
| `uninstall` | Stop, remove container, optionally delete data |

## Global flags

```
--config string   Config file path (default: ~/.config/omnideck-cli/config.yaml)
--name string     Instance name (e.g. omnideck, omnideck2)
--no-color        Disable color output
--debug           Print raw engine commands and stderr
--version         Print version and exit
```

## Install flags

```
--image string    Override the container image (for testing alternate builds)
```

## Logs flags

```
--follow, -f      Follow log output
--tail int        Number of lines to show from the end of the logs
```

## Examples

```bash
# Tail logs and follow
omnideck logs --follow --tail 100

# Run health checks
omnideck doctor

# Manage a specific instance by name
omnideck --name omnideck2 status
omnideck --name omnideck2 stop

# Test an alternate image without changing the default
omnideck install --image ghcr.io/example/omnideck:dev

# Update a config value
omnideck config set memory 6g

# Uninstall a specific instance
omnideck --name omnideck2 uninstall
```

## The `doctor` command

`omnideck doctor` runs parallel health checks and prints a pass/warn/fail report:

- **Container** — is the container running and on the expected image?
- **Data directories** — does `~/Omnideck` exist and is it writable?
- **Ollama** — is Ollama reachable on the host? (only relevant for local models)
- **Web UI** — is the web UI responding on the configured port?

Start here when something isn't working. The output tells you exactly what's wrong and how to fix it.

## Multiple instances

If Omnideck is already installed, `omnideck install` asks whether to update the existing instance or install a new one. New instances get a unique container name (`omnideck2`, `omnideck3`, …), separate data directories under `~/Omnideck2`, and an incremented port.

Commands that need an instance (e.g. `start`, `status`) show a picker when more than one instance exists, or accept `--name` to skip the prompt.

## Configuration file

Config files live at:

```
~/.config/omnideck-cli/instances/<container-name>.yaml
```

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

- **`shared_dir`** — mounted into the container, visible to you as `~/Omnideck`
- **`state_dir`** — hidden subdirectory for persistent container state
- **`memory`** and **`shm_size`** — set by the wizard, can be changed with `config set`

## Building from source

To build the Omnideck container image yourself instead of pulling from the registry:

```bash
git clone https://github.com/omnideck-dev/omnideck
cd omnideck
docker build -f container/Dockerfile -t omnideck:latest .
```

Then point the CLI at your local image:

```bash
omnideck install --image omnideck:latest
```
