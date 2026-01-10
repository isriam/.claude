---
name: commit
description: Git add, commit, and push all changes
allowed-tools:
  - Bash(git add:*)
  - Bash(git status:*)
  - Bash(git commit:*)
  - Bash(git push:*)
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your task

1. Stage all changes with `git add -A`
2. Create a commit with a concise, descriptive message (use ONLY the user's git identity - no AI/Claude co-authorship)
3. Push to origin

Show the proposed commit message and get user confirmation before committing.
