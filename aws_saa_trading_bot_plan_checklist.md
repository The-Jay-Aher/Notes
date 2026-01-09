# 6-Week DevOps Plan — AWS SAA + Trading Bot (Checklist)

> Time budget: **Weekdays 3–4h**, **Weekends 6–7h**  
> Primary goal: **AWS SAA** (finish by Week 4)  
> Parallel goal: **Trading bot MVP** (by Week 2) + deploy (by Week 4)  
> Later goal: **CKA** (start light prep after SAA; buy exam on Black Friday sale)

---

## How to use this file
- Mark tasks as you complete them: change `- [ ]` to `- [x]`
- Keep notes under each day (optional)
- If a day spills over, move items to the next day — **do not skip the weekly checkpoint**

---

# Week 1 — AWS Foundations + Bot Setup

## Mon
### AWS (2h)
- [x] Read the AWS SAA exam guide + domains
- [x] Review AWS global infra: Regions / AZs / Edge
- [ ] IAM basics: users, groups, roles, policies
### Trading Bot (1–2h)
- [ ] Decide bot scope (market, timeframe, strategy type)
- [ ] Choose API + paper trading (e.g., Alpaca for stocks / broker sandbox)
- [ ] Create Git repo and initial README (project goal + setup notes)

## Tue
### AWS (2h)
- [ ] EC2 basics: instance types, key pairs, SGs
- [ ] Launch 1 Free Tier EC2 and SSH in
### Trading Bot (1–2h)
- [ ] Set up local env (venv/conda) + install SDKs
- [ ] Write a script to fetch latest price/quote (API connectivity check)

## Wed
### AWS (2h)
- [ ] S3 basics: buckets, objects, storage classes
- [ ] S3 security basics: bucket policy vs IAM policy (high level)
- [ ] Hands-on: create bucket + upload file + test access rules
### Trading Bot (1–2h)
- [ ] Draft simple strategy in pseudocode (keep it minimal)
- [ ] Fetch historical candles/bars needed for indicator calculation

## Thu
### AWS (2h)
- [ ] VPC basics: subnets, route tables, IGW, NAT (concept)
- [ ] High availability basics: Multi-AZ idea
### Trading Bot (1–2h)
- [ ] Implement indicator function(s) (e.g., MA/RSI)
- [ ] Generate Buy/Sell signals as print output (dry-run)

## Fri
### AWS (2h)
- [ ] RDS vs DynamoDB: when to use which
- [ ] Create a simple DynamoDB table OR review RDS concepts (whichever is easier)
### Trading Bot (1–2h)
- [ ] Add decision logging (console log + file log)
- [ ] Add basic error handling around API calls

## Sat (6–7h)
### AWS (3–4h)
- [ ] Lambda basics + deploy a “Hello” Lambda
- [ ] CloudWatch basics: logs/metrics (view Lambda logs)
### Trading Bot (2–3h)
- [ ] Create a simple loop to fetch data and evaluate signals
- [ ] Run a short dry-run session and record outputs

## Sun (6–7h)
### AWS (3–4h)
- [ ] Review Week 1 notes (IAM/EC2/S3/VPC intro)
- [ ] Take a short quiz (course quiz / topic quiz)
### Trading Bot (2–3h)
- [ ] Cleanup repo: README update + instructions
- [ ] Commit all changes (clean history)
### Week 1 Checkpoint
- [ ] AWS: can explain IAM, EC2, S3, and basic VPC in your own words
- [ ] Bot: can fetch data + compute indicator(s) + print signal

---

# Week 2 — AWS Core Completion + Bot MVP (Paper Trading)

## Mon
### AWS (2h)
- [ ] S3 deeper: encryption, lifecycle, versioning
- [ ] CloudFront high-level (CDN + S3)
### Bot (1–2h)
- [ ] Add paper trade order placement (no real money)
- [ ] Log orders placed with timestamps

## Tue
### AWS (2h)
- [ ] VPC deeper: SG vs NACL, VPC endpoints (high-level)
- [ ] Hands-on: sketch a public/private subnet design (diagram/notes)
### Bot (1–2h)
- [ ] Improve logging + structured errors
- [ ] Add retry/backoff for API rate limits (basic)

## Wed
### AWS (2h)
- [ ] Load Balancer + Auto Scaling concepts
- [ ] Understand Multi-AZ patterns for web apps
### Bot (1–2h)
- [ ] Refactor: move config to env vars / config file
- [ ] Make the bot runnable via one command

## Thu
### AWS (2h)
- [ ] DynamoDB deeper: partition key, read/write capacity (high level)
- [ ] RDS HA basics: Multi-AZ, read replicas (concept)
### Bot (1–2h)
- [ ] Persist decisions/orders to CSV/SQLite (choose one)
- [ ] Write a tiny script to summarize results (PnL/signal count)

## Fri
### AWS (2h)
- [ ] SQS/SNS: decoupling concepts + common patterns
- [ ] CloudTrail basics: auditing API calls
### Bot (1–2h)
- [ ] Add a simple notification (email/telegram/webhook) for trade signal

