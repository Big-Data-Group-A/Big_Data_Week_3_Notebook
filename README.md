# Week 3 Lab — Control Flow & Functions

This lab took me through control flow, loops, functions, and file handling in Python, working with a 40-row student dataset (`week3_students.csv`). The twist: 3 of the score values in the dataset are broken (not numbers), so a chunk of the work was making sure my code could catch that and keep going instead of crashing.

## What I submitted

- My notebook, renamed `Week3_YourName`, with everything running clean end to end
- A short write-up (½–1 page) naming the 3 broken records and explaining how my code handled them
- Screenshots of the working code and output
- Answers to the reflection questions below

## Walking through the parts

**Part 1 — Making Decisions (5 marks)**
Built a grading ladder with `if`/`elif`/`else` — A ≥ 85, B 70–84, C 60–69, D 50–59, F below 50 — and tested it on 91, 76, 64, 52, and 43. Then a combined-condition check: a course only counts as "Validated" if the score is at least 50 *and* attendance is at least 75%, otherwise it's either "Blocked: low attendance" or "Failed". I also had to explain in a sentence why the order of the `elif` checks matters — if you check `>= 50` before `>= 70`, everything above 50 gets swallowed by the wrong branch.

**Part 2 — Loops & the Accumulator (7 marks)**
Filtered a list of scores to just the ones ≥ 80, then practiced the accumulator pattern by hand — no `sum()`, `len()`, or `max()` allowed — to get the total, count, average, and pass/fail counts. Finished with a `while` loop working out how many months it'd take to save 250,000 RWF at 15,000 RWF a month, being careful not to write an infinite loop.

**Part 3 — Functions (6 marks)**
Turned the Part 1 grading ladder into a proper function, `get_grade(score)`, with a docstring, and wrote `pass_rate(score_list)` to return the percentage of passing scores using the same accumulator idea — expected 90.0% on the Part 2 list.

**Part 4 — Reading the File (5 marks)**
Opened `week3_students.csv` with `with open(...) as f:` and `readlines()`, and printed the line count, the header, and the first student's row. There are 41 lines, not 40, because of the header row. Then looped through and pulled out just the `name` column into a list.

**Part 5 — The Resilient Pipeline (12 marks)**
This was the core of the lab. Looped through every row and used `try`/`except ValueError` to convert each score to an integer — on success it counts toward the total, on failure the student ID gets logged to `bad_ids`. Checkpoint: exactly 3 broken records should turn up. From there, among the valid rows, I tracked pass/fail counts and found the top-scoring student using two accumulators (`best_score = -1`, `best_name = ""`), then ran their score through `get_grade`. As a stretch, I broke scores down by district using two dictionary accumulators to find the district with the highest average.

**Bonus — Output File (+3)**
Wrote a short report — student count, valid/bad counts, average, top student — to `week3_report.txt`, then read it back in and printed it to confirm it saved correctly.

## My results

- **Broken record IDs found:** ___
- **Valid records / average score:** ___
- **Top student & grade:** ___
- **District with the highest average score:** ___
- **Months to save for the laptop (2.3):** ___

## Reflection

1. My pipeline skipped 3 out of 40 records (7.5%). At what point would I stop trusting a dataset like this, and what would I do instead of just skipping the bad rows?
2. One thing from this session that surprised or confused me: ___

## Marking scheme

| Part | Topic | Marks |
|---|---|---|
| 1 | Making Decisions | 5 |
| 2 | Loops & the Accumulator | 7 |
| 3 | Functions | 6 |
| 4 | Reading the File | 5 |
| 5 | The Resilient Pipeline | 12 |
| **Total** | | **35** |
| Bonus | Output file | +3 |

## Before I submit

- [ ] Notebook renamed `Week3_YourName`
- [ ] Everything runs without errors
- [ ] 3 broken records identified
- [ ] Reflection answered
- [ ] Screenshots included
- [ ] Short report written
- [ ] Submitted before the end of Week 3