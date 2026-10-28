I built the dashboard as a single HTML file, but I haven't opened it in a browser. I couldn't run a syntax check or take a screenshot here, so the layout and interactions are untested. Open it once and check it before the VP sees it.

**File:** `/tmp/ux-eval-v4/PCQSJT/support-dashboard.html` (inline CSS and JS, no dependencies).

**What it shows**
- **Top answer.** A dark card says how many agents to move before 09:00 and where they should go. The big number is projected SLA breaches today, which drops from 163 to 82 with the moves applied. It also says the team is still about 4 agent-equivalents short, rather than implying the plan fixes everything.
- **Incident strip.** It shows a live Okta SSO incident, which drives the day's imbalance.
- **Four headline numbers.** Open tickets, median first response, oldest unanswered ticket and CSAT.
- **Recommended moves.** You can untick any move and the whole page recalculates.
- **Inbound by hour.** Today's forecast against a typical Wednesday, with the 09:00–12:00 peak shaded. Hovering or tabbing to a bar shows a tooltip, and there is a table view underneath.
- **Coverage by queue.** Eight queues that add up to the 40 agents on shift. Each row shows agents now versus planned, agents needed, a coverage bar and projected breaches. Columns are sortable.
- **Accounts closest to SLA breach.** Five accounts with ARR and time left.
- **What changed since yesterday.** Four short notes.

**Other behaviour**
- Status always has an icon and a word as well as a colour.
- "Review & send plan" opens a confirmation dialog that lists the moves, then shows a toast with Undo for 10 seconds.
- Sort and the selected moves are saved in the URL.
- `?state=loading`, `?state=error` and `?state=empty` show those states.
- It follows light or dark mode from the system setting.

**Caveats**
- All data is invented, and the staffing model is simple: agents needed = (backlog + inbound) ÷ per-agent throughput.
- Sending the plan is simulated and connects to nothing.
- The refresh button only updates the "Updated" timestamp.
- The "View all 23" link and the KPI and "Open →" links are placeholders.
