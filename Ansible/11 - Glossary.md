# 11 - Ansible Glossary

| Term | Meaning | Trap |
| --- | --- | --- |
| Control node | Machine running Ansible. | Needs correct Ansible version. |
| Managed node | Target host. | Needs connection/auth/interpreter support. |
| Inventory | Host/group source. | Wrong inventory means wrong targets. |
| Playbook | YAML automation file. | Syntax valid does not mean logic safe. |
| Play | Maps hosts to tasks. | Too-broad host pattern. |
| Task | Single automation step. | Non-idempotent shell. |
| Module | Unit that performs work. | Module behavior/version matters. |
| Handler | Task triggered by change notification. | Restarts too often if template changes every run. |
| Role | Reusable playbook structure. | Hidden variable/default behavior. |
| Collection | Package of modules/plugins/roles. | FQCN avoids ambiguity. |
| Fact | Host data gathered by Ansible. | Fact gathering costs time. |
| Vault | Encrypted file/string support. | Does not prevent runtime leaks. |
| Check mode | Preview mode. | Not fully supported by all modules. |
| Diff mode | Shows file/content changes. | Can leak secrets. |
| Idempotency | Repeated run converges without unnecessary changes. | Must be tested by repeated runs. |

## Questions to Test Understanding

1. What defines where Ansible runs?
2. What performs work on managed nodes?
3. What does a handler respond to?
4. What protects secrets at rest?
5. What is the main idempotency smell?

## Answers and Reasoning

1. Inventory and play host pattern.
2. Modules.
3. A notification from a changed task.
4. Ansible Vault or external secret management.
5. A task reporting changed on every run without real drift.

