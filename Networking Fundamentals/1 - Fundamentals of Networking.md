# 1 - Fundamentals of Networking

## Quick Summary

Computer networking is the practice of connecting devices so they can exchange data. Every cloud platform, Kubernetes cluster, CI/CD system, website, database, VPN, and monitoring system depends on networking.

At a high level:

```text
application data -> transport protocol -> IP packets -> frames -> physical or wireless medium
```

Networking becomes easier when you separate the problem into layers:

- What application is trying to communicate?
- Which port and protocol does it use?
- Which IP address is the destination?
- Which route sends traffic there?
- Which firewall or security rule allows or blocks it?
- Which physical or virtual network carries it?

## Why It Matters

Networking knowledge helps you:

- Design secure cloud architectures.
- Troubleshoot "service unavailable", timeout, DNS, and connection refused errors.
- Understand VPCs, subnets, route tables, NAT gateways, load balancers, and Kubernetes Services.
- Build reliable CI/CD and deployment systems.
- Communicate clearly with infrastructure, security, and platform teams.

Most production incidents eventually involve one of these questions:

- Can the client resolve the name?
- Can the client reach the IP?
- Is the port open?
- Is the application listening?
- Is a firewall, route, proxy, load balancer, or certificate blocking the request?

## Core Concepts

| Concept | Meaning |
| --- | --- |
| Node | Any device on a network, such as a laptop, server, router, VM, container host, or printer. |
| Host | A device that sends or receives application traffic. |
| Client | The side that initiates a request. |
| Server | The side that listens for requests. |
| Protocol | Rules for communication, such as HTTP, DNS, TCP, UDP, IP, or Ethernet. |
| Packet | A unit of data sent across a network layer. |
| Frame | A data unit at the data-link layer, usually Ethernet or Wi-Fi. |
| Port | A number used by TCP/UDP to identify an application on a host. |
| IP address | Logical network address used for routing. |
| MAC address | Link-layer address used on a local network segment. |
| Subnet | A range of IP addresses treated as one local network. |
| Gateway | The router used to leave the local subnet. |
| Firewall | Rules that allow or block traffic. |

## Types Of Networks

| Type | Meaning | Example |
| --- | --- | --- |
| PAN | Personal Area Network | Bluetooth between phone and earbuds. |
| LAN | Local Area Network | Office/home network. |
| WLAN | Wireless LAN | Wi-Fi network. |
| WAN | Wide Area Network | Internet or private network between regions. |
| VPN | Virtual Private Network | Encrypted tunnel over another network. |
| VPC | Virtual Private Cloud | Isolated cloud network in AWS, Azure, or GCP. |

## OSI Model

The OSI model is a learning model with seven layers.

| Layer | Name | Main Idea | Examples |
| --- | --- | --- | --- |
| 7 | Application | User-facing network protocols | HTTP, HTTPS, DNS, SMTP, SSH |
| 6 | Presentation | Data format, compression, encryption concepts | TLS, encoding |
| 5 | Session | Session management | RPC sessions, auth sessions |
| 4 | Transport | Process-to-process delivery | TCP, UDP |
| 3 | Network | Logical addressing and routing | IP, ICMP, routers |
| 2 | Data Link | Local network delivery | Ethernet, Wi-Fi, switches, MAC |
| 1 | Physical | Signals and media | Cable, radio, fiber |

Memory hook:

```text
Application -> Transport -> Network -> Data Link -> Physical
```

For practical troubleshooting, you usually think in this compressed form:

```text
App -> TCP/UDP port -> IP route -> local network -> physical/virtual link
```

## TCP/IP Model

The TCP/IP model is closer to how the internet is actually built.

| TCP/IP Layer | Similar OSI Layers | Examples |
| --- | --- | --- |
| Application | OSI 5-7 | HTTP, DNS, SSH, SMTP |
| Transport | OSI 4 | TCP, UDP |
| Internet | OSI 3 | IP, ICMP |
| Network Access | OSI 1-2 | Ethernet, Wi-Fi |

## Encapsulation

Encapsulation means each layer wraps the data from the layer above it.

Example of opening a website:

```text
HTTP request
  inside TCP segment
    inside IP packet
      inside Ethernet/Wi-Fi frame
        sent over cable or radio
```

When the destination receives it, the layers unwrap it in reverse order.

## Switching

A switch connects devices inside a LAN. It learns which MAC addresses are reachable on which ports.

Key points:

- Switches work mostly at Layer 2.
- They forward frames based on destination MAC address.
- They reduce unnecessary traffic compared with hubs.
- VLANs can split one physical switch into multiple logical networks.

Example:

```text
Laptop A -> Switch -> Laptop B
```

