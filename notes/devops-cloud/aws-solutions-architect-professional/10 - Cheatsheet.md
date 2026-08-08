# 10 - SAP-C02 Cheatsheet

## Exam Domains

| Domain | Weight |
| --- | --- |
| Organizational complexity | 26% |
| New solutions | 29% |
| Continuous improvement | 25% |
| Migration and modernization | 20% |

Source checked: official AWS SAP-C02 guide on 2026-05-27.

## Decision Keywords

| Wording | Usually points toward |
| --- | --- |
| all accounts / future accounts | Organizations, SCP, Control Tower pattern |
| grant access | IAM policy, resource policy, role trust |
| maximum permissions | SCP or permission boundary |
| least operational overhead | managed service |
| minimal application change | rehost/replatform |
| strict RTO/RPO | warm standby / active-active depending target |
| private AWS service access | VPC endpoints / PrivateLink |
| many VPCs | Transit Gateway / Cloud WAN |
| dedicated connectivity | Direct Connect |
| encrypted quick hybrid link | VPN |

## Guardrail Rules

- SCPs do not grant permissions.
- Permission boundaries do not grant permissions.
- IAM policies grant within boundaries.
- Resource policies can enable cross-account access depending service.
- Central logs should be protected from workload accounts.

## DR Quick Map

| Pattern | Cost | Recovery |
| --- | --- | --- |
| Backup/restore | lowest | slow |
| Pilot light | low-medium | moderate |
| Warm standby | medium | faster |
| Active-active | highest | fastest/complex |

