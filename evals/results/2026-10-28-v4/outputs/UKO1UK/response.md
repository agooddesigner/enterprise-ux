I've built the dashboard as one self-contained HTML file. I couldn't open it or run the script, because the command to check it needed approval and I didn't get it. So I haven't looked at it rendered, and layout or script bugs could still turn up. The numbers I worked through by hand do check out: Billing ends up 2 agents over, and Integrations and Data & Reporting end up short.

It's built around the VP's morning question, "where do my agents go today?":

- **Staffing call (top left):** A dark hero card gives the main answer. With the sample data it reads "Move 2 agents out of Billing & Invoicing". Underneath are concrete moves, such as 1 agent to Integrations & API, each with its own Apply button, plus an "Apply all" button. After you apply a move, a toast appears with Undo. The bottom line says the workload needs 39 agents against 36 working, so the team is 3 short even after the moves.
- **Headline numbers:** Four tiles with 14-day trends: open backlog (396), tickets set to breach SLA by noon (60), median first response (23 min) and CSAT over 7 days (91.2%). Each tile has a delta against its target or yesterday.
- **Queue table:** Seven queues, each with open tickets, inbound forecast, oldest waiting ticket, breach risk, and assigned versus needed agents. Needed agents come from forecast inbound plus 35% of the backlog, times average handle time, divided by 6 productive hours per agent. You can sort it, filter it (all, needs agents, covered), and search it with `/` or ⌘K. Sort, filter and search are saved in the URL.
- **Hourly chart:** Inbound tickets against capacity for each hour, with a hover tooltip. Hours running at 90% or more of capacity are highlighted, with a callout to hold breaks until after the 10:00–12:00 peak. A Table toggle shows the same numbers as text.
- **Side cards:** Who's working today (36 of 40, with the out-of-office breakdown) and five escalated accounts with ARR, age and owner.
- **Page shell:** Side navigation, breadcrumbs, a freshness timestamp, a Refresh button and the notification and account buttons.
- **Preview states:** The footer has a "Preview state" selector for the loading, error and ready views. Each card shows its own loading placeholder or error message with a Retry button. You can also reach these states with `?state=loading` or `?state=error`.

**Notes:**
- All data is invented but internally consistent; it's in the `QUEUES` and `ESC` arrays at the top of the script, so you can swap in your own.
- The "View tickets" links and the nav items other than Today and Queues are placeholders (`#`).
- There is no dark mode.

The file is at `/tmp/ux-eval-v4/UKO1UK/support-staffing-dashboard.html`.
