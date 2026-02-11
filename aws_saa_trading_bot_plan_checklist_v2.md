# 6-Week DevOps Plan — AWS SAA + Trading Bot + Terraform (Checklist)

> Time budget: **Weekdays 3–4h**, **Weekends 6–7h**  
> Primary goal: **AWS SAA** (finish by Week 4)  
> Parallel goal: **Trading bot MVP** (by Week 2) + deploy (by Week 4)  
> Continuous goal: **Terraform revision daily** (Option A — integrated into weekdays)  
> Later goal: **CKA** (start light prep after SAA; buy exam on Black Friday sale)

---

## How to use this file
- Mark tasks as you complete them: change `- [ ]` to `- [x]`
- Keep notes under each day (optional)
- If a day spills over, move items to the next day — **do not skip the weekly checkpoint**
- Terraform rule: **do the micro-revision even on busy weekdays** (20–40 min)

---

# Terraform cadence (Option A)

## Weekdays — Terraform Micro-Revision (20–40 min)
Use this every weekday after AWS study:
- [ ] 5–10 min: review notes/flashcards for the topic
- [ ] 15–25 min: implement 1 small Terraform change
- [ ] 5 min: `terraform fmt` + `terraform validate` (+ skim plan output)

## Weekends — Terraform Build Block (2–3 hours)
One bigger infra milestone each weekend:
- [ ] Implement a coherent infra chunk (VPC/EC2/IAM/etc.)
- [ ] Make it reproducible (README commands)
- [ ] Verify `apply` + `destroy` works cleanly (cost safety)

---

# Week 1 — AWS Foundations + Bot Setup + Terraform Basics

## Mon
### AWS (2h)
- [x] Read the AWS SAA exam guide + domains
- [x] Review AWS global infra: Regions / AZs / Edge
- [x] IAM basics: users, groups, roles, policies
### Trading Bot (1–2h)
- [ ] Decide bot scope (market, timeframe, strategy type)
- [ ] Choose API + paper trading (e.g., Alpaca for stocks / broker sandbox)
- [ ] Create Git repo and initial README (project goal + setup notes)
### Terraform Micro (20–40 min)
- [ ] Install/verify Terraform version (`terraform version`)
- [ ] Create `infra/` folder scaffold: `main.tf`, `variables.tf`, `outputs.tf`
- [ ] Run `terraform fmt` and `terraform validate` (even if empty/skeleton)

## Tue
### AWS (2h)
- [ ] EC2 basics: instance types, key pairs, SGs
- [ ] Launch 1 Free Tier EC2 and SSH in
### Trading Bot (1–2h)
- [ ] Set up local env (venv/conda) + install SDKs
- [ ] Write a script to fetch latest price/quote (API connectivity check)
### Terraform Micro (20–40 min)
- [ ] Add AWS provider block (region var)
- [ ] Add basic tagging locals: `Project`, `Env`, `Owner`
- [ ] Run `terraform init` (provider download) + `terraform validate`

## Wed
### AWS (2h)
- [ ] S3 basics: buckets, objects, storage classes
- [ ] S3 security basics: bucket policy vs IAM policy (high level)
- [ ] Hands-on: create bucket + upload file + test access rules
### Trading Bot (1–2h)
- [ ] Draft simple strategy in pseudocode (keep it minimal)
- [ ] Fetch historical candles/bars needed for indicator calculation
### Terraform Micro (20–40 min)
- [ ] Provision an S3 bucket via Terraform (name with random suffix)
- [ ] Enable bucket versioning (basic)
- [ ] Output bucket name/ARN

## Thu
### AWS (2h)
- [ ] VPC basics: subnets, route tables, IGW, NAT (concept)
- [ ] High availability basics: Multi-AZ idea
### Trading Bot (1–2h)
- [ ] Implement indicator function(s) (e.g., MA/RSI)
- [ ] Generate Buy/Sell signals as print output (dry-run)
### Terraform Micro (20–40 min)
- [ ] Add variables with types + defaults (region, env, project_name)
- [ ] Add README snippet: `init/plan/apply/destroy`
- [ ] Run `terraform plan` and skim for correctness

