# UX spec: CSV contact import (up to 50,000 rows)

Status: draft v1 · Pattern basis: Flatfile/Dromo import flow, enterprise-ux defaults. If the CRM's design system conflicts with a default here, the design system wins.

## 1. Purpose and assumptions

**Job:** A sales-ops admin or rep moves contacts from a spreadsheet or old tool into the CRM, correctly, without creating duplicates or corrupting existing records. Typical use: a few times a month, with an occasional one-off migration at the 50,000 ceiling. Frequency is low, so favour guidance over speed. The user is anxious about damaging live data.

**Assumptions (confirm before build):**
- A contact is identified by **email** as the primary match key. Optional secondary key: external ID.
- Import can **create and update** (user chooses). Default is create new and skip matches.
- Fields: standard (name, email, phone, company, title, address, owner, lifecycle stage, source) plus custom fields.
- Max file size 50 MB, 50,000 data rows, UTF-8 and common legacy encodings, CSV only in v1 (XLSX is a fast-follow; copy says "Export as CSV" until then).
- Server processing is asynchronous. The browser can be closed after the commit step.
- Imports can be **rolled back** for 7 days (see 6.7). If engineering can't support this, the commit-step confirmation becomes stricter (see 6.5 note).
- Roles: Admin and Manager can import. Rep can import only if the admin enables it, and only as owner of the records. Viewer cannot import.

**Success metrics:** import completion rate (started → committed); % of imports with zero failed rows; median time to complete mapping; support tickets tagged "import"; duplicate-creation rate post-import.

## 2. Entry points and layout

- **Contacts list** → page-level secondary button "Import contacts" (beside "Add contact", which stays the primary action). Also in the ⋯ menu and the command palette ("Import contacts").
- **Contacts empty state (first use):** "No contacts yet" with two actions: primary "Import contacts", secondary "Add contact".
- **Settings → Data → Imports:** the history list (section 7).

The flow is a **full-page wizard** at `/contacts/import/:importId`, not a modal. It has 5 steps, a persistent stepper (non-interactive for future steps, interactive for completed ones), and a draft that autosaves server-side so a refresh or return later resumes. The step is in the URL (`?step=map`). Only one primary action per step. Cancel is a text link, never primary.

| Step | Primary action | Back |
|---|---|---|
| 1 Upload | Continue (enabled after a valid file) | — |
| 2 Map columns | Continue to review | Yes |
| 3 Review and fix | Continue to import | Yes |
| 4 Confirm and import | Import 48,213 contacts | Yes |
| 5 Progress and result | Go to imported contacts | — |

## 3. Step 1: Upload

**Layout:** Requirements panel above the dropzone: accepted format (.csv), max 50,000 rows and 50 MB, required column (Email), UTF-8 recommended. Link: "Download CSV template" and "Download example file".

**Dropzone:** Drag and drop plus a real "Choose file" button (the click path is mandatory, WCAG 2.5.7). One file at a time.

**Import options (before upload, defaults in bold):**
- When a contact with the same email already exists: **Skip it** / Update empty fields only / Update all mapped fields (overwrite).
- Assign owner: **Me** / Use the "Owner" column / Specific user.
- Tag these contacts (optional free text, e.g. "Webinar Oct 2026"). A tag makes the batch findable later.

**On file selected:**
- Show filename, size, a progress bar with percent, and a Cancel link. Upload streams in chunks and is resumable.
- Then a client-side parse of the first 100 rows to detect delimiter (comma, semicolon, tab), encoding and header row. Show "We detected: semicolon-separated, UTF-8, first row is headers" with an override control for each. A "First row is a header" checkbox, on by default.
- Show a 5-row preview so the user can see the file was read correctly.
- Row count and file-level checks run server-side after upload with a "Checking file…" skeleton state.

**File-level errors (block, keep user on step, file stays selected for replacement):**

