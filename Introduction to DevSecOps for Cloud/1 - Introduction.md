# 1 - Introduction

## Quick Summary

DevSecOps is the practice of integrating security into DevOps workflows. Instead of building software first and asking security to review it at the end, teams add security thinking, automation, and feedback throughout the lifecycle.

Simple idea:

```text
Security is everyone's responsibility, but it still needs ownership, standards, and automation.
```

## Why It Matters

Cloud systems change quickly:

- Infrastructure is created through APIs.
- Deployments happen frequently.
- Dependencies change constantly.
- Secrets are used across CI/CD, cloud, and applications.
- Attackers scan public cloud assets continuously.

If security is manual and late, it cannot keep up. DevSecOps makes security faster, earlier, and more repeatable.

## DevOps vs DevSecOps

| Area | DevOps | DevSecOps |
| --- | --- | --- |
| Goal | Fast and reliable delivery. | Fast, reliable, and secure delivery. |
| Security timing | Often late review. | Built into every stage. |
| Tooling | Build/test/deploy automation. | Build/test/deploy plus security automation. |
| Ownership | Dev and Ops collaboration. | Dev, Sec, and Ops collaboration. |
| Feedback | Quality and operations feedback. | Quality, operations, and security feedback. |

## Course Goal

By the end of this section, you should understand:

- What DevSecOps means.
- Why cloud changes security workflows.
- Where security controls fit in CI/CD.
- How to think about secure planning, coding, testing, releasing, deploying, monitoring, and responding.
- How tools such as SAST, SCA, DAST, IaC scanning, secret scanning, and SIEM fit together.

## Prerequisites

Recommended basics:

- Linux and command line.
- Git and pull requests.
- CI/CD fundamentals.
- Cloud basics.
- Networking basics.
- Containers and Kubernetes basics.
- Security basics such as authentication, authorization, encryption, and least privilege.

## Core Principles

| Principle | Meaning |
| --- | --- |
| Shift left | Find issues earlier in design, code, and CI. |
| Shift right | Monitor runtime behavior and learn from production. |
| Automate repeatable checks | Use pipeline controls where possible. |
| Risk-based decisions | Not every finding has the same urgency. |
| Least privilege | Give only required permissions. |
| Secure defaults | Start from safe configurations. |
| Traceability | Know what changed, who approved it, and what ran. |
| Continuous improvement | Use incidents and findings to improve controls. |

## DevSecOps Lifecycle

```text
Plan -> Code -> Build -> Test -> Release -> Deploy -> Operate -> Monitor -> Respond
```

Security examples by stage:

| Stage | Security Activities |
| --- | --- |
| Plan | Threat modeling, abuse cases, security requirements. |
| Code | Secure coding, code review, secret scanning. |
| Build | SAST, SCA, artifact signing, SBOM. |
| Test | DAST, API tests, fuzzing, security test cases. |
| Release | Risk review, approvals, artifact promotion. |
| Deploy | IaC checks, policy checks, runtime hardening. |
| Monitor | Logs, alerts, SIEM, anomaly detection. |
| Respond | Incident handling, patching, lessons learned. |

## Benefits

- Finds security issues earlier.
- Reduces manual review bottlenecks.
- Improves auditability.
- Makes security repeatable across projects.
- Helps teams respond faster to vulnerabilities.
- Encourages developers to understand security impact.

## Drawbacks / Limitations

- Tool noise can overwhelm teams.
- Security automation needs tuning.
- Developers need training, not just scanners.
- Compliance checks do not automatically mean secure systems.
- Runtime risks still exist even if CI passes.

## Hidden Details / Caveats

- "Shift left" does not remove the need for runtime monitoring.
- A scanner finding must be triaged by exploitability, exposure, and business risk.
- Secrets scanning is not enough; you also need rotation and incident response.
- DevSecOps needs policy and culture, not only tools.
- Cloud misconfiguration can be as dangerous as application code vulnerabilities.

## Common Mistakes

| Mistake | Better Approach |
| --- | --- |
| Adding many tools without ownership | Assign owners and triage rules. |
| Blocking builds for every low-risk finding | Use risk-based gates. |
| Treating security as only the security team's job | Define shared responsibilities. |
| Ignoring runtime monitoring | Add logs, alerts, and incident response. |
| Storing cloud credentials in CI variables forever | Use short-lived credentials where possible. |

## Interview Notes

- DevSecOps integrates security into DevOps pipelines and culture.
- It includes both shift-left and shift-right practices.
- Common tools include SAST, SCA, DAST, secret scanning, IaC scanning, container scanning, and SIEM.
- Security gates should be risk-based.
- Cloud DevSecOps must cover identity, network, data, runtime, and infrastructure configuration.

## Related Topics

- [Learning GitHub Actions](../Learning%20GitHub%20Actions.md)
- [Jenkins](../Jenkins/INDEX.md)
- [Terraform](../Terraform/1%20-%20Understanding%20Infrastructure%20as%20Code.md)

