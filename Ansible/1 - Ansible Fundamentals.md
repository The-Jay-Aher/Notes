# 1 - Ansible Fundamentals

## Quick Summary

Ansible automates work on servers and infrastructure. You define the desired tasks in YAML, tell Ansible which hosts to target, and Ansible connects to those hosts to make changes.

Beginner mental model:

```text
Your laptop/control node -> SSH/WinRM -> servers -> modules make changes
```

## Why Ansible Matters

Without automation:

- Server setup is manual.
- Configuration drifts.
- Repeating changes across many servers is slow.
- Documentation may not match reality.

With Ansible:

- Setup steps are written as code.
- Changes can be reviewed.
- The same playbook can run against many hosts.
- Repeated runs should become safe when tasks are idempotent.

## Core Terms

| Term | Meaning |
| --- | --- |
| Control node | Machine where Ansible CLI runs. |
| Managed node | Target machine Ansible configures. |
| Inventory | List/groups of managed nodes. |
| Playbook | YAML file describing automation. |
| Play | Maps hosts to tasks. |
| Task | One automation step. |
| Module | Unit of work, such as install package or copy file. |
| Collection | Distribution format for modules, roles, plugins, playbooks. |
| Role | Reusable playbook structure. |
| Facts | Data Ansible gathers about hosts. |

## Agentless Model

For most Linux targets, Ansible uses SSH and does not require a long-running agent on managed nodes.

Requirements commonly include:

- SSH access.
- Python on the managed node for many modules.
- Correct user permissions.
- `sudo`/privilege escalation if tasks need root.

Windows uses WinRM or related mechanisms instead of SSH in many setups.

## Idempotency

Idempotency means running the same automation repeatedly should not keep changing the system if it is already correct.

Example:

```yaml
- name: Install nginx
  ansible.builtin.apt:
    name: nginx
    state: present
```

If nginx is already installed, Ansible should report `ok`, not `changed`.

Bad pattern:

```yaml
- name: Append config every run
  ansible.builtin.shell: echo "setting=true" >> /etc/app.conf
```

This changes the file every run. Use modules such as `lineinfile`, `template`, or `copy` instead.

## Ad Hoc Commands

Ad hoc command:

```bash
ansible all -i inventory.ini -m ping
```

Run command:

```bash
ansible web -i inventory.ini -m ansible.builtin.command -a "uptime"
```

Ad hoc commands are good for quick checks. Playbooks are better for repeatable automation.

## Modules

Modules do the actual work.

Examples:

| Module | Use |
| --- | --- |
| `ansible.builtin.ping` | Test Ansible connectivity. |
| `ansible.builtin.apt` | Manage Debian/Ubuntu packages. |
| `ansible.builtin.yum` / `dnf` | Manage Red Hat-family packages. |
| `ansible.builtin.copy` | Copy files. |
| `ansible.builtin.template` | Render Jinja2 templates. |
| `ansible.builtin.service` | Manage services. |
| `ansible.builtin.user` | Manage users. |
| `ansible.builtin.file` | Manage files/directories/permissions. |

Use module documentation:

```bash
ansible-doc ansible.builtin.copy
```

## Benefits

- Human-readable YAML.
- Agentless for common Linux workflows.
- Large module ecosystem.
- Good for configuration management and orchestration.
- Idempotent modules make repeated runs safer.

## Drawbacks / Limitations

- YAML indentation mistakes are common.
- Very large playbooks can become hard to maintain.
- Imperative shell tasks can break idempotency.
- Performance can be slower for very large fleets compared with agent-based systems.
- Secrets need Ansible Vault or external secret management.

## Hidden Details / Caveats

- Ansible runs tasks in order.
- A task runs on all targeted hosts before moving to the next task unless strategy changes.
- `changed` does not always mean failure; it means Ansible modified something.
- `ok` means already in desired state.
- `failed` stops the play for that host unless handled.
- Modules often need Python on managed hosts.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Using shell for everything | Use idempotent modules. |
| No inventory groups | Group hosts by role/environment. |
| Hard-coded secrets | Use Vault or secret manager. |
| Running as root directly | Use normal SSH user plus `become` where needed. |
| Ignoring check mode | Use `--check` for safer previews where supported. |

## Interview Notes

- Ansible is agentless for most Linux targets.
- Inventory defines hosts.
- Playbooks define automation.
- Modules perform work.
- Idempotency is central.
- Roles organize reusable automation.
- Ansible Vault encrypts sensitive variables/files.

## Related Topics

- [Inventory and Configuration](2%20-%20Inventory%20and%20Configuration.md)
- [Playbooks Tasks and Modules](3%20-%20Playbooks%20Tasks%20and%20Modules.md)

## Official References

- [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- [Ansible basic concepts](https://docs.ansible.com/ansible/latest/getting_started/basic_concepts.html)
- [Ansible getting started](https://docs.ansible.com/ansible/latest/getting_started/index.html)
