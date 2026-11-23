---
tags:
  - study/revision
  - study/plan
status: active
created: 2026-11-18
updated: 2026-11-23
---

# Learning Plan: November 2026 to May 2027

This plan answers one question: given what you already do well as a DevOps engineer, what should you learn next, in what order, and how will you know each stage is finished? It is built from your resume, your mentor notes, your to-do list and the state of this vault on 2026-11-18. The [Learning Tracker](Learning%20Tracker.md) records how each session actually goes; this file says where those sessions are heading.

## Assumptions

The plan rests on four assumptions. If one is wrong, the order changes, so correct it before Week 1.

1. **The goal is to grow as a DevOps or platform engineer** and be ready for mid-level DevOps, SRE or platform interviews by spring 2027. The competitive-exam tracks (UPSC, MPSC, RBI, SEBI) and trading-strategy research are paused. If you are actively preparing for an exam, it competes for the same hours and the plan has to be rebalanced.
2. **Time budget is about 11 hours a week**: 60 to 75 minutes on weekdays, 3 hours on Saturday, 45 minutes on Sunday. The older six-week checklist assumed 3 to 4 hours every weekday and reached 4 of its 225 items, which suggests that budget was too heavy alongside a full-time job.
3. **You have not taken the CKA yet.** The vault holds a one-line note titled "Passed CKA with 88%", but it has no detail and your resume lists only Terraform Associate and AWS Cloud Practitioner, so it reads like a saved post. If it is your result, Phase 2 becomes CKAD or CKS instead.
4. **You can use a personal AWS account** for labs, with a budget alarm set before the first lab.

## Where you stand

| Area | Evidence | Verdict |
| --- | --- | --- |
| CI/CD with GitHub Actions and Jenkins, quality gates | Designed and ran production pipelines; large runtime reduction | Strong. Maintain, don't study. |
| Containers on AWS: Docker, ECR, ECS, EFS, EventBridge, Step Functions | Moved a single-server application onto ECS tasks | Strong |
| CloudFormation, Git and SCM migration, scripting | Used at work, scripts reused across teams | Strong |
| Ansible | Used at work; KodeKloud course in progress (config files, precedence, YAML so far); 7 vault chapters | Working knowledge. Deepen it on Saturdays (see the Ansible thread in Phase 1). |
| AWS breadth and architecture | Cloud Practitioner; daily use of a slice of AWS; SAA notes are deep but the SAA checklist is barely started | In progress. Finish it. |
| Networking fundamentals | Marked "in progress" in the mentor notes and still open in the to-do list. Placement quiz on 2026-11-23: 1.0 / 4 (25%). | **The recurring gap**, confirmed |
| Kubernetes | On the resume's skills line, no project behind it | **The biggest market gap** |
| Terraform | Certified, but work uses CloudFormation | Theory without practice |
| Prometheus, Grafana, Loki | Listed; production monitoring was Dynatrace and CloudWatch | Theory without practice |
| Data structures and algorithms | The Competitive-Programming repo has a handful of files since 2024 | Not started |
| Linux | Daily use, but placement quiz on 2026-11-23: 1.25 / 4 (31%). Permissions, exit codes, and ports and signals were weak; systemd was solid. The vault has no Linux notes beyond Bash. | **Needs its own block** alongside networking |

The pattern matters more than any single row. **Everything under your resume's Experience section is strong. Three things under Skills (Kubernetes, Terraform, and Prometheus with Grafana and Loki) have no experience bullet behind them.** An interviewer reads a resume the same way: they probe the claims that have no story attached. This plan turns each of those three into something you have built and can defend.

## What to start with: networking, and why

Start with networking, taught through AWS, then carry it straight into the AWS Solutions Architect Associate (SAA).

The chain of reasons:

