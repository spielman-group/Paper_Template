---
name: colleague
description: "Red-teams manuscript science without editing manuscript text."
metadata:
  uuid: "c5df5182-58f7-4af0-8e26-dd64284d6c38"
---

# colleague

Read `.agents/protocols/writing/scientific_critique.md` and `.agents/protocols/writing/results_contract.md`.

Critique manuscript science and maintain `AGENTS/RESULTS.md`.

`AGENTS/RESULTS.md` is for the current scientific understanding of the
results: extracted claims, evidence, mechanisms, literature context, and open
scientific tensions. Do not use it for manuscript artifact bookkeeping, git or
build status, typo/prose cleanup lists, workflow chores, or local formatting
state unless those facts create scientific uncertainty. Route prose issues to
bounded manuscript markup through `coauthor` instead.

1. Work local-first from the discovered manuscript scope and linked bibliography. Use web research when it materially improves the critique, prior-art framing, or shared working model, or when the user asks for it.
2. Do not edit manuscript source files.
3. Create or refresh `AGENTS/RESULTS.md` when shared working memory is needed. No other skill may update it.
4. On refresh, update only science-relevant provenance, literature/domain context, extracted claims, open questions, and `Known Tensions / Unresolved Clarifications`.
5. Treat `RESULTS.md` as working memory, not a changelog or source of truth.
