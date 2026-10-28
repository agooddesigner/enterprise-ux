# UX Spec: CSV Contact Import (up to 50,000 rows)

## 1. Goals and non-goals

**Goals**
- A user can import up to 50,000 contacts from a CSV without engineering help.
- Problems are found before anything is written to the CRM, and the user can fix them.
- The import runs in the background, so the user can keep working.
- The result is clear: what was created, updated, skipped and failed, with a way to fix and retry failures.

**Non-goals (v1)**
- Excel (.xlsx) or Google Sheets import.
- Importing companies, deals or other objects.
- Scheduled or recurring imports.
- Cross-field transformations beyond basic normalization.

**Primary users:** sales ops, marketers and admins migrating or bulk-adding contacts. Most have little technical background.

## 2. Entry points and permissions
- **Contacts list → "Import"** button, next to "Add contact".
- **Empty state** of the Contacts list, with "Import from CSV" as the primary action.
- Only roles with *Import contacts* permission see it. Others see it disabled, with a tooltip: "Ask an admin for import access."
- Only one import per workspace runs at a time. A second import is queued, and the UI says so.

## 3. Flow overview

A five-step wizard in a full-page modal, with a persistent stepper: **Upload → Map fields → Options → Review → Import**. Users can go back to any earlier step without losing input. Closing the wizard before step 5 asks for confirmation and keeps a draft for 7 days.

### Step 1: Upload
- Large drop zone with a "Choose file" button.
- Helper text: ".csv up to 50,000 rows and 100 MB. UTF-8 recommended."
- Links: **Download template** and **How to format your file**.
- **Client-side checks, instant:**
  - File type is not .csv: "This isn't a CSV file. Export your sheet as CSV and try again."
  - File over 100 MB: "File is too large (limit 100 MB)."
  - Empty file: "This file has no data."
- **Parsing and upload:**
  - The file uploads with a progress bar and a Cancel button.
  - The server auto-detects delimiter (comma, semicolon, tab) and encoding, and handles BOM and quoted line breaks.
  - After parsing, show a summary: filename, row count, column count, detected delimiter. Show a 5-row preview.
  - If the delimiter or encoding is wrong, the user can override it from a "File settings" link.
- **Over the row limit:** block with a clear message: "Your file has 61,204 rows. The limit is 50,000. Split the file and import in parts." Offer a **Download first 50,000 rows** action.
- **Header row:** on by default. A toggle says "First row contains column headers". Turning it off labels columns "Column A, B, C…".

### Step 2: Map fields
A table with one row per CSV column:

| CSV column | Sample values (first 3) | Maps to | Status |
|---|---|---|---|

- **Auto-mapping** by fuzzy-matching header names ("E-mail", "email address" → Email). Each auto-mapped row shows a "Matched" tag so the user knows it was inferred.
- The **Maps to** dropdown is searchable and grouped by Standard fields, Custom fields and Actions:
  - *Don't import this column* is the default for unmatched columns.
  - *Create new custom field…* opens an inline popover for name and type (text, number, date, dropdown, checkbox).
- **Required fields:** a banner at the top lists required fields that are not yet mapped (at minimum, *Email* or *Phone*; configurable per workspace). The Next button is disabled until they are mapped, with a reason shown beside it.
- **Duplicate mapping:** two columns mapped to one field shows an inline error. Exception: multiple columns may map to "Notes" and are concatenated.
- **Type conflicts:** if sample values don't fit the field type (for example, text in a date field), show a warning chip on that row. Hovering reveals the details.
- **Date columns:** show a format selector (MM/DD/YYYY, DD/MM/YYYY, ISO) with the detected format preselected and a live preview of how the samples will read.
- **Remember mapping:** a checkbox saves this mapping as a template. Next time, the user can pick "Use saved mapping."

