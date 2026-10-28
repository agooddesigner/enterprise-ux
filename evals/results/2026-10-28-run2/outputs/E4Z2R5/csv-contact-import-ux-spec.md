# UX Spec: CSV Contact Import (up to 50,000 contacts)

Status: Draft v1 · Owner: Design · Audience: Product, Eng, QA, Support

## 1. Goal and success criteria

Let a user bring up to 50,000 contacts from a CSV into the CRM with confidence, without losing data or creating a mess of duplicates.

| Metric | Target |
|---|---|
| Import completion rate (started → finished) | ≥ 85% |
| Users who abandon at the mapping step | < 10% |
| Support tickets per 1,000 imports | < 15 |
| Time from file drop to "ready to import" (50k rows) | < 30 s |
| Imports needing a re-run due to mapping mistakes | < 5% |

## 2. Users and scenarios

- **Admin / ops (primary):** migrating from another CRM or spreadsheet. Large file, messy data, cares about duplicates and ownership.
- **Sales rep (secondary):** uploads a list from an event, 100–2,000 rows. Wants speed.
- **Returning user:** re-imports to update existing records.

## 3. Principles

1. **Never import blind.** Validate and preview before committing.
2. **Errors are per-row, not per-file.** One bad row never blocks 49,999 good ones.
3. **Long work happens in the background.** The user can leave and be notified.
4. **Everything is recoverable.** Imports can be undone for 30 days; error rows are downloadable.

## 4. Entry points and permissions

- Contacts list → **Import** button (primary action in the overflow/toolbar) and empty-state CTA.
- Global "+ New" menu → Import contacts.
- Permission: `contacts.import`. Users without it see the button disabled with a tooltip naming who can grant it.

## 5. Flow overview

1. Upload → 2. Map columns → 3. Configure (duplicates, owner, tags) → 4. Review & validate → 5. Import (background) → 6. Results

A persistent stepper shows progress. Back is always available until step 5 starts. The wizard is a full-page flow (not a modal) because of the density of steps 2 and 4.

## 6. Step details

### Step 1: Upload

- Drop zone + "Choose file". Accepts `.csv` (also `.tsv`, `.txt` with delimiter detection). UTF-8 and UTF-16 supported; encoding auto-detected with a manual override.
- Limits shown up front: **max 50,000 rows, max 50 MB**, up to 100 columns. Link to download a **template CSV** and a short "how to format" help panel.
- Client-side: read the first 1 MB to detect delimiter, encoding and header row, and show a 5-row preview immediately. Then upload in chunks with a progress bar, cancel button, and resumable retry on network failure.
- "First row is a header" toggle (default on, auto-detected).
- Rejections (inline, specific, with the fix):
  - Over 50,000 rows: "Your file has 61,204 rows. The limit is 50,000. Split the file and import in parts." Offer a link to split guidance.
  - Wrong file type, empty file, unreadable encoding, no header row detected, file over 50 MB.
- Do not allow a second file; replacing the file resets later steps with a confirm if mapping was edited.

### Step 2: Map columns

- Two-column table: **CSV column (with 3 sample values)** → **CRM field** dropdown.
- Auto-map by header name and synonyms ("E-mail", "Email Address" → Email). Auto-mapped rows show a "Matched" chip; user can change any.
- Status summary at top: "14 of 16 columns mapped · 2 skipped".
- Options per column: map to a standard field, a custom field, **Create new custom field** (inline, with type picker), or **Don't import**.
- Required mapping: at least one identifier, **Email** or **Phone** (configurable by workspace). Blocking message appears inline if missing; "Next" stays disabled with the reason adjacent.
- Prevent two columns mapping to the same single-value field (warn, offer to pick one). Multi-value fields (e.g., secondary emails) allow multiple.
- Format hints for typed fields: date format selector (auto-detected, e.g. `DD/MM/YYYY` vs `MM/DD/YYYY` with an ambiguity warning), phone default country, boolean values.
- **Save mapping as template** and **Apply saved mapping** for repeat imports.

### Step 3: Configure

