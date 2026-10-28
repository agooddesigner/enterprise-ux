I wrote the dashboard to `/tmp/ux-e9v3b/DK0VW0/support-staffing-dashboard.html`, but I haven't opened it or run its script. No browser is installed in this environment, and my attempt to syntax-check the JavaScript in Node needed approval that wasn't granted. Open it in a browser first and check the layout and that the buttons work.

It's one HTML file with inline CSS and JS and no external dependencies.

- **Title and freshness:** the page is headed "Where agents should be today", dated Wednesday 28 October, with "Data as of 08:10 PT" and a Refresh button.
- **Incident strip:** a banner for an active webhook-delivery incident, which is the story behind the numbers.
- **Hero card:** a dark card with one big number, how many agents are out of place against the recommended plan. It lists the moves (for example, "3 × Onboarding → Integrations") and has a lime "Apply recommended plan" button.
- **Four headline numbers:**
  - Tickets waiting for a first reply, with a mini chart of the last 8 mornings.
  - First-response SLA over the last 24 hours.
  - Queues projected to breach today, in the lime card.
  - Agents on shift (38 of 40).
- **Staffing plan table:** 7 queues with the waiting backlog, tickets still to arrive, current first-reply time against target, a +/− agent stepper, the number needed, and a load bar with a status label and outlook.
  - The 38 available agents can't be over-assigned.
  - Load, status and the projected breach time recalculate as you adjust the stepper.
  - "Publish to team leads" shows an Undo toast.
- **Arrivals by hour:** actual and forecast bars against a typical Wednesday, with the 10:00 peak highlighted and a table view underneath.
- **Accounts needing attention:** five escalated accounts sorted by ARR, each with its queue, issue and wait time.

Some details you may want to know:
- **Demo data:** the figures, account names and the incident are all made up. The capacity model assumes each queue has a fixed per-agent daily throughput.
- **Plan in the URL:** the staffing plan is saved in the address, for example `?plan=6,7,8,…`.
- **Preview states:** a "Preview state" dropdown switches between live, loading, error and empty views.
- **Fixed date and time:** the date and the 08:10 PT time are fixed in the file, not read from the clock.
- **Light only:** there is no dark mode.
