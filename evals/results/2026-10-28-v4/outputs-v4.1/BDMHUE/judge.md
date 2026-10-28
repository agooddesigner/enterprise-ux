| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit assumptions on users/data/roles | 1 | "all-day agents… about 140 tickets… two roles (agent and view-only)" |
| 2 | Names visual direction | 1 | "Data-dense utility… light and dark, one indigo accent" |
| 3 | Direction justified by context | 1 | "Data-dense utility (lead; … ops/queue context)"; all-day agents working a queue |
| 4 | Compact density (≤40px rows or ≤14px text) | 1 | `--row:32px`; body `font:13px/1.45` |
| 5 | List-detail / table-first | 1 | Table with side `.pane` ticket detail; no KPI dashboard |
| 6 | Keyboard shortcuts implemented and visible | 1 | Help dialog lists J/K, X, A, E; ⌘K hint in search |
| 7 | App shell: nav with current, search, account/notifications | 1 | `.rail` with aria-current Tickets; `#gs` search; bell and account menus |
| 8 | ≥40 realistic tickets | 1 | 140 generated tickets with realistic subjects, customers, priorities |
| 9 | Loading, empty, error states reachable | 1 | `?state=` param and `#r-state` select; skeleton, empty, error renderers |
| 10 | Bulk select with count and "select all N matching" | 1 | "${n} selected"; "Select all ${all.length} matching tickets" button |
| 11 | SLA/due time with absolute time + time zone | 0 | SLA pill shows relative text; the title with absolute time and zone is on `timeEl` (created/updated), not the SLA pill |
| 12 | Built the screen without asking questions | 1 | Complete HTML file built and delivered |

TOTAL: 11/12
