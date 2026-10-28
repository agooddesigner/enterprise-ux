| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Native table with name and th scope=col | 0 | No caption/aria-label on table; th lacks scope attribute |
| 2 | Sort buttons in th, aria-sort only on sorted column | 0 | aria-sort="none" set on all unsorted sortable columns |
| 3 | ≥50 rows, long vendor, empty optional, zero/negative amount | 0 | 200 rows, empty PO exists, but no vendor ≥40 chars, no credit notes |
| 4 | Empty renders dash; real 0 renders 0 | 0 | Empty PO renders nothing, no dash |
| 5 | Right-aligned tabular-nums, currency 2 decimals | 1 | .num text-align:right, tabular-nums; money() USD 2 decimals |
| 6 | Unambiguous dates | 1 | fmtDate gives "Oct 28" style month-short day (no year, but unambiguous) |
| 7 | Search/filters/sort/page in URL and restored | 0 | No URL handling at all |
| 8 | Removable filter chips plus Clear all | 0 | Chips are toggles only; no applied-filter chips or Clear all |
| 9 | Visible result count reflects filters | 1 | `<b>${rows.length}</b> invoices · total` updates with filters |
| 10 | Distinct first-use empty and no-results with Clear filters | 0 | No-results message has no Clear filters button |
| 11 | Skeleton rows on initial load, reachable | 0 | No loading state |
| 12 | Load-failure state with Retry | 0 | None |
| 13 | Header checkbox page-only plus Select all N matching | 0 | Header selects all rows; no separate select-all-matching option |
| 14 | Selection count, Clear selection, behaviour on filter change | 1 | Bulk bar shows count and Clear; derive() drops hidden selections |
| 15 | Bulk handles ineligible rows | 1 | Approve/Reject hidden unless all selected are pending |
| 16 | Delete undo or named-count confirm; focus not on destructive | 1 | del() pushes undo stack with toast Undo, soft delete |
| 17 | Bulk buttons name object and count; no generic labels | 0 | Bulk buttons "Approve", "Delete", "Clear" without count/object |
| 18 | Live region, no error only in auto-dismiss toast | 1 | Toast has role="status" aria-live="polite"; no errors shown |
| 19 | Row actions keyboard reachable with focus-visible | 1 | .btn:focus-visible outline; buttons are native, not hover-only |
| 20 | Fixed-vocabulary text badges and last-updated/refresh | 0 | Text badges present, but no last-updated time or refresh control |

TOTAL: 7/20
