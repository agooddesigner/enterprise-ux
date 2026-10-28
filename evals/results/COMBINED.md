# Combined results (2 runs, strict design checklists)

| Case | No skill | v1 | v2 |
|---|---|---|---|
| E1 Design: invoices list | 28% | 75% | 80% |
| E2 Design: members & roles | 60% | 73% | 80% |
| E3 Spec: CSV import | 88% | 96% | 100% |
| E4 Grill: weak PRD | 70% | 55% | 100% |
| E5 Plan: approvals inbox | 58% | 62% | 96% |
| E6 Audit: planted issues | 95% | 98% | 100% |
| E7 A11y: kanban | 85% | 80% | 85% |
| E8 AI: auto-categorise | 79% | 88% | 96% |
| **Overall (2 runs)** | **152/222 (68%)** | **177/222 (80%)** | **203/222 (91%)** |
| Run 1 | 69% | 79% | 93% |
| Run 2 | 68% | 80% | 90% |

**Setup:** Claude Code 2.1.311 headless, default model, clean config (no personal skills/plugins), 2 independent runs × 8 cases × 3 conditions = 48 sessions. Blind LLM grading against the fixed checklists in `../cases.md` (E1/E2/E7 use the strict checklists; run 1 design outputs were re-graded with them). Run-level totals are consistent: 69 → 68% (no skill), 79 → 80% (v1), 93 → 90% (v2).

**What holds across both runs**
- v2 beats no skill by ~23 points overall and v1 by ~11.
- Biggest v2 gains: **Grill** (100% vs 70% no skill, 55% v1) and **Plan** (96% vs 58% / 62%).
- Design-code cases: both skill versions far ahead of no skill on E1 (80% / 75% vs 28%); v2 slightly ahead on E2.
- No reliable gain on **E7 accessibility** (85 / 80 / 85%) — the base model already handles kanban a11y well; this is where the skill adds least.
- Audit (E6) and CSV spec (E3) are near ceiling for everyone — those checklists are too easy to separate conditions.

**Limits:** LLM judge (spot-check a few by hand), single model, 2 runs, checklists written by the skill author. Raw outputs, judge reasoning and screenshots are in each run folder.

**Screenshots:** `2026-10-27-run1/screenshots/` and `2026-10-28-run2/screenshots/` — one full-page capture per HTML output plus `<case>-side-by-side.png` (No skill | v1 | v2).
