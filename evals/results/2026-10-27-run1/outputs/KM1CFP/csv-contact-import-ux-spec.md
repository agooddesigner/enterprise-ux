# UX Spec: CSV Contact Import (up to 50,000 rows)

## 1. Job, user, frequency

- **Users:** Sales/marketing ops and admins (primary); reps with import permission (secondary).
- **Job:** Get a list from another system (events, old CRM, purchased list, spreadsheet) into the CRM without creating duplicates or corrupting existing records.
- **Frequency:** Low to medium (weekly to quarterly per person), but high stakes. A bad import pollutes the whole database. Optimise for **guidance and safety**, with fast repeat runs via saved mappings.
- **Scale:** Up to 50,000 rows, about 10–25 MB, 5–60 columns. Expect messy data: mixed encodings, Excel-mangled phone numbers, dates in several formats, blank rows, duplicate emails, values over 255 characters.

## 2. Principles

1. **Nothing is written until the user confirms a preview with real counts.** Validation happens first, commit happens second.
2. **Never lose work.** Mapping, uploaded file and decisions survive refresh, tab close and session timeout (draft import, 7 days).
3. **Errors are fixable in bulk.** Users download a file of failed rows with reasons, fix it and re-upload only that. They never hand-fix 2,000 rows in the UI.
4. **Long-running means leave-able.** After confirmation, the import runs in the background. The user can navigate away and gets notified.
5. **Undoable.** Every completed import can be rolled back as a batch for 30 days, as long as the created records are untouched.

## 3. Permissions

| Role | Can do |
|---|---|
| Admin, Import manager | Import, update existing, roll back any import, set owner to anyone |
| Standard rep | Import as new records owned by self, only if "Can import" is on; roll back own imports |
| Read-only / no permission | **Import contacts** button is visible but disabled. Tooltip: "You don't have permission to import. Ask an admin (Priya Raman, Dana Okafor) to grant 'Import contacts'." with a "Request access" link |

Imports are capped at 50,000 rows per file. Concurrent imports per workspace: 3 active, extra ones are queued with visible position.

## 4. Entry points

- Contacts list, toolbar: **Import** (secondary button). Also in the ⋯ menu and command palette ("Import contacts").
- Empty Contacts state: primary **Import from CSV** next to **Add contact**.
- Import history page: **New import** (primary).
- Route: `/contacts/import/:importId`. Each step has its own URL (`/upload`, `/map`, `/review`, `/progress`, `/results`), so links are shareable and the browser Back button works. Draft imports are listed on the history page.

## 5. Flow overview

A full-page flow (not a modal), because the task is long and needs space. A stepper sits at the top: **1 Upload → 2 Map columns → 3 Settings → 4 Review → 5 Import**. Completed steps are clickable. The footer is sticky with **Back** (secondary) and one primary action. Closing the flow shows "Save draft and exit" with no data loss.

### Step 1: Upload

**Layout:** A large drop zone, a "Choose file" button, and a side panel containing:
- Download template CSV (with our field names, one example row).
- Requirements: .csv or .tsv, up to 50,000 rows, up to 25 MB, first row must be headers, UTF-8 recommended.
- Link: "How to export from Salesforce / HubSpot / Excel / Google Sheets".

**Behaviour:**
- On drop, upload begins immediately with a progress bar, filename, size and a Cancel control.
- Client-side sniff of the first 1 MB: detect delimiter (comma, semicolon, tab), encoding (UTF-8, UTF-8 BOM, Windows-1252, Latin-1) and header row. Show detected values with a small "Change" control (for example "Delimiter: semicolon · Encoding: Windows-1252"). Changing re-parses the preview instantly.
- The full file is then parsed server-side. Show "Reading file… 31,200 of 48,730 rows".
- Show a 5-row preview of raw data as the user will see it, so that garbled characters are caught immediately.
- Row count is displayed prominently: "48,730 rows · 14 columns".
- **Continue** is disabled until parsing completes with at least 1 data row.

**Hard stops (inline error, file rejected):**

