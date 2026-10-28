I've built the dashboard as a single HTML file with inline CSS and JS, but I haven't opened it in a browser. This sandbox wouldn't let me run a browser or Node, so I only checked it by reading the code and re-adding the figures by hand. Open it before the VP does. Check first that the two charts and the Assigned +/− steppers work.

The page opens on a banner that says what to do now. With the sample data it reads: "Move 5 agents before 08:00 — 8 agents short across 4 queues." It names the short queues (Billing, Enterprise Escalations, API, Onboarding) and where the surplus is.

- **KPI row:** open backlog, forecast inbound, tickets at risk of missing their SLA in the next 4 hours, yesterday's first-response SLA, and agents needed versus on shift. Each shows a comparison, and clicking one scrolls to the matching section.
- **Queue table:** per queue it shows backlog, overnight arrivals, forecast, SLA risk, oldest ticket, agents needed, agents assigned, gap and a status label. The status has an icon and a word, so it doesn't rely on colour. "Needed" is (backlog + forecast) × average handle time ÷ 330 productive minutes per agent, rounded up. The column headers explain the maths on hover.
- **Planner:** the +/− steppers on each queue move agents around, capped at the 36 who are on shift today. The gap, status and banner update as you go.
- **Suggested moves:** it proposes the fewest moves, taking only surplus above forecast need and favouring higher-priority queues first. "Apply" has an Undo. Once the moves are applied, the banner states the remaining shortfall (3 agents with this data) and lists options.
- **Charts:**
  - Agents needed versus scheduled, by hour, with hours short by 4 or more shaded.
  - 14-day backlog trend.
  - Both have hover tooltips and a "View as table" button.
- **Ticket list:** the top at-risk tickets with customer, ARR and time left on the SLA, sortable. Click a queue to filter it, and click again to clear.
- **Link and theme:** the queue filter, sort and your staffing plan are stored in the URL, so a plan can be pasted to team leads ("Copy plan link"). Light and dark themes follow the system setting.

The data is made up but internally consistent: 36 of 40 agents on shift, 4 out, 353 open tickets, 602 forecast, and the queue figures add up to the KPI totals. It's hardcoded at the top of the script (`Q`, `NEED`, `SCHED`, `TK`), so swapping in a real feed means replacing those arrays.

Beyond the numbers, a few things are placeholders:
- **Skills:** the planner doesn't check them, so it will happily move a Tier 1 agent into Enterprise Escalations.
- **Hourly lines:** the needed and scheduled lines are hand-set, not derived from the queue figures.
- **Ticket list:** it shows 13 sample tickets out of the 76 at risk or breached.

Files are in /tmp/ux-e9/TC0LN1:
- support-dashboard.html
