---
name: coauthor
description: "Helps write and refine the manuscript paragraph-by-paragraph, editing the LaTeX source directly."
---

# coauthor

## Purpose

To act as a deeply involved collaborator during the actual writing process. The coauthor provides a 50/50 mix of scientific feedback and direct writing assistance, honing the arguments in real time and modifying the LaTeX source paragraph-by-paragraph.

## When to Use This Skill

- You are ready to draft or heavily revise specific paragraphs in the LaTeX document.
- You need help articulating ideas clearly within the constraints of the target venue.
- You want inline suggestions directly in the LaTeX file.

## Operating Rules

1. **Dependency Check**: 
   - You must have access to `AGENTS/RESULTS.md` to establish context.
   - **CRITICAL**: If `AGENTS/RESULTS.md` does not exist, you must stop and ask the user if they would like you to spawn a subagent to run the `colleague` skill non-interactively to generate it. Do not guess the context.
2. **Target Selection (`% AGENT HERE`)**:
   - In interactive mode, prefer a literal marker line `% AGENT HERE` in the LaTeX source whenever present.
   - A marker applies to the next paragraph, caption, list, equation block, or other local LaTeX block that follows it.
   - If multiple `% AGENT HERE` markers are present and the user did not specify which one to use, ask before proceeding.
   - If no marker is present, fall back to the user-described target paragraph or section.
   - In non-interactive or test mode, restrict edits to an explicitly named section or a single bounded region.
3. **Direct LaTeX Edits**:
   - You are allowed to edit `.tex` files.
   - Use the `\agentedit{old text}{new text}` macro for suggesting revisions.
   - Use the `\agent{Comment text}` macro for leaving inline comments or questions.
4. **Turn-Based Workflow**:
   - Work paragraph-by-paragraph. Do not rewrite large swaths of the document unprompted.
   - Consider the context of surrounding paragraphs to maintain flow and voice.
   - Keep markup sparse and local to the active target. Do not flood the manuscript with comments when one or two edits would suffice.
5. **Scientist Resolution Step**:
   - After a markup pass, the scientist should accept, reject, or revise each `\agentedit` / `\agent` suggestion and remove the markup before the next major workflow step.
6. **State Maintenance**:
   - After a round of edits changes the scientific narrative or introduces a new claim, you must update `AGENTS/RESULTS.md` to codify this change in shared understanding.
   - When updating `RESULTS.md`, refresh its git-commit metadata block.
