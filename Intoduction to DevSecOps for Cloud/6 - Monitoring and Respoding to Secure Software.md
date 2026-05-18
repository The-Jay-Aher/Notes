# 6 - Monitoring and Responding to Secure Software

## Monitoring Secure Software

## Monitoring Stage Goals

- Detect suspicious activity quickly
- Maintain visibility across systems and applications
- Reduce time to detection and response

## Logging Fundamentals

Effective logging captures:

- Events and actions
- Identity/user context
- Source and destination details
- Timestamps and outcomes

## Security Information and Event Management (SIEM)

SIEM platforms help by:

- Aggregating multi-source logs
- Enabling query/correlation
- Surfacing high-priority alerts
- Providing dashboards for incident analysis

Cloud security monitoring examples:

- AWS GuardDuty / Detective / Security Hub ecosystem
- Azure Sentinel / Defender ecosystem
- GCP Chronicle / Security Command Center ecosystem

## WAF vs RASP

- **WAF (Web Application Firewall):** Filters malicious HTTP(S) traffic at application edge.
- **RASP (Runtime Application Self-Protection):** Security controls embedded in application runtime context.

Both can be complementary.

## Responding to Security Events

## Response Stage Goals

- Contain active threats
- Eradicate root cause
- Restore services safely
- Capture lessons learned

## NIST Incident Response Lifecycle (High Level)

1. Preparation
2. Detection and analysis
3. Containment, eradication, and recovery
4. Post-incident activities

## Cloud API Security Considerations

- Authentication and authorization
- API keys/token management
- Rate limiting
- Request validation
- Encryption in transit

## Availability and DDoS Response

- Load balancing improves resilience under heavy traffic.
- DDoS protection services help absorb/mitigate attacks (for example AWS Shield, Azure DDoS Protection, GCP Cloud Armor).

## Quick Summary

1. Monitoring quality determines detection speed and response quality.
2. SIEM and cloud-native detection tools improve security visibility.
3. Incident response must be repeatable, documented, and continuously improved.
