# Week 3 Lab Report — Control Flow & Functions

## 1. Introduction

This lab focuses on Python control flow, loops, functions, and file handling. The main objective is to process student records, calculate grades and statistics, and build a reliable data-processing pipeline that can handle invalid data.

## 2. Objectives

* Use conditional statements to determine student grades and validation status.
* Apply `for` and `while` loops to process data and perform calculations.
* Create reusable functions for grading and calculating pass rates.
* Read and process student records from a CSV file.
* Handle invalid scores using `try/except` to prevent program errors.
* Calculate student statistics and analyze results by district.

## 3. Methodology

The lab was organized into six parts:

1. **Making Decisions:** Used `if/elif/else` statements to assign letter grades and determine whether students meet the course validation requirements based on scores and attendance.

2. **Loops & Accumulators:** Used loops to filter high scores, calculate totals and averages, count passed and failed students, and determine the number of months needed to save for a laptop.

3. **Functions:** Created reusable functions to return letter grades and calculate the percentage of students who passed.

4. **Reading the File:** Opened the `week3_students.csv` file, read its contents, and extracted student names for further processing.

5. **The Resilient Pipeline:** Processed student records, handled invalid scores with exception handling, calculated statistics, identified the top student, and calculated average scores for each district.

6. **Reflection:** Considered the reliability of datasets containing invalid records and reflected on lessons learned during the session.

## 4. Results

The dataset contains 40 student records. According to the lab instructions, 3 records have invalid scores, representing 7.5% of the dataset.

The pipeline is designed to identify these records, process valid scores, calculate the average, determine pass and fail counts, identify the highest-scoring student, and compare district averages.

**Results to complete after running the notebook:**

* Number of valid records: 37
* Number of invalid records: 3 
* Average valid score: 75.27
* Top student and score:  Bonaventure Nkurunziza (95)
* District with the highest average: Muhanga

## 5. Challenges and Lessons Learned

One important challenge was handling invalid score values without stopping the entire program. Using `try/except` helps the pipeline continue processing valid records while identifying errors.

The lab also demonstrated the importance of initializing and updating accumulator variables correctly, using functions to avoid repeating code, and checking data quality before drawing conclusions.

## 6. Reflection

If more than 10% of a dataset's records were invalid, I would investigate its reliability rather than automatically skipping the errors. I would check the original data source, correct invalid values where possible, and document any records that cannot be recovered.

One thing that surprised me was how exception handling allows a program to continue running even when it encounters invalid data. This showed me why error handling is important when working with real-world datasets.

## 7. Conclusion

This lab provided practical experience with Python control flow, loops, functions, and CSV file processing. It demonstrated how these concepts can be combined to analyze student records and handle invalid data. The exercises also highlighted the importance of data validation, error handling, and reliable calculations in data analytics.
