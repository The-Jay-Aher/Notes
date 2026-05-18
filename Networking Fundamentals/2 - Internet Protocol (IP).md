# 2 - Internet Protocol (IP)

## Quick Summary

Internet Protocol, usually called IP, is the addressing and routing system that lets devices send packets across networks. IP answers two major questions:

- What is the destination address?
- Which next hop should the packet use to get closer to that destination?

IP does not guarantee delivery by itself. Reliability, ordering, retries, and application behavior are handled by higher layers such as TCP or by the application.

## Why It Matters

IP knowledge is required for:

- Subnet design.
- Cloud VPC design.
- Kubernetes Service and Pod networking.
- Firewall rules.
- VPNs and private connectivity.
- Troubleshooting routing, NAT, and connectivity problems.

If you understand IP, cloud networking becomes much less mysterious.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| IP address | Logical address assigned to a network interface. |
| Network prefix | The network part of an address, such as `/24`. |
| Host portion | The part used to identify a host inside the subnet. |
| Subnet | A range of IP addresses grouped together. |
| CIDR | Notation for IP ranges, such as `10.0.1.0/24`. |
| Route | Rule that says where to send packets for a destination range. |
| Default gateway | Router used when no more specific route matches. |
| Public IP | Internet-routable address. |
| Private IP | Address reserved for internal networks. |
| NAT | Address translation, often private-to-public for outbound internet. |

## IPv4 Addressing

IPv4 uses 32-bit addresses, usually written as four decimal octets.

Example:

```text
192.168.1.25
```

Each octet ranges from 0 to 255.

```text
192      .168      .1        .25
11000000 10101000 00000001  00011001
```

## IPv6 Addressing

IPv6 uses 128-bit addresses and is written in hexadecimal groups.

Example:

```text
2001:db8:1234:abcd::10
```

Why IPv6 exists:

- IPv4 address space is limited.
- IPv6 provides a much larger address space.
- IPv6 reduces the need for NAT in many designs.
- IPv6 supports modern network features, but adoption varies by environment.

Important: IPv6 is not just "longer IPv4". It has different address types, neighbor discovery behavior, and operational patterns.

## Public And Private IPv4 Ranges

Private IPv4 ranges are not routed directly on the public internet.

| Range | CIDR | Common Use |
| --- | --- | --- |
| 10.0.0.0 - 10.255.255.255 | `10.0.0.0/8` | Large private networks and cloud VPCs. |
| 172.16.0.0 - 172.31.255.255 | `172.16.0.0/12` | Medium private networks, Docker defaults sometimes use this space. |
| 192.168.0.0 - 192.168.255.255 | `192.168.0.0/16` | Home and small office networks. |

Special ranges:

| Range | Purpose |
| --- | --- |
| `127.0.0.0/8` | Loopback; `127.0.0.1` means the local machine. |
| `169.254.0.0/16` | Link-local IPv4, often automatic fallback addressing. |
| `0.0.0.0/0` | Default route, meaning any IPv4 destination. |
| `255.255.255.255` | Limited broadcast address. |

## CIDR Notation

CIDR format:

```text
network-address/prefix-length
```

Example:

```text
192.168.1.0/24
```

This means:

- First 24 bits are the network part.
- Remaining 8 bits are host addresses.
- Total addresses: `2^8 = 256`.

For traditional IPv4 subnets, usable host count is often:

```text
2^(host bits) - 2
```

The subtraction accounts for network and broadcast addresses. Some cloud providers reserve additional addresses inside each subnet.

## Common IPv4 Prefix Sizes

| CIDR | Subnet Mask | Total Addresses | Common Use |
| --- | --- | --- | --- |
| `/32` | `255.255.255.255` | 1 | Single host route. |
| `/30` | `255.255.255.252` | 4 | Point-to-point links in traditional networks. |
| `/28` | `255.255.255.240` | 16 | Small subnet. |
| `/24` | `255.255.255.0` | 256 | Common LAN subnet. |
| `/20` | `255.255.240.0` | 4096 | Larger subnet. |
| `/16` | `255.255.0.0` | 65536 | Large private network/VPC block. |
| `/8` | `255.0.0.0` | 16777216 | Very large network range. |

