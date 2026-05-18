# 4 - Building and Testing Secure Software

## Building Secure Software

## Build Stage Security Activities

- Run static application security testing (SAST)
- Validate dependencies and third-party components
- Execute unit tests and quality gates

## SAST (Static Application Security Testing)

- White-box testing approach (source code visibility required).
- Detects security issues during development/build stages.
- Helps reduce cost of fixing vulnerabilities early.

## SCA (Software Composition Analysis)

SCA analyzes third-party/open-source dependencies for known vulnerabilities and licensing risk.

Why it matters:

- Modern apps rely heavily on external packages.
- Vulnerable dependencies can introduce critical risk.

## CVE and CVSS Basics

- **CVE:** Identifier for publicly disclosed vulnerabilities.
- **CVSS:** Severity scoring framework (for example Low/Medium/High/Critical ranges).

## Supply Chain Security Maturity (SLSA)

Higher SLSA levels indicate stronger software supply chain integrity and provenance controls.

## Testing Secure Software

## Test Stage Security Activities

- Dynamic application security testing (DAST)
- Unit/integration/security testing
- Fuzzing where relevant

## DAST (Dynamic Application Security Testing)

- Black-box approach (no source code required).
- Tests running applications in runtime context.
- Finds issues not always visible in static scans.

## OWASP and ZAP

- **OWASP Top 10:** High-risk web app vulnerability categories.
- **ZAP (Zed Attack Proxy):** Popular open-source DAST tool.

## Cloud Web Security Scanning

Cloud-native scanners can assess deployed/public web apps and provide remediation guidance.

## Quick Summary

1. Build phase emphasizes SAST + dependency security.
2. Test phase adds runtime validation through DAST/fuzzing.
3. Combining both provides stronger coverage than either approach alone.
