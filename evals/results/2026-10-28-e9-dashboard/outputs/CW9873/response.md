I built the dashboard as one self-contained HTML file, but I haven't opened it in a browser, so the layout and charts haven't been checked. I tried to find a headless browser to render it, but that command needed approval and I didn't pursue it. Open it once before the VP sees it.

**Layout, top to bottom**
1. **Recommendation banner:** it says how many agents to move and between which queues (for example, "Move 5 agents to cover 3 short queues"). It also shows uncovered demand before and after the plan. "Apply plan" loads the moves into the table below.
2. **Four headline numbers:**
   - Open backlog, compared with last Wednesday.
   - Tickets about to breach SLA in the next 4 hours.
   - Median first response time against its target.
   - CSAT over the last 7 days.
3. **Staffing plan by queue:**
   - The table lists six queues, sorted by how short they are.
   - Each row shows open tickets, forecast inbound, oldest ticket age, SLA breaches in the next 4 hours, agents needed, and agents assigned.
   - A bar shows how far short or spare each queue is.
   - The +/− buttons let the VP try their own plan against the 36 available agents (40 minus 4 out).
   - "Reset to current" restores today's assignments.
4. **Coverage by hour:** agents needed against agents scheduled, with short hours highlighted and a hover tooltip.
5. **Backlog over the last 14 days:** one line with a hover tooltip.
6. **Accounts to watch:** five escalated accounts with ARR, owner and status, sorted by ARR.

**Behavior you should know about**
- **Recommended moves:** they only go between queues that can cover for each other (for example, Account Access to Enterprise Escalations), and a queue is only drained if it has at least one agent of spare capacity.
- **Agents needed:** that is (open + forecast inbound) × average handle time ÷ 390 productive minutes per agent.
- **Display options:** both charts have a Table toggle, and there's a light/dark switch. The layout adapts down to phone width.
- **Status labels:** warnings and critical flags always carry an icon and a label, not just color.

**Data caveat**
All the data is made-up sample data: the queues, account names, backlog history and hourly inbound curve. The ticket counts and the 36 available agents are consistent with each other, but none of it comes from a real system. To use real numbers, the data constants at the top of the script are the place to swap them in.

Files are in /tmp/ux-e9/CW9873:
- support-dashboard.html
