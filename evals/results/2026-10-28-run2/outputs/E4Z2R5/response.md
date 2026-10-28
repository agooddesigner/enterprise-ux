I wrote the UX spec to `/tmp/ux-run2/E4Z2R5/csv-contact-import-ux-spec.md`. I haven't published it anywhere; tell me if you want it as a shareable page.

**The flow:** a six-step wizard.
1. **Upload:** shows the 50,000-row and 50 MB limits up front, auto-detects delimiter and encoding, and rejects bad files with a specific fix.
2. **Map columns:** auto-maps headers, shows sample values, lets users create custom fields, and requires an Email or Phone identifier.
3. **Configure:** duplicate handling (skip, update, or create anyway), owner, and a batch tag. Automations are off by default so an import can't accidentally email 50,000 people.
4. **Review and validate:** server-side checks on the whole file, counts by outcome, a downloadable error report, and a preview. The import button states the count, for example "Import 48,000 contacts".
5. **Import in progress:** runs in the background, so users can leave and get notified.
6. **Results:** a breakdown, retry for failed rows, and undo for 30 days.

**Principles behind it:** one bad row never blocks the file, every import is reversible, and nothing is imported without a preview.

**Other sections:** import history, notifications, performance targets, an edge-case table, accessibility, security and compliance, analytics events, and a QA checklist.

**Open questions for you:**
- Is 50 MB enough for 50k rows with many columns?
- Should duplicate matching support a custom external ID?
- Do you need `.xlsx` support in v1?
- Is a 30-day undo window acceptable?
- Should large imports be limited to one at a time per workspace or per user?

I assumed several defaults that need your sign-off. They are duplicate matching on email, a 20% error rate that triggers a warning, one large import at a time per workspace, and a 24-hour retention for draft imports.
