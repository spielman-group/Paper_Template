---
name: latex-build
description: "Builds a LaTeX manuscript and reports warnings or failures."
metadata:
  uuid: "6562258b-681d-4c1f-8e0e-fcb66ae7ad92"
---

# latex-build

Read `.agents/protocols/writing/results_contract.md` for manuscript-scope discovery.

Build the active manuscript and report whether it is clean, warning-only, or blocked.

1. Build the active manuscript entrypoint. If multiple plausible entrypoints remain, ask the user which one to compile.
2. Prefer `latexmk`. If manual passes are needed, use:
   1. `pdflatex <entrypoint>`
   2. `bibtex <basename>`
   3. `pdflatex <entrypoint>`
   4. `pdflatex <entrypoint>`
3. Parse build logs for fatal errors, undefined references, missing citations, and important warnings such as overfull boxes.
4. Report the build status and the narrowest actionable fix when blocked.
