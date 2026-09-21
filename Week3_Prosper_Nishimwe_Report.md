# Week 3 Lab — Short Report

**Student:** Prosper NISHIMWE
**Student ID:** 28926

## Resilient Pipeline

The dataset contains 40 student records. During the analysis, 3 records had broken or non-numeric scores:

* AUCA008 — Emmanuel Nsengiyumva: `N/A`
* AUCA020 — Samuel Rukundo: blank score
* AUCA032 — Gilbert Uwituze: `absent`

Therefore, 37 scores were valid and 3 were invalid. The average of the valid scores was **77.8**.

The program handled the broken records using `try` and `except ValueError`. When a score could not be converted to an integer, the program caught the error, recorded the student ID in `bad_ids`, and continued processing the remaining records instead of stopping.

The highest valid score was **95**, achieved by **Bonaventure Nkurunziza**, who received grade **A**.