| Condition | Message |
|---|---|
| Over 50,000 rows | "This file has 62,415 rows. The limit is 50,000 per import. Split it into 2 files and import them one after the other." Offer **Download split files** (generated client-side/server-side in 50k chunks). |
| Over 25 MB | "This file is 31 MB. The limit is 25 MB. Remove unused columns or split the file." |
| Wrong type (.xlsx, .xls) | "Excel files can't be imported directly. In Excel, choose File → Save As → CSV UTF-8, then upload that file." |
| No header / duplicate header names | "Two columns are both called 'Email' (columns C and H). Rename one and re-upload." |
| Empty file | "This file has headers but no data rows." |
| Corrupt or unparseable (unclosed quotes) | "Couldn't read the file after row 4,212 (unclosed quote). Fix that row and re-upload. Reference: IMP-8F2K1." |

### Step 2: Map columns

**Layout:** A table with one row per CSV column (not per CRM field).

| CSV column | Sample values (first 3 non-empty) | Maps to CRM field | Status |
|---|---|---|---|

- **Auto-mapping** by exact and fuzzy header match ("E-mail", "email address" → Email) plus the user's previous mappings for the same header names. Auto-matched rows show an "Auto" tag and a confidence indicator. Low-confidence matches are highlighted and must be confirmed.
- The field selector is a searchable combobox grouped as Standard fields, Custom fields and Special actions: **Don't import this column**, **Create new custom field…** (opens a side panel; type is inferred, admins only).
- Samples are truncated with an ellipsis and a tooltip with the full value.
- Per-row **Data format** control where relevant (date format DD/MM/YYYY vs MM/DD/YYYY with live examples from the file, phone country default, boolean values yes/no/true/1).
- A summary strip above the table: "11 of 14 columns mapped · 2 ignored · 1 needs attention".
- A column-level quality hint appears under the sample: "3% blank · 41 values don't look like emails".
- Filters on the table: All / Needs attention / Unmapped / Mapped. Sticky header with 14+ columns; keyboard navigable (arrow keys through selects, type to search).
- **Save this mapping as** [name] checkbox. The next import with matching headers offers "Use saved mapping 'Eventbrite export'".

**Validation to proceed:**
- **Email is required** (or Phone, per workspace setting). If unmapped, the primary action is disabled with the reason inline: "Map a column to Email to continue."
- Two CSV columns can't map to the same single-value field (inline error on both rows). Multi-value fields (secondary email) are separate fields.

### Step 3: Settings

A short form with radio choices, each with a one-line consequence:

1. **What to do with contacts that already exist** (matched on Email by default; the match field is selectable among Email, Phone, External ID):
   - *Skip them* (default, safest): "Existing contacts stay unchanged."
   - *Update only empty fields*: "Fills blanks, never overwrites."
   - *Update and overwrite*: "Replaces existing values with the file's values." Shows a warning and requires Review confirmation.
