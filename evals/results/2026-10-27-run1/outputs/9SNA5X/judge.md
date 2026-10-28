| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | AI suggestions labelled as AI-generated | 0 | Column "Suggested GL" and "Suggestions" only; no explicit AI label on suggestions |
| 2 | Accept, reject or edit each suggestion | 1 | Inline editable combobox; `A` approve, `E` edit, alternatives one-click switch |
| 3 | Categorical confidence | 1 | Labelled chip High / Medium / Low, number on hover |
| 4 | Low-confidence to human review | 1 | Low: no pre-selection, flagged "Needs a human"; forced review rules |
| 5 | Explains why / sources | 1 | "Why this code" sentence plus evidence chips (rule, history, receipt text) |
| 6 | Undo / revert | 1 | 30-second toast undo, then "Recent activity" until period closes |
| 7 | Bulk accept for high-confidence | 1 | "Approve 164 high-confidence" with confirmation and review sample |
| 8 | Admin controls | 1 | Settings → AI coding: enable per entity, thresholds, auto-post toggle |
| 9 | Audit log AI vs human | 1 | Stores suggestion, score, source, model version, reviewer, final code |
| 10 | Limits/accuracy explained up front | 0 | Shadow-mode accuracy is for admins; no user-facing limits explanation |
| 11 | Manual fallback without AI | 1 | Banner: "Suggestions are unavailable. Manual coding still works." |
| 12 | Quality metric tracked | 1 | Accuracy dashboard: acceptance rate, override rate by GL and vendor |

TOTAL: 10/12