| Condition | Message | Action |
|---|---|---|
| Over 50,000 rows | "This file has 63,402 rows. You can import up to 50,000 at a time. Split the file and import each part." | "Choose a different file" |
| Over 50 MB | "This file is 82 MB. The limit is 50 MB. Remove unused columns or split the file." | same |
| No email column or no data | "We couldn't find an Email column. Continue and choose it in the next step." (This is a warning, not a block; mapping resolves it.) | Continue |
| Garbled characters detected | "Some characters look wrong (e.g. “JosÃ©”). Try a different encoding." | Encoding dropdown, preview refreshes |
| Not a CSV / binary / macro file | "This file isn't a CSV. In Excel, choose File → Save As → CSV UTF-8." | Choose file |
| Upload network failure | "Upload stopped at 62%. Your file is safe on your computer." | Retry (resumes) |

## 4. Step 2: Map columns

**Job:** Tell the CRM which spreadsheet column is which CRM field. Auto-suggest, so most users only confirm.

**Layout:** A table with one row per source column.

| Your column | Sample values (first 3 non-empty) | Maps to | Status |
|---|---|---|---|
| E-mail Address | ana@acme.com, … | Email (suggested) | Mapped |
| Cell | +44 7700 900123, … | Phone (mobile) (suggested) | Mapped |
| Notes 2 | — | Don't import | Skipped |
| Tier | Gold, Silver, … | Choose field… | Needs attention |

- **Auto-mapping** by header name, synonyms (e-mail, mail, cell, mobile, org, organisation → Company) and sample-value patterns. Suggestions are labelled "(suggested)" until the user confirms by pressing Continue. Mapping is reviewable, never hidden.
- **Maps to** is a searchable combobox listing standard fields, custom fields, "Create new custom field…" (admins only, otherwise hidden), and "Don't import this column". Each CRM field can be mapped once; a field already used is shown as "Mapped to column D" and picking it moves the mapping with an announcement.
- **Unmapped columns** default to "Don't import" and are dimmed with the label "Skipped". Nothing is dropped silently: the footer says "3 of 14 columns won't be imported."
- **Required field missing:** a persistent inline alert above the table: "Email isn't mapped. Choose which column contains email addresses." Continue stays enabled; clicking it focuses the alert and the relevant control (do not disable the primary button to signal errors).
- **Enum/pick-list mapping:** when a column maps to a pick-list field (lifecycle stage, country, owner), a "Match values" sub-row shows distinct values in the file with a count and a target: "Prospect (4,210) → Lead", "Cust. (812) → Customer", "Unknown (3) → Leave empty". Show up to 50 distinct values; above that show "Too many distinct values: 212. Values that don't match will be left empty and reported." Owner values match by email or name; unmatched are reported.
- **Saved mappings:** a "Use a saved mapping" select at the top lists prior mappings by name; applying is one click and still reviewable. A checkbox at the bottom: "Save this mapping as ___" (optional name; default is the filename).
- Keyboard: every row is reachable by Tab; the combobox follows the ARIA APG combobox pattern. Table is a real `<table>` with column headers.

## 5. Step 3: Review and fix

Validation runs server-side on all rows in the background. A progress line "Checking 50,000 rows… 31,200 done" appears with Cancel. The table is usable as soon as the first page is ready.

**Summary header (counts, each a filter button, state in the URL):**
`48,213 ready · 1,204 with errors · 583 will update existing contacts · 412 duplicates within this file · 0 warnings`

- **Ready:** will import as-is.
- **Errors:** row cannot import until fixed or excluded (invalid email, missing email, bad date, value too long, unmatched required pick-list).
- **Warnings:** will import but something was changed or left empty (phone reformatted to E.164, unmatched optional owner, trailing spaces trimmed). Always tell the user what was normalised.
- **Matches existing:** will be skipped or updated per the chosen option; a row-level diff shows "Phone: 020 7946 0000 → +44 20 7946 0000".
- **Duplicates within file:** same email appears several times; the last row wins unless the user picks otherwise (row-level "Keep this one").

