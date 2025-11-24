---
name: network-baseline
description: Create pre/post upgrade network baselines for Cisco, Juniper, and Fortinet devices. Collects OSPF, BGP, ISIS, LDP, LLDP, RSVP, interface states, and routing information. Compares pre and post snapshots to identify changes. Use when user mentions "baseline", "pre-upgrade", "post-upgrade", "snapshot comparison", or needs to validate network state before/after maintenance.
allowed-tools:
  - mcp__mcp-ssh__runRemoteCommand
  - mcp__mcp-ssh__checkConnectivity
  - mcp__desktop-commander__write_file
  - mcp__desktop-commander__read_file
  - mcp__desktop-commander__create_directory
  - mcp__desktop-commander__list_directory
---

# Network Baseline Skill

This skill creates comprehensive network device baselines and compares pre/post upgrade states.

## Workflow

1. **Gather Information from User:**
   - Device hostname or IP address
   - Vendor type: cisco, juniper, or fortinet
   - Phase: pre or post
   - Optional: custom label (e.g., "upgrade-v1.2.3")

2. **Check Connectivity:**
   - Use `mcp__mcp-ssh__checkConnectivity` to verify SSH access
   - If fails, report to user and stop

3. **Execute Baseline Collection:**
   - Run vendor-specific command sets (see below)
   - Collect all outputs into a structured JSON format
   - Save to: `~/.claude/baselines/{hostname}/{timestamp}-{phase}.json`

4. **Post-Upgrade Comparison:**
   - If phase is "post", automatically look for the most recent "pre" baseline
   - Compare key metrics and generate a detailed diff report
   - Highlight critical changes (neighbor losses, route count changes, interface down)

5. **Generate Report:**
   - Summary of collected data
   - If comparison: detailed differences with severity levels
   - Save report to: `~/.claude/baselines/{hostname}/{timestamp}-comparison.md`

## Vendor Command Sets

### Juniper (MX, SRX, EX, QFX)
Run these commands sequentially:
```
show version | no-more
show chassis hardware | no-more
show configuration | display set | no-more
show system uptime | no-more
show system alarms | no-more
show system processes extensive | no-more
show chassis routing-engine | no-more
show chassis environment | no-more
show bgp summary | no-more
show bgp neighbor | no-more
show ospf neighbor | no-more
show ospf database | no-more
show isis adjacency | no-more
show isis database | no-more
show ldp neighbor | no-more
show ldp session | no-more
show lldp neighbors | no-more
show rsvp neighbor | no-more
show rsvp session | no-more
show mpls lsp | no-more
show interfaces terse | no-more
show interfaces diagnostics optics | no-more
show route summary | no-more
show route protocol bgp terse | count | no-more
show route protocol ospf terse | count | no-more
show route protocol isis terse | count | no-more
show arp no-resolve | no-more
show ipv6 neighbors | no-more
show pfe statistics traffic | no-more
show log messages | last 100 | no-more
```

### Cisco (Catalyst, ASR, ISR, Nexus)
Run these commands sequentially:
```
terminal length 0
show version
show inventory
show running-config
show processes cpu history
show processes memory sorted
show environment all
show ip bgp summary
show ip bgp vpnv4 all summary
show ip bgp neighbors
show ip ospf neighbor
show ip ospf database
show isis neighbors
show isis database
show mpls ldp neighbor
show mpls ldp bindings summary
show lldp neighbors
show cdp neighbors detail
show mpls traffic-eng tunnels brief
show ip interface brief
show ipv6 interface brief
show interfaces status
show interfaces counters errors
show interfaces description
show ip route summary
show ipv6 route summary
show arp
show ipv6 neighbors
show ip cef summary
show mpls forwarding-table summary
show spanning-tree summary
show vlan brief
show mac address-table count
show log | tail 100
```

### Fortinet (FortiGate)
Run these commands sequentially:
```
get system status
get hardware status
show full-configuration
get system performance status
diagnose sys top 1 20
get router info bgp summary
get router info bgp neighbors
get router info ospf neighbor
get router info ospf database brief
get router info routing-table all count
get router info routing-table database
get system interface physical
get system arp
get system ipv6-neighbor-cache
diagnose ip address list
diagnose hardware deviceinfo nic
diagnose netlink interface list
diagnose debug flow trace show 100
execute log display
```

