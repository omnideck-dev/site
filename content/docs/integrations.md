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

Go to **Settings → Integrations** and click **Add integration**. Setup has four steps: **Integration**, **Connection**, **Tools**, and **Review**. If you cancel before the last step, omnideck removes the credentials that setup saved.

### Gmail and iCloud

Both use app-specific passwords. Your provider issues these for third-party apps, separate from your main account password. You need two-factor authentication turned on for your account.

1. **Pick your provider**: Gmail or iCloud.
2. **Create an app password.** The form links to your provider's account page:
   - Gmail: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - iCloud: [account.apple.com](https://account.apple.com/account/manage) → Sign-In and Security → App-Specific Passwords
3. **Enter your email and the app password.** A connection name is optional.
4. Click **Connect**.
5. **Choose tools**, then review and click **Add integration**. See [Choosing tools](#choosing-tools).

### Google Workspace

Google Workspace uses OAuth with a desktop client you create in your own Google Cloud project. The form's **Google Cloud setup** section walks you through it:

1. **Create a Google Cloud project.** The form links to the Google Cloud Console.
2. **Enable the APIs**: Gmail, Calendar, Drive, and People.
3. **Set up the Google Auth Platform** and configure the consent screen.
4. **Publish the app.** In Testing, Google authorizations expire after seven days.
5. **Create a Desktop app OAuth client** and copy its Client ID and Client secret.
6. **Enter the account email** and, optionally, a connection name. Paste the Client ID and Client secret, then click **Authorize with Google**.
7. **Sign in to Google** in the window that opens and allow access. Then return to omnideck.
8. **Choose tools**, then review and click **Add integration**.

omnideck asks Google for access to Gmail, Calendar, Drive, and Contacts. The tools you can choose come from the access Google actually grants. If you don't allow a service, its tools don't appear.

### HTTP API

Point an agent at a REST API that authenticates with a static token:

1. **Enter a connection name and a base URL.** Agent requests are locked to this host.
2. **Enter the header name and template.** The defaults produce `Authorization: Bearer {token}`.
3. **Enter the token** and click **Connect**.
4. **Choose tools.** HTTP has one tool, **Call API**. Then review and click **Add integration**.

When **Call API** is on, agents can send read and write requests to the base URL, within what the token allows. To limit what an agent can change, use a token with read-only access at the provider.

<h2 id="choosing-tools">Choosing tools</h2>

You decide which individual tools omnideck can use with each connection. Examples are **Search email**, **Send email**, **Create calendar event**, **Delete calendar event**, and **Share Drive file**. Nothing is selected at first. omnideck can use only the tools you turn on.

Tools are grouped by service: Email, Calendar, Drive, Contacts, or API. You can search the list, use **Select all** or **Deselect all**, and see how many are selected.

For example, to let omnideck read your mail and manage your calendar without sending mail or deleting events, turn on the reading and searching email tools and the calendar tools except the delete ones. Leave **Send email** off.

To change tools later, open the integration in **Settings → Integrations** and click **Change tools**. Changes apply from the agent's next run. If you turn a tool off, calls to it are refused right away, even in a run that has already started.

## Integration status

| Status | Meaning |
|---|---|
| Connected | The integration is running and its credential was accepted |
| Auth failed | The provider rejected the credential. Update it from Connection settings |
| Not running | omnideck could not reach or start the integration. Update its connection, or remove it and add it again |

## Editing an integration

Open the integration in **Settings → Integrations**. The page lists what omnideck can do with it. You can:

- **Change tools**: turn individual tools on or off. This is available while the integration is Connected.
- **Rename** it, under **Connection settings**.
- **Update its credential**, under **Connection settings**: **Update app password** for Gmail and iCloud, **Sign in again** for Google Workspace, or **Update token** for HTTP. Your tool choices are kept.

## Removing an integration

Open **Connection settings**, click **Remove integration**, then **Confirm removal?**. This stops the integration, removes its credentials from the vault, and removes its tools from future agent runs.

## Security model

omnideck separates credentials from agent execution:

- Credentials are encrypted with AES-256-GCM in a vault owned by a separate container user.
- The agent never receives raw credentials — it calls broker tools over a Unix socket, and the broker talks to the upstream provider.
- Agents get only the tools you turned on for each integration, and omnideck checks again when each tool is called.
- HTTP credentials are only sent to the host in the configured base URL.

<div class="callout" data-tone="warn">
<strong>Treat the omnideck state volume as sensitive.</strong> It contains encrypted credential data and the local key used to decrypt it. Protect exported copies like a password-manager backup.
</div>

## Troubleshooting

**The integration shows “auth failed”**

The credential was wrong, expired, or revoked. Open the integration, then **Connection settings**, and use **Update app password**, **Sign in again**, or **Update token**. For Google, also check that the Google Cloud app is published. Authorizations from an app in Testing expire after seven days.

**The integration shows “not running”**

omnideck could not reach or start it. Check the network and the provider's status, then update the connection from **Connection settings**. If it still doesn't start, remove the integration and add it again. CLI users can inspect runtime output with `omnideck logs --follow=false`.

**Settings says “Integrations unavailable”**

The app cannot reach its credential service. Restart omnideck. If you manage the runtime with the CLI, run `omnideck restart`, then inspect `omnideck logs --follow=false` if the error returns.

**An integration is connected but an agent cannot use it**

Open the integration and check that the tool the agent needs is turned on under **What omnideck can do**. Also check that the agent has the **assistant** skill, which grants the connected-service tool categories. A run that was already going when you turned a tool on keeps its starting tools; start a new request.