- **Networking is the dependency under everything that follows.** In the SAA, VPC design, routing, NAT, endpoints, Route 53 and load balancers show up inside a large share of scenario questions, even ones that look like they are about databases or containers. In the CKA, Services, DNS, CNI plugins, Ingress and NetworkPolicy are all networking, and the largest exam domain, troubleshooting, is mostly "why can't A reach B?" In interviews, "what happens when you open a URL?" and "the container can't reach the database, what do you check?" are standard.
- **Without it, you memorize service names but can't reason when something breaks.** You will pick NAT gateway over VPC endpoint because a flashcard said so, not because you can see the packet's path.
- **It has been open the longest.** It appears in your mentor notes and your current to-do list. Unfinished foundations do not stay small; they make every later topic slower.
- **You already have the hook.** At work you enabled SSH, SCP and SMTP from ECS containers. Networking is finished when you can answer this from memory:

> [!question] Anchor question for networking
> An ECS task in a private subnet sends an email through an external SMTP server. Name every hop and every control the connection passes: DNS resolution, the route table entry, the NAT gateway, the security group and network ACL rules in both directions, the ports, and what changes if the SMTP server is reached through a VPC endpoint or a VPN instead.

Why SAA before the CKA: the SAA notes are the most developed track in this vault, the exam validates the AWS work you do every day, it forces the networking study that the CKA reuses, and finishing a goal already in motion costs less than restarting momentum on a new one.

## The plan at a glance

| Phase | Weeks | Dates | Outcome | Proof that it is done |
| --- | --- | --- | --- | --- |
| 0. Placement | Done | 18 to 23 Nov 2026 | Know what you can skip | Done: 2.25 / 8, results in the tracker |
| 1. Networking, Linux and AWS SAA | 1 to 9 | 23 Nov 2026 to 24 Jan 2027 | SAA certified, foundations solid | Two consecutive timed practice exams at 80% or more, then the exam |
| 2. Kubernetes and CKA | 10 to 17 | 25 Jan to 21 Mar 2027 | CKA certified | Simulator sessions finished in time, then the exam |
| 3. Capstone platform project | 18 to 23 | 22 Mar to 2 May 2027 | A public repository you can demo | Someone else can deploy and tear it down from your README |
| Running track: interview readiness | All | Throughout | Pass DevOps and SRE screens | Medium problems in about 30 minutes; every resume bullet defended |

## Phase 0: Placement (done 23 November 2026)

1. **Placement quiz: 2.25 / 8.** Networking 1.0 / 4 and Linux 1.25 / 4. The networking questions stopped after four, because no result on the rest could have reached the 80% that would shorten the networking block. Two patterns showed up, and Phase 1 now targets both:
   - **Errors read as "connectivity is broken" instead of "how far did the request get?"** "Connection refused" proves the host was reached; an expired certificate proves DNS and TCP worked; any HTTP status code proves the whole network path worked.
   - **Tools known by name from daily use, but not the mechanism underneath.** Examples: the octal 750 was right, but the permission string wasn't read correctly; subnets were assumed to be /24; script behaviour was predicted from intent rather than exit codes; `ps` was used to look for a port.

   Result: networking keeps its full time and grows to three weeks, a Linux block runs alongside it, and Phase 1 grows from eight weeks to nine. Every later date moves by one week.
2. **Decide on the CKA voucher.** Your older plan intended to buy it in the Black Friday sale; Black Friday is 27 November 2026 and Cyber Monday is 30 November. Before buying, check the price, whether a free retake and simulator sessions are included, and how long the voucher stays valid. Historically it has been 12 months from purchase; verify for currency on the Linux Foundation site. Buying commits you to the exam; you schedule the date later.
3. **Set up a safe lab environment**: an AWS budget with an email alarm, MFA on the root user, an IAM user or SSO role for daily work, and a local Kubernetes cluster with `kind` for later.

## Phase 1: Networking, Linux and AWS SAA (Weeks 1 to 9)

In Weeks 1 and 2, networking takes Monday, Wednesday and Friday and Linux takes Tuesday and Thursday. The vault has no Linux notes beyond Bash yet, so the Linux reference is the standard documentation: `man chmod`, `man 7 signal`, `man systemctl`, `man journalctl` and `man ss`.

