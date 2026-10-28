| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Table name and `th scope="col"` | 0 | `aria-label="Vendor invoices"` is present, but no `<th>` has a `scope` attribute. |
| 2 | Sort buttons; `aria-sort` only on the sorted column | 0 | Buttons are inside `<th>`, but unsorted columns get `aria-sort="none"`. |
| 3 | Seed data: ≥50 rows, long name, empty field, credit | 1 | 240 rows, a 53-char vendor name, null PO, negative amounts. |
| 4 | Dash for empty, real 0 shown as 0 | 1 | `x.po\|\|'—'` and the due-date dash; `money()` formats amounts so 0 would show as 0.00. |
| 5 | Right-aligned, tabular figures, currency, 2 decimals | 1 | `td.num` has `text-align:right` and `tabular-nums`; header "Amount (USD)"; 2 decimals. |
| 6 | Unambiguous dates | 1 | `fmtDate` gives "Oct 28, 2026" style. |
| 7 | Search, filters, sort, page in the URL and restored | 1 | `writeHash` and `readHash` cover `q`, `v`, `sort`, `dir`, `p` and `s`. |
| 8 | Removable filter chips plus Clear all | 0 | Only a single "Clear filters" button; no individual chips. |
| 9 | Result count reflects filters | 1 | Pager shows "from–to of total"; tab counts follow the filters. |
| 10 | First-use and no-results states, Clear filters | 1 | "No invoices yet" and "match your filters" states with a `data-clear` button. |
| 11 | Skeleton rows, reachable | 1 | 12 skeleton rows on initial load with a 700ms delay, plus a "Stuck loading" toggle. |
| 12 | Load-failure state with Retry | 1 | "Couldn't load invoices" with a Retry button, and no empty-state text. |
| 13 | Page-only header checkbox plus "Select all N matching" | 1 | `selPage` selects `view.rows`; the banner offers "Select all N matching invoices". |
| 14 | Selection count, Clear selection, selection handling | 1 | "N selected" and "Clear selection"; `setQ` clears the selection on filter and sort changes. |
| 15 | Ineligible rows in bulk actions | 1 | "N not pending — skipped by Approve and Reject", plus a warning box in the dialog. |
| 16 | Delete undo or named confirmation; focus not on destructive button | 1 | "Delete 24 invoices?" dialog with `autofocus` on Cancel; single deletes are undoable. |
| 17 | Bulk buttons name object and count | 0 | Toolbar buttons read "Approve 5 pending", "Reject…" and "Delete…", with no object or count on the last two. |
| 18 | Live-region announcements; errors not only in a toast | 1 | `#toasts` has `role="status"`, the reject error has `role="alert"`, and the load error is persistent. |
| 19 | Keyboard reachable with `:focus-visible`; nothing hover-only | 1 | Global `:focus-visible` outline; row actions are real buttons that are always visible. |
| 20 | Text status badges plus "last updated" or refresh | 0 | Badges carry text, but there is no last-updated time or refresh control. |

TOTAL: 16/20
