---
name: coauthor
description: "Marks up bounded manuscript regions with proposed text edits and agent comments, especially around `% AGENT HERE` drafting markers."
metadata:
  uuid: "f2f5a1cf-532d-475c-a433-0c4e2ff28137"
---

# coauthor

Read `.agents/protocols/writing/scientific_critique.md`, `.agents/protocols/writing/results_contract.md`, and `.agents/protocols/writing/latex_markup.md`.

Mark up one bounded manuscript region at a time.

1. Select one local target. Prefer a literal `% AGENT HERE` marker; if multiple markers exist and the user did not choose one, ask. Otherwise use the user-named section or paragraph.
2. Use `AGENTS/RESULTS.md` only as advisory context. If it is missing and shared context matters, ask whether to refresh it via `colleague`.
3. If the target is in material scientific tension with `AGENTS/RESULTS.md`, ask which source is correct, or leave a bounded `\agent{...}` clarification comment and stop before changing meaning.
4. Use `\edit` for text changes and `\agent` for comments. Keep markup local, sparse, and reviewable.
5. Do not expand into large unrequested rewrites. Do not update `AGENTS/RESULTS.md`.

## Drafting-marker workflow

The usual coauthor workflow is that the human has already revised one paragraph, inserted local `\edit` markup, and marked the handoff point with `% AGENT HERE`.

- Before changing the live paragraph, copy the starting paragraph into a commented baseline block immediately above it. Prefix every copied line with `%` and use this exact wrapper:

```tex
% AGENT BASELINE START
% <starting paragraph copied here exactly as found>
% AGENT BASELINE END
```

- Keep the commented baseline unchanged while revising and while running the eval loop. It gives both the main agent and the checker a durable reference for the paragraph state at handoff.
- Read the live paragraph as if existing human `\edit`, `\ibsedit`, and similar edit macros have been accepted. Their output text is the current draft for purposes of flow, grammar, and further revision.
- Existing edit macros are not special or protected. Preserve them when possible for reviewability, but revise inside or across them when the better local edit requires it.
- When adding or revising a prose change, the `old` argument in `\edit[old]{new}` must reflect the text before any edit macros were applied. Use the existing bracketed `old` arguments in the commented baseline and live paragraph to reconstruct that pre-edit text. Use `\edit{new}` only for a pure insertion or when the old argument would be invented.
- When adding a question, concern, uncertainty, structural note, or optional suggestion, use `\agent{...}`. Do not encode non-text comments as `\edit[]{...}`.
- Preserve the `% AGENT HERE` marker exactly. It is the user's durable handoff marker, not a completion checklist item.
- Remove the commented baseline block only after the eval loop has passed. If an unresolved issue remains, represent it as an author-facing `\agent{...}` comment, rerun the eval check, and remove the baseline only after that check passes.

## Process

Before finishing, run the coauthor eval loop with the commented baseline still present:

1. Read `.agents/skills/coauthor/eval.md`.
2. When subagents are available, spin up a separate clean-context checker to evaluate the proposed markup against `eval.md`. The checker must not edit files; it only reports which evals pass or fail and why.
3. If a checker is unavailable, perform the same eval yourself and say that no independent checker was run.
4. If any eval fails, revise the markup and repeat the eval loop until all checks pass.
5. After the eval loop passes, remove the commented baseline block before finishing.
