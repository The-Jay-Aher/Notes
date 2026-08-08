# 3 - Planning and Coding Secure Software

## Quick Summary

Secure software starts before code is written. Planning identifies what must be protected, who might attack it, and what controls are required. Coding turns those decisions into implementation practices such as input validation, authentication, authorization, secrets handling, and safe dependency use.

## Planning Stage Objectives

Planning should answer:

- What data does the system handle?
- Who are the users and administrators?
- What systems does it connect to?
- What can go wrong?
- What security requirements are mandatory?
- What logs and alerts are needed?
- What compliance or privacy rules apply?

## Security Requirements

Examples:

- Users must authenticate with SSO.
- Admin actions must be audited.
- Secrets must not be stored in source control.
- Sensitive data must be encrypted at rest and in transit.
- Public APIs must rate-limit requests.
- Production deployment requires approval.
- Backups must be recoverable within defined RTO/RPO.

Good security requirements are testable.

Bad:

```text
The app should be secure.
```

Better:

```text
All admin API calls must require the Admin role and must write audit logs with actor, action, resource, result, and timestamp.
```

## Threat Modeling

Threat modeling is structured thinking about how a system can be attacked or misused.

Common flow:

1. Draw the architecture.
2. Identify assets.
3. Identify trust boundaries.
4. Identify threats.
5. Rank risk.
6. Add controls.
7. Track unresolved risk.

Simple diagram:

```text
User -> CDN/WAF -> API -> Database
                 -> Queue -> Worker
```

Questions:

- Can unauthenticated users reach the API?
- What stops a user from accessing another user's data?
- Where are secrets stored?
- What logs prove what happened?
- What happens if the queue is flooded?

## STRIDE Threat Categories

| Category | Question |
| --- | --- |
| Spoofing | Can someone pretend to be another user/service? |
| Tampering | Can someone modify data or code? |
| Repudiation | Can someone deny an action because logs are missing? |
| Information disclosure | Can sensitive data leak? |
| Denial of service | Can the system be made unavailable? |
| Elevation of privilege | Can someone gain higher permissions? |

## Cloud Threat Considerations

Cloud-specific planning must include:

- IAM permissions.
- Public exposure.
- Security groups/firewalls.
- Object storage bucket policies.
- Secrets in CI/CD.
- Network paths between services.
- Managed service configuration.
- Logging and audit trails.
- Backup and deletion protection.

Common cloud planning mistake:

```text
The app has secure code but the storage bucket is public.
```

## Secure Coding Practices

| Practice | Why It Matters |
| --- | --- |
| Input validation | Prevent malformed/unexpected input from reaching unsafe paths. |
| Output encoding | Prevent injection into HTML, shell, SQL, logs, etc. |
| Parameterized queries | Prevent SQL injection. |
| Strong authentication | Verify identity correctly. |
| Authorization checks | Enforce what authenticated users can do. |
| Safe secret handling | Avoid hard-coded credentials and leaks. |
| Dependency control | Reduce vulnerable/outdated packages. |
| Error handling | Avoid leaking internals while preserving useful logs. |
| Secure defaults | Fail closed where possible. |

## Authentication vs Authorization

| Term | Meaning |
| --- | --- |
| Authentication | Proves who the user/service is. |
| Authorization | Decides what they are allowed to do. |

Common mistake:

```text
User is logged in, so allow access to all records.
```

Correct:

```text
User is logged in, then check whether this user can access this specific record/action.
```

## Secrets In Code

Never commit:

- API keys.
- Cloud access keys.
- Database passwords.
- Private keys.
- Tokens.
- Real connection strings with credentials.

Use:

- Secret managers.
- CI/CD secret stores.
- Short-lived cloud credentials where possible.
- Environment-specific secret injection.

If a secret is committed:

1. Revoke/rotate it.
2. Remove from current code.
3. Consider repository history cleanup if necessary.
4. Review logs and usage for abuse.

## Code Analysis Goals

Static analysis and code review should look for:

- Injection paths.
- Missing authorization.
- Unsafe deserialization.
- Path traversal.
- Secrets.
- Insecure crypto.
- Dependency misuse.
- Logging of sensitive data.
- Error handling leaks.

## Tooling Awareness

Examples:

- SAST tools for source code patterns.
- Secret scanners for committed secrets.
- Dependency scanners for vulnerable packages.
- IDE security plugins.
- Code review bots.

Tooling supports humans. It does not replace design review.

## Benefits

- Prevents expensive late fixes.
- Improves clarity of risk.
- Gives developers actionable requirements.
- Reduces common vulnerability classes.

## Drawbacks / Limitations

- Threat modeling takes practice.
- Tools miss business logic flaws.
- Requirements can become stale if architecture changes.
- False positives need triage.

## Hidden Details / Caveats

- Most serious authorization bugs are business-logic bugs, not syntax bugs.
- Secret scanning must trigger rotation, not only code cleanup.
- Secure coding standards must match the language/framework.
- Cloud IAM mistakes can bypass otherwise strong application controls.
- Threat models should be updated after major architecture changes.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Threat modeling only once | Revisit after major changes. |
| Only scanning code | Also review design, cloud config, and runtime. |
| Vague security stories | Write testable security requirements. |
| Ignoring abuse cases | Ask how features can be misused. |
| Hard-coded secrets | Use secret management and rotation. |

## Interview Notes

- Secure planning includes assets, threats, trust boundaries, and controls.
- STRIDE is a common threat modeling framework.
- Authentication proves identity; authorization enforces permissions.
- Secret leakage requires rotation, not only deletion from code.
- SAST helps but does not catch all design/business logic issues.

## Related Topics

- [DevSecOps Fundamentals](2%20-%20DevSecOps%20Fundamentals.md)
- [Building and Testing Secure Software](4%20-%20Building%20and%20Testing%20Secure%20Software.md)

