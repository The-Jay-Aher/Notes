---
name: deep-notes
description: The full procedure for creating or upgrading mastery-level study notes in this vault - inspect before writing, upgrade rather than duplicate, the required chapter structure, the "Small Details That Matter Later" rule, source and accuracy rules, required files per topic, command and diagram rules, the changelog, and the quality bar. Load it whenever the user asks to create, write, upgrade, expand, restructure or fix notes, a roadmap, a cheatsheet, a glossary or practice questions for any subject, and load the matching subject-* skill alongside it.
---

# Deep Notes: Creating and Upgrading Notes

Notes in this vault are the textbook the learner studies from. Write them so a serious student can understand the topic from the notes alone, then explain it, apply it, troubleshoot it and connect it to other topics. Do not write short summaries; write mastery-level notes in the teacher voice described in AGENTS.md.

Also load the matching subject skill (subject-kubernetes, subject-aws, subject-devops-tools, subject-programming, subject-indian-exams) for the topic checklist.

## Workflow

When the user asks for notes on a topic:

1. First inspect the repository.
2. Check whether notes already exist.
3. If notes exist, upgrade them.
4. If notes do not exist, create them.
5. Create or update the roadmap.
6. Create or update deep chapter files.
7. Add Mermaid diagrams where useful.
8. Add practice questions and answers.
9. Add glossary terms.
10. Add revision sheets.
11. Add changelog.
12. Summarize what was created or changed.

### If notes already exist: upgrade, don't duplicate

1. Do not create a duplicate folder blindly.
2. Read the existing notes.
3. Identify what is already good.
4. Identify what is missing, shallow, outdated, confusing, duplicated, or badly structured.
5. Preserve useful existing content.
6. Rewrite weak explanations into legendary-teacher-level explanations.
7. Add missing architecture, internals, examples, edge cases, diagrams, practice questions, and causal chains.
8. Improve organization and file naming if needed.
9. Add cross-links between related files.
10. Add a changelog entry explaining what was improved.
11. Do not delete existing useful material unless it is clearly wrong, stale, duplicated, or harmful.
12. If removing or replacing content, mention why in the changelog.
13. If uncertain about correctness, mark it clearly as something to verify against official sources.

### If no notes exist

1. Create a new structured folder.
2. Start with a roadmap.
3. Then create deep notes file by file.
4. Include diagrams, examples, practice questions, answers, and revision sheets.

### Final summary after upgrading notes

- Files updated
- Files created
- Major improvements
- Missing areas added
- Any uncertain points marked for verification
- Recommended next topics to connect

## What every topic must explain (core mission)

1. What the concept is
2. Why it exists
3. What problem it solves
4. What came before it
5. What caused it to become important
6. What changed because of it
7. What future topics or events depend on it
8. How it works internally
9. How it connects to other concepts
10. What assumptions it makes
11. What constraints it has
12. What can go wrong
13. How to debug, analyze, or answer questions about it
14. What small details become important later
15. How it appears in real scenarios, exams, interviews, or production systems

## Required chapter structure

Every major chapter follows this structure unless a better structure is clearly needed. `_System/Templates/Study Chapter.md` is the same skeleton as an Obsidian template.

```markdown
# Chapter Title
## Why This Chapter Matters
## The Big Picture
## First-Principles Explanation
## Core Vocabulary
## Mental Model
## Historical / Evolution / Causal Chain
## Architecture or Conceptual Structure
## Step-by-Step Explanation
## Internal Mechanics
## Practical Examples
## Small Details That Matter Later
## Common Misunderstandings
## Failure Modes / Mistakes / Traps
## Debugging / Analysis / Answer-Writing Method
## Real-World or Exam Relevance
## Connected Topics
## Chapter Summary
## Questions to Test Understanding
## Answers and Reasoning
```

### Make the questions usable for self-testing

The learner uses "Questions to Test Understanding" for active recall, so:

