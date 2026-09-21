# Week 3 Lab Report — Control Flow, Functions & File Handling

## 1. Short Report

This Week 3 lab focused on using Python control flow, loops, functions, file handling, data validation, and exception handling to process student records.

The lab was completed through several parts, starting with basic decision-making and gradually building a data-processing workflow using the provided student dataset.

### Main Tasks Completed

- Used `if`, `elif`, and `else` statements to make decisions based on student scores and attendance.
- Used `for` and `while` loops to process data and perform calculations.
- Created reusable functions for grading and calculating results.
- Read student records from a CSV file.
- Used `try/except` to handle invalid data without stopping the program.
- Calculated statistics from the student records.
- Analyzed the student data by district.

### Data Validation and Bad Records

During the data validation process, the dataset contained three invalid student records.

The identified bad student IDs were:

- `AUCA008`
- `AUCA020`
- `AUCA032`

These records were handled as invalid data during the processing stage so that they would not cause the rest of the program to fail.

### Data Processing Pipeline

The work followed a simple data-processing pipeline:

1. **Read the data**  
   The student records were loaded from the CSV file.

2. **Validate the data**  
   Student records were checked for invalid values and the three bad IDs were identified: `AUCA008`, `AUCA020`, and `AUCA032`.

3. **Process and analyze the data**  
   Valid records were processed to calculate grades, statistics, pass/fail results, and other required outputs.

The use of exception handling helped the program continue processing the dataset even when invalid records were encountered.

---

## 2. Reflection

This lab helped me understand how different Python concepts can work together to solve a data-processing problem.

One of the main things I learned was how to use conditional statements and loops to process multiple student records efficiently. I also learned how functions can make the code more organized and reusable instead of repeating the same logic.

Another important part of the lab was handling invalid data. The dataset contained three bad student IDs: `AUCA008`, `AUCA020`, and `AUCA032`. Using validation and `try/except` helped me understand how programs can deal with unexpected or invalid data without crashing completely.

The lab also showed me that data processing is not only about writing code. The data needs to be checked, cleaned, processed, and then analyzed to produce meaningful results.

Overall, this lab improved my understanding of Python control flow, functions, loops, file handling, validation, and exception handling, and showed me how these concepts can be combined into a basic data-processing pipeline.