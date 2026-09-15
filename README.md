# Big Data — Week 3 Lab: Control Flow & Functions

**Course:** Introduction to Big Data Analytics (AUCA)
**Instructor:** Prince Ishimwe — Prince.ishimwe@auca.ac.rw
**Total marks:** 35 (+3 bonus) · **Due:** end of Week 3

This repository holds the Week 3 lab assignment and dataset. Every student works on their **own branch** in this repo — do not commit directly to `main`.

## What's in this repo

| File | Purpose |
|---|---|
| [`Lab 2.pdf`](./Lab%202.pdf) | The full lab handout: all exercises, instructions, and the marking scheme (Parts 1–6). |
| [`week3_students.csv`](./week3_students.csv) | The dataset used in every exercise (40 students, 3 with intentionally broken scores). |
| [`week3_students.xlsx`](./week3_students.xlsx) | Same dataset in spreadsheet form, for reference/inspection. |

Read `Lab 2.pdf` first — it has the exercises, the exact columns/indices you'll use with `split(",")`, and the submission checklist.

## How to work on this assignment

### 1. Clone the repo

```bash
git clone https://github.com/Big-Data-Group-A/Big_Data_Week_3_Notebook.git
cd Big_Data_Week_3_Notebook
```

### 2. Create your own branch

Never work directly on `main`. Branch off it using your student ID and name:

```bash
git checkout main
git pull
git checkout -b week3/AUCA0XX-yourlastname
```

Example: `week3/AUCA001-uwase`

### 3. Do the lab

- Create your notebook as **`Week3_YourName.ipynb`** (Colab or Jupyter) inside your branch.
- Keep `week3_students.csv` in the same folder as your notebook (Colab: use the folder icon → upload).
- Work through Parts 1–6 in `Lab 2.pdf`:
  - Part 1 — Making Decisions (if/elif/else)
  - Part 2 — Loops & the Accumulator pattern
  - Part 3 — Functions (`get_grade`, `pass_rate`)
  - Part 4 — Reading the file with `open()`/`readlines()`
  - Part 5 — The Resilient Pipeline (finding the 3 broken records with `try`/`except`)
  - Part 6 — Reflection questions (required)
  - Bonus (+3) — write and re-read `week3_report.txt`
- Write your ½–1 page report identifying the 3 broken student records and how your code handled them.
- Take the screenshots requested in the handout.

### 4. Commit your work to your branch

```bash
git add Week3_YourName.ipynb <your-report-file> <your-screenshots>
git commit -m "Week 3 lab submission - Your Name"
git push -u origin week3/AUCA0XX-yourlastname
```

### 5. Submit by opening a Pull Request

Open a Pull Request from your branch into `main` (title it with your name and student ID). This is how the instructor/TA will review and grade your submission — **do not merge your own PR**.

## Ground rules

- One branch per student — don't edit another student's branch or files.
- Don't push directly to `main`.
- Don't modify `week3_students.csv`/`.xlsx` — everyone uses the same dataset.
- Everything needed for this lab was covered in the Week 3 session — check the slides before searching online.

## Submission checklist (from the handout)

- [ ] Notebook renamed `Week3_YourName`
- [ ] All exercises run without errors
- [ ] 3 broken records identified
- [ ] Reflection (Part 6) answered
- [ ] Screenshots included
- [ ] Short report included
- [ ] Pull request opened before the end of Week 3
