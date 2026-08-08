# 6 - Vault Troubleshooting and Best Practices

## Quick Summary

Ansible Vault encrypts sensitive files or variables so they can be stored more safely with playbooks. Troubleshooting Ansible usually means checking inventory, SSH, privilege escalation, variable values, module docs, and playbook output.

## Ansible Vault

Encrypt a file:

```bash
ansible-vault encrypt secrets.yml
```

Edit encrypted file:

```bash
ansible-vault edit secrets.yml
```

Decrypt:

```bash
ansible-vault decrypt secrets.yml
```

Run playbook with vault prompt:

```bash
ansible-playbook -i inventory.ini site.yml --ask-vault-pass
```

Use password file:

```bash
ansible-playbook -i inventory.ini site.yml --vault-password-file .vault-pass
```

Do not commit `.vault-pass`.

## Encrypt A Single Variable

```bash
ansible-vault encrypt_string 'my-secret-password' --name 'db_password'
```

Output can be placed in YAML variable files.

## What To Encrypt

Encrypt:

- Passwords.
- API tokens.
- Private keys.
- Sensitive connection strings.
- Certificates if private/sensitive.

Do not encrypt everything blindly; it makes reviews difficult. Encrypt only sensitive values/files.

## Troubleshooting Flow

1. Confirm inventory target.
2. Test connectivity with ping module.
3. Check SSH user/key/port.
4. Check privilege escalation.
5. Run with `-v`, `-vv`, or `-vvv`.
6. Inspect variable values.
7. Read module docs.
8. Try check mode/diff mode where safe.

## Useful Debug Commands

```bash
ansible all -i inventory.ini -m ping
ansible-inventory -i inventory.ini --graph
ansible-inventory -i inventory.ini --host web1
ansible-config dump --only-changed
ansible-playbook -i inventory.ini site.yml --check --diff
ansible-playbook -i inventory.ini site.yml -vvv
ansible-doc ansible.builtin.copy
```

## Common Failure Areas

| Symptom | Likely Cause |
| --- | --- |
| `UNREACHABLE` | SSH/network/user/key/firewall problem. |
| Permission denied | Wrong user/key or missing sudo/become. |
| Module not found | Missing collection or wrong FQCN. |
| Undefined variable | Scope, spelling, inventory, group_vars/host_vars. |
| Task always changed | Non-idempotent command/shell task. |
| Vault password error | Wrong vault password or missing vault option. |

## Best Practices

- Use clear inventory groups.
- Keep playbooks readable.
- Prefer modules over shell.
- Use roles for reusable logic.
- Use Vault or external secret management for secrets.
- Test with `--check` where supported.
- Use `--diff` for file changes, but avoid leaking secrets.
- Pin role/collection dependencies.
- Keep automation in version control.
- Review changes before running against production.

## Production Safety

Before running against production:

- Confirm inventory.
- Limit hosts if needed:

```bash
ansible-playbook -i prod.ini site.yml --limit web1
```

- Use check mode.
- Review diffs.
- Confirm backups for risky changes.
- Use serial/rolling updates for fleets.

Example rolling update:

```yaml
- name: Rolling web update
  hosts: web
  serial: 2
  tasks:
    - name: Update package
      ansible.builtin.apt:
        name: nginx
        state: latest
```

## Benefits

- Vault protects secrets better than plaintext.
- Debug flags expose useful execution details.
- Check/diff mode improves review.
- Idempotent playbooks are safer to rerun.

## Drawbacks / Limitations

- Vault password handling still needs process discipline.
- Encrypted files are harder to review.
- Check mode is not supported equally by all modules.
- Verbose logs can contain sensitive data.

## Hidden Details / Caveats

- Vault encrypts content, not the filename.
- Anyone with vault password can decrypt.
- Do not put vault password files in Git.
- Extra vars can override many other variables.
- `--limit` can save you from targeting too many hosts.
- `serial` controls batch size for rolling changes.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Committing vault password file | Add to `.gitignore` and rotate if leaked. |
| Encrypting all vars | Encrypt only secrets. |
| Running prod playbook without limit/check | Start small and verify. |
| Debug output prints secrets | Avoid debug on secret vars. |
| Using `state: latest` everywhere | Prefer pinned versions or planned updates. |

## Interview Notes

- Ansible Vault encrypts sensitive files/variables.
- `--ask-vault-pass` prompts for vault password.
- `--check` previews changes where supported.
- `--diff` shows file changes.
- `-vvv` increases debug output.
- `serial` enables rolling execution.
- `--limit` restricts target hosts.

## Related Topics

- [Inventory and Configuration](2%20-%20Inventory%20and%20Configuration.md)
- [Roles Collections and Reuse](5%20-%20Roles%20Collections%20and%20Reuse.md)

## Official References

- [Ansible Vault guide](https://docs.ansible.com/ansible/latest/vault_guide/index.html)
- [Ansible playbook command reference](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)
- [Ansible troubleshooting](https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html)
