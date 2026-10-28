# Judge prompt (for blind grading)

Use this in a **fresh chat with no skills enabled**. Paste the prompt below, then the case's checks from `cases.md`, then one output. Grade one output per chat so outputs don't influence each other.

```
You are grading a design output against a fixed checklist. You don't know which system produced it. Be strict and literal.

Rules:
- Score each check 1 (clearly and specifically present) or 0 (missing, wrong, or only vaguely gestured at, e.g. "consider error states" with no actual error state).
- For code, judge what the code actually does, not what comments claim.
- Do not reward length, polish or tone. Only the checks count.
- Quote the evidence (≤15 words or a line reference) for every 1.

Output exactly this table, then the total:

| # | Check | Score | Evidence |
|---|---|---|---|

TOTAL: <passed>/<total>

CHECKLIST:
<paste the checks for this case>

OUTPUT TO GRADE:
<paste the output>
```

## Calibrate the judge
Before trusting it, grade **2 outputs yourself** with the same checklist and compare. If you disagree on more than 2 checks per case, tighten the wording of those checks in `cases.md` and re-grade.
