# Plan rubric

Used to grade any plan governing this pipeline before it is acted on. 100 points. A plan below 75
gets revised before execution, not after.

| # | Criterion | Points | What full marks looks like | What loses points |
| --- | --- | --- | --- | --- |
| 1 | Diagnoses the real failure mode | 10 | Names the specific mechanism that produces bad output today, with evidence from the repo | Describes a symptom, or asserts a problem no artifact demonstrates |
| 2 | Decisions decided, not deferred | 10 | Every choice in the Decisions section is settled with a rationale | "TBD", "we should consider", or a choice restated as a question |
| 3 | Executable unattended | 15 | Every step names an owner and a done-when condition a cloud agent could evaluate | Steps with no owner; verbs like "improve" or "review" with no checkable end state |
| 4 | Measurable quality bar | 15 | Checks are mechanical, and failing one has a stated consequence | A gate that records a result but changes no behavior; thresholds that conflate volume with quality |
| 5 | Closes the feedback loop | 10 | What happened in the room gets recorded, and a later step demonstrably reads it | A log file with no mechanism that causes anyone to fill it |
| 6 | Scope discipline | 10 | An explicit out-of-scope list naming the adjacent work most likely to creep in | Open-ended scope, or scope that grew past what was asked |
| 7 | Handles the supply problem | 10 | States how much input material exists, how fast it is consumed, and what happens when it runs out | Assumes input is infinite; optimizes selection on a pool that is about to empty |
| 8 | Sequencing correctness | 10 | No step depends on an artifact a later step creates; no step races a live automation | Steps out of dependency order; concurrent writes to the same state file |
| 9 | Preserves the hard commitment | 10 | The two-workshops-a-month floor survives every change, including failure paths | A change that could cause a skipped month |

## How to grade

Score each criterion independently before totalling. Do not adjust a score because the total
looks low — the total is the finding. Record the grade, the reason for every deduction, and what
changed in response, in the plan's own `## Grading record` section.

A criterion scoring below half its points is a hole, not a rough edge. Name it in prose as well as
in the table, because tables get skimmed.
