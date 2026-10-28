I wrote the dashboard to `/tmp/ux-e9/I3JAUJ/support-dashboard.html`, but I haven't run or rendered it. This sandbox has no browser, and it blocked my attempts to run a JavaScript syntax check. Open it once in a browser and tell me if anything looks off.

It's a single file with inline CSS and JS and no external dependencies. All figures are made-up sample data, and the footer says so.

- **Today's call:** A banner at the top states the one decision, for example that Integrations and Billing are short while Onboarding has agents to spare. It also shows an active-incident note (a Salesforce sync outage, which is why Integrations is so far behind).
- **Key numbers:** Five tiles cover open tickets, tickets about to breach SLA in the next 4 hours, median first response, CSAT, and agents on shift (37 of 40, with 2 on PTO and 1 out sick).
- **Staffing planner:** This is the main part. It has one row per queue: Technical Support, Billing, Integrations, Onboarding, Enterprise, Security and Escalations. Each row shows work due today, tickets at SLA risk, a coverage bar, a Short/Tight/Covered/Surplus status, and an agent count you can raise or lower with +/− buttons.
  - **Suggested plan:** "Apply suggested plan" spreads the 37 available agents so every queue ends up at about the same coverage. "Reset to today's rota" puts the counts back to the default assignment.
  - **Moves:** The banner and the "moves" list update as you edit, for example "3 Onboarding → Integrations".
- **Charts:** One shows expected inbound tickets by hour today against a typical Wednesday. The other shows open tickets over the last 14 days. Both have hover tooltips and a "View as table" option.

It also follows light/dark mode automatically (there's a Theme button to override), and the layout reflows for narrow screens.

Coverage is the queue's agents times its typical tickets handled per agent per day, divided by the work due today. The suggested plan assumes agents are cross-trained, which the footer notes. In particular, Integrations moves would need API-certified agents.
