---
name: pi-structure
description: "Reviews a manuscript end-to-end for structure, argument flow, and clarification points."
metadata:
  uuid: "9e8cfef9-1109-4340-9b74-857bf6e27778"
---

# pi-structure

Read `.agents/protocols/writing/scientific_critique.md` and `.agents/protocols/writing/results_contract.md`.

Review the active manuscript scope end-to-end and describe the scientific argument it makes.

1. Read the manuscript autonomously once the scope is clear. If multiple manuscript roots are plausible, ask the user which one is active.
2. Use `AGENTS/RESULTS.md` only as advisory context. If it is missing, continue with a manuscript-only structural review and note that limitation.
3. Write `AGENTS/PI_STRUCTURE.md` with three sections:
   - internal structural weaknesses in the draft
   - tensions between the draft and `AGENTS/RESULTS.md`
   - author clarification points
4. Do not edit manuscript source.
