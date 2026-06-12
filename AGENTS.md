# AGENTS

## Purpose

This repository is a scientific manuscript package. The workflow priority is correctness, reproducibility, and preserving scientific meaning.

## Core Rules

1. Safety over throughput. If a requested change could alter scientific claims, analysis logic, figures, tables, or computed results, ask for direction or constrain the work to comments.
2. Reproducibility first. Prefer local evidence, deterministic build steps, and explicitly stated assumptions.
3. No silent scientific drift. Do not introduce new claims, strengthen conclusions, or reinterpret results without making that status explicit.
4. Be explicit about uncertainty. If you did not run something or cannot verify a point, say so.
5. Prose rewrites are allowed only through the manuscript-markup workflow (`coauthor` or `pi-revision`).

## `RESULTS.md` Contract

1. `AGENTS/RESULTS.md` is provisional working memory: the agent's extracted understanding of the manuscript, relevant literature, related discussion, and unresolved issues.
2. It may be stale, incomplete, or wrong.
3. It coordinates agents; it does not outrank the manuscript draft.
4. When the manuscript and `RESULTS.md` are in material scientific tension, ask the user which is correct before changing meaning.
5. Only the `colleague` skill may create or update `AGENTS/RESULTS.md`.

## Skill Directory

- `colleague`: Scientific red-team discussion and maintenance of `AGENTS/RESULTS.md`.
- `coauthor`: Bounded manuscript markup using `\edit` comments and replacements.
- `pi-structure`: End-to-end structural critique of the manuscript.
- `pi-revision`: End-to-end manuscript markup review.
- `editor`: Desk-review style editorial assessment against a target journal.
- `reviewer`: Blind referee report derived from the manuscript only; writes numbered review-round artifacts such as `AGENTS/REFEREE_REPORT_1.md` and `AGENTS/REFEREE_RESULTS_1.md`.
- `reviewer-misconceptions`: Comparison of blind-review understanding against `AGENTS/RESULTS.md`; writes numbered review-round artifacts such as `AGENTS/REFEREE_MISCONCEPTIONS_1.md`.
- `bibliography`: Bibliography cleaning, citation validation, and reference addition.
- `paper-template-style`: Generic manuscript-package hygiene and layout checks.
- `latex-build`: LaTeX build verification for the active manuscript scope.
