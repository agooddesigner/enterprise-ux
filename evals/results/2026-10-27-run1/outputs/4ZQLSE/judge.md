| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Table layout for list | 1 | `<table>` with rows from `rowHtml`, no cards |
| 2 | First column human-readable ID | 1 | First data column is invoice number (`NWI-2026-xxxx`) |
| 3 | Amount right-aligned | 1 | `th.num,td.num{text-align:right}` |
| 4 | Currency and consistent decimals | 1 | Header "Amount (USD)", `nf` fixes 2 decimals; `usd()` elsewhere |
| 5 | Seed ≥30 rows | 1 | Loop `n<212` generates 212 invoices |
| 6 | Edge cases in seed | 1 | Japanese vendor, long name, null desc/PO, credit notes |
| 7 | Native table with th | 1 | `<table>` with `<th>` in `thead()` |
| 8 | First-use empty state | 1 | `ui.data==='empty'` "No invoices yet" statebox |
| 9 | Distinct no-results state | 1 | "No invoices match these filters" with Clear filters |
| 10 | Loading state | 1 | Skeleton rows with `.skel`, `aria-busy` table |
| 11 | Error state | 1 | "Couldn't load invoices" with retry and reference ID |
| 12 | Filters visible and clearable | 1 | Search/vendor/check filters, "Clear filters" link when active |
| 13 | State in URL | 1 | `toHash`/`syncUrl` writes status, q, sort etc. to hash |
| 14 | Selection with N selected | 1 | `${n} selected` in bulk bar |
| 15 | Bulk approve/reject | 1 | Bulk bar has Approve and Reject… buttons |
| 16 | Delete protected | 1 | Confirmation names count, total, invoices; plus Restore/Deleted tab |
| 17 | Delete visually separated | 1 | Delete uses `danger-o` style; in row menu after `<hr>` |
| 18 | Specific verbs | 0 | Dialog uses "Close" confirm, and bare "Approve"/"Reject"; "Try again" generic |
| 19 | Focus preserved | 1 | `:focus-visible{outline:2px solid var(--focus)}`, no outline:none |
| 20 | Status not colour alone | 1 | Badges include icon and text label |

TOTAL: 19/20
