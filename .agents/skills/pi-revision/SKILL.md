---
name: pi-revision
description: "Runs a whole-document or scoped manuscript markup review."
---

# pi-revision

Read `.agents/protocols/scientific_critique.md`, `.agents/protocols/results_contract.md`, and `.agents/protocols/latex_markup.md`.

Run a full-draft or bounded-scope markup review.

1. Use the user-requested scope. If the task is whole-document and `AGENTS/PI_STRUCTURE.md` exists, read it first as advisory critique.
2. Use `AGENTS/RESULTS.md` only as advisory context. If it is missing and shared context matters, ask whether to refresh it via `colleague`.
3. If the active text is in material scientific tension with `AGENTS/RESULTS.md`, do not steer the manuscript toward it. Ask the user which is correct, or leave a bounded `\edit[]{...}` clarification comment and stop before changing scientific meaning.
4. Use `\edit` markup only. Keep the pass representative and reviewable.
5. Do not update `AGENTS/RESULTS.md`.
