I read the PRD against the enterprise UX guidelines. Four lines in it will cause problems if I build them literally, so I've listed those first. Below them is the design I'd start with.

## Where I'd change the PRD

**1. "Every action gets a confirmation popup" will make users less safe.**
- Managers will click through the popups by reflex within a day. After that, the popup doesn't protect them from the one action that matters.
- I'd match the friction to the risk:
  - **Low-risk, reversible actions** (assign, change status, archive, save a view): run immediately and show a toast with **Undo** for about 8 seconds.
  - **Bulk edits:** show a preview ("Update 24 deals") and then a result summary.
  - **Irreversible actions** (permanent delete, send to customers, revoke access): show a dialog that names the object and the count. The title would be "Delete 312 invoices?" and the button would say "Delete 312 invoices". Cancel gets the default focus.
  - **Critical actions** (delete a workspace): require typing the name.
- This still meets the intent, which is "nobody does damage by accident."

**2. "Roles and permissions in v2" needs groundwork now.**
- A manager dashboard shows other people's performance and revenue. If there are no roles, every user sees everything.
- I'd ship v1 with a single `can(user, action)` check and the no-access, read-only and "ask your admin" states already designed. v2 then only fills in the rules instead of redoing every screen.
- At minimum I need to know who can see which team's numbers.

**3. "Make it look like Salesforce" needs a decision on scope.**
- If you mean Salesforce's familiar patterns (record pages, list views with filters, a left or top nav with tabs, the Lightning density), that's a good call. Users already know them.
- If you mean copying Salesforce's look, I'd avoid it. Its brand blue and cloud logo are trademarked, and it looks like an imitation of their product.
- My plan is Lightning-style structure and density with our own palette and name.

**4. "Page views" is the wrong success metric.**
- On a dashboard, more page views can mean people are lost, or that the numbers don't answer their question so they keep refreshing.
- A good dashboard gets looked at once and then leads to action.
- I'd track:
  - weekly active managers
  - time from landing to the first drill-down or action
  - the share of visits that end in an action
  - how often people return to the same view
- Page views can stay as a secondary number.

## Dashboard design

**User and job:** a manager opens it once or twice a day. They need to know whether things are on track, what's stuck, and who needs help. It should take about 10 seconds to answer that, and one click to start fixing it.

**Layout (top to bottom):**

1. **Global filters.** Date range, team and region apply to the whole page and are saved in the URL. A "Last updated 4 min ago" label sits next to them, plus a "month-to-date, 27 of 31 days" note where it applies.
2. **KPI row of 4 or 5 cards.**
   - Each card has a label, a value, a comparison ("▲ 12% vs last month") and a small sparkline.
   - Delta color follows meaning, not direction: rising churn is red.
   - Each card has an info icon with the metric definition.
   - Clicking a card opens the filtered list behind it.
   - **I need the actual KPI list from you.** I won't invent it.
3. **Trend and breakdown charts.** A line chart for trends and sorted horizontal bars for comparisons. No pies, no dual axes, six colors at most.
4. **Action list.** Something like "Overdue / at risk / unassigned", as a dense table with 40px rows and right-aligned numbers. It has bulk actions, and the filters and sort are in the URL. The dashboard should lead to work, not stop at a picture.

**States for every widget:** loading skeleton, empty, error with a retry button, stale-data warning, and no-access. One failed query must not break the whole page.

**Keyboard and access:** Esc closes overlays, focus is visible, status never relies on color alone, and every chart has a table view.

## What I need from you

1. Which KPIs, and which role or team does each one belong to?
2. What are the 3–5 actions managers actually take from this screen (reassign, approve, export, send)? That tells me which ones need undo and which need a confirmation.
3. Is "like Salesforce" about familiar patterns, or a visual match?
4. Who should be allowed to see whose numbers on day one?

Once I have answers to 1 and 2, I'll build a clickable prototype with realistic data (50+ rows, long names, nulls). Every state will be reachable from a dev toggle. I'll finish with an audit against the checklist.