## Fri
### AWS (2h)
- [ ] RDS vs DynamoDB: when to use which
- [ ] Create a simple DynamoDB table OR review RDS concepts (whichever is easier)
### Trading Bot (1–2h)
- [ ] Add decision logging (console log + file log)
- [ ] Add basic error handling around API calls
### Terraform Micro (20–40 min)
- [ ] Create DynamoDB table in Terraform (optional) OR add notes file mapping AWS→Terraform
- [ ] Ensure consistent tagging on resources
- [ ] Confirm `terraform fmt` clean on all files

## Sat (6–7h)
### AWS (3–4h)
- [ ] Lambda basics + deploy a “Hello” Lambda
- [ ] CloudWatch basics: logs/metrics (view Lambda logs)
### Trading Bot (2–3h)
- [ ] Create a simple loop to fetch data and evaluate signals
- [ ] Run a short dry-run session and record outputs
### Terraform Build Block (2–3h, can be on Sat or Sun)
- [ ] Create minimal VPC notes (public/private subnet concepts)
- [ ] Decide: default VPC vs custom VPC for Week 2 build (pick one and commit)

## Sun (6–7h)
### AWS (3–4h)
- [ ] Review Week 1 notes (IAM/EC2/S3/VPC intro)
- [ ] Take a short quiz (course quiz / topic quiz)
### Trading Bot (2–3h)
- [ ] Cleanup repo: README update + instructions
- [ ] Commit all changes (clean history)
### Terraform Build Block (if not done on Sat)
- [ ] Add `Makefile` or scripts for `init/plan/apply/destroy`
- [ ] Verify `terraform plan` runs without errors
### Week 1 Checkpoint
- [ ] AWS: can explain IAM, EC2, S3, and basic VPC in your own words
- [ ] Bot: can fetch data + compute indicator(s) + print signal
- [ ] Terraform: provider set + at least 1 resource managed + repeatable commands exist

---

# Week 2 — AWS Core Completion + Bot MVP (Paper Trading) + Terraform Networking/EC2

## Mon
### AWS (2h)
- [ ] S3 deeper: encryption, lifecycle, versioning
- [ ] CloudFront high-level (CDN + S3)
### Bot (1–2h)
- [ ] Add paper trade order placement (no real money)
- [ ] Log orders placed with timestamps
### Terraform Micro (20–40 min)
- [ ] Add S3 encryption (SSE-S3 or SSE-KMS, keep simple)
- [ ] Add lifecycle rule (optional) and document why
- [ ] `plan` review: ensure changes are safe

## Tue
### AWS (2h)
- [ ] VPC deeper: SG vs NACL, VPC endpoints (high-level)
- [ ] Hands-on: sketch a public/private subnet design (diagram/notes)
### Bot (1–2h)
- [ ] Improve logging + structured errors
- [ ] Add retry/backoff for API rate limits (basic)
### Terraform Micro (20–40 min)
- [ ] Build VPC + public subnet + IGW + route table (if using custom VPC)
- [ ] Output VPC ID + subnet ID
- [ ] Commit a VPC diagram to `infra/docs/`

## Wed
### AWS (2h)
- [ ] Load Balancer + Auto Scaling concepts
- [ ] Understand Multi-AZ patterns for web apps
### Bot (1–2h)
- [ ] Refactor: move config to env vars / config file
- [ ] Make the bot runnable via one command
### Terraform Micro (20–40 min)
- [ ] Add Security Group for EC2 (SSH + app port if needed)
- [ ] Add key pair reference approach (document how you manage it)
- [ ] `terraform validate` + quick plan skim

