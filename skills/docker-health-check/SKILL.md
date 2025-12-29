---
name: docker-health-check
description: Monitor high-risk Docker container health including Squid proxy, Plex media server, Gluetun VPN, Cloudflared tunnels, and SWAG reverse proxy. Use when checking Docker container status, diagnosing container issues, or validating service health.
---

# Docker Health Check Skill

Comprehensive health check for high-risk Docker containers.

**Script Location:** `/mnt/nas/admin/network/scripts/docker-health-check.py`

## Usage

```bash
# JSON output (default)
./docker-health-check.py

# Human-readable text output
./docker-health-check.py --text
```

## Monitored Containers

- **Squid Proxy** - Container status, proxy functionality, port accessibility
- **Plex Media Server** - Service status, media library accessibility
- **Gluetun VPN** - VPN tunnel status, connection health
- **Cloudflared** - Tunnel status, endpoint connectivity
- **SWAG** - Reverse proxy status, SSL certificate health

## Features

- Container running state detection
- Service-specific health checks
- Port accessibility validation
- Critical/warning/info severity levels
- JSON and text output formats

## Dependencies

- Python 3.8+
- Inventory file: `/mnt/nas/admin/network/inventory/inventory-docker.yaml`
- Python packages: `pyyaml`, `requests`
- SSH access to Docker hosts

## Output Format

- **JSON** (default): Structured data with device health, summary, and issues
- **Text**: Human-readable output with severity indicators
