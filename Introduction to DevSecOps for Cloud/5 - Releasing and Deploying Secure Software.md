# 5 - Releasing and Deploying Secure Software

## Quick Summary

Release and deployment security controls protect the path from a tested artifact to a running system. The goal is to deploy the correct artifact, to the correct environment, with the correct permissions, configuration, approvals, and rollback plan.

## Release Stage Focus Areas

Before release, confirm:

- The artifact came from the trusted pipeline.
- Tests and required scans passed.
- Critical findings are fixed or approved as exceptions.
- Release notes and change record are ready.
- Deployment plan and rollback plan exist.
- Secrets/config are environment-specific and controlled.
- Approvals are captured where required.

## Build Once, Promote

Good release pattern:

```text
build artifact once -> test same artifact -> promote same artifact -> deploy same artifact
```

Avoid rebuilding for each environment because it creates drift.

## Configuration Management

Configuration should be:

- Version-controlled where non-secret.
- Environment-specific where needed.
- Reviewed through change control.
- Separated from secrets.
- Validated before deployment.

Examples:

- Terraform variables.
- Kubernetes manifests.
- Helm values.
- Feature flags.
- Application environment variables.

## Access Management

Deployment access should follow least privilege.

Good practices:

- Use separate roles for CI, deploy, and runtime.
- Avoid long-lived cloud keys where possible.
- Prefer short-lived credentials or workload identity.
- Limit who can approve production.
- Log deployment actor, artifact, version, and target.

High-risk pattern:

```text
One permanent admin cloud key stored in Jenkins/GitHub.
```

Better pattern:

```text
CI job assumes a limited deploy role for the target environment.
```

## Container And Runtime Security

Deployment controls:

- Use signed/trusted images where required.
- Scan images before deployment.
- Run as non-root where possible.
- Drop unnecessary Linux capabilities.
- Set read-only root filesystem where possible.
- Use resource requests and limits.
- Do not mount host paths unless reviewed.
- Use runtime policies in Kubernetes where available.

Kubernetes example:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
```

## Network Security Controls

Deployment should verify:

- Public exposure is intentional.
- Security groups/firewalls are least privilege.
- Private services stay private.
- TLS is configured correctly.
- Ingress rules route only expected hosts/paths.
- NetworkPolicies restrict pod traffic where supported.

Common cloud mistake:

```text
Database security group allows 0.0.0.0/0.
```

## Data Security Controls

Protect:

- Customer data.
- Credentials.
- Logs containing sensitive fields.
- Backups.
- Object storage.
- Databases.

Controls:

- Encryption at rest.
- Encryption in transit.
- Access policies.
- Data retention.
- Backup recovery tests.
- Masking/redaction in logs.

## Infrastructure As Code

IaC makes infrastructure reviewable and repeatable.

Security checks:

- Public access.
- Overly broad IAM.
- Missing encryption.
- Missing logging.
- Open security groups.
- Weak Kubernetes settings.
- Missing backup/deletion protection.

Pipeline flow:

```text
terraform fmt -> validate -> plan -> IaC scan -> approval -> apply
```

## Deployment Strategies

| Strategy | Use |
| --- | --- |
| Rolling | Gradually replace old instances/Pods. |
| Blue/green | Switch traffic between two full environments/versions. |
| Canary | Send small traffic percentage to new version first. |
| Feature flags | Control feature exposure without redeploying. |
| Manual approval | Human gate before sensitive deployment. |

## Penetration Testing

Penetration testing simulates attacker behavior to find real exploit paths.

Use it:

- Before major launches.
- After major architecture changes.
- For compliance or high-risk systems.
- To validate security assumptions.

Do not rely only on pentesting. It is periodic. DevSecOps needs continuous checks too.

## Benefits

- Reduces release-time surprises.
- Makes production changes traceable.
- Prevents accidental exposure.
- Supports safer rollback.
- Improves compliance evidence.

## Drawbacks / Limitations

- Approvals can become rubber stamps if not meaningful.
- Too many manual gates slow delivery.
- IaC scans can be noisy.
- Rollbacks can be hard if database changes are not planned.
- Secure deployment still needs runtime monitoring.

## Hidden Details / Caveats

- A deployment can pass tests but fail because environment config is wrong.
- Secret rotation must be part of operational design.
- Rollback must consider data migrations.
- Feature flags need lifecycle management or they become technical debt.
- Production access should be rare, logged, and reviewed.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Rebuilding per environment | Build once and promote. |
| Permanent admin deploy key | Use scoped, short-lived credentials. |
| No rollback plan | Define rollback and verify it works. |
| Public-by-default infrastructure | Review exposure before apply. |
| Database migrations not reversible | Use expand/contract or forward-compatible migrations. |

## Interview Notes

- Release security verifies artifact integrity, approvals, and readiness.
- Deployment security verifies environment, permissions, network, runtime, and rollback.
- IaC enables reviewable infrastructure changes.
- Blue/green and canary reduce deployment risk.
- Least-privilege deploy roles are safer than static admin keys.

## Related Topics

- [Building and Testing Secure Software](4%20-%20Building%20and%20Testing%20Secure%20Software.md)
- [Monitoring and Responding to Secure Software](6%20-%20Monitoring%20and%20Responding%20to%20Secure%20Software.md)
- [Terraform](../Terraform/1%20-%20Understanding%20Infrastructure%20as%20Code.md)

