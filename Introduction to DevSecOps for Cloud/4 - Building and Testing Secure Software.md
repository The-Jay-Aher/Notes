# 4 - Building and Testing Secure Software

## Quick Summary

Build and test stages turn source code into artifacts and verify them. In DevSecOps, these stages also check code, dependencies, containers, infrastructure definitions, secrets, and runtime behavior before release.

## Build Stage Security Activities

Common checks:

- SAST.
- SCA/dependency scanning.
- Secret scanning.
- IaC scanning.
- Container image scanning.
- License checks.
- SBOM generation.
- Artifact signing/provenance.
- Reproducible build controls where required.

## SAST

Static Application Security Testing analyzes source code or compiled code without running the application.

Finds examples:

- Injection patterns.
- Hard-coded secrets.
- Unsafe deserialization.
- Path traversal.
- Weak crypto usage.
- Missing validation patterns.

Benefits:

- Runs early.
- Fits pull requests.
- Gives line-level feedback.

Limitations:

- False positives.
- Misses runtime configuration issues.
- Misses many business logic flaws.

## SCA

Software Composition Analysis checks third-party dependencies.

It helps answer:

- Which packages are used?
- Which versions are vulnerable?
- Which licenses are present?
- Are transitive dependencies risky?

Important: dependency scanning should use lockfiles where possible so it scans actual resolved versions.

Common files:

- `package-lock.json`
- `yarn.lock`
- `poetry.lock`
- `requirements.txt`
- `Pipfile.lock`
- `pom.xml`
- `build.gradle`
- `go.sum`

## CVE And CVSS Basics

| Term | Meaning |
| --- | --- |
| CVE | Public identifier for a known vulnerability. |
| CVSS | Scoring system for vulnerability severity. |
| EPSS | Estimate of likelihood that a vulnerability is exploited in the wild. |
| CPE/package metadata | Helps scanners map software to vulnerabilities. |

Do not prioritize only by CVSS. Consider:

- Is the vulnerable code reachable?
- Is the service internet-facing?
- Is there an exploit?
- Is a fix available?
- Is compensating control present?
- Is the dependency used in production?

## SLSA And Supply Chain Security

SLSA focuses on software supply chain integrity.

Supply chain risks include:

- Compromised dependencies.
- Tampered build artifacts.
- Untrusted build scripts.
- Stolen CI/CD credentials.
- Malicious package updates.
- Unreviewed release changes.

Controls:

- Source control protections.
- Reviewed build definitions.
- Isolated build environments.
- Artifact provenance.
- Signing.
- Dependency pinning.
- Least-privilege CI tokens.

## Container Image Scanning

Container scans check:

- OS packages.
- Language dependencies.
- Known vulnerabilities.
- Misconfigurations.
- Running as root.
- Exposed secrets.

Good practices:

- Use minimal base images.
- Keep base images updated.
- Do not put secrets in images.
- Run as non-root where possible.
- Pin base image versions/digests for sensitive builds.

## DAST

Dynamic Application Security Testing tests a running application from the outside.

Finds examples:

- Some injection vulnerabilities.
- Authentication/session issues.
- Security header issues.
- Exposed paths.
- Misconfiguration visible over HTTP.

Benefits:

- Tests runtime behavior.
- Good for staging environments.

Limitations:

- Needs a running app.
- Authenticated scanning is harder.
- Can be noisy or disruptive.
- Does not see source code.

## OWASP ZAP

OWASP ZAP is a popular web application security testing tool often used for DAST-style checks.

Common uses:

- Baseline scans.
- Active scans in safe test environments.
- API scanning.
- Manual proxy testing.

Warning: active scans can send potentially disruptive payloads. Run them only against approved environments.

## Test Stage Security Activities

Security tests can include:

- Auth tests.
- Authorization tests.
- API contract tests.
- Negative tests for invalid input.
- Rate-limit tests.
- Security header tests.
- TLS configuration checks.
- DAST.
- Container runtime tests.

## Benefits

- Catches many issues before release.
- Creates repeatable evidence.
- Gives developers fast feedback.
- Improves supply chain visibility.

## Drawbacks / Limitations

- Tool results need triage.
- DAST can be slow and environment-dependent.
- SAST and SCA can be noisy.
- CI/CD credentials and runners become high-value assets.
- Passing scans does not prove an app is secure.

## Hidden Details / Caveats

- A vulnerability in a dev-only dependency may have different risk than one in production.
- Scanners can miss vulnerabilities in custom business logic.
- Build artifacts should be immutable after creation.
- Security tools need baselines and exception handling.
- SBOM is useful only if it is accurate and connected to vulnerability response.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Running scans only before production | Run important checks in PR/CI. |
| Treating all findings equally | Prioritize by exploitability and exposure. |
| No owner for findings | Assign owners and SLA. |
| Scanning source but not containers/IaC | Cover the deployment artifact and infrastructure. |
| DAST against production without approval | Use safe staging targets. |

## Interview Notes

- SAST analyzes code without running it.
- SCA analyzes dependencies and licenses.
- DAST tests a running application externally.
- CVSS is severity, not the full priority decision.
- SLSA focuses on supply chain integrity.
- SBOM lists software components.

## Related Topics

- [Planning and Coding Secure Software](3%20-%20Planning%20and%20Coding%20Secure%20Software.md)
- [Releasing and Deploying Secure Software](5%20-%20Releasing%20and%20Deploying%20Secure%20Software.md)
- [Learning GitHub Actions](../Learning%20GitHub%20Actions.md)

