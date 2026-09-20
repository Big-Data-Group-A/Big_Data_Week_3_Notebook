# Part 6 · Reflection

**1. At what percentage of broken records would you stop trusting the dataset, and what would you do instead of skipping?**

Three out of forty broken records (7.5 percent) is still manageable to skip and report on, since the vast majority of the data remains reliable. Once the broken-record rate climbed toward somewhere around 15 to 20 percent, I would stop simply skipping bad rows and instead treat it as a data quality problem: go back to whoever produced the file, check whether there was a systematic issue in how the scores were entered or exported, and consider re-collecting or manually verifying the affected records rather than silently excluding a meaningful chunk of the class from the analysis.

**2. Describe one thing from today's session that surprised or confused you.**

It was interesting to see how a single non-numeric value like the word "absent" can silently break an entire pipeline if there is no `try/except` around the conversion, yet a small addition of error handling lets the program keep running smoothly and even report exactly which records caused the problem.
