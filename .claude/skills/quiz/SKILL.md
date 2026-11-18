---
name: quiz
description: Test the learner on a topic with retrieval practice drawn from this vault's notes - one question at a time or as a mock test, mixed question types, honest grading (correct, partly correct or incorrect, and why), explanations tied to the note that teaches the point, and results logged to the Learning Tracker. Use it when the user says quiz me, test me, ask me questions, mock test, practice questions or MCQs, or asks to check whether they know a topic.
---

# Quiz: Retrieval Practice and Mock Tests

Retrieval, meaning pulling an answer out of memory, strengthens that memory far more than re-reading does. A quiz exists to make the learner retrieve, and then to find exactly what they don't know.

Load the matching subject skill for the question styles that suit the subject.

## Set up

1. **Topic and scope:** take them from the user's request. If the request is vague, offer the current focus or the due items from `notes/revision/Learning Tracker.md`.
2. **Mode:**
   - **Practice** (the default): one question at a time, with feedback after each.
   - **Mock test:** N questions answered without feedback, graded at the end, and timed if the learner wants. Use it to simulate an exam.
3. **Count:** 5 questions by default in practice mode. For a mock test, ask how many.
4. **Source:** read the relevant notes. Every question must be answerable from the vault's notes or from official sources, and each explanation cites the note file and section. If a question goes beyond the notes, say so.

## Writing good questions

- **Use at least three question types per quiz:**
  - why or purpose ("Why does X exist?")
  - mechanism ("Walk through what happens when…")
  - predict the output or behavior
  - debug ("Here is the error or log. What is wrong?")
  - scenario (AWS-style: requirements, then the best option)
  - compare and contrast
  - MCQ with realistic distractors (for exam tracks)
  - ordering or matching (chronology, acts and their provisions)
  - short written answer (a mains answer, or "explain in three sentences")
  - hands-on task (kubectl, a playbook, code)
- **Prefer reasoning over recall of a single word.** Include at least one question drawn from a "Small Details That Matter Later" section.
- **Interleave:** if the tracker lists weak spots in related topics, include one of them.
- **Adapt the difficulty:** start at medium, go harder after two correct answers in a row and easier after two wrong ones.
- **Don't copy the notes' own practice questions** if the learner may have just read them. Rephrase them or use a new scenario.
- **For MCQs,** exactly one option must be defensibly correct. The distractors should be plausible mistakes drawn from common misconceptions, not jokes.

## Grading

For each answer:

- **Verdict:** correct, partly correct or incorrect. Be strict and honest.
- **Specifics:** what was right, what was missing, what was wrong.
- **The correct answer with its reasoning,** as a causal chain rather than a bare fact. For MCQs, also say why each wrong option is wrong.
- **Where to re-read:** the note path and section.
- **Written answers** (mains, descriptive, explain-in-words) are graded against a rubric stated up front, for example: directive covered, structure, dimensions, examples, conclusion. Then give one rewritten paragraph as a model.
- **Never reveal an answer before the learner attempts it.** If they say "skip" or "I give up", reveal it and count it as incorrect.

## Closing

- Give the score (for example 3.5/5), broken down by question type or subtopic.
- Name the pattern in the mistakes, for example "mixes up NodePort and LoadBalancer" or "drops the 'critically' half of the directive".
- Update `notes/revision/Learning Tracker.md`, using the box rules in the revise skill:
  - An incorrect or partly correct item goes into the Review Queue in box 1, or back to box 1 if it is already there. Add 1 to its Misses count.
  - An item already in the queue that was answered correctly moves up one box.
  - Add a Session Log entry with the score and the misconceptions, and set `updated:` in the frontmatter.
- Offer to teach the weakest subtopic now (teach skill), or to run another round on the misses.
