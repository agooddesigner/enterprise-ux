I built the invoices page at `/tmp/ux-run2/76GTLX/invoices.html`, but I never ran it. Both syntax-check attempts were blocked for approval, so I only reviewed the code by reading it. Open it in a browser and try it before relying on it.

I built it for someone who reviews about 200 invoices a day, so most of the design is about speed on repeated actions.

**Reviewing**
- The page opens on the Pending tab, sorted by due date with the most urgent first. Tabs for Approved, Rejected, Deleted and All show counts.
- Approve and Reject sit on each pending row.
- The invoice number opens a side panel with line items and an activity log. Arrow keys inside the panel move to the previous or next invoice.
- Keyboard shortcuts: `J`/`K` move between rows, `A` approves, `R` rejects, `Del` deletes, `X` selects, `Enter` opens details, `/` searches and `Z` undoes.
- After an action, the next invoice moves into the highlighted row, so you can keep going.

**Safety**
- Approve takes effect immediately, with a 9-second Undo toast and `Z` as a shortcut. Reopen and Restore work the same way.
- Reject opens a dialog that asks for a reason, which is sent to the vendor.
- Deleting a single pending or rejected invoice is immediate and undoable. Deleting several at once, or any approved invoice, asks for confirmation. The dialog names the count ("Delete 24 invoices?"), warns if some are already approved and may be scheduled for payment, and says deleted invoices can be restored for 30 days.
- Selecting rows shows an action bar that says how many rows will be skipped, for example "3 not pending — skipped". Selecting a whole page offers "Select all N matching", and shift-click selects a range.

**Table**
- Seeded with 240 invoices, including long vendor names, a Japanese vendor name, missing PO numbers and due dates, credit notes, a very large amount, overdue flags, and five pairs flagged "Possible duplicate".
- Amounts are right-aligned with consistent decimals, and blank values show "—".
- Sort, status, search, vendor, page and the open invoice are all in the URL, so a link reproduces the view.
- It has pagination (25, 50 or 100 rows), a compact row option, CSV export that matches the current filters, and light and dark themes.

**States**
- Loading skeleton, "all caught up", "no first invoices yet", "no results" with Clear filters, and an error screen with Retry and a reference ID.
- A "Prototype controls" bar at the bottom lets you force the loading, empty and error states. It also switches to a read-only Viewer role, where action buttons are disabled and the tooltip explains why.

**Audit** (from reading the code only)
- I checked the data, state, permission, destructive-action, URL-state, keyboard and copy items from the checklist.
- Not done: a column picker, which I skipped at 8 columns.
- Not done: row click opening the panel. Only the invoice number opens it.
- Not done: a warning when you navigate away with a reject dialog half filled in.
- I'm also unsure about horizontal scroll: the invoice column sticks at the left edge and may overlap the checkbox column.
