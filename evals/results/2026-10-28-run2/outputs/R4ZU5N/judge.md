| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Native table with name and `th scope="col"` | 1 | `<caption class="sr-only">` and `<th scope="col">` headers |
| 2 | Sort buttons in `th`; `aria-sort` only on sorted column | 0 | Unsorted columns get `aria-sort="none"`, so it is set on all of them |
| 3 | ≥50 rows, long vendor, empty optional, credit note | 1 | 214 rows, 67-character vendor name, `po: null`, negative amount at `i%53===17` |
| 4 | Empty values show a dash, real 0 shows 0 | 0 | The table has no PO column. No zero amount is seeded or shown. |
| 5 | Right-aligned amounts, tabular figures, currency with 2 decimals | 1 | `td.num` has `tabular-nums` and right alignment; amounts use `Intl` USD format |
| 6 | Unambiguous dates | 1 | `en-GB` format with a short month name, e.g. "28 Oct 2026" |
| 7 | Search, filters, sort and page in URL, restored on load | 1 | `readURL`/`writeURL` cover q, vendor, due, flag, min, max, sort, dir, page |
| 8 | Removable chips plus "Clear all" | 1 | Chips with ×, and a "Clear all filters" link |
| 9 | Visible result count reflects filters | 1 | "N invoices · total" and the pager's "from–to of N" both use the filtered list |
| 10 | First-use and no-results states; no-results has one-click clear | 1 | `emptyHTML` has "No invoices yet" and "No invoices match" with a clear-all button |
| 11 | Skeleton rows on initial load, reachable | 1 | `skeleton()` rows; `U.loading` is true until a 500ms timeout |
| 12 | Load failure with Retry, not the "no invoices" message | 1 | Error banner with "Try again"; the empty zone says "aren't available right now" |
| 13 | Header checkbox selects the page; separate "Select all N matching" | 1 | `chkAll` selects `pageRows`; the strip offers "Select all N matching invoices" |
| 14 | Selection count, "Clear selection", cleared on change | 1 | "N invoices selected", a Clear selection button, and `U.sel.clear()` on filter, page and sort changes |
| 15 | Ineligible rows warned about or reported | 1 | "N skipped: not pending" in the result message; duplicate warning dialog |
| 16 | Delete has Undo or a confirmation naming count and consequence; focus not on destructive button | 1 | Single delete has Undo, bulk delete has a confirm dialog, and initial focus goes to `[data-cancel]` |
| 17 | Buttons name object and count; no generic labels | 0 | Bulk buttons read "Approve ${n}" with no noun, and row and panel buttons read just "Approve" |
| 18 | Live-region announcements; errors not only in auto-dismissing toasts | 1 | `#live` and `role=status` on toasts; load error is a persistent `role="alert"` banner |
| 19 | Keyboard-reachable actions with `:focus-visible` | 1 | Global `:focus-visible` outline; all actions are buttons, none hover-only |
| 20 | Text status badges and last-updated time | 1 | Badges carry text labels plus an icon; "Data as of HH:MM" in the subtitle |

TOTAL: 17/20
