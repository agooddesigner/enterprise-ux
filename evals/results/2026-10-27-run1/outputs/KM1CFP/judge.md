| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Template or file requirements before upload | 1 | Step 1: "Download template CSV" and requirements panel (.csv, 50,000 rows, 25 MB) |
| 2 | Header-row detection or confirmation | 1 | Client-side sniff detects "delimiter, encoding and header row" with Change control |
| 3 | Column mapping with auto-suggestions, overridable | 1 | Step 2: fuzzy auto-mapping with "Auto" tag; searchable combobox to edit |
| 4 | Value mapping for enum/picklist fields | 1 | Fix rule: "Map 'Hot lead' → [Lead ▾]" or create new option |
| 5 | Row/cell-level errors with specific message | 0 | Errors are grouped by reason; in-cell highlight exists but not row-level messages |
| 6 | Fix errors in place or exclude bad rows without re-upload | 1 | Bad rows are skipped and "Import valid rows" is offered; fix rules apply in-flow |
| 7 | Duplicate handling strategy chosen by user | 1 | Step 3: Skip / Update only empty / Update and overwrite radios |
| 8 | Background processing with progress, can leave | 1 | "You can close this page"; determinate progress, batches of ~500 rows |
| 9 | Completion summary with counts | 1 | "Created 41,208 · Updated 5,114 · Skipped 1,796" |
| 10 | Downloadable error report | 1 | "Download error report (CSV)" with error_row_number and error_reason |
| 11 | Undo/rollback or no-undo statement | 1 | "Roll back import" available for 30 days, with a confirmation naming counts |
| 12 | States covered: uploading, processing, success, partial failure, total failure | 1 | §7 table has Uploading, Running, Success, Partial, Failed/All rows invalid |

TOTAL: 11/12