- Mix question types: purpose or cause, mechanism, tradeoff or constraint, failure mode or trap, and connection to another topic. These are the same five as `_System/Templates/Revision Sheet.md`.
- Hide each answer in a collapsed Obsidian callout, so the learner has to attempt the question before seeing the answer:

  ```markdown
  > [!question]- Answer
  > The answer and the reasoning behind it.
  ```

- Prefer questions that need reasoning ("what breaks if…", "why not…") over recall of a single word.

## "Small Details That Matter Later" rule

Every major file must include a section named `## Small Details That Matter Later`. It explains the tiny things that become important during exams, interviews, debugging, architecture design or real-world decision-making.

For technical topics, include:

- defaults
- hidden constraints
- naming confusion
- lifecycle behavior
- race conditions
- version-sensitive behavior
- security implications
- performance traps
- configuration mistakes
- debugging clues
- things beginners often ignore

For exam topics, include:

- wording traps
- timeline traps
- similar-sounding terms
- institution vs act vs committee confusion
- chronology confusion
- cause-effect confusion
- static-current linkage
- how examiners may twist the concept
- answer-writing traps
- elimination tricks for MCQs

## Causal chains: worked examples

Pattern: **Cause → Mechanism → Immediate Result → Long-Term Impact → Next Connected Topic.**

For history, polity, economics, governance and current affairs:

- Explain what happened.
- Explain why it happened.
- Explain what conditions created it.
- Explain which people, institutions, laws, wars, policies, ideas, or economic forces influenced it.
- Explain what changed immediately after it.
- Explain what future event, reform, conflict, movement, institution, or policy came from it.
- Connect it to the exam syllabus and possible questions.

> **Bad:** "The Regulating Act of 1773 was passed by the British Parliament."
>
> **Good:** "The Regulating Act of 1773 was not an isolated law. It came after the East India Company became politically powerful in Bengal after Plassey and Buxar, but its administration was corrupt, unstable, and financially troubled. The British Parliament could not ignore a private company ruling territory and creating political risk. So the Act tried to bring the Company under parliamentary control. This became the first major step in British state control over Indian administration, later developing through Pitt's India Act, Charter Acts, and eventually Crown rule after 1858."

For technical subjects:

- Explain what problem existed.
- Explain why older solutions were insufficient.
- Explain what design was introduced.
- Explain how the new design works.
- Explain the tradeoffs.
- Explain what new problems the design created.
- Explain how later tools, patterns, or architectures evolved from it.

> **Bad:** "Kubernetes uses a control plane."
>
> **Good:** "Kubernetes uses a control plane because manually managing containers across many machines becomes unreliable once systems scale. Containers can crash, nodes can fail, traffic can shift, and deployments need controlled rollout. The control plane exists to continuously compare desired state with actual state. This reconciliation model leads directly to controllers, the API server, etcd, the scheduler, and kubelet. Once you understand this chain, Kubernetes stops looking like random YAML and starts looking like a distributed decision-making system."

## Source and accuracy rules

Use authoritative sources whenever possible. For technical subjects, prefer:

- official documentation
- official certification guides
- standards
- RFCs
- vendor documentation
- project documentation
- source code comments where useful
- trusted engineering references

For AWS, Kubernetes, Docker, Jenkins, Ansible, Chef and Argo CD:

- Always mention version assumptions where relevant.
- Mention when behavior may vary by version, plugin, provider, distribution, or managed service.
- Do not hallucinate commands or flags.
- If unsure, mark the point as "verify against current docs."

For UPSC, MPSC, RBI Assistant, RBI Grade B and SEBI Grade A:

- Use the latest official syllabus, notification, and exam pattern where available.
- Clearly distinguish stable syllabus topics from current-affairs-dependent topics.
- Mention when data, schemes, acts, committees, or policies need current verification.
- Avoid outdated claims.
- If a fact may change, mark it for current verification.

## Folder structure

The vault layout and filing rules are in `README.md` and `notes/INDEX.md`; follow them. Topic folders live under:

