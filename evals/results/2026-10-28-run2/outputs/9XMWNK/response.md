I wrote the invoices page, but I haven't opened it in a browser or run it. The attempt to syntax-check the script was blocked by a permission prompt, so any typo in it is still undetected.

**File:** `/tmp/ux-run2/9XMWNK/invoices.html` (single file, inline CSS and JS, no dependencies, light and dark themes)

It loads 200 made-up invoices with a fixed seed, so the list is the same on every reload. Changes aren't saved, so a reload resets them.

**Reviewing 200 a day**
- **Tabs:** The page opens on "Needs review", with live counts for Approved, Rejected and All. Rows leave the list as you act on them, so the list shrinks to zero.
- **Row contents:** Each row shows the invoice number, vendor, memo and PO, due date with days late, amount, flags and status.
- **Flags:** "Possible duplicate" (same vendor and amount), "No PO" and "High value" (over $10k) appear on the row, so you can check them while approving.
- **Finding invoices:**
  - Search covers vendor, invoice number, PO and memo.
  - You can filter by vendor.
  - "Overdue" and "Needs attention" are one-click filters.
  - Every column except flags and actions can be sorted. The default sort is due date, oldest first.
  - The header stays in place while you scroll, and the count and dollar total of what's shown stay visible.

**Approve, reject, delete**
- **Approve:** One click, no confirmation. Undo is the safety net.
- **Reject:** Opens a short dialog with preset reasons and an optional note. The reason shows on the row afterwards.
- **Delete:** A small trash icon kept away from Approve and Reject, so it's harder to hit by mistake.
- **Undo:** Every action shows an undo toast for 10 seconds, and pressing `Z` also undoes it. This works for bulk actions too.
- **Reopen:** Approved and rejected rows have a Reopen button to move them back to review.
- **Bulk:** Use the checkboxes, shift-click for a range, or select all. A floating bar then shows the count and combined dollar amount with Approve, Reject, Delete and Clear.

**Keyboard**
- **Navigation and selection:** `J`/`K` or the arrow keys move down and up. `X` or `Space` selects a row. `/` jumps to search. `Esc` clears the selection.
- **Actions:** `A` approves, `R` rejects, `D` or `Delete` deletes. If a row is part of a multi-row selection, these act on the whole selection. After an action the cursor stays at the same place in the list, so you can keep pressing `A` down the list.

In a real system, delete would normally be a soft delete the server can restore. Here, deleted invoices are removed from view and can only be brought back with Undo, in the same session.
