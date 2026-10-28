I've built the dashboard as one HTML file with inline CSS and JS. I couldn't render it or run its JavaScript here: the shell needs approval for node and has no headless browser. I read the code through, but I haven't seen the layout. Open it and check for overlaps before you rely on it.

**File:** `/tmp/ux-eval-v4/66A0B0/support-staffing-dashboard.html`

I wrote it for a VP who opens it each morning to decide where the 40 agents go. All numbers are made-up but realistic.

- **Top card:** it gives one recommendation, for example "move 5 agents", with the specific moves between queues. It also shows the weakest queue's coverage before and after.
- **Headline numbers:** SLA breached now, tickets due in 2 hours, forecast new tickets against a typical Wednesday, and agents available (38 of 40).
- **Incident strips:** the two things driving today's volume, a webhook outage and the month-end invoice run.
- **Staffing planner:** the main tool. There are six queues, each with a coverage bar, a status label, and the current, suggested and planned agent counts. The planned counts have +/− buttons. Coverage means agent capacity divided by today's workload, which is forecast new tickets plus backlog due today. The planner also shows the moves needed to reach your plan, and its state is saved in the URL.
- **Arrivals chart:** hourly forecast against last Wednesday, with the peak hour marked and a "view as table" option.
- **Big accounts at risk:** customers over $250K ARR with a ticket breached or due soon, filterable by queue.

The suggested split is a rule I chose: each agent goes to whichever queue has the lowest coverage. Even with that split, 38 agents cover only about 91% of today's workload. The planner says so and lists levers (overtime, macros, Tier 2 help). The numbers per queue, agent output rates and the "9 more breaches than yesterday" note are all invented.

I added `?state=loading` and `?state=error` to the URL so you can check those views. Copy summary puts a plain-text plan on the clipboard. There's no real send-to-team action. The nav links and ticket links point nowhere, because there's no backend.

I used a soft, light layout with one dark card for the main answer, and I didn't ask about style or data first. Tell me if you'd prefer a denser or darker look, or if your real queues and rates differ from my guesses.
