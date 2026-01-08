# Notification Webhook System

## Overview

Toggles n8n webhook notifications on/off by creating/removing a file.
Hooks in settings.json check for this file before sending webhooks.
Notifications include tmux pane ID for multi-session support.

## Toggle File

`~/.claude/notifications-enabled`

## Webhook URL

```
https://n8n.mediaserver.me/webhook/claude-notification
```

## Cloudflare Access Headers

```
CF-Access-Client-Id: f097c1afcbfe9729b5b771f3ad02b825.access
CF-Access-Client-Secret: b1eb9a3385f005dda7dde299bad644b5c7cedcf182f77fd651c1c97297df49df
```

## Hooks Configured (in ~/.claude/settings.json)

### Notification Hook

Fires on: Permission prompts, idle waiting, auth events

```bash
[ -f ~/.claude/notifications-enabled ] && \
PANE=$(tmux display-message -p '#{pane_id}') && \
cat | jq --arg pane "$PANE" '. + {tmux_pane: $pane}' | \
curl -s -X POST https://n8n.mediaserver.me/webhook/claude-notification \
  -H 'Content-Type: application/json' \
  -H 'CF-Access-Client-Id: ...' \
  -H 'CF-Access-Client-Secret: ...' \
  -d @- || true
```

### Stop Hook

Fires on: Claude finishes responding

Sends fixed JSON: `{"event":"stop","message":"Claude finished responding"}`

## Webhook Payload (Notification hook)

```json
{
  "session_id": "uuid",
  "transcript_path": "/path/to.jsonl",
  "cwd": "/home/claude",
  "hook_event_name": "Notification",
  "notification_type": "permission_prompt",
  "message": "Claude needs your permission to use Write",
  "tmux_pane": "%0"
}
```

## n8n Workflow: claude-notifications

### Flow

```
Webhook -> Switch (by notification_type) -> permission_prompt path:
  -> set-transcript-tail (build SSH command)
  -> debian-sandbox-ssh1 (execute: tail -n 1 transcript_path)
  -> get-tool-name (parse JSON stdout)
  -> Merge (combine with webhook data)
  -> Send message and wait for response (Discord)
  -> Switch1 (by data.approved)
  -> approve/deny (set tmux command)
  -> debian-sandbox-ssh (execute tmux send-keys)
```

### Key Nodes

1. **set-transcript-tail:**
   ```
   command = ssh claude@debian-sandbox "tail -n 1 {{ $json.body.transcript_path }}"
   ```

2. **get-tool-name:**
   Parses stdout JSON to extract tool_use details:
   - `$json.stdout.message.content[0].name` (tool name)
   - `$json.stdout.message.content[0].input` (tool parameters)

3. **Merge:**
   - Mode: Combine (merges webhook data + discord response into one item)
   - Input 0: Webhook data (has body.tmux_pane)
   - Input 1: Discord response (has data.approved)

4. **Discord message format:**
   ```
   "Claude permission prompt:
   {{ $json.stdout.message.content[0].name }}({{ $json.stdout.message.content[0].input.file_path ?? $json.stdout.message.content[0].input.command ?? '' }})"
   ```

5. **approve node:**
   ```
   command = ssh claude@debian-sandbox "tmux send-keys -t {{ $json.body.tmux_pane }} 1"
   ```

6. **deny node:**
   ```
   command = ssh claude@debian-sandbox "tmux send-keys -t {{ $json.body.tmux_pane }} Escape"
   ```

## Tmux Approval Keystrokes

Claude permission prompts accept number keys:
- `1` = Approve (once)
- `2` = Approve always (add to allowlist)
- `3` = Deny / Escape

```bash
tmux send-keys -t %0 1       # Approve in pane %0
tmux send-keys -t %0 2       # Approve always
tmux send-keys -t %0 Escape  # Deny/cancel
```

## Transcript File Format

The transcript_path points to a JSONL file. Each line is a JSON object.
The last line during a permission prompt contains the tool_use:

```json
{
  "type": "assistant",
  "message": {
    "content": [{
      "type": "tool_use",
      "name": "Write",
      "input": {
        "file_path": "/tmp/test.txt",
        "content": "..."
      }
    }]
  }
}
```

To extract:
```bash
tail -n 1 transcript.jsonl | jq '.message.content[0]'
```
