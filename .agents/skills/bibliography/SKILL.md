---
name: bibliography
description: "Cleans the BibTeX file, adds new references, and validates existing citations."
---

# bibliography

## Purpose

To manage, clean, and validate the project's BibTeX files. This skill can fetch new references from the web, standardize citation keys, and ensure that the `.bib` file remains perfectly synchronized with the `.tex` files that depend on it.

## When to Use This Skill

- You want to add a new reference (via DOI, ArXiv ID, or description).
- You want to perform a "Full Clean" of your bibliography to standardize keys and remove unused references.
- You want to validate that all `\cite{}` commands in your manuscript correspond to existing `.bib` entries.

## Operating Rules

1. **Initial Interaction**:
   - Always ask the user what mode they want: "Add a reference" or "Full Clean", unless the mode was already specified by the user or the skill is being run non-interactively for a test.
   - Do the minimum work necessary unless a Full Clean is explicitly requested.
   
2. **Adding References**:
   - Use web search tools to resolve DOIs, ArXiv IDs, or plaintext descriptions into valid BibTeX entries.
   - If a request is ambiguous, present the found paper and ask for confirmation before writing to the `.bib` file.
   - **Key Standardization**: Format all new citation keys as `[FirstAuthorLastName][Year][abc]` (e.g., `Spielman2025`, and if a collision occurs, `Spielman2025a`, `Spielman2025b`).
   - Check for existing collisions before appending to the `.bib` file.
   - If a standardized key would require transliteration, invented metadata, or other ambiguous judgment, prefer reporting the ambiguity or preserving the existing key over forcing a rename.

3. **Full Clean Validation**:
   - Prefer a local-first pass: parsing `.tex` and `.bib` files is sufficient for validation and key synchronization. Web lookup is optional unless the user explicitly requests metadata verification or new references are being added.
   - **Key Standardization**: Reformat all existing keys in the `.bib` file to match the `[FirstAuthorLastName][Year][abc]` standard.
   - If a rename would require nontrivial transliteration or judgment, do not force it silently; report the ambiguity.
   - **Targeted Replace**: If an existing key is changed, you must perform a find-and-replace to update the `\cite{...}` commands. **CRITICAL**: Only apply this find-and-replace to `.tex` files that explicitly reference the specific `.bib` file being cleaned (e.g., files containing `\bibliography{main}`). Do not touch `.tex` files in other directories (like `Arxiv_documents/`) if they rely on a different `.bib` file.
   - **Orphan Pruning**: Parse the relevant `.tex` files for `\cite{}` keys. Identify any references in the `.bib` file that are never used.
   - In non-interactive or test runs, report orphaned entries but do not delete them unless the user explicitly requested deletion.
   - In interactive runs, ask the user before deleting orphaned entries.
   - **Missing Citations**: Flag any `\cite{}` keys in the `.tex` file that do not exist in the `.bib` file.
4. **Minimum Acceptable Completion**:
   - A valid Full Clean pass may stop after:
     - synchronizing safe key renames,
     - confirming that cited keys resolve,
     - and reporting orphaned or ambiguous entries.
   - Do not stall the task in pursuit of optional metadata polishing.