## Thu
### AWS (2h)
- [ ] DynamoDB deeper: partition key, read/write capacity (high level)
- [ ] RDS HA basics: Multi-AZ, read replicas (concept)
### Bot (1–2h)
- [ ] Persist decisions/orders to CSV/SQLite (choose one)
- [ ] Write a tiny script to summarize results (PnL/signal count)
### Terraform Micro (20–40 min)
- [ ] Add EC2 instance resource (Free Tier) + attach SG + subnet
- [ ] Output public IP / DNS + ready-to-copy SSH command
- [ ] Add tags to EC2 and SG

## Fri
### AWS (2h)
- [ ] SQS/SNS: decoupling concepts + common patterns
- [ ] CloudTrail basics: auditing API calls
### Bot (1–2h)
- [ ] Add a simple notification (email/telegram/webhook) for trade signal
### Terraform Micro (20–40 min)
- [ ] Add IAM role + instance profile (least privilege baseline)
- [ ] Attach minimal policy (start with CloudWatch logs if you plan to use it)
- [ ] Document permissions rationale in `infra/README.md`

## Sat (6–7h)
### AWS (3–4h)
- [ ] Hands-on labs: pick 1–2 (S3 hosting / VPC / serverless)
- [ ] Rebuild 1 lab from scratch (repeat for retention)
### Bot (2–3h)
- [ ] Run longer paper-trading simulation OR backtest
- [ ] Record results + notes (what worked, what broke)
### Terraform Build Block (2–3h, can be on Sat or Sun)
- [ ] Run `terraform apply` to create EC2 + network + IAM
- [ ] SSH into EC2 and verify connectivity (from your machine)
- [ ] Practice `terraform destroy` and confirm clean teardown

## Sun (6–7h)
### AWS (3–4h)
- [ ] Create 1-page summary of all services covered so far
- [ ] Topic quiz to identify weak areas
### Bot (2–3h)
- [ ] README: “How it works” + “Roadmap” section
- [ ] Tag a version/release (v0.1)
### Terraform Build Block (if not done on Sat)
- [ ] Repeat `apply`/`destroy` once more to ensure reproducibility
- [ ] Add a “Cost Safety” checklist (stop/terminate resources)
### Week 2 Checkpoint
- [ ] AWS: core services covered (compute/storage/network/db/serverless basics)
- [ ] Bot: MVP works end-to-end (data → signal → paper order → logs)
- [ ] Terraform: can spin up and tear down EC2 stack reliably

---

# Week 3 — Advanced AWS + DevOps Practices (Terraform/Docker) + Exam Practice Begins

## Mon
### AWS (2h)
- [ ] Security deep dive: IAM policies, roles, least privilege
- [ ] KMS basics + encryption at rest vs in transit
### Bot (1–2h)
- [ ] Secrets management: move API keys to env vars / .env (not committed)
- [ ] Add “safe mode” (no order placement unless explicitly enabled)
### Terraform Micro (20–40 min)
- [ ] Refine IAM policies (least privilege) for EC2 role
- [ ] Add KMS note: when you would use SSE-KMS vs SSE-S3
- [ ] `plan` and confirm no accidental destructive changes

## Tue
### AWS (2h)
- [ ] Serverless deeper: Lambda limits + API Gateway basics
- [ ] Event-driven basics: SNS/EventBridge (concept)
### Bot (1–2h)
- [ ] Draft deployment plan (EC2 vs ECS/Fargate vs Lambda)
- [ ] Decide 1 target deployment path (keep it simple)
### Terraform Micro (20–40 min)
- [ ] Add optional SNS topic resource (if you’ll use notifications)
- [ ] Add variables for toggling optional resources (booleans)
- [ ] Document “why optional” in README

## Wed
### AWS (2h)
- [ ] Well-Architected pillars review (Reliability/Cost/Security)
- [ ] Study common SAA scenario patterns (notes)
### Bot (1–2h)
- [ ] Tune strategy parameters (small changes) + rerun test
- [ ] Write down what changed and why
### Terraform Micro (20–40 min)
- [ ] Introduce modules: create `modules/ec2_runner/` (minimal)
- [ ] Move EC2 + SG into module with inputs/outputs
- [ ] `terraform fmt` + `validate`

