# `RESULTS.md` Contract

## Manuscript Scope Discovery

1. Infer the active manuscript scope by scanning for likely LaTeX entrypoints.
2. Follow `\input`, `\include`, bibliography declarations, and figure/include references to infer supporting sources.
3. Treat the discovered manuscript sources, linked bibliography files, and directly referenced figure-generation sources as the relevant scope.
4. If one manuscript root is clearly primary, proceed.
5. If multiple plausible manuscript roots remain, ask the user which scope is active before document-level work.

## Meaning of `AGENTS/RESULTS.md`

1. `AGENTS/RESULTS.md` is provisional working memory: an extracted model of the manuscript, related discussion, and unresolved issues.
2. It may be stale, incomplete, or wrong.
3. It is advisory context, not ground truth.

## Trust States

- `current`: metadata matches the current commit and no discovered manuscript-scope changes make the summary obviously outdated
- `stale`: metadata mismatches or manuscript-scope changes likely affect the summary
- `missing`: no `AGENTS/RESULTS.md`

Use:
- `current`: advisory context for local decisions
- `stale`: background context only; do not use it to resolve paragraph-level disputes
- `missing`: if shared context matters, ask whether to refresh it via `colleague`

## Manuscript vs `RESULTS.md`

1. The manuscript is authoritative for what the draft currently says.
2. `RESULTS.md` never overrides the manuscript.
3. If the active text is in material scientific tension with `RESULTS.md`, do not steer the manuscript to restore alignment.
4. Instead, ask the user which is correct, or leave a bounded clarification comment and stop before changing scientific meaning.

Material tension includes disagreement about claim content, interpretation, mechanism, novelty framing, evidence strength, figure/table implications, or any other scientific meaning that changes how the draft should be read.

Non-material tension includes style, compression, paragraph flow, notation, or harmless summarization differences.

## Artifact Ownership

- `colleague` alone creates or updates `AGENTS/RESULTS.md`
- `coauthor` and `pi-revision` do not update `AGENTS/RESULTS.md`
- `pi-structure` writes `AGENTS/PI_STRUCTURE.md`
- `editor` writes `AGENTS/EDITOR.md`
- `reviewer` writes only blind-review artifacts
- `reviewer-misconceptions` writes `AGENTS/REFEREE_MISCONCEPTIONS_n.md`
