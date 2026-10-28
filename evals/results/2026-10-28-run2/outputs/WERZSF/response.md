I haven't built any screens yet. Three of the five requirements would produce the wrong product if I took them literally, and the PRD never says which KPIs "all the KPIs" means. A mockup now would use invented numbers, so I've written a grill log and a design direction first.

## Grill log: Manager KPI dashboard, round 1

| # | Question | Why it matters | Default I'll assume | Risk if wrong |
|---|---|---|---|---|
| 1 | Which 3–5 decisions should a manager make from this? ("Is my team on target?", "Which accounts are at risk?") | "All the KPIs" produces a wall of tiles. A dashboard has to support specific decisions (NN/g). | Pipeline vs. target, at-risk deals, team activity, forecast, and a short "needs attention" list | High: wrong content means a redesign |
| 2 | Which data sources, how fresh, and how many records per tenant? | This decides loading and stale-data states, and whether one slow query can blank the page. | Several sources, refreshed every 15 min, 20k records at p95 | High |
| 3 | Do all managers see everything? | Managers usually see their own team, and directors see more. This changes the data on every tile. | Managers see their own team. Directors see their org. | High |
| 4 | Is the dashboard read-only, or can managers act from it? | It decides whether any "actions" exist at all. | Read-only, with drill-down links to the underlying records | Medium |
| 5 | What does success mean for the user? | See pushback 3 below. | Time to answer a weekly review question, plus return use by managers | Medium |

## Pushbacks

1. **"Every action should have a confirmation popup."**
   - Confirm dialogs on everything train people to click through without reading, and they slow down experts. NN/g and Ant recommend Undo for reversible actions.
   - Replace the blanket rule with three tiers:
     - **Reversible actions** run immediately and show an Undo.
     - **Irreversible single actions** get a confirm dialog that names the object and the consequence.
     - **Critical or bulk actions** need typed confirmation.
   - A read-only dashboard may have almost no destructive actions anyway (question 4).

2. **"Roles and permissions in v2."**
   - The PRD is a manager dashboard, so roles already exist in v1. Retrofitting RBAC changes the states of every screen, and enterprise buyers will ask about it in a security review.
   - For v1, I'd ship a minimal scope: managers see their team's data only. Each widget gets a designed no-permission state, so v2 extends the design instead of redoing it.

3. **"Success metric: page views."**
   - Page views can't tell us whether the job got easier. A confusing dashboard that people reload to hunt for numbers scores well on them.
   - Better signals:
     - time from landing to a drill-down, or to "done"
     - weekly return rate among managers
     - how many KPI tiles get opened
     - how many "where is X?" support tickets come in
   - Page views can stay as a secondary metric.

4. **"Make it look like Salesforce."**
   - I'll follow Lightning's conventions (density, 12-column grid, tile and header patterns, and clear page structure). I won't copy their logo, brand marks or exact blue.
   - Which part do you want? Density and familiarity, the enterprise CRM feel, or something specific like record pages or list views? That decides how closely I follow Lightning.

## Design direction (assuming the defaults above)

- **Job:** a manager opens the dashboard once or twice a day, usually before a weekly review, to see where the team stands and what needs attention.
- **Type:** operational and static. It gets no widget customisation in v1, and I won't mix operational and analytical views on one page.
- **Layout:**
  - A global header with the date range and team scope.
  - A row of 4–5 KPI tiles at the top.
  - One main trend chart.
  - One "needs attention" list of 5–10 items, linking to the full page.
- **KPI tiles:** each shows the label, value and unit, the comparison baseline ("vs prior 7 days"), and when it was measured. Direction is shown with an arrow plus text, not colour alone. All tiles share one time window. Each tile links to its breakdown.
- **Charts:** line for trends, bullet for progress to target. No pies, donuts or gauges. Each chart has a "View as table" toggle.
- **States:** every widget has its own loading, empty, error (with Retry), no-permission and stale state. A failed value shows "—", never 0. One failing widget never blanks the page.
- **Accessibility:** WCAG 2.2 AA from the start. That covers contrast on chart marks, a keyboard path through every tile, and a text alternative for every chart.

## Most dangerous open question

**Which KPIs does this dashboard show, and what decision does each one support?** I'll treat the defaults above as the starting list. The best reply is your real KPI list with one line each on what the manager does when the number moves.

Once I have that, or if you tell me to go with my defaults, I'll build a clickable Lightning-style mockup (as an Artifact page) showing every state.
