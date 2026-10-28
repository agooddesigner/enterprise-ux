I wrote the UX spec for the contact import, using the enterprise-ux skill's CSV import, export and defaults guidance. The file is `/tmp/ux-eval-results/HB875G/contact-import-ux-spec.md`.

**What it covers**
- **Flow:** a five-step wizard: Upload, Map columns, Review and fix, Import options, Confirm and run. The step state and the review filters are in the URL. Nothing is written to the CRM until the last step.
- **Review step:** every row ends as created, updated, skipped or failed, and the counts add up to the file. Users can edit cells inline, apply bulk fixes, and download an error report they can re-upload.
- **Safe defaults:** existing contacts get their empty fields filled, not overwritten. Automations are off, and consent defaults to "Not opted in".
- **The 50,000-row case:** the import runs in the background with progress and Cancel, and it survives a closed tab. The user is notified on completion, and the review grid is virtualised for large files.
- **Undo:** an import can be undone for 7 days. The dialog warns about contacts edited since the import.
- **Also included:** the states and edge cases (permissions, plan limits, interrupted uploads, session expiry), accessibility to WCAG 2.2 AA, performance targets, success metrics, and the copy for key messages.

**Assumptions to confirm**
- Contacts match on email.
- CSV only.
- Up to 50,000 rows or 50 MB.
- Only one import runs per workspace at a time.
- The 7-day undo is technically feasible (it is also the first open question in the spec).

The spec ends with five open questions. The main ones are whether undo is feasible at this scale and what consent wording legal requires.

I haven't published it as a shareable page. I can do that if you want to send it to your team.