## Thu
### AWS (2h)
- [ ] IaC: CloudFormation overview + Terraform on AWS mapping
- [ ] Write Terraform to provision 1–2 AWS resources (S3/EC2/SG) (review)
### Bot (1–2h)
- [ ] Add Terraform for the bot infra (minimal) (refine)
- [ ] Document “terraform apply/destroy” steps
### Terraform Micro (20–40 min)
- [ ] Add `for_each` or `count` once (e.g., tags/resources) to practice
- [ ] Add variable validation rules (e.g., env allowed values)
- [ ] Ensure outputs are useful for deployment steps

## Fri
### AWS (2h)
- [ ] CloudWatch deeper: logs, metrics, alarms
- [ ] CloudTrail review (what it captures)
### Bot (1–2h)
- [ ] Add basic alerting for failures (SNS/email/telegram)
### Terraform Micro (20–40 min)
- [ ] Add CloudWatch log group / agent notes (implementation optional)
- [ ] Add alarms concept note (what you’d alarm on for the bot)
- [ ] Update infra README with monitoring section

## Sat (6–7h)
### AWS (3–4h)
- [ ] Take SAA practice test #1 (timed)
- [ ] Review every wrong answer + write “why” notes
### Bot (2–3h)
- [ ] Dockerize bot (Dockerfile + run command)
- [ ] Test container locally (end-to-end)
### Terraform Build Block (2–3h, can be on Sat or Sun)
- [ ] Use Terraform to bring up EC2, then deploy Docker container on it
- [ ] Confirm bot runs remotely (logs visible)
- [ ] Confirm destroy still works cleanly

## Sun (6–7h)
### AWS (3–4h)
- [ ] Patch weak topics from mock #1
- [ ] Update your “weak list” (services/topics)
### Bot (2–3h)
- [ ] Repo cleanup + docs for Docker
- [ ] Tag a release (v0.2)
### Terraform Build Block (if not done on Sat)
- [ ] Repeat deploy procedure from a clean Terraform `apply`
- [ ] Add a one-command deploy script (optional)
### Week 3 Checkpoint
- [ ] AWS: you have a clear weak-topic list and a plan
- [ ] Bot: runs in Docker + logs correctly
- [ ] Terraform: infra is modular (at least EC2 runner module) + reproducible

---

# Week 4 — Exam Sprint + Cloud Deployment of Bot (Terraform-managed)

## Mon
### AWS (3–4h)
- [ ] Full-length practice exam #2 (timed)
- [ ] Deep review of incorrect answers (write explanations)
### Bot (0–1h)
- [ ] Finalize deployment checklist (accounts, keys, env vars)
### Terraform Micro (20–40 min)
- [ ] Lock down infra changes (no major refactors this week)
- [ ] Ensure `apply` and `destroy` are stable and predictable

## Tue
### AWS (2–3h)
- [ ] Weak topics repair session (focus only on top 3 weaknesses)
### Bot (1–2h)
- [ ] Deploy bot (target: EC2 + Docker is simplest)
- [ ] Confirm it runs remotely and logs correctly
### Terraform Micro (20–40 min)
- [ ] Run `apply` from scratch and confirm outputs are correct
- [ ] Record exact deploy commands in README

## Wed
### AWS (3–4h)
- [ ] Practice exam #3 (different provider if possible)
- [ ] Review + update weak list
### Bot (0–2h)
- [ ] Add CloudWatch logs/agent OR simple log shipping
- [ ] Add SNS/email alert on important events (optional)
### Terraform Micro (20–40 min)
- [ ] Add minimal monitoring support (optional resources only if stable)
- [ ] Confirm no drift: `terraform plan` shows no unexpected changes