**Grid (virtualised; supports 50,000 rows):**
- Real table semantics (`role="grid"` with cell editing only if the cell is editable), sticky header and first column, row number column that matches the spreadsheet's row number so users can find it in Excel.
- Default filter: **Errors only** when errors exist, otherwise All rows. Filters: All / Errors / Warnings / Updates / Duplicates / Excluded. Search within file.
- Error cells have an icon and text, not colour only, and a cell-level message on focus/hover: "Row 37: 'ana@acme' isn't a valid email. Add a domain such as .com."
- **Fix in place:** Enter edits a cell; Esc cancels; changes revalidate that row immediately. Edits are made to the staged copy, never the original file. A "Revert" per cell.
- **Bulk fix:** "Find and replace in column" (preview count before applying: "Replace 312 values"), "Trim whitespace", "Exclude all error rows" (needs confirmation: "Exclude 1,204 rows? They won't be imported. You can download them to fix and re-import.").
- **Row actions:** Exclude row / Include row (reversible, no confirm, Undo in the status line).
- **Download:** "Download rows with errors (CSV)" includes an extra "Error" column in plain language, row number retained, so the file can be fixed and re-imported alone.
- Row-level errors never block other rows. Never reject the whole file for one bad row.

**Continue rules:** The button label is "Continue to import". With unresolved errors, Continue is allowed: the next step states plainly that error rows will be skipped and counted. Zero importable rows disables nothing, but the step 4 button is replaced by an explanation and a "Back to fix" action.

## 6. Step 4: Confirm and import

### 6.1 Confirmation summary (one screen, no scroll on desktop)
- **What will happen:** "Create 47,630 new contacts. Update 583 existing contacts (empty fields only). Skip 1,204 rows with errors. Skip 412 duplicate rows in the file."
- Options recap: owner, tag, duplicate rule, mapping name. Each has an "Edit" link back to its step.
- Plain-language impact: "New contacts will be visible to everyone with access to Contacts." If automations (workflows, emails, round-robin assignment) trigger on new contacts, a checked-by-default control: "Don't trigger workflows or notifications for imported contacts" with a link to which workflows would fire. This protects 50,000 people from a welcome email.
- Consent/compliance prompt where the product handles it: a required checkbox, "I have the right to contact these people (marketing consent, privacy law)." Only if the org's legal setting requires it. Flag for legal review ("verify").
- Estimated time: "Takes about 3–5 minutes. You can leave this page; we'll notify you when it's done."

### 6.2 Primary action
"Import 47,630 contacts" (specific verb and count). Secondary: Back. Tertiary link: Cancel import (discards the draft, confirm: "Discard this import? Your uploaded file and mapping will be deleted.").

### 6.3 Two-tier friction
- Create-only imports: single click.
- Imports that **update** existing records at more than 100 rows, or overwrite: typed-free confirmation dialog naming the count and consequence: "Update 583 existing contacts? Existing values in mapped fields will be overwritten. You can undo this import for 7 days." Buttons: "Cancel" (initial focus) / "Update 583 contacts". Typed confirmation is not used because the action is reversible.

### 6.4 Prevent double submit
After click, the button enters a loading state and the page transitions to step 5 within 100 ms. A second import of the same file shows a warning on step 1 ("You imported a file named contacts-q3.csv on 12 Oct 2026, 14:03 UTC. Import it again?").

### 6.5 Rollback note
If rollback is not available at launch, update-mode imports require typed confirmation of the word "import" and the dialog says "This can't be undone."

### 6.6 Concurrency
Only one import per workspace runs at a time per user; a second one queues with an explicit "Queued, starts after 'contacts-q3.csv'" message.

### 6.7 Undo (see 8)

## 7. Step 5: Progress and result

