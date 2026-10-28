# Evaluating the skill

Question this answers: **does Claude produce better enterprise UX with the skill than without it — and is v2 better than v1?**

- 8 cases (`cases.md`) across Plan, Grill, Design, Audit, accessibility and AI — 111 binary checks in total.
- 3 conditions: **A = no skill**, **B = v1**, **C = v2**.
- Blind grading with a fixed checklist (`judge-prompt.md`), recorded in `scoresheet.csv`.

## What makes the result trustworthy

1. **Same model** for every run (pick one, e.g. Opus or Sonnet — note it down).
2. **Fresh chat per run.** Never run two cases in one chat.
3. **Nothing else helping.** Turn off every other design skill (frontend-design, impeccable, ui-ux-pro-max, ux-heuristics, emil-design-eng, hooked-ux…) for *all* conditions, or the baseline isn't a baseline. Don't run inside a Project with design docs. Turn off memory / past-chat search during the test (or use a chat mode without memory if skills still work there).
4. **Prompts pasted exactly.** Never mention the skill in the prompt.
5. **2 runs per case per condition** if you can — outputs vary run to run. 1 run gives a rough signal only.
6. **Grade blind.** The grader (you or the judge chat) must not know which condition produced an output.

---

## Option 1 — Claude.ai (no coding; recommended)

Time: ~2–3 hours for 1 run of everything (24 chats + grading), double for 2 runs.

**Setup**
1. Have both zips ready: `enterprise-ux-v1-for-eval.zip` (v1) and `enterprise-ux-claude-ai.zip` (v2). Both use the same skill name, so **only one can be uploaded at a time**.
2. In Claude's settings, open the Skills section. Disable every other design skill. (The settings UI changes often — look for "Skills" under capabilities.)
3. Make a folder on your laptop: `eval-runs/` with sub-folders named by a random code per run (e.g. `K7Q2`, `M91X`…). Keep a private `key.txt` mapping code → case + condition. Don't look at it while grading.

**Run order** (do one condition fully, then switch skills)
1. **Condition A (no skill):** for each case E1–E8, open a new chat, paste the prompt, save the full response (copy text; download any HTML file) into its code folder.
2. **Condition B:** upload the v1 zip, enable it. Repeat E1–E8 in fresh chats. Check one response: Claude should mention using the skill — if it doesn't, the skill didn't load; redo.
3. **Condition C:** remove v1, upload v2, enable it. Repeat E1–E8.
4. For E6, paste only from `<html>` to `</html>` of `fixtures/audit-target.html` — **not** the comment at the top (it's the answer key).

## Option 2 — Claude Code (automated)

Runs everything unattended and handles blinding for you.

```bash
# 1. get v1 out of git history (or unzip enterprise-ux-v1-for-eval.zip)
git archive 15f39e2 plugins/enterprise-ux/skills/enterprise-ux | tar -x -C /tmp/v1

# 2. temporarily move personal design skills out of ~/.claude/skills

# 3. run (2 runs × 8 cases × 3 conditions = 48 runs)
python3 evals/run_claude_code.py --v1 /tmp/v1/plugins/enterprise-ux/skills/enterprise-ux --runs 2 --model sonnet
```

Outputs land in `evals/results/<code>/` (response text + any files Claude wrote). The key is saved separately in `evals/results_KEY_do_not_open_until_graded.json`. Flags (`-p`, `--permission-mode acceptEdits`, `--setting-sources project`, `--model`) were checked against Claude Code docs in Oct 2026 — run `claude --help` once to confirm on your version.

---

## Grading

1. For each output, open a **fresh chat with no skills enabled**, paste the judge prompt from `judge-prompt.md`, the case's checks from `cases.md`, and the output. For HTML outputs, paste the code.
2. Record the score against the blind code in `scoresheet.csv`.
3. **Calibrate first:** grade 2 outputs yourself before using the judge. If you and the judge differ on >2 checks in a case, tighten those checks.
4. For design cases (E1, E2), also open the HTML in a browser and click through — the judge reads code; you can see behaviour. Override a check if the code claims something the page doesn't do.
5. Only after everything is graded, open the key and fill in the condition column.

## Reading the results

- Report **per-case %** and **overall %** for A, B, C (overall = total checks passed ÷ 111 per run).
- A difference is believable when it shows up in **both runs** and in **most cases**, not one big swing in a single case.
- Look at *which* checks flip. That tells you what the skill actually changes (e.g. states, safety, a11y) and where it doesn't help yet — feed those back into the skill.
- Expect the baseline to already pass easy checks (tables, labels). The skill's value is in the hard ones: states, undo, permissions, URL state, WCAG 2.2 specifics, pushing back in Grill.

## Publishing the result

Put a small table in the main README, e.g.:

| Condition | Overall | E1 Design | E4 Grill | E6 Audit | E7 A11y |
|---|---|---|---|---|---|
| No skill | xx% | | | | |
| v1 | xx% | | | | |
| v2 | xx% | | | | |

State the model, date, number of runs, and that grading used a fixed checklist with blind codes. Keep the raw outputs in the repo (`evals/results/`) so anyone can re-grade. Honest numbers — including cases where the skill didn't help — are more convincing than a perfect score.
