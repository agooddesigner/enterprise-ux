| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Native table with name and th scope=col | 0 | `aria-label="Invoices"` present, but `<th>` elements have no `scope="col"`. |
| 2 | Sort buttons in th, aria-sort only on sorted column | 1 | `th()` puts `<button class="sortbtn">` in th; aria-sort only if `S.sort===k`. |
| 3 | ≥50 rows; long vendor, empty optional, negative amount | 1 | 212 rows; 87-char vendor; `po:null`, null desc; indices 3,41,97 negative. |
| 4 | Empty → dash; real 0 → 0 | 0 | Dashes for empty PO, but no real 0 value is shown or handled. |
| 5 | Right-aligned, tabular-nums, 2 decimals, currency | 1 | `td.num` right-aligned, tabular-nums, `nf` 2 decimals, "Amount (USD)" header. |
| 6 | Unambiguous dates | 1 | `dDue` formats as "Oct 27, 2026" (month short name). |
| 7 | Search, filters, sort, page in URL and restored | 1 | `toHash`/`fromHash` cover q, vendor, flag, sort, dir, page, status. |
| 8 | Removable chips plus Clear all | 0 | Only a "Clear filters" link; no individual removable chips. |
| 9 | Visible result count reflecting filters | 1 | Footer "a–b of N · total"; tab counts follow filters. |
| 10 | Distinct first-use and no-results; Clear filters one-click | 1 | "No invoices yet" vs "No invoices match these filters" with Clear filters button. |
| 11 | Skeleton rows, reachable | 1 | 12 `.skel` rows; 700ms boot delay and Loading toggle. |
| 12 | Load-failure with Retry, not the empty message | 1 | `ui.data==='error'` statebox "Couldn’t load invoices" with "Try again". |
| 13 | Header checkbox page-only; Select all N matching separate | 1 | `selpage` selects the page; the banner has a "Select all N matching invoices" link. |
| 14 | Selection count, Clear selection; cleared/preserved on change | 1 | "N selected", Clear button; `go()` clears sel unless keepSel; the banner explains. |
| 15 | Ineligible rows handled | 1 | "Approve and reject apply to the N pending"; the toast reports "skipped (not eligible)". |
| 16 | Delete undo/confirm naming count; focus not on destructive | 1 | Dialog "Delete N invoices?" with `autofocus` on Cancel; Undo toast. |
| 17 | Buttons name object and count; no generic labels | 0 | The help dialog's confirm button is "Close"; Approve button "Approve 5" lacks the object noun. |
| 18 | Live region for results; errors not only in an auto-dismiss toast | 1 | `#toast role=status`; bulk failure is sticky and the error state has `role=alert`. |
| 19 | Row actions keyboard reachable with focus-visible; nothing hover-only | 0 | `.acts` is opacity:0 until hover or focus-within; the focus ring exists, but the actions are mostly hidden. |
| 20 | Text status badges; last updated or refresh | 1 | Badges carry text labels; the footer shows "Updated" time and a refresh button. |

TOTAL: 14/20
