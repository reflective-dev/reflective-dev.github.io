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

- Created a data pipeline that:
  - Accepted an arbitrary amount of new test result data at any time.
  - Stored all test results in a standard PostgreSQL database.
  - Made just-in-time decisions about which patients to make API
    requests for, based on the combined test result data for a given
    patient.
  - Made requests to the different API endpoints at different rates
    which were configurable in real time.
- Created a custom live dashboard showing the current status of all the
  parts of the pipeline and a UI for controlling the request frequency
  for each API endpoint.
- Ran the entire pipeline on a single cloud server that was monitored
  with standard monitoring and alerting mechanisms.

## Conclusion / Take aways

- Fine-grained rate limiting provided the best possible throughput
  without overhwelming the target APIs.
- Using real-time prioritization instead of a job queue allowed for the
  most actionable data to be delivered to epidemiologists first.
- Running the entire pipeline on a single cloud server greatly
  simplified deployment.
- Persisting both the data and the API request statuses resulted in a
  system that could easily recover from downtime.
