# Week 3 Lab Report: Control Flow & Functions
**Course:** Introduction to Big Data Analytics  
**Student Name:** Manzifred  
**Student ID:** 26634  
**Date:** September 21, 2026  
**Repository Branch:** `week3/26634-manzi`  

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

In Python, invoking `int()` on a non-numeric or empty string throws an immediate `ValueError`. Without defensive handling, this terminates execution on row AUCA008. To ensure fault tolerance, the pipeline wraps score casting inside a `try...except ValueError` block:

```python
# Exercise 5.1 — Resilient Pipeline
total   = 0
valid   = 0
bad     = 0
bad_ids = []

for line in lines[1:]:
    parts = line.strip().split(",")
    try:
        score = int(parts[7])        # raises ValueError for broken values
        total = total + score
        valid = valid + 1
    except ValueError:
        bad = bad + 1
        bad_ids.append(parts[0])     # log the broken student_id

average_valid = total / valid
```

### Key Principles Applied

1. **Graceful Degradation:** Malformed records are intercepted and quarantined (`bad_ids`) rather than crashing the program.
2. **Data Isolation:** Broken rows are excluded from numerical accumulators (`total` and `valid`), preserving accuracy for statistical metrics.
3. **Auditability:** Problematic student IDs are logged so that administrative follow-up is possible.

---

## 4. Key Findings & Analytics Results

- **Total Records Processed:** 40
- **Valid Records:** 37
- **Corrupted Records:** 3 (7.5%)
- **Valid Scores Average:** **75.3**
- **Passed (≥ 50):** 35
- **Failed (< 50):** 2
- **Top Performing Student:** **Bonaventure Nkurunziza** (AUCA024, Score: **95**, Grade: **A**)
- **Top Performing District:** **Muhanga** (highest district average)

### District Performance Breakdown

| District | Avg Score |
| :--- | :---: |
| Gasabo | 80.40 |
| Huye | 68.40 |
| Kicukiro | 64.00 |
| Muhanga | **87.00** 🏆 |
| Musanze | 65.20 |
| Nyagatare | 82.80 |
| Nyarugenge | 74.80 |
| Rubavu | 78.67 |

---

## 5. Reflection (Part 6)

### Question 1 — Data Trust Threshold & Remediation

> *At what percentage would you stop trusting the dataset — and what would you do instead of skipping?*

At 7.5%, skipping is acceptable: 37 valid records are sufficient for meaningful analysis. However, if the bad-record rate crossed **15%**, I would stop trusting the dataset for direct automated processing, because dropping 15%+ of samples introduces substantial **selection bias** and distorts district/program distributions.

Instead of silently skipping, I would:
1. **Investigate the root cause** — query the registrar or exam system logs to diagnose why values are missing.
2. **Impute cautiously** — replace missing scores with the district or program median, and add an `imputed_flag` column.
3. **Report transparently** — always state the missing-data rate in any output so readers can judge reliability themselves.

### Question 2 — Session Takeaway

> *Describe one thing from today's session that surprised or confused you.*

The concept that surprised me most was **variable scope**. I assumed that a variable created inside a function would still be accessible after the function ran. Discovering that it disappears — and that `return` is the only way to get a value out — completely changed how I think about functions. Without scope, every variable name in every function would risk colliding with variables in the rest of the program. `return` is the deliberate, controlled output port.

---

## 6. Submission Checklist

- [x] Notebook renamed: `Week3_Manzifred.ipynb`
- [x] All exercises run without errors (Parts 1–5 + Bonus)
- [x] 3 broken records identified: AUCA008 (`"N/A"`), AUCA020 (`""`), AUCA032 (`"absent"`)
- [x] Reflection (Part 6) answered
- [x] Short report: `Week3_Lab_Report_Manzifred.md`
- [x] Branch created: `week3/26634-manzi`
- [ ] Screenshots *(take in Google Colab after running all cells)*
- [ ] Submitted before end of Week 3