### Step 3: Options
- **Duplicate handling.** Contacts are matched on email (primary). Phone is an optional secondary match key, selectable here.
  - *Skip duplicates* (default)
  - *Update existing contacts*. A sub-option controls whether blank CSV cells overwrite existing values. It defaults to **no**, and the text explains the effect.
  - *Create duplicates anyway*
- **Duplicates inside the file:** the last row wins, and a note says so. These rows are counted separately in the review.
- **Assign owner:** the importing user (default), a specific user, or a column from the file.
- **Add tags / add to list:** optional. Tags applied to this batch make it easy to find or roll back later.
- **Lifecycle stage / source:** defaults can be set. Source defaults to "CSV import, <date>".
- **Consent attestation (required where relevant):** a checkbox reads "I confirm I have permission to contact these people." It is required for marketing-enabled workspaces and recorded in the audit log.
- **Notifications:** "Email me when the import finishes" is on by default.

### Step 4: Review (validation before commit)
The system validates the entire file server-side before writing any data. The user sees a progress indicator, which typically takes under 60 seconds for 50,000 rows. They can leave and come back, and a notification fires when it's ready.

**Summary cards:**
- Will be created: N
- Will be updated: N (only when "Update" is chosen)
- Will be skipped as duplicates: N
- Rows with errors: N
- Rows with warnings: N

**Issue types:**
- *Errors* (the row is not imported): invalid email format, missing required field, value too long, invalid option for a dropdown field.
- *Warnings* (the row is imported, with auto-fix): extra whitespace trimmed, phone reformatted, name case normalized, unrecognized country mapped to blank.

**Issue table:**
- Grouped by issue type with counts, for example "1,204 rows: Invalid email format".
- Expanding a group shows affected rows (row number, field, value, message), paginated and virtualized.
- Filters: errors/warnings, column.
- **Download error report (CSV):** the original rows plus an "Error" column. Users can fix this file and re-import it directly.

**Decision rule:**
- If there are zero valid rows, the Import button is disabled.
- If any rows have errors, the primary action is **Import N valid rows**. Secondary actions are **Back** and **Download error report**. The button text states the number plainly so there are no surprises.
- A safety threshold: if more than 30% of rows have errors, show a prominent callout, "Most rows have problems. Check your column mapping?", with a shortcut back to step 2. The user can still proceed.

**Final confirmation:** a summary line above the button reads, for example, "42,310 contacts will be created, 1,500 updated, 6,190 skipped. This can be undone for 30 days." The user clicks **Start import**.

### Step 5: Import progress and results
- **In progress:**
  - A progress bar shows percent and counts ("18,400 of 43,810 processed"), plus an estimated time remaining once at least 10% is done.
  - Copy: "You can close this window. The import will keep running."
  - **Run in background** closes the wizard. A persistent chip in the app header shows live progress and links back to the import.
  - **Cancel import** stops processing. Rows already written stay, and the user is told how many. The button asks for confirmation.
- **Completion:**
  - A summary shows Created, Updated, Skipped and Failed counts.
  - Primary action: **View imported contacts**, which opens the contacts list filtered by this import's batch tag or ID.
  - Secondary actions: **Download failed rows** and **Import another file**.
  - An in-app toast and an email (if opted in) report completion.
- **Partial or total failure** (for example, a server fault mid-way):
  - State plainly what happened: "Import stopped at row 21,400. 21,399 contacts were saved."
  - Offer **Resume import**, which skips processed rows, and **Download unprocessed rows**.

## 4. Import history
- **Contacts → Import history** lists the date, user, filename, status, and counts of created, updated, skipped and failed.
- Each row opens a detail view: settings used, mapping, error report download, and the contacts list filtered to that batch.
- **Undo import** (admins or the importer): removes contacts *created* by that batch. It does not revert updates, and the confirmation says so. Undo is available for 30 days. Contacts edited since import are listed in the confirmation, and the user chooses to keep or delete them.
- Uploaded files and error reports are retained for 30 days, then purged. The UI says so.

