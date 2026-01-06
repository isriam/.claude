<!--
=============================================================================
NOTIFICATION WEBHOOK TOGGLE
=============================================================================

WHAT THIS DOES:
  Toggles n8n webhook notifications on/off by creating/removing a file.
  Hooks in settings.json check for this file before sending webhooks.

TOGGLE FILE:
  ~/.claude/notifications-enabled

WEBHOOK URL:
  https://n8n.mediaserver.me/webhook/claude-notification

EVENTS CONFIGURED (in ~/.claude/settings.json):
  - Notification: Permission prompts, idle waiting, auth events
  - Stop: When Claude finishes responding

HOOKS LOCATION:
  ~/.claude/settings.json → "hooks" section

TO MODIFY HOOKS:
  1. Edit ~/.claude/settings.json
  2. Find the "hooks" section
  3. Change the webhook URL or add/remove events
  4. Restart Claude for changes to take effect

TO ADD MORE EVENTS:
  Available events: Notification, PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd

  Example - add PreToolUse for Bash commands:
  "PreToolUse": [{
    "matcher": "Bash",
    "hooks": [{
      "type": "command",
      "command": "[ -f ~/.claude/notifications-enabled ] && curl -s -X POST https://n8n.mediaserver.me/webhook/claude-notification -H 'Content-Type: application/json' -H 'CF-Access-Client-Id: YOUR_ID' -H 'CF-Access-Client-Secret: YOUR_SECRET' -d \"$(cat)\" || true"
    }]
  }]

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