Memory hook:

```text
larger prefix number = smaller network
smaller prefix number = larger network
```

Example:

- `/24` is smaller than `/16`.
- `/32` is one IPv4 address.
- `/0` means all IPv4 addresses.

## Subnetting Example

You have:

```text
10.0.0.0/16
```

You want smaller `/24` subnets:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

Each `/24` has 256 total addresses.

Example cloud layout:

| Subnet | Purpose |
| --- | --- |
| `10.0.1.0/24` | Public subnet in Availability Zone A. |
| `10.0.2.0/24` | Private app subnet in Availability Zone A. |
| `10.0.3.0/24` | Private database subnet in Availability Zone A. |
| `10.0.11.0/24` | Public subnet in Availability Zone B. |
| `10.0.12.0/24` | Private app subnet in Availability Zone B. |
| `10.0.13.0/24` | Private database subnet in Availability Zone B. |

## Route Tables

A route table decides where packets go.

Example Linux route table:

```text
default via 192.168.1.1 dev wlan0
192.168.1.0/24 dev wlan0
```

Meaning:

- Traffic for `192.168.1.0/24` stays on local Wi-Fi.
- Everything else goes to gateway `192.168.1.1`.

Route selection uses longest prefix match.

Example:

| Route | Destination Match |
| --- | --- |
| `10.0.0.0/8` | Broad match. |
| `10.10.0.0/16` | More specific. |
| `10.10.5.0/24` | Most specific. |

If traffic is going to `10.10.5.20`, the `/24` route wins because it is the most specific match.

## Default Route

The default route catches traffic that does not match a more specific route.

IPv4 default route:

```text
0.0.0.0/0
```

IPv6 default route:

```text
::/0
```

In a home network, default traffic usually goes to the router. In AWS, default traffic might go to an internet gateway, NAT gateway, transit gateway, virtual private gateway, or other target depending on subnet purpose.

## ARP

Address Resolution Protocol maps IPv4 addresses to MAC addresses on the local network.

Example:

```text
Who has 192.168.1.10?
192.168.1.10 is at aa:bb:cc:dd:ee:ff
```

ARP matters only for local link delivery. If the destination IP is outside the local subnet, the host sends the frame to the default gateway MAC address, not directly to the remote server MAC address.

Useful command:

```bash
ip neigh
```

## ICMP

ICMP is used for control and diagnostic messages.

Common examples:

- Echo request/reply, used by `ping`.
- Destination unreachable.
- Time exceeded, used by traceroute-style tools.

Important: ICMP can be blocked, rate-limited, or treated differently by networks. A failed ping does not always mean the host or service is down.

## NAT And IP

NAT changes addresses and sometimes ports.

Outbound NAT example:

```text
private host 10.0.2.15 -> NAT gateway public IP -> internet
```

Why NAT is used:

- Let private IP systems reach the internet.
- Hide internal addressing.
- Conserve IPv4 addresses.
- Publish internal services through port forwarding.

Drawbacks:

- Makes logs harder to interpret.
- Can break protocols that embed IP addresses.
- Adds state and scaling limits.
- Does not replace firewall rules.

## Public Cloud IP Design

Cloud networks usually separate:

- VPC/VNet CIDR block.
- Public subnets.
- Private application subnets.
- Private database subnets.
- Route tables.
- NAT gateways.
- Internet gateways.
- Security groups/firewall rules.

Good practice:

```text
public subnet: load balancers, NAT gateways, bastions if required
private app subnet: application servers, containers, internal services
private database subnet: databases and stateful systems
```

Avoid putting databases in public subnets unless there is a strong, reviewed reason.

## Kubernetes IP Concepts

Kubernetes commonly has multiple IP ranges:

| Range | Purpose |
| --- | --- |
| Node IP range | IPs assigned to Kubernetes nodes. |
| Pod CIDR | IPs assigned to Pods. |
| Service CIDR | Virtual IPs used by Kubernetes Services. |

Important:

