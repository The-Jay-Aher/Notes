# Ansible

## Quick Summary

Ansible is an automation tool used for configuration management, application deployment, orchestration, and repeatable operations. It is agentless for most Linux/Unix use cases: the control node connects to managed hosts, commonly over SSH, and runs modules to make the target state true.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [Ansible Fundamentals](1%20-%20Ansible%20Fundamentals.md) | What Ansible is, control node, managed nodes, modules, idempotency. |
| 2 | [Inventory and Configuration](2%20-%20Inventory%20and%20Configuration.md) | Hosts, groups, inventory variables, ansible.cfg, ad hoc commands. |
| 3 | [Playbooks Tasks and Modules](3%20-%20Playbooks%20Tasks%20and%20Modules.md) | YAML playbooks, plays, tasks, modules, become, check mode. |
| 4 | [Variables Facts Templates and Handlers](4%20-%20Variables%20Facts%20Templates%20and%20Handlers.md) | Variables, facts, Jinja2 templates, handlers, conditionals, loops. |
| 5 | [Roles Collections and Reuse](5%20-%20Roles%20Collections%20and%20Reuse.md) | Reusable structure, roles, collections, Galaxy, project layout. |
| 6 | [Vault Troubleshooting and Best Practices](6%20-%20Vault%20Troubleshooting%20and%20Best%20Practices.md) | Secrets, Ansible Vault, debugging, dry runs, common mistakes. |

## Mental Model

```text
inventory says where -> playbook says what -> modules do the work -> Ansible reports changed/ok/failed
```

## Official References

- Ansible documentation: <https://docs.ansible.com/ansible/latest/>
- Basic concepts: <https://docs.ansible.com/ansible/latest/getting_started/basic_concepts.html>
- Inventory guide: <https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html>
- Playbook guide: <https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html>
- Ansible Vault: <https://docs.ansible.com/ansible/latest/vault_guide/index.html>

