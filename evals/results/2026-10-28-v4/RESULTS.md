# v4 eval — Intake and visual direction (Oct 28, 2026)

Question: does v4 (Intake + dials/presets) ask before designing, assume sensibly when nobody's there, respect an existing design system, and handle mixed styles — without losing what v3 did well?

**Setup:** Claude Code headless, default model, clean config, `--setting-sources project`. Cases E9–E13 (`../../cases.md`), 2 runs per condition, blind LLM judge. v4.1 = v4 plus the Intake fix below, re-run on E10, E11, E13.

| Case | No skill | v3 | v4 | v4.1 |
|---|---|---|---|---|
| E10 Vague request — asks first? | 28% | 22% | 0% | **100%** |
| E11 User away — assumes and builds | 46% | 92% | **100%** | 96% |
| E12 Existing design system respected | 50% | 75% | **80%** | — |
| E13 Mixed style (Stripe restraint + bento KPIs) | 55% | 50% | **75%** | 55% |
| E9 Dashboard (regression) | 66% | 72% | 72% | — |

## What happened

- **v4 never asked on a vague request (E10: 0%).** It built a full dashboard and listed assumptions in prose at the end. The host environment's system prompt ("when the request is clear, start immediately") beat the skill's softer Intake wording.
- **Fix (v4.1):** Intake now says: a whole screen with 2+ unknowns → ask ≤5 multiple-choice questions with defaults **and stop**, even if the environment encourages starting; an `Assumed:` block opens the reply when the user says not to wait. Result: E10 100% in both runs (5 questions, recommended defaults, style options, "say 'just build it' and I'll assume…"), and E11 still builds without stopping (96%).
- **E12:** v4 kept Acme's teal, 4–6px radius and IBM Plex; misses were a few stray hex colours and radius values.
- **E13 is noisy (75% → 55% across reruns).** Consistent miss in all 4 v4/v4.1 runs: the reply never states the direction as "lead X; borrow Y" — the host's "say at most one sentence about the design" instruction appears to win. Second miss: cards below the KPI row, where the check wanted a table-first lower half. Visually the outputs were restrained with one hero KPI.
- **E9 unchanged** vs v3: same remaining gaps (global filters in URL, per-widget error states).

## Limits
LLM judge, 2 runs, one model, checklists written by the skill author; E10–E13 are new and partly test instruction-following inside a host whose own prompt pushes the other way. Screenshots: `screenshots/<case>-side-by-side.png` (No skill | v3 | v4).