| Week | Dates | Topic | Vault notes |
| --- | --- | --- | --- |
| 1 | 23 to 29 Nov | **Networking I:** IP addressing, CIDR block sizes and ranges by hand, routing and longest prefix match, NAT, ports, DNS resolution. **Linux I:** users, groups and permissions (which of owner, group and others applies, octal modes); processes and signals (`ps`, `top`, SIGTERM versus SIGKILL). | [Fundamentals of Networking](../shared-foundations/networking/1%20-%20Fundamentals%20of%20Networking.md), [Internet Protocol](../shared-foundations/networking/2%20-%20Internet%20Protocol%20%28IP%29.md) |
| 2 | 30 Nov to 6 Dec | **Networking II:** how a request travels (DNS, then TCP, then TLS, then HTTP) and what each error proves about how far it got: refused versus timed out, certificate errors, HTTP status codes. Lab: `dig`, `curl -v`, `traceroute`, `ss`, `nc`. **Linux II:** systemd and journald; sockets and ports with `ss` and `lsof`; disk usage; exit codes and `set -euo pipefail`. | [Fundamentals of Networking](../shared-foundations/networking/1%20-%20Fundamentals%20of%20Networking.md) ("HTTP And HTTPS", "Troubleshooting Flow"), [Bash](../shared-foundations/linux/Bash.md) |
| 3 | 7 to 13 Dec | **Networking III on AWS:** VPC, subnets and the five reserved addresses, route tables, internet and NAT gateways, security groups versus network ACLs (both drop silently, so they cause timeouts), VPC endpoints, peering versus Transit Gateway, Route 53, Layer 4 versus Layer 7 load balancing. Two Linux troubleshooting drills. Finish with the anchor question above and a re-quiz of the placement misses. | [Networking VPC](../devops-cloud/aws-solutions-architect-associate/26%20-%20Networking%20VPC.md), [Route 53](../devops-cloud/aws-solutions-architect-associate/8%20-%20Route%2053.md), [ELB and ASG](../devops-cloud/aws-solutions-architect-associate/6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md) |
| 4 | 14 to 20 Dec | Compute and storage: EC2, EBS, instance store, EFS, S3 and its security. Much of this is review for you, so go fast and focus on "when should I *not* choose this?" | SAA notes 3 to 5, 10 to 12, 14 |
| 5 | 21 to 27 Dec | Holiday week, lighter: identity, encryption, monitoring and audit. | SAA notes 12, 23 to 25 |
| 6 | 28 Dec to 3 Jan | Databases and caching, decoupling with SQS, SNS and Kinesis, containers and serverless. You know ECS from work; use it to learn the exam's tradeoff framing. | SAA notes 7, 16 to 20 |
| 7 | 4 to 10 Jan | Resilience and disaster recovery, CloudFront and Global Accelerator, migration and transfer, analytics and ML at awareness level. | SAA notes 13, 15, 21, 22, 27 |
| 8 | 11 to 17 Jan | Scenario reasoning, then the first full timed practice exam. Every miss becomes a tracker item. | [Scenario Playbook](../devops-cloud/aws-solutions-architect-associate/28%20-%20SAA-C03%20Alignment%20Audit%20and%20Scenario%20Playbook.md), [Practice Questions](../devops-cloud/aws-solutions-architect-associate/29%20-%20SAA-C03%20Practice%20Questions%20and%20Rationales.md) |
| 9 | 18 to 24 Jan | More timed exams, final pass with the cheatsheet. Book the exam once two consecutive timed exams reach 80%. | [Rapid Revision Cheatsheet](../devops-cloud/aws-solutions-architect-associate/30%20-%20SAA-C03%20Rapid%20Revision%20Cheatsheet%20and%20Glossary.md) |

