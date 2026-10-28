| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Downloadable template or file requirements before upload | 1 | "Download CSV template"; format, max 50,000 rows/50 MB requirements panel |
| 2 | Header-row detection or confirmation | 1 | "First row looks like headers" with "First row is not a header" toggle |
| 3 | Column mapping with auto-suggestions, overridable | 1 | Auto-suggest via synonyms; searchable select to change mapping |
| 4 | Value mapping for enum fields | 1 | "Match values" panel: "USA", "U.S." → United States |
| 5 | Row/cell-level errors with specific message | 1 | "Row 37, Email: 'jane@acme' is missing a domain extension" |
| 6 | Fix in place or exclude rows without re-upload | 1 | Inline edit cells, bulk fixes, "Skip all rows with errors" |
| 7 | Duplicate handling strategy chosen by user | 1 | Step 4: update empty/overwrite/skip existing; duplicates in-file policy |
| 8 | Background processing with progress, can leave | 1 | Determinate progress; close tab, job continues, notification on completion |
| 9 | Completion summary with counts | 1 | "Created 44,870 · Updated 1,903 · Skipped 0 · Failed 440" |
| 10 | Downloadable error report | 1 | "Download error report" for failed rows, re-uploadable |
| 11 | Undo/rollback or stated non-undoable | 1 | "Undo import" available 7 days, with consequence dialog |
| 12 | States: uploading, processing, success, partial failure, total failure | 1 | Upload bar; progress; Result states: Succeeded, Partially failed, Failed (nothing written) |

TOTAL: 12/12
