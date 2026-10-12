# Week 3 Lab: Control Flow & Functions

**Student:** Hirwa Ngenzi Honore
**Student ID:** 29111
**Course:** Introduction to Big Data Analytics, AUCA
**Instructor:** Prince Ishimwe
**Lab:** Week 3, "Decide, Repeat, Recover" (35 marks + 3 bonus)

## About this lab

This lab covers `if/elif/else` decisions, `for` and `while` loops, the
accumulator pattern, functions, reading a file, `try/except` error handling,
and dictionary accumulators. The dataset has 40 students, and 3 of the records
have broken scores that the code must survive.

## Repository contents

| File / folder | Description |
|---|---|
| `Lab_2.pdf` | Lab instructions (Week 3) |
| `Week3_HirwaNgenzi.ipynb` | Completed lab notebook |
| `week3_students.csv` | Student dataset (40 students) |
| `week3_report.txt` | Output file written by the Bonus exercise |
| `screenshots/` | Screenshots of the output of each part |
| `README.md` | This file |

> File names above should match what is actually in the repository. Edit this
> table if a name is different.

## Dataset

Columns (by index): `0 student_id`, `1 name`, `2 age`, `3 gender`,
`4 program`, `5 district`, `6 attendance_pct`, `7 score`.

The file has 41 lines: 1 header line plus 40 students.

## How to run

1. Put `week3_students.csv` in the same folder as the notebook.
2. Open `Week3_HirwaNgenzi.ipynb` and choose Restart and Run All.

No extra libraries are needed. Everything uses built-in Python.

## Broken records

3 of the 40 records have scores that are not numbers. The pipeline reads each
score inside `try/except ValueError`, counts the bad row, saves its ID, and
continues instead of crashing.

| Student ID | Name | Broken score |
|---|---|---|
| AUCA008 | Emmanuel Nsengiyumva | `N/A` |
| AUCA020 | Samuel Rukundo | empty |
| AUCA032 | Gilbert Uwituze | `absent` |

## Key results

| Question | Result |
|---|---|
| Valid / bad records | 37 / 3 |
| Average of valid scores | 75.3 |
| Passed / failed (valid rows) | 35 / 2 |
| Top student | Bonaventure Nkurunziza, 95 (grade A) |
| District with the highest average | Muhanga (87.0) |
| Part 2 list: total / average | 734 / 73.4 |
| Part 2 list: pass rate | 90.0% |
| Months to save for the laptop | 17 |

District averages (valid scores only): Muhanga 87.0, Nyagatare 82.8,
Gasabo 80.4, Rubavu 78.7, Nyarugenge 74.8, Huye 68.4, Musanze 65.2,
Kicukiro 64.0. Rubavu has 3 valid students and Kicukiro has 4, because the
broken records fall in those districts.

## Screenshots

Screenshots of each part's output are in the `screenshots/` folder.

| Part | File |
|---|---|
| Part 1: Making decisions | `screenshots/part1_decisions.png` |
| Part 2: Loops and the accumulator | `screenshots/part2_loops.png` |
| Part 3: Functions | `screenshots/part3_functions.png` |
| Part 4: Reading the file | `screenshots/part4_reading_file.png` |
| Part 5.1 and 5.2: Resilient pipeline and top student | `screenshots/part5_pipeline.png` |
| Part 5.3: Report by district | `screenshots/part5_districts.png` |
| Bonus: Output file | `screenshots/bonus_report_file.png` |
