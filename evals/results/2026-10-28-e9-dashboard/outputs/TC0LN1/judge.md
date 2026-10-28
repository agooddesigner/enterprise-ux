| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Organised around decisions | 1 | Banner "Move N agents before 08:00"; "where should the 40 agents sit today?" |
| 2 | 3–6 KPI tiles with unit and baseline comparison | 1 | 5 tiles; "vs yesterday (331)", "vs 95% target" |
| 3 | Change direction not colour alone | 1 | ICON.up/down arrows plus text like "+22", "−3.6 pts" |
| 4 | Last updated timestamp | 1 | "Snapshot 07:45 PT · Helpdesk sync every 5 min" |
| 5 | One stated time window / global filter | 0 | Mixed windows: yesterday, 4h, full day, 14-day; none stated globally |
| 6 | Actionable list that drills to records | 0 | Ticket list shows IDs but no links to the underlying records; only queue filtering |
| 7 | Bar/line encodings, no pie/gauge/3D | 1 | Only SVG line charts, no pie, gauge or 3D |
| 8 | Bars start at zero and are sorted | 0 | No bar charts; the trend line axis starts at 240 |
| 9 | Series colour consistent, ≤6 colours | 1 | var(--s1) is Needed and Backlog, var(--s2) Scheduled; few colours |
| 10 | Hover/focus gives exact values or direct labels | 1 | Pointer tooltips give exact values via cfg.tip; table view too |
| 11 | Chart text alternative | 1 | "View as table" buttons plus role=img aria-label |
| 12 | Per-widget loading/error state | 0 | No loading or error states; data is hardcoded |
| 13 | Real support staffing metrics | 1 | Backlog, SLA at risk, first-response SLA, agents needed vs on shift, forecast |
| 14 | Global filters apply to all widgets, in URL | 0 | The queue filter affects only tickets and is not global; it is in the hash |
| 15 | Clear hierarchy: summary top, detail lower | 1 | Banner, then KPIs, then table, charts, tickets |

TOTAL: 9/15
