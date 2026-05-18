# 2 - DevSecOps Fundamentals

## Quick Summary

DevSecOps fundamentals combine secure software development, application security, cloud security, CI/CD automation, and operational response. The main idea is to manage security risk throughout the software lifecycle, not only after deployment.

## Software Security In The SDLC

Traditional SDLC:

```text
requirements -> design -> code -> test -> release -> operate
```

Secure SDLC adds security activities:

```text
security requirements -> threat modeling -> secure coding -> security testing -> release review -> monitoring -> vulnerability response
```

## NIST SSDF

NIST Secure Software Development Framework (SSDF), SP 800-218, provides high-level practices for secure software development.

The SSDF groups practices into four broad areas:

| Area | Meaning |
| --- | --- |
| Prepare the Organization | Define roles, policies, tools, and secure development practices. |
| Protect the Software | Protect code, repositories, credentials, and build artifacts. |
| Produce Well-Secured Software | Design, code, review, test, and build securely. |
| Respond to Vulnerabilities | Identify, triage, fix, disclose, and learn from vulnerabilities. |

Use SSDF as a framework, not as a copy-paste checklist. Adapt it to project risk.

## Application Security

Application Security, or AppSec, focuses on reducing software vulnerabilities.

Common AppSec activities:

- Secure design review.
- Threat modeling.
- Secure code review.
- SAST.
- SCA.
- DAST.
- API security testing.
- Secrets management.
- Secure dependency management.
- Vulnerability triage.

## Security Teaming Concepts

| Term | Meaning |
| --- | --- |
| Blue team | Defends systems, monitors, detects, and responds. |
| Red team | Simulates attackers to test defenses. |
| Purple team | Collaboration between red and blue teams to improve detection and defense. |
| Security champions | Developers or engineers who help promote security practices inside teams. |

## Cloud Security Foundations

Cloud security depends heavily on configuration and identity.

Core areas:

- Identity and Access Management.
- Network segmentation.
- Encryption at rest and in transit.
- Secrets management.
- Logging and audit trails.
- Backup and recovery.
- Runtime protection.
- Patch and vulnerability management.
- Policy and compliance.

## Shared Responsibility Model

Cloud providers secure the cloud infrastructure. Customers secure what they build and configure in the cloud.

Typical customer responsibilities:

- IAM users/roles/policies.
- Network rules.
- Application code.
- Data classification.
- Encryption settings.
- OS/container patching depending on service model.
- Logging and monitoring.

Responsibility changes by service type:

| Service Model | Customer Manages More/Less |
| --- | --- |
| IaaS | More: OS, runtime, app, data, network config. |
| PaaS | Less OS/runtime work, still app/data/IAM/config. |
| SaaS | Least infrastructure work, still identity/data/config/governance. |

## CI/CD And DevSecOps Lifecycle

Security checks by pipeline stage:

| Stage | Example Checks |
| --- | --- |
| Pre-commit | Secret scanning, formatting, linting. |
| Pull request | SAST, SCA, IaC scan, unit tests, code review. |
| Build | Dependency lock, artifact build, SBOM, signing. |
| Test | DAST, API tests, container scan. |
| Release | Approval, change record, provenance, artifact promotion. |
| Deploy | Policy checks, environment protections, config verification. |
| Runtime | Logs, alerts, vulnerability monitoring, incident response. |

## Security Gates

Good gates:

- Block critical/high exploitable issues.
- Allow documented exceptions with expiry.
- Link findings to owners.
- Avoid blocking for noisy low-value alerts.
- Include fast feedback in PRs.

Bad gates:

- Fail builds for every warning.
- Produce findings nobody owns.
- Run only after release.
- Ignore context such as internet exposure or exploitability.

## Benefits

- Creates a shared language for security work.
- Makes security repeatable.
- Reduces late surprises.
- Improves incident readiness.
- Supports compliance evidence.

## Drawbacks / Limitations

- Security tools can create false positives.
- Framework adoption can become paperwork if not tied to real controls.
- Teams need training and ownership.
- Cloud security changes as services and defaults evolve.

## Hidden Details / Caveats

- Secure software requires both prevention and detection.
- CI/CD credentials are high-value targets.
- Build systems are part of the production trust chain.
- Dependency risk is not only direct dependencies; transitive dependencies matter.
- Runtime context changes priority: a critical vulnerability in an unreachable test tool is different from one in an internet-facing API.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Confusing compliance with security | Use compliance as baseline, then manage real risk. |
| Ignoring build pipeline security | Protect CI/CD credentials, runners, and artifacts. |
| No vulnerability ownership | Assign service owners and remediation SLAs. |
| One-time security review | Add continuous checks and monitoring. |
| Same gate for every app | Use risk-based policies. |

## Interview Notes

- SSDF is NIST's secure software development framework.
- AppSec focuses on application-level vulnerabilities.
- DevSecOps embeds security into CI/CD and operations.
- Cloud security depends strongly on IAM, network, encryption, logging, and configuration.
- Security gates should be risk-based and actionable.

## Related Topics

- [Planning and Coding Secure Software](3%20-%20Planning%20and%20Coding%20Secure%20Software.md)
- [Building and Testing Secure Software](4%20-%20Building%20and%20Testing%20Secure%20Software.md)

