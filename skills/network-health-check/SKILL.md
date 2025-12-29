---
name: network-health-check
description: Comprehensive network infrastructure health monitoring. Monitors FortiGate firewall, Proxmox hypervisor, VMs, LXC containers, Mist WiFi AP, PiHole DNS, and device correlation. Use when checking network health, infrastructure status, or diagnosing network issues.
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

- **FortiGate Firewall** - System status, CPU, memory, WAN interfaces, sessions
- **Proxmox Hypervisor** - CPU load, memory, disk, LXC containers, VMs, NFS
- **Mist WiFi AP** - Connection status, uptime, client count, cloud monitoring
- **PiHole DNS** - DNS statistics, blocked queries, blocklist health
- **Docker Hosts** - Container health, service status
- **WireGuard VPN** - Interface status, peer connections

## Output

Color-coded status output with critical/warning alerts. Green checkmark = healthy.

## Dependencies

- Python 3.8+
- SSH access to network devices
- Inventory file: `/mnt/nas/admin/network/inventory/inventory-simple.yaml`
- Python packages: `pyyaml`, `requests`

## Exit Codes

- **0**: All checks passed (no critical issues)
- **1**: One or more critical issues detected
