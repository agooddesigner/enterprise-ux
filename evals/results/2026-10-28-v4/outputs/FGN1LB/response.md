I've built the dashboard as a single HTML file with inline CSS and JS. I couldn't render it in a browser here, so nobody has looked at the layout yet, and I never ran the script. I did work through the recommendation logic by hand, and it behaves as described below.

It's built around one question: where do the 40 agents go today?

- **Recommendation:** A banner at the top says how many agents to move and from which queue to which. With today's data it says to move 5 agents: 2 each into Enterprise escalations and API & integrations, from Onboarding, How-to and SSO. That would bring the busiest queue's load down from 141% to about 104%.
- **Staffing table:** Each of the six queues has an agent count with − / + buttons, so the VP can try their own split and watch the load bars and status labels update. "Apply recommended plan" and "Reset" are one click each. Load is the work due today divided by what the assigned agents can close.
- **Headline numbers:** Backlog, tickets near SLA breach, median first response, 7-day SLA attainment and CSAT, each with its target, the change versus last week, and a 14-day trend line.
- **Hourly chart:** Forecast inbound tickets against staffed capacity, with a hover readout and a "View as table" toggle. It shows the 10 AM peak and the lunch dip.
- **Escalations:** Named accounts closest to breaching SLA, with ARR, the reason and time left.

The data is invented but internally consistent. It assumes 37 of 40 agents are in today. Work due today is the inbound forecast plus 35% of the open backlog. The throughput per agent for each queue is an assumption too, and it's listed in the footnote.

The page follows light and dark mode automatically. The staffing-status labels (understaffed, stretched, balanced, spare capacity) each have their own icon, so none relies on color alone.

Three limits:
- The recommendation doesn't check whether an agent is trained for the queue they'd move to. The footnote says so for Enterprise and SSO.
- The page won't update by itself. To use real data, replace the `Q`, `KP`, `ESC` and hourly arrays at the top of the script.
- The hourly chart doesn't change when you move agents in the table.

Files are in /tmp/ux-eval-v4/FGN1LB:
- support-dashboard.html
