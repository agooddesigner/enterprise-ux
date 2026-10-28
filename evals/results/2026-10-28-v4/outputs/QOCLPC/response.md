I've designed the dashboard and saved it as `/tmp/ux-eval-v4/QOCLPC/cs-dashboard.html`. I haven't opened it in a browser, and my script syntax check was blocked, so none of it has been run or checked.

I also couldn't publish it as a shareable Artifact. That publish wasn't approved, so I built a local file instead. I can publish it if you approve.

All figures are made-up sample data, and the page is marked "Sample data". Nothing is connected to your CRM or product usage data yet.

**What's on the page**
- **ARR at risk:** the main number sits top-left in a dark card, split by critical, watch and healthy. It answers "how much money is in danger in the next 90 days?"
- **Four KPI tiles:** net revenue retention, gross retention, average health score and open escalations, each with a trend line and a change since the last period.
- **Renewals by month:** a bar chart of renewing ARR with the at-risk part highlighted, and a tooltip on hover or focus.
- **Health mix by segment:** the share of Enterprise, Mid-market and SMB accounts that are healthy, on watch or at risk.
- **"Needs attention" table:** accounts ranked by ARR, with health score, renewal date, the main warning sign, the owner and a "Create plan" button. You can sort by account, health, ARR or renewal date.
- **Today:** a task checklist.
- **Incident strip:** a banner for a sync problem, so people know when the data may be out of date.

**How it behaves**
- The filters (my accounts or whole team, segment, renewal window) are saved in the page link, so a view can be shared.
- Health is shown with a label and icon as well as a colour.
- The no-results view has a "Clear filters" button.
- "Create plan" shows an Undo toast.
- It works in light and dark themes, on a phone, and with a keyboard.

**Not built yet:** loading and error views, and real data.

Questions for you:
- Which metrics does your team actually run on? I assumed retention, health score, escalations and renewals.
- How do you calculate health score, and what are its inputs?
- Is the main user a CSM working their own accounts, or a manager looking across the team? I assumed the CSM and gave it a "My accounts" default.
