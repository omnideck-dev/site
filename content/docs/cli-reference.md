+++
title    = "CLI Reference"
date     = 2026-08-16
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Install omnideck from the terminal and use the commands available in the current standalone CLI."
order = 5
+++

<div class="callout" data-tone="info"><strong>Most people should start with the <a href="/install.html">omnideck desktop app</a>.</strong> Use the standalone CLI if you prefer to install and manage omnideck from a terminal.</div>

The `omnideck` CLI sets up and manages the same local omnideck runtime as the desktop app. It uses Podman on Windows, macOS, and Linux; other container runtimes are not supported.

Running `omnideck` without a subcommand opens the appropriate interactive screen for first setup, runtime preparation, repair, or managing an existing installation.

This reference was verified against the published `v0.10.0` stable and `v0.11.0-beta.5` preview binaries. Run `omnideck --version` to check the build installed on your computer.

<h2 id="install-the-cli">Install the CLI</h2>

### Homebrew on macOS or Linux

The Homebrew tap is the non-preview CLI channel:

```bash
brew install omnideck-dev/tap/omnideck
```

Upgrade it later with:

```bash
brew upgrade omnideck
```

### Release archive

For the current stable command set, Windows builds, preview builds, or a manual installation, download the archive for your operating system and architecture from the <a href="https://github.com/omnideck-dev/cli/releases" target="_blank" rel="noopener">omnideck CLI releases ↗<span class="sr-only"> (opens in a new tab)</span></a>. Releases include Linux and macOS tar archives, Windows ZIP archives, and a `SHA256SUMS` file.

Extract `omnideck` (`omnideck.exe` on Windows), put it somewhere on your `PATH`, and verify the installation:

```bash
omnideck --version
```

Run `omnideck` as your normal user. Do not put `sudo` before it or choose **Run as administrator**; guided setup asks the operating system for approval only when a system change requires it.

## First run

```bash
omnideck
```

The first run prepares Podman when needed and guides you through creating the first omnideck installation. When setup finishes:

```bash
omnideck doctor
omnideck status
```

The local browser address is normally `http://localhost:2337` and is also shown by `omnideck list` and `omnideck status`.

## Commands

### Setup and everyday management

| Command | What it does |
|---|---|
| `omnideck` | Open the right interactive screen for setup, repair, or management |
| `omnideck tui` | Open the terminal dashboard directly |
| `omnideck add` | Set up one new instance; `install` and `setup` are supported aliases |
| `omnideck list` | List saved instances, their status, and browser addresses; `instances` is an alias |
| `omnideck update` | Download the current omnideck image and safely recreate an instance while keeping its data |
| `omnideck start` | Start a stopped instance |
| `omnideck stop` | Stop an instance |
| `omnideck restart` | Stop and start an instance without changing its saved configuration |
| `omnideck status` | Show the selected instance, image, runtime, volumes, Ollama status, and browser address |
| `omnideck logs` | Show logs and follow new output by default |
| `omnideck doctor` | Check Podman, the instance, browser access, saved data, available memory, and optional Ollama access |
| `omnideck remove NAME` | Remove one instance; keeps its data unless deletion is explicitly confirmed; `uninstall` is an alias |
| `omnideck help [command]` | Show help for the CLI or one command; `<command> --help` does the same thing |

### Saved configuration

| Command | What it does |
|---|---|
| `omnideck config show` | Display the selected instance configuration |
| `omnideck config set <key> <value>` | Change one supported setting |
| `omnideck config path` | Print the selected instance configuration path |

Supported keys for `config set` are `home_volume`, `state_volume`, `memory`, `shm_size`, `web_ui_port`, and `image`. Apply a changed setting by running `omnideck update` for that instance; a simple restart does not recreate the container with new settings.

### Runtime and automation

| Command | What it does |
|---|---|
| `omnideck runtime status` | Report whether the shared Podman runtime is ready |
| `omnideck runtime ensure` | Prepare or repair the shared Podman runtime |
| `omnideck environment ensure` | Reconcile an exact application environment for the desktop app or automation |
| `omnideck completion <shell>` | Generate a completion script for Bash, Fish, PowerShell, or Zsh |

`environment ensure` requires `--name` and accepts `--image`, `--port`, `--memory`, `--shm-size`, `--home-volume`, and `--state-volume`. It is primarily an integration surface for the desktop app and automation; interactive users normally use bare `omnideck` or `omnideck add`.

## Global flags

| Flag | Purpose |
|---|---|
| `--config <path>` | Use an explicit configuration file |
| `--name <name>`, `-n <name>` | Select an instance by name |
| `--no-color` | Disable styled output |
| `--debug` | Print raw Podman commands and output |
| `--json` | Emit machine-readable JSON or NDJSON; never prompt or open the terminal UI |

Run `omnideck --version` to print the version, commit, and build date. `--version` belongs to the root command rather than every subcommand.

