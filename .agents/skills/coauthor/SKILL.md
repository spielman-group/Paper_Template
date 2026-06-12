---
name: coauthor
description: "Marks up bounded manuscript regions with comments and replacements."
---

# coauthor

Read `.agents/protocols/scientific_critique.md`, `.agents/protocols/results_contract.md`, and `.agents/protocols/latex_markup.md`.

Mark up one bounded manuscript region at a time.

1. Select one local target. Prefer a literal `% AGENT HERE` marker; if multiple markers exist and the user did not choose one, ask. Otherwise use the user-named section or paragraph.
2. Use `AGENTS/RESULTS.md` only as advisory context. If it is missing and shared context matters, ask whether to refresh it via `colleague`.
3. If the target is in material scientific tension with `AGENTS/RESULTS.md`, ask which source is correct, or leave a bounded `\edit[]{...}` clarification comment and stop before changing meaning.
4. Use `\edit` only. Keep markup local, sparse, and reviewable.
5. Do not expand into large unrequested rewrites. Do not update `AGENTS/RESULTS.md`.
