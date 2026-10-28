I designed a customer success dashboard and saved it at `/tmp/ux-eval-v4/3XC7Y8/cs-dashboard.html`. I haven't opened it in a browser, so layout and the filters are untested.

My attempt to publish it as a shareable artifact didn't go through (it looks like the approval was declined), so it's only a local file. Tell me if you want it published.

All figures are sample data that I made up, and the page labels them that way. Nothing is connected to a real source.

**Layout, top to bottom**
- **Revenue at risk:** this is the dark card at top left, since it's the first thing a CSM needs to know. It's followed by six KPIs: net revenue retention, gross churn, NPS, first-response time, open escalations and onboarding on track.
- **Accounts by health:** a 12-week stacked bar chart of healthy, needs-attention and at-risk accounts.
- **Renewals, next 90 days:** bars of ARR renewing each month, shaded red when more than 25% is flagged at risk.
- **Accounts needing action:** a worklist sorted with at-risk accounts first, then by ARR. Each row shows the main signal, the owner and when the account was last contacted. It has search and a segment filter (all, Enterprise, Mid-market, SMB).

**Choices I made**
- The segment filter is saved in the page URL, so a filtered view can be shared as a link.
- Health is shown as a coloured pill with a text label, so it doesn't depend on colour alone.
- The page has light and dark themes and works at phone width.
- The page has no loading or error states yet.

**Questions for you**
- Which metrics does your team use, and what counts as "at risk" (health score, usage drop, overdue invoice)?
- Where does the data live (CRM, support tool, billing)? I can build the live version once I know.
- Do you need separate views for CSMs and for managers?