## Data Structure

Store baseline data as JSON with this structure:
```json
{
  "metadata": {
    "hostname": "device-name",
    "vendor": "juniper|cisco|fortinet",
    "phase": "pre|post",
    "timestamp": "ISO-8601 timestamp",
    "label": "optional custom label",
    "collected_by": "network-baseline skill"
  },
  "raw_outputs": {
    "command_name": "command output string",
    ...
  },
  "parsed_data": {
    "system": {
      "version": "software version string",
      "uptime": "uptime string",
      "model": "hardware model",
      "serial": "serial number"
    },
    "bgp": {
      "neighbor_count": 0,
      "neighbors": [{"peer": "x.x.x.x", "state": "Established", "prefixes": 0}]
    },
    "ospf": {
      "neighbor_count": 0,
      "neighbors": [{"neighbor_id": "x.x.x.x", "state": "Full", "interface": "ge-0/0/0"}]
    },
    "isis": {
      "adjacency_count": 0,
      "adjacencies": [{"system": "router1", "state": "Up", "interface": "ge-0/0/1"}]
    },
    "ldp": {
      "neighbor_count": 0,
      "neighbors": [{"address": "x.x.x.x", "state": "Operational"}]
    },
    "lldp": {
      "neighbor_count": 0,
      "neighbors": [{"local_port": "ge-0/0/0", "remote_system": "switch1"}]
    },
    "cdp": {
      "neighbor_count": 0,
      "neighbors": [{"device_id": "switch1", "local_port": "Gi0/0/1", "platform": "cisco"}]
    },
    "rsvp": {
      "neighbor_count": 0,
      "neighbors": [{"address": "x.x.x.x", "state": "Up"}]
    },
    "interfaces": {
      "total": 0,
      "up": 0,
      "down": 0,
      "errors": 0,
      "details": [{"name": "ge-0/0/0", "status": "up", "protocol": "up", "description": "to-router2"}]
    },
    "routes": {
      "total": 0,
      "protocols": {"bgp": 0, "ospf": 0, "isis": 0, "static": 0, "direct": 0, "connected": 0}
    },
    "arp": {
      "entry_count": 0,
      "entries": [{"ip": "x.x.x.x", "mac": "aa:bb:cc:dd:ee:ff", "interface": "ge-0/0/0"}]
    },
    "configuration": {
      "hash": "md5 hash of config",
      "line_count": 0,
      "saved_to": "path to saved config file"
    },
    "alarms": {
      "count": 0,
      "critical": 0,
      "warnings": 0
    },
    "environment": {
      "cpu_utilization": 0,
      "memory_utilization": 0,
      "temperature": "normal|warning|critical"
    }
  }
}
```

## Comparison Logic

When comparing pre vs post baselines:

### Critical Changes (RED):
- BGP neighbors down
- OSPF neighbors lost
- ISIS adjacencies down
- LDP sessions down
- Interfaces down (that were up)
- Route count decreased by >10%
- Critical alarms appeared
- Configuration changes that affect routing protocols
- ARP table size decreased by >20%

### Warning Changes (YELLOW):
- Route count changed by 5-10%
- New neighbors added
- Interface state changes (up/down transitions)
- Interface errors increased
- CPU/Memory utilization changed significantly
- ARP table size changed by 10-20%
- Configuration changes (non-routing)
- Software version changed

### Informational (GREEN):
- Route count increased
- New LLDP/CDP neighbors
- Hardware/version info
- ARP entries added
- Uptime reset (expected after upgrade)
- Minor configuration changes

### Report Format

