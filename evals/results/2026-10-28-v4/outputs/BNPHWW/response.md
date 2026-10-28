I've designed the dashboard as a single HTML file, `/tmp/claude-0/-tmp-ux-eval-v4-BNPHWW/882ebbf6-be06-577b-985f-f27acad8a989/scratchpad/cs-dashboard.html`. I haven't opened or tested it in a browser. All the numbers are made-up sample data, and the page says so in a banner. I also haven't published it as an artifact, because my attempt to create one was declined. Tell me if you want it published.

**What it shows, top to bottom:**
- **Filters:** a segment dropdown and 7, 30 or 90 day buttons. In this version they don't change any data yet.
- **Key numbers:** net revenue retention, gross retention, ARR at risk, average health score, CSAT and open escalations. Each has a change figure and a small trend line.
- **Accounts that need action:** the largest at-risk renewals first. Each row shows the health status, the reason, ARR, renewal date and owner, so a CSM can pick up work straight from the list.
- **Health distribution:** healthy, watch and at-risk shares, overall and by segment.
- **Renewals by month:** renewing ARR, with the at-risk part marked.
- **Trends:** net revenue retention over 12 months, and weekly tickets opened versus escalated.

It has hover tooltips, light and dark themes, and a layout that works on a phone. Status is shown with a label as well as color.

**I assumed these; correct me where I'm wrong:**
- You work with Enterprise, Mid-market and SMB segments.
- Health score bands are 50 and 65, with below 50 counted as at risk.
- Renewals within 90 days are the main thing to act on.

To make it real I'd need the source for the data (CRM, support tool or a spreadsheet) and your actual health-score definition. I can also add more views, such as onboarding progress or adoption by feature.