**Saturday lab thread: Terraform.** This is what turns your Terraform certificate into experience. Over the nine Saturdays, rebuild the shape of the system you run at work, in your own account and in Terraform: a VPC with public and private subnets across two Availability Zones, an Application Load Balancer, an ECS Fargate service running an image from ECR, a secret from Secrets Manager, an EventBridge scheduled task and CloudWatch logs. Keep state in a remote backend with locking. Run `terraform destroy` at the end of every session, because a forgotten NAT gateway bills by the hour.

**Saturday lab thread: Ansible (the last hour of the Saturday block, Weeks 1 to 7).** The Saturday split becomes about two hours of Terraform and one hour of Ansible. They answer two different questions, which is why they pair well: **Terraform creates the machines and networks; Ansible walks into a machine that already exists and sets it up**: users, files, packages, services. An analogy: Terraform builds and furnishes the empty flat; Ansible is the checklist a housekeeper follows every visit, and only does what isn't already done. That "only what isn't done" property is called **idempotency**, and it's the one idea the whole thread keeps coming back to.

The thread is also deliberately tied to the weekday Linux block. Every Ansible module is a Linux action written down: the `file` module is `chmod` and `chown`, the `user` module is `useradd`, the `systemd` module is `systemctl`. So each Saturday practises that week's Linux topic a second time, from a different angle. Keep going with the KodeKloud course at its own pace; this thread is the hands-on half that the course and the vault chapters feed into.

Setup: Ansible's control node (the machine you run `ansible-playbook` from) doesn't run natively on Windows, so install it inside WSL (Ubuntu). Until Week 3, practise against local targets (a Linux VM, or WSL talking to `localhost`); from Week 3, use an EC2 instance that your Terraform code creates.

| Week | Saturday | Ansible lab | Ties to | Vault notes |
| --- | --- | --- | --- | --- |
| 1 | 28 Nov | Install Ansible in WSL. Write an inventory and `ansible.cfg`; run ad hoc commands (`ansible all -m ping`, `-m command -a "id"`). Find out which `ansible.cfg` wins and why. | KodeKloud course so far | [Fundamentals](../devops-cloud/ansible/1%20-%20Ansible%20Fundamentals.md), [Inventory and Configuration](../devops-cloud/ansible/2%20-%20Inventory%20and%20Configuration.md) |
| 2 | 5 Dec | First playbook: create a group and a user, a directory with mode `0750`, and a script with mode `0755`. Run it twice: the first run says `changed`, the second says `ok`. Explain why. | Linux I: permissions | [Playbooks Tasks and Modules](../devops-cloud/ansible/3%20-%20Playbooks%20Tasks%20and%20Modules.md) |
| 3 | 12 Dec | Terraform creates one small EC2 instance in a public subnet, with a security group that allows SSH only from your home IP as a `/32`. Ansible installs nginx, writes its config from a Jinja2 template, and a **handler** restarts it only when the config changes. Confirm with `systemctl status` and `ss -ltnp`. | Linux II: systemd, ports; Networking III: security groups, `/32` | [Variables Facts Templates and Handlers](../devops-cloud/ansible/4%20-%20Variables%20Facts%20Templates%20and%20Handlers.md) |
| 4 | 19 Dec | Turn the Week 3 playbook into a **role** (a reusable folder with a fixed layout). Feed the instance's IP from `terraform output` into the inventory. | Reuse; Terraform outputs | [Roles Collections and Reuse](../devops-cloud/ansible/5%20-%20Roles%20Collections%20and%20Reuse.md) |
| 5 | 26 Dec | Holiday week, light: encrypt one secret with Ansible Vault and use it in the role. Never commit the vault password. | Identity and encryption week | [Vault Troubleshooting and Best Practices](../devops-cloud/ansible/6%20-%20Vault%20Troubleshooting%20and%20Best%20Practices.md) |
| 6 | 2 Jan | Idempotency drills: `--check --diff`; why `command` and `shell` always report `changed` and how `creates:` or `changed_when:` fix it; break a task on purpose and read the error with `-vvv`. | Troubleshooting habit | [Idempotency and Operational Runbooks](../devops-cloud/ansible/7%20-%20Idempotency%20Infrastructure%20Labs%20and%20Operational%20Runbooks.md) |
| 7 | 9 Jan | Replace the hand-written inventory with the `amazon.aws.aws_ec2` dynamic inventory plugin, so Ansible finds instances by tag. Then pause the thread. | AWS tags, IAM | [Inventory and Configuration](../devops-cloud/ansible/2%20-%20Inventory%20and%20Configuration.md) |

