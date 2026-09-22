Exercise 1.1 — The grading ladder
def print_grade(score):
    if score >= 85:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"{score} -> {grade}")

for score in [91, 76, 64, 52, 43]:
    print_grade(score)


 Exercise 1.2 — Combined conditions
def validation_status(score, attendance):
    if score >= 50 and attendance >= 75:
        return "Validated"
    elif score >= 50 and attendance < 75:
        return "Blocked: low attendance"
    else:
        return "Failed"

tests = [(76, 92), (76, 68), (43, 95)]
for score, attendance in tests:
    print(score, attendance, "->", validation_status(score, attendance))

scores = [72, 85, 91, 64, 78, 47, 88, 55, 93, 61]

 Exercise 2.1 — Loop + filter
for score in scores:
    if score >= 80:
        print(f"Top score: {score}")

 Exercise 2.2 — Accumulator pattern
 No sum(), len(), or max() is used here.
total = 0
count = 0
passed = 0
failed = 0

for score in scores:
    total += score
    count += 1

    if score >= 50:
        passed += 1
    else:
        failed += 1

average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Passed:", passed)
print("Failed:", failed)


 Exercise 2.3 — while loop
saved = 0
months = 0
target = 250000
monthly_saving = 15000

while saved < target:
    saved += monthly_saving
    months += 1

print("Months needed:", months)
print("Amount saved:", saved, "RWF")


 Exercise 3.1 — get_grade
def get_grade(score):
    """Return the letter grade for a score."""
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

for score in [91, 76, 43]:
    print(score, "->", get_grade(score))

Exercise 3.2 — pass_rate
def pass_rate(score_list):
    passed = 0
    count = 0

    for score in score_list:
        count += 1
        if score >= 50:
            passed += 1

    return (passed / count) * 100

print("Pass rate:", pass_rat 
      
 Exercise 4.1 — First contact
with open("week3_students.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))
print("Header line:", lines[0].strip())
print("First student's line:", lines[1].strip())

 There are 41 lines because there is 1 header line plus 40 student records.

 Exercise 4.2 — Extract a column
names = []

for line in lines[1:]:
    parts = line.strip().split(",")
    names.append(parts[1])

print("Name count:", len(names))
print("First 5 names:", names[:5])


 Exercise 5.1 — Survive the mess
total = 0
valid_count = 0
bad_count = 0
bad_ids = []

with open("week3_students.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    try:
        score = int(parts[7])
        total += score
        valid_count += 1
    except ValueError:
        bad_count += 1
        bad_ids.append(parts[0])

average_valid = total / valid_count

print("Valid:", valid_count)
print("Bad:", bad_count)
print("Bad IDs:", bad_ids)
print("Average of valid scores:", round(average_valid, 1))


 Exercise 5.2 — Grades & the top student
passed = 0
failed = 0
best_score = -1
best_name = ""

for line in lines[1:]:
    parts = line.strip().split(",")
    try:
        score = int(parts[7])
    except ValueError:
        continue

    if score >= 50:
        passed += 1
    else:
        failed += 1

    if score > best_score:
        best_score = score
        best_name = parts[1]

print("Passed:", passed)
print("Failed:", failed)
print("Best score:", best_score)
print("Best student:", best_name)
print("Top student's grade:", get_grade(best_score))


Exercise 5.3 — Report by district
sums = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    d = parts[5]

    try:
        s = int(parts[7])
    except ValueError:
        continue

    sums[d] = sums.get(d, 0) + s
    counts[d] = counts.get(d, 0) + 1

highest_district = ""
highest_average = -1

for d in sums:
    average = sums[d] / counts[d]
    print(d, "average:", round(average, 1))

    if average > highest_average:
        highest_average = average
        highest_district = d

print("Highest-average district:", highest_district)
print("Highest district average:", round(highest_average, 1))

 Bonus — Write and read the first output file
report_text = (
    "Week 3 Lab Report\n"
    "Student count: 40\n"
    "Valid scores: 37\n"
    "Bad scores: 3\n"
    "Average valid score: 75.3\n"
    "Top student: Bonaventure Nkurunziza (95)\n"
)

with open("week3_report.txt", "w", encoding="utf-8") as f:
    f.write(report_text)

with open("week3_report.txt", "r", encoding="utf-8") as f:
    print(f.read())