Every command also accepts `-h` or `--help`.

`--json` also selects the non-interactive path for commands that support one. When more than one instance exists, non-interactive commands require `--name` instead of opening a picker.

## Command-specific flags

### `add`

| Flag | Purpose |
|---|---|
| `--plain` | Run non-interactively with plain-text output |
| `--port <port>` | Set the local browser port; default is `2337` |
| `--memory <size>` | Set the container memory limit, such as `2g` |
| `--shm-size <size>` | Set shared memory, such as `1024m` |
| `--image <reference>` | Use a different container image |
| `--runtime podman` | Compatibility flag; Podman is the only accepted runtime |
| `--suggest-defaults` | Print the next available name and port; intended for JSON automation |

The global `--name` flag sets the new instance name when used with `add`.

### `update`

| Flag | Purpose |
|---|---|
| `--plain` | Update non-interactively with plain-text output |

### `logs`

| Flag | Purpose |
|---|---|
| `--follow`, `-f` | Follow new log output; defaults to `true` outside JSON mode |
| `--tail <lines>` | Start with this many lines; default is `50` |

Use `--follow=false` for a finite plain-text log read. In JSON mode, following defaults to `false` unless you explicitly pass `--follow`.

### `remove NAME`

| Flag | Purpose |
|---|---|
| `--plain` | Remove non-interactively with plain-text output |
| `--yes` | Skip the confirmation prompt; required with `--plain` or `--json` |
| `--keep-volumes` | Keep saved data volumes |
| `--delete-volumes` | Permanently delete saved data volumes |
| `--backup` | Back up data before deleting volumes |
| `--no-backup` | Delete volumes without a backup |

Non-interactive removal requires exactly one of `--keep-volumes` or `--delete-volumes`. Deleting volumes also requires exactly one of `--backup` or `--no-backup`.

## Examples

```bash
# Create another instance interactively
omnideck add

# List every saved instance
omnideck list

# Inspect and manage a specific instance
omnideck --name omnideck2 status
omnideck --name omnideck2 stop
omnideck --name omnideck2 start

# Follow logs, starting with the latest 100 lines
omnideck --name omnideck2 logs --tail 100

# Run health checks
omnideck --name omnideck2 doctor

# Change a setting, then recreate safely to apply it
omnideck --name omnideck2 config set memory 4g
omnideck --name omnideck2 update

# Create an instance without a TUI
omnideck add --plain --name staging --port 2338

# Remove an instance interactively
omnideck remove staging
```

## Multiple instances

`omnideck add` creates one additional instance with its own name, browser port, home volume, and state volume. `omnideck list` shows all saved instances.

Commands that act on one instance open a picker when more than one exists. Pass `--name` to select directly. Scripts and JSON callers must pass `--name`; the CLI never opens a picker without an interactive terminal.

<h2 id="configuration">Configuration</h2>

### Configuration files

Instance files live under the platform's conventional configuration directory:

| Operating system | Directory |
|---|---|
| Linux | `$XDG_CONFIG_HOME/omnideck-cli`, or `~/.config/omnideck-cli` |
| macOS | `~/Library/Application Support/omnideck-cli` |
| Windows | `%AppData%\omnideck-cli` |

Each instance is stored at `instances/<name>.yaml`. The shared Podman choice is stored separately in `settings.yaml`.

```yaml
container_name: omnideck
layout_version: 1
home_volume: omnideck-home
state_volume: omnideck-state
memory: 2g
shm_size: 1024m
web_ui_port: "2337"
image: ghcr.io/omnideck-dev/omnideck:latest
installed_at: 2026-08-16T12:00:00Z
```

The home and state values are Podman volume names, not host directory paths. The home volume holds user-visible working files; the state volume holds application state. `omnideck remove` keeps both unless you explicitly choose permanent deletion.

<div class="callout" data-tone="warn"><strong>Treat the state volume as sensitive.</strong> It contains application state, encrypted credential data, and the local key used to decrypt it. Protect exported copies like a password-manager backup.</div>

### Memory limits

Guided setup suggests a container memory limit based on the computer's total RAM, from 1 GB on smaller systems up to 6 GB on larger ones. Shared memory defaults to half of the container limit. On macOS, the container limit also stays below the memory assigned to the Podman machine.

These limits apply to the omnideck container, not to Ollama or another model server running separately on the host. Check the requirements of any local model you plan to use.

Change the limits, then recreate the container safely to apply them:

```bash
omnideck config set memory 4g
omnideck config set shm_size 2g
omnideck update
```

## Build from source

Building the CLI requires Go 1.25.13 or newer:

```bash
git clone https://github.com/omnideck-dev/cli
cd cli
go build -trimpath -o omnideck .
```

Run `./omnideck --version`, then move the binary to a directory on your `PATH` if you want it available system-wide.