If both laptops are in the same subnet, traffic can stay inside the LAN without going through a router.

## Routing

A router connects different networks. It forwards packets based on destination IP address and routing table entries.

Example:

```text
Laptop -> default gateway/router -> ISP -> internet -> remote server
```

Common route table concepts:

| Term | Meaning |
| --- | --- |
| Destination | The network range the route matches. |
| Next hop | The router/interface/gateway to send matching traffic to. |
| Default route | Route used when no more specific route matches, often `0.0.0.0/0`. |
| Metric | Preference/cost used when multiple routes are possible. |

## DNS

DNS maps names to records, commonly IP addresses.

Example:

```text
www.example.com -> 93.184.216.34
```

Important DNS record types:

| Record | Purpose |
| --- | --- |
| A | Maps a name to an IPv4 address. |
| AAAA | Maps a name to an IPv6 address. |
| CNAME | Alias from one name to another name. |
| MX | Mail server for a domain. |
| TXT | Text data, often SPF/DKIM/verification records. |
| NS | Authoritative name servers for a zone. |

Common DNS troubleshooting commands:

```bash
nslookup example.com
dig example.com
dig +trace example.com
```

## DHCP

DHCP automatically gives hosts network configuration.

Typical DHCP-provided settings:

- IP address.
- Subnet mask/prefix.
- Default gateway.
- DNS servers.
- Lease duration.

Without DHCP, you usually need to configure these manually.

## NAT

Network Address Translation changes source or destination IP/port information.

Common NAT types:

| Type | Purpose |
| --- | --- |
| Source NAT | Lets private hosts access another network using a different source IP. |
| Destination NAT | Sends inbound traffic to an internal host. |
| Port forwarding | Maps traffic on one external port to an internal host and port. |

Home internet example:

```text
laptop 192.168.1.20 -> router public IP -> internet
```

Cloud example:

```text
private subnet instance -> NAT gateway -> internet
```

## Firewalls

Firewalls allow or block traffic based on rules.

Rules commonly match:

- Source IP or subnet.
- Destination IP or subnet.
- Protocol, such as TCP, UDP, or ICMP.
- Port, such as 22, 80, 443, or 5432.
- Direction: inbound or outbound.

Cloud examples:

- AWS Security Groups are stateful.
- AWS Network ACLs are stateless.
- Kubernetes NetworkPolicies control pod-to-pod or pod-to-external traffic when the CNI supports them.

## Ports And Protocols

Common ports:

| Port | Protocol | Use |
| --- | --- | --- |
| 22 | TCP | SSH |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 80 | TCP | HTTP |
| 123 | UDP | NTP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |

TCP is connection-oriented and reliable. UDP is connectionless and lower overhead.

## TCP Basics

TCP provides reliable ordered delivery.

Key features:

- Three-way handshake.
- Retransmission for lost data.
- Ordering.
- Flow control.
- Congestion control.

Three-way handshake:

```text
Client -> SYN -> Server
Client <- SYN-ACK <- Server
Client -> ACK -> Server
```

If a TCP connection fails, check:

- DNS resolution.
- Route to destination.
- Firewall rules.
- Whether the server is listening on the port.
- TLS/certificate issues if using HTTPS.

## UDP Basics

UDP sends datagrams without a connection handshake.

Used for:

- DNS.
- NTP.
- Streaming.
- VoIP.
- Some VPN protocols.
- QUIC/HTTP/3.

Benefits:

- Lower overhead.
- Good for latency-sensitive systems.
- Application can implement its own reliability if needed.

Drawbacks:

- No built-in delivery guarantee.
- No built-in ordering.
- Harder to troubleshoot with connection-oriented tools.

## HTTP And HTTPS

HTTP is the application protocol used by websites and APIs.

HTTPS is HTTP over TLS encryption.

Basic flow:

```text
browser -> DNS lookup -> TCP connection -> TLS handshake -> HTTP request -> HTTP response
```

Common HTTP status codes:

| Code | Meaning |
| --- | --- |
| 200 | Success. |
| 301/302 | Redirect. |
| 400 | Bad request. |
| 401 | Not authenticated. |
| 403 | Authenticated but not allowed, or blocked by policy. |
| 404 | Resource not found. |
| 429 | Rate limited. |
| 500 | Server error. |
| 502 | Bad gateway, often proxy/load balancer upstream issue. |
| 503 | Service unavailable. |
| 504 | Gateway timeout. |

## Load Balancing

A load balancer distributes traffic across multiple targets.

Benefits:

- High availability.
- Scaling.
- Health checks.
- TLS termination.
- Central traffic entry point.

Common types:

