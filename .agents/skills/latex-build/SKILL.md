---
name: latex-build
description: "Compiles the LaTeX document to ensure reproducibility and checks for common errors."
---

# latex-build

## Purpose

To compile the LaTeX manuscript and ensure the document builds successfully without critical errors or missing references.

## When to Use This Skill

- You need to verify that recent edits have not broken the LaTeX build.
- You are preparing the final PDF for review or submission.

## Operating Rules

1. **Compilation**:
   - Execute the appropriate build commands (e.g., `latexmk`, `pdflatex`, and `bibtex`) to compile `main.tex`.
   - If `latexmk` is unreliable in the current checkout, fall back to the manual sequence:
     1. `bibtex main`
     2. `pdflatex main.tex`
     3. `pdflatex main.tex`
   - Run sequential passes, not parallel LaTeX passes.
2. **Error Checking**:
   - Parse the build logs for `Overfull \hbox`, missing citations, undefined references, or fatal compilation errors.
   - Distinguish among:
     - `clean build`: compilation succeeds without important warnings.
     - `warning build`: compilation succeeds, but warnings remain.
     - `blocked build`: compilation fails or produces unusable output.
3. **Reporting**:
   - Provide a clear summary of the build status.
   - If the build fails, pinpoint the exact line in `.tex` causing the issue and propose a fix.
   - If the build succeeds only after a narrow mechanical workaround that does not alter scientific meaning, report that workaround explicitly.
