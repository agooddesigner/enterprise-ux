I couldn't run the page or check its script. Every shell command I tried to syntax-check it was blocked pending approval, so the file is untested.

I wrote `/tmp/ux-eval-results/4ZQLSE/invoices.html`, a single file with inline CSS and JS. It has 212 invoices of seeded data, including long vendor names, a Japanese vendor name, credit notes, missing POs and possible duplicates.

**How I designed it:** I assumed a finance admin clearing about 200 invoices a day, so it is built around speed and avoiding mistakes.
- **Work queue:** it opens on **Pending approval**, sorted by due date with the soonest first. Status tabs show counts, and the page header shows how many invoices await approval and their total.
- **Table:** it is a dense, sticky-header table with the invoice number as the first column. Amounts are right-aligned and tabular, and missing values show "—". You can switch between comfortable and compact rows, and your choice is remembered.
- **Overdue and risk flags:** overdue, possible duplicate, no PO and credit note are shown with text, not colour alone.
- **Search and filters:** you can search by invoice number, vendor or PO, and filter by vendor or check. Filters, sort, page and the open invoice are stored in the URL hash, so links can be pasted into Slack.
- **Paging and export:** pages are 25, 50 or 100 rows. "Export N rows" downloads the filtered rows as CSV.
- **Approve:** it happens instantly and shows an Undo toast for 10 seconds (also `Z`).
- **Reject:** it asks for a reason, and a note if you pick "Other", and says the vendor will be emailed. The dialog keeps your input if validation fails.
- **Delete:** it opens a confirmation that names the count, the total and the first invoices. It moves them to a Deleted tab where they can be restored, and Cancel has focus by default. Approved invoices can't be deleted.
- **Bulk actions:** the bar shows the selection count and total, and shift-click selects a range. "Select all N matching" is a separate explicit step. Ineligible invoices are skipped with a message, and partial failures are reported with a retry button.
- **Detail panel:** a side panel shows the line items, flags and an activity log with timestamps in ET. After you decide on an invoice there, it advances to the next one.
- **Keyboard:** `J`/`K` move between invoices, `Enter` opens details, `X` selects, `A` approves, `R` rejects, `Delete` deletes, `/` searches, `?` lists the shortcuts, and `Esc` closes things.
- **States:** loading skeleton, error with a reference ID and retry, first-use empty, no results, "Queue clear", and an empty Deleted tab. A "Prototype controls" strip at the bottom switches data state and role, and can simulate a partial bulk failure. In the Viewer role, action buttons are disabled with an explanation.

**Not built:**
- **Column picker:** the nine columns are fixed.
- **Sorting and pagination:** both run in the browser. A real backend would need them done server-side.
- **Approval limits:** no spending limits or separation of duties.
- **Viewport check:** the narrow-screen layout was not looked at.

If you can approve one shell command, I'll syntax-check the script and click through approve, reject, delete and undo. I'd fix whatever that turns up.