| Type | Layer | Use |
| --- | --- | --- |
| Layer 4 | Transport | TCP/UDP forwarding. |
| Layer 7 | Application | HTTP routing by host/path/header. |

Example:

```text
users -> load balancer -> app instance 1
                     -> app instance 2
                     -> app instance 3
```

## Proxy Basics

A proxy sits between client and server.

| Proxy Type | Meaning |
| --- | --- |
| Forward proxy | Client-side proxy used to reach external systems. |
| Reverse proxy | Server-side proxy in front of applications. |

Examples:

- Nginx as a reverse proxy.
- Corporate outbound web proxy.
- API gateway in front of services.

## Common Network Commands

```bash
# Show IP addresses
ip addr

# Show routes
ip route

# Test basic reachability
ping 8.8.8.8

# Trace network path
traceroute example.com

# Test TCP connectivity
nc -vz example.com 443

# Show listening ports
ss -tulpen

# DNS lookup
dig example.com

# HTTP request details
curl -v https://example.com
```

Windows equivalents:

```powershell
ipconfig
route print
Test-NetConnection example.com -Port 443
nslookup example.com
tracert example.com
```

## Troubleshooting Flow

Use this order to avoid guessing:

1. Confirm the exact symptom.
2. Check DNS resolution.
3. Check IP reachability.
4. Check route and gateway.
5. Check firewall/security rules.
6. Check whether the destination port is listening.
7. Check application logs.
8. Check TLS/certificate/proxy/load balancer behavior.

Example:

```text
curl says "connection timed out"
-> DNS resolved?
-> route exists?
-> firewall allows outbound and inbound?
-> server is listening?
-> load balancer health check passes?
```

## Benefits Of Layered Thinking

- You can isolate failures faster.
- You avoid blaming the wrong system.
- You can explain issues clearly to cloud/security/platform teams.
- You understand cloud networking concepts more easily.

## Drawbacks / Limitations

- The OSI model is a learning model, not a perfect real-world map.
- Modern systems blur layers through TLS termination, proxies, service meshes, VPNs, and overlays.
- Cloud provider networking has abstractions that hide physical details.
- Kubernetes adds another networking layer with pods, Services, kube-proxy or eBPF, CNI, and ingress.

## Hidden Details / Caveats

- DNS success does not prove the service is reachable.
- Ping failure does not always mean the host is down; ICMP may be blocked.
- Connection refused means the host responded, but nothing accepted the port.
- Timeout often means packets are dropped or the response cannot return.
- A firewall may allow outbound but block return traffic if it is stateless.
- A load balancer can be reachable while all backend targets are unhealthy.
- NAT can make logs show the NAT device IP instead of the original client IP unless forwarding headers or proxy protocol are used.

## Common Mistakes

| Mistake | Correct Approach |
| --- | --- |
| Troubleshooting by random command | Follow DNS -> IP -> route -> firewall -> port -> app. |
| Confusing public and private IPs | Check which network the client is on and whether routing/NAT exists. |
| Assuming DNS updates are instant | Check TTL and resolver cache. |
| Opening a port on the server but not the cloud firewall | Check both OS firewall and cloud security rules. |
| Using ping as the only test | Test the actual TCP/UDP port. |
| Ignoring return path | Routing must work in both directions. |

## Best Practices

- Document IP ranges and subnet purpose.
- Use least-privilege firewall rules.
- Prefer DNS names over hard-coded IP addresses for services that may move.
- Use private connectivity for internal services when possible.
- Monitor latency, packet loss, error rates, and connection failures.
- Keep network diagrams updated.
- Test from the same network path as the real client.

## Interview Notes

- A switch forwards frames inside a LAN using MAC addresses.
- A router forwards packets between networks using IP routes.
- DNS maps names to records such as A, AAAA, CNAME, MX, TXT, and NS.
- DHCP automatically assigns IP configuration.
- NAT translates private addresses to other addresses, often public IPs.
- TCP is reliable and connection-oriented; UDP is connectionless.
- Firewalls block or allow traffic by source, destination, protocol, port, and direction.
- `connection refused` usually means the host is reachable but the service is not listening or is rejecting.
- `timeout` often indicates packet drop, firewall block, route issue, or no return path.

## Related Topics

- [Internet Protocol (IP)](2%20-%20Internet%20Protocol%20%28IP%29.md)
- [AWS Cloud Practitioner - Storage, Networking and Database](../AWS%20Cloud%20Practitioner/2%20-%20Storage%2C%20Networking%20and%20Database.md)
- [AWS Solutions Architect - High Availability and Scalability](../AWS%20Solution%20Architect/6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md)
- [Certified Kubernetes Administrator - Services and Networking](../Certified%20Kubernetes%20Administrator/4%20-%20Services%20and%20Networking.md)
