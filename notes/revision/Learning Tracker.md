---
tags:
  - study/revision
status: active
created: 2026-11-18
updated: 2026-11-23
---

# Learning Tracker

This is the memory of your learning sessions. The `teach`, `quiz` and `revise` skills read and update it, and you can edit it by hand too. Keep the table columns as they are, so the skills can parse them.

## Learner Profile

- **Current focus:** Week 1 of the [Learning Plan](Learning%20Plan.md) (23 to 29 Nov 2026): Networking I on Monday, Wednesday and Friday, Linux I on Tuesday and Thursday.
- **Goals and deadlines:** proposed, not yet confirmed: AWS SAA by late January 2027, CKA by late March 2027, capstone platform project by early May 2027. Each moved one week after the placement quiz added a Linux block.
- **Preferred session length:** assumed 60 to 75 minutes on weekdays and a 3-hour Saturday lab block; confirm.
- **Learning style:** stated on 2026-11-23: dense, jargon-heavy explanations don't land. Start with an everyday analogy, define every term before using it, teach in short chunks with a worked example after each, and keep chat explanations equally plain. Networking now starts from [0 - Networking in Plain Language](../shared-foundations/networking/0%20-%20Networking%20in%20Plain%20Language.md).
- **Known strengths:** from the resume, not yet tested in a session: CI/CD with GitHub Actions and Jenkins, Docker and ECS, CloudFormation, Ansible, Git and SCM migration, Bash, PowerShell and Python scripting. Tested on 2026-11-23: systemd basics (start versus enable, `systemctl status`).
- **Known weak areas:** tested in the placement quiz on 2026-11-23 (2.25 / 8): reading errors to locate how far a request got, CIDR sizing, longest prefix match, the order of DNS, TCP, TLS and HTTP, Linux permissions, exit codes under `set -euo pipefail`, and finding the process on a port. Not yet tested: no project experience with Kubernetes, Terraform, or Prometheus with Grafana and Loki; algorithms practice not started.

## Review Queue

Each row is something worth recalling. A correct recall moves it up one box; a miss sends it back to box 1 and adds 1 to Misses. An item with 3 or more misses gets re-taught instead of drilled again.

| Box | Review again after |
| --- | --- |
| 1 | 1 day |
| 2 | 3 days |
| 3 | 7 days |
| 4 | 16 days |
| 5 | 35 days |

