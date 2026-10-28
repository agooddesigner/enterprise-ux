| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit assumptions about users/data/roles | 1 | "agents live in this screen all day"; signed-in agent Priya, three other agents, sample data |
| 2 | Names visual direction (preset or dial choices) | 0 | Describes features and themes; no named style or density/radius/palette dials |
| 3 | Direction justified by context | 0 | Keyboard-first is justified, but no visual direction is named to justify |
| 4 | Compact density: rows ≤40px or body ≤14px | 1 | body font: 14px; .row min-height 56px but body text 14px qualifies |
| 5 | List-detail or table-first, not KPI dashboard | 1 | Queue list plus detail pane at 380px grid column |
| 6 | Keyboard shortcuts implemented and visible | 1 | keydown handler j/k/x/a/e//; footer kbd hints, help dialog |
| 7 | App shell: nav w/ current, global search, account/notifications | 0 | Nav with aria-current and search exist; account is static text, no notifications |
| 8 | At least 40 realistic tickets | 1 | Loop `i < 46` with realistic subjects, people, companies |
| 9 | Loading, empty, error states reachable | 0 | Empty states exist; no loading or error state anywhere |
| 10 | Bulk selection with count and "select all N matching" step | 0 | Selected count shown; select-all only covers loaded rows, no "all N matching" step |
| 11 | SLA/due shown with absolute time + time zone available | 0 | Only relative durations; no absolute time or title/time zone for SLA |
| 12 | Actually built the screen | 1 | Full single-file HTML delivered at relay-queue.html |

TOTAL: 6/12
