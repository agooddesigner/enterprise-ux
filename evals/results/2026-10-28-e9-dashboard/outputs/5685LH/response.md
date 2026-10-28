I couldn't run the script check or open the page, because the shell kept asking for approval on every command I tried. So the dashboard is written but untested. I haven't seen it render, and I haven't confirmed the script has no syntax errors.

The file is at `/tmp/ux-e9/5685LH/support-staffing-dashboard.html`. It's a single HTML file with inline CSS and JS and no external dependencies. All the data is made up: one snapshot at 08:05 on Wed 28 Oct, with 36 of 40 agents available.

**What the VP sees**
- **Summary line:** it says how many agents today needs against how many are available, and which queues will end the day with unfinished tickets (e.g. "needs 37, 36 available; Integrations & API will carry over 41").
- **Five key figures:** agents available, open backlog, tickets within 30 minutes of breach, forecast inbound, and projected carry-over. Each is compared with a typical Wednesday.
- **Queue table:** six queues, sorted worst first. Each row shows a status (icon plus label), backlog, oldest wait against target, agents staffed, agents needed, the gap, and projected carry-over at 18:00.
- **Staffing controls:** +/− buttons on each row let the VP try a different split. The total stays at 36, and each queue has a minimum, so a queue can't be emptied.
- **Suggested moves:** moves such as "Move 3 from Tier 1 General to Integrations & API", with how many tickets each clears. They apply one at a time or all at once, and they recompute after every change.
- **Chart:** click a queue to see its work arrived against what its staffed agents can clear, hour by hour from 08:00 to 18:00. It has hover and arrow-key readout and a "view as table" option.
- **Side panels:** the tickets closest to breaching (named customer, ARR, minutes left) and who's out today.
- **Plan handling:** Undo, Reset, and "Copy plan for team leads", which copies a plain-text summary. The plan is also stored in the URL, so a link shares it.

**Assumptions to check**
- "Needed" uses a fixed tickets-per-agent rate for each queue.
- Capacity is spread evenly across the 10-hour day.
- Inbound follows a fixed hourly shape.

Swap in real rates and forecasts when you connect it to data.

Next, open the file in a browser and check three things: the layout renders at your window width, the +/− buttons and "Apply" update the numbers, and dark mode looks right. If you approve a check from the sandbox, I can do it and fix whatever turns up.
