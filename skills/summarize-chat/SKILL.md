---
name: summarize
description: Summarize the current conversation and save to SUMMARY.md for project continuity. Use when finishing a session or before compacting. Optionally specify a custom path after the command.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Summarize Conversation

Save a structured summary of the current conversation to enable seamless project continuity.

## Usage

- `/summarize` - saves to `SUMMARY.md` in current working directory
- `/summarize ~/` - saves to `~/SUMMARY.md`
- `/summarize /path/to/dir/` - saves to `/path/to/dir/SUMMARY.md`
- `/summarize /path/to/file.md` - saves to exact file specified

**Path logic:** If argument is a directory (or empty), append `SUMMARY.md`. If argument is a file path, use it directly.

## File Structure

The summary file uses a hybrid approach with sections that get REPLACED and sections that get APPENDED:

```markdown
# Project Summary

## Current State
**Goal:** [One sentence - what we're trying to achieve]
**Status:** [Where we are right now]
**Next Step:** [Exact action to take when resuming]

## Key Decisions
- [YYYY-MM-DD] Decision and WHY it was made

## Open Tasks
- [ ] Task 1
- [ ] Task 2

## Blockers
- Active blocker (or "None" if clear)

## Session History
### YYYY-MM-DD HH:MM
1-2 sentence outcome summary
```

## Section Rules

### Current State (REPLACED each time)
- **Goal**: One sentence, the core objective
- **Status**: Brief progress indicator
- **Next Step**: The EXACT action to resume work - be specific

### Key Decisions (APPENDED, deduplicated)
- Only architectural/design decisions that affect future work
- Include the WHY, not just the what
- Skip minor implementation details
- Check for duplicates before adding

### Open Tasks (REPLACED each time)
- Active tasks only
- Remove completed items (don't track history here)
- Keep to essential items

### Blockers (REPLACED each time)
- Only active blockers
- Remove resolved ones
- Write "None" if clear

### Session History (APPENDED, pruned)
- Add new session at TOP (newest first)
- **Maximum 5 sessions** - delete oldest when adding new
- **1-2 sentences per session** - outcomes only, not process
- Format: `### YYYY-MM-DD HH:MM`

## What to Capture (High Value)

- The core goal/objective
- Architectural decisions and trade-offs (with reasoning)
- Current precise state (where exactly we stopped)
- Active blockers preventing progress
- Exact next action to resume

## What to EXCLUDE (Noise)

- Debugging attempts that went nowhere
- Every file that was touched
- Exploration/research that didn't pan out
- Conversational back-and-forth
- Minor implementation details
- Completed task history
- Obvious or trivial decisions

## Size Target

**Keep total file under 150 lines** to avoid filling context when loaded.

## Execution Steps

1. **Determine target file path**
   - If no argument provided: use `./SUMMARY.md` (current working directory)
   - If argument is a directory (ends with `/` or is an existing directory): append `SUMMARY.md`
   - If argument is a file path: use it directly

2. **Check if file exists** at target location
   - If exists: Read current contents
   - If not: Create new file with template

3. **Analyze the conversation** for:
   - Core goal/objective
   - Key decisions made (with reasoning)
   - Current state and progress
   - Open tasks remaining
   - Active blockers
   - What the next action should be

4. **Update the file**:
   - REPLACE: Current State, Open Tasks, Blockers sections
   - APPEND: New decisions to Key Decisions (check for duplicates first)
   - APPEND: New session entry to Session History (at top, prune if >5)

5. **Verify file size** - warn if approaching 150 lines

6. **Confirm to user** with brief summary of what was captured

## Template for New File

```markdown
# Project Summary

## Current State
**Goal:** [Goal from this session]
**Status:** [Current status]
**Next Step:** [Next action to resume]

## Key Decisions
- [YYYY-MM-DD] [First decision and why]

## Open Tasks
- [ ] [Task 1]

## Blockers
None

## Session History
### YYYY-MM-DD HH:MM
[Initial session summary - 1-2 sentences]
```

## Example Output

```markdown
# Project Summary

## Current State
**Goal:** Add JWT authentication to the REST API
**Status:** Login/logout endpoints complete, password reset in progress
**Next Step:** Create POST /auth/reset-password endpoint with email token flow

## Key Decisions
- [2024-01-05] Using JWT over sessions (stateless, better horizontal scaling)
- [2024-01-05] Chose bcrypt with cost factor 12 for password hashing (security/performance balance)
- [2024-01-04] Storing refresh tokens in HttpOnly cookies (XSS protection)

## Open Tasks
- [ ] Password reset endpoint
- [ ] Email verification flow
- [ ] Rate limiting on auth endpoints

## Blockers
Waiting on SMTP credentials from DevOps for email sending

## Session History
### 2024-01-05 14:30
Implemented login/logout endpoints with JWT middleware. Started password reset flow.

### 2024-01-04 10:15
Set up User model, database migrations, and bcrypt integration. Decided on JWT architecture.
```