## Thu
### AWS (2–3h)
- [ ] Final review notes (no new topics)
- [ ] Revisit Well-Architected patterns
### Bot (1–2h)
- [ ] Document deployment architecture in README (diagram/steps)
- [ ] Cost check + stop unnecessary resources
### Terraform Micro (20–40 min)
- [ ] Run `destroy` and confirm everything is removed (cost safety)
- [ ] Add final “Cost Safety” checklist section

## Fri
### AWS (2–3h)
- [ ] Light review + short topic quizzes
- [ ] Confirm readiness (target: consistent passing score range)
### Bot (0–1h)
- [ ] Verify bot stability (logs, retries, uptime)
### Terraform Micro (20–40 min)
- [ ] Freeze infra: tag release `infra-v1`
- [ ] Confirm README is complete and copy-paste runnable

## Sat (6–7h)
### AWS
- [ ] Take the AWS SAA exam **OR** final full mock + review
### Personal
- [ ] Rest + good sleep before exam

## Sun (6–7h)
- [ ] If exam done: write a short post-mortem (what was hard, what to revisit)
- [ ] If exam pending: light revision + rest
### Week 4 Checkpoint
- [ ] AWS: exam attempted or scheduled with confidence
- [ ] Bot: deployed + documented + monitored at basic level
- [ ] Terraform: apply/destroy reproducible + cost-safe + README complete

---

# Week 5 — After SAA: Light Kubernetes Intro + Portfolio/Job Prep

## Mon–Wed (repeat pattern)
### Kubernetes (1–2h/day)
- [ ] Learn core K8s objects: Pod, Deployment, Service
- [ ] Practice `kubectl` basics on a local cluster (kind/minikube)
### DevOps Portfolio (1–2h/day)
- [ ] Add CI (GitHub Actions) for lint/tests
- [ ] Improve Terraform module quality + README
### Terraform Micro (20–40 min)
- [ ] Practice one Kubernetes-related IaC thought: what would EKS require? (notes only)
- [ ] Keep infra code tidy: small refactors, better docs, no breaking changes

## Thu
- [ ] Update resume + LinkedIn with AWS SAA (and Terraform/AWS project)
- [ ] Add trading bot as a “DevOps project” with bullet highlights

## Fri
- [ ] Create a target list of 20 DevOps jobs (Pune/Mumbai + remote)
- [ ] Extract required skills into a learning backlog

## Weekend
- [ ] Do 1 Kubernetes lab session (2–3h)
- [ ] Apply to 5–10 jobs (with tailored resume keywords)

### Week 5 Checkpoint
- [ ] Resume updated + project clearly presentable
- [ ] You can explain what Kubernetes is and how you’d deploy the bot on it

---

# Week 6 (Optional) — Buffer + Next 90-Day Plan

- [ ] If SAA not done: use this week as final buffer for exam + retake plan
- [ ] If SAA done: start a 90-day roadmap:
  - [ ] Weeks 1–4: Kubernetes foundations + labs
  - [ ] Weeks 5–8: CKA-style practice + clusters + troubleshooting
  - [ ] Weeks 9–12: job switch sprint (apply/interview cycle)

- [ ] Plan Black Friday: buy CKA exam voucher during sale window
- [ ] Decide CKA exam target month (after steady practice)

---

## Progress Tracker
- [ ] AWS SAA: course finished
- [ ] AWS SAA: 3 full mocks completed
- [ ] AWS SAA: exam attempted
- [ ] Bot: MVP complete (paper trading)
- [ ] Bot: Dockerized
- [ ] Bot: deployed to AWS
- [ ] Terraform: daily micro blocks completed (track weekly)
- [ ] Terraform: EC2 stack reproducible (apply/destroy)
- [ ] Terraform: infra modularized (at least 1 module)
- [ ] Resume + LinkedIn updated
- [ ] 20 jobs shortlisted
- [ ] 20 job applications sent
- [ ] Kubernetes basics done
