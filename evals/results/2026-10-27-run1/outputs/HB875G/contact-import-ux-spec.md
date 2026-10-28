# UX spec: CSV contact import (up to 50,000 rows)

Status: draft v1. Assumptions in §1 need confirming before build.

## 1. Job, users, assumptions

**Job:** get an existing list of contacts into the CRM correctly, without creating duplicates or overwriting good data, and know exactly what happened.

| User | Frequency | Need |
|---|---|---|
| Sales/marketing ops (primary) | Weekly to monthly, 1k–50k rows | Speed, repeatability, a trustworthy result |
| Rep (secondary) | Occasional, 50–500 rows (event lists) | Guidance, low risk |
| Admin | Rare | Control over who can import; audit trail |

**Assumptions (confirm):**
1. Import is permission-gated (`contacts.import`); reps may have it, viewers do not.
2. Duplicate key is email by default. Admins can add a secondary key (external ID).
3. Max file is 50,000 data rows and 50 MB. XLSX is not supported in v1 (CSV only, UTF-8, auto-detected delimiter).
4. Custom fields exist and can be mapped. Creating new custom fields during import is out of scope for v1.
5. An imported batch can be undone for 7 days (see §9). This is the main safety net.
6. Contacts may carry consent/marketing-opt-in flags. Imports must not silently opt people in.

## 2. Principles

- **Never silently drop or change rows.** Every row ends as created, updated, skipped or failed, and the totals add up to the file.
- **Validate before commit.** Nothing is written until the user reviews a summary and confirms.
- **Fix errors without leaving the flow.** A bad row is never a reason to reject the file.
- **Long work runs in the background.** The user can leave and is notified.
- **Undo beats confirm.** The commit is reversible, so the confirm step is light. Overwriting existing data is the exception and gets explicit confirmation.

## 3. Entry points and URL

