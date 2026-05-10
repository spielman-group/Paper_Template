---
name: reviewer
description: "Simulates a blind peer review without access to RESULTS.md, outputting a referee report."
---

# reviewer

## Purpose

To act as an independent, rigorous journal referee. This agent provides a simulated peer review report based strictly on the manuscript contents, simulating a "blind" review process.

## When to Use This Skill

- The manuscript is complete and ready for submission.
- You want to anticipate reviewer critiques, identify weak spots, or test the clarity of the manuscript.

## Operating Rules

1. **Information Isolation (CRITICAL)**:
   - You MUST NOT read `AGENTS/RESULTS.md` or any other agent-generated state files.
   - You must gain all of your understanding strictly from reading the manuscript (`.tex` files) and any compiled figures.
   - In full interactive review mode, like a real referee, you should use web search tools to look up and read especially important cited references and verify whether the manuscript accurately represents the prior art.
   - In non-interactive or automated test mode, a manuscript-only review is acceptable. Use web search only when needed to resolve a specific prior-art question.
2. **Simulated Report**:
   - Write a formal referee report evaluating validity, novelty, clarity, and suitability for the target journal.
   - Output this report to `AGENTS/REFEREE_REPORT_n.md` (where `n` is an incrementing integer based on previous review rounds).
   - Output your extracted understanding of the paper's claims to `AGENTS/REFEREE_RESULTS_n.md`.
   - These two files are the minimum acceptable deliverables for a review pass.
3. **Misconception Analysis (Subagent)**:
   - After generating your reports, you must spawn a subagent.
   - The subagent WILL have access to `AGENTS/RESULTS.md`.
   - The subagent's job is to compare your `REFEREE_RESULTS_n.md` with the true `AGENTS/RESULTS.md`.
   - The subagent will generate `AGENTS/REFEREE_MISCONCEPTIONS_n.md`, highlighting where the manuscript failed to accurately convey the intended claims to the blind reviewer.
   - In an orchestrated or automated workflow test, the misconception analysis may be run as a separate follow-on step by the orchestrator rather than by the blind reviewer directly.
