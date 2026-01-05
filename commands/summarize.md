---
description: Summarize the current conversation and save to SUMMARY.md for project continuity. Use when finishing a session or before compacting. Optionally specify a custom path after the command.
allowed-tools: Read, Write, Edit, Bash(wc:*), Bash(date:*)
---

# Summarize Conversation

Follow the detailed instructions in `~/.claude/skills/summarize-chat/SKILL.md`

**Target path:** $ARGUMENTS (default: current working directory)

- If path is a directory (or empty): save as `SUMMARY.md` in that directory
- If path is a file: save to that exact file

Examples:
- `/summarize` → `./SUMMARY.md`
- `/summarize ~/` → `~/SUMMARY.md`
- `/summarize ~/projects/myapp/` → `~/projects/myapp/SUMMARY.md`
- `/summarize ~/notes/session.md` → `~/notes/session.md`

Read the skill file first, then execute the summarization process for this conversation.
