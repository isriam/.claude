# Network Baseline Skill

A comprehensive network device baseline and comparison tool for pre/post upgrade validation.

## Quick Start

Simply tell Claude to create a baseline:

```
"Create a pre-upgrade baseline for router1.lab.local, it's a Juniper device"
```

After the upgrade:

```
"Create a post-upgrade baseline for router1.lab.local, Juniper"
```

Claude will automatically compare the baselines and generate a detailed report.

## What It Collects

### Routing Protocols
- **BGP**: Neighbors, states, prefix counts, session details
- **OSPF**: Neighbors, adjacencies, database summaries
- **IS-IS**: Adjacencies, databases
- **LDP**: Sessions and neighbors
- **RSVP**: Sessions and neighbors

### Network Discovery
- **LLDP**: Layer 2 neighbors
- **CDP**: Cisco Discovery Protocol neighbors (Cisco only)
- **ARP**: IPv4 address resolution table
- **IPv6 Neighbors**: IPv6 neighbor discovery cache

### Device State
- **Interfaces**: Status, errors, descriptions, optics
- **Routes**: Protocol-specific route counts and summaries
- **Configuration**: Full config with hash for change detection
- **System**: Version, uptime, hardware, serial numbers
- **Environment**: CPU, memory, temperature, alarms
- **Logs**: Recent system messages

## Supported Vendors

### Juniper
- MX Series (routers)
- SRX Series (firewalls)
- EX Series (switches)
- QFX Series (data center switches)

### Cisco
- Catalyst Series (switches)
- ASR Series (routers)
- ISR Series (routers)
- Nexus Series (data center)

### Fortinet
- FortiGate (firewalls)

## Output Files

All baselines are stored in: `~/.claude/baselines/{hostname}/`

### Baseline Files
- `{timestamp}-pre.json` - Pre-upgrade baseline data
- `{timestamp}-post.json` - Post-upgrade baseline data
- `{timestamp}-config.txt` - Full device configuration
- `{timestamp}-config-diff.txt` - Configuration differences (if changed)
- `{timestamp}-comparison.md` - Human-readable comparison report

## Comparison Report

The skill automatically generates a detailed comparison report with color-coded severity:

### 🔴 Critical Issues
- Neighbor/adjacency losses
- Interfaces down
- Route count drops >10%
- New critical alarms
- Major configuration changes affecting routing

### 🟡 Warnings
- Route count changes 5-10%
- New neighbors/adjacencies
- Interface state changes
- Increased error counters
- Configuration changes

### 🟢 Informational
- Route count increases
- New discovery neighbors
- Version changes (expected)
- Uptime resets (expected after reboot)

## Usage Examples

### Basic Baseline
```
"Create a baseline for core-rtr-1, Juniper, pre-upgrade"
```

### With Custom Label
```
"Create a baseline for core-rtr-1, Juniper, pre-upgrade, label it 'junos-24.2R1'"
```

### Post-Upgrade Comparison
```
"Create post baseline for core-rtr-1, Juniper"
```
→ Automatically finds the most recent pre-baseline and compares

### Manual Comparison
```
"Compare baselines for core-rtr-1"
```
→ Compares the most recent pre and post baselines

## Tips

1. **Always create pre-baseline first** - Run it right before starting maintenance
2. **Wait for convergence** - After upgrade, wait a few minutes before running post-baseline
3. **Label your baselines** - Use custom labels for specific upgrade versions
4. **Check the detailed report** - Review `comparison.md` for full analysis
5. **Keep config diffs** - Configuration diffs are saved separately for detailed review

## What Gets Compared

The skill intelligently compares:
- Neighbor/adjacency counts and states
- Route counts by protocol
- Interface states and error counters
- Configuration changes (protocol-relevant sections highlighted)
- ARP table sizes
- System alarms
- Resource utilization (CPU/memory)

## Large Output Handling

The skill automatically handles large outputs:
- **Configurations**: Saved separately, hashed for change detection, only protocol changes shown in report
- **Route Tables**: Only counts and summaries collected, not full tables
- **Logs**: Last 100 lines only

## Requirements

This skill requires:
- SSH MCP server configured and connected
- SSH access to network devices
- Appropriate user permissions to run show commands
- Desktop Commander MCP (for file operations)

## Troubleshooting

**SSH Connection Failed**
- Verify SSH MCP is configured: Check `~/.ssh/config` has the device
- Test connectivity: `ssh {hostname}` from terminal
- Check credentials and permissions

**Commands Failing**
- Some commands may not be available on all platforms
- The skill continues collecting other data even if some commands fail
- Failed commands are noted in the baseline

**No Pre-Baseline Found**
- Make sure you ran a "pre" baseline before running "post"
- Check the hostname matches exactly
- Look in `~/.claude/baselines/{hostname}/` for existing baselines

## Future Enhancements

Potential additions:
- Support for more vendors (Arista, Huawei, Nokia)
- Baseline scheduling (automated daily baselines)
- Trend analysis (compare multiple baselines over time)
- Alert thresholds (customize warning/critical levels)
- Email reports
- Integration with change management systems
