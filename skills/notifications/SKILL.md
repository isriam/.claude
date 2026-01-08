---
name: notifications
description: Toggle webhook notifications on or off
allowed-tools:
  - Bash(touch:*)
  - Bash(rm:*)
  - Bash(test:*)
  - Bash(ls:*)
---

# Notification Toggle

Toggle webhook notifications on or off.

See README.md in this directory for full system documentation.

## Argument: $ARGUMENTS

If the argument is "on", create the file `~/.claude/notifications-enabled` using the Bash tool.
If the argument is "off", remove the file `~/.claude/notifications-enabled` using the Bash tool.
If no argument provided, check if the file exists and report the current status.

After making the change, confirm to the user what you did:
- "Notifications enabled" (when turned on)
- "Notifications disabled" (when turned off)
- "Notifications are currently [on/off]" (when checking status)
