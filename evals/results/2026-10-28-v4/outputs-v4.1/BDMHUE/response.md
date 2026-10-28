I built the Relay ticket queue as a single HTML file, but I haven't run it. This sandbox has no browser, and my attempts to run a syntax check were blocked pending approval. I didn't retry. Open it once and expect possible small bugs, especially in focus handling and the detail pane, which I haven't tested. It also hasn't been checked against a screenshot.

**File:** `/tmp/ux-eval-v41/BDMHUE/relay-ticket-queue.html`

Assumed: all-day agents working a queue, about 140 tickets here and more in production, and two roles (agent and view-only).
Direction: Data-dense utility, with a list and detail layout, light and dark themes, and one indigo accent. Status colours are used only for status, priority and SLA.

**How it works**
- **Layout:** a list on the left and the open ticket on the right, with the usual app shell: side nav, search (⌘K), notifications and account menu.
- **Views:** My open, Unassigned, Mentions, SLA at risk, All open and Solved, each with a count.
- **Default sort and the main button:** the queue sorts by SLA deadline, soonest first. The one primary button is "Take next ticket". It assigns the most urgent unassigned ticket to you and opens it.
- **SLA:** it shows as text plus an icon ("Breached 1h 12m ago", "Due in 38m", "Paused"), not colour alone.
- **Table:** sortable columns, 50 per page, and a compact or cozy row-density toggle in the account menu.
- **Filters:** search, status, priority and assignee. All of it, plus the view, sort, page and open ticket, is saved in the URL.
- **Selection and bulk actions:** checkboxes with "Select all N matching". Assign, set priority and solve all report how many tickets they changed or skipped.
- **Undo and live updates:** each change shows an Undo toast, and Z also undoes. New tickets that arrive wait behind a "Show" banner, so the list never reorders under the cursor.
- **Detail pane:**
  - Status, priority and assignee are editable in place.
  - The thread shows customer messages, agent replies and internal notes.
  - The reply box has macros and a "set status after sending" option.
  - Drafts are saved per ticket.
  - Sending an empty reply gives an inline error.
- **Keyboard:** J/K to move, Enter to open, X to select, A to assign to me, E to solve, R to reply, / to search, ? for help, Esc to close.
- **States:** a Review controls bar at the bottom switches the page between loading, empty, error and view-only. You can also use `?state=` and `?role=viewer` in the URL. Filtered-to-nothing and "My open" empty are separate designed states.

**Calls I made without you**
- Agents have no way to un-send a reply. Undo after a reply therefore only reverts the status change, and the toast says so.
- Assigning a ticket also sets it to Open.
- Pending tickets pause the SLA clock, so they don't appear in "SLA at risk".
- The notifications and account menus, the Customers, Reports and Articles nav items, and the "Connect email address" and "Add chat widget" buttons in the empty state are placeholders.
- The data is generated with a fixed seed. It includes a very long subject, a Japanese name, a missing company and urgent tickets that are already breached.
