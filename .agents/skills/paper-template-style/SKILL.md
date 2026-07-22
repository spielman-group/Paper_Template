---
name: paper-template-style
description: "Checks a manuscript repository for layout and reproducibility hygiene problems."
metadata:
  uuid: "100a2827-1b1f-4308-80ae-35a6b8e8916c"
---

# paper-template-style

Read `.agents/protocols/writing/results_contract.md` for manuscript-scope discovery.

Check the repository for generic manuscript-package hygiene problems.

1. Use the active manuscript scope to infer which source files, bibliography files, figure paths, and build artifacts matter.
2. Check for path mismatches, machine-specific absolute paths, tracked junk, broken include chains, and bibliography/figure references that do not match the on-disk layout.
3. Classify findings as `error`, `warning`, or `info`.
4. Safe mechanical fixes are allowed only when they do not change scientific meaning and the user asked for cleanup; otherwise report the issue only.
