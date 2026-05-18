# 2 - Inventory and Configuration

## Quick Summary

Inventory tells Ansible which hosts exist and how to group/connect to them. Configuration, usually through `ansible.cfg`, controls defaults such as inventory path, remote user, roles path, host key checking, and privilege behavior.

Beginner mental model:

```text
inventory = where to run
playbook = what to run
ansible.cfg = default behavior
```

## Inventory Basics

INI inventory:

```ini
[web]
web1 ansible_host=10.0.1.10
web2 ansible_host=10.0.1.11

[db]
db1 ansible_host=10.0.2.10
```

YAML inventory:

```yaml
all:
  children:
    web:
      hosts:
        web1:
          ansible_host: 10.0.1.10
        web2:
          ansible_host: 10.0.1.11
    db:
      hosts:
        db1:
          ansible_host: 10.0.2.10
```

## Groups

Groups let you target roles of servers.

```bash
ansible web -i inventory.ini -m ping
ansible db -i inventory.ini -m ping
ansible all -i inventory.ini -m ping
```

Group examples:

- `web`
- `db`
- `cache`
- `prod`
- `staging`
- `linux`

## Inventory Variables

Host variable:

```ini
web1 ansible_host=10.0.1.10 ansible_user=ubuntu
```

Group variable:

```ini
[web:vars]
ansible_user=ubuntu
app_port=8080
```

Better for larger projects:

```text
group_vars/
  web.yml
host_vars/
  web1.yml
```

## Common Connection Variables

| Variable | Meaning |
| --- | --- |
| `ansible_host` | Real IP/DNS to connect to. |
| `ansible_user` | Remote SSH user. |
| `ansible_port` | SSH port. |
| `ansible_ssh_private_key_file` | SSH key path. |
| `ansible_connection` | Connection type, such as `ssh` or `local`. |
| `ansible_python_interpreter` | Python path on managed host. |

## ansible.cfg

Example:

```ini
[defaults]
inventory = ./inventory.ini
remote_user = ubuntu
host_key_checking = True
roles_path = ./roles

[privilege_escalation]
become = True
become_method = sudo
become_user = root
```

Find current config:

```bash
ansible-config dump --only-changed
```

## Config Precedence

Ansible looks for config in several places. In general, project-local `ansible.cfg` is common for repo-specific defaults.

Be careful: running Ansible from a different directory can change which config is used.

## Testing Inventory

List hosts:

```bash
ansible-inventory -i inventory.ini --list
ansible-inventory -i inventory.ini --graph
```

Ping:

```bash
ansible all -i inventory.ini -m ping
```

## Dynamic Inventory

Dynamic inventory gets hosts from an external source such as:

- AWS EC2.
- Azure.
- GCP.
- VMware.
- Kubernetes.
- CMDB.

Use dynamic inventory when hosts change often.

## Benefits

- Clear target grouping.
- Environment-specific variables.
- Reusable defaults.
- Supports static and dynamic infrastructure.

## Drawbacks / Limitations

- Variable precedence can be confusing.
- Bad group names lead to messy playbooks.
- Inventory secrets need encryption.
- Dynamic inventory requires plugin setup and credentials.

## Hidden Details / Caveats

- Inventory host alias and `ansible_host` can differ.
- Group variables apply to all hosts in the group.
- A host can belong to multiple groups.
- Variable precedence decides final value when multiple places define the same variable.
- Host key checking protects against MITM but can surprise beginners.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Hard-coding IPs in playbooks | Put hosts in inventory. |
| Mixing prod and dev accidentally | Separate inventories or clear groups. |
| Disabling host key checking globally | Understand risk; manage known hosts. |
| Secrets in plain group_vars | Use Vault. |
| Wrong SSH user | Set `ansible_user`. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| Host unreachable | IP/DNS, SSH key, user, port, security group/firewall. |
| Wrong inventory used | `ansible-inventory --list`, working directory, config. |
| Python not found | `ansible_python_interpreter`. |
| Permission denied | SSH user, key permissions, sudo/become config. |
| Variables not expected | `ansible-inventory --host <host>` and precedence. |

## Interview Notes

- Inventory defines managed hosts.
- Groups let playbooks target roles/environments.
- `ansible.cfg` controls defaults.
- Static inventory is file-based; dynamic inventory queries external systems.
- `group_vars` and `host_vars` store variables.

## Related Topics

- [Ansible Fundamentals](1%20-%20Ansible%20Fundamentals.md)
- [Variables Facts Templates and Handlers](4%20-%20Variables%20Facts%20Templates%20and%20Handlers.md)

## Official References

- [Inventory guide](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)
- [Ansible configuration settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html)
- [Ad hoc commands](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html)
