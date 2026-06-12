# Agent Workflow Guide

This project keeps agent instructions and agent-produced state separate.

## Layers

1. `AGENTS.md`: compact constitutional rules for any agent working in the repo.
2. `.agents/protocols/`: shared normative rules used by multiple skills.
3. `.agents/skills/`: role-specific instructions.
4. `AGENTS/`: visible state and reports produced by the skills.

## `RESULTS.md`

`AGENTS/RESULTS.md` is provisional working memory, not scientific truth. It records an agent's extracted understanding of the manuscript, relevant literature, related discussion, and unresolved tensions. Literature-derived context is a normal and expected part of this file, especially after `colleague` performs prior-art checking or literature search. It may be stale, incomplete, or wrong. When it materially conflicts with the manuscript, agents should surface the tension and ask the user rather than silently force alignment.

## Workflow Graph

- `colleague` -> `AGENTS/RESULTS.md`
- `coauthor` / `pi-structure` / `pi-revision` consume `AGENTS/RESULTS.md` as advisory context
- `reviewer` -> numbered review-round artifacts such as `AGENTS/REFEREE_REPORT_1.md` + `AGENTS/REFEREE_RESULTS_1.md`
- `reviewer-misconceptions` -> numbered review-round artifacts such as `AGENTS/REFEREE_MISCONCEPTIONS_1.md`
- `editor` -> `AGENTS/EDITOR.md`

## Artifact Map

- `AGENTS/RESULTS.md`: extracted working model of the manuscript and open tensions
- `AGENTS/PI_STRUCTURE.md`: structural critique
- `AGENTS/EDITOR.md`: editorial decision memo
- `AGENTS/REFEREE_REPORT_1.md`, `AGENTS/REFEREE_REPORT_2.md`, ...: blind referee reports for successive review rounds
- `AGENTS/REFEREE_RESULTS_1.md`, `AGENTS/REFEREE_RESULTS_2.md`, ...: blind reviewers' extracted understanding for successive review rounds
- `AGENTS/REFEREE_MISCONCEPTIONS_1.md`, `AGENTS/REFEREE_MISCONCEPTIONS_2.md`, ...: comparison between blind understanding and `RESULTS.md` for successive review rounds