- **Duplicate handling** (match on Email by default; Phone as secondary; user can choose):
  - Skip duplicates (default)
  - Update existing records (choose: overwrite all mapped fields / only fill empty fields)
  - Create anyway
  Also notes duplicates *within the file* are merged by first occurrence (shown as a count in review).
- **Owner:** assign all to me / a specific user or team / use an "Owner" column (requires mapping).
- **Tags / list:** optional tag applied to all imported contacts (e.g., "Webinar Oct 2026"); strongly suggested so the batch can be found later.
- **Consent / marketing status:** required choice when the workspace has compliance mode on ("I confirm these contacts may be contacted").
- Trigger options: "Run automations and workflows for these contacts" (default **off**, with explanation, to avoid accidentally emailing 50,000 people).

### Step 4: Review & validate

Validation runs server-side on the full file; show progress ("Checking 50,000 rows… 62%"). User may stay or leave; resumes where they left off.

Summary card:

| | Count |
|---|---|
| Ready to import (new) | 41,870 |
| Will update existing | 6,120 |
| Duplicates skipped | 1,210 |
| Rows with errors (will be skipped) | 800 |

- Error breakdown by type with counts: invalid email format, missing identifier, invalid date, value too long, unknown picklist value, etc. Each type expands to show up to 20 example rows (row number, value, reason).
- **Download error report (CSV)** with the original columns plus `row_number` and `error_reason`, so it can be fixed and re-imported.
- Preview table: first 25 resulting records exactly as they will appear in the CRM.
- Warnings (non-blocking) distinct from errors (row skipped): e.g., "312 phone numbers were reformatted to E.164."
- Primary button states:
  - Normal: **Import 48,000 contacts**
  - 100% errors: disabled, with guidance to go back to mapping.
  - Error rate over 20%: button remains enabled but a callout asks "Many rows failed. Check your mapping?" with a Back to mapping action.
- Confirmation is the button itself (no extra modal), because the summary counts are the confirmation.

### Step 5: Import in progress

- Runs as a background job. Screen shows determinate progress bar, "Imported 23,400 of 48,000", elapsed and estimated time remaining, and live counts of created / updated / skipped / failed.
- Message: "You can close this page. We'll email you and notify you in the app when it's done."
- Actions: **Cancel import** (confirm modal: "Contacts already imported will be kept. Undo is available afterwards.") and **Go to contacts**.
- Rate-limited to protect system performance; no UI changes needed beyond the ETA.
- One active import per workspace at a time for large jobs (>10k rows); a second shows "Another import is running; yours will start next" in a queue state.
- Persistent app-level progress indicator (toast or header chip) while an import runs, linking back to this screen.

### Step 6: Results

