| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit assumptions about users/data/roles | 1 | "Assumptions I made": support agents, ~1,200 tickets, roles agent/lead/viewer |
| 2 | Names visual direction | 1 | Header: "Data-dense / classic enterprise"; "dense and neutral, one blue accent" |
| 3 | Direction justified by context | 1 | Comment: "daily support agents work a shared queue (~1,200 tickets)"; dense for all-day use |
| 4 | Compact density ≤40px rows or ≤14px text | 1 | `--row-h:40px`; body font 14px; compact mode 32px |
| 5 | List-detail / table-first, not KPI dashboard | 1 | Table-first queue with right-hand preview aside |
| 6 | Keyboard shortcuts implemented and visible | 1 | J/K/X/A/E/N// handlers; help dialog; ⌘K kbd in header |
| 7 | App shell: nav w/ current, global search, account/notifications | 1 | Nav `aria-current="page"`; `#gsearch` ⌘K; `#bellBtn`, `#meBtn` |
| 8 | ≥40 realistic tickets | 1 | genData generates 1243 tickets from realistic templates and people |
| 9 | Loading, empty, error states reachable | 1 | `?state=loading/empty/error` and account menu Data state selector |
| 10 | Bulk selection with count and select-all-N | 1 | "N selected" toolbar; "Select all N matching tickets" banner |
| 11 | SLA/due with absolute time + time zone | 1 | SLA title "First-response due " + abs() with `timeZoneName:"short"` |
| 12 | Built the screen without stopping to ask | 1 | Delivered full single-file queue screen, stating assumptions |

TOTAL: 12/12
