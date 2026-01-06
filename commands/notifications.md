.claude/settings.json
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
  CF-Access-Client-Id: a987c1888e4f0dfa183afee90a05e468.access
  CF-Access-Client-Secret: f8fbfb8f5f19c523a2167a2d56f7fc0341781247f9ebf473a2f43b24af0a2f4b

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
