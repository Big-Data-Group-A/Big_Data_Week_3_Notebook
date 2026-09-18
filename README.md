

PART 6 Reflection

*1. 3/40 = 7.5% bad is okay to skip* (Ex 5.1). We used `try/except` and got `valid=37`.

I would stop trusting at *15-20% bad*. Then skipping changes results: Ex 5.2 passed/failed counts become wrong, and Ex 5.3 district averages become unfair because some districts would have 3 students and others 5.

I would stop if I got stuck, save `bad_ids`, check why `parts[7]` is broken, fix the CSV, then re-run from Ex 4.2. Don't write `week3_report.txt` yet.

I was Surprised on Ex 5.3 needing two dicts `sums` and `counts` with `.get(d,0)` instead of just a list like in Ex 4.2. Confusing at first, but it's needed to get average per district.