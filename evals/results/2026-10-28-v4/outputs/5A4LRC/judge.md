| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit assumptions about users, data volume and/or roles | 1 | "Sidebar views: my guess at what agents want"; 148 tickets; viewer role |
| 2 | Names visual direction (preset or dial choices) | 1 | "cool-grey page, white surfaces, one indigo accent… red and amber only for risk" |
| 3 | Direction justified by context | 1 | "this is a dense worklist, not a dashboard"; CSS "for people who live in it all day" |
| 4 | Compact density: rows ≤40px or body ≤14px | 1 | `--row:40px`, compact 32px; body font 14px |
| 5 | List-detail or table-first, not KPI dashboard | 1 | Table with side preview panel; no KPI cards |
| 6 | Keyboard shortcuts implemented and visible | 1 | J/K/X/A/S/`/`/`?` handlers; Shortcuts button and help dialog |
| 7 | App shell: nav with current section, global search, account/notifications | 0 | Nav and account shown; search is table-only, no notifications |
| 8 | At least 40 realistic tickets | 1 | 148 generated tickets with realistic subjects, people and priorities |
| 9 | Loading, empty, error states reachable | 1 | `?state=loading/error/empty`; skeleton, error with retry, empty |
| 10 | Bulk selection with count and "select all N matching" | 1 | "N selected"; "Select all N matching tickets" button |
| 11 | SLA/due time with absolute time and time zone | 1 | Panel shows `absFmt` with timeZoneName; updated column has title |
| 12 | Actually built the screen | 1 | Full HTML file delivered |

TOTAL: 11/12
