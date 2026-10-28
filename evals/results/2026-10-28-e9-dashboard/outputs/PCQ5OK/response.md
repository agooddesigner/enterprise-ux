The dashboard is written, but I haven't run it. Chrome wouldn't open a local `file://` page, and the shell blocked every command I tried for syntax-checking the script, so it's untested. Open it once before relying on it. If something looks broken, the browser console will show the error.

**File:** `/tmp/ux-e9b/PCQ5OK/support-staffing-dashboard.html` (single file, inline CSS and JS, no network calls)

**What it shows**
- **Headline:** a sentence generated from the data that says where the pressure is. With the sample data, Billing and Integrations & API are covered at 62% and 65%, and the team is about 3.8 agents short overall.
- **Four key numbers:** queues under 80% coverage, tickets at SLA risk, open backlog, and expected new tickets today. Each shows its comparison baseline.
- **Staffing planner:** the core of the page. Seven queues, each with backlog, SLA risk, forecast, agents needed, agents now, a plus/minus stepper for the plan, and coverage. Coverage updates live as you adjust, and the key numbers and chart follow.
  - **Recommended moves:** "Apply recommended plan" evens out coverage across queues, and "Reset to current roster" puts the original assignment back. Both offer Undo.
  - **Copy plan:** copies a Slack-ready summary to the clipboard.
- **Workload vs. capacity by hour:** for the selected queue, with the shortfall shaded and a "Now 08:10" marker. Hover or arrow keys read exact values, and there's a Table toggle.
- **Backlog trend:** the last 14 days, with last Wednesday called out.
- **Next tickets to breach SLA:** eight tickets with customer, ARR and time left.

**Things to know**
- The data is invented but internally consistent: 40 agents on roster, 37 in (2 PTO, 1 sick), 576 expected tickets.
- "Agents needed" is my own formula: forecast tickets plus 40% of the backlog, divided by tickets resolved per agent per day. It's explained in a "How needed is calculated" note on the page. Swap in your real staffing model before trusting the numbers.
- The sort order and chosen queue are saved in the URL. Each panel has a loading state, and the tickets and trend panels have error and empty states. A "Preview state" dropdown in the footer switches between them.
- The ticket, queue and "View all" links point to `helpdesk.example.com` placeholders.
- The page follows your system's light or dark setting.