```markdown
# Network Baseline Comparison Report

**Device:** {hostname}
**Vendor:** {vendor}
**Pre-Baseline:** {pre-timestamp}
**Post-Baseline:** {post-timestamp}

## Summary
- Critical Issues: X
- Warnings: Y
- Informational: Z

## System Changes
- Software Version: v1.2.3 → v1.3.0
- Uptime: 45 days → 5 minutes (expected after reboot)
- CPU Utilization: 15% → 18%
- Memory Utilization: 45% → 47%

## Configuration Changes
- Total lines changed: 5 additions, 2 deletions
- Critical protocol changes: None
- See detailed diff: `~/.claude/baselines/{hostname}/{timestamp}-config-diff.txt`

### Key Configuration Differences:
```
+ set protocols bgp group external neighbor 192.168.1.5
- set protocols ospf area 0.0.0.1 interface ge-0/0/5
```

## BGP Changes
### Critical
- Neighbor 192.168.1.1 state changed: Established → Idle
- Total neighbors: 10 → 9 (1 lost)

### Informational
- Neighbor 192.168.1.2 prefixes: 1000 → 1050 (+50)
- New neighbor added: 192.168.1.5 (Established, 500 prefixes)

## OSPF Changes
### Critical
- Neighbor 10.1.1.1 lost (was Full on ge-0/0/5)
- Total neighbors: 4 → 3 (1 lost)

## ISIS Changes
### Informational
- All adjacencies maintained: 2 Up

## LDP Changes
### Informational
- All sessions operational: 3 sessions

## Interface Changes
### Critical
- ge-0/0/5: up/up → down/down

### Warning
- ge-0/0/1 errors: 0 → 125 (CRC errors detected)

### Informational
- All other interfaces: stable

## Route Summary Changes
- Total routes: 15,432 → 15,380 (-52, -0.3%)
- BGP routes: 10,000 → 10,050 (+50)
- OSPF routes: 5,000 → 4,900 (-100, WARNING)
- Static routes: 432 → 430 (-2)

## ARP Table Changes
- Total entries: 1,250 → 1,248 (-2, -0.2%)
- New entries: 5
- Missing entries: 7

## Alarms/Errors
### Critical
- New alarm: Interface ge-0/0/5 is down

### Cleared
- Previous alarm cleared: Fan 2 RPM low
```

## Error Handling

- If SSH connection fails, report clearly and suggest checking SSH MCP configuration
- If a command fails, note it in the baseline but continue with other commands
- If no pre-baseline exists during post collection, create post baseline and warn user
- If parsing fails for a protocol, keep raw output and note parsing failure

## Handling Large Outputs

### Configuration Files
Configuration files can be very large (thousands of lines). Handle them specially:

1. **Save full config separately**: Store in `~/.claude/baselines/{hostname}/{timestamp}-config.txt`
2. **Generate hash**: Use MD5/SHA256 hash to detect if config changed
3. **For comparison**:
   - If hash unchanged: Report "Configuration unchanged"
   - If hash changed: Generate line-by-line diff and save to `{timestamp}-config-diff.txt`
   - Extract only protocol-related changes for the main report
   - Focus on: protocols, interfaces, routing-instances, policy-options, route-maps, access-lists

**Configuration Diff Strategy:**
- Don't include full configs in JSON baseline
- Store path to config file instead
- Only show critical protocol/routing changes in comparison report
- Make full diff available as separate file

### Route Tables
Full route tables can have hundreds of thousands of entries. Strategies:

1. **Use route summary commands**: These are already in the command sets
2. **For detailed routes**: Only collect specific protocols (BGP, OSPF)
3. **Store counts, not full tables**:
   - Total routes per protocol
   - Route table size trends
   - Sample of first 100 routes for validation
4. **For comparison**: Compare counts and statistics, not individual routes

**Route Comparison Strategy:**
- Focus on route count changes per protocol
- Flag significant decreases (>10%) as critical
- Don't try to diff individual route entries
- Use `show route summary` / `show ip route summary` for counts

## User Interaction Examples

User: "Create a baseline for router1.lab.local, it's a Juniper, pre-upgrade"
→ Collect baseline, save to `~/.claude/baselines/router1.lab.local/{timestamp}-pre.json`

User: "Create post baseline for router1.lab.local, Juniper"
→ Collect baseline, find most recent pre, compare, generate report

User: "Compare baselines for router1.lab.local"
→ Find most recent pre and post, generate comparison report

## Implementation Notes

1. Always use `mcp__desktop-commander__create_directory` to ensure baseline directory exists
2. Use ISO-8601 timestamps for filenames: `YYYY-MM-DDTHH-MM-SS`
3. Parse command outputs intelligently based on vendor format
4. Store both raw and parsed data for future analysis
5. Make comparison reports human-readable with clear severity indicators
6. If user doesn't specify phase, ask them explicitly (pre or post)
