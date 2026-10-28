I built the page, but I couldn't run it. The commands I tried for a syntax check and browser test were blocked pending approval. So nothing has been opened or tested, and there may be a bug I haven't seen.

The file is `/tmp/ux-run2/R4ZU5N/invoices.html`, a single file with inline CSS and JS. It holds 214 seeded invoices, including long and non-Latin vendor names, a few credit notes, missing POs and planted duplicates.

**The page**
- **Landing view:** it opens on "Pending approval", sorted by due date, oldest first. Tabs show counts for Pending, Approved, Rejected, All and Deleted. The summary line shows the invoice count and the total amount for the current filters.
- **Filters and sorting:** search, vendor, due date, flags and an amount range, with removable chips. Columns sort, and the page splits into 25 to 200 rows. All of this state is saved in the URL.
- **Table:** the header and the action column stay in place while scrolling. Amounts are right-aligned. Rows can be switched to compact height.

**Approve, reject and delete**
- **Approve:** this acts immediately and shows an Undo message. A possible duplicate triggers a warning first, and a bulk approve can approve only the unflagged invoices.
- **Reject:** it asks for a reason, and a note is required when the reason is "Other". It is also undoable.
- **Delete:** a single pending or rejected invoice deletes at once with Undo. Bulk deletes, and deleting an already-approved invoice, ask for confirmation with the count and total amount. Deleted invoices go to a Deleted tab where they can be restored.
- **Undo:** also available with Ctrl/⌘+Z, not only from the message.
- **Bulk selection:** a bar replaces the summary when rows are selected. Shift-click selects a range, and there is a "Select all N matching" step. Invoices that don't apply are skipped, and the result message says how many.
- **Triage speed:** after an action the next row is highlighted, so you can keep going. Shortcuts are `j`/`k` to move, `x` to select, `a` approve, `r` reject, `#` delete, `/` search and `?` for the list. Single-key shortcuts can be turned off in the shortcuts dialog.

**States and access**
- **States:** a "Preview state" dropdown at the bottom shows loading, load error, first use (no invoices), and a view-only role. Pending "all caught up" and "no results" appear on their own.
- **Accessibility:** it uses native elements, row-specific labels, a detail side panel that isn't a modal, and dark mode.

**Assumptions to check**
- Everything is in USD.
- Approving only queues an invoice for payment.
- Deleted invoices are kept for 30 days.
- Changes live in memory only, so a reload resets them (the "Reset demo data" link does the same).
- Dual approval limits are not included.

Opening the file in a browser and trying the keyboard flow, the reject dialog and the state previews is the quickest check.
