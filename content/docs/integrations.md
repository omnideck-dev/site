+++
title    = "Integrations"
date     = 2026-08-16
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Connect Gmail, Google Workspace, iCloud, and HTTP APIs so agents can read and act on them."
order = 7
+++

Integrations give agents tools for services you connect: email, calendars, Google Drive, contacts, and token-authenticated HTTP APIs. The raw credentials stay outside the agent process.

## Supported integrations

| Provider | Capabilities | Auth method |
|---|---|---|
| **Google Workspace** | Gmail, Calendar, Drive, and Contacts, selected individually | OAuth using your own Google Cloud desktop client |
| **Gmail** | Email | App-specific password |
| **iCloud** | Email and calendar | App-specific password |
| **HTTP API** | Requests to one base-URL host | Static token in a configurable request header |

## Adding an integration

Go to **Settings → Integrations** and click **Add integration**. The wizard shows the credentials and permission choices required by each provider.

### Gmail and iCloud

Both use app-specific passwords — credentials your provider issues for third-party apps, separate from your main account password. You need two-factor authentication enabled on your account.

1. **Pick your provider** — Gmail or iCloud
2. **Generate an app password** — the wizard links directly to your provider's account page:
   - Gmail: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - iCloud: [account.apple.com](https://account.apple.com/account/manage) → Sign-In and Security → App-Specific Passwords
3. **Enter your email and app password**, then choose **Read only** or **Read + Write** for each available capability.
4. Click **Verify & save**. If the provider accepts the credentials, the integration appears as **connected**.

### Google Workspace

Google Workspace uses OAuth with a desktop client you create in your own Google Cloud project. The wizard walks you through the setup:

1. **Create a Google Cloud project** — the wizard links to the Google Cloud Console
2. **Enable the APIs** — Gmail, Calendar, Drive, and People APIs
3. **Set up the Google Auth Platform** — configure the consent screen
4. **Publish the app** — this prevents a testing-mode refresh token from expiring after seven days
5. **Create a Desktop app OAuth client** — copy its Client ID and Client Secret
6. **Paste the credentials** into omnideck and authorize in the Google window that opens

Before authorization, choose which capabilities to connect and their access levels. Gmail, Calendar, and Drive support read-only or read-write access; Contacts is read-only. The wizard currently starts Gmail, Calendar, and Drive at **Read + Write**, so review the selections before continuing.

### HTTP API

Point an agent at a REST API that authenticates with a static token:

1. **Enter a base URL** — all agent requests are locked to this host
2. **Enter the header name and value template** — the defaults produce `Authorization: Bearer {token}`
3. **Enter the token**, choose read-only or read-write access, and optionally add a label
4. Click **Save**

Read-only HTTP access allows `GET`, `HEAD`, and `OPTIONS`. Read-write access also allows `POST`, `PUT`, `PATCH`, and `DELETE`.

## Permissions

Permissions are set per capability. Gmail, iCloud, and HTTP connections start at **Read only**; Google Workspace uses the defaults shown above. Open a connected integration to change each capability among **Off**, **Read**, and **Read + Write**, when the provider and granted OAuth scopes allow it.

Reducing or changing permissions updates the tools available to agents. If a Google capability was authorized with read-only scopes, broader access requires deleting the integration and adding it again with read-write selected.

## Integration status

| Status | Meaning |
|---|---|
| Connected | Broker is running and upstream auth succeeded |
| Auth failed | Provider rejected the credential — generate a fresh app password and re-add |
| Not running | omnideck could not reach or start the integration; delete and re-add it |

## Editing an integration

Open the integration in **Settings → Integrations**. You can:

- **Change its label**
- **Change permissions** for each available capability

Credentials and account identity cannot be edited in place. Delete and re-add the integration to replace them.

## Deleting an integration

Click **Delete**, then confirm. This stops its broker, removes its credentials from the vault, and removes its tools from future agent turns.

## Security model

omnideck separates credentials from agent execution:

- Credentials are encrypted with AES-256-GCM in a vault owned by a separate container user.
- The agent never receives raw credentials — it calls broker tools over a Unix socket, and the broker talks to the upstream provider.
- Tools are exposed according to the permission selected for each capability.
- HTTP credentials are only sent to the host in the configured base URL.

<div class="callout" data-tone="warn">
<strong>Treat the omnideck state volume as sensitive.</strong> It contains encrypted credential data and the local key used to decrypt it. Protect exported copies like a password-manager backup.
</div>

## Troubleshooting

**The integration shows “auth failed”**

The credentials were wrong, expired, or revoked. Generate a fresh app password (or OAuth credentials) from your provider and re-add the integration. You cannot edit credentials in place — delete and re-add.

**The integration shows “not running”**

omnideck could not reach or start it. Check the network and provider status, then delete and re-add the connection. CLI users can inspect runtime output with `omnideck logs --follow=false`.

**Settings says “Integrations unavailable”**

The app cannot reach its credential service. Restart omnideck. If you manage the runtime with the CLI, run `omnideck restart`, then inspect `omnideck logs --follow=false` if the error returns.

**An integration is connected but an agent cannot use it**

Check that the capability is not set to **Off** and that the agent has the **assistant** skill, which grants the connected-service tool categories.
