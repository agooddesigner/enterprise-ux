# UX Spec: CSV Contact Import (up to 50,000 rows)

**Status:** Draft v1 · **Surface:** CRM → Contacts → Import

## 1. Job, user, frequency

- **Users:** Sales/RevOps admins and team leads migrating or bulk-loading lists (event leads, a previous CRM, a purchased list). Secondary: reps importing small lists (<500).
- **Job:** Get a messy spreadsheet into the CRM correctly, without creating duplicates or overwriting good data.
- **Frequency:** Weekly to quarterly. Not a daily task, so optimise for **guidance and safety over speed**. Users won't remember the flow, and mistakes pollute data other people rely on.
- **Success:** The user trusts the result. They know exactly what will happen before it happens, what did happen after, and how to reverse it.

## 2. Design principles

1. **Nothing is written until the user has seen a dry-run summary.** Counts of what will be created, updated, skipped and rejected come before the commit.
2. **Large imports are background jobs.** The user can close the tab. Nothing blocks the UI for 50k rows.
3. **Row-level errors never block valid rows.** Bad rows are rejected into a downloadable file. The rest can proceed, at the user's choice.
4. **Every import is undoable** for a limited window, and the limits of undo are stated up front.
5. **State lives in the URL and on the server.** Refresh, back, or switching devices never loses progress.

## 3. Scope and limits

| Item | Limit | Behaviour when exceeded |
|---|---|---|
| Rows | 50,000 data rows | Reject at upload: "This file has 62,310 rows. The limit is 50,000. Split the file and import in parts." Offer to import the first 50,000 only. |
| File size | 50 MB | Reject at upload with size shown. |
| Columns | 100 | Warn, ignore columns beyond 100 and list them. |
| Cell length | Per target field (e.g. Notes 5,000 chars) | Row-level validation error. |
| Concurrent imports | 1 running per workspace, others queued | Show queue position and estimate. |
| Format | `.csv`, `.tsv`, `.txt` (delimited). Not `.xlsx` in v1 | Say so: "Excel files: use File → Save As → CSV (UTF-8)." Link to template. |

Auto-detect: encoding (UTF-8, UTF-8 BOM, Windows-1252), delimiter (comma, semicolon, tab) and header row. Show the detected values and let the user override.

## 4. Entry points

- **Contacts list → "Import" button** (secondary action, top right next to "New contact"). Visible to users with `contacts.import`.
- **Contacts list empty state:** "Import from CSV" as co-primary beside "Add contact".
- **Contacts → Imports** history tab (see §10).
- Keyboard: none needed (infrequent task).

## 5. Flow overview

A single full-page wizard at `/contacts/import/:importId`. The `importId` is created at upload, so every step is a URL (`?step=map`), refreshable and shareable with a colleague who has permission. It is a page rather than a modal, because the content is dense and long-running.

Stepper: **1 Upload → 2 Map fields → 3 Rules → 4 Review → 5 Import**. Completed steps are clickable. Later steps are disabled until prerequisites are met. Footer is sticky: `Back` (left), primary action (right), `Cancel import` (text link, far left).

### Step 1: Upload

- Drop zone plus "Choose file" button. Beside it: "Download template CSV" and "Download sample with 3 example rows". Plain-language guidance: one row per contact, first row is headers, **Email** or **Phone** is recommended for matching.
- Upload goes straight to storage with chunked, resumable transfer. Show a progress bar with filename, size, MB/s, and `Cancel`. Interruption (wifi drop) resumes automatically and says so ("Connection lost. Resuming…").
- After upload, the server parses and returns: row count, detected encoding/delimiter, first 25 rows for preview, header list. Show a "Detected" line: `UTF-8 · comma-separated · 48,212 rows · 14 columns` with `Change` links.
- Checkbox "First row contains headers" (default on, auto-detected).
- Parse problems found here (unclosed quotes, inconsistent column counts, garbled characters from wrong encoding) show an inline banner with the first affected line numbers and an encoding picker. Example: "Some characters look garbled (e.g. 'MÃ¼ller'). Try Windows-1252 encoding." Picker re-parses the preview live.
- **Primary:** `Continue to mapping` (disabled until parse succeeds).

### Step 2: Map fields

Table with one row per CSV column (not per CRM field).

| CSV column | Sample values (first 3 non-empty) | Maps to CRM field | Status |
|---|---|---|---|
| `E-mail Address` | jo.alvarez@northwind.example, … | Email ▾ | ✓ Auto-matched |
| `Company` | Northwind Traders, … | Company ▾ | ✓ Auto-matched |
| `Lead Src` | Webinar Q3, Trade show, … | — Don't import ▾ | ⚠ Not mapped |

