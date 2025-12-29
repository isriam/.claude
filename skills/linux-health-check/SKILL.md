---
name: linux-health-check
description: Comprehensive Linux system health analysis for Ubuntu/Debian servers, VMs, and LXC containers. Monitors CPU, memory, disk, network, systemd services, security, updates, and logs. Use when checking Linux system health, diagnosing performance issues, or validating server status.
---

# Linux Health Check Skill

Comprehensive health check for Linux systems (Ubuntu/Debian VMs, LXC containers, physical servers).

**Script Location:** `/mnt/nas/admin/network/scripts/linux-health-check.py`

## Usage

```bash
# Text output (default)
./linux-health-check.py <hostname/ip>

# JSON output
./linux-health-check.py <hostname/ip> --json

# Specify SSH user
./linux-health-check.py <hostname/ip> --user root
```

## Checks Performed

### System Metrics
- **CPU**: Core count, load averages, current usage, top processes
- **Memory**: Total/used/available RAM, swap usage, top memory consumers
- **Disk**: Filesystem usage, inode usage, disk I/O stats
- **Network**: Interface status, IP addresses, traffic stats, listening ports

### Services & Processes
- **Systemd Services**: Failed services detection
- **Auto-detected Services**: Docker, PiHole, WireGuard with service-specific metrics
- **Process Health**: Zombie processes, D-state processes, hung processes

### Security & Maintenance
- **Security**: Failed SSH attempts, active sessions, sudo usage
- **Updates**: Available updates count, security updates
- **Log Analysis**: Kernel errors, OOM events, disk errors, segfaults

### Mounts
- Mount point status and accessibility (detects stale NFS mounts)

## Output Formats

- **Text** (default): Human-readable with progress indicators and severity levels
- **JSON**: Machine-readable structured data for automation/integration

## Issue Detection

- **CRITICAL**: High CPU load (>2.0/core), memory >95%, disk >95%, failed services, stale mounts
- **WARNING**: Elevated CPU (>1.0/core), memory >85%, disk >85%, swap >50%, security updates

## Dependencies

- Python 3.8+
- SSH access with key-based authentication
- Optional: `sysstat` package for disk I/O stats