- Success headline: "Import complete: 47,990 contacts imported."
- Breakdown: created, updated, skipped, failed, with the same labels as step 4.
- Actions: **View imported contacts** (list pre-filtered by the import's tag/import ID), **Download error report**, **Undo import**, **Import another file**.
- Partial failure state (e.g. system error mid-run): amber banner, states exactly what was and wasn't imported and offers **Retry failed rows**.
- Full failure: red banner, nothing imported, plain cause, retry action, support link with the import ID.
- **Undo import:** available 30 days, removes only contacts *created* by this import and reverts *updated* fields where original values were stored. Confirm modal states counts. Records edited by users since import are flagged and excluded, with a count.

## 7. Import history

Settings → Imports (also linked from step 6). Table: file name, date, user, status, counts, actions (view results, download error report, undo). Filter by status and user. Retained 90 days.

## 8. Notifications

- In-app notification and email on completion, partial failure, or failure. Email includes counts and a link to results; no contact data in the email body.
- Notify the importer only (admins optionally via setting).

## 9. Performance and scale requirements (affect UX)

- Parsing preview: < 2 s. Full validation of 50k rows: < 30 s. Import throughput: ≥ 1,000 contacts/s target (50k in ~1–2 min typical; UI must remain accurate if slower).
- Browser must stay responsive: parse and upload in a web worker; render previews with virtualized tables (never render 50k rows into the DOM).
- Progress updates polled or pushed at ≤ 2 s intervals.
- Browser refresh, tab close, or session timeout at any step must not lose an in-progress import; steps 1–4 draft is retained for 24 hours ("Resume your import?").

## 10. Error and edge-case handling

| Case | Behavior |
|---|---|
| Network drops during upload | Auto-retry chunks; after 3 failures show "Upload paused. Retry" preserving progress |
| File has BOM, quoted newlines, embedded commas | Parsed correctly; covered by test fixtures |
| Header names duplicated | Auto-suffix in the UI ("Phone (2)") and flag |
| Blank rows / trailing empty rows | Silently ignored; count shown in review |
| Leading `=`, `+`, `-`, `@` in cells (formula injection) | Stored as text; escaped in error report and any export |
| Extremely long values | Flagged per field limit, row skipped or truncated per field config (default: row error) |
| Picklist value not in options | Offer "Add new option" for admins, else row error |
| Workspace contact limit exceeded | Blocked at review with "This import would exceed your plan limit by 3,200 contacts" and upgrade path |
| User loses permission mid-import | Job continues under the original authorization; recorded in the audit log |
| Browser language / locale differences | Date and number parsing uses explicit user-selected format, not browser locale |

## 11. Accessibility

- Full keyboard operation of the wizard, mapping dropdowns, and drop zone (Enter/Space opens file picker).
- Stepper, progress bar and counts exposed with `aria-live="polite"` (throttled to meaningful changes, e.g. every 10%), not on every tick.
- Status never relies on color alone; icons and text accompany chips and banners.
- Error messages are associated with their controls; focus moves to the first error on a failed "Next".
- Tables have proper headers; virtualized lists announce row count and position.
- Contrast WCAG 2.2 AA; works at 200% zoom and 320 px width (mapping table collapses to stacked cards on mobile; upload and results remain usable, import on mobile is supported but not optimized).

## 12. Content guidelines

- Plain language, specific numbers, and the next action in every error ("Row 214: 'john@' isn't a valid email. Fix it in your file and re-import this row.").
- Use "contacts" consistently; "records" only in admin/API contexts.
- Button labels state the outcome and count: "Import 48,000 contacts".

## 13. Security, privacy and compliance

- Files are encrypted at rest and in transit; the raw file is deleted 30 days after import (or immediately on user request); error reports expire in 90 days.
- Audit log entry per import: user, time, file name, counts, settings used, undo events.
- GDPR/consent capture when compliance mode is on (step 3); imported contacts record source = "CSV import" and import ID.
- Malware scan on upload; a failing scan shows a generic "We couldn't accept this file".

## 14. Analytics events

`import_started`, `file_uploaded` (rows, size), `file_rejected` (reason), `mapping_changed`, `mapping_template_used`, `validation_completed` (error rate), `import_confirmed`, `import_cancelled`, `import_completed` (counts, duration), `import_undone`, `error_report_downloaded`. Funnel step drop-off tracked for each stage. No contact PII in analytics payloads.

## 15. Open questions

1. Is the 50 MB size limit sufficient for 50k rows with many custom/notes columns?
2. Should update-on-duplicate support matching on a custom unique ID (e.g., external ID)?
3. Can the import be scheduled, or is an immediate run sufficient for v1?
4. Do we support Excel (`.xlsx`) in v1? (Recommend: v1.1; CSV only now.)
5. Undo window: is 30 days acceptable for storage cost and compliance?
6. Concurrency: one large import per workspace, or per user?

## 16. Out of scope (v1)

`.xlsx` import, recurring/scheduled imports, import from Google Sheets or other CRMs via connectors, importing companies/deals (only contacts), fuzzy-match duplicate detection.

## 17. QA acceptance checklist (summary)

- 50,000-row file completes with accurate counts matching the error report.
- 50,001-row file is rejected at upload with the specified message.
- Closing the tab during import does not interrupt or corrupt the job; completion notification arrives.
- A file with 100% invalid rows cannot be submitted.
- Undo restores the pre-import state for created and updated records.
- All steps pass keyboard-only and screen-reader walkthroughs.
