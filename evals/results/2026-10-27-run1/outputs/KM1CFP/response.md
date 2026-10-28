I wrote the UX spec for the 50,000-contact CSV import. It's a draft that hasn't been checked with engineering. Its timing targets are proposals, and its permission roles need checking against your CRM's real role model.

**Where it's saved:** `/tmp/ux-eval-results/KM1CFP/csv-contact-import-ux-spec.md`

**Core design decisions**
- **Preview before writing:** nothing is saved until the user confirms a dry-run review showing real counts (created, updated, skipped, duplicates). The button reads "Import 46,322 contacts".
- **Flow:** it is a full-page, five-step flow: Upload, Map columns, Settings, Review, Import progress. Each step has its own URL, and drafts are kept for 7 days.
- **Errors are fixed in bulk:** errors are grouped by reason (for example "Invalid email: 1,204 rows") rather than listed row by row. Users download an error report CSV, fix it, and re-import only those rows.
- **Leave-able imports:** imports run in the background in batches of about 500 rows, so users can close the page and get a notification when it finishes.
- **Rollback:** any import can be rolled back for 30 days. The confirmation states the counts and says that contacts edited since the import are left as they are.
- **Safe defaults:** existing contacts are skipped by default. Overwriting needs an explicit confirmation naming the count.
- **Hard limits:** files over 50,000 rows or 25 MB are rejected, with a split-file download offered for the row limit. Excel files get instructions for exporting as CSV.

**What else the spec covers**
- A states table with about 30 rows, covering permission, upload, mapping, validation, progress, results, history and session-expiry cases.
- Data-handling rules for matching, dates, blanks, duplicates within a file, and spreadsheet formula injection on export.
- Performance targets, notifications, accessibility and keyboard behaviour, copy rules, success metrics, and open questions.
- Out of scope for now: direct XLSX import, importing companies or deals, and scheduled imports.

Open questions I left for you:
- **Soft-deleted contacts:** should the duplicate check include them? I recommend yes, with an option to restore the matches.
- **Overwrite rights:** should reps without admin rights be able to overwrite existing contacts? I recommend no.
- **File retention:** how long should uploaded files be kept? The spec assumes 30 days, which needs confirming with legal because the files contain personal data.
