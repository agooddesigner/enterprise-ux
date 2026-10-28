I haven't drawn any screens yet. The PRD has four requirements that would each cause a rebuild or a bad product if built as written, so I'm raising those first. I've also drafted a design brief with the assumptions I'll use unless you correct them.

## Pushbacks on the four requirements

| PRD line | Problem | What I'd do instead |
|---|---|---|
| **"A dashboard with all the KPIs"** | "All the KPIs" produces a wall of tiles that supports no decision. NN/g and Cloudscape say to name the 3–5 questions the page must answer. | Pick the decisions first (see question 1 below). Put KPIs at the top, then one actionable "needs attention" list. Each tile gets a unit, a comparison baseline, a "measured at" time, and a drill-down. |
| **"Every action has a confirmation popup"** | Users learn to click through it, and experts get slower. Nielsen Norman Group and Ant Design recommend Undo for reversible actions. A popup that appears every time protects against nothing. | Use three tiers. Reversible actions run immediately with an Undo toast. Irreversible single-item actions get a confirmation that names the object and the consequence. Cascading or bulk-critical actions get a typed confirmation. |
| **"Roles and permissions in v2"** | Retrofitting permissions changes the states of every screen. Managers will see revenue, headcount or customer data that not every manager should see. Enterprise buyers treat RBAC and an audit trail as must-haves, and they ask about them in security review. | Ship a minimal v1: 2–3 fixed roles (Admin, Manager, Viewer), a permission matrix, and the "no access" state designed for every widget. Leave custom roles for v2. |
| **"Look like Salesforce"** | This is fine as a convention, since users who know Lightning will find it familiar. It isn't a job, though. Copying it also copies Salesforce's density and clutter. I also shouldn't reproduce their branding. | Use Lightning's conventions: app shell, page header, card grid, and user-selectable density. Build it with your own tokens and name. Tell me if you meant "match our existing Salesforce-based tooling". |
| **"Success metric: page views"** | Page views can't tell you whether the job got easier. A dashboard that answers the question at a glance gets fewer views. Rising views can mean people can't find things. | Use a task-based metric (see below). |

## Proposed success metrics
- **Task success:** a manager answers the key question ("Are we on target? What needs me?") in under 30 seconds, measured in moderated testing.
- **Time to first action:** the time from landing to opening a drill-down or acting on an item.
- **Weekly active managers** as an adoption signal, with a median-session-length cap so longer isn't counted as better.
- **Attitude:** SEQ after the key task.
- Keep page views only as a secondary diagnostic.

## Design brief (draft)
- **Outcome:** managers can see how their area is performing and act on exceptions without asking an analyst or opening a spreadsheet.
- **Primary job:** "When I start my day or go into a 1:1 or review, I want to see which KPIs are off-target and why, so I can act or escalate." I'm assuming daily use, low-to-medium criticality, and a laptop at 1280–1440px.
- **Audiences:** managers (primary), an admin who configures KPIs and access, and executives who view only.
- **Page type:** an analytical dashboard that is static and not configurable in v1. It doesn't mix operational and analytical views. Anything that needs real work (long lists, bulk actions) lives on a normal list page.
- **Layout:**
  - A global filter bar at the top (time range, team or region), with state in the URL so views can be shared.
  - 4–6 KPI tiles, all on the same time window and the same data source.
  - A trend chart per question.
  - An actionable "needs attention" top-N list.
  - Freshness ("Updated 3 min ago") and a metric-definition popover on every tile.
- **States:** every widget has its own loading, empty, error (with Retry) and no-permission state. One failing widget never blanks the page, and a failed value shows "—", never 0.
- **Accessibility:** WCAG 2.2 AA. Every chart has a "View as table" option, and trend direction is shown with an icon and text as well as colour.
- **Out of v1:** custom roles, configurable widgets, AI summaries.

## Questions that would change the design
1. **Which decisions should this support, and for which managers?** What are the top 3–5 questions? Do all managers see the same KPIs, or only their own team's? *My default: each manager sees their own scope, and the 3–5 KPIs per role are agreed with you.*
2. **Where does the data come from, and how fresh must it be?** Is it Salesforce itself, a warehouse, or several sources? *My default: one source, refreshed every 15 minutes or so.*
3. **How many teams, regions and records do you have at p95?** This decides whether filters are simple dropdowns or searchable pickers. *My default: 50 teams and up to 20,000 records in the drill-down.*
4. **Which actions can a manager take from here?** Approve, reassign, export? Which can't be undone? *My default: export and "assign owner" are reversible, and nothing is destructive in v1, so confirmation popups are mostly unnecessary.*
5. **What does "like Salesforce" mean for you?** Is it a brand requirement, a familiarity argument, or a request to match an existing system? *My default: Lightning-style conventions with our own branding.*

The riskiest open question is #1. If the KPI list isn't tied to decisions, we'll end up with the chart wall.

If you answer these (or tell me to go with my defaults), I'll build a clickable HTML prototype of the dashboard with all the states, a minimal role switcher, and the tiered confirmation pattern.
