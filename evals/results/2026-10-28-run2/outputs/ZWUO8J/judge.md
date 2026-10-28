| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | AI suggestions labelled as AI-generated | 0 | States "Auto-coded/Suggested" chip states; no explicit AI label. |
| 2 | Accept, reject or edit each suggestion | 1 | Drawer actions: "Accept, Change, Always do this for this vendor". |
| 3 | Shows confidence, preferably categorical | 0 | Calibrated confidence is computed, but nothing shows it to users. |
| 4 | Low-confidence items go to human review | 1 | Route step: auto-post / suggest / human review; "Needs review" state. |
| 5 | Explains why or shows sources | 1 | One-line reason: "Matches 14 past Zoom charges → 6240". |
| 6 | Undo / revert for AI-applied changes | 1 | "Undo: bulk recode with one click, as long as the period is open." |
| 7 | Bulk accept for high-confidence items | 0 | Bulk approve is for similar items such as all "Uber" rows, not tied to confidence. |
| 8 | Admin controls: enable/disable, thresholds, scope | 1 | Admin settings: auto-post threshold, excluded accounts, editable rules. |
| 9 | Audit log records AI vs human changes | 1 | Logs model version, confidence, "who accepted or overrode it". |
| 10 | Explains limits/accuracy to users up front | 1 | Shadow mode: "customer sees their own accuracy score" before suggest mode. |
| 11 | Manual fallback path that works without AI | 0 | Manual coding is implied, but no explicit non-AI path or AI-off mode. |
| 12 | Tracks a quality metric | 1 | Metrics table: auto-post precision, suggestion acceptance rate, reversal rate. |

TOTAL: 8/12