- Auto-match on exact and fuzzy header names plus content sniffing (emails, phones, dates). Show a confidence label, not just a tick.
- Field dropdown is searchable, grouped (Standard / Custom), and has "Create new custom field…" (permissioned) and "Don't import". A CRM field already mapped elsewhere is marked "Already used by *E-mail Address*". Selecting it again prompts to swap rather than silently double-mapping.
- Type-specific options appear inline once mapped: date format (auto-detected, with a preview of three parsed dates), multi-value separator for tags, picklist value matching (below).
- **Picklist fields** (e.g. Lifecycle stage, Country): show distinct CSV values found (up to 200) and how they map to CRM options, with "Create option", "Map to…", or "Leave blank".
- **Required to proceed:** at least one identity field mapped (Email, Phone, or both First+Last name). Otherwise inline message: "Map at least one of Email, Phone or Last name so contacts can be identified."
- Unmapped columns: a summary strip "3 columns won't be imported" with a link to filter them. Not an error.
- `Save this mapping as template` checkbox. A `Use saved mapping ▾` menu at top auto-applies when headers match a saved one.
- **Primary:** `Continue`.

### Step 3: Rules

Three decisions, each with a safe default and a plain explanation.

1. **When a contact already exists** (matched on [Email ▾] by default; can add Phone as a second key):
   - ◉ **Skip it** (default): existing record untouched.
   - ○ **Update it, only filling empty fields**
   - ○ **Update it, overwriting existing values** (shows an amber note: "Replaces current values with file values. Can be undone for 7 days.")
   - ○ **Create a duplicate anyway**
   - Also matching *inside the file*: duplicates within the CSV are detected. Rule: "keep the last row" (default) or "keep the first".
2. **Ownership:** Assign to [me ▾ / user / round-robin team / use *Owner Email* column]. Required.
3. **Tags and consent:**
   - "Add tag to every imported contact": text field, default `Import 2026-10-28 · {filename}`. This tag makes the batch findable.
   - Marketing consent: "Contacts in this file have consented to marketing email" ◯ Yes ◯ No ◉ Don't set. Choosing Yes requires a source description (compliance). Never defaults to Yes.
- **Primary:** `Check file` (runs the dry-run).

### Step 4: Review (dry run)

Server validates all rows **without writing** and streams progress ("Checking… 31,400 of 48,212 rows"). This usually takes seconds to a couple of minutes. Show a progress bar, estimated time, and `Cancel check`. The user may leave and get an in-app notification when it's ready.

Result summary (the key screen):

```
48,212 rows in file
 ├─ 41,870  will be created
 ├─  4,102  will be skipped   (already exist)
 ├─    ...  will be updated
 └─  2,240  have errors and won't be imported   [Download error file]
```

Present as a horizontal stacked bar with a labelled legend (never colour alone; each segment has a count and text label) plus the list above.

- **Errors panel:** grouped by reason with counts, e.g. "Invalid email format · 1,318 rows", "Required field Last name is empty · 612", "Value 'Platinum' is not a valid Tier · 310". Expand a group to see up to 50 example rows (row number, the offending value, the message). `Download all errors (CSV)` produces the original rows plus `row_number` and `error_reason` columns, so users can fix and re-upload just those.
- **Warnings (non-blocking):** e.g. "1,044 phone numbers will be reformatted to E.164", "212 rows have emails on a do-not-contact list; they'll import as Do not contact".
- **Preview table:** first 100 outcomes with filter chips (All / Create / Update / Skip / Error), showing the CRM value as it will be stored, so formatting changes are visible. Column order matches the mapping. Rows with changed values show old → new for updates.
- **Decision when errors exist:**
  - Primary: `Import 45,972 valid contacts`
  - Secondary: `Fix file and re-upload` (returns to step 1 keeping mappings and rules)
  - If errors exceed 50% of rows, default focus moves to `Fix file and re-upload`, and a banner warns: "More than half of rows have errors. Check the column mapping and encoding before importing." The import remains possible.
- If zero rows are importable, the primary is disabled and the message explains the most common cause and links to step 2.
- Confirmation is the button itself because it names the count. No extra "Are you sure?" modal. For the "overwrite" rule only, the button label includes it: `Import and overwrite 3,900 existing contacts`.

### Step 5: Import (progress)

