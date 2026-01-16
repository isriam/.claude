---
name: network-health-check
description: Comprehensive network infrastructure health monitoring. Monitors hypervisors, VMs, LXC containers, Docker hosts, and device correlation on the local network. Use when checking network health, infrastructure status, or diagnosing network issues.
---

# Network Health Check Skill

Comprehensive health check across all network infrastructure devices.

**Script Location:** `/mnt/nas/admin/network/scripts/network-health-check.py`

## Usage

```bash
# Run from skill directory
./network-health-check.py

# Or directly from scripts
/mnt/nas/admin/network/scripts/network-health-check.py
```

## Devices Monitored

Devices are defined in the inventory file. The health check dynamically reads from:
`/mnt/nas/admin/network/inventory/inventory.yml`

Typical device types include hypervisors, VMs, LXC containers, Docker hosts, network devices, and DNS servers.

## Output

Color-coded status output with critical/warning alerts. Green checkmark = healthy.

## Dependencies

- Python 3.8+
- SSH access to network devices
- Inventory file: `/mnt/nas/admin/network/inventory/inventory.yml`
- Python packages: `pyyaml`, `requests`

## Exit Codes

- **0**: All checks passed (no critical issues)
- **1**: One or more critical issues detected