Weeks 8 and 9 have no Ansible: those Saturdays go to timed SAA practice exams. Ansible items stay in `/revise` so they don't fade, and the thread comes back in Week 14.

**Ansible exit criteria:** you can write a role from scratch that sets up a fresh server and reports `changed=0` on its second run; explain why a `command` task breaks idempotency and fix it; say which of two variables wins in the common cases (inventory, play vars, `-e`); keep a secret in Ansible Vault; and debug a failed task from its error message. Before the labs, check which Ansible version WSL installs; ansible-core 2.19 (Ansible 12) changed templating, so match the docs to your version (verify against current docs).

The older [six-week checklist](../finance-trading/study-plans/aws_saa_trading_bot_plan_checklist_v2.md) is still useful as a list of daily AWS tasks, and its trading safety gate still applies. This plan replaces its schedule and its daily Terraform cadence.

**Exit criteria:** you can give the size and range of any CIDR block on paper, answer the anchor question without notes, and name the step that failed from any `curl -v` error. On Linux, you can read any permission string, predict a script's exit code under `set -euo pipefail`, find which process holds a port and stop it gracefully, and diagnose a systemd service that fails at boot. Finally, you score 80% or more on two consecutive timed practice exams. Verify the current exam code, domain weights and passing score (historically 720 out of 1000) in the AWS exam guide before booking; the vault last checked it on 2026-05-27.

## Phase 2: Kubernetes and CKA (Weeks 10 to 17)

Why Kubernetes now: it is on your resume with nothing behind it, it is widely required in DevOps and platform job descriptions, and the CKA is a hands-on exam, so passing it is evidence rather than a claim. Why the CKA before the CKAD: the CKA covers cluster operations (installing, upgrading, backing up etcd, troubleshooting nodes), which is the work a DevOps engineer owns. The CKAD overlaps heavily and becomes a short add-on later if a role asks for it.

**Bridge from ECS.** You already think in ECS. Use that, then note exactly where the analogy breaks, because the breaks are what the exam tests.

| ECS concept | Kubernetes counterpart | Where the analogy breaks |
| --- | --- | --- |
| Task definition | Pod template inside a Deployment | You control placement yourself with requests, limits, affinity, taints and tolerations. |
| Service with a desired count | Deployment and ReplicaSet | Reconciliation is a general pattern every controller follows, not a feature of one service. |
| Load balancer target group | Service, plus Ingress or Gateway API | A Service is a virtual IP programmed on every node by kube-proxy or an eBPF data plane, not a load-balancer box. |
| Task IAM role | ServiceAccount; on EKS, IRSA or Pod Identity | RBAC governs the Kubernetes API and IAM governs AWS. They are two separate permission systems. |
| EFS volume | PersistentVolume and PersistentVolumeClaim through a CSI driver | StorageClasses and dynamic provisioning have no direct ECS equivalent. |
| EventBridge scheduled task | CronJob | Missed schedules and concurrency policy are your problem now. |
| Control plane run by AWS | Control plane you install and upgrade with kubeadm | **The biggest new thing.** etcd, the API server, the scheduler and controller manager are yours. |

