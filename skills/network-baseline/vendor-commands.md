# Vendor-Specific Command Reference

This file contains parsing hints and command notes for the network-baseline skill.

## Juniper Command Notes

### BGP Summary
```
show bgp summary | no-more
```
Look for: "Peer" lines with State column (Established/Active/Idle)
Count: Total peers shown before table

### OSPF Neighbor
```
show ospf neighbor | no-more
```
Look for: Neighbor ID, State (Full/2-Way/etc), Interface
Count: Lines with "Full" state

### ISIS Adjacency
```
show isis adjacency | no-more
```
Look for: System name, State (Up/Down), Interface
Count: Lines with "Up" state

### LDP Neighbor
```
show ldp neighbor | no-more
```
Look for: Address, State (Operational/Non-Operational)
Count: Total neighbor lines

### LLDP Neighbors
```
show lldp neighbors | no-more
```
Look for: Local Interface, Remote System Name
Count: Total neighbor entries

### RSVP Neighbor
```
show rsvp neighbor | no-more
```
Look for: Address, State (Up/Down)
Count: Lines with "Up" state

### Interfaces
```
show interfaces terse | no-more
```
Look for: Interface name, Admin status, Link status
Count: Total interfaces, up/up count, down states

### Route Summary
```
show route summary | no-more
```
Look for: Protocol-specific route counts (BGP, OSPF, Static, Direct)
Count: Total active routes

## Cisco Command Notes

### BGP Summary
```
show ip bgp summary
```
Look for: Neighbor lines with State/PfxRcd column
Count: Total neighbors before table

### OSPF Neighbor
```
show ip ospf neighbor
```
Look for: Neighbor ID, State (FULL/2WAY/etc), Interface
Count: Lines with "FULL" state

### ISIS Neighbors
```
show isis neighbors
```
Look for: System ID, State (UP/DOWN), Interface
Count: Lines with "UP" state

### MPLS LDP Neighbor
```
show mpls ldp neighbor
```
Look for: Peer LDP Ident, State (Oper/Non-Oper)
Count: Operational neighbors

### LLDP Neighbors
```
show lldp neighbors
```
Look for: Device ID, Local Interface, Port ID
Count: Total entries

### MPLS TE Tunnels
```
show mpls traffic-eng tunnels brief
```
Look for: Tunnel name, State (up/down)
Count: Active tunnels

### Interfaces
```
show ip interface brief
```
Look for: Interface, IP-Address, Status, Protocol
Count: Total interfaces, up/up count

### Route Summary
```
show ip route summary
```
Look for: Protocol route counts
Count: Total routes

## Fortinet Command Notes

### System Status
```
get system status
```
Look for: Version, Serial Number, Model

### BGP Summary
```
get router info bgp summary
```
Look for: Neighbor, State (Established/etc)
Count: Total neighbors

### OSPF Neighbor
```
get router info ospf neighbor
```
Look for: Neighbor ID, State (Full/etc), Interface
Count: Full adjacencies

### Interfaces
```
get system interface physical
```
Look for: Interface name, link status
Count: Total interfaces, up count

### Route Count
```
get router info routing-table all count
```
Look for: Total route entries
Count: Total routes

## Common Parsing Patterns

### Neighbor States
- **Good states**: Established, Full, Up, Operational, Oper
- **Bad states**: Idle, Down, Init, Non-Operational, Active (BGP)

### Interface States
- **Up**: Both admin and link up
- **Down**: Either admin down or link down
- **Degraded**: Admin up but link down (physical issue)

### Route Count Thresholds
- Critical if change > 10%
- Warning if change > 5%
- Informational if change < 5%

## Example Output Snippets

### Juniper BGP Summary
```
Groups: 2 Peers: 4 Down peers: 0
Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State
192.168.1.1           65001      12345      12340       0       0     1d 2:30 Established
```

### Cisco OSPF Neighbor
```
Neighbor ID     Pri   State           Dead Time   Address         Interface
10.1.1.1          1   FULL/DR         00:00:35    192.168.1.1     GigabitEthernet0/0
```

### Fortinet BGP Summary
```
BGP router identifier 10.0.0.1, local AS number 65000
Neighbor        V    AS MsgRcvd MsgSent   Up/Down State
192.168.1.1     4 65001   12345   12340  01:23:45 Established
```
