I wrote the spec to `/tmp/ux-run2/QTZ3MR/contact-import-ux-spec.md`. I haven't tested any of it with users, and the performance targets need engineering to confirm.

**Main decisions**
- **Who it's for:** admins and team leads who import occasionally, such as weekly to quarterly. So I optimised for guidance and safety over speed.
- **Flow:** a five-step page at `/contacts/import/:importId`, with the step in the URL so a refresh doesn't lose progress. The steps are Upload, Map fields, Rules, Review and Import.
- **Dry run first:** the Review step validates the whole file without writing anything. It shows how many contacts will be created, updated, skipped or rejected. The final button names the count, for example "Import 45,972 contacts", so there's no separate "Are you sure?" dialog.
- **Bad rows:** rows with errors never block the good ones. Users can download an error CSV with the row number and the reason for each failure, then fix it and re-upload.
- **Scale:** the browser only holds a 25-row preview. Parsing, validation and the import itself all run on the server in the background, so users can leave the page and get notified when it finishes. The upload resumes if the connection drops.
- **Duplicates:** the default is to skip contacts that already exist. Overwriting existing values is opt-in and named on the button. Duplicates inside the file are handled too.
- **Undo:** every import can be undone for 7 days. The undo dialog states what it will do and how many records. Contacts edited since the import are left alone.
- **Also in the spec:**
  - file limits: 50,000 rows and 50 MB, CSV only in v1;
  - an imports history page;
  - a table of states covering upload, mapping, review and import, plus permission, plan-limit and session expiry;
  - data integrity rules;
  - accessibility, copy and success metrics.

**Open questions for you**
- Should Excel (`.xlsx`) files be supported in v1? I recommended phase 2.
- Can non-admin reps import, and with what row cap?
- Is a consent source required on every import, or only when "marketing consent: Yes" is chosen? Legal should confirm.
- Should the 7-day undo window be configurable by admins?

The spec's full list of open questions also covers round-robin owner assignment and who can create custom fields from the mapping step.
