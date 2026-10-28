I couldn't run a syntax check or render the page here, because the shell commands needed approval. The dashboard is written, but it hasn't been run or looked at yet.

The file is `/tmp/ux-e9/WSG5DM/support-dashboard.html`. It's a single file with inline CSS and JS, no dependencies, and it follows light or dark mode from the system setting.

**What it shows, top to bottom**
1. **Header:** the date, a "data as of 8:10 AM" stamp, and 37 of 40 agents on shift (2 on PTO, 1 sick).
2. **Incident banner:** a webhook-delay incident that explains why API inbound is up 38% today.
3. **Five KPI tiles:** open tickets, SLA at risk in the next 4 hours, SLA met yesterday, median first response, and CSAT. Each has a delta against target or last week and a 14-day trend line.
4. **Recommendation:** the staffing move to make today.
   - It moves 3 agents out of Billing and 1 out of SSO, and puts 2 into Escalations and 2 into Technical: API.
   - It also states what the move can't fix. Technical: API stays about 16 tickets over capacity, so it suggests overtime or a status-page banner.
   - **Apply recommended plan** fills the table with that plan, and **Reset to current** puts it back.
5. **Queue table:** 6 queues showing what's due today, what's at risk, agents, capacity and load. Load is shown as both a bar and a label such as "Over capacity" or "Tight", so it doesn't rely on colour alone.
   - The +/− buttons let the VP test their own plan. Every number, plus the count of tickets carrying over to tomorrow, updates as they click.
   - The VP can't assign more than the 37 agents on shift.
6. **Chart:** tickets waiting through the day for the selected queue, with the current assignment against your plan. It has a hover tooltip and a "View as table" fallback.
7. **Accounts closest to breach:** the five highest-ARR accounts with tickets due in under 6 hours, with the time left on each.

All data is invented. The queue loads, KPI trends, incident and account names are placeholders, so the numbers are internally consistent but don't come from a real system.

**Assumptions I made**
- **Target load:** 90% of capacity per queue.
- **Capacity:** agents × tickets resolved per agent per day, with a different rate for each queue.
- **Queue priority:** Escalations get agents first, then Technical: API, then SSO, Reports, Onboarding and Billing.

Say if your team's priorities or target load differ and I'll change them.

To wire it to real data, replace the `Q`, `KPI` and `ACCTS` arrays at the top of the script.