2. **Owner:** [Me ▾] or a column from the file ("Owner email").
3. **Add to list / tag:** optional, creatable combobox (for example "Import 2026-10-27 – Webinar leads"). A default tag "import-<date>" is prefilled, which makes later cleanup easy.
4. **Lifecycle stage / source:** optional default values.
5. **Consent/opt-in:** checkbox "I confirm these contacts have given permission to be contacted" (required where the workspace's compliance setting is on; stored with the import record).
6. **Notify me by:** in-app plus email when finished (default on).

### Step 4: Review (the dry run)

The server runs a full **validation dry run** and shows results before anything is written. Show a progress indicator (determinate: "Checking 48,730 rows… 62%") that can be left and returned to.

**Summary cards (with counts and percentages):**

| Outcome | Example |
|---|---|
| **Will be created** | 41,208 |
| **Will be updated** (or skipped, per setting) | 5,114 |
| **Duplicates within the file** (same email appears multiple times, the last or first row wins, selectable) | 612 |
| **Will be skipped, with errors** | 1,796 |

Each count is a link that filters the preview table below.

**Error breakdown** (grouped by reason, sorted by count, not row-by-row):
- "Invalid email format: 1,204 rows" — example values: `john@@acme`, `n/a`, `jane.doe`
- "Required field missing (Email): 342"
- "Value too long (Notes, max 2,000 characters): 31"
- "Unrecognized date in 'Birthday': 187"
- "Unknown value for 'Lifecycle stage': 32 ('Hot lead')"

Each group has actions:
- **View rows** (opens the filtered preview).
- **Fix rule**, where cheap: for instance, for unknown picklist values, "Map 'Hot lead' → [Lead ▾]" or "Create new option". For dates, "Try DD/MM/YYYY instead" (jumps back to the format control).
- Warnings (non-blocking, row still imports) are shown separately from errors (row skipped): for example, "Phone number reformatted: 2,310 rows", "Value truncated: 0".

**Preview table:** Virtualised, 40px rows, showing the first rows of each category with filters for Created / Updated / Skipped / Warnings. Columns show mapped fields with errors highlighted in-cell (red text + icon + tooltip, never colour alone). For updates, a diff view displays "old → new" per cell on hover or in a row detail panel. Sticky header, horizontal scroll with a frozen first column, right-aligned numbers.

**Actions:**
- **Download error report (CSV)**: the original rows plus `error_row_number` and `error_reason` columns, so users can fix and re-upload just those.
- **Primary: "Import 46,322 contacts"** (the count is in the button label, reflecting what will actually be written, for example created plus updated).
- If any rows would be skipped, there's a non-blocking line above the button: "1,796 rows will be skipped. Download the error report to fix and import them later."
- If overwrite is chosen, a confirmation dialog: "Overwrite existing data for 5,114 contacts? Their current values will be replaced. You can undo this import for 30 days." with buttons **Cancel** and **Overwrite 5,114 contacts**.
- If more than 50% of rows are errors, the primary action requires an extra checkbox: "I understand most rows will be skipped."
- Secondary: **Back to mapping**, **Save draft and exit**.

### Step 5: Import progress

- A dedicated page with a determinate progress bar: "Importing… 18,400 of 46,322 (40%)", rate and estimated time ("about 2 minutes left"; no estimate shown for the first 10 seconds).
- Live counters: Created, Updated, Skipped.
- **The user can leave.** Copy: "You can close this page. We'll notify you when it's done." The import continues server-side. A global in-app indicator (a spinner chip in the top bar) links back to the progress page.
- **Cancel import** (secondary, with confirmation: "Stop importing? 18,400 contacts have already been added. They will stay, and you can roll back the whole import from the import history."). On cancel, state is "Cancelled – partially imported".
- The contacts list and reports shown to other users aren't blocked, but a banner on Contacts says "An import is in progress; new contacts may still appear."
- Processed in batches of about 500 rows, so partial progress is durable and retries are idempotent (no duplicate contacts if a batch is retried).

### Step 6: Results

- A status headline: "Import complete" (success), "Import complete with issues" (warning), or "Import failed" (error).
- Result summary: Created 41,208 · Updated 5,114 · Skipped 1,796 · Duration 3 min 12 s · Finished 27 Oct 2026, 14:32 UTC (absolute time with timezone; relative form in lists).
- Actions: **View imported contacts** (primary; opens Contacts filtered by this import's tag/ID), **Download error report**, **Re-import failed rows** (starts a new import prefilled with the error file and the same mapping), **Roll back import**, **Import another file**.
- **Roll back** (ghost/destructive): confirmation names the object and count: "Roll back this import? 41,208 contacts created by this import will be deleted. 5,114 updated contacts will be restored to their previous values. Contacts edited since the import (212) will be left as they are." Buttons: **Cancel** / **Roll back import**. It runs as a background job with its own progress and notification. Available for 30 days.

## 6. Import history page (`/contacts/imports`)

A table: File name · Status (icon + label) · Created / Updated / Skipped (right-aligned, tabular) · Imported by · Started (relative, absolute on hover) · Actions (⋯: View results, Download original file, Download error report, Roll back, Duplicate settings).
- Filters: status, user, date range. Sort by started date (default descending). State in URL. Pagination of 25 per page.
- Draft imports show a **Continue** action and an expiry date.
- Original files are kept for 30 days (admin-configurable) for audit, and the page says so.

## 7. States table

| View | State | Trigger | What the user sees | Actions available |
|---|---|---|---|---|
| Entry | No permission | Role lacks Import | Disabled **Import** button with tooltip naming who can grant access | Request access |
| Upload | Idle | First arrival | Drop zone, template, requirements | Choose file, download template |
| Upload | Drag-over | File dragged onto zone | Zone highlight, "Drop to upload" | Drop / leave |
| Upload | Uploading | File selected | Progress bar, name, size | Cancel |
| Upload | Parsing | Upload finished | "Reading file… 31,200 of 48,730 rows" | Cancel |
| Upload | Network failure mid-upload | Connection drop | Inline error "Upload interrupted at 62%. Your connection dropped." Auto-retries 3 times, then manual | Retry, Choose a different file |
| Upload | Rejected file | Size / type / row limit / corrupt | Specific error from table in §5 Step 1 plus fix | Choose a different file, Download split files |
| Upload | Encoding problem | Replacement characters (�) detected | Warning "Some characters look garbled. Try Windows-1252." with encoding selector and live preview | Change encoding |
| Map | Auto-mapped | Headers recognised | Table with "Auto" tags | Edit mappings, Continue |
| Map | Missing required | No Email mapping | Inline message at top and disabled Continue | Map a column |
| Map | Conflict | Two columns to one field | Red on both rows with message | Change one |
| Map | Field creation failed | Custom field create error | Inline error with reference ID | Retry |
| Review | Validating | Entering step | Determinate progress, "You can leave this page" | Leave, Cancel |
| Review | All clean | 0 errors | Green summary "46,322 rows ready to import" | Import |
| Review | Some errors | 1+ errors | Counts, grouped reasons, error report download | Fix rules, Download, Import valid rows |
| Review | All rows invalid | 0 importable | Error state "None of the 48,730 rows can be imported" with the top 3 reasons and a link to remap. Import disabled | Back to mapping, Download error report |
| Review | Validation service failed | 5xx / timeout | "We couldn't check your file. Your upload and mapping are saved. Reference IMP-8F2K1." | Retry, Contact support |
| Review | Stale | Draft is 7+ days old or contacts changed heavily | "Duplicate check is out of date" | Re-run check |
| Progress | Running | Confirmed | Determinate bar, counters, ETA | Cancel, Leave |
| Progress | Queued | Workspace at its concurrent limit | "Waiting to start — 2 imports ahead of yours" | Cancel, Leave |
| Progress | Slow / stalled | No progress for 60 s | "This is taking longer than usual. We're still working on it." after 5 min offers support link | Keep waiting, Cancel |
| Progress | Lost connection (client) | Offline | "Reconnecting… your import continues on our servers" | Auto-reconnects |
| Results | Success | All done | Success headline and summary | View contacts, Roll back, Import another |
| Results | Partial | Errors skipped | Warning headline with counts and error report | Re-import failed rows |
| Results | Failed | Server error mid-run | "Import stopped after 18,400 of 46,322. Those contacts were added; the rest were not. Reference IMP-8F2K1." | Resume from row 18,401, Roll back, Contact support |
| Results | Cancelled | User cancelled | "Cancelled – partially imported" with counts | Roll back, Resume |
| Results | Rolled back | After rollback | "Rolled back on 27 Oct 2026, 15:05 UTC by Dana Okafor" | View audit |
| Results | Rollback unavailable | 30 days passed | Disabled action with "Rollback is available for 30 days after import" | None |
| History | Empty | No imports | "No imports yet" with **Import contacts** | Import |
| History | Loading | Fetching | Skeleton rows | None |
| History | Load error | API failure | Inline error with Retry and reference ID | Retry |
| History | No results | Filters exclude all | "No imports match these filters" | Clear filters |
| Draft | Expired | 7 days | "This draft expired. Start a new import." | New import |
| Any step | Session expired | Auth timeout | Re-login modal that preserves state; draft is already saved | Sign in |
| Any step | Leave with unsaved step changes | Navigation | Dialog "Leave this import? Your file and progress are saved as a draft." | Stay, Leave |

## 8. Data-handling rules

- **Matching:** case-insensitive, trimmed email; plus-addressing is not collapsed. Phone matched after normalisation to E.164 using the selected default country.
- **Whitespace:** trimmed. Leading `=`, `+`, `-`, `@` in text cells is stored as-is but escaped on any CSV export (prevents formula injection).
- **Blank cells:** never overwrite existing values (unless "Update and overwrite" and the user ticks "Blank values clear existing data", off by default).
- **Dates:** parsed with the user-chosen format; ambiguous values (for example 03/04/2026) trigger a warning about the format selection, never silent guessing.
- **Limits:** text fields truncated? No. Over-length values are errors, never silently cut.
- **Duplicates within the file:** default "keep the last row", selectable ("keep first", "skip all duplicates").
- **Idempotency:** each import has a unique ID; retrying a batch never double-creates.
- **Audit:** every created or updated contact records `import_id`, source = "CSV import", and timestamp. Import records store who, when, file name and hash, settings and mapping, and counts.

## 9. Performance targets

| Action | Target |
|---|---|
| Show first preview after file select | Under 2 s for a 25 MB file |
| Full parse (50k rows) | Under 20 s |
| Dry-run validation | Under 60 s typical; progress shown, leave-able |
| Import throughput | 50k rows in under 5 min typical |
| Preview table | Virtualised; scroll stays 60 fps at 50k rows |
| Progress updates | Poll or push every 1–2 s |

## 10. Notifications

- In-app bell and optional email when: validation finished (if the user left), import finished, import failed, rollback finished.
- Email subject: "Your import of contacts-q4.csv finished: 41,208 created, 1,796 skipped". Includes a link to the results page and (if any) the error report link, which requires sign-in.

## 11. Accessibility & keyboard

- Full flow operable by keyboard. The drop zone is also a focusable button (Enter/Space opens the file dialog). Esc closes the field-creation panel and dialogs. Enter on a focused primary action proceeds.
- Stepper is `nav` with `aria-current="step"`. Progress bars use `role="progressbar"` with `aria-valuenow`, announced politely at 10% intervals through a live region. Completion and errors are announced assertively.
- Errors never rely on colour alone (icon + text + `aria-describedby` on the field).
- Preview table: proper table semantics when virtualised (`aria-rowcount`, `aria-rowindex`), visible focus, minimum 4.5:1 contrast.
- Respect reduced-motion for progress animation.

## 12. Copy guidelines

- Buttons are verbs with outcomes: **Import 46,322 contacts**, **Download error report**, **Roll back import**, **Continue to review**. Never "Submit", "OK" or "Next".
- Always give counts, never "some" or "many".
- Error format: what happened → why → what to do → reference ID for system failures.
- Avoid jargon: "Skipped" rather than "Rejected", "Matching contact" rather than "Duplicate record entity".

## 13. Out of scope / open questions

- Direct XLSX import (v2; for now the error tells users how to export CSV).
- Importing companies/deals in the same flow, and associating contacts to companies by name (v2).
- Scheduled / recurring imports from SFTP or cloud storage (v2).
- Open: do we dedupe against soft-deleted contacts? Recommendation: yes, offer "Restore deleted contacts that match" as a setting.
- Open: should reps without admin rights be allowed to overwrite? Recommendation: no, create-only or skip-existing.
- Open: retention period for uploaded files (default 30 days; confirm with legal for personal data).

## 14. Success metrics

- Import completion rate (started → finished) above 85%.
- Median time from upload to confirmed review under 4 minutes with saved mapping.
- Share of imports with 10%+ rows in error that are followed by a successful re-import of the error file.
- Rollback rate and support tickets tagged "import" (target: down 40% vs current).

---

## Audit summary

- **States:** every screen has empty/idle, loading, error, no-permission, overflow (too many rows, too large, too long) and partial-success states, listed in the states table in §7.
- **Safety:** nothing is written until a dry-run review with real counts. Overwrite requires explicit confirmation naming the count. Cancel and rollback confirmations name the objects and counts, and rollback is available for 30 days.
- **Input preservation:** drafts persist uploads, mappings and settings for 7 days. Failed validation and network errors never discard the file.
- **URL / keyboard / a11y:** each step has its own route, history and filters live in the URL, the flow is fully keyboard operable, progress is announced to assistive tech, and errors don't depend on colour.
- **Copy:** buttons are outcome verbs with counts. Errors state cause and next step with reference IDs. Timestamps are absolute with timezone on audit surfaces.
- **Not verified:** this is a spec, not a built screen. Throughput and timing targets in §9 are proposals to validate with engineering, and the permission roles in §3 need to be checked against the CRM's actual role model.
