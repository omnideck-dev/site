+++
title    = "Getting Started"
date     = 2026-08-15
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Choose the desktop app or standalone CLI and get omnideck running on your computer."
order = 1
+++

Choose the desktop app for guided setup in a native window. Use the standalone CLI if you prefer to install and manage omnideck from a terminal.

<div class="setup-paths" aria-label="Choose a setup path">
  <a class="setup-path-card" href="#desktop-app">
    <span class="setup-path-label">Recommended</span>
    <strong>Desktop app</strong>
    <span>Guided installation and setup in a native app for Windows, macOS, and Linux.</span>
    <span class="setup-path-link">Follow the desktop path →</span>
  </a>
  <a class="setup-path-card" href="#standalone-cli">
    <span class="setup-path-label">Advanced</span>
    <strong>Standalone CLI</strong>
    <span>Install and manage the same omnideck runtime from a terminal.</span>
    <span class="setup-path-link">Follow the CLI path →</span>
  </a>
</div>

## Prerequisites

- **Supported computer:** The desktop app supports Windows 11, macOS, and supported desktop Linux distributions. Choose a package offered for your operating system and architecture on the install page. The standalone CLI publishes x86-64 and ARM64 builds for Windows, macOS, and Linux.
- **Memory:** The desktop app has a published minimum of 4 GB of system RAM. The CLI sizes omnideck's container between 1 GB and 6 GB based on the host. Local Ollama models need additional RAM or VRAM, and the amount varies by model.
- **Model connection:** Agents need one configured model. Use Anthropic, OpenAI, or OpenRouter with an API key; a reachable OpenAI-compatible endpoint; or [Ollama](https://ollama.com/) for local models. You can add this after installation.
- **Internet connection:** Initial setup and updates download runtime and application files. After setup, internet access depends on the model provider and integrations you choose.

You do not need to install Podman first; both guided setup paths can prepare it. The desktop app already includes the matching CLI, so desktop users do not install the standalone CLI separately.

<h2 id="desktop-app">Desktop app</h2>

The desktop app is the default way to run omnideck on a personal computer. It keeps installation and day-to-day runtime management in one place.

<h3 id="install-omnideck">1. Install omnideck</h3>

Open the **[omnideck install page](/install.html)**, choose your operating system, and follow its visual walkthrough. The page points to the current desktop release and provides the correct packages and SHA-256 checksums for each supported architecture.

<p><a href="/install.html" role="button" data-variant="primary">Choose your installer →</a></p>

<div class="callout" data-tone="warning">
<strong>Preview packages:</strong> The current macOS and Windows installers do not yet carry paid publisher identities. Download only from the <a href="/install.html">official install page</a> and verify the checksum before approving a Gatekeeper or SmartScreen warning.
</div>

<h3 id="prepare-your-machine">2. Prepare your machine</h3>

Open omnideck and select **Set up omnideck**. Guided setup:

1. Checks your operating system and architecture
2. Installs, prepares, or repairs the supported Podman runtime
3. Creates the local Podman machine where the platform requires one
4. Pulls the application image pinned to your app release
5. Starts omnideck and confirms that it is healthy

Setup can take several minutes. Agent Dash remains playable while the runtime is prepared. If Windows shows **Restart needed**, select **Restart now**; omnideck reopens and continues setup automatically after you sign back in.

<h3 id="connect-a-model">3. Connect a model</h3>

When the app reports that omnideck is ready, select **Open omnideck**. The workbench setup guides you through:

1. **Adding an LLM provider** — OpenAI, Anthropic, OpenRouter, another OpenAI-compatible endpoint, or local Ollama
2. **Picking your main model** — used for chat, context compaction, and conversation titles
3. **Picking an optional vision model** — for work involving image input

Cloud providers list their available models automatically. Ollama lists the models already available on your machine.

<h3 id="open-your-workbench">4. Open your workbench</h3>

Open a new conversation and give an agent a useful job: research a question, create something you can use, or set up work you want to run again. Your conversations, agent profiles, routines, and generated files remain available when omnideck restarts or updates.

Selecting **Open omnideck** replaces the setup screen with the workbench in the same desktop window. After setup, opening the desktop app takes you straight to the workbench. If the local environment needs setup or repair, omnideck shows that flow before opening it.

<h2 id="standalone-cli">Standalone CLI</h2>

The standalone `omnideck` CLI installs and manages the same local runtime from a terminal. Desktop users do not need to install it separately because the desktop app already includes the matching CLI.

1. Follow the **[CLI installation instructions](/docs/cli-reference.html#install-the-cli)**. The Homebrew tap provides a non-preview build for macOS and Linux, while the release archive provides the current command set and Windows builds.
2. Run `omnideck` as your normal user. The first run opens guided setup and prepares Podman when needed.
3. Run `omnideck doctor` to confirm the runtime, storage, and browser interface are healthy.
4. Open the local workbench address reported by the CLI, normally `http://localhost:2337`.

See the **[CLI Reference](/docs/cli-reference.html)** for lifecycle commands, multiple instances, and non-interactive automation.

## Next steps

- [Installation guide](/install.html#install) — desktop walkthroughs for macOS, Windows, and Linux
- [Local Models](/docs/local-models.html) — run model inference locally with Ollama
- [Integrations](/docs/integrations.html) — connect Gmail, Calendar, and Drive
- [Agents](/docs/agents.html) — create and customize agent profiles
- [Routines](/docs/routines.html) — run useful work again on a schedule

<div class="callout" data-tone="info">
<strong>Privacy:</strong> omnideck does not require an omnideck account or hosted control plane. The application and its data run on your machine.
</div>
