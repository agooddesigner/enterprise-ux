# Eval results — 27 Oct 2026, run 1

**Setup:** Claude Code 2.1.311 headless (`claude -p`), default model, clean config (no personal skills or plugins), 1 run per case per condition, 24 sessions. Graded blind by a separate Claude session using the fixed checklists in `../../cases.md`; the judge never saw which condition produced an output.

| Case | No skill | v1 | v2 |
|---|---|---|---|
| E1 Design: invoices list | 15/20 | 19/20 | 18/20 |
| E2 Design: members & roles | 13/15 | 14/15 | 12/15 |
| E3 Spec: CSV import | 10/12 | 11/12 | 12/12 |
| E4 Grill: weak PRD | 8/10 | 5/10 | 10/10 |
| E5 Plan: approvals inbox | 8/12 | 7/12 | 12/12 |
| E6 Audit: 18 planted issues | 19/20 | 19/20 | 20/20 |
| E7 A11y: kanban | 9/10 | 10/10 | 9/10 |
| E8 AI: auto-categorise | 11/12 | 10/12 | 12/12 |
| **Overall** | **93/111 (84%)** | **95/111 (86%)** | **105/111 (95%)** |

## What it shows
- v2 wins most clearly where the skill adds *process*: **Grill** (+2 over no skill, +5 over v1) and **Plan** (+4 over no skill, +5 over v1). It was the only condition to score full marks on Plan, Grill, CSV spec, Audit and AI.
- v1 barely beat no skill overall (+2). The research-backed rebuild is what moved the needle (+10 over v1).
- On code-generation design cases (E1, E2, E7) there's **no clear win**: the baseline is already strong and differences are 1–3 checks — within run-to-run noise for a single run.

## Caveats (read before quoting)
- **One run per cell.** A 1–3 check difference on a single case is noise. Only the overall gap and the Plan/Grill gaps are large enough to take seriously, and they still need a second run.
- **Checklists are too easy for design cases.** No-skill already scores 75–90% there; harder checks are needed (e.g. URL state actually works, all states reachable, WCAG 2.2 specifics) to see real separation.
- **LLM judge.** Some 0s are debatable (E1 check 2 marked v2 down because a checkbox column sits before the invoice number). Calibrate by hand-grading a few outputs.
- **Two harness fixes were applied mid-run** and are documented: (1) one v2 output (E2, code `197ZF1`) saved its HTML to the session scratchpad, so the judge first saw only the summary (9/15) — re-graded with the file (12/15); (2) the original E7 prompt referenced an existing board without providing code — v2 correctly asked for the code and scored 0 while others improvised — the prompt was fixed and E7 re-run for all three conditions.

## Where v2 still lost points
- E1: bulk-bar buttons "Approve 5" / generic Cancel in a dialog; checkbox column before identifier.
- E2: no last-admin protection; no "last changed by"; table selects with visually hidden labels.
- E7: didn't explicitly recommend keyboard + screen-reader testing.

These are fed back as candidate improvements for the skill.

## Update: stricter design checklists (same outputs, re-graded)

The E1, E2 and E7 checklists were rewritten to test deeper enterprise behaviour (URL state restored on load, select-all-matching, partial-failure handling, skeleton + error states actually reachable, last-admin protection, audit attribution, WCAG 2.2 specifics). The same 9 outputs were re-graded blind:

| Case | No skill | v1 | v2 |
|---|---|---|---|
| E1 Invoices list | 4/20 | 14/20 | 15/20 |
| E2 Members & roles | 9/15 | 13/15 | 13/15 |
| E7 A11y kanban | 8/10 | 9/10 | 9/10 |
| **Design total** | **21/45 (47%)** | **36/45 (80%)** | **37/45 (82%)** |

Reading: with harder checks, both skill versions clearly beat no skill on design work (+33–35 points), but v2 ≈ v1 on design — v2's extra value shows up in Plan and Grill. Checks are combined (all parts must be present), which makes grading strict; one judge call on E1 (baseline, check 16) was uncertain. Per-output judge files are in `regrade-strict-checks/`.
