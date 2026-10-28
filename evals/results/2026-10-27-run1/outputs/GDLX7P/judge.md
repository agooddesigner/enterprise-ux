| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | AI suggestions labelled as AI-generated | 1 | "Code posted, marked 'AI'"; source "Rule" vs AI distinguished |
| 2 | Accept, reject or edit each suggestion | 1 | "`Enter` accept, `1/2/3` pick an alternative, `E` edit" |
| 3 | Shows confidence, preferably categorical | 1 | "confidence chip" in the queue table; tiers Auto-apply/Suggest/Needs human |
| 4 | Low-confidence items go to human review | 1 | "<70%... Needs human"; risk overrides force review |
| 5 | Explains why / shows sources | 1 | "Notion was coded here in 14 of 14 prior transactions" |
| 6 | Undo / revert for AI-applied changes | 1 | "bulk-revert AI-coded items in a date range" |
| 7 | Bulk accept for high-confidence items | 1 | "Accept all 42 high-confidence AWS items" |
| 8 | Admin controls: enable/disable, thresholds, scope | 1 | "Auto-apply threshold, per-account exclusions"; kill switch |
| 9 | Audit log records AI vs human changes | 1 | Records model version, suggestion, "who accepted or overrode it" |
| 10 | Explains limits/accuracy to users up front | 0 | Shadow mode shows projected accuracy to customer, but no user-facing limits explanation |
| 11 | Manual fallback path works without AI | 1 | Rules layer deterministic; "Needs human" queue; rule manager |
| 12 | Tracks a quality metric | 1 | "Override rate by account", auto-apply precision, calibration error |

TOTAL: 11/12
