+++
title    = "Integrations"
date     = 2025-06-01
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Connect Gmail, Calendar, Drive, and other services so agents can read and act on them."
order = 7
+++

Integrations give the agent access to external services — email, calendar, and (in future versions) more. Each integration becomes a set of agent tools the agent can call by name.

## Supported integrations

| Provider | Capabilities |
|---|---|
| **Gmail** | Read email, search messages, send email, move messages |
| **iCloud** | Read email (IMAP), send email (SMTP), read calendar (CalDAV) |

More integrations — Drive, Notion, Slack, and others — are planned.

## Adding an integration

Go to **Settings → Integrations** in the web UI and click **Add Integration**.

1. **Pick your provider** — Gmail or iCloud
2. **Generate an app password** — the wizard links directly to your provider's app-passwords page. You must use an app-specific password, not your main account password.
   - Gmail: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - iCloud: [appleid.apple.com](https://appleid.apple.com) → Sign-In and Security → App-Specific Passwords
3. **Enter your email and app password** and click Save
4. Omnideck verifies the credentials by connecting to the provider. If they're accepted, the integration shows as **connected**.

## Write access

By default, integrations are read-only — the agent can read messages and events but can't send email or modify calendar entries. This is a deliberate safe default.

To allow writes, open the integration in **Settings → Integrations** and enable **Allow writes**. Omnideck will restart the broker process briefly (~1–3 seconds) and the integration shows as connected again.

With writes enabled, the agent gains tools for sending email, moving messages, and (for iCloud) creating or modifying calendar events.

## Integration status

| Status | Meaning |
|---|---|
| Connecting | Broker is starting; verifying credentials with the provider |
| Connected | Broker is running and upstream auth succeeded |
| Auth failed | Provider rejected the credential — generate a fresh app password and re-add |
| Not running | Broker crashed three times; check `omnideck logs` for details |

## Editing an integration

Open the integration in **Settings → Integrations**. You can:

- **Change the label** — cosmetic only, no reconnect needed
- **Toggle Allow writes** — the broker respawns briefly to pick up the new setting

You cannot change the email address or integration ID after creation — delete and re-add instead.

## Deleting an integration

Click **Delete** on the integration. This stops the broker, removes the encrypted credentials, and removes the integration's tools from the agent immediately.

## Security model

Credentials are stored in an encrypted vault inside the container and are never accessible to the agent:

- Credentials are encrypted with AES-256-GCM and stored at `/var/lib/computron/vault/` inside the container. This directory is owned by a separate OS user that the agent cannot read.
- The agent never receives raw credentials — it calls broker tools over a Unix socket, and the broker talks to the upstream provider.
- The broker wipes credentials from its process environment immediately after connecting to the provider, so they don't appear in process listings.
- Write tools are hidden from the agent's tool registry when writes are disabled, so the agent can't attempt writes even indirectly.

<div class="callout" data-tone="warn">
<strong>Backup security:</strong> The <code>~/Omnideck/.state</code> directory contains the vault master key alongside the encrypted credentials. Treat backups of this directory the same way you'd treat a password manager export — keep them encrypted and access-controlled.
</div>

## Troubleshooting

**Integration shows "auth failed" shortly after adding**

The app password was wrong, expired, or revoked. Generate a fresh app password from your provider's app-passwords page and re-add the integration. You cannot edit credentials in place — delete and re-add.

**Integration shows "not running"**

The broker crashed repeatedly before completing its initial handshake. Check `omnideck logs` for lines tagged with the integration name — common causes are a network firewall blocking outbound IMAP/SMTP/CalDAV connections, or the provider being temporarily unavailable.

**"Integrations unavailable" in the Settings tab**

The app can't reach the credential vault supervisor. Check `omnideck logs` for `[supervisor]` errors. If the container was stopped uncleanly, `omnideck restart` usually resolves it.

**The agent says it can't list emails but the integration shows "connected"**

Email servers sometimes drop idle connections after 10–30 minutes. Omnideck reconnects automatically. Check `omnideck logs` for a reconnect message — if the reconnect succeeded, the next agent call will work. If the reconnect failed, treat it as a real network issue.
