---
name: reviewer-misconceptions
description: "Compares a blind reviewer's understanding against the manuscript working model."
---

# reviewer-misconceptions

Read `.agents/protocols/results_contract.md`.

Compare a blind reviewer's extracted understanding against `AGENTS/RESULTS.md`.

1. Use the latest matching referee artifacts unless the user specifies a review round.
2. If `AGENTS/RESULTS.md` is missing, stop and ask whether to refresh it via `colleague`.
3. If `AGENTS/RESULTS.md` is stale, note that the comparison may mix reviewer misunderstanding with stale agent memory.
4. Write `AGENTS/REFEREE_MISCONCEPTIONS_n.md`.
