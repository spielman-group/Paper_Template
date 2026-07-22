---
name: pi-revision
description: "Runs a whole-document or scoped manuscript markup review."
metadata:
  uuid: "378d5ae1-5938-4389-9f36-b473decd6ab4"
---

# pi-revision

Read `.agents/protocols/writing/scientific_critique.md`, `.agents/protocols/writing/results_contract.md`, and `.agents/protocols/writing/latex_markup.md`.

Run a full-draft or bounded-scope markup review.

1. Use the user-requested scope. If the task is whole-document and `AGENTS/PI_STRUCTURE.md` exists, read it first as advisory critique.
2. Use `AGENTS/RESULTS.md` only as advisory context. If it is missing and shared context matters, ask whether to refresh it via `colleague`.
3. If the active text is in material scientific tension with `AGENTS/RESULTS.md`, do not steer the manuscript toward it. Ask the user which is correct, or leave a bounded `\agent{...}` clarification comment and stop before changing scientific meaning.
4. Use `\edit` for text changes and `\agent` for comments. Keep the pass representative and reviewable.
5. Do not update `AGENTS/RESULTS.md`.
