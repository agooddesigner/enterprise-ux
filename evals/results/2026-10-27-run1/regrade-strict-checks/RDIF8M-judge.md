| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Native table with name and `th scope="col"` | 1 | `<caption class="sr">` plus `<th scope="col">` in `renderTable` |
| 2 | Sort buttons in `th`, `aria-sort` only on sorted column | 0 | `sortHead` sets `aria-sort="none"` on every unsorted column |
| 3 | ≥50 rows, long vendor, empty field, credit note | 1 | 212 rows; 85-character vendor; PO empty about 10% of the time; credit notes about 4% |
| 4 | Empty shows a dash, real 0 shows 0 | 0 | An empty PO renders as nothing in the table; the drawer says "None" |
| 5 | Right-aligned, tabular figures, currency, 2 decimals | 1 | `td.num` has `tabular-nums`; `Intl` USD currency format |
| 6 | Unambiguous dates | 1 | `fmtDate` gives "Oct 27, 2026" |
| 7 | Search, filters, sort and page in URL, restored on load | 1 | `writeURL` and `readURL` cover q, filters, sort, dir, page |
| 8 | Removable chips plus Clear all | 1 | Chips with a ✕ button; "Clear all filters" button |
| 9 | Visible result count reflecting filters | 1 | Summary "N invoices · total" and pager "from–to of N" |
| 10 | Distinct first-use and no-results states, with Clear filters | 1 | "You're all caught up" vs "No invoices match" with a clear button |
| 11 | Skeleton rows, reachable | 1 | `skeleton()` rows shown during the 550ms simulated load |
| 12 | Load failure with Retry, not the empty message | 1 | `role="alert"` "Couldn't load invoices" with a retry button; `?sim=error` |
| 13 | Header checkbox is page-only; Select all N matching exists | 1 | `chkAll` selects the page; `selAll` button "Select all N matching invoices" |
| 14 | Selection count and clear control; cleared or preserved on change | 1 | Bulk bar shows count and "Clear"; `setFilter` clears the selection |
| 15 | Bulk handles ineligible rows | 1 | Approve skips over-limit rows and reports "Skipped N (M over your limit)" |
| 16 | Delete confirm or undo; initial focus not on destructive button | 1 | Dialog names count and total, plus Undo; focus goes to Cancel |
| 17 | Buttons name object and count; no generic labels | 0 | Bulk bar buttons read "Approve 5", "Reject…", "Delete…", "Clear" |
| 18 | Live region announcements; no toast-only errors | 0 | Over-limit and nothing-to-approve errors appear only in a 10s toast |
| 19 | Keyboard reachable, visible `:focus-visible`, nothing hover-only | 1 | Global `:focus-visible` outline; all row actions are buttons |
| 20 | Fixed text badges and a "last updated" time or refresh control | 0 | Text badges exist, but there is no last-updated time or refresh control |

TOTAL: 15/20