| Topic | Note | What to recall | Box | Misses | Last reviewed | Next due |
| --- | --- | --- | --- | --- | --- | --- |
| Networking: TCP failure modes | [Fundamentals of Networking](../shared-foundations/networking/1%20-%20Fundamentals%20of%20Networking.md), "Hidden Details / Caveats" | What "connection refused" and "connection timed out" each prove about how far a TCP connection got, and why security groups and NACLs cause timeouts, never refusals | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Networking: CIDR sizing | [Internet Protocol (IP)](../shared-foundations/networking/2%20-%20Internet%20Protocol%20%28IP%29.md), "CIDR Notation" | Size and range of a CIDR block by the block-size method (10.0.4.0/22 is 10.0.4.0 to 10.0.7.255), and the five addresses AWS reserves in every subnet | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Networking: longest prefix match | [Internet Protocol (IP)](../shared-foundations/networking/2%20-%20Internet%20Protocol%20%28IP%29.md), "Route Tables" | Why the most specific matching route wins over 0.0.0.0/0, and how to predict the target for a destination | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Networking: request stages | [Fundamentals of Networking](../shared-foundations/networking/1%20-%20Fundamentals%20of%20Networking.md), "HTTP And HTTPS" | The order DNS, TCP, TLS, HTTP and why; naming the failed step from an error (an expired certificate is TLS; any HTTP status code means the network path worked) | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Networking: CIDR overlap and peering | [Networking in Plain Language](../shared-foundations/networking/0%20-%20Networking%20in%20Plain%20Language.md), "Small Details That Matter Later" | Can `10.0.0.0/16` peer with `10.0.128.0/17`? With `10.0.0.0/8`? Why does containment in either direction block peering (each side's `local` route claims the other's addresses)? | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Networking: firewalls see post-NAT addresses | [Networking in Plain Language](../shared-foundations/networking/0%20-%20Networking%20in%20Plain%20Language.md), Part 3 | A security group allows only the office's `/32`: who in the office can log in, who can't, and what error do the blocked people see? (The firewall sees the NAT'd public address; blocked people see a timeout.) | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Linux: file permissions | none yet (`man chmod`) | Reading a permission string: owner, then group, then others, with exactly one set applying; octal 4, 2, 1; scripts need both read and execute | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Linux: systemd and journald | none yet (`man systemctl`, `man journalctl`) | `start` versus `enable` (the `.wants` symlink); `journalctl -u`, `-b` and `-f`; `daemon-reload` after editing a unit | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Bash: exit codes and pipefail | [Bash](../shared-foundations/linux/Bash.md), "Script Header And Safety Options" | Tracing exit codes under `set -euo pipefail`: grep exits 1 when nothing matches, pipefail fails the pipeline, `set -e` stops the script; tolerating expected failures explicitly | 1 | 1 | 2026-11-23 | 2026-11-24 |
| Linux: ports and signals | none yet (`man ss`, `man 7 signal`) | Finding which process holds a port with `ss -ltnp` or `lsof -i` (not `ps`), and why SIGTERM comes before SIGKILL | 1 | 1 | 2026-11-23 | 2026-11-24 |

## Session Log

Newest first. Each entry uses this shape:

```text
### YYYY-MM-DD: Topic (teach | quiz | revise)
- Covered:
- Score:
- Misconceptions:
- Added to queue:
- Next step:
```

### 2026-11-23: CIDR in real life (teach)

- Covered: Rewrote the networking on-ramp in plain language at the learner's request: [0 - Networking in Plain Language](../shared-foundations/networking/0%20-%20Networking%20in%20Plain%20Language.md). Then CIDR sizing and range by hand, and three real-world stories: a too-wide SSH rule, EKS subnet exhaustion, and overlapping ranges (home VPN, company merger, Docker's bridge network).
- Score: `10.0.32.0/19` fully correct (8,192 addresses, ends `10.0.63.255`), with no help beyond the step prompts. Correctly reasoned that a task outside the security group's range times out, but didn't say why (silent drop) until prompted. On `/32`: right that it's one address, but missed the timeout error and NAT. On peering: answered "yes" for a `/17` inside the VPC; reasoned out the local-route mechanism; then, on the three-option question, got a) and b) right but chose c) (`/8` containing the VPC) as safe.
- Misconceptions: treats containment as compatibility for separate networks, "their range inside mine is bad, mine inside theirs is fine" (corrected: no shared address in either direction); thought subtraction had to start from the lower prefix (both routes work, both give the same free bits); didn't connect a firewall rule with NAT (the firewall sees the shared public address).
- Added to queue: CIDR overlap and peering; firewalls see post-NAT addresses.
- Learner feedback: the upgraded notes were too dense and jargon-heavy, so lead with analogies, define terms first and keep chunks short. Recorded in the learner profile. Real-world stories ("what's the use of this?") landed well; use them for each new topic.
- Next step: tomorrow's `/revise` (10 items due, including today's). Then Linux I on Tuesday. On Wednesday, Part 2 (routing) and NAT, with an explain-back of today's overlap rule as the warm-up.

### 2026-11-23: Placement quiz, networking and Linux (quiz)

- Covered: TCP failure modes, CIDR sizing, longest prefix match, the stages of an HTTPS request, Linux permissions, systemd and journald, exit codes under `set -euo pipefail`, ports and signals. Started 2026-11-18. The remaining four networking questions were skipped because no result on them could have shortened the networking block.
- Score: 2.25 / 8. Networking 1.0 / 4, Linux 1.25 / 4. By type: debugging 0.25 / 1, calculation 0 / 1, prediction 0.75 / 3, ordering 0.25 / 1, scenario 1.0 / 2.
- Misconceptions: reads "connection refused" as a network failure, when it proves the host was reached; believes NACL drops don't cause timeouts; assumes every subnet is a /24; puts TLS before TCP; places an expired certificate at DNS and an HTTP 503 at TCP; reads permissions without the owner, group, others first-match rule; predicts script behaviour from intent rather than exit codes; uses `ps` to find the owner of a port. Two patterns underneath: errors are read as "connectivity is broken" instead of "how far did the request get?", and tools are known by name from daily use without the mechanism underneath.
- Added to queue: 8 items, all in box 1, due 2026-11-24.
- Next step: Week 1 of the Learning Plan. Phase 1 grew to nine weeks with a Linux block. Note gaps found: the VPC note doesn't list the five reserved addresses or say that security groups and NACLs drop silently, and the vault has no Linux notes beyond Bash.