- Starts a background job. Page shows a progress bar and counts (created / updated / skipped / failed), the elapsed time, and an ETA. Updates every 2s via polling or push. Screen-reader announcements are throttled (every 10% and on completion) via `aria-live="polite"`.
- Banner: "You can leave this page. We'll notify you when it's done." Provide `Go to Contacts` and `View all imports`. Also notify by email when finished if the job ran over 2 minutes (setting-controlled).
- `Cancel import` (confirm dialog): "Stop importing? 18,400 contacts already imported will stay. You can undo them from the import summary." Buttons: `Stop import` / `Keep importing`. Stopping is graceful: the current batch finishes.
- Contacts become visible in the list progressively, with the batch tag already applied. The Contacts list shows a non-blocking info bar: "Import in progress: 18,400 of 45,972 added." with a link.

### Completion screen

- Outcome headline with exact numbers: "Import complete: 45,972 created, 3,900 updated, 4,102 skipped, 2,240 failed." If failures happened, the icon is a warning, not a success tick.
- Actions: `View imported contacts` (primary; opens Contacts filtered by the batch tag via URL), `Download error file`, `Undo import`, `Import another file`.
- **Undo** (`Undo import…`): dialog states what it will do: "Delete 41,870 contacts created by this import and restore the previous values of 3,900 updated contacts. Contacts edited since import (212) will be left as they are." Confirmation button: `Undo import (41,870 deleted)`. Available 7 days. After that, the button is replaced with "Undo window ended on Nov 4. Delete by tag instead" linking to the filtered list (where normal bulk delete safeguards apply).

## 6. Imports history

`Contacts → Imports` is a table (dense, 40px rows): Name/file, Started (relative, absolute on hover), By, Status (Checking / Ready to review / Importing / Completed / Completed with errors / Cancelled / Failed / Undone), Created, Updated, Skipped, Failed (right-aligned, tabular figures), Actions (⋯: View, Download errors, Undo, Delete record).

- Filters: Status, User, Date range. Sort by Started descending. State in URL. Default page size 25.
- Drafts (uploaded but not committed) appear as "Ready to review" and `Resume` returns to the saved step. Drafts expire after 7 days. Uploaded files are deleted 30 days after completion (stated in UI).
- Admins see all imports. Others see their own.

## 7. States

| View | State | Trigger | What the user sees | Actions available |
|---|---|---|---|---|
| Upload | Empty | First visit | Drop zone, template links, guidance | Choose file, download template |
| Upload | Uploading | File selected | Progress bar, speed, filename | Cancel |
| Upload | Connection lost | Network drop | "Connection lost. Resuming…" inline, keeps progress | Cancel, Retry now |
| Upload | Wrong type | Non-CSV (e.g. .xlsx, .pdf) | "We can't read .xlsx files yet. In Excel choose Save As → CSV UTF-8." | Choose another file |
| Upload | Too large / too many rows | >50 MB or >50k rows | Specific numbers and limits, option to import first 50,000 | Choose another file, Import first 50,000 |
| Upload | Empty file / no data rows | 0 rows | "This file has a header row but no contacts." | Choose another file |
| Upload | Unparseable | Corrupt/binary | "We couldn't read this file as a table. Reference: IMP-8F3K2" | Choose another file, Contact support |
| Map | Auto-matched | Parse OK | Table with matches and confidence | Edit any mapping, Continue |
| Map | No identity field mapped | User unmaps Email | Inline error under table, Continue disabled | Fix mapping |
| Map | Picklist values unmatched | New values found | Value-mapping panel with count | Map, create, blank |
| Review | Checking | Click Check file | Progress bar, ETA, rows checked | Cancel check, leave page |
| Review | Clean | 0 errors | Summary without error panel | Import N contacts, Back |
| Review | Partial errors | Some invalid rows | Summary, error groups, download | Import valid rows, Fix and re-upload |
| Review | All rows invalid | Nothing importable | Primary disabled, likely-cause message | Back to mapping, Re-upload |
| Review | Check failed | Server error | "The check stopped at row 20,400. Nothing was imported. Reference: IMP-91XQ" | Retry check, Contact support |
| Import | Queued | Another import running | "Waiting for another import. Position 2." | Cancel, leave page |
| Import | Running | Job started | Live progress, counts, ETA | Cancel import, leave page |
| Import | Slow / stalled | No progress >60s | "Taking longer than usual. Your data is safe. We'll keep going." | Leave page |
| Import | Completed | Job done, no failures | Success summary | View contacts, Undo, Import another |
| Import | Completed with errors | Some rows failed at write time (e.g. race with another user) | Warning summary and error file | View contacts, Download errors, Retry failed rows |
| Import | Failed | System error | "Import stopped at 12,000 of 45,972. 12,000 contacts were imported. Reference: IMP-77AB" | Resume remaining, Undo, Contact support |
| Import | Cancelled | User stops | Summary of what was imported | Undo, View contacts |
| Import | Undoing | Undo confirmed | Progress as above | Leave page |
| Import | Undone | Undo done | Counts restored, edited-since list | Download skipped list |
| Any | No permission | Lacks `contacts.import` | Page-level message: "You don't have permission to import contacts. Ask a workspace admin (Dana Whitfield, Priya Raman)." Import button disabled with tooltip on list | Request access |
| Any | Read-only workspace / plan limit | Contact quota reached | "Your plan allows 100,000 contacts; this import would exceed it by 3,200." | Import fewer rows, Manage plan |
| Any | Session expired | Token timeout | Draft preserved server-side; sign-in prompt, returns to same step | Sign in |
| Any | Browser closed mid-wizard | — | Draft appears in Imports history as "Ready to review" | Resume |