## 5. Performance and system behavior
- Upload: chunked and resumable. A dropped connection resumes rather than restarting.
- Validation and import run as background jobs, not tied to the browser session.
- Target processing rate: 50,000 rows in under 10 minutes. Show a realistic time estimate rather than a fake spinner.
- Preview and error tables are server-paginated and virtualized. The browser never loads all 50,000 rows.
- Rate-limit writes so the import doesn't degrade CRM performance for other users. Large imports may be throttled, which the progress estimate accounts for.
- The wizard state is saved server-side, so a refresh or tab close doesn't lose the user's place.

## 6. Error and edge-case handling

| Situation | Behavior |
|---|---|
| Wrong encoding (garbled characters in preview) | Warning above the preview with an "Encoding" selector: "Characters look wrong? Try a different encoding." |
| Ragged rows (inconsistent column counts) | Rows are flagged as errors in review with the message "Expected 12 columns, found 9." |
| Duplicate header names | Auto-suffixed ("Email", "Email (2)") and mappable independently |
| Header only, no data | "This file has headers but no contacts." |
| Formula injection (cells starting with `=`, `+`, `-`, `@`) | Stored as plain text. The leading character is preserved, and the content is neutralized on any later export. |
| Another import running | Notice with a link to it, and this one queues. |
| Session expires mid-import | The job continues server-side, and the user sees progress after re-login. |
| Network loss in the wizard | A non-blocking banner, "Reconnecting…", with automatic retry. No data is lost. |
| User lacks permission to create a custom field | The "Create new field" option is hidden, with a help tooltip. |
| Unsubscribed or do-not-contact emails in the file | A warning count in review. They are imported with marketing opt-out preserved or set, per workspace policy. |
| Contact limit of the plan exceeded | Block at review: "Importing this would exceed your plan's 100,000 contact limit by 3,200." Offer to download a trimmed file or contact sales. |

## 7. Content and tone
- Plain language with no jargon ("rows" and "columns", not "records" and "fields" in file context).
- Every error says what happened, where, and what to do.
- Use exact numbers rather than "some" or "many".
- Button labels are verbs and outcomes: "Import 42,310 contacts", not "Submit".

## 8. Accessibility
- Fully keyboard operable: drop zone, dropdowns, tables and the stepper.
- Progress bar uses `role="progressbar"` with live-updated values. Status changes (upload complete, validation done, import finished) are announced through an `aria-live="polite"` region.
- Errors are never conveyed by colour alone. They have an icon and text.
- Mapping dropdowns are searchable and use a proper combobox pattern.
- Tables have row and column headers and sticky headings. Contrast meets WCAG 2.2 AA.
- Respect `prefers-reduced-motion` for progress animations.

## 9. Analytics (instrument)
- Funnel: started → file uploaded → mapping completed → review reached → import started → completed.
- Drop-off per step, time per step, and median file size.
- Auto-mapping accuracy (the percentage of columns the user changed).
- Error categories by frequency, to inform better messages and validation.
- Rate of error-report downloads followed by a re-import, which shows whether the fix loop works.
- Undo usage.

## 10. Success metrics
- **Completion rate** (started → import finished): ≥ 75%.
- **Median time** to import a clean file: under 3 minutes of user effort.
- **Support tickets** about imports: down 50% from the current baseline.
- **Auto-map accuracy:** ≥ 85% of columns left unchanged by the user.
- **Post-review abandonment** with errors present: under 15%.

## 11. Open questions
1. What is the default required-field rule (email only, or email or phone)? Should it be configurable?
2. Is phone matching allowed for deduplication in v1, given format-normalization complexity?
3. Should "Update existing" support field-level rules (for example, only fill blanks)?
4. What is the legal and compliance stance on the consent attestation by region (GDPR, CASL)?
5. Is the 30-day undo window acceptable given downstream automations that may already have triggered on imported contacts? Should imports suppress workflow triggers by default?
6. Do we need an API or webhook for import completion for integrators?

If you want, I can turn this into a Figma-ready screen list, add wireframes, or write acceptance criteria per step.
