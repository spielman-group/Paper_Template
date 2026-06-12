# LaTeX Markup Protocol

Use `\edit` only.

- `\edit[old]{new}` for replacements
- `\edit[]{comment}` for questions, concerns, clarification requests, and structural notes

If `\edit` is missing, define it near the local edit macros before using it.

## Markup Rules

1. Keep edits local and granular; do not wrap mostly unchanged text in one large edit.
2. Use comments instead of stronger rewrite when the issue is uncertainty, unsupported meaning, or unresolved tension.
3. When existing edit macros are present, treat the accepted prose as the macro output, but any new `old` text must refer to the pre-edit baseline.
4. Do not normalize another author's macros unless revising inside that marked region.
5. For inserted text from an existing macro, do not invent an `old` argument.
6. For moves, use paired comments such as `Move A` / `Destination A`; do not duplicate the moved prose.
7. Keep markup sparse enough for a scientist to review in one pass.
8. The scientist resolves markup before the next major workflow step.
