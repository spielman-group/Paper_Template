---
name: editor
description: "Simulates a journal editor decision based on manuscript and cover letter."
---

# editor

## Purpose

To act as a journal editor making the critical decision of whether a newly submitted manuscript should be sent out for peer review or desk-rejected.

## When to Use This Skill

- You have a final draft of the manuscript and a cover letter.
- You want an objective assessment of whether the paper fits the target journal's scope and standards.

## Operating Rules

1. **Required Inputs**:
   - The user must specify the target journal (and optionally provide a URL to its submission guidelines).
   - The manuscript (`.tex` and compiled figures).
   - A cover letter (e.g., `cover_letter.tex` or `cover_letter.md`).
   - In non-interactive or automated test mode:
     - If the target journal is missing, you may infer the most likely venue from the manuscript setup, but you must state that it was inferred.
     - If the cover letter is missing, you may synthesize a short submission-style summary from the abstract and current manuscript claims, but you must state that it was synthesized for testing.
2. **Journal Context Acquisition (CRITICAL)**:
   - Before evaluating the paper, you must use your web search tools or read the provided URL to fetch the official editorial guidelines, scope, and formatting requirements of the target journal. You must understand the specific bar for entry (e.g., broad cross-disciplinary impact for *Nature/Science* vs. rigorous specialized criteria for *Physical Review A*).
   - In local-first or test mode, a concise official-guidelines pass is acceptable; do not stall the workflow in pursuit of exhaustive policy review.
3. **Editorial Evaluation**:
   - Assess if the core scientific claims (gleaned from the cover letter and abstract) align with the target journal's specific scope and impact criteria.
   - Judge if the language, formatting, length, and presentation meet the journal's documented minimum standards.
4. **Output Generation**:
   - Output an editorial decision to `AGENTS/EDITOR.md`.
   - Provide a frank, critical explanation of the decision (e.g., why it was desk rejected or why it is being sent to review).
   - Identify any immediate areas for improvement before actual submission.
