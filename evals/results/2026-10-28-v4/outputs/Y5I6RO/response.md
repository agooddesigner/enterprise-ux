I wrote the dashboard to `/tmp/ux-eval-v4/Y5I6RO/support-dashboard.html`, but I haven't opened it or run its script. No browser is installed here, and the command I tried for a headless script check needed approval, so I stopped. Open it once in a browser before you rely on it. The staffing figures below come from working the numbers by hand, so check them against the page.

It's a single file with inline CSS and JS and no external dependencies. It has light and dark themes, and it works on a phone.

**How it's laid out, top to bottom:**
1. **Recommendation banner.** It tells the VP what to do first, for example "Move 3 agents out of Technical Support first thing."
   - It lists each move with a reason: queue, agent count, and the breached and at-risk counts.
   - It then lists what's still uncovered after the moves, with a suggested lever for each (overtime, deferring low-priority tickets, and so on).
2. **Five key numbers.** These are open tickets, SLA breached now, tickets that will breach in the next 4 hours, median first response, and 7-day CSAT. Each compares against yesterday or its target.
3. **Queue table.** There are 8 queues, sorted by urgency.
   - Each row shows status, open, breached, at-risk, and oldest ticket.
   - A bar compares agents assigned with agents needed, followed by the gap and a 14-day backlog sparkline.
   - A toggle switches the view to "After recommended moves."
4. **Inbound tickets by hour.** It compares today's forecast with yesterday's actuals, with a hover tooltip and a table view.
5. **Accounts to watch.** It lists large accounts with breached or at-risk tickets.

**How the recommendation is worked out.** Workload is the breached plus at-risk tickets, plus today's forecast inbound, plus 40% of the other open tickets. Agents needed is that workload divided by what one agent clears in a day, rounded up. Agents move only between queues they're cross-certified for, and each move goes where one more agent relieves the most SLA pressure.

**What it shows with the sample data.**
- 37 of 40 agents are on shift (three are out).
- Technical Support has 3 spare agents; two go to Integrations & API and one to Escalations.
- Even after that, Escalations, Integrations & API, Onboarding and Security & Compliance stay short by 5 agents in total, and the banner flags those for a decision.

All the data is invented for illustration, and the customer names are fictional. The queue numbers, hourly forecast, account list and the figures for CSAT, first response and yesterday's comparisons are all hardcoded at the top of the script, so you can edit them or connect a real feed there. The footer also states the staffing formula so a reader can see how "needed" is derived.
