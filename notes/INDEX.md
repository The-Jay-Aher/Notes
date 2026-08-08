# Study Notes Index

This is the main catalogue for subject notes. Each category owns a distinct kind of knowledge so that a note has one predictable home.

| Category | Use it for | Main tracks |
| --- | --- | --- |
| [DevOps and cloud](devops-cloud/INDEX.md) | Infrastructure, delivery, platforms, cloud architecture, and certifications | AWS, Kubernetes, CKA, CKAD, Docker, Terraform, Ansible, Jenkins, Argo CD, GitHub Actions, DevSecOps |
| [Programming](programming/INDEX.md) | Languages, algorithms, data structures, and software design | Java, Python, C++, competitive programming, low-level design |
| [Competitive exams](competitive-exams/INDEX.md) | Exam-specific syllabi, static subjects, current affairs, strategies, and revision | UPSC, MPSC, RBI Assistant, RBI Grade B, SEBI Grade A |
| [Shared foundations](shared-foundations/INDEX.md) | Concepts reused across several technical tracks | Networking, Linux/Bash, Markdown |
| [Finance and trading](finance-trading/INDEX.md) | Market education, research methods, strategy notes, and risk governance | Fundamental analysis, positional trading, probabilistic trading, workbooks |

## Placement Test

Use this decision rule when adding a note:

```text
Is it tied to one exam or certification?
├── Yes → that exam or certification folder
└── No
    ├── Reused by several technical tracks? → shared-foundations
    ├── Cloud, delivery, or platform operations? → devops-cloud
    ├── Language, algorithm, or software design? → programming
    └── Markets, trading, or investment research? → finance-trading
```

Personal tasks and private references do not belong here; file them through the [personal index](../personal/INDEX.md).
