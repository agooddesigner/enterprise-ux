I wrote the dashboard, but I couldn't check it. I never saw it rendered and never ran its script. There's no local Chrome, the Chrome extension wasn't permitted, and the Node smoke test I wrote needed approval that I didn't get. So the layout and the JS are untested, and bugs are possible.

**File:** `/tmp/ux-e9v3b/OP256U/support-staffing-dashboard.html`. It's a single file with inline CSS and JS and no external dependencies.

The page is organised around what the VP has to decide each morning:

- **Headline:** The title is computed from the data, e.g. "Integrations & API is 4.5 agents short; Onboarding has 2.1 to spare."
- **Recommended moves:** A dark card at top-left shows "3 agents to reassign before 09:00".
  - It lists two concrete moves with named agents. Priya Raman and Tomás Herrera go from Onboarding to Integrations. Hannah Okafor goes from Technical to Access & SSO.
  - Each move has a Reassign button, and there's a "Reassign all" button.
  - Moves show an Undo toast, and every number on the page recalculates when you apply them.
  - Predicted SLA goes from about 78% to about 88%.
  - It also says plainly that Integrations stays about 2.5 agents short after the moves.
- **KPI tiles:** Open tickets, oldest unanswered, predicted SLA against the 95% target, and agents available (36 of 40). Each one links to the relevant detail.
- **Staffing chart:** Agents assigned versus needed per queue, with the shortfall hatched.
- **Who's out:** The 4 people out today.
- **Hourly chart:** Ticket volume against staffed capacity, with over-capacity hours marked, a "now" line, and hover or keyboard tooltips.
- **Queue table:** Sortable. Clicking a queue opens a dialog with its oldest tickets.
- **Filters and state:** Queue filter chips plus sort order and the open queue are saved in the URL. A "Preview state" selector in the footer switches between ready, loading, error and empty views.
- **Incident strip:** An INC-2291 webhook-delay incident strip sits above the cards.

The data is made up but consistent: 612 tickets across 6 queues, a forecast of 1,449 tickets, and the staffing numbers add up. "Agents needed" and "predicted SLA" come from a simple formula I invented, not a real model. Swap in your real figures before anyone relies on them.

Open the HTML file in a browser and tell me what looks wrong. If you approve the browser tool or the Node test, I can run the checks myself and fix what turns up.
