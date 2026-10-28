| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Downloadable template or file requirements before upload | 1 | "Download template"; helper text ".csv up to 50,000 rows and 100 MB" |
| 2 | Header-row detection or confirmation | 1 | Toggle "First row contains column headers", on by default |
| 3 | Column mapping with auto-suggestions, overridable | 1 | Fuzzy auto-mapping, "Matched" tag, searchable Maps-to dropdown |
| 4 | Value mapping for enum/picklist fields | 0 | Only invalid dropdown options flagged; unrecognized country blanked; no value-mapping UI |
| 5 | Row/cell-level errors with specific message | 1 | Row number, field, value, message; "Expected 12 columns, found 9." |
| 6 | Fix errors in place or exclude bad rows without re-upload | 1 | "Import N valid rows" excludes error rows without re-uploading |
| 7 | User chooses duplicate strategy | 1 | Skip / Update existing / Create duplicates anyway options |
| 8 | Background processing, progress, can leave | 1 | "You can close this window"; header chip shows live progress |
| 9 | Completion summary with counts | 1 | Summary shows Created, Updated, Skipped and Failed counts |
| 10 | Downloadable error report | 1 | "Download error report (CSV)" and "Download failed rows" |
| 11 | Undo/rollback or statement it can't be undone | 1 | "Undo import" removes created contacts, available 30 days |
| 12 | States: uploading, processing, success, partial, total failure | 0 | Upload, progress, success, mid-way failure covered; total failure not distinct |

TOTAL: 10/12
