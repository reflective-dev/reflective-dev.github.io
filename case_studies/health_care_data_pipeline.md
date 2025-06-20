## Context

- The department of health for a large US state wanted to run
  comorbidity analysis across 2 years of COVID-19 test results.
- HIPAA-protected patient records were distributed across multiple
  Health Information Exchanges (HIEs).
- Each HIE API had different, low resource limits. The records that were
  of most interest to epidemiologists were also the most problematic in
  terms of size, and length of time to compile and access in the HIEs.
  - Some API requests would take more than 10 minutes to complete.
- Test results had specific markers indicating were more relevant to
  comorbidity analysis. Tests performed in a hospital setting might
  indicate a worse case of COVID, for instance.
- New test results were available every day, and thus would change the
  priority of the backlog.

## Solution

## Conclusion / Take aways