- Pods need network connectivity according to the cluster networking model.
- Services provide stable virtual access to changing Pods.
- NetworkPolicies can restrict traffic if the CNI plugin supports them.
- Pod IPs are usually not stable and should not be hard-coded.

## Practical Commands

```bash
# Show addresses
ip addr

# Show routing table
ip route

# Show neighbor/ARP table
ip neigh

# Ping an IP
ping 8.8.8.8

# Trace route path
traceroute 8.8.8.8

# Test a TCP port
nc -vz 1.1.1.1 443

# Show listening TCP/UDP ports
ss -tulpen
```

## Benefits

- IP gives a common addressing system across networks.
- Routing lets networks scale beyond one LAN.
- CIDR allows flexible address allocation.
- Private addressing makes internal networks practical.
- IPv6 gives a much larger address space.

## Drawbacks / Limitations

- IPv4 address space is limited.
- NAT adds complexity and can hide the original client.
- IP alone does not guarantee delivery.
- Subnetting mistakes can cause overlapping ranges and routing failures.
- Dual-stack IPv4/IPv6 environments require careful testing.

## Hidden Details / Caveats

- Longest prefix match decides route selection.
- The default gateway must be reachable on the local subnet.
- Overlapping CIDR ranges break VPN, peering, and routing designs.
- Cloud providers may reserve addresses inside each subnet.
- Security rules and route tables both matter; fixing only one may not restore connectivity.
- `127.0.0.1` means "this same machine", not another host.
- `0.0.0.0` can mean "all interfaces" when binding a service, but `0.0.0.0/0` means "all IPv4 destinations" in routing.

## Common Mistakes

| Mistake | Why It Hurts |
| --- | --- |
| Choosing overlapping CIDRs for two VPCs | Peering/VPN routing becomes difficult or impossible. |
| Making subnets too small | You run out of addresses, especially in Kubernetes or cloud environments. |
| Putting all resources in public subnets | Increases attack surface. |
| Confusing IP reachability with app health | The port or app may still be down. |
| Hard-coding Pod IPs | Pod IPs change when Pods are recreated. |
| Assuming NAT is security | NAT hides addresses but is not a policy control by itself. |

## Best Practices

- Plan CIDR ranges before creating cloud networks.
- Leave room for future subnets and regions.
- Avoid overlap with home, office, VPN, and partner networks.
- Use private subnets for internal workloads.
- Use route tables intentionally; do not rely on defaults blindly.
- Record subnet purpose and owner.
- Test the actual port, not only ping.
- Prefer DNS names for services that may move.

## Troubleshooting

| Symptom | Likely Areas To Check |
| --- | --- |
| No route to host | Local route table, gateway, VPN/peering route, subnet config. |
| Connection timed out | Firewall drop, no return path, wrong route, service blocked. |
| Connection refused | Destination reachable, but service not listening or rejecting. |
| DNS resolves to wrong IP | DNS record, cache, split-horizon DNS, wrong environment. |
| Works from one subnet but not another | Route table, security rules, NACL/firewall, NAT path. |
| Works by IP but not by name | DNS issue. |
| Works by name but app fails | Port, protocol, TLS, authentication, or app issue. |

## Interview Notes

- IPv4 is 32-bit; IPv6 is 128-bit.
- CIDR `/24` means 24 network bits and 8 host bits.
- Private IPv4 ranges are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
- `0.0.0.0/0` is the IPv4 default route.
- Route tables use longest prefix match.
- ARP maps IPv4 addresses to MAC addresses on the local network.
- NAT translates addresses and sometimes ports.
- Public IPs are internet-routable; private IPs are for internal networks.

## Related Topics

- [Fundamentals of Networking](1%20-%20Fundamentals%20of%20Networking.md)
- [AWS Cloud Practitioner - Storage, Networking and Database](../AWS%20Cloud%20Practitioner/2%20-%20Storage%2C%20Networking%20and%20Database.md)
- [AWS Solutions Architect - High Availability and Scalability](../AWS%20Solution%20Architect/6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md)
- [Certified Kubernetes Administrator - Services and Networking](../Certified%20Kubernetes%20Administrator/4%20-%20Services%20and%20Networking.md)
