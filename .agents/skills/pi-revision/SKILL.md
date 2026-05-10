---
name: pi-revision
description: "Marks up the paper from beginning to end using LaTeX macros based on the user's desired level of detail."
---

# pi-revision

## Purpose

To act as a Principal Investigator who has accepted the high-level structure of the paper and is now performing a detailed, end-to-end line edit of the manuscript. 

## When to Use This Skill

- The structural review (`pi-structure`) is complete and accepted.
- You want a comprehensive copyedit and scientific review of the entire document.

## Operating Rules

1. **Dependency Check**: 
   - Read `AGENTS/RESULTS.md` to establish context. 
   - If missing, offer to spawn a subagent to run the `colleague` skill.
2. **Detail Level Selection**:
   - In interactive mode, ask the user to specify the desired level of detail before modifying files.
   - Example prompt: "Should I suggest new text directly using the `\agentedit` macro, or should I restrict myself to high-level commentary using the `\agent` macro?"
   - In non-interactive or automated test mode, default to a mixed mode: use `\agentedit` for concrete wording improvements and `\agent` for framing, evidence, or unresolved-claim issues.
3. **Target Selection (`% AGENT HERE`)**:
   - In interactive mode, if the user inserts `% AGENT HERE`, prefer the marked local region over a whole-document pass.
   - A marker applies to the next paragraph, caption, list, equation block, or local LaTeX block that follows it.
   - If multiple markers are present and the user did not specify which one to use, ask before proceeding.
   - If no marker is present, follow the user's requested scope. Full-document review remains allowed when explicitly requested.
4. **Execution**:
   - Once the review mode is established, read the manuscript end-to-end or within the requested target scope.
   - Insert macros (`\agentedit` and/or `\agent`) directly into the `.tex` files according to the agreed-upon rules.
   - Keep markup representative and sparse enough that the scientist can realistically review it.
   - Preserve the author's voice and do not alter the core scientific results (unless explicitly requested).
5. **Scientist Resolution Step**:
   - After the markup pass, the scientist should accept, reject, or revise the inserted `\agentedit` / `\agent` suggestions and remove them before the next major workflow step.
6. **State Maintenance**:
   - If the review materially changes the intended scientific narrative, update `AGENTS/RESULTS.md` and refresh its git-commit metadata block.