## Sat (6–7h)
### AWS (3–4h)
- [ ] Hands-on labs: pick 1–2 (S3 hosting / VPC / serverless)
- [ ] Rebuild 1 lab from scratch (repeat for retention)
### Bot (2–3h)
- [ ] Run longer paper-trading simulation OR backtest
- [ ] Record results + notes (what worked, what broke)

## Sun (6–7h)
### AWS (3–4h)
- [ ] Create 1-page summary of all services covered so far
- [ ] Topic quiz to identify weak areas
### Bot (2–3h)
- [ ] README: “How it works” + “Roadmap” section
- [ ] Tag a version/release (v0.1)
### Week 2 Checkpoint
- [ ] AWS: core services covered (compute/storage/network/db/serverless basics)
- [ ] Bot: MVP works end-to-end (data → signal → paper order → logs)

---

# Week 3 — Advanced AWS + DevOps Practices (Terraform/Docker) + Exam Practice Begins

## Mon
### AWS (2h)
- [ ] Security deep dive: IAM policies, roles, least privilege
- [ ] KMS basics + encryption at rest vs in transit
### Bot (1–2h)
- [ ] Secrets management: move API keys to env vars / .env (not committed)
- [ ] Add “safe mode” (no order placement unless explicitly enabled)

## Tue
### AWS (2h)
- [ ] Serverless deeper: Lambda limits + API Gateway basics
- [ ] Event-driven basics: SNS/EventBridge (concept)
### Bot (1–2h)
- [ ] Draft deployment plan (EC2 vs ECS/Fargate vs Lambda)
- [ ] Decide 1 target deployment path (keep it simple)

## Wed
### AWS (2h)
- [ ] Well-Architected pillars review (Reliability/Cost/Security)
- [ ] Study common SAA scenario patterns (notes)
### Bot (1–2h)
- [ ] Tune strategy parameters (small changes) + rerun test
- [ ] Write down what changed and why

## Thu
### AWS (2h)
- [ ] IaC: CloudFormation overview + Terraform on AWS mapping
- [ ] Write Terraform to provision 1–2 AWS resources (S3/EC2/SG)
### Bot (1–2h)
- [ ] Add Terraform for the bot infra (minimal)
- [ ] Document “terraform apply/destroy” steps

## Fri
### AWS (2h)
- [ ] CloudWatch deeper: logs, metrics, alarms
- [ ] CloudTrail review (what it captures)
### Bot (1–2h)
- [ ] Add basic alerting for failures (SNS/email/telegram)

## Sat (6–7h)
### AWS (3–4h)
- [ ] Take SAA practice test #1 (timed)
- [ ] Review every wrong answer + write “why” notes
### Bot (2–3h)
- [ ] Dockerize bot (Dockerfile + run command)
- [ ] Test container locally (end-to-end)

## Sun (6–7h)
### AWS (3–4h)
- [ ] Patch weak topics from mock #1
- [ ] Update your “weak list” (services/topics)
### Bot (2–3h)
- [ ] Repo cleanup + docs for Docker
- [ ] Tag a release (v0.2)
### Week 3 Checkpoint
- [ ] AWS: you have a clear weak-topic list and a plan
- [ ] Bot: runs in Docker + logs correctly

---

# Week 4 — Exam Sprint + Cloud Deployment of Bot

## Mon
### AWS (3–4h)
- [ ] Full-length practice exam #2 (timed)
- [ ] Deep review of incorrect answers (write explanations)
### Bot (0–1h)
- [ ] Finalize deployment checklist (accounts, keys, env vars)

## Tue
### AWS (2–3h)
- [ ] Weak topics repair session (focus only on top 3 weaknesses)
### Bot (1–2h)
- [ ] Deploy bot (target: EC2 + Docker is simplest)
- [ ] Confirm it runs remotely and logs correctly

## Wed
### AWS (3–4h)
- [ ] Practice exam #3 (different provider if possible)
- [ ] Review + update weak list
### Bot (0–2h)
- [ ] Add CloudWatch logs/agent OR simple log shipping
- [ ] Add SNS/email alert on important events (optional)

## Thu
### AWS (2–3h)
- [ ] Final review notes (no new topics)
- [ ] Revisit Well-Architected patterns
### Bot (1–2h)
- [ ] Document deployment architecture in README (diagram/steps)
- [ ] Cost check + stop unnecessary resources

## Fri
### AWS (2–3h)
- [ ] Light review + short topic quizzes
- [ ] Confirm readiness (target: consistent passing score range)
### Bot (0–1h)
- [ ] Verify bot stability (logs, retries, uptime)

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

---

# Week 5 — After SAA: Light Kubernetes Intro + Portfolio/Job Prep

## Mon–Wed (repeat pattern)
### Kubernetes (1–2h/day)
- [ ] Learn core K8s objects: Pod, Deployment, Service
- [ ] Practice `kubectl` basics on a local cluster (kind/minikube)
### DevOps Portfolio (1–2h/day)
- [ ] Add CI (GitHub Actions) for lint/tests
- [ ] Improve Terraform module quality + README

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
- [ ] Resume + LinkedIn updated
- [ ] 20 jobs shortlisted
- [ ] 20 job applications sent
- [ ] Kubernetes basics done
