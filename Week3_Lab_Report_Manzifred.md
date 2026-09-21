# Week 3 Lab Report - Control Flow & Functions

**Course:** Introduction to Big Data Analytics  
**Student Name:** Manzifred  
**Student ID:** 26634  
**Date:** September 21, 2026  
**Branch:** week3/26634-manzi  

---

## Summary

This report covers my work for Week 3 lab on control flow and functions. I worked through the dataset week3_students.csv which has 40 student records. The main challenge was that 3 of those records had broken scores that would crash the program if not handled properly. I used try/except to deal with that and managed to get results from the 37 valid records.

---

## The 3 Broken Records

When I looped through the file and tried to convert the score column to an integer using int(), it failed on 3 rows. Here is what was in those rows:

| Student ID | Name | Score Value | Why it failed |
|---|---|---|---|
| AUCA008 | Emmanuel Nsengiyumva | N/A | that is a string, not a number |
| AUCA020 | Samuel Rukundo | (nothing) | the cell was empty |
| AUCA032 | Gilbert Uwituze | absent | that is a string, not a number |

Python throws a ValueError when you call int() on something that is not a number. The try/except block I wrote catches that error and instead of crashing, it just adds the student ID to a bad_ids list and moves on to the next row.

```python
for line in lines[1:]:
    parts = line.strip().split(",")
    try:
        score = int(parts[7])
        total = total + score
        valid = valid + 1
    except ValueError:
        bad = bad + 1
        bad_ids.append(parts[0])
```

This way none of the good data gets lost and at the end I can see exactly which students had the problem.

---

## Results

- Total students: 40  
- Valid records: 37  
- Bad records: 3  
- Average score (valid only): 75.3  
- Passed (score >= 50): 35  
- Failed (score < 50): 2  
- Top student: Bonaventure Nkurunziza, score 95, grade A  
- Best district: Muhanga (average 87.00)  

### Scores by district

| District | Average Score |
|---|---|
| Gasabo | 80.40 |
| Huye | 68.40 |
| Kicukiro | 64.00 |
| Muhanga | 87.00 |
| Musanze | 65.20 |
| Nyagatare | 82.80 |
| Nyarugenge | 74.80 |
| Rubavu | 78.67 |

Muhanga came out on top with 87.00, well above the class average of 75.3.

---

## Reflection

**Question 1:** At what percentage would you stop trusting the dataset, and what would you do instead of skipping?

At 7.5% I think it is still okay to skip the bad rows because there are enough valid records left to work with. But if the number of broken records went up to something like 15% or higher, I would be more careful. At that point there is a real chance the missing data is not random. Maybe all the students with no score were absent the same day, or they all come from the same district. If I skip them without checking, the averages and other results will look better than they really are.

What I would do instead is first try to find out where the data came from and why those values are missing. If I can get the actual scores from the registrar I would fill them in. If not, I would replace the missing values with the average for that district or program, but mark those rows clearly so it is obvious they were estimated and not real values. The key thing is to never just quietly remove data without saying so anywhere in the output.

**Question 2:** What surprised or confused you from today's session?

Scope confused me more than I expected. I had written a variable inside a function and then tried to print it from outside the function and got a NameError. My first thought was that something was broken, but actually it is just how Python works. Variables that are created inside a function only exist while that function is running. Once it is done they are gone. The only way to get a value out is to use return. Once I understood that it made sense, but it took me a moment because I kept expecting it to behave like code written outside any function.

---

## Submission checklist

- [x] Notebook: Week3_Manzifred.ipynb  
- [x] All exercises completed and running without errors  
- [x] 3 broken records found: AUCA008, AUCA020, AUCA032  
- [x] Reflection answered  
- [x] Report written  
- [x] Branch: week3/26634-manzi  
- [ ] Screenshots (to be taken from Google Colab)  
- [ ] Submitted before end of Week 3  
