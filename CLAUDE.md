# CRITICAL REQUIREMENTS - MUST FOLLOW FIRST
- **ALWAYS verify with me before making ANY changes** (commits, file modifications, etc.)
- **NEVER add Claude/AI authorship to commits** - use only user's git identity
- **ASK PERMISSION before running commands that modify the system**

# Workflow Requirements
- **Before any git operations**: Show me the exact commands you plan to run
- **Before file modifications**: Confirm the changes with me first
- **For commits**: Use simple messages with only my authorship

# System Information
<!-- Machine-specific info - update for each system -->
- OS: kde neon
- RAM: 32GB
- CPU: 8
- Architecture: 64x86
- Hostname: jw-laptop
- User: jeremy

# Python Environment
- **Shared Virtual Environment**: `~/.claude/venv`
- Claude Code uses this venv for all Python execution (skills, scripts, ad-hoc tasks)
- See `~/.claude/venv/README.md` for detailed documentation
- Installed packages: odfpy, pandas, requests, matplotlib, numpy
- To install new packages: `~/.claude/venv/bin/pip install <package-name>`
- When creating Python scripts: use `#!/home/jeremy/.claude/venv/bin/python3` shebang

# Skills Storage Locations
- **Local Skills**: `~/.claude/skills/` (standard location)
- **Github Backup**: `~/.claude/` is a git repo

# My Preferences
- I prefer tackling problems one at a time
- I'm a beginner programmer mostly using Python
- I'm a network engineer with extensive routing protocol experience
- Please verify configurations with me before making changes

# Development Philosophy

- **Simplicity**: Write simple, straightforward code
- **Readability**: Make code easy to understand
- **Performance**: Consider performance without sacrificing readability
- **Maintainability**: Write code that's easy to update
- **Testability**: Ensure code is testable
- **Reusability**: Create reusable components and functions
- **Less Code = Less Debt**: Minimize code footprint

# Coding Best Practices

- **Early Returns**: Use to avoid nested conditions
- **Descriptive Names**: Use clear variable/function names (prefix handlers with "handle")
- **Constants Over Functions**: Use constants where possible
- **DRY Code**: Don't repeat yourself
- **Functional Style**: Prefer functional, immutable approaches when not verbose
- **Minimal Changes**: Only modify code related to the task at hand
- **Function Ordering**: Define composing functions before their components
- **TODO Comments**: Mark issues in existing code with "TODO:" prefix
- **Simplicity**: Prioritize simplicity and readability over clever solutions
- **Build Iteratively**: Start with minimal functionality and verify it works before adding complexity
- **Run Tests**: Test your code frequently with realistic inputs and validate outputs
- **Build Test Environments**: Create testing environments for components that are difficult to validate directly
- **Functional Code**: Use functional and stateless approaches where they improve clarity
- **Clean Logic**: Keep core logic clean and push implementation details to the edges
- **File Organization**: Balance file organization with simplicity - use an appropriate number of files for the project scale
- **Never Lazy**: You are a senior developer, never be lazy.  Always identify proper fixes
- **Simplicity**: Again, make sure your fixes are simplistic, and only affecting code you must touch
