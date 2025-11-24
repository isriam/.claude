# Python Virtual Environment Guide for Claude Code

## Quick Reference

**Venv Location:** `~/.claude/venv`

**Install packages:**
```bash
~/.claude/venv/bin/pip install <package-name>
```

**List packages:**
```bash
~/.claude/venv/bin/pip list
```

**Use in Python scripts:**
```python
#!/home/jeremy/.claude/venv/bin/python3
```

## Why Use a Shared Venv?

✅ **Consistency** - All skills use the same packages and versions
✅ **Isolation** - Doesn't affect system Python or other projects
✅ **Simplicity** - One place to manage packages for all skills
✅ **No sudo** - Install packages without system permissions

## Common Tasks

### Adding a New Package

When you need a new Python package for a skill:
```bash
~/.claude/venv/bin/pip install package-name
```

Update CLAUDE.md to document it:
```markdown
# Python Environment for Skills
- Installed packages: odfpy, pandas, requests, matplotlib, NEW_PACKAGE
```

### Creating a New Skill with Python

1. Create skill directory:
   ```bash
   mkdir -p ~/.claude/skills/my-new-skill
   ```

2. Create Python script using venv:
   ```python
   #!/home/jeremy/.claude/venv/bin/python3
   """My new skill"""

   import requests  # Available from venv

   # Your code here
   ```

3. Make it executable:
   ```bash
   chmod +x ~/.claude/skills/my-new-skill/script.py
   ```

### Checking What's Installed

```bash
~/.claude/venv/bin/pip list
```

Sample output:
```
Package           Version
----------------- -------
matplotlib        3.10.7
numpy             2.3.4
odfpy             1.4.1
pandas            2.3.3
requests          2.32.5
...
```

### Upgrading a Package

```bash
~/.claude/venv/bin/pip install --upgrade package-name
```

### Installing from requirements.txt

If a skill provides a requirements file:
```bash
~/.claude/venv/bin/pip install -r requirements.txt
```

## Troubleshooting

### "ModuleNotFoundError"

If you get this error, the package isn't installed:
```bash
~/.claude/venv/bin/pip install missing-package-name
```

### Check Which Python is Being Used

In your script, add:
```python
import sys
print(f"Python: {sys.executable}")
```

Should show: `/home/jeremy/.claude/venv/bin/python3`

### Venv Corrupted or Broken

Recreate it:
```bash
rm -rf ~/.claude/venv
python3 -m venv ~/.claude/venv
~/.claude/venv/bin/pip install --upgrade pip
~/.claude/venv/bin/pip install odfpy pandas requests matplotlib
```

## Best Practices

1. **Always use the venv for Claude skills** - Keep skills consistent
2. **Document installed packages** - Update CLAUDE.md when adding packages
3. **Don't mix with system Python** - Keep Claude Code isolated
4. **Test after installing** - Make sure packages work before using in skills
5. **Use requirements.txt for complex skills** - Document dependencies

## Examples

### Example 1: Simple Script
```python
#!/home/jeremy/.claude/venv/bin/python3

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)
```

### Example 2: With sys.path (alternative)
```python
#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/jeremy/.claude/venv/lib/python3.12/site-packages')

import requests

response = requests.get('https://api.example.com')
print(response.status_code)
```

### Example 3: Import Custom Library + Venv Packages
```python
#!/home/jeremy/.claude/venv/bin/python3
import sys
sys.path.insert(0, '/home/jeremy/.claude/skills/my-skill')

# Import from venv
import pandas as pd

# Import custom library
from my_helper import MyClass
```

## Current Installed Packages

As of setup:
- odfpy (1.4.1) - ODS file parsing
- pandas (2.3.3) - Data analysis
- requests (2.32.5) - HTTP requests
- matplotlib (3.10.7) - Plotting
- numpy (2.3.4) - Numerical computing

Plus their dependencies (see `~/.claude/venv/bin/pip list` for full list)