```text
notes/devops-cloud/        kubernetes, cka, ckad, aws-*, docker, ansible, jenkins, argocd, terraform, github-actions, devsecops (chef/ if created)
notes/programming/         competitive-programming, java, python, cpp, low-level-design
notes/competitive-exams/   upsc, mpsc, rbi-assistant, rbi-grade-b, sebi-grade-a
notes/shared-foundations/  linux, networking, tools (add cloud-computing, distributed-systems, databases, security, economics, indian-polity, modern-history, programming-fundamentals when needed)
notes/finance-trading/     foundations, strategies, governance, workbooks, study-plans, book-notes
notes/revision/            Learning Tracker (used by teach, quiz, revise)
```

Create shared foundations where useful, and cross-link to them instead of repeating the same explanation badly in many places. When moving or renaming notes, update both Markdown links and Obsidian wikilinks, then run `_System/Scripts/validate_markdown_links.py`.

Never commit PDFs or other large binaries. `*.pdf` is gitignored because a 56 MB commit of book PDFs crashed Obsidian Git on mobile. Keep source books on disk only and link to them by name.

## Required files for each topic

Each topic folder should contain files like:

```text
00-roadmap.md
01-foundations.md
02-core-concepts.md
03-architecture-or-structure.md
04-deep-dives.md
05-practical-application.md
06-small-details-that-matter.md
07-failure-modes-or-common-mistakes.md
08-exam-interview-or-answer-writing.md
09-practice-questions.md
10-cheatsheet.md
11-glossary.md
CHANGELOG.md
```

Adjust based on the subject. For large topics, create more files. Do not force everything into one huge unreadable file. Many existing tracks also have an `INDEX.md`; keep it current.

## Technical notes requirements

For technical subjects (Kubernetes, AWS, Docker, Ansible, Jenkins, Chef, Argo CD, Java, Python, C++, Competitive Programming and similar), include:

- first-principles explanation
- architecture
- internals
- lifecycle
- control flow
- data flow
- commands
- configuration examples
- code examples
- diagrams
- debugging
- monitoring
- performance
- security
- scaling
- failure modes
- production scenarios
- interview questions
- hands-on labs
- practice problems
- revision cheatsheets

Whenever commands are used, explain:

- what the command does
- when to use it
- important flags
- expected output
- how to interpret output
- what bad output looks like
- safe usage
- dangerous usage
- common mistakes

Use Mermaid diagrams where useful. Diagram types may include:

- component diagrams
- request flow diagrams
- lifecycle diagrams
- state transition diagrams
- decision trees
- troubleshooting flowcharts
- architecture diagrams
- network flow diagrams
- dependency diagrams

## Exam notes requirements

For all exam-oriented subjects (certifications included), include:

- syllabus mapping
- chapter priority
- previous-year-question relevance
- conceptual explanation
- factual memory hooks
- timelines
- cause-effect chains
- MCQs
- mains/descriptive questions where relevant
- answer frameworks
- common traps
- revision tables
- one-page cheat sheets
- glossary

Do not create only coaching-style bullet notes. Explain like a teacher who wants the student to understand the machinery behind the facts.

## Changelog

Every change to a topic's notes gets an entry in that topic's `CHANGELOG.md`, dated `YYYY-MM-DD`, saying what improved and why anything was removed or replaced. Vault-wide changes (structure, AGENTS.md, skills, templates) go in `_System/CHANGELOG.md`.

## Quality bar

Before finishing, check whether the notes satisfy this standard:

- Can a beginner understand the topic from these notes alone?
- Are the explanations deep enough for interviews, exams, or production?
- Are architecture and internals explained where relevant?
- Are small but important details included?
- Are causal chains included?
- Are examples and diagrams included?
- Are common mistakes included?
- Are practice questions included?
- Are existing notes preserved and improved instead of duplicated?
- Are uncertain or version-sensitive points marked clearly?

If the answer is no, continue improving the notes before finalizing.
