# 5 - Roles Collections and Reuse

## Quick Summary

Roles organize Ansible automation into reusable folders. Collections package Ansible content such as roles, modules, plugins, and playbooks for distribution. Use roles when playbooks become too large or repeated across projects.

## Why Reuse Matters

Without reuse:

- Playbooks become huge.
- Tasks are copied between projects.
- Fixes must be repeated in many places.
- Standards drift.

With roles and collections:

- Common logic is reusable.
- Project structure is clearer.
- Teams can share tested automation.
- CI can test automation content.

## Role Structure

Common role layout:

```text
roles/
  nginx/
    defaults/
      main.yml
    vars/
      main.yml
    tasks/
      main.yml
    handlers/
      main.yml
    templates/
      nginx.conf.j2
    files/
      static-file.txt
    meta/
      main.yml
```

Important directories:

| Directory | Purpose |
| --- | --- |
| `tasks` | Main work. |
| `handlers` | Service restarts/reloads. |
| `templates` | Jinja2 templates. |
| `files` | Static files. |
| `defaults` | Low-precedence default variables. |
| `vars` | Higher-precedence role variables. |
| `meta` | Role metadata/dependencies. |

## Using A Role

```yaml
- name: Configure web servers
  hosts: web
  become: true
  roles:
    - nginx
```

With variables:

```yaml
roles:
  - role: nginx
    nginx_port: 8080
```

## defaults vs vars

| Location | Precedence | Use |
| --- | --- | --- |
| `defaults/main.yml` | Low | Values callers should override. |
| `vars/main.yml` | Higher | Internal values that should rarely change. |

Prefer defaults for role customization.

## Collections

A collection can include:

- Modules.
- Roles.
- Playbooks.
- Plugins.
- Documentation.

Install:

```bash
ansible-galaxy collection install community.general
```

Use fully qualified collection name:

```yaml
- name: Use module from collection
  community.general.some_module:
    option: value
```

## requirements.yml

Example:

```yaml
collections:
  - name: community.general
    version: ">=9.0.0"

roles:
  - name: geerlingguy.nginx
```

Install:

```bash
ansible-galaxy install -r requirements.yml
```

## Project Layout

Example:

```text
ansible/
  ansible.cfg
  inventory/
    dev.ini
    prod.ini
  group_vars/
    web.yml
  host_vars/
    web1.yml
  playbooks/
    site.yml
  roles/
    nginx/
  requirements.yml
```

## Benefits

- Reusable automation.
- Cleaner playbooks.
- Easier testing.
- Better sharing across teams.
- Standard file layout.

## Drawbacks / Limitations

- Too many roles can make flow harder to follow.
- Variable precedence across roles can confuse beginners.
- External roles/collections need version pinning.
- Collections add dependency management.

## Hidden Details / Caveats

- Role defaults are easy for callers to override.
- Role vars are harder to override and should be used carefully.
- Handlers in roles can be notified by role tasks.
- Collections should be referenced with FQCN for clarity.
- External automation content should be reviewed before use.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| One giant playbook | Split into roles. |
| Role has hard-coded environment values | Move to defaults/vars. |
| No version pinning for dependencies | Use `requirements.yml`. |
| Copying roles from internet blindly | Review content first. |
| Too much logic hidden in roles | Keep role interfaces documented. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| Role not found | `roles_path`, directory name, requirements install. |
| Collection module not found | Collection installed, FQCN, execution environment. |
| Variable not overriding | Precedence, role vars vs defaults. |
| Handler missing | Handler name and role handler file. |
| Dependency not installed in CI | Run `ansible-galaxy install -r requirements.yml`. |

## Interview Notes

- Roles organize reusable Ansible content.
- Collections distribute roles, modules, plugins, and playbooks.
- `ansible-galaxy` installs roles/collections.
- `requirements.yml` declares dependencies.
- Use role defaults for configurable values.

## Related Topics

- [Playbooks Tasks and Modules](3%20-%20Playbooks%20Tasks%20and%20Modules.md)
- [Vault Troubleshooting and Best Practices](6%20-%20Vault%20Troubleshooting%20and%20Best%20Practices.md)

## Official References

- [Roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html)
- [Collections](https://docs.ansible.com/ansible/latest/collections_guide/index.html)
- [Ansible Galaxy user guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html)
