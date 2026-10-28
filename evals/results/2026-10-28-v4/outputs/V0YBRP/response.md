I couldn't run a syntax check on the script because the command needed approval and you're offline. I also haven't opened the page in a browser, so none of it has been tested.

The screen is at `/tmp/ux-eval-v4/V0YBRP/relay-queue.html`. It's a single file with inline CSS and JS, no dependencies, and it runs on made-up sample tickets.

**What's on the screen**
- **Queues sidebar:** My tickets, Unassigned, SLA at risk, All open, Waiting on customer and Resolved, each with a live count. SLA at risk turns red when it isn't empty. The last queue and sort you used are remembered.
- **Ticket list:** each row shows priority, ID, subject, requester and company, a one-line preview, status, assignee, an SLA countdown and time since last update. Unread tickets are bold.
- **Detail pane:** opens beside the list and lets you change status, priority and assignee. It also has Assign to me and Resolve buttons.
- **Search, sort and filter:** search covers subject, requester and ID. You can filter by priority and sort by SLA, priority, newest or oldest.
- **Bulk actions:** select several tickets to assign them, resolve them or set a priority in one go.
- **Undo:** every change shows a 7-second Undo toast.
- **Display:** light and dark themes follow your system setting. Below 1180px the detail pane becomes a slide-over, and below 760px the sidebar becomes a top strip and the list shows fewer columns.

**Calls I made without you**
- **Keyboard first:** agents live in this screen all day, so everything has a shortcut.
  - `j`/`k` move between tickets, `x` selects and `a` assigns to me.
  - `e` resolves, `/` searches, `Esc` clears and `?` lists the shortcuts.
  - `g` then `1`–`6` jumps to a queue.
- **Default sort is SLA due soonest.** Tickets waiting on the customer sink to the bottom, because their SLA clock is paused.
- **The list never re-sorts on its own.** SLA timers update in place every 30 seconds so rows don't move under the agent's cursor. A new sort or filter, or an action like resolving, does re-order the list.
- **SLA state is never shown by colour alone.** Each one has a text cue: "⚠ Overdue 22m", "⏱ 38m", "Paused".
- **The first ticket in the list is the active one when the page loads.**
- **Sample data:** the data is generated, not real. The signed-in agent is "Priya Nair", and there are three other agents to assign to.

**Not built:** reply composer, full ticket page, real data or API, and keyboard shortcuts for changing priority.
