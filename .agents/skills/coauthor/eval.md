# coauthor eval

Check the proposed manuscript markup before the main agent finishes.

Report each item as pass/fail with a one-sentence reason. Do not edit files.

1. The edit target is bounded to the requested marker, paragraph, caption, or section.
2. Every `\edit[old]{new}` preserves unchanged surrounding text outside the macro.
3. Any sentence- or paragraph-scale `\edit` block is necessary because the whole sentence or paragraph was genuinely rewritten end to end.
4. Large edit blocks that contain mostly unchanged text are flagged as decomposable.
5. A commented `AGENT BASELINE` block is present during evaluation and is used as the starting-paragraph reference.
6. Existing author edit macros are treated as accepted draft text for purposes of evaluating the revised prose, but they are not protected from further revision.
7. New `old` arguments refer to the pre-edit baseline inferred from existing edit macros, not to already-proposed output text.
8. Scientific changes are either explicitly supported by local manuscript/figure evidence or left as bounded `\agent{...}` comments.
9. Questions, concerns, clarification requests, optional suggestions, and structural notes use `\agent{...}`, not `\edit` with an empty old argument.
10. Any `% AGENT HERE` marker present at handoff is preserved exactly.
11. The markup is sparse enough for the author to review in one pass.
