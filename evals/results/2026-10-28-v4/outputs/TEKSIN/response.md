I built the queue screen as one HTML file, but I haven't run it. I couldn't get approval to run commands while you were away, so there was no syntax check and no browser test. Open it in a browser and click through it once before trusting it.

The file is `/tmp/ux-eval-v4/TEKSIN/relay-queue.html`.

**What's on screen**
- **Layout:** views sit on the left, the ticket list in the middle, and the open ticket on the right. Below about 1100px the ticket opens full-screen with a Back button.
- **Views:** Your open, Unassigned, SLA at risk, All open, and Solved. Each shows a live count, and the SLA at risk count turns red when it's above zero. The default sort is SLA due soonest.
- **Search and filters:** search covers subject, requester, company and ticket number. You can also filter by priority and channel, and sort by SLA, longest waiting, newest or priority.
- **Ticket rows:** each shows unread state, priority, a Pending or Solved tag, the requester, how long ago it was last active, who it's assigned to, and the SLA text. SLA status is written out ("Breached 18m ago", "Due in 25m"), not shown by color alone. Countdowns update every 30 seconds without redrawing the list, so your scroll position and any half-typed reply survive.
- **Ticket detail:** the conversation, assignee, status and priority dropdowns, and a reply box. There are two send buttons: "Send · set Pending" and "Send & resolve". Drafts are kept per ticket.

**Choices I made without you**
- **Keyboard first:** `j` and `k` move through tickets and the detail pane follows. `x` selects, `a` assigns to you, `e` resolves, `r` or Enter jumps to the reply box, `u` marks unread, `/` searches, `Ctrl+Enter` sends, and `?` lists them all.
- **Undo:** every change (assign, resolve, status, priority, reply) shows a toast with Undo, and `z` also undoes it. I did this instead of confirmation dialogs because dialogs slow down a full day of triage.
- **After resolving:** the cursor moves to the next ticket instead of jumping back to the top.
- **Pending tickets:** they show "Waiting on customer" instead of an SLA clock.
- **Bulk actions:** selecting several tickets shows "Assign to me" and "Resolve" in a bar above the list.
- **Theme:** light and dark follow the system setting, with a manual toggle. The last view and sort are remembered in the browser.
- **Data:** it's all made-up sample data (27 tickets, relative to when you load the page), and nothing is saved to a backend. Your changes reset on refresh. Replace the `seeds` array with your real API when you wire it up.

**Not built:** macros or canned replies, internal notes, merge, and a "my team's tickets" view.