### 7.1 Progress
- Determinate progress bar with counts: "Importing… 18,400 of 47,630 contacts (39%)", elapsed time and estimate. `role="progressbar"` with value; announcements via `aria-live="polite"` at 25% steps, not every tick.
- Actions: **Cancel import** (stops further rows; already-imported rows are kept and reported: "Cancel import? 18,400 contacts have already been created. They'll stay unless you undo the import.") and **Leave this page** ("Keep working; we'll notify you").
- Persistent global indicator in the app header while running ("Import running 39%") linking back here. The user can navigate away; the job continues.
- On completion: in-app notification, plus an email to the initiating user if they left the page (default on; setting in notification preferences).

### 7.2 Result summary (the page persists at its URL)
Headline: "Import finished" with counts in a table, not colour alone:

| Outcome | Count | Action |
|---|---|---|
| Created | 47,630 | "View these contacts" (filtered list by this import's tag/ID) |
| Updated | 583 | "View updated contacts" |
| Skipped (already existed) | 0 | — |
| Skipped (duplicates in file) | 412 | — |
| Failed | 1,204 | "Download error report (CSV)" |

- Primary action: "Go to imported contacts". Secondary: "Download error report", "Import another file", "Undo import" (7.3).
- Every row of the file is accounted for: created + updated + skipped + failed = rows in file. A line states this: "50,000 rows in your file. All accounted for."
- Partial-failure state: if the job fails mid-way for system reasons, show "Import stopped at 31,200 of 47,630. 31,200 contacts were created. The rest were not imported." with "Resume import" (continues from the last committed chunk, idempotent) and "Undo import". Never "Something went wrong" alone.
- Whole-job failure: "We couldn't import your file. No contacts were created. Try again in a few minutes. Reference ID: IMP-8F3K2." with Retry and a copyable reference.

### 7.3 Imports history (Settings → Data → Imports)
Table: file name, started (absolute with time zone, e.g. "28 Oct 2026, 14:03 UTC"; relative on hover is not needed in an audit-type list), by, status (Queued / Running / Completed / Completed with errors / Failed / Cancelled / Undone), created, updated, failed, actions (View, Download error report, Undo). Sortable, filterable by status and user; filters in URL. Retained 90 days; file itself deleted after 30 days and the copy says so.

## 8. Undo / rollback
- "Undo import" is available for 7 days to the importing user and admins.
- Confirmation names object, count and consequence: "Undo import 'contacts-q3.csv'? This deletes 47,630 contacts created by this import and restores 583 updated contacts to their previous values. Changes made to these contacts since the import will be lost." Buttons: Cancel (initial focus) / "Undo import". If any imported contact has since had activity (notes, deals, emails), list the count and exclude them by default: "1,082 contacts have new activity and will be kept."
- Undo runs as an async job with the same progress component.

## 9. Data quality and safety rules
- **Never silently drop or alter data.** Any normalisation (phone to E.164, lowercasing email, trimming, date parsing) appears as a warning with before → after.
- **Date formats:** detect the format from the column; if ambiguous (03/04/2026), ask once: "Is 03/04/2026 3 April or 4 March?" Never guess.
- **Encoding:** BOM and legacy encodings handled; spreadsheet formula injection: cells starting with =, +, -, @ are imported as text and never evaluated; they're stripped of the leading character only on export per OWASP guidance (verify with security).
- **Limits per field** shown in the mapping tooltip (e.g. name 200 chars).
- **Privacy:** uploaded file is stored encrypted, deleted after 30 days, access limited to the importer and admins. Imports are audit-logged (who, when, file name, counts) and visible in the audit log.
- **Sensitive columns:** if the file has columns that look like government ID, payment card or health data, show a warning on step 2: "This column looks like payment card numbers. Don't import card numbers into the CRM." Default to "Don't import".

## 10. States matrix

| View | State | Trigger | What the user sees | Actions |
|---|---|---|---|---|
| Step 1 | Initial | Open | Requirements, template, dropzone | Choose file, drop |
| Step 1 | Uploading | File chosen | Progress, filename, size | Cancel |
| Step 1 | Error | See table in 3 | Inline alert near dropzone, file kept | Replace file |
| Step 2 | Loading | After upload | Skeleton table rows | — |
| Step 2 | Needs attention | Required field unmapped | Alert + highlighted row | Map column |
| Step 3 | Validating | Entering step | Skeleton rows, "Checking 31,200 of 50,000" | Cancel check |
| Step 3 | Clean | No errors | "No problems found" success summary | Continue |
| Step 3 | Filter yields none | Filter with 0 | "No rows with errors" + "Show all rows" | Clear filter |
| Step 3 | Validation failed | Server error | "We couldn't check your file. Your edits are saved." | Retry |
| Step 4 | Nothing to import | 0 importable | "None of the 1,500 rows can be imported" | Back to fix, Download error report |
| Step 5 | Running / Done / Partial / Failed / Cancelled / Undone | See 7 | See 7 | See 7 |
| All steps | Resumed draft | Return within 7 days | "Continue your import of contacts-q3.csv?" | Continue, Start over |
| All steps | Session expired | Auth timeout | Re-auth dialog; draft preserved | Sign in |
| All steps | Offline | No connection | Banner "You're offline. Changes will sync when you reconnect." (In step 5 the job continues server-side.) | — |
| All | No permission | Viewer role | Button hidden. Direct URL shows "You don't have permission to import contacts. Ask an admin (Sam Lee, Maria Ortiz)." | Request access |
| All | Import disabled by plan limit | Contact cap reached | "Your plan allows 100,000 contacts. This import would exceed it by 3,412." | Import fewer, Upgrade plan (visible to admins only) |
| Imports list | Empty | Never imported | "No imports yet" + "Import contacts" | Import |
| Imports list | Error | Load fail | "We couldn't load import history." + Retry | Retry |

## 11. Permissions

| Action | Admin | Manager | Rep | Viewer |
|---|---|---|---|---|
| See "Import contacts" | Yes | Yes | Only if enabled by admin | Hidden |
| Import and update existing contacts | Yes | Yes | Create only, own records | — |
| Create custom fields during mapping | Yes | Hidden | Hidden | — |
| Assign owner other than self | Yes | Yes | Disabled with reason: "Reps can only import contacts they own." | — |
| View others' imports | Yes | Own team | Own | — |
| Undo import | Yes | Own | Own | — |
| Download error report | Yes | Own | Own | — |

## 12. Interaction notes
- **Validation timing:** file/structure errors immediately after upload. Row validation after mapping. Cell edits revalidate on commit (Enter/blur). Following the product default, errors don't appear before the user has acted.
- **Save model:** the draft (file, options, mapping, edits, exclusions) autosaves on each step transition and every cell edit batch, with "Draft saved" status text. Final import is explicit.
- **Leaving the wizard:** if the user navigates away, no prompt, because the draft is saved ("Your draft is saved. Resume from Imports."). Closing the tab during upload prompts (`beforeunload`), because the upload would be lost.
- **Focus:** on step change, focus moves to the step heading. After an error summary appears, focus moves to it. Dialogs focus Cancel on destructive confirms.
- **Keyboard:** Tab/Shift+Tab through controls; arrow keys within the grid; Enter to edit; Esc to cancel an edit; `/` focuses in-file search (optional shortcut, not the only path).
- **Performance:** grid virtualised, page size irrelevant; filter and sort run server-side with <1 s response on 50,000 rows; skeletons shown after 300 ms. Browser should never parse or hold the full file in memory: only the first 100 rows are parsed client-side.
- **URL state:** step, active filter, sort, search, and scroll anchor (row number) are in the URL; importId is the resource.

## 13. Copy deck (excerpt)

- Page title: "Import contacts"
- Steps: "Upload file", "Map columns", "Review", "Import"
- Requirements: "Up to 50,000 rows and 50 MB. Your file needs an Email column."
- Dropzone: "Drag a CSV file here, or choose a file"
- Duplicate option: "If an email already exists: Skip it / Fill in empty fields only / Overwrite with values from the file"
- Skipped column: "Won't be imported"
- Missing email: "Email isn't mapped. Choose which column holds email addresses."
- Row error: "Row 37: 'ana@acme' isn't a valid email address. Add a domain, for example ana@acme.com."
- Date ambiguity: "Is 03/04/2026 3 April or 4 March?"
- Workflow control: "Don't run workflows or send notifications for these contacts"
- Primary: "Import 47,630 contacts"
- Progress: "Importing… 18,400 of 47,630 contacts"
- Leave link: "Keep working. We'll notify you when it's done."
- Complete: "Import finished. 47,630 created, 583 updated, 1,204 not imported."
- Notification: "Your import of contacts-q3.csv finished. 1,204 rows couldn't be imported."
- Failure: "We couldn't import your file. No contacts were created. Reference ID: IMP-8F3K2."
- Banned: "Oops", "Invalid file", "Success!", "Please", "successfully".

## 14. Accessibility notes (WCAG 2.2 AA)
- Dropzone has a keyboard- and click-operable "Choose file" button; drag is never the only path (2.5.7).
- Stepper is an ordered list with `aria-current="step"`; completed steps are links.
- Mapping and review tables use `<table>` / `grid` semantics with column headers; sticky headers must not obscure focused cells (2.4.11).
- Errors: icon + text + programmatic association (`aria-describedby`); error summary receives focus on submit-like actions (Continue).
- Progress: `role="progressbar"` with `aria-valuenow`; polite live-region updates at coarse intervals, completion announced with `role="status"`.
- Count chips used as filters are buttons with `aria-pressed`, not colour-coded text only.
- Targets ≥24×24 px; contrast ≥4.5:1 for text, 3:1 for UI; no time limits on any step (draft persists).
- Test with keyboard-only and a screen reader (NVDA/VoiceOver) on steps 2, 3, and 5 before release.

## 15. Acceptance criteria
1. A 50,000-row, 40 MB CSV uploads, maps and reaches the review grid; the grid scrolls at 60 fps and shows the first page of results within 2 s of entering the step (on a reference laptop).
2. A user can complete the flow with a keyboard only, and every drag action has a click alternative.
3. A file with one invalid email among 49,999 valid rows imports 49,999 contacts and reports exactly 1 failed row with its spreadsheet row number and reason.
4. Rows in file = created + updated + skipped + failed, on the result screen and in the history list, for every import.
5. Closing the browser after clicking "Import" does not stop the job; on return the user sees current progress; an email/notification is sent on completion.
6. Resuming a draft after refresh returns to the same step with mapping, options, edits and exclusions intact.
7. No data entered in mapping or review is lost on server error, session timeout or offline.
8. A Viewer never sees an Import button and sees the permission message on direct URL.
9. Phone, email and date normalisations are listed as warnings with before → after.
10. Undo import deletes only records created by that import that have no later activity, restores updated fields, and reports counts.
11. Importing the same file twice shows a warning before the second run.
12. Imports with workflow triggers off create no workflow runs and no emails.
13. Import appears in the audit log with user, file name, counts, and timestamp with time zone.

## 16. Open questions
1. Is email the only match key, or do customers need external ID / phone matching?
2. Can the backend do rollback for 7 days? (Drives 6.3, 6.5, 8.)
3. XLSX support in v1 or later?
4. What is the actual per-workspace contact cap, and what is the upgrade path?
5. Does legal require a consent attestation checkbox (6.1)? Flag for review.
6. Are there rate/concurrency limits per workspace (one active import)?
7. Retention of uploaded files and error reports (30/90 days proposed): confirm with security and privacy.
