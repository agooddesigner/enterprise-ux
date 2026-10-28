| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Table layout, not cards | 1 | `<table>` with rows for invoices |
| 2 | First column human-readable | 0 | First column is a checkbox; invoice # is the second column |
| 3 | Amount right-aligned | 1 | `th.num,td.num{text-align:right}` |
| 4 | Currency, consistent decimals | 1 | Intl.NumberFormat USD currency format |
| 5 | Seed ≥30 rows | 1 | Loop generates 212 invoices |
| 6 | Edge cases in seed | 1 | Long vendor name, Japanese name, empty PO, negative credits |
| 7 | Native table with th | 1 | `<th scope="col">` in thead |
| 8 | First-use empty state | 1 | "You're all caught up" state for the pending tab |
| 9 | Distinct no-results state | 1 | "No invoices match these filters" with Clear all filters |
| 10 | Loading state | 1 | skeleton() with shimmer bars, aria-busy |
| 11 | Error state | 1 | "Couldn't load invoices" with Try again; `?sim=error` |
| 12 | Filters visible and clearable | 1 | Chips with ✕ remove buttons; Clear all filters |
| 13 | State in URL | 1 | writeURL uses history.replaceState with query params |
| 14 | Selection with "N selected" | 1 | `${ids.length} selected · total` in bulk bar |
| 15 | Bulk approve/reject | 1 | bApprove and bReject buttons in bulk bar |
| 16 | Delete protected | 1 | Confirmation names invoice number or count and total; Undo toast |
| 17 | Delete separated from approve | 1 | Delete is in the ⋯ menu, styled red; the bulk Delete uses a distinct outline style |
| 18 | Specific verbs | 0 | Bulk bar says "Approve 5", "Reject…", "Delete…" and the dialog Cancel/Reject buttons are generic, though row aria-labels are specific. Visible labels are mostly bare verbs |
| 19 | Focus visible preserved | 1 | `:focus-visible` outline defined; no outline removal without replacement |
| 20 | Status not colour alone | 1 | Badge has icon and text label |

TOTAL: 18/20
