---
name: pi-structure
description: "Non-interactively reads the entire paper to describe the scientific argument and check alignment with RESULTS.md."
---

# pi-structure

## Purpose

To play the role of a Principal Investigator reviewing a draft from a junior colleague. This agent reads the paper end-to-end and attempts to reconstruct and describe the scientific argument paragraph-by-paragraph to ensure logical flow and structural integrity.

## When to Use This Skill

- You have a complete or mostly complete draft.
- You want a high-level structural review of the argument's flow.
- You need to verify if the manuscript actually aligns with the intended claims.

## Operating Rules

1. **Dependency Check**: 
   - You must read `AGENTS/RESULTS.md` before starting.
   - If it does not exist, pause and ask the user if you should spawn a subagent to generate it via the `colleague` skill.
2. **Non-Interactive Review**:
   - Do not ask the user questions during the reading phase. Read the document from end to end autonomously.
3. **Output Generation**:
   - Generate a markdown file at `AGENTS/PI_STRUCTURE.md`.
   - The file should contain a paragraph-by-paragraph breakdown of the scientific argument, or a concise section-by-section breakdown if that is sufficient to surface the main structural problems.
   - Call out specific places where the paper is misaligned with the claims in `AGENTS/RESULTS.md`.
   - Propose structural revisions, additions, or deletions of content.
   - In non-interactive or test mode, prefer timely delivery of the main structural misalignments over exhaustive commentary.
4. **No Direct Edits**:
   - Do not modify the `.tex` files. Only produce the `PI_STRUCTURE.md` report.
