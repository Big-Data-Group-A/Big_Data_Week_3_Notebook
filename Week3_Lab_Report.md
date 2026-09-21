# Week 3 Lab Report: Control Flow & Functions
**Course:** Introduction to Big Data Analytics  
**Student Name:** Kwizera Pacifique  
**Student ID:** 28054  
**Date:** September 21, 2026  
**Repository Branch:** `week3/28054-kwizera-pacifique`  
**Colab Notebook:** [Google Colab Link](https://colab.research.google.com/drive/1OrjIuYpLPeS-WZv4dluKQEkSjZbraUL9?usp=sharing)  

---

## 1. Executive Summary

This report documents the implementation and results for **Week 3 Lab: Control Flow & Functions**. Using raw student records from `week3_students.csv`, a resilient Python data pipeline was constructed to clean, filter, and aggregate student performance metrics without halting on corrupted data.

Out of **40 total student records**, the pipeline successfully validated **37 clean records** and safely isolated **3 broken records (7.5% corruption rate)**. All exercises from Parts 1 through 5, including the Bonus output file generation and Part 6 Reflection questions, were implemented and verified with zero runtime errors.

---

## 2. Identified Broken Records

During the dataset iteration, parsing the `score` column (index 7) with `int()` revealed 3 corrupted entries that would otherwise crash standard scripts:

| Student ID | Student Name | Program | District | Attendance % | Raw Score Value | Cause of Failure |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **AUCA008** | Emmanuel Nsengiyumva | Accounting | Rubavu | 65% | `"N/A"` | Non-numeric placeholder string |
| **AUCA020** | Samuel Rukundo | Accounting | Kicukiro | 94% | `""` | Missing value (empty string) |
| **AUCA032** | Gilbert Uwituze | Accounting | Rubavu | 63% | `"absent"` | Textual status instead of numerical score |

---

## 3. How the Code Survived Dirty Data

### Resilient Architecture (`try / except ValueError`)

In Python, invoking `int()` on non-numeric or empty string representations throws an immediate `ValueError`. Without defensive handling, this terminates execution on line 9 (AUCA008). 

To ensure fault tolerance, our pipeline wrapped score casting inside a `try...except ValueError` block:

```python
# Exercise 5.1 - Resilient Pipeline
valid_count = 0
bad_count = 0
total_valid_score = 0
bad_ids = []

for line in lines[1:]:
    parts = line.strip().split(',')
    student_id = parts[0]
    score_str = parts[7]

    try:
        score = int(score_str)
        total_valid_score += score
        valid_count += 1
    except ValueError:
        bad_count += 1
        bad_ids.append(student_id)

valid_avg = round(total_valid_score / valid_count, 1)
```

### Key Engineering Principles Applied:
1. **Graceful Degradation:** Malformed records were intercepted and quarantined (`bad_ids`) rather than allowing the application to crash.
2. **Data Isolation:** Broken rows were excluded from numerical accumulators (`total_valid_score` and `valid_count`), preserving mathematical accuracy for statistical metrics.
3. **Auditability:** Problematic student IDs (`AUCA008`, `AUCA020`, `AUCA032`) were logged to allow follow-up administrative verification.

---

## 4. Key Findings & Analytics Results

* **Total Records Processed:** 40
* **Valid Records:** 37
* **Corrupted Records:** 3 (7.5%)
* **Valid Scores Average:** **75.3** (Total points: 2,786 across 37 students)
* **Valid Students Passed (≥ 50):** 35 (94.6%)
* **Valid Students Failed (< 50):** 2 (5.4% — AUCA013: 47, AUCA025: 48)
* **Top Performing Student:** **Bonaventure Nkurunziza** (Student ID: AUCA024, Score: **95**, Grade: **A**)
* **Top Performing District:** **Muhanga** (Highest district average of **87.00**)

### District Performance Breakdown:
| District | Average Score | Status |
| :--- | :---: | :--- |
| **Muhanga** | **87.00** | 🏆 Highest District Average |
| **Nyagatare** | 82.80 | High Performance |
| **Gasabo** | 80.40 | High Performance |
| **Rubavu** | 78.67 | Above Class Average |
| **Nyarugenge** | 74.80 | Near Class Average |
| **Huye** | 68.40 | Passing |
| **Musanze** | 65.20 | Passing |
| **Kicukiro** | 64.00 | Passing |

---

## 5. Reflection (Part 6)

### 1. Data Trust Threshold & Remediation
> **Question:** *Your pipeline skipped 3 broken records out of 40 (7.5%). At what percentage would you stop trusting the dataset — and what would you do instead of skipping?*

**Response:**  
At **7.5%**, skipping missing or corrupt records is an acceptable compromise for exploratory data analysis, as 37 records remain sufficient to capture central tendencies. However, if corrupt records reach **15% or higher**, I would stop trusting the dataset for direct automated processing, because dropping 15%+ of samples introduces substantial **selection bias** and distorts district/program distributions.

Instead of silently skipping:
1. **Upstream Source Audit:** Halt automatic ingestion and query the database logs or upstream collection forms to diagnose the root cause (e.g., frontend input validation bugs or CSV export delimiter collisions).
2. **Domain-Specific Imputation:** For records with missing scores but valid attendance, apply principled statistical imputation (such as district or program medians) with an explicit `imputed_flag` boolean column.
3. **Dead-Letter Quarantine (DLQ):** Route invalid records to an administrative review queue with error metadata so registrar staff can provide verified make-up scores.

### 2. Session Takeaway & Learning
> **Question:** *Describe one thing from today's session that surprised or confused you.*

**Response:**  
What surprised me most was how brittle standard Python type conversion (`int()`) is when applied to real-world CSV files. A single string like `"absent"` or an empty string `""` halts the entire script if not explicitly guarded. Discovering how few lines of defensive code (`try...except ValueError`) are required to make a pipeline robust and capable of completing data processing without human intervention was a highlight of this lab.

---

## 6. Execution Verification & Screenshots

All 9 uncropped execution screenshots demonstrating error-free execution across all parts of the lab have been organized in the `screenshots/` directory:

| Step / Exercise | Filename | Description |
| :--- | :--- | :--- |
| **Part 1 (Ex 1.1 & 1.2)** | [`screenshots/01_Exercise_1.1_and_1.2.png`](./screenshots/01_Exercise_1.1_and_1.2.png) | Grading ladder (A–F) and AUCA validation logic with compound boolean conditions. |
| **Part 2 (Ex 2.1 & 2.2)** | [`screenshots/02_Exercise_2.1_and_2.2.png`](./screenshots/02_Exercise_2.1_and_2.2.png) | Loop filtering scores ≥ 80 and custom accumulators (without built-ins). |
| **Part 2 (Ex 2.3)** | [`screenshots/03_Exercise_2.3.png`](./screenshots/03_Exercise_2.3.png) | While loop calculating monthly savings for 250,000 RWF laptop (17 months). |
| **Part 3 (Ex 3.1 & 3.2)** | [`screenshots/04_Exercise_3.1_and_3.2.png`](./screenshots/04_Exercise_3.1_and_3.2.png) | Pure functions `get_grade(score)` and `pass_rate(score_list)` with docstrings. |
| **Part 4 (Ex 4.1 & 4.2)** | [`screenshots/05_Exercise_4.1_and_4.2.png`](./screenshots/05_Exercise_4.1_and_4.2.png) | File ingestion with `open()`, line counting (41 lines), and column extraction. |
| **Part 5 (Ex 5.1 & 5.2)** | [`screenshots/06_Exercise_5.1_and_5.2.png`](./screenshots/06_Exercise_5.1_and_5.2.png) | `try-except` resilient loop identifying 3 broken records and finding top student. |
| **Part 5 (Ex 5.3 Code)** | [`screenshots/07_Exercise_5.3_Code.png`](./screenshots/07_Exercise_5.3_Code.png) | Dictionary accumulators computing sums and counts per district. |
| **Part 5 (Ex 5.3 Output)**| [`screenshots/08_Exercise_5.3_Output.png`](./screenshots/08_Exercise_5.3_Output.png) | Printed averages for all 8 districts, crowning Muhanga as top district. |
| **Bonus (+3 Output File)**| [`screenshots/09_Bonus_Output_File.png`](./screenshots/09_Bonus_Output_File.png) | Writing summary report to `week3_report.txt` and reading it back to verify. |

---

## 7. Submission Checklist Verification

- [x] **Notebook renamed:** `Week3_Kwizera_Pacifique.ipynb`
- [x] **All exercises run without errors:** Verified across Parts 1–5 and Bonus
- [x] **3 broken records identified:** AUCA008 (`"N/A"`), AUCA020 (`""`), AUCA032 (`"absent"`)
- [x] **Reflection (Part 6) answered:** Thoroughly detailed in notebook and report
- [x] **Screenshots included:** 9 uncropped screenshots ordered in `screenshots/`
- [x] **Short report included:** `Week3_Lab_Report.md` / `Week3_Lab_Report.pdf`
- [x] **Branch created:** `week3/28054-kwizera-pacifique` ready for Pull Request
