I've built the invoices page as a single file, but I haven't run it. This environment blocked every script and syntax check, so there's been no browser test and no `node --check`. Expect to hit a bug or two on first open.

The file is `/tmp/ux-eval-results/RDIF8M/invoices.html`. It opens with 212 realistic fake invoices and no network calls.

**How it works for a reviewer handling about 200 a day:**
- **Starting view:** it opens on **Needs review**, sorted by due date, most urgent first. Overdue invoices show "3d overdue". Tabs for Approved, Rejected and All show counts.
- **Finding invoices:** search covers invoice number, vendor and PO. Filters are vendor, due date, amount band and flagged-only. Active filters appear as removable chips. Filters, sort and page live in the URL, so a view can be shared.
- **Rows:** amounts are right-aligned, and status is shown as text plus an icon, never colour alone. Warning flags include "Possible duplicate", "No PO" and "Over PO amount". Long and non-Latin vendor names are in the data to test truncation.
- **Keyboard:**
  - **J / K** move between rows.
  - **X** selects a row.
  - **A** approves and **R** rejects.
  - **Enter** opens an invoice.
  - **/** focuses search.
  - **Ctrl+Z** undoes the last action.
  - After an action, focus stays at the same position so the reviewer can keep going.
- **Approve:** it happens immediately and shows an Undo toast for 10 seconds.
- **Reject:** it asks for a reason from a list. Choosing "Other" requires a note.
- **Delete:** it sits in the row's ⋯ menu, away from Approve. A confirmation names the count and total, then offers a short Undo. Deleting 10 or more at once also requires typing DELETE.
- **Approval limit:** I made up a $25,000 per-invoice limit. Over-limit invoices have a disabled Approve with the reason stated, and bulk approve skips them and says how many.
- **Bulk actions:** a bar shows the selected count and dollar total. You can select the page, then all matching invoices.
- **Detail panel:** it holds the full fields, flags and history. "Approve & next" moves straight to the next invoice. Arrow keys move between invoices.
- **States:** there are loading placeholders and a first-time "all caught up" view. A no-results view offers "Clear all filters". The error view has a Retry button; you can see it by adding `?sim=error` to the URL.
- **Other:** it follows light and dark mode, and screen readers announce actions.

**What I assumed:**
- **Limit and delete:** the $25,000 limit and the undo-then-gone delete are my guesses. Both are easy to change.
- **Data:** it's in-memory only, so a refresh resets everything.

I'd test the row ⋯ menu, the detail panel and the reject dialog first, since those have the most moving parts.
