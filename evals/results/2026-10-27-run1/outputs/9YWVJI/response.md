I wrote the page to `/tmp/ux-eval-results/9YWVJI/invoices.html`. I haven't opened it in a browser or run its script, so it's untested. The only check I tried, a syntax check on the script, was blocked by a permission prompt.

It opens on "Needs review", sorted by due date with the most urgent first. It runs on 200 mock invoices, and everything you do is only held in the page, so a reload resets it.

**Reviewing**
- The header shows how many invoices are awaiting review, their total value and how many are overdue.
- Tabs for Needs review, Approved, Rejected and All show live counts.
- You can search by vendor, invoice number or PO. A "Flagged only" toggle narrows the list to invoices with a problem.
- Problem invoices carry a tag: possible duplicate, over PO by a percentage, or no PO. Overdue and due-soon dates are marked.
- Every column sorts. Status is shown with a shape and a label as well as colour.

**Approve, reject, delete**
- **Approve:** one click on a row, or in bulk.
- **Reject:** asks for a reason, with a short list plus an optional note. The reason shows on the row afterwards.
- **Delete:** acts straight away, with an Undo toast for 8 seconds. Ctrl/⌘+Z also undoes the last action. Deleting several at once asks you to confirm first, with the count and total value.
- **Mis-click guard:** Delete sits apart from Approve and Reject and is styled quietly.
- **Bulk selection:** use the checkboxes, click a row, or Shift-click a range. A bar shows how many are selected and their total value.
- **Keeping your place:** after an action, the highlight moves to the next row.

**Keyboard**
- `j` / `k` moves between rows and `x` selects one.
- `a` approves, `r` rejects and `d` deletes.
- `/` goes to search, `Esc` clears the selection and `?` shows the shortcut list.
- Actions apply to the selected rows, or to the highlighted row if none are selected.

It also follows the system light or dark setting.

I assumed everything fits on one scrolling page, since 200 rows is manageable. If the real volume grows, it would need pagination or a virtualised list.
