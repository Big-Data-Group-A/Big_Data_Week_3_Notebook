# Week 3 Lab — Control Flow & Functions

**Course:** Introduction to Big Data Analytics
**Instructor:** Prince Ishimwe
**Notebook:** `Week3_SultanRay28214.ipynb`
**Dataset:** `week3_students.csv`

## Overview

This notebook covers control flow (if/elif/else, for/while loops), functions,
file reading, and a resilient data pipeline that handles broken records in
the student dataset.

## Files

| File | Description |
|---|---|
| `Week3_SultanRay28214.ipynb` | Main notebook with all exercises (Parts 1–5 + bonus) |
| `week3_students.csv` | Dataset: 40 students, 8 columns (student_id, name, age, gender, program, district, attendance_pct, score) |
| `week3_report.txt` | Auto-generated summary report (written and read back in the Bonus exercise) |

## How to run

1. Place `week3_students.csv` in the same folder as the notebook.
2. Run all cells top to bottom (`Runtime > Run all` in Colab, or `Cell > Run All` in Jupyter).
3. `week3_report.txt` will be created automatically by the Bonus cell.

## Structure

- **Part 1 — Decisions:** grading ladder, combined conditions (score + attendance)
- **Part 2 — Loops:** filtering, accumulator pattern, while loop (savings goal)
- **Part 3 — Functions:** `get_grade(score)`, `pass_rate(score_list)`
- **Part 4 — Reading the file:** `readlines()`, extracting the `name` column
- **Part 5 — Resilient pipeline:**
  - 5.1: parses `score` with `try/except ValueError`, isolating bad records
  - 5.2: finds pass/fail counts and the top-scoring student among valid rows
  - 5.3: average score per district (8 districts, 5 students each)
- **Bonus:** writes a summary to `week3_report.txt` and reads it back

## Broken records found

The dataset contains 3 rows with a non-numeric `score` value:

| Student ID | Issue |
|---|---|
| AUCA008 | `N/A` |
| AUCA020 | empty value (trailing comma, no score) |
| AUCA032 | `absent` |

All 3 are caught by `int(parts[7])` raising `ValueError`, so they're excluded
from `total`/`count` but logged in `bad_ids` rather than crashing the pipeline.

## Reflection notes

- 3 out of 40 broken records (7.5%) is small enough that skipping is a
  reasonable default, but a rule of thumb worth stating: if a much higher
  share of a column were broken, the fix should shift from *skipping* rows
  to *investigating* the source (was it a bad export? a form that allowed
  free text where it shouldn't have?) rather than silently dropping data.
