# 11 - SAP-C02 Glossary

| Term | Meaning | Exam trap |
| --- | --- | --- |
| Organization | AWS multi-account hierarchy. | One-account thinking. |
| OU | Organizational unit grouping accounts. | Bad grouping causes policy sprawl. |
| SCP | Maximum permission guardrail. | Does not grant permissions. |
| Permission boundary | Max permissions for IAM identity. | Does not grant permissions. |
| Landing zone | Governed multi-account baseline. | Not only account creation. |
| Transit Gateway | Routing hub for VPC/hybrid connectivity. | Route table segmentation matters. |
| Direct Connect | Dedicated private connectivity. | Not encrypted by default at Layer 3. |
| VPN | Encrypted tunnel over network path. | Internet VPN has path variability. |
| RTO | Time to recover. | Drives standby pattern. |
| RPO | Data loss window. | Drives replication/backup. |
| Rehost | Lift and shift. | Fast but not modernized. |
| Replatform | Modest optimization. | Still needs compatibility checks. |
| Refactor | Redesign application. | High effort/risk. |
| Well-Architected | AWS architecture review framework. | Not just reliability. |

## Questions to Test Understanding

1. What does an SCP do?
2. What does Direct Connect not automatically provide?
3. What does RPO measure?
4. What migration strategy changes least?
5. What pattern replaces VPC peering mesh at scale?

## Answers and Reasoning

1. Sets maximum available permissions for accounts/OUs.
2. Layer 3 encryption.
3. Acceptable data loss window.
4. Rehost.
5. Transit Gateway or broader network hub pattern.