| Week | Dates | Topic | Vault notes |
| --- | --- | --- | --- |
| 10 | 25 to 31 Jan | Architecture and reconciliation. Lab: a `kind` cluster; delete Pods and watch a Deployment heal itself. | [Desired State and Reconciliation](../devops-cloud/kubernetes/01%20-%20Desired%20State%20and%20Reconciliation.md), Kubernetes notes 02 and 03, CKA note 0 |
| 11 | 1 to 7 Feb | Workloads and scheduling | CKA note 3, Kubernetes note 04 |
| 12 | 8 to 14 Feb | Services and networking: DNS, NetworkPolicy, Ingress and Gateway API. Phase 1 pays off here. | CKA note 4, [Service Networking](../devops-cloud/kubernetes/05%20-%20Service%20Networking%20DNS%20and%20Traffic%20Flow.md) |
| 13 | 15 to 21 Feb | Storage, RBAC, ServiceAccounts, TLS | CKA note 5, Kubernetes notes 06 and 07 |
| 14 | 22 to 28 Feb | Cluster lifecycle on two or three VMs: kubeadm install, version upgrade, etcd backup and restore. Do each three times from memory. Saturday: once the manual install is solid, write an Ansible playbook that prepares fresh nodes for kubeadm (container runtime, kernel modules, sysctl settings, swap, pinned kubeadm, kubelet and kubectl packages; check each step against the current kubeadm install docs). Keep practising the manual steps, because the exam has no Ansible. | [Cluster Architecture, Installation and Configuration](../devops-cloud/cka/2%20-%20Cluster%20Architecture%20Installation%20and%20Configuration.md) |
| 15 | 1 to 7 Mar | Troubleshooting: break things on purpose, then fix them. The kubelet is a systemd service, so the Linux block pays off here. | [CKA Troubleshooting](../devops-cloud/cka/6%20-%20Troubleshooting.md), [Failure Modes and Flowcharts](../devops-cloud/kubernetes/08%20-%20Failure%20Modes%20and%20Troubleshooting%20Flowcharts.md) |
| 16 | 8 to 14 Mar | Speed: imperative commands, `kubectl explain`, finding things in the docs fast. First simulator session. | [Command Labs](../devops-cloud/cka/7%20-%20Command%20Labs%20and%20Verification%20Playbook.md), CKA cheatsheet |
| 17 | 15 to 21 Mar | Second simulator session, then the exam | [CKA index](../devops-cloud/cka/INDEX.md) |

**Exit criteria:** you finish simulator sessions within the time limit, can back up and restore etcd and upgrade a kubeadm cluster from memory, and can diagnose a broken Pod, node or Service in under ten minutes each. Verify the current CKA curriculum, Kubernetes version, duration, passing score and simulator inclusion with the Linux Foundation before booking.

## Phase 3: Capstone platform project (Weeks 18 to 23)

Why a project after two certificates: a certificate proves you can pass a test; a system you can demo and defend proves you can build one. This project is where Kubernetes, Terraform and Prometheus with Grafana and Loki get real experience bullets, and it gives you one story to walk through in every interview.

| Week | Dates | Build |
| --- | --- | --- |
| 18 | 22 to 28 Mar | Terraform modules for a VPC and a Kubernetes cluster, with remote state. EKS bills the control plane by the hour (check current pricing), so a k3s cluster on EC2 is a cheaper alternative while you iterate. |
| 19 | 29 Mar to 4 Apr | GitHub Actions that authenticate to AWS through OIDC federation, so no long-lived access keys exist anywhere. This is the next step up from the self-hosted runner pattern you use at work. Build, test, scan the image with Trivy, push to ECR. |
| 20 | 5 to 11 Apr | A Helm chart and Argo CD. Git becomes the source of truth; promoting from dev to prod is a pull request. |
| 21 | 12 to 18 Apr | Prometheus, Grafana and Loki. Define one service level objective, for example 99% of requests under 300 ms, with an alert that reaches you. |
| 22 | 19 to 25 Apr | Hardening and failure: least-privilege IAM, workload identity for Pods, NetworkPolicies. Then induce one failure, such as a bad deploy, recover from it, and write the postmortem. |
| 23 | 26 Apr to 2 May | Write-up: architecture diagram, each decision and its tradeoff, monthly cost estimate, the postmortem. Then write the new resume bullets. |

The workload can be a small service of your own. Your trading program is a good candidate, deployed in paper or simulation mode only; the trading safety gate in the older plan still applies.

