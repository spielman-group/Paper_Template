# LaTeX Markup Protocol

Use two distinct markup channels: `\edit` for proposed text changes and `\agent` for agent comments.

- `\edit[old]{new}` for replacements
- `\edit{new}` for inserted replacement text with no reliable local `old` argument
- `\agent{comment}` for questions, concerns, clarification requests, and structural notes

Do not put comments, questions, reviewer-style concerns, or "you might want to think about..." notes inside `\edit`. That macro is for changes to the manuscript text. Comments belong in `\agent` so the author can distinguish proposed prose from unresolved discussion.

If `\edit` or `\agent` is missing, define the missing macro near the local edit macros before using it. Match the style of the author's comment macros, for example:

```tex
\newcommand{\agent}[1]{{\color{cyan}[Agent: #1]}}
```

## Markup Rules

1. Always keep edits local and granular. Preserve unchanged surrounding text outside `\edit`; do not wrap mostly unchanged text in one sentence- or paragraph-scale edit. Sentence- or paragraph-scale `\edit` blocks are allowed only when that whole sentence or paragraph is genuinely rewritten end to end and cannot be decomposed into reviewable phrase-level changes.
2. Use `\agent` comments instead of stronger rewrite when the issue is uncertainty, unsupported meaning, or unresolved tension.
3. When existing edit macros are present, read the paragraph as if the proposed outputs have been accepted. Existing edits are part of the working draft, not protected text.
4. A later agent revision may change text that is already inside an edit macro. When it does, the new `old` argument must refer to the text before any edits, using the existing bracketed `old` arguments as the evidence for that baseline.
5. Do not normalize another author's macros unless revising inside that marked region.
6. For inserted text from an existing macro, do not invent an `old` argument.
7. For moves, use paired `\agent` comments such as `Move A` / `Destination A`; do not duplicate the moved prose.
8. Keep markup sparse enough for a scientist to review in one pass.
9. The scientist resolves markup before the next major workflow step.

## Granular Markup Examples

Yes:

```tex
\textit{Distribution functions}---\edit[Moving]{To go} beyond \edit{the} average properties, we \edit[study]{extract} \edit[the]{full} probability distribution \edit{function} (PDF) $P_k \equiv P(h_k)$ of ripplon amplitudes \edit[$h_k$]{using ensembles of about $70$ experimental realizations}.
```

No:

```tex
\edit[\textit{Distribution functions}---Moving beyond the averaged properties, we study the probability distribution $P_k \equiv P(h_k)$ of ripplon amplitudes $h_k$.]{\textit{Distribution functions}---To go beyond average properties, we extract the full probability distribution function (PDF) $P_k \equiv P(h_k)$ of ripplon amplitudes using ensembles of about $70$ experimental realizations.}
```

The "No" example hides unchanged text inside the edit block and makes the scientist review a large replacement when only local words changed.
