## Context

- A global logistics company wanted to build a new customer-facing
  application that would provide near real-time carbon emissions
  calculations for their shipped goods.
- The company had a manual workflow for calculating customer-specific
  carbon emissions, which took days or weeks to generate for each
  customer.
- The company wanted to build the new application using Elixir, but had
  only a small number of existing team members with Elixir experience.
- They had a large data warehouse from which the results could be
  calculated, but the data required considerable transformation, and was
  hosted in a system that could not be relied upon for customer-facing
  use at their scale.
- The carbon emissions calculation required data enrichment using
  unreliable 3rd-party APIs with very low resource constraints.

## Solution

- We helped to bootstrap the application and trained less-experienced
  team members in design patterns for application development with
  Elixir, Phoenix, and Live View.
- We architected and developed the application to build a normalized
  data cache over the data warehouse, with a focus on using data streams
  to reduce the memory requirements (and carbon impact) of our
  application.
- Using our normalized data cache, we built a concurrent data enrichment
  pipeline that could be re-configured on the fly to saturate but not
  overload the capacity of 3rd-party APIs.
- We developed highly-optimized PostgreSQL common table expressions
  (CTEs) to produce extremely fast carbon missions calculations over
  hundreds of millions of records without requiring further caching.

## Conclusion / Take aways

- Climate software is just software. Expertise in building data
  pipelines to handle large amounts of non-normalized data will be
  needed to monitor and tackle large-scale climate problems.
