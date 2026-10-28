I wrote the UX spec to `/tmp/ux-run2/S8HEV4/contact-import-ux-spec.md`. I haven't reviewed it against your CRM's design system or current import screens. I didn't know either, so the spec rests on the assumptions below.

**Assumptions to confirm**
- Email is the key for matching existing contacts.
- Imports can both create and update contacts, and the default is skip-if-exists.
- The limits are 50,000 rows and 50 MB.
- Processing runs in the background, so users can close the browser after they commit.
- The backend can roll an import back for 7 days.
- Admins and Managers can import, Reps only if an admin enables it, and Viewers can't.

**The flow:** it's a full-page wizard with five steps and a draft that autosaves, so a refresh or a return later resumes where the user left off.
1. **Upload:** shows the requirements and a template, detects delimiter and encoding, and lets the user choose a duplicate rule, owner and tag. Each file-level error says what to do next.
2. **Map columns:** mapping is auto-suggested and reviewable, and columns that aren't imported are listed rather than dropped. Pick-list values are matched, and mappings can be saved for reuse.
3. **Review and fix:** a virtualised grid with filters for errors, warnings, updates and duplicates. Users can fix cells in place or in bulk and download the error rows to fix and re-import. One bad row never blocks the rest.
4. **Confirm:** a summary with counts, a "don't trigger workflows or notifications" option, and a button labelled with the count ("Import 47,630 contacts"). Updating more than 100 existing contacts needs a confirmation dialog.
5. **Progress and result:** progress shows counts, and the user can leave and get a notification. The result accounts for every row (created, updated, skipped, failed). Partial and total failures are handled, there is an error-report download, and the user can undo for 7 days.

The spec also covers an imports history page, a state-by-state table, a permissions table, a copy deck, accessibility notes (WCAG 2.2 AA) and 13 testable acceptance criteria.

**Open questions** (full list of 7 is in section 16):
- Can the backend really roll back an import? If not, section 6.5 makes update imports require typed confirmation.
- Does legal require a consent checkbox before importing? I included one, flagged for review.
- Is email the only key for matching existing contacts, or do you also need external ID or phone?
- Do you need XLSX in v1? The spec assumes CSV only.
