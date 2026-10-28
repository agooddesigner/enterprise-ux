| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Decisions stated / organised around them | 1 | "Recommendation" banner; "Where the 40 agents are today" staffing table |
| 2 | 3–6 KPI tiles with unit and stated baseline | 1 | 5 tiles; "vs last Wed", "vs 95% target"; units %, tickets |
| 3 | Change direction via arrow/icon/text, not colour alone | 0 | Tags use triangle/circle/check status icons and signed text (+38, −3.6), but no direction arrows |
| 4 | Visible last-updated timestamp | 1 | "Updated 08:10 PT" in header, `#fresh` |
| 5 | One stated time window / global filter | 1 | "Window: today 08:00–17:00 PT" in header |
| 6 | Actionable list linking to records | 1 | At-risk accounts table with ticket links `#/tickets/…` |
| 7 | Length/position encodings only; no pie/gauge/3D | 1 | Line chart, load bars, sparklines only |
| 8 | Bars start at zero and categorical bars sorted | 1 | Load bars start at 0; table rows sorted by load descending |
| 9 | Consistent series colours, ≤6 colours | 1 | Current = grey dashed, plan = accent blue, consistent |
| 10 | Hover/focus exact values or direct labels | 1 | Chart tooltip on hover; load % labelled directly |
| 11 | Text alternative / view as table | 1 | `<details>` "View as table" plus svg aria-label |
| 12 | Per-widget loading/error state, one failure doesn't blank dashboard | 0 | Loading/error are page-wide `?state=`, not per-widget independent failure |
| 13 | Real support staffing domain metrics | 1 | Backlog, first-response SLA, carryover, agents, forecast inbound |
| 14 | Global filters apply to all widgets and reflected in URL | 0 | No team/region/channel filters; URL stores only plan |
| 15 | Clear hierarchy, summary top, detail lower | 1 | Banner, then KPIs, then table/chart, then risk list |

TOTAL: 11/15
