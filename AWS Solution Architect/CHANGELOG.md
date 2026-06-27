# AWS Solution Architect Changelog

## 2026-06-28

### Upgraded

- Merged the three High Availability and Scalability ELB/ASG chapter variants into one canonical file: [6 - High Availability and Scalability ELB and ASG](6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md).
- Removed the typo-named duplicate `6 - High Availabilty and Scalability ELB & ASG.md` after preserving its unique content in the canonical chapter.
- Removed the Manual folder duplicate `Manual/6 - High Availability and Scalability (ELB & ASG).md` after preserving its unique content in the canonical chapter.

### Major Improvements

- Converted the chapter from short service notes into a deep SAA-ready explanation covering first principles, causal chains, ALB/NLB/GWLB/CLB selection, health checks, sticky sessions, cross-zone behavior, TLS/SNI, connection draining, ASG capacity, scaling policies, cooldowns, lifecycle hooks, instance refresh, troubleshooting, exam traps, practice questions, and glossary.
- Added Mermaid diagrams for ELB/ASG architecture, request flow, and troubleshooting.
- Added official AWS source links and marked version-sensitive behavior such as cross-zone defaults, pricing, NLB security group behavior, quotas, and AWS feature changes for current verification.

### Preservation Notes

- Existing details from the main chapter, the typo-named chapter, and the Manual chapter were union-merged.
- Repeated material was consolidated instead of duplicated.
- Obvious spelling mistakes and ambiguous phrases from the source notes were corrected while preserving the underlying facts.

### Verify Later

- Recheck official AWS documentation for load balancer feature support, pricing, quotas, cross-zone behavior, certificate behavior, and SAA exam guide changes before production use or exam booking.

## 2026-05-27

### Upgraded

- Added [28 - SAA-C03 Alignment Audit and Scenario Playbook](28%20-%20SAA-C03%20Alignment%20Audit%20and%20Scenario%20Playbook.md).
- Added [29 - SAA-C03 Practice Questions and Rationales](29%20-%20SAA-C03%20Practice%20Questions%20and%20Rationales.md).
- Added [30 - SAA-C03 Rapid Revision Cheatsheet and Glossary](30%20-%20SAA-C03%20Rapid%20Revision%20Cheatsheet%20and%20Glossary.md).
- Updated [INDEX](INDEX.md) with the 2026-05-27 source snapshot and final SAA revision path.

### Major Improvements

- Refreshed the SAA-C03 exam alignment against the official AWS exam guide.
- Added official domain weights: secure architectures 30%, resilient architectures 26%, high-performing architectures 24%, cost-optimized architectures 20%.
- Added scenario reasoning chains for security, resilience, performance, and cost decisions.
- Added practice questions with rationales to train exam-style elimination rather than memorized service names.
- Added rapid service-decision clues, traps, patterns, and glossary terms.

### Preservation Notes

- Existing 27 service chapters were preserved because they already cover the main AWS SAA service families.
- The upgrade adds an exam-alignment layer instead of duplicating existing service explanations.

### Verify Later

- Recheck the official AWS SAA-C03 guide before booking or revising for the exam.
- Recheck service-specific docs for pricing, quotas, new features, deprecations, and managed-service behavior.
