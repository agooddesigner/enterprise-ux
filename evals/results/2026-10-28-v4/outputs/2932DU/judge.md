| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit assumptions about users/data volume/roles | 1 | Header comment: "support agents triage and clear 40–150 tickets a day"; roles agent/viewer |
| 2 | Names visual direction (style/dial choices) | 1 | "calm, dense work surface… cool-grey canvas… one indigo accent"; comfortable/compact density |
| 3 | Direction justified by context | 1 | "people who live in it 8 hours a day… speed + keyboard beat decoration" |
| 4 | Compact density: rows ≤40px or body ≤14px | 1 | `--row:40px`; body font 14px; compact 32px |
| 5 | List-detail / table-first, not KPI dashboard | 1 | Table queue plus side `.detail` panel with thread |
| 6 | Keyboard shortcuts implemented and visible | 1 | Footer `<kbd>j</kbd> <kbd>k</kbd>…`; keydown handler; help dialog |
| 7 | App shell: nav w/ current, global search, account/notifications | 0 | Nav aria-current and account "Priya Nair" exist, but there's no notifications; search is only in the list toolbar, not global |
| 8 | At least 40 realistic tickets | 1 | 240 generated tickets from 18 realistic subjects, people, orgs |
| 9 | Loading, empty, error states reachable | 1 | `?state=loading/empty/error` and footer links; renderList branches |
| 10 | Bulk selection with count and "select all N matching" | 1 | `${nSel} selected`; "Select all ${P.total} matching" button |
| 11 | SLA/due with absolute time + time zone | 1 | `title="Due ${abs(t.due)}"` with timeZoneName:"short" formatter |
| 12 | Actually built the screen without asking | 1 | Complete HTML file delivered |

TOTAL: 11/12