## 8. Data integrity rules

- **Atomicity:** Processed in batches of 500 rows. Each batch is transactional. A failed batch retries twice, then its rows go to the error file with the reason "System error. Retry these rows".
- **Idempotency:** Each import has a unique ID. Double-clicking `Import` or reloading never starts a second job.
- **Normalisation (previewed in step 4):** trim whitespace, lowercase emails, phone to E.164 with a default country chosen in step 3 when the numbers have no country code, dates to the chosen format, de-duplicate multi-value tags.
- **Formula injection:** Cells beginning with `= + - @` are stored as text and escaped on export.
- **Audit:** Every created/updated contact records `source = Import`, import ID, user, and timestamp (UTC, displayed in user timezone) in its activity log. Field-level change history is retained for overwritten values (basis of undo).
- **Large-file performance targets:** upload+parse feedback within 5s for 50 MB; dry run ≤ 2 min for 50k rows; import ≤ 10 min. If estimates exceed this, the ETA is shown honestly rather than a spinner.

## 9. Accessibility and keyboard

- Wizard is fully keyboard operable. Stepper uses `aria-current="step"`. The drop zone is a real button that opens the file dialog on Enter/Space.
- Focus moves to the step heading on step change. Errors move focus to the first invalid control and are linked via `aria-describedby`.
- Status is never colour-only: each state has an icon and text label. Contrast ≥ 4.5:1.
- Progress uses `role="progressbar"` with value, plus throttled live announcements.
- Mapping table: dropdowns operable by typing to search. Row `Tab` order: select, then next row.
- `Esc` closes any dialog. Sticky footer never covers focused fields.

## 10. Copy guidelines

- Buttons are verbs with outcomes: `Continue to mapping`, `Check file`, `Import 45,972 contacts`, `Undo import`, `Download error file`. Never "Submit" or "OK".
- Always use numbers with thousands separators and the same unit across screens ("contacts", not sometimes "records").
- Errors: what happened → why → what to do → reference ID for system errors.
- Do not use "invalid" alone. Say which field and what was expected ("Email must look like name@company.com").

## 11. Analytics and success measures

- Funnel by step (upload → map → rules → review → commit) and drop-off reasons.
- % of imports using auto-mapping unchanged, % with error files downloaded, % re-uploaded after fix.
- Undo rate within 24h (a proxy for surprised users; target < 3%).
- Duplicate rate created per import (target ≈ 0 under default rules).
- Support tickets tagged "import" per 1,000 imports.

## 12. Open questions

1. Do we need `.xlsx` in v1? Likely the top support request, but parsing adds scope. Recommend phase 2.
2. Should the 7-day undo window be configurable by admins? Undo storage cost grows with overwrite imports.
3. Is round-robin owner assignment in scope for v1, or only a single owner or an owner column?
4. Compliance: do we require a consent source description for every import, or only for marketing-consent = Yes? (Legal to confirm.)
5. Can reps (non-admins) import, and with a lower row cap (e.g. 5,000) pending admin approval?
6. Custom-field creation from the mapping step: allowed for all importers, or admins only?

## 13. Audit summary

- **States:** every step has empty, loading, error, partial and permission states (§7), including the failure modes specific to large files (resume on network loss, stalled job, partial failure).
- **Safety:** nothing is written before a dry-run summary. Overwrite is opt-in and named on the button. Cancel and undo state their exact effect and count. Undo limits (7 days, edited-since records) are disclosed.
- **Scale:** server-side parse, validation and import. The browser only holds a 25-row preview, so a 50k-row file doesn't freeze the UI. The user can leave the page.
- **Input retention:** drafts, mappings and rules persist server-side and in the URL, and "Fix and re-upload" retains previous settings.
- **Not verified:** no usability testing yet, and the performance targets in §8 need engineering confirmation.
