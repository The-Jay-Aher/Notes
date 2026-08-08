# 3 - Playbooks Tasks and Modules

## Quick Summary

Ansible playbooks are YAML files that describe automation. A playbook contains one or more plays. A play maps hosts to tasks. Each task usually calls a module.

Mental model:

```text
playbook -> plays -> tasks -> modules
```

## Basic Playbook

```yaml
- name: Configure web servers
  hosts: web
  become: true
  tasks:
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present

    - name: Ensure nginx is running
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

Run:

```bash
ansible-playbook -i inventory.ini site.yml
```

## Play

A play defines:

- Name.
- Target hosts.
- Privilege escalation.
- Variables.
- Tasks.
- Handlers.

Example:

```yaml
- name: Update app servers
  hosts: app
  become: true
  tasks:
    - name: Install package
      ansible.builtin.apt:
        name: curl
        state: present
```

## Task

A task is one step.

```yaml
- name: Create application directory
  ansible.builtin.file:
    path: /opt/app
    state: directory
    owner: app
    group: app
    mode: "0755"
```

Good task names explain the desired outcome.

## Modules

Modules are the units of work.

Examples:

```yaml
- name: Copy config
  ansible.builtin.copy:
    src: app.conf
    dest: /etc/app/app.conf
    mode: "0644"
```

```yaml
- name: Create user
  ansible.builtin.user:
    name: app
    shell: /usr/sbin/nologin
```

Use docs:

```bash
ansible-doc ansible.builtin.user
```

## become

Use `become` for privilege escalation.

```yaml
- name: Install packages
  hosts: web
  become: true
  tasks:
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```

This usually means sudo on Linux.

## Check Mode

Preview changes:

```bash
ansible-playbook -i inventory.ini site.yml --check
```

Check mode support depends on modules. Some tasks cannot fully predict changes.

## Diff Mode

Show file changes:

```bash
ansible-playbook -i inventory.ini site.yml --diff
```

Do not use diff mode with secrets unless output is protected.

## Command vs Shell

`command` does not use shell features:

```yaml
- name: Show uptime
  ansible.builtin.command: uptime
```

`shell` uses a shell and supports pipes/redirection:

```yaml
- name: Find nginx process
  ansible.builtin.shell: ps aux | grep nginx
```

Prefer specific modules first, then `command`, then `shell` only when shell features are required.

## Idempotent Task Example

Good:

```yaml
- name: Ensure line exists
  ansible.builtin.lineinfile:
    path: /etc/app.conf
    line: "enabled=true"
```

Bad:

```yaml
- name: Append line
  ansible.builtin.shell: echo "enabled=true" >> /etc/app.conf
```

## Benefits

- Readable YAML automation.
- Repeatable server configuration.
- Modules reduce custom scripting.
- Check/diff mode helps review changes.

## Drawbacks / Limitations

- YAML indentation errors are common.
- Shell tasks can break idempotency.
- Some modules behave differently across operating systems.
- Very long playbooks need roles for organization.

## Hidden Details / Caveats

- Tasks run in order.
- By default, a failed task stops that host's play.
- Handlers run at the end of a play unless flushed.
- `changed_when` and `failed_when` can override task result logic.
- `ignore_errors` should be rare and intentional.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| No task names | Add clear names. |
| Shell for package/file/service work | Use modules. |
| Not using become | Use `become: true` for root-required tasks. |
| Ignoring check mode | Test with `--check` where possible. |
| Huge playbook | Split into roles. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| YAML error | Indentation, tabs, quoting. |
| Module not found | Collection installed, FQCN, Ansible version. |
| Permission denied | `become`, remote user, file permissions. |
| Task always changed | Module choice, `changed_when`, command/shell usage. |
| Different OS fails | Use OS-specific modules/conditionals. |

## Interview Notes

- Playbook is YAML automation.
- Play maps hosts to tasks.
- Task calls a module.
- Modules are usually idempotent.
- `become` handles privilege escalation.
- `--check` previews changes where supported.

## Related Topics

- [Variables Facts Templates and Handlers](4%20-%20Variables%20Facts%20Templates%20and%20Handlers.md)
- [Roles Collections and Reuse](5%20-%20Roles%20Collections%20and%20Reuse.md)

## Official References

- [Intro to playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)
- [Playbook guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- [Module index](https://docs.ansible.com/ansible/latest/collections/index_module.html)
