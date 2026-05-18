# 6 - Monitoring and Responding to Secure Software

## Quick Summary

Security does not end at deployment. Monitoring detects suspicious behavior, misconfiguration, abuse, and failures. Response turns alerts into investigation, containment, eradication, recovery, and lessons learned.

## Monitoring Stage Goals

Security monitoring should answer:

- Who accessed what?
- Which admin actions happened?
- Which errors or suspicious events increased?
- Are secrets or credentials being abused?
- Are public endpoints being attacked?
- Are cloud resources changing unexpectedly?
- Are logs complete enough for investigation?

## Logging Fundamentals

Good logs include:

- Timestamp.
- Actor/user/service.
- Source IP or request context where appropriate.
- Action.
- Resource.
- Result.
- Error reason.
- Request/correlation ID.

Avoid logging:

- Passwords.
- Tokens.
- Full secrets.
- Sensitive personal data unless required and protected.
- Payment card data.

## Security Logs To Collect

| Area | Examples |
| --- | --- |
| Application | Login, access denied, admin action, errors, rate limits. |
| Cloud control plane | IAM changes, network changes, storage policy changes. |
| CI/CD | Workflow runs, deployment approvals, secret usage events where available. |
| Network | WAF logs, load balancer logs, firewall logs, DNS logs. |
| Host/container | Process, file integrity, runtime alerts. |
| Kubernetes | API audit logs, admission events, Pod security alerts. |

## SIEM

Security Information and Event Management systems collect, normalize, correlate, and alert on security data.

SIEM helps with:

- Centralized investigation.
- Alert correlation.
- Compliance evidence.
- Threat detection.
- Incident timelines.

Limitations:

- Bad logs lead to bad alerts.
- Too many alerts cause fatigue.
- SIEM needs tuning and ownership.

## WAF vs RASP

| Control | Meaning | Use |
| --- | --- | --- |
| WAF | Web Application Firewall that filters HTTP traffic before the app. | Block common web attacks at the edge. |
| RASP | Runtime Application Self-Protection inside/near app runtime. | Detect/block suspicious runtime behavior. |

WAF is easier to deploy broadly. RASP can have deeper application context but may be more invasive.

## Responding To Security Events

High-level incident response flow:

1. Detect.
2. Triage.
3. Contain.
4. Eradicate.
5. Recover.
6. Review and improve.

For each incident, capture:

- What happened?
- When did it start?
- Which systems/users/data were affected?
- How was it detected?
- What was done to contain it?
- What evidence supports the conclusion?
- What prevention/detection improvements are needed?

## NIST Incident Response Lifecycle

Common NIST-style lifecycle:

| Phase | Meaning |
| --- | --- |
| Preparation | Tools, runbooks, access, training, backups. |
| Detection and Analysis | Identify and understand incidents. |
| Containment, Eradication, Recovery | Limit damage, remove cause, restore service. |
| Post-Incident Activity | Lessons learned and control improvements. |

## Cloud API Security Considerations

Cloud control plane logs are critical.

Monitor:

- IAM policy changes.
- New access keys.
- Security group changes.
- Public bucket/object changes.
- New internet gateways/routes.
- Disabled logging.
- Unusual API calls.
- Region activity where you do not operate.

Cloud attackers often use legitimate APIs with stolen credentials, so API logs are evidence.

## Availability And DDoS Response

DDoS and availability response controls:

- CDN.
- WAF.
- Rate limiting.
- Load balancing.
- Auto scaling.
- Queue buffering.
- Caching.
- DDoS protection services.
- Runbooks for traffic spikes.

Design for graceful degradation:

- Serve cached data.
- Disable expensive optional features.
- Queue non-critical work.
- Protect databases from overload.

## Vulnerability Response

When a new vulnerability appears:

1. Identify affected assets.
2. Determine exposure and exploitability.
3. Prioritize patch or mitigation.
4. Test fix.
5. Deploy fix.
6. Verify.
7. Document exception if not fixed.
8. Monitor for exploitation.

Sources:

- Dependency scanner.
- Vendor advisory.
- Cloud provider alert.
- Container scan.
- Runtime detection.
- Penetration test.

## Benefits

- Detects issues missed before deployment.
- Supports incident investigation.
- Improves audit readiness.
- Provides feedback to planning and coding.
- Reduces response time.

## Drawbacks / Limitations

- Too many alerts reduce attention.
- Logs can be expensive.
- Missing logs make incidents hard to investigate.
- Monitoring cannot fix weak architecture by itself.
- Privacy and data retention need careful handling.

## Hidden Details / Caveats

- Time synchronization matters for investigations.
- Logs must be protected from tampering.
- Alert rules need owners and runbooks.
- Production debugging access should be controlled and logged.
- Backups matter only if restore is tested.
- Incident response should include communication, not only technical fixes.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Logging secrets | Redact sensitive values. |
| No runbooks | Write response steps for common alerts. |
| Alerts without owners | Assign ownership and escalation. |
| Ignoring cloud control plane logs | Monitor IAM/network/storage changes. |
| No post-incident review | Feed lessons back into controls. |

## Interview Notes

- Monitoring is shift-right security.
- SIEM centralizes and correlates security logs.
- WAF filters web traffic before the app.
- Incident response includes preparation, detection, containment, eradication, recovery, and lessons learned.
- Cloud API logs are essential because attackers may use legitimate APIs.
- Vulnerability response should consider exposure and exploitability, not only CVSS.

## Related Topics

- [Releasing and Deploying Secure Software](5%20-%20Releasing%20and%20Deploying%20Secure%20Software.md)
- [Conclusion](7%20-%20Conclusion.md)

