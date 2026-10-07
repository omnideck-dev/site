+++
title    = "Getting Started"
date     = 2026-08-15
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Install the omnideck desktop app, connect an AI model, and give omnideck its first job."
order = 1
+++

omnideck is a free desktop app for macOS, Windows 11, and Linux. This page shows what you need, how setup works, and how to start your first job. If you prefer a terminal, see [Prefer a terminal?](#standalone-cli) at the end.

## What you need

- **A computer:** a Mac with Apple silicon or Intel, a Windows 11 PC, or a desktop Linux computer. x86-64 and ARM64 are both supported. You need at least 4 GB of memory. 8 GB is recommended if you want to run models on your own computer. On Linux, check the [package and library requirements](/install.html#install-linux-panel); they differ by package and architecture.
- **Permission to install software:** setup installs the parts omnideck runs on, and your computer asks you to approve that. On a Mac, that's an administrator password or Touch ID. On Windows, it's a User Account Control prompt. On Linux, it's an administrator prompt.
- **An internet connection:** the application image is about 680 MB on x86-64 or 850 MB on ARM64. A fresh setup also downloads operating-system components and Podman files, so the total can exceed 1 GB.
- **An AI model to connect:** omnideck asks for one before your first chat. Choose one of these:
  - **A cloud account:** an API key from Anthropic, OpenAI, or OpenRouter. The provider bills API use to your account with them, separately from omnideck, which is free. API access is also billed separately from any chat subscription you have with that provider. Create a key at [Anthropic](https://platform.claude.com/settings/keys), [OpenAI](https://platform.openai.com/api-keys), or [OpenRouter](https://openrouter.ai/settings/keys).
  - **A model on your computer:** install [Ollama](https://ollama.com/download) and download a model before you open omnideck. See [Local Models](/docs/local-models.html). This costs nothing per use, but it needs enough memory for the model.
  - **Another compatible server:** such as LM Studio.

You do not need an omnideck account.

<h2 id="desktop-app">Set up the desktop app</h2>

<h3 id="install-omnideck">1. Install omnideck</h3>

Open the **[install page](/install.html)** and choose your computer. It has the right download for your system and pictures of each step.

<p><a href="/install.html" role="button" data-variant="primary">Choose your download →</a></p>

<div class="callout" data-tone="warning">
<strong>Preview packages:</strong> The current macOS and Windows installers are not yet signed with a paid publisher identity, so macOS or Windows may warn you before opening them. Download only from the <a href="/install.html">official install page</a>. Each download there shows its SHA-256 fingerprint and how to check it.
</div>

<h3 id="prepare-your-machine">2. Let setup prepare your computer</h3>

Open omnideck and select **Set up omnideck**. The **Preparing your environment** screen shows the current activity and progress. Setup includes these stages:

1. **Getting your computer ready**: installs or repairs the container runtime omnideck runs in. This is where your computer asks for approval.
2. **Preparing a secure space to run in**: on macOS and Windows only.
3. **Downloading omnideck’s files**
4. **Almost ready**: final checks

Setup can take several minutes. You can play Agent Dash while you wait. If Windows shows **Restart needed**, select **Restart now**. omnideck reopens and continues after you sign back in.

If setup stops, omnideck explains the cause and shows a next step, such as approving a permission prompt or restarting Windows. Follow that step, then select **Try again** when it is offered. If it stops again, open **Technical details** and share them in the [community Slack](/community.html) or a [GitHub issue](https://github.com/omnideck-dev/omnideck/issues).

On Windows, if Technical details mention `memory.max`, follow the [tested WSL recovery steps](/install.html#windows-wsl3). Current WSL 3.0.1 and Podman 6.0.2 can require this explicit configuration change before setup can finish.

<h3 id="connect-a-model">3. Connect a model</h3>

When setup reports that omnideck is ready, select **Open omnideck**, then **Get Started**.

1. **Choose a provider.** **Cloud API** takes a key from Anthropic, OpenAI, or OpenRouter. **Ollama (local)** uses the models already downloaded in Ollama on this computer. omnideck normally fills in Ollama’s address for you. **OpenAI-compatible endpoint** works with servers such as LM Studio. Your API key is stored on your computer.
2. **Pick a main model.** It becomes the default for the built-in agents. It is also used to summarize long conversations and to title them.
3. **Pick a vision model**, for work with images. This is optional. Select **Skip — I’ll configure this later** if you don’t have one.

You can change providers and models later in **Settings**.

<h3 id="open-your-workbench">4. Start your first job</h3>

Select **Start Chatting**. Your first chat is a short welcome tour. It ends with requests you can try, such as connecting your calendar or setting up a morning summary of your inbox.

For your own first job, select **New chat** and describe what you need in plain words. For example:

- “Plan five weeknight dinners for a family of four. One of us doesn’t eat nuts. Then make one shopping list.”
- “Find this weekend’s free events at my public library and list them by day.”

omnideck keeps your conversations, agents, routines, and files when it restarts or updates. After the first setup, opening the app takes you straight to your workbench.

## Next steps

- [Integrations](/docs/integrations.html): connect Gmail, Calendar, and Drive
- [Routines](/docs/routines.html): run a job again on a schedule
- [Agents](/docs/agents.html): create agents for different kinds of work
- [Local Models](/docs/local-models.html): run models on your own computer with Ollama

<div class="callout" data-tone="info">
<strong>Privacy:</strong> omnideck does not require an omnideck account or hosted control plane. The application and its data run on your computer.
</div>

<h2 id="standalone-cli">Prefer a terminal?</h2>

The standalone `omnideck` CLI installs and manages the same omnideck from a terminal. Desktop users don’t need it, because the desktop app already includes it.

1. Follow the **[CLI installation instructions](/docs/cli-reference.html#install-the-cli)**. Use a release archive: Windows users should choose v0.11.0-beta.6; macOS and Linux users can choose stable or preview. The Homebrew tap currently installs the older v0.9.0 release, which has a different setup flow and command set.
2. Run `omnideck` as your normal user. The first run opens guided setup and prepares Podman when needed.
3. Run `omnideck doctor` to confirm the runtime, storage, and browser interface are healthy.
4. Open the local workbench address reported by the CLI, normally `http://localhost:2337`.

The CLI sizes omnideck’s container between 1 GB and 6 GB of memory based on the host. See the **[CLI Reference](/docs/cli-reference.html)** for lifecycle commands, multiple instances, and non-interactive automation.
