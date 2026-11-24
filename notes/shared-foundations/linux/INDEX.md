# Linux Fundamentals

## Quick Summary

These notes cover the Linux you need on every server, container and Kubernetes node: who may touch which file, how to find and stop processes, and how services start at boot and log. Each chapter opens with an everyday analogy, defines every term before using it, and ends with self-test questions whose answers are hidden until you try.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [Users, Groups and File Permissions](1%20-%20Users%20Groups%20and%20File%20Permissions.md) | Users and groups, reading `-rwxr-x---`, the first-match rule (exactly one of owner, group and others applies), octal modes, `chmod` and `chown`, directories versus files, umask, setuid, setgid and sticky, ACLs. |
| 2 | [Processes, Ports and Signals](2%20-%20Processes%20Ports%20and%20Signals.md) | `ps` and `top`, listening on `127.0.0.1` versus `0.0.0.0`, finding who holds a port with `ss -ltnp` and `lsof`, SIGTERM before SIGKILL, zombies, and PID 1 in containers. |
| 3 | [systemd and journald](3%20-%20systemd%20and%20journald.md) | Unit files, `start` versus `enable` (the symlink), `daemon-reload`, reading `systemctl status`, `Restart=`, `journalctl` filters, journal persistence, and a boot troubleshooting flowchart. |
| 4 | [Bash](Bash.md) | Shell scripting: commands, quoting, variables, exit codes and `set -euo pipefail`. |
| Log | [CHANGELOG](CHANGELOG.md) | Change history and points to verify. |

## Related Notes

- [Networking in Plain Language](../networking/0%20-%20Networking%20in%20Plain%20Language.md): "connection refused" versus "timed out" pairs with chapter 2.
- [Ansible: Playbooks, Tasks and Modules](../../devops-cloud/ansible/3%20-%20Playbooks%20Tasks%20and%20Modules.md): the `file`, `user` and `systemd` modules are these chapters written as desired state.
- [CKA Troubleshooting](../../devops-cloud/cka/6%20-%20Troubleshooting.md): kubelet is a systemd service.
