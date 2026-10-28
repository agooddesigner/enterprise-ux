I built the dashboard as one self-contained file, but I haven't opened it in a browser or run its script. Open it before you rely on it. The data is made up: seven queues, 442 open tickets, 40 agents, and eight accounts about to breach SLA.

**What the VP sees, top to bottom**
- **Recommendation banner:** it says which agents to move and what that does to carryover. With the sample data it comes out as "Move 5 agents" into Billing, Tier 2 and Security. It recomputes from the queue numbers.
- **Five headline numbers:** open backlog, yesterday's first-response SLA, projected carryover, 7-day CSAT, and the oldest open ticket. Each links to its detail, and four show a 14-day trend.
- **Staffing table:** each queue shows open tickets, forecast inbound, agents now, and a stepper for today's agents. It also shows a load bar with a marker at 100% capacity, projected carryover, and a status label. Rows are sorted worst first, and the total stays at 40.
- **Open-tickets chart:** it simulates the day hour by hour, with the current assignments as a dashed line and your edited plan in blue. It has a hover tooltip and a "View as table" option.
- **At-risk accounts:** the top eight accounts about to breach SLA, with ARR, owner and time left. Unassigned owners are flagged.

**Behavior worth knowing**
- **Plan state:** your edited plan is saved in the page URL, so you can share it. "Copy plan summary" puts a text version on your clipboard. Nothing is sent to agents.
- **Page states:** `?state=loading` and `?state=error` show those views.
- **Display:** it follows the system dark mode, and status labels come with an icon as well as colour.

**Assumptions to confirm**
- **Close rates and arrivals:** I invented per-agent daily close rates and an hourly arrival pattern, and they are stated in the footer. Replace them with your own trailing numbers.
- **Cross-training:** the recommendation assumes any agent can move to any queue, with at least one agent kept per queue. In practice Security and Tier 2 probably need a skills check, which the page notes. You may want a "cross-trained pool" column.

The file is at `/tmp/ux-e9b/6NQ2YX/support-dashboard.html`.
