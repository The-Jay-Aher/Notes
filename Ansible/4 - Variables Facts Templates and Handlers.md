# 4 - Variables Facts Templates and Handlers

## Quick Summary

Variables make playbooks reusable. Facts are host details Ansible gathers. Templates generate files from variables. Handlers run only when notified by changed tasks, commonly to restart services after config changes.

## Variables

Example:

```yaml
app_port: 8080
app_user: app
```

Use:

```yaml
- name: Print app port
  ansible.builtin.debug:
    msg: "App listens on {{ app_port }}"
```

## Where Variables Can Live

- Inventory.
- `group_vars/`.
- `host_vars/`.
- Playbook `vars`.
- Role defaults.
- Role vars.
- Extra vars.
- Facts.
- Registered task output.

Variable precedence can be complex. When confused, inspect host variables:

```bash
ansible-inventory -i inventory.ini --host web1
```

## Facts

Facts are data about managed hosts.

```yaml
- name: Show OS family
  ansible.builtin.debug:
    msg: "{{ ansible_facts['os_family'] }}"
```

Gathering facts is enabled by default.

Disable if not needed:

```yaml
- name: Fast play
  hosts: all
  gather_facts: false
```

## Registered Variables

```yaml
- name: Check disk
  ansible.builtin.command: df -h /
  register: disk_output

- name: Print output
  ansible.builtin.debug:
    var: disk_output.stdout
```

Registered values are useful for conditionals and debugging.

## Conditionals

```yaml
- name: Install nginx on Debian family
  ansible.builtin.apt:
    name: nginx
    state: present
  when: ansible_facts['os_family'] == 'Debian'
```

## Loops

```yaml
- name: Install packages
  ansible.builtin.apt:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - curl
    - git
```

## Templates

Templates use Jinja2.

Template file `templates/app.conf.j2`:

```jinja2
port={{ app_port }}
environment={{ app_env }}
```

Task:

```yaml
- name: Render app config
  ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app/app.conf
    mode: "0644"
  notify: Restart app
```

## Handlers

Handlers run when notified by changed tasks.

```yaml
handlers:
  - name: Restart app
    ansible.builtin.service:
      name: app
      state: restarted
```

Why handlers matter:

- Restart only when config changed.
- Avoid unnecessary service restarts.
- Keep playbooks efficient and safe.

## Benefits

- Variables avoid hard-coded values.
- Facts adapt tasks to host details.
- Templates generate config files cleanly.
- Handlers reduce unnecessary restarts.

## Drawbacks / Limitations

- Variable precedence can confuse beginners.
- Facts can slow runs.
- Templates can hide syntax errors until rendered.
- Handlers run later, which can surprise people.

## Hidden Details / Caveats

- Extra vars have very high precedence.
- Handlers run once even if notified multiple times.
- Handlers usually run at the end of a play.
- Templates should not include plaintext secrets unless encrypted/protected.
- Undefined variables fail unless defaults are used.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Hard-coding environment values | Use variables. |
| Restarting service every run | Use handler notified by template/copy change. |
| Secret variables in plain YAML | Use Vault. |
| Confusing variable source | Inspect inventory and precedence. |
| Missing quotes around Jinja values in YAML | Quote values like `"{{ var }}"`. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| Variable undefined | Inventory/group_vars/host_vars, spelling, scope. |
| Wrong variable value | Precedence and inventory output. |
| Template error | Jinja syntax, undefined values. |
| Handler not running | Did notifying task report changed? Is handler name exact? |
| Task skipped unexpectedly | `when` condition and fact values. |

## Interview Notes

- Variables make playbooks reusable.
- Facts are gathered host data.
- Templates use Jinja2.
- Handlers run when notified by changed tasks.
- `register` stores task result.
- `when` adds conditions; `loop` repeats tasks.

## Related Topics

- [Inventory and Configuration](2%20-%20Inventory%20and%20Configuration.md)
- [Playbooks Tasks and Modules](3%20-%20Playbooks%20Tasks%20and%20Modules.md)

## Official References

- [Using variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html)
- [Discovering variables: facts and magic variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_vars_facts.html)
- [Templating with Jinja2](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html)
- [Handlers](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_handlers.html)
