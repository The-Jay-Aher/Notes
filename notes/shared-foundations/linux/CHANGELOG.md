# Linux Notes Changelog

## 2026-11-24

- Created [1 - Users Groups and File Permissions](1%20-%20Users%20Groups%20and%20File%20Permissions.md), [2 - Processes Ports and Signals](2%20-%20Processes%20Ports%20and%20Signals.md) and [3 - systemd and journald](3%20-%20systemd%20and%20journald.md). The placement quiz and the first spaced review (2026-11-23 and 2026-11-24) showed gaps in the permission first-match rule, `ss -ltnp`, the `enable` symlink and `daemon-reload`, and the vault had no Linux notes beyond Bash. Written in the plain-language style the learner asked for: an analogy first, terms defined before use, short parts with worked examples.
- Created [INDEX](INDEX.md) for the folder. [Bash](Bash.md) is unchanged.
- Points marked to verify against current docs: default umask per distribution; the ACL mask detail; `net.ipv4.ip_unprivileged_port_start`; default grace periods (`docker stop` 10 s, Kubernetes 30 s, systemd `TimeoutStopSec` 90 s); systemd unit paths on merged-/usr distributions; systemd's special exit codes (`203/EXEC`, `217/USER`, `200/CHDIR`); `StartLimitBurst` and `StartLimitIntervalSec` defaults; `ExecStart=` path search in recent versions; journal persistence defaults per distribution; journal reader groups; the kubeadm `10-kubeadm.conf` drop-in path; `fsGroup` support per volume type; SELinux audit commands.
