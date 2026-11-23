# Networking Changelog

## 2026-11-23 (later)

The learner found the upgraded notes hard to follow in all four areas the placement quiz had flagged. The reasons were jargon used before it was explained, no everyday analogies, and pages that were too dense. The detailed chapters stay as the full reference, and a plain-language on-ramp now comes before them.

### Created

- [0 - Networking in Plain Language](0%20-%20Networking%20in%20Plain%20Language.md): a glossary of the basic words in everyday terms, then four short parts:
  - CIDR, built up from Indian PIN codes, with an "odometer" method that starts from the easy prefixes `/8`, `/16`, `/24` and `/32`
  - Routing and longest prefix match, using an apartment mail room and a post-office sorting chart
  - Refused versus timed out, using a letter returned to sender versus one shredded by a security guard
  - DNS, TCP, TLS and HTTP, using a phone order to a shop

  Each part has worked examples and collapsed self-check questions. The chapter also has a "Small Details That Matter Later" section and links into the deep chapters.

### Updated

- [1 - Fundamentals of Networking](1%20-%20Fundamentals%20of%20Networking.md) and [2 - Internet Protocol (IP)](2%20-%20Internet%20Protocol%20%28IP%29.md): added a "start here" callout pointing to the new chapter.
- [INDEX](INDEX.md): added the new chapter as step 0 in the learning order.

- Added the overlap rule (CIDR blocks are either separate or nested, and nesting in either direction blocks peering) to "Small Details That Matter Later" in the plain-language chapter, after the learner judged a containing `/8` safe to peer with.

### To verify

- The exact `curl -v` output lines vary by curl version; the chapter says so.

## 2026-11-23

A placement quiz showed the learner assuming every subnet is a `/24`, unsure why the most specific route wins, and reading "connection refused" as a network failure. The notes stated the facts but didn't teach the mechanisms behind them, so they were upgraded before the Week 1 lesson.

### Upgraded

- [2 - Internet Protocol (IP)](2%20-%20Internet%20Protocol%20%28IP%29.md) now follows the vault's chapter structure. All the existing content is kept and reorganized under the new headings.
- Added a first-principles explanation of why addresses are grouped into blocks (route aggregation), a mental model, and the history from classful addressing through CIDR, RFC 1918 and NAT, to IPv4 exhaustion and IPv6, with a diagram.
- Added a four-step method for working out any CIDR block by hand (size, block size, range, membership), the binary view that explains it, more worked examples, the "256 minus block size" mask shortcut, splitting and aggregation, and an extended table of prefix sizes.
- Added how a host decides between local delivery and the gateway, with a diagram, and why the reason for longest prefix match matters, including VPC gateway endpoints.
- Added a VPC address plan with room to grow (`/16` split into a `/18` per Availability Zone and a `/20` per tier), with a diagram, plus Kubernetes Pod and Service ranges for kubeadm and EKS.
- Added commands: `ip -br addr`, `ip route get`, a Python `ipaddress` check, and `aws ec2 describe-subnets` with `AvailableIpAddressCount`.
- Replaced "Hidden Details / Caveats" with "Small Details That Matter Later". The original bullets are kept, and new ones cover alignment, mid-block `.0` and `.255` addresses, AWS's five reserved addresses and size limits, Amazon DNS addresses, the metadata address, Docker's default bridge range, `/31` and `/32`, and public IPv4 pricing.
- Added "Common Misunderstandings", extra failure modes and debugging rows, a three-step analysis method (arithmetic, then routing, then policy), exam relevance, a chapter summary, and ten questions with collapsed answers.
- [1 - Fundamentals of Networking](1%20-%20Fundamentals%20of%20Networking.md): added "What a connection attempt can return" under "TCP Basics". It covers SYN-ACK, RST or nothing, who sends a reset, and why AWS security groups and NACLs cause timeouts, never refusals. Renamed "Hidden Details / Caveats" to "Small Details That Matter Later" and added how an error shows how far a request got (DNS, TCP, TLS, HTTP), plus the fact that cloud firewalls drop silently.

### To verify against current docs

- AWS public IPv4 pricing, VPC secondary CIDR quotas, the default IPv6 block sizes for VPCs and subnets, how AWS treats a misaligned CIDR, and EKS options for Pod address space (secondary CIDRs, `100.64.0.0/10`, prefix delegation).

### Still missing

- [1 - Fundamentals of Networking](1%20-%20Fundamentals%20of%20Networking.md) has not yet been rebuilt to the full chapter structure. NAT, DNS, ports and the request lifecycle need the same depth before the Week 1 Friday and Week 2 lessons.
- This topic has no roadmap, practice-question file, cheatsheet or glossary yet.
