+++
title    = "Slack Integration"
date     = 2026-07-18
draft    = false
template = "templates/types/docs.html"

[extra]
description = "Connect Omnideck to Slack for DMs, threads, and channel mentions — locked to your user only, with reactions, live status, and mid-response cancellation."
order = 1
+++

# Connect Slack to Omnideck

This guide gets Omnideck talking to you through Slack: DMs, threads, and any
public or private channel you invite the bot into. It only responds to you,
not to anyone else in the workspace, and you can stop it mid-response with
"stop," "cancel," or just deleting your message.

You'll do three things, in this order:

1. Set up the Slack app
2. Collect the handful of values the bridge needs
3. Paste one prompt into Omnideck, which fetches the bridge script and starts it for you

No terminal commands. No local setup on your end.

---

## Step 1: Set up the Slack app

### Create the Slack app

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and click **Create New App**.
2. Choose **From an app manifest**.
3. Select the workspace you want the bot in.
4. Paste the manifest [from this Gist](https://gist.github.com/rlnorthcutt/34a0d61db5c7dce12bc0ad5da80725f9) *(switch the editor to the **JSON** tab if it defaults to YAML).
5. Click **Next**, then **Create**.

Feel free to rename "Omni" to whatever you want your bot called first — the manifest is just a starting point.

> **Why these specific scopes and events, and nothing more:** this manifest
> only grants what the bridge script actually uses (read/post messages,
> read/write files, add reactions).  Fewer
> permissions means less exposure if a token ever leaks.

---

### Install the app to your workspace

Creating the app from a manifest doesn't install it yet — you still need to do this once.

1. In the left sidebar, go to **OAuth & Permissions**.
2. Click **Install to Workspace**.
3. Review the permissions and click **Allow**.

---

## Step 2: Get the data for the connection

### Collect your tokens

You need two tokens, from two different pages.

| Token | Where to find it | Starts with |
|---|---|---|
| Bot Token | **OAuth & Permissions** → Bot User OAuth Token | `xoxb-` |
| App Token | **Basic Information** → App-Level Tokens → **Generate Token and Scopes** → add the `connections:write` scope → **Generate** | `xapp-` |

Copy both somewhere safe for a moment — you'll hand them to Omnideck in Step 6.

---

### Get your Slack user ID

The bridge is locked down to respond to exactly one person: you. It needs
your Slack user ID to do that.

1. Click your profile picture in Slack (top right).
2. Click **Profile**.
3. Click the **More** (•••) button on your profile card.
4. Click **Copy member ID**.

You'll get something like `U0123ABC456`. That's it.

(Menu wording can shift slightly between Slack versions — if you don't see
"Copy member ID" in that exact spot, it's usually one click away in the same
profile card.)

---

### Invite the bot to any channels you want it in

The bot only sees messages in channels it's actually a member of — this is
true for public channels too, not just private ones. For each channel you
want it active in:

```
/invite @Omni
```

(swap in whatever name you gave the bot in Step 1). DMs don't need this —
you can just message the bot directly once it's running.

---

## Step 3: Set up the bridge in Omnideck

Now hand everything off to Omnideck. Paste the prompt below into Omnideck,
filling in your own values first:

```
- `<SLACK_BOT_TOKEN>` — your `xoxb-...` token from Step 3
- `<SLACK_APP_TOKEN>` — your `xapp-...` token from Step 3
- `<YOUR_SLACK_USER_ID>` — your `U...` ID from Step 4

The script itself is already linked below:
`https://gist.githubusercontent.com/rlnorthcutt/33751b3b79af10b872d65b44038e0a61/raw/slack_bridge.py`


Set up my Slack bridge. Do this:

1. Download the Python script from this URL and save it as slack_bridge.py:
   https://gist.github.com/rlnorthcutt/33751b3b79af10b872d65b44038e0a61/raw/f3932f378eb0ecdacbc1dcea2bd6e66f79ae3f45/slack_bridge.py

2. Install its dependencies (slack-bolt, slack-sdk, aiohttp) if they aren't
   already available.

3. Set these environment variables for the process:
   SLACK_BOT_TOKEN=<SLACK_BOT_TOKEN>
   SLACK_APP_TOKEN=<SLACK_APP_TOKEN>
   ALLOWED_USER_IDS=<YOUR_SLACK_USER_ID>

   Leave OMNIDECK_URL and OMNIDECK_PROFILE_ID unset unless I tell you
   otherwise — they default to this Omnideck instance and the "omnideck"
   profile.

4. Run the script so it keeps running persistently in the background (not
   just for this session) and will restart automatically if it crashes or
   this machine reboots.

5. Confirm it started successfully and tell me how to check its logs later
   if I need to.

If anything above is missing or unclear, ask me before proceeding — don't
guess at token values or skip a step.
```

Omnideck will ask you for anything you left blank. Once it confirms the
bridge is running, you're done — no separate terminal session required.

> **Keep those tokens private.** Treat `xoxb-` and `xapp-` values like
> passwords — anyone with the bot token can act as your bot in Slack.

---

### Verify it's working

Send the bot a DM, or `@Ozri` mention it in a channel you invited it to.
You should see, in order:

1. A 🤔 reaction appear on your message (it saw you)
2. A reply posted in-thread
3. A ✅ reaction replacing the 🤔 once it's done

Try sending "stop" partway through a long response — it should cancel and
show 🛑 instead of ✅. Deleting your message mid-response does the same
thing.

If none of that happens, jump to Troubleshooting below.

---

## Environment variable reference

| Variable | Required? | Purpose |
|---|---|---|
| `SLACK_BOT_TOKEN` | Yes | Bot token from Step 3 (`xoxb-...`) |
| `SLACK_APP_TOKEN` | Yes | App-level token from Step 3 (`xapp-...`) |
| `ALLOWED_USER_IDS` | Strongly recommended | Comma-separated Slack user IDs allowed to use the bot. Leave unset and *anyone* in the workspace who can DM or mention the bot gets a response. |
| `OMNIDECK_URL` | No | Defaults to `http://localhost:8080`. Only set this if Omnideck runs somewhere else. |
| `OMNIDECK_PROFILE_ID` | No | Defaults to `omnideck`. Set this if you want the bridge talking to a different agent profile. |

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Bot never replies to anything | Check the manifest's `event_subscriptions.bot_events` includes `message.channels`, `message.groups`, and `message.im`. Socket Mode being "on" isn't enough by itself — the event subscriptions have to be declared too. |
| Bot works in DMs but not in a channel | You need to `/invite` the bot to that channel (Step 5) — this applies to public channels too, not just private ones. |
| Private channel messages ignored | Confirm `groups:history` and `groups:read` are in the app's scopes, and that the bot has been invited to that channel. |
| File attachments don't come through | Confirm `files:read` and `files:write` are in the app's scopes. |
| Bot replies to people who aren't you | `ALLOWED_USER_IDS` isn't set, or has the wrong ID. Double-check Step 4. |
| Reactions (🤔/✅/🛑) don't appear but replies still work | Confirm `reactions:write` is in the app's scopes, then reinstall the app (Step 2) — Slack requires reinstalling after scopes change on an already-installed app. |
| Bot stops responding after several hours with no crash message | Check the manifest has `token_rotation_enabled: false`. Rotating tokens expire every few hours and need a refresh flow this bridge doesn't implement — with rotation off, the bot token doesn't expire on its own. |
| Bot goes offline after a machine restart | The bridge has no built-in supervisor — ask Omnideck (Step 6, item 4) to confirm it set it up to auto-restart, or check what process manager it used. |
| "Stop"/deleting a message shows 🛑 but Omnideck seems to keep working | The bridge tells Omnideck to stop server-side via `/api/chat/stop`, in addition to closing its own connection. If Omnideck doesn't have that endpoint (or it errors), you'll see a logged warning but the cancel still closes the Slack-side connection either way — worth confirming that endpoint exists on your Omnideck version. |
| Bot missed messages sent while it was restarting | Expected — this bridge is Socket Mode only, with no polling fallback, so anything sent during a genuine outage isn't retried. Short reconnects (a few seconds) are handled automatically and don't lose messages. |

---

## What this bot can and can't do

**Can:**
- Reply to DMs and thread replies
- Respond to `@mentions` in any channel it's been invited to (public or private)
- Read and forward file attachments you send it
- Post back files Omnideck generates
- Show a live "thinking" status and a done/cancelled reaction on your message
- Be stopped mid-response with "stop," "cancel," or by deleting your message

**Can't (by design, to keep this simple and locked-down):**
- Respond to anyone but you (`ALLOWED_USER_IDS`)
- React to other people's reactions, run polls, or post to Slack Lists/Canvas — none of that is wired up in this version
- Recover messages sent during an actual outage (no polling fallback)
