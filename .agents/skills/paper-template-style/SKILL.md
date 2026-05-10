---
name: paper-template-style
description: "Checks and enforces project hygiene and directory structure formatting."
---

# paper-template-style

## Purpose

To ensure the repository conforms to the standard paper template structure, checking for project hygiene, proper directory layouts, and correct file naming conventions.

## Canonical Template

The canonical template definition is the Spielman group Paper_Template repository:

- `https://github.com/spielman-group/Paper_Template`

Use that repository, together with its top-level `README.md`, as the normative reference for the manuscript package layout. Do not guess what the template is supposed to look like.

## When to Use This Skill

- You are starting a new paper from a template.
- You are importing an existing paper into the template workflow.
- You are preparing a manuscript for final submission and want to ensure no stray files or disorganized folders remain.

## Operating Rules

1. **Template Definition First**:
   - Compare the current repository against the canonical Paper_Template layout before reporting conformance.
   - At minimum, check for the expected top-level manuscript assets from the template: `Arxiv_documents/`, `Figure_source_files/`, `Notes/`, `PR materials/`, `References/`, `Submission_documents/`, `.gitignore`, `README.md`, `main.bib`, and `main.tex`.
   - Treat AI workflow additions such as `AGENTS/` and `.agents/` as allowed extras, not template violations.
2. **Hygiene Check**:
   - Verify that the required directories and files exist.
   - Ensure the bibliography file is properly located and that the manuscript points to the expected bibliography and figure locations.
   - Check for obvious repository-hygiene problems such as tracked junk files, machine-specific absolute paths in scripts, and figure/include paths that do not match the on-disk layout.
3. **Severity Classification**:
   - Classify findings as:
     - `error`: likely build-breaking or clearly nonconformant to the template.
     - `warning`: inconsistent with the template or harmful to reproducibility, but not immediately build-breaking.
     - `info`: stylistic or organizational notes.
4. **Refactoring**:
   - Safe, purely mechanical fixes may be applied automatically in non-interactive or test runs if they do not change scientific meaning.
   - Examples of safe fixes include correcting obviously broken path separators or case/underscore mismatches.
   - Moves, renames, or broader reorganization still require user approval unless the user explicitly asked for automatic cleanup.
5. **Reporting**:
   - Summarize deviations from the canonical template, state what reference you used, and list any actions taken to correct issues.
