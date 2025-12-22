# Claude Code Python Virtual Environment

This is a shared Python virtual environment used by Claude Code for executing Python scripts and importing modules.

## Purpose

Claude Code uses this virtual environment whenever it needs to run Python code - whether for custom skills, one-off scripts, or any Python execution during conversations. This provides:

- **Consistent environment** - All Python execution uses the same package versions
- **Isolation** - Won't interfere with system Python or other projects
- **Convenience** - Packages installed once are available for all Claude Code tasks

See `~/.claude/CLAUDE.md` for integration details and usage guidelines.

## Installed Packages

Core packages currently installed:
- **odfpy** - LibreOffice Calc ODS file parsing
- **pandas** - Data analysis and manipulation
- **requests** - HTTP library for web requests
- **matplotlib** - Plotting and visualization
- **numpy** - Numerical computing (dependency of pandas/matplotlib)

## Usage

### In Python Scripts

**Option 1: Direct venv Python (recommended)**
```python
#!/home/jeremy/.claude/venv/bin/python3

# Your code here
import pandas as pd
```

**Option 2: Add to sys.path**
```python
#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/jeremy/.claude/venv/lib/python3.12/site-packages')

# Your code here
import pandas as pd
```

### Installing New Packages

To add a package for Claude Code to use:
```bash
~/.claude/venv/bin/pip install <package-name>
```

Example:
```bash
~/.claude/venv/bin/pip install beautifulsoup4 lxml
```

### Listing Installed Packages

```bash
~/.claude/venv/bin/pip list
```

### Upgrading Packages

```bash
~/.claude/venv/bin/pip install --upgrade <package-name>
```

## Maintenance

### Recreating the venv

If something goes wrong, you can recreate it:
```bash
rm -rf ~/.claude/venv
python3 -m venv ~/.claude/venv
~/.claude/venv/bin/pip install --upgrade pip setuptools wheel
~/.claude/venv/bin/pip install odfpy pandas requests matplotlib
```

### Checking Python Version

```bash
~/.claude/venv/bin/python3 --version
```

## Notes

- This venv is isolated from your system Python
- It won't interfere with other Python projects
- All Claude Code Python execution should use this venv for consistency
- If you need different package versions for a specific project, create a separate venv for that project
- Claude Code will reference this venv automatically for Python tasks
