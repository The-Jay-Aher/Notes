# 10 - Ansible Cheatsheet

## Source Snapshot

Source checked: official Ansible community docs on 2026-05-27. Current docs note ansible-core 2.19 / Ansible 12 templating changes; verify your project version before upgrading.

## Mental Model

```text
inventory says where
playbook says desired work
modules make target state true
results report ok/changed/failed/skipped
```

## Core Commands

```bash
ansible-inventory -i inventory.ini --graph
ansible all -i inventory.ini -m ansible.builtin.ping
ansible web -i inventory.ini -m ansible.builtin.command -a "uptime"
ansible-doc ansible.builtin.copy
ansible-playbook -i inventory.ini site.yml --syntax-check
ansible-playbook -i inventory.ini site.yml --check --diff
ansible-playbook -i inventory.ini site.yml --limit web1
ansible-vault create group_vars/prod/vault.yml
```

## Result Meanings

| Result | Meaning |
| --- | --- |
| `ok` | Already correct. |
| `changed` | Modified target. |
| `failed` | Task failed. |
| `skipped` | Condition prevented execution. |
| `unreachable` | Connection/auth/transport problem. |

## Idempotency Rules

- Prefer modules over shell.
- Repeat the playbook and expect stable `ok`.
- Use handlers for restarts.
- Use templates/copy/lineinfile instead of appending.
- Use `changed_when` carefully.
- Use `--check --diff`, but understand module limits.

## Common Traps

- wrong inventory
- wrong group variables
- variable precedence surprise
- plaintext secrets
- diff leaking secrets
- shell appending every run
- missing `become`
- unquoted file modes
- roles with hidden dependencies
- Ansible version/templating behavior changes