- Contacts list: primary toolbar menu **Import** (the page's "New contact" stays the primary action).
- Empty contacts list: empty state with "Import contacts" and "Add a contact".
- Command palette: "Import contacts".
- Route: `/contacts/import` for the wizard, `/contacts/imports` for history, `/contacts/imports/:id` for one job. Step state is in the URL, so refresh and back work and a job link can be shared.

## 4. Flow overview

A five-step wizard, with a persistent step indicator and a Back button on every step. Steps 1–4 are cheap and happen in the browser or on a draft server-side upload. Only step 5 writes data.

1. **Upload**
2. **Map columns**
3. **Review and fix**
4. **Import options**
5. **Confirm and run**, followed by **Progress** and **Result**

If the user has a saved mapping that matches the file, steps 2 and 3 are prefilled and the user can jump to step 5 ("Use saved mapping 'HubSpot export'").

### Step 1: Upload

**Layout:** a single drop zone plus "Choose file" button (the button is the keyboard and screen-reader path). Beside it, a requirements panel:

- Format: CSV, UTF-8. Max 50,000 rows / 50 MB.
- Required: at least one of Email or External ID.
- "Download CSV template" (headers plus 2 example rows) and "See field reference".

**Behaviour:**
- Show filename, size and a determinate upload bar with Cancel.
- After upload, parse a preview server-side: row count, detected delimiter and encoding, header row guess. Show: "47,213 rows, 14 columns. First row looks like headers." with a toggle "First row is not a header".
- If the encoding looks wrong (mojibake) show the detected encoding with a picker.
- Files over limits are rejected before upload where possible, with a specific message and a suggested fix, e.g. "This file has 63,410 rows. The limit is 50,000. Split it into 2 files, or ask your admin about bulk loading." Never "Invalid file".
- Empty file, header-only file, binary file, and corrupt quoting each get their own message.
- Large-file note: "Files over 10,000 rows are processed in the background."

**Primary action:** "Continue" (enabled once the file is parsed).

### Step 2: Map columns

A table, one row per CSV column.

| CSV column | Sample values (first 3 non-empty) | Maps to | Status |
|---|---|---|---|

- Auto-suggest the target field from header name and synonyms ("E-mail", "Email Address", "Company Name" → Company) and by sniffing values. Show a confidence cue as text ("Suggested"), not colour alone.
- "Maps to" is a searchable select with groups: Standard fields, Custom fields, "Don't import this column".
- A target field can be mapped once. Choosing a taken field offers to move the mapping.
- A summary above the table: "12 of 14 columns mapped. 2 will be ignored. Required: Email ✓".
- Required-field gaps block Continue with an inline reason next to the missing field and a link to the unmapped column that might fit.
- Enum fields (Country, Lifecycle stage, Lead source, Owner): after mapping, an expandable "Match values" panel lists distinct file values against allowed values ("USA", "U.S.", "United States" → United States). Unmatched values can be mapped, left blank, or (for fields that allow it) added as new options if the user has permission. Unmatched is a count, e.g. "3 unmatched values affect 212 rows".
- Owner by email or name: unmatched owners default to "importing user", stated explicitly.
- "Save this mapping" checkbox with a name, on by default. Saved mappings appear as a select at the top of this step.

**Primary action:** "Continue to review".

### Step 3: Review and fix

Runs validation on all rows (server-side, chunked), with a progress indicator ("Checking 31,000 of 47,213 rows") and Cancel. The user can leave a long validation and come back (it is a job; see §7).

**Summary header (the decision point):**

> 47,213 rows checked. **44,870 ready · 1,903 will update existing contacts · 440 have errors**

with segmented filter controls: All · Ready · Will update · Errors · Warnings. Filter state is in the URL.

**Error and warning taxonomy:**

| Type | Examples | Default treatment |
|---|---|---|
| Error (row won't import unless fixed) | Invalid email format, missing required value, unmatched required enum, value too long | Row is skipped at import |
| Warning (row imports, data changed) | Phone normalised, trailing spaces trimmed, date format guessed, enum blank | Imported, change listed |
| Duplicate in file | Same email on rows 12 and 3,401 | Warning; policy chosen in step 4 |
| Matches existing contact | Email exists in CRM | Counted as "update", policy in step 4 |

**Review grid:**
- Virtualised table, so 50,000 rows scroll smoothly. Columns are the mapped fields, plus Row # and Status. 32px rows (data-heavy review tool), a density toggle is available.
- Cells with problems are marked with icon + text in a tooltip/popover, not colour alone. Error cell text example: "Row 37, Email: 'jane@acme' is missing a domain extension (like .com)."
- Inline edit any cell; edits revalidate that row immediately and update the counters. Edits are kept in the draft and apply to the import only (the source file is not changed).
- **Fix in bulk** for common patterns: "Find and replace in column", "Trim whitespace", "Skip all rows with errors", "Fix 118 phone numbers to +1 format" (shows a before/after sample before applying). Bulk fixes are undoable within the step.
- Sort by status; "Next error" / "Previous error" buttons (keyboard: `]` and `[`) jump through problems.
- **Download error report (CSV)**: original rows that fail, with `row_number`, `column`, `error` and `how_to_fix` columns, so the user can fix them in a spreadsheet and re-upload only those.
- Duplicates-in-file are grouped so the user can see both rows side by side.

**Primary action:** "Continue" is always available. If errors remain, the button label stays "Continue" and the next step states clearly that error rows will be skipped. Do not disable Continue to signal errors.

### Step 4: Import options

Short form, sensible defaults, each with a one-line consequence.

1. **When a contact already exists (matched by email):**
   - **Update only empty fields** (default, safest)
   - Overwrite with file values (only for mapped, non-empty columns)
   - Skip existing contacts
   Shows the live count affected: "1,903 contacts match".
2. **Duplicates inside the file:** Use the last row (default) · Use the first row · Skip all duplicates.
3. **Assign owner:** "Owner column from file" if mapped, otherwise a select (default: me).
4. **Tag this import:** an auto-generated tag "Import 2026-10-27 · contacts.csv" that is editable. It allows filtering and rollback later. Always applied.
5. **Consent / marketing status** (only if the CRM tracks it): "Imported contacts are marked **Not opted in** unless the file has a consent column mapped. Confirm you have permission to contact these people." Checkbox attestation, unchecked, required only when a consent column is mapped to opted-in values.
6. **Notifications:** "Email me when this finishes" (default on for >10,000 rows).
7. **Run workflows/automations on imported contacts:** off by default, with a hint: "Turning this on may send emails to up to 44,870 people." Prevents a 50k-person accidental blast.

### Step 5: Confirm and run

A plain summary the user can read in 5 seconds, not a modal.

> **Ready to import `contacts.csv`**
> Create **44,870** new contacts · Update **1,903** existing · Skip **440** rows with errors
> Matching on email · Existing contacts: update empty fields only · Tagged "Import 2026-10-27 · contacts.csv"
> Automations will not run. You can undo this import for 7 days.

- Primary: **Import 46,773 contacts** (specific verb and count). Secondary: Back. Tertiary: "Save as draft".
- If "Overwrite" is chosen, the summary states "Overwrites existing values on 1,903 contacts" with a warning icon, and the button needs one extra checkbox: "I understand existing values will be replaced." (Reversible via undo, so no typed confirmation.)
- If skipped rows exceed 20% of the file, add a warning line: "9,500 rows (20%) will be skipped. Review errors?" with a link back to step 3.

## 5. Progress (the 50k case)

After confirm, navigate to the job page `/contacts/imports/:id`. Never block the UI with a modal.

- Determinate progress: "Importing… 18,400 of 46,773 (39%)", plus stage labels (Validating → Writing → Indexing) and a rough time remaining once stable. Pre-estimate is shown on step 5 for big files ("About 3 minutes").
- Cancel: "Stop import". Stopping keeps what's already written, says so ("18,400 contacts were already created. Undo them?"), and offers Undo import.
- The user may close the tab or navigate. A persistent, dismissible "Import running" indicator appears in the app shell (a jobs/activity area) linking back here. Progress is server-side and survives refresh.
- On completion: in-app notification, plus email if opted in. The browser tab title updates ("Import complete").
- The progress region is announced to screen readers politely at 10% steps (`role="progressbar"` with values, plus a live region `aria-live="polite"`; not on every tick).
- Concurrency: one active import per workspace by default. Starting a second shows "An import is already running (started by Sam, 40%). You can queue yours or wait." Offer Queue.

## 6. Result

Same page when the job ends. Heading states the outcome in words.

> **Import finished with 440 rows skipped**
> Created 44,870 · Updated 1,903 · Skipped (duplicate action) 0 · Failed 440
> Totals: 47,213 rows in file = 47,213 accounted for.

Actions:
- Primary: **View imported contacts** (opens the contact list filtered by the import tag, URL-shareable).
- **Download error report** for failed rows (re-uploadable as-is).
- **Download full results** (every row with outcome and created/updated contact ID).
- **Undo import** (see §9).
- **Import failed rows** shortcut: starts a new import prefilled with the error file and saved mapping.

States: Succeeded · Succeeded with skipped rows · Failed (nothing written) · Partially failed (system error mid-run, with what was written and a Retry remaining rows button) · Cancelled · Undone.

## 7. Import history

`/contacts/imports`: a table (job, file name, user, started, duration, status, created/updated/failed counts). Default sort by started descending; absolute timestamps with time zone (audit-style data). Filter by status and user. Row click opens the job page. Drafts and in-progress validations appear here and can be resumed or discarded. Retain job records and error reports for 90 days, stated on the page.

## 8. States and edge cases

| Situation | Behaviour |
|---|---|
| No permission | Import hidden from users who can never import. If the role could request access: item disabled with "Ask an admin for import access" and a link. |
| Another import running | See §5 concurrency. |
| Upload interrupted (network) | Resume if supported, else a clear retry; the selected file is kept in the control. |
| Browser closed during validation or import | Job continues server-side; on return the wizard resumes at the right step. |
| Session expires mid-wizard | Draft is saved server-side; after re-login the user returns to the same step. |
| Workspace contact limit would be exceeded | Detected at step 3/5: "This import would exceed your plan limit by 3,100 contacts." Options: remove rows, upgrade (link, non-pushy), cancel. No partial surprise failures. |
| API rate limit / downstream sync failures | Rows still import; sync failures surface as a separate count with retry. |
| All rows error | Step 5 primary disabled with visible reason: "No valid rows to import. Fix errors in the previous step." (Valid prerequisite-based disable.) |
| Zero rows after filtering in review | "No rows match this filter" + "Clear filters". |
| Leaving the wizard with unsaved edits | "Leave import?" dialog: Stay (default) / Save as draft / Discard. Draft autosaves at each step transition. |
| Very long values, emoji, RTL names, leading zeros in phone/ZIP | Preserved as text; phone/ZIP never coerced to numbers. Long cell values truncated with full text in popover. |
| Formula-injection values (`=`, `+`, `-`, `@` prefixes) | Stored as plain text; flagged as a warning; escaped in any export. |
| Sensitive data | Uploaded files encrypted at rest and deleted after the retention period; import events written to the audit log (who, when, file name, counts). |

## 9. Undo

- "Undo import" is available on the result page and history for 7 days.
- Dialog names the consequence: "Undo 'Import 2026-10-27'? This deletes 44,870 contacts created by this import and restores 1,903 contacts to their earlier values. Changes made to these contacts since the import (by anyone) will be lost for 212 contacts." Offer "View the 212 changed contacts" before confirming.
- Primary button: "Undo import". Default focus on Cancel. No typed confirmation, since it is the reverse of a reversible action, but the 212-edited warning gives the user the information to decide.
- Undo runs as a background job with the same progress and result pattern.
- After 7 days, the action is replaced by text: "Undo is no longer available. Delete these contacts by filtering on tag ...".

## 10. Writing

Sentence case. Specific verbs. No "Oops", "Invalid", "Success!".

| Where | Copy |
|---|---|
| Wizard title | Import contacts |
| Drop zone | Drop a CSV file here, or choose a file |
| Missing required field | Map a column to Email or External ID to continue. |
| Row error | Row 37, Email: "jane@acme" is missing a domain ending, like .com. |
| Phone warning | Phone number reformatted to +1 415 555 0100. |
| Step 5 primary | Import 46,773 contacts |
| Completion toast not used | Outcome is shown on the page; a toast would duplicate it. Notification centre carries the completion message when the user left. |
| Empty history | No imports yet. Import a CSV to add many contacts at once. [Import contacts] |

## 11. Accessibility (WCAG 2.2 AA)

- Wizard is a single page with `h1` + step list (`ol`, `aria-current="step"`). On step change, focus moves to the step heading and the step title is announced.
- Drop zone has an equivalent visible "Choose file" button; drag is never the only path (2.5.7).
- Review grid: real `table`/`grid` semantics with virtualisation announcing total row count (`aria-rowcount`, `aria-rowindex`); cell edit via Enter, Esc cancels; all error cells have text, not colour-only (1.4.1); error summary reachable by keyboard; target size ≥24px (2.5.8).
- Validation and progress updates use polite live regions; completion uses a status message (4.1.3). No auto-moving focus during background updates.
- Focus is never hidden behind sticky headers/footers (2.4.11).
- The mapping table is fully operable by keyboard: select controls are native or APG combobox-compliant.
- Don't rely on hover for error details; offer a focusable "Why?" control.
- Respect reduced motion for progress animations.

## 12. Performance targets

- Upload feedback within 100 ms of file selection; parse preview of the first 100 rows in under 2 s for 50 MB.
- Mapping step interactions under 100 ms; sample data comes from the preview, not a re-parse.
- Full validation of 50,000 rows in under 60 s with live counters; review grid scrolls at 60 fps via virtualisation (render ~50 rows); filters on status run server- or index-side, not by scanning in the main thread.
- Import throughput target ≥ 500 rows/s, so the 50k worst case finishes in about 2 minutes; show a pre-estimate and update it from actual throughput.
- Writes in chunks of 5,000 rows; each chunk is idempotent so retries cannot create duplicates.

## 13. Analytics and success metrics

- Import completion rate: started → confirmed (target ≥ 80%).
- Drop-off by step; time on mapping and review steps.
- Share of imports with auto-suggested mapping accepted unchanged.
- Rows failed per import; top 10 error types (feeds validation copy and template improvements).
- Undo rate (a high rate signals unclear options or defaults in step 4).
- Support tickets tagged "import" (target: down 40% after launch).
- Repeat use of saved mappings.

## 14. Out of scope for v1 (parked)

XLSX and Google Sheets sources; scheduled/recurring imports; creating custom fields during mapping; importing related objects (companies, deals) in the same file; API-level bulk import (separate spec).

## 15. Open questions

1. Is a 7-day undo technically feasible (soft-delete and field-history storage cost for 50k rows)? If not, step 5 needs a stronger confirm and the default policy must stay "update empty fields only".
2. Which consent/legal attestation text is required (GDPR, CAN-SPAM, CASL) and by whom is it approved?
3. Should reps be limited to a smaller row cap than ops/admins?
4. Who is notified when someone else's import is running or finishes (workspace admins)?
5. Is one active import per workspace acceptable for large customers, or do we need per-user queues?
