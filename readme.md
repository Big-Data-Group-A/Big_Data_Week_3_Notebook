WEEK 3 LAB REPORT — Control Flow & Functions

Student ID : 29254
Name       : Didier Ndahimana


1. WHAT IT DOES
Reads week3_students.csv (40 rows), loops over each row, uses
try/except to survive non-numeric scores. Valid rows update
total, count, passed, failed, and top student. Broken rows
increment 'bad' and store the student_id in 'bad_ids'.

2. THE 3 BROKEN RECORDS
  1. [AUCA0XX] — [name] — score was: [value]
  2. [AUCA0XX] — [name] — score was: [value]
  3. [AUCA0XX] — [name] — score was: [value]

3. HOW THE CODE SURVIVED THEM
int(parts[7]) was inside try/except ValueError. A bad value
jumped to the except branch, counted as bad, saved the id,
and the loop continued to the next row — no crash, no lost
data.

Results:
  Valid: [37]   Bad: [3]   Average: [75.3]
  Passed: [34]  Failed: [3]
  Top student: [name] with [score] — grade [X]

4. REFLECTION
(a) Past ~5-10% bad rows, skipping starts to bias the
    average because the missing rows aren't random. I'd
    report the bad ids, fix them at the source, and
    document any exclusions openly.
(b) [One honest sentence — e.g. "I was surprised that
    sum() and len() are just loops someone already wrote."]

5. FILES
- Week3_[YourName].ipynb
- screenshots/
- README.txt
- week3_report.txt (bonus)



