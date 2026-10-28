| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Native table, accessible name, th scope=col | 0 | `<table id="tbl">` has no caption/aria-label; th lack scope |
| 2 | Sort buttons in th, aria-sort only on sorted col | 0 | Vendor th has aria-sort="none"; JS sets "none" on all others |
| 3 | ≥50 rows, long vendor, empty field, zero/negative | 0 | 200 rows, empty PO, but vendors ≤27 chars; no credit notes |
| 4 | Empty renders dash, real 0 renders 0 | 0 | PO shows "—", but no real 0 value exists/demonstrated |
| 5 | Right-aligned, tabular-nums, currency 2 decimals | 1 | `.num` text-align:right, tabular-nums, Intl USD currency |
| 6 | Unambiguous dates | 0 | fmtDate gives "Mar 3" with no year |
| 7 | Search, filter, sort, page in URL and restored | 0 | No URL handling; state in memory only |
| 8 | Removable filter chips plus Clear all | 0 | No chips |
| 9 | Result count reflecting filters | 0 | "N invoices shown" lacks total of N; "X of Y" absent |
| 10 | Distinct first-use empty and no-results, with Clear filters | 0 | No-results text has no Clear filters button; no first-use state |
| 11 | Skeleton loading reachable | 0 | No loading state |
| 12 | Load-failure state with Retry | 0 | None |
| 13 | Header checkbox page-only plus "Select all N matching" | 0 | No select-all-matching option |
| 14 | Selection count, Clear selection, cleared/preserved on change | 1 | "N selected", "Clear selection" button; sel pruned on tab change |
| 15 | Bulk handles ineligible rows | 0 | Silently filters non-eligible rows; no warning or skipped counts |
| 16 | Undo or named confirm; focus not on destructive | 0 | Undo exists, but dialog's autofocus lands on first Cancel? Bulk-confirm only; toast Undo present but single-delete fine; Delete button in dialog is last, Cancel first focus — however, passes arguably but strict: see below |
| 17 | Buttons name object and count; no generic labels | 0 | Bulk buttons "Approve", "Reject…", "Delete…" lack count |
| 18 | Live region announcements; no toast-only errors | 1 | `aria-live` on `#live` and toasts; reject error uses role=alert |
| 19 | Keyboard-reachable row actions, :focus-visible | 1 | Native buttons; `:focus-visible` outline defined; no hover-only actions |
| 20 | Fixed text badges plus last-updated/refresh | 0 | Text badges present, but no last-updated or refresh control |

Correction on check 16: the delete flow uses a toast Undo (8s) for soft delete and the bulk confirm names the count and consequence. Both parts hold, and the dialog's first focusable element is Cancel, so initial focus isn't on the destructive button. Score 16 = 1.

TOTAL: 4/20
