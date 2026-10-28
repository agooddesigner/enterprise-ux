| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Downloadable template or file requirements before upload | 1 | Limits shown up front; link to download template CSV |
| 2 | Header-row detection or confirmation step | 1 | "First row is a header" toggle, auto-detected |
| 3 | Column mapping with auto-suggestions, overridable | 1 | Auto-map by header/synonyms, "Matched" chip, user can change |
| 4 | Value mapping for enum/picklist fields | 0 | Only "Add new option" or row error; no value-to-value mapping |
| 5 | Row/cell-level errors with specific message | 1 | "Row 214: 'john@' isn't a valid email"; example rows with reason |
| 6 | Fix errors in place or exclude bad rows without re-upload | 1 | Error rows automatically skipped; import proceeds without them |
| 7 | Duplicate strategy chosen by user | 1 | Skip / Update / Create anyway in Configure step |
| 8 | Background processing, progress, can leave | 1 | "You can close this page"; determinate progress bar, ETA |
| 9 | Completion summary with counts | 1 | Results: created, updated, skipped, failed breakdown |
| 10 | Downloadable error report | 1 | Download error report CSV with row_number and error_reason |
| 11 | Undo/rollback or statement it can't be undone | 1 | Undo import available 30 days, confirm modal states counts |
| 12 | States: uploading, processing, success, partial failure, total failure | 1 | Chunked upload progress; validation/import progress; success; amber partial; red full failure |

TOTAL: 11/12
