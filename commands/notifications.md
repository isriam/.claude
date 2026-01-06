<!--
=============================================================================
NOTIFICATION WEBHOOK TOGGLE
=============================================================================

WHAT THIS DOES:
  Toggles n8n webhook notifications on/off by creating/removing a file.
  Hooks in settings.json check for this file before sending webhooks.
  Notifications include tmux pane ID for multi-session support.

TOGGLE FILE:
  ~/.claude/notifications-enabled

WEBHOOK URL:
  https://n8n.mediaserver.me/webhook/claude-notification

EVENTS CONFIGURED (in ~/.claude/settings.json):
  - Notification: Permission prompts, idle waiting, auth events (includes tmux_pane)
  - Stop: When Claude finishes responding

PAYLOAD INCLUDES:
  - session_id: Claude session identifier
  - transcript_path: Path to session transcript (for tool use details)
  - notification_type: "permission_prompt", "idle_prompt", etc.
  - message: Human-readable notification message
  - tmux_pane: Pane ID (e.g., "%0") for sending approval keystrokes

DISCORD APPROVAL FLOW:
  1. Notification hook fires -> webhook to n8n
  2. n8n reads transcript_path via SSH to get tool details
  3. n8n sends to Discord with Approve/Deny buttons
  4. On response, n8n sends tmux keystrokes:
     - Approve: tmux send-keys -t %0 1
     - Deny: tmux send-keys -t %0 3

HOOKS LOCATION:
  ~/.claude/settings.json -> "hooks" section

CLOUDFLARE ACCESS HEADERS:
  CF-Access-Client-Id: f097c1afcbfe9729b5b771f3ad02b825.access
  CF-Access-Client-Secret: b1eb9a3385f005dda7dde299bad644b5c7cedcf182f77fd651c1c97297df49df

=============================================================================
-->

# Notification Toggle

Toggle webhook notifications on or off.

## Argument: $ARGUMENTS

If the argument is "on", create the file `~/.claude/notifications-enabled` using the Bash tool.
If the argument is "off", remove the file `~/.claude/notifications-enabled` using the Bash tool.
If no argument provided, check if the file exists and report the current status.

After making the change, confirm to the user what you did:
- "Notifications enabled" (when turned on)
- "Notifications disabled" (when turned off)
- "Notifications are currently [on/off]" (when checking status)
