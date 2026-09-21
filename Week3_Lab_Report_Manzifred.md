# Week 3 Lab Report - Control Flow & Functions

**Name:** Manzifred  
**ID:** 26634  
**Course:** Introduction to Big Data Analytics  
**Date:** September 21, 2026

---

## What I did

This lab was about using if/else, loops, functions, reading a csv file and handling bad data. The dataset had 40 students but 3 of them had broken scores so I had to use try/except to skip those without crashing the whole program.

---

## The 3 broken records

When I tried to convert the score column to int() it failed on these three:

| Student ID | Name | Score found |
|---|---|---|
| AUCA008 | Emmanuel Nsengiyumva | N/A |
| AUCA020 | Samuel Rukundo | empty |
| AUCA032 | Gilbert Uwituze | absent |

The try/except block caught the ValueError each time and saved the student ID to a list so I could report them at the end. The other 37 records all worked fine.

---

## Results from the pipeline

- Valid: 37, Bad: 3
- Average score: 75.3
- Passed: 35, Failed: 2
- Top student: Bonaventure Nkurunziza, score 95, grade A
- Best district: Muhanga with average 87.00

---

## Reflection

**Q1: At what point would you stop trusting the data?**

At 7.5% skipping is fine, 37 records is still enough to work with. But if it went up to like 15 or 20 percent I would be more careful because the missing ones might all share something in common like being from the same district, which would mess up the results. I would try to get the real scores from the registrar first, and if not possible I would fill them in with the district average and mark them clearly so anyone reading knows they are estimates.

**Q2: What confused you?**

Variable scope. I created a variable inside a function and then tried to use it outside and got a NameError. I didn't realise variables inside a function disappear once it finishes running. You have to use return to get the value out. Once I understood that it was fine but it caught me off guard.
