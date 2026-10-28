| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit assumptions on users/volume/roles | 1 | "Users: support agents… Volume: hundreds of tickets… Roles: agent and view-only" |
| 2 | Names visual direction | 1 | "lead Data-dense utility, borrowing Restraint's single accent"; 32px rows, one accent |
| 3 | Direction justified by context | 1 | "ops/queue context", "agents working the queue all day" in header comment |
| 4 | Compact density ≤40px rows or ≤14px body | 1 | `--row:32px`; body `font:13px/1.45` |
| 5 | List-detail / table-first, not KPI dashboard | 1 | Table with 420px preview panel; "table-first layout and a preview panel" |
| 6 | Keyboard shortcuts implemented and visible | 1 | Shortcuts dialog (`?`), `⌘K` kbd and `/` kbd hints, j/k/x/a handlers |
| 7 | App shell: nav, global search, account/notifications | 1 | Sidebar nav with Queue current; `#gsearch`; `#bellBtn`, `#acctBtn` |
| 8 | ≥40 realistic tickets | 1 | 260 seeded from 23 realistic subject templates and 18 customers |
| 9 | Loading, empty, error reachable | 1 | `?state=` param and `#statePick` select; skeleton, error, empty states |
| 10 | Bulk selection with count and select-all-N | 1 | `#bulkCount` "N selected"; "Select all N matching tickets" button |
| 11 | SLA/due time with absolute time and TZ | 1 | SLA cell `title="Due "+absTime(due)` with `timeZoneName:'short'` |
| 12 | Built the screen without asking questions | 1 | Full HTML file built; response says it was delivered |

TOTAL: 12/12
