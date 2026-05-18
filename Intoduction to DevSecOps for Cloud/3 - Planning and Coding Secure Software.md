# 3 - Planning and Coding Secure Software

## Planning Secure Software

## Planning Stage Objectives

During planning, define:

- Security objectives
- Risk tolerance
- Security testing strategy
- Threat model scope and priorities

## Threat Modeling

Threat modeling is a structured process to identify threats and design mitigations before implementation.

Typical workflow:

1. Define security objectives
2. Map architecture and data flows
3. Identify threats and vulnerabilities
4. Prioritize by risk and impact
5. Implement and validate controls

Common frameworks:

- STRIDE
- DREAD
- PASTA
- OWASP risk concepts
- MITRE ATT&CK knowledge base for adversary behavior

## Cloud Threat Considerations

- Misconfiguration risk
- Identity and access abuse
- Sensitive data exposure
- Retention/governance gaps
- Shared responsibility misunderstandings

## Coding Secure Software

## Secure Coding Stage

Integrate security checks directly into developer workflow:

- Static code analysis
- Peer review
- Dependency checks
- Secure coding standards

## Code Analysis Goals

- Detect vulnerabilities early
- Improve code quality and maintainability
- Reduce technical/security debt before build/release stages

## Example Tooling Awareness

### Amazon CodeGuru

- **Reviewer:** analyzes repositories and flags quality/security patterns.
- **Profiler:** helps identify runtime inefficiencies.

### Google Cloud Code (IDE integration)

- IDE tooling to support development workflows in GCP environments.

## Quick Summary

1. Security planning begins with threat modeling and risk prioritization.
2. Secure coding combines static analysis, reviews, and standards.
3. Earlier detection significantly reduces downstream remediation cost.
