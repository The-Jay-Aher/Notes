---
name: revise
description: Run a spaced-repetition review from the Learning Tracker - find the items due today, test each one with a fresh question, move items between Leitner boxes based on the answers, schedule the next review dates, and report what is coming up. Use it when the user says revise, review, what's due, spaced repetition, flashcards, daily review or warm-up, or asks what to study today.
---

# Revise: Spaced Review From the Learning Tracker

Reviewing each item just before you would forget it is the cheapest way to make knowledge last. This skill runs that schedule from `notes/revision/Learning Tracker.md`.

## Schedule (Leitner boxes)

| Box | Next review after |
| --- | --- |
| 1 | 1 day |
| 2 | 3 days |
| 3 | 7 days |
| 4 | 16 days |
| 5 | 35 days |

- **Correct, with sound reasoning:** move up one box (an item in box 5 stays there). Next due is today plus the new box's interval.
- **Partly correct:** stay in the same box. Next due is today plus that box's interval.
- **Incorrect:** back to box 1, due tomorrow. Add 1 to Misses.

Use today's date from the environment and write dates as `YYYY-MM-DD`.

## Procedure

1. **Read the tracker** and collect the Review Queue rows whose Next due is today or earlier. Put overdue items first, then the lowest boxes.
2. **If more than about 15 items are due,** take the 15 most overdue and tell the learner how many remain.
3. **If nothing is due,** say when the next item is due and offer either a mixed review of the lowest-box items or a teach or quiz session on the current focus.
4. **For each item:**
   - Ask a fresh question that targets its "What to recall". Change the wording, or apply the idea to a new scenario, so the learner has to retrieve the idea rather than recognize a familiar question. Don't show the answer.
   - When several subjects are due, mix them instead of grouping them (interleaving).
   - Wait for the answer. Grade it briefly as correct, partly correct or incorrect, and give the right answer, its reasoning and the note path to re-read.
5. **After the round,** update every reviewed row: Box, Misses, Last reviewed (today) and Next due. Never delete a row. An item in box 5 stays in the queue until the learner says it is mastered; then remove the row and note it as retired in the Session Log entry.
6. **Add a Session Log entry** listing the items reviewed, the results and the items that fell back to box 1.
7. **Report** the score, what slipped and the next few due dates. If an item has 3 or more Misses, recommend re-teaching it with the teach skill instead of drilling it again. Repeated misses usually mean the learner's underlying model is wrong, not that their recall is weak.

## Editing the tracker

- Keep the table format exactly as it is (pipes and column order), so it stays readable in Obsidian and on mobile.
- Change only the rows you reviewed and the Session Log. Don't reorder or reword the learner's own entries.
- Set `updated:` in the frontmatter to today.
