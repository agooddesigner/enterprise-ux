The dashboard is at `/tmp/ux-eval-v4/8Z2L04/support-staffing-dashboard.html`. It's one HTML file with inline CSS and JS and no dependencies. I couldn't run it or open it in a browser. The tool that would run the code needed approval I didn't have, so the layout and the reallocation logic are untested, and one number in the dashboard is a guess (the hero card's figures depend on random cross-training).

**What it shows**
- **Recommended reallocation:** the top card suggests moves such as "Move 2 agents from Tier 1 → Integrations & API". Each move names the agents (only those cross-trained in the target queue) and shows coverage before and after.
- **Buttons on the card:** per-move "Apply move", "Apply all", "Reset to default roster" and "Send plan to team leads". Every apply shows an Undo toast. "Send" is a demo and sends nothing.
- **Headline tiles:** queues short on coverage (before and after the moves), tickets waiting, tickets about to breach SLA in the next 2 hours, first-response SLA today, and the oldest waiting ticket.
- **What's different today:** three notes, for example an API deprecation email driving Integrations up 42%, an open Sev 2 incident, and month-end billing on Friday.
- **Queue table:** 8 queues sorted by least coverage first. Each row has a coverage bar, agents versus agents needed, SLA against target, oldest ticket, volume versus a typical Wednesday, and a 7-day backlog sparkline.
- **Queue detail:** click a queue to open a panel listing its agents with their skills. You can move one agent at a time from there.

**How coverage is worked out**
- Coverage is agent hours available divided by hours of work due today. Work due is tickets waiting plus forecast new tickets, multiplied by average handle time.
- Each agent counts for 6 productive hours. That figure and the queue data (volumes, handle times, SLA numbers, agent names) are invented to look realistic, so swap in real numbers.
- Totals are 40 agents, 249 hours of work against 240 hours of capacity. Moving agents reshuffles that capacity and doesn't add any. If the moves can't close a gap, the card says so and suggests overtime or deflection instead of overpromising.

**Also built in**
- Sort order and the open queue are saved in the URL.
- Loading, error and ready states, switchable from the footer or with `?state=error`.
- Light and dark themes.
- Status is shown with text and an icon, not colour alone.
- Keyboard and screen-reader support.

**Needs checking:** I changed the skill mapping so Billing and Renewals agents can cover SSO, but I couldn't confirm this gives sensible recommendations. I expect about three moves, with Bugs & Escalations left short and flagged in the residual message. Please open it and check that card first.
