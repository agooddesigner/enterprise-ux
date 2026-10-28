I built the dashboard at `/tmp/ux-e9/BHKRG0/support-dashboard.html`. It's one self-contained file with inline CSS and JS, and no external requests. I have not opened it in a browser or run its script, because both were blocked here. Open it once before the VP does, and tell me what looks off.

**What the VP sees, top to bottom**
- **Incident banner:** a webhook outage (INC-4471) is driving Integrations & API inbound to 3.1× normal.
- **Six headline numbers:** open backlog, yesterday's first-response SLA, tickets at risk of breaching today, oldest unanswered ticket, CSAT, and agents on shift (36 of 40, with the names of who's out on hover).
- **Recommendation:** says how many agents to move, from which queues, to which, and why. "Apply recommended plan" loads it into the table.
- **Queue table (7 queues):** shows open tickets, at-risk tickets, oldest wait against SLA, rest-of-day inbound, agents needed and agents staffed now. The "Plan for today" column has − / + steppers. The plan is capped at the 36 agents on shift, and status updates as you move people.
  - **Plan sharing:** "Copy plan" produces a Slack-ready summary, and the plan is stored in the URL so a link carries it.
- **Two charts:** inbound tickets per hour (today, with the forecast part dashed, against last Wednesday) and open backlog over 14 days. Both have hover tooltips and a Table toggle.
- **Named accounts nearest an SLA breach:** ARR, days to renewal, owner, and which tickets have no owner.

**How "agents needed" is calculated:** (rest-of-day inbound + tickets that will breach today) × average handle time ÷ 330 productive minutes per agent. The recommendation then gives each agent to whichever queue has the lowest coverage so far. With the seeded numbers the day needs about 39 agents' time against 36 available. The plan therefore spreads the shortfall rather than leaving one queue badly short.

**Other details**
- All numbers are made up. The whole snapshot is fixed at Wed Oct 28, 2026, 08:05 PT.
- **Status labels:** status never relies on colour alone. Each has an icon and a word, such as Breached, Tight or Surplus.
- **Theme:** light and dark themes are supported.
- **Extra states:** add `?state=loading` or `?state=error` to the URL to see those screens. The error screen deliberately shows no figures rather than stale ones.
- **Refresh button:** it only simulates a reload, since there's no live data source. It shows "already up to date".

To make it real, replace the seeded `Q`, `TODAY`, `BACKLOG` and `ESC` arrays near the top of the script with your ticketing-system feed. The rest derives from them.
