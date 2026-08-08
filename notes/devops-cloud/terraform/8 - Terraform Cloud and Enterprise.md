# 8 - Terraform Cloud and Enterprise

## Quick Summary

HCP Terraform, formerly commonly referred to as Terraform Cloud, and Terraform Enterprise provide remote state, remote runs, policy controls, private module registries, variable management, collaboration, and governance features for teams.

Use these platforms when Terraform needs shared workflows, controlled applies, approvals, policy checks, audit history, and secure state management.

## Terminology

| Term | Meaning |
| --- | --- |
| HCP Terraform | HashiCorp-managed Terraform collaboration platform. |
| Terraform Enterprise | Self-hosted enterprise version. |
| Workspace | A unit that stores configuration settings, variables, state, and run history. |
| Run | Plan/apply workflow in a workspace. |
| Variable set | Reusable variables shared across workspaces. |
| Policy | Rule that evaluates plans or runs. |
| Private registry | Internal registry for modules/providers. |

## Why Use HCP Terraform / Enterprise

Benefits:

- Remote state storage.
- State locking/run coordination.
- Remote execution.
- Team access controls.
- Sensitive variable storage.
- Run history.
- VCS integration.
- Policy as code.
- Private module registry.
- Audit trails.

## CLI Workflow vs Remote Runs

Local CLI:

```text
terraform plan/apply runs on your machine or CI runner
```

Remote run:

```text
Terraform CLI/VCS triggers run -> HCP Terraform executes plan/apply -> state stored remotely
```

Remote runs reduce dependency on a user's laptop and centralize execution history.

## Workspaces

HCP Terraform/Terraform Enterprise workspaces are different from Terraform CLI workspaces.

| Workspace Type | Meaning |
| --- | --- |
| Terraform CLI workspace | Multiple state instances for one local configuration/backend. |
| HCP Terraform workspace | Remote unit containing state, variables, settings, run history, and execution configuration. |

Do not assume they are interchangeable.

## VCS-Driven Workflow

Common flow:

```text
Pull request -> speculative plan
Merge to main -> plan -> policy checks -> approval -> apply
```

Benefits:

- Plans are attached to code review.
- Applies happen from approved code.
- History is centralized.
- Teams can require approvals.

## Variables And Secrets

Workspace variables can include:

- Terraform variables.
- Environment variables.
- Sensitive values.

Best practices:

- Mark secrets as sensitive.
- Use variable sets for shared values.
- Avoid putting secrets in Git.
- Use dynamic credentials/workload identity where available.
- Restrict who can read/manage variables.

## Policy As Code

Policy checks enforce rules before apply.

Examples:

- No public S3 buckets.
- Required tags.
- Approved regions only.
- Instance types must be from an allowed list.
- Database deletion protection required.
- No overly broad IAM policies.

Policy tools may include Sentinel in HashiCorp environments or other policy engines depending on platform and workflow.

## Private Module Registry

Private registry helps teams publish reusable modules.

Benefits:

- Discoverable internal modules.
- Versioned releases.
- Documentation.
- Standard patterns.
- Governance.

Use semantic versioning and changelogs for shared modules.

## Terraform Enterprise

Terraform Enterprise is for organizations that need self-hosted control.

Reasons:

- Network isolation.
- Compliance requirements.
- Data residency.
- Custom operational control.
- Integration with internal systems.

Trade-off: self-hosting creates operational responsibility.

## Benefits

- Centralized Terraform workflow.
- Safer state handling.
- Better team collaboration.
- Policy enforcement.
- Auditability.
- Standardized modules.

## Drawbacks / Limitations

- Adds platform cost and administration.
- Requires workspace design.
- Policy can become noisy if poorly written.
- Remote execution needs network access to target APIs.
- Self-hosted Enterprise requires operational maintenance.

## Hidden Details / Caveats

- HCP Terraform workspaces are not CLI workspaces.
- Remote state still contains sensitive values and needs access control.
- A passing policy check does not prove architecture is good.
- Workspace sprawl can become difficult to manage.
- Private modules need versioning discipline.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Treating workspace as just a folder | Understand state, variables, runs, and settings. |
| No policy exceptions process | Define controlled, expiring exceptions. |
| Secrets in tfvars committed to Git | Use sensitive workspace variables or secret systems. |
| One workspace for unrelated systems | Split by lifecycle/ownership. |
| Modules published without versions | Use versioned releases. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| Remote plan cannot reach cloud API | Credentials, variables, network access, agent configuration. |
| Policy fails | Policy message, plan content, exception process. |
| Workspace uses wrong variables | Variable sets, workspace variables, precedence. |
| Module not found | Registry source, version, permissions. |
| Run stuck | Queue, policy approval, manual confirmation, agent availability. |

## Interview Notes

- HCP Terraform provides remote runs, state, variables, policies, and collaboration.
- Terraform Enterprise is self-hosted.
- HCP Terraform workspaces differ from CLI workspaces.
- Policy as code can enforce governance before apply.
- Private module registry standardizes reusable modules.
- Remote state still must be protected.

## Related Topics

- [Terraform State](4%20-%20Terraform%20State.md)
- [Terraform Modules](5%20-%20Terraform%20Modules.md)
- [Terraform CLI](7%20-%20Terraform%20CLI.md)

