I built the first design pass as a local HTML prototype, but I haven't published it. The publish call was declined, so there's no link. You can open it from this path: `/tmp/claude-0/-tmp-ux-run2-U1GCBY/882ebbf6-be06-577b-985f-f27acad8a989/scratchpad/kpi.html`. I can publish it as a private page if you want one. I haven't opened or tested it in a browser.

**What's in it**
- **Layout:** a dark global header, a tab bar (Overview, Sales, Support, People), and a grey canvas with white bordered panels. It has a blue accent and light and dark themes.
- **Headline row:** six KPI tiles, each with the current value, change versus the prior period, target, and a sparkline.
- **Charts:** revenue against target, with a hover readout and a 4, 8 or 12 week range. Next to it, quota attainment by team.
- **KPI table:** searchable, with status shown as a pill that has an icon and a label, so it doesn't rely on color alone.
- **Sample data:** all numbers are made up and labeled "Sample data". The PRD doesn't say which KPIs managers need.

**"Looks like Salesforce"**
I matched the Lightning style: the shell, spacing, density and blue. I used no Salesforce name, logo or mascot, and a Google font instead of their proprietary one. Copying their branding outright would be a legal and trust problem, so I'd keep it as inspiration.

**Where I departed from the PRD, and what to decide**
1. **Confirmation on every action.** I didn't do this.
   - Constant popups train people to click through them, which makes the real dangerous ones less safe.
   - In the prototype, "Remove KPI" is permanent and shows a confirmation naming what will be deleted. Export and Refresh just show a short toast.
   - For reversible changes, toast plus Undo is the safer pattern.
   - If you really want confirmation on all of them, it's a small change. Tell me and I'll switch it.
2. **No roles until v2.** This is fine for a first release only if every manager can see every KPI, including people and attrition data. Please confirm that's acceptable, or at least that HR-type KPIs are left out of v1. It's worth designing the layout now so v2 permissions don't force a redesign.
3. **Success metric: page views.** I'd replace it. On a dashboard, more views can mean people can't find what they need. Better candidates are weekly active managers, time to answer a question, or how often the exports and follow-up actions are used. Which decision is this dashboard meant to speed up?

**Questions I need answered**
- Which 6 to 8 KPIs matter most, and where does each one's data come from?
- Who are the managers: sales, support, or all teams? That decides the default tabs.
- Do you need desktop only, or phone too? The layout already adapts to phone width.
