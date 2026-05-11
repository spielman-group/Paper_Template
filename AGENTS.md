# AGENTS

## Purpose
This file defines the mandatory operating rules and invariants for any automated assistant interacting with this repository.

This repository is a **scientific manuscript**:
1) A LaTeX document (the paper).
2) Julia and Python scripts used to generate figures/tables and other artifacts included in the paper.

The priority is **correctness, reproducibility, and preserving scientific meaning**.

---

## Core Principles
1) **Safety over throughput.** If the request risks changing scientific meaning or results without explicit approval, stop and ask for direction or constrain the change to comments/suggestions.
2) **Reproducibility first.** Prefer changes that make builds and figure generation deterministic and documented.
3) **No silent scientific drift.** Do not introduce new scientific claims, change analysis logic, or change figure outputs unless the user explicitly requests it.
4) **Be explicit about uncertainty.** If you did not run something, say so; do not guess about outputs.

---

## Allowed Actions
1) **Use predefined skills** (see Skill Directory below).
2) **Edit LaTeX sources** using the `coauthor` or `pi-revision` skills via macros (`\agentedit` and `\agent`).
3) **Create/modify scripts** for figures with result-preservation guardrails.
4) **Add/update build instructions** to improve reproducibility.
5) **Refactor code** if it does not change computed results.

## Prohibited Actions
1) **Do not introduce new scientific claims** without marking them as proposed.
2) **Do not change figure/table results** without explicit approval.
3) **Do not fabricate citations.**
4) **Do not rewrite prose;** you are a discussion partner, not an author. 

---

## Result Integrity Rules (Julia/Python)
When touching analysis or figure-generation code:
1) Default assumption: **outputs must remain identical**.
2) Prefer “refactor-only” changes (variable renames, dead code removal).
3) If a change could alter results, explain why, propose a test, and wait for explicit approval.

---

## Skill Directory

The detailed workflows for interacting with this manuscript have been modularized into skills. You should invoke these skills based on the user's current need:

* **`colleague`**: For brainstorming and scientific feedback without editing LaTeX. Generates `AGENTS/RESULTS.md`.
* **`coauthor`**: For real-time writing assistance, paragraph-by-paragraph, using LaTeX markup macros. Requires `AGENTS/RESULTS.md`.
* **`pi-structure`**: For a non-interactive, end-to-end structural review of the manuscript's arguments, in the way a senior author would when provided a draft for the first time.  PI stands for Principal Investigator.
* **`pi-revision`**: For an end-to-end copyedit and markup pass using LaTeX macros.
* **`editor`**: To simulate an editorial decision based on the manuscript and cover letter.
* **`reviewer`**: To simulate a blind peer review and generate a referee report.

Supporting skills:

* **`bibliography`**: To clean the BibTeX file, add references, and validate existing citations.
* **`paper-template-style`**: For project hygiene and directory structure formatting.
* **`latex-build`**: To compile the manuscript and check for errors.
