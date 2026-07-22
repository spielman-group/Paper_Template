---
name: reviewer
description: "Simulates a blind peer review of a manuscript."
metadata:
  uuid: "a2a7622f-48b9-45c7-8fd2-283cff3548f9"
---

# reviewer

Read `.agents/protocols/writing/results_contract.md` only for manuscript-scope discovery. Do not read `AGENTS/RESULTS.md` or any other agent-generated state file.

Produce a blind referee report and a blind reviewer's extracted understanding of the manuscript.

1. Read only manuscript-derived materials within the active manuscript scope.
2. Use web search only when a specific prior-art question materially affects the review.
3. Write:
   - `AGENTS/REFEREE_REPORT_n.md`
   - `AGENTS/REFEREE_RESULTS_n.md`
4. Do not run misconception analysis. That belongs to `reviewer-misconceptions`.
