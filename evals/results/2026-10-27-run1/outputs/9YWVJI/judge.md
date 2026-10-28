| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Table layout, not cards | 1 | `<table id="tbl">` with rows for invoices |
| 2 | First column human-readable identifier | 1 | The first data column is the vendor name; the leading column is a checkbox |
| 3 | Amount column right-aligned | 1 | `th/td class="num"` with `text-align:right` |
| 4 | Currency and consistent decimals | 1 | `Intl.NumberFormat` USD, e.g. `$1,234.56` |
| 5 | Seed data ≥ 30 rows | 1 | Loop `i < 200` |
| 6 | Edge case in seed data | 1 | Empty PO (`""` shown as "—"), plus large amounts and overdue dates |
| 7 | Native table with `<th>` | 1 | `<thead><tr><th>` cells |
| 8 | First-use empty state | 0 | Only "All caught up" or "Nothing here"; no first-use state for having no invoices |
| 9 | Distinct no-results state | 1 | "No invoices match your filters." differs from the other empty texts |
| 10 | Loading state | 0 | Data is synchronous; no skeleton or loading indicator |
| 11 | Error state for failed loading | 0 | No loading-error handling anywhere |
| 12 | Filters visible and clearable | 0 | Search and flag toggle exist, but there are no applied-filter chips or clear-filters control |
| 13 | Filter/sort state in URL | 0 | No `location` or `history` use |
| 14 | Row selection with "N selected" | 1 | `${n} selected` in bulk bar |
| 15 | Bulk approve/reject | 1 | `data-bulk="approve"` and `data-bulk="reject"` buttons |
| 16 | Delete protected | 1 | Undo toast; bulk delete dialog names count and total |
| 17 | Delete separated from approve | 1 | `.btn.ghost.del` with a 14px margin, quiet style vs. coloured Approve and Reject |
| 18 | Specific verbs, no Submit/OK | 1 | Buttons read "Approve", "Reject…", "Delete…", "Cancel", "Close"; no "Submit" or "OK" |
| 19 | Visible focus preserved | 1 | `:focus-visible{outline:2px solid var(--focus)}`; no bare `outline:none` |
| 20 | Status not colour-only | 1 | Badge has a text label plus a shape marker |

TOTAL: 15/20