Vault notes for this phase: [Terraform](../devops-cloud/terraform/INDEX.md), [GitHub Actions](../devops-cloud/github-actions/Learning%20GitHub%20Actions.md), [Argo CD](../devops-cloud/argocd/INDEX.md), [DevSecOps](../devops-cloud/devsecops/INDEX.md), [Docker](../devops-cloud/docker/INDEX.md).

**Exit criterion:** someone else can clone the repository, deploy it and tear it down using only your README, and you can explain why every component exists and what would break without it.

## Running track: interview readiness (all weeks)

About three hours a week, kept small so it survives busy weeks.

- **Data structures and algorithms in Python, three sessions of 30 to 45 minutes a week.** Arrays and hashing, two pointers, sliding window, stacks and queues, binary search, breadth-first and depth-first search on grids and graphs, heaps. The target is easy and medium problems in 25 to 35 minutes. Use Python because you already script in it daily, so all the effort goes into problem solving rather than syntax. Log solutions in your Competitive-Programming repository. Product companies usually run a coding round even for DevOps and SRE roles; if you only target roles without one, drop this to one session a week.
- **Defend one resume bullet a week.** Interviewers dig into every number. Write five lines answering the follow-ups, for example: what were the bottlenecks behind the pipeline speed-up and how did you measure them? How does the CloudFormation update roll a new image onto ECS without downtime? How did you prove a repository migration lost nothing?
- **One troubleshooting scenario a week**, said out loud step by step: a Pod in CrashLoopBackOff, a full disk on a node, a 502 from a load balancer, DNS that resolves while the connection times out.
- **Ten to fifteen minutes of `/revise` every day**, so what you learned in Week 2 is still there in Week 17.

## Weekly rhythm

| Day | Time | What |
| --- | --- | --- |
| Monday to Friday | 60 to 75 min | 45 to 60 minutes on the current phase (read the note, answer its questions, do the lab), then 15 minutes of `/revise` |
| Monday, Wednesday, Friday | plus 30 to 45 min | One algorithms problem |
| Saturday | 3 h | Lab block. Weeks 1 to 7: about 2 h Terraform, then 1 h Ansible. Later: cluster work or the capstone |
| Sunday | 45 min | Weekly checkpoint: `/quiz` on the week's topics, update the tracker, adjust next week. The rest of the day is off. |

Two rules keep the plan alive. **When a week slips, move the exam date, not the exit criteria**: passing late with real understanding beats passing on time with gaps that surface in an interview. **Never skip the Sunday checkpoint**: plans rarely fail in one dramatic week; they fail through quiet weeks nobody reviews.

## Deliberately not now

| Not now | Why | When it comes back |
| --- | --- | --- |
| CKAD | Heavy overlap with the CKA | A short add-on after Phase 2, if a target role asks for it |
| AWS DevOps Engineer Professional, Solutions Architect Professional, CKS | They build on the SAA and CKA | After the capstone. DevOps Professional matches your daily work most closely. The CKS requires an active CKA (verify). |
| Chef | Shrinking usage; Ansible already covers configuration management for you | Only if a job needs it |
| Red Hat Certified Engineer (RHCE, an Ansible-based hands-on exam) | Needs RHEL-specific study and usually the RHCSA first (verify current prerequisites) | After the capstone, if you want a certificate for Ansible |
| Low-level design | Matters more for software-engineering roles | If you aim for platform roles that write services |
| Competitive exams and trading research | Compete for the same hours | When you decide to switch focus; tell Claude and the plan gets rebalanced |

## Points to verify before acting

- SAA: current exam code, domain weights and passing score (verify against the current AWS exam guide).
- CKA: curriculum, Kubernetes version, passing score, retake and simulator inclusion, voucher validity, and any sale discount (verify for currency).
- EKS control-plane pricing (verify for currency).
- Ansible: the version WSL installs, and whether the `amazon.aws` collection's `aws_ec2` inventory plugin options match the docs for that version (verify against current docs).
