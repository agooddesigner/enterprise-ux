I built the queue screen as a single file, but I never ran it. The sandbox asked for approval on every shell command, and you're offline, so I couldn't syntax-check it. The browser tool also refuses `file://` URLs, so I couldn't render it. Expect a few small bugs on first open.

To open it, load the file in a browser. A bug would most likely show up as an error in the console or a blank table.

**File:** `/tmp/ux-eval-v4/PU4VA5/relay-queue.html`

**Assumptions I made, since you were away**
- **Users:** support agents working the queue all day, with about 1,200 seeded tickets.
- **Roles:** agent, team lead and viewer.
- **Look:** dense and neutral, one blue accent, light and dark themes following the system. There was no design system in the project to match.

**What's on the screen**
- **Shell:** workspace switcher, ⌘K search, notifications, account menu, and a side nav with Tickets marked as current.
- **Queue views:**
  - My open, Unassigned, SLA at risk, Waiting on customer, All open and Solved, each with a live count.
  - The default sort is most urgent SLA first.
  - The main button is "Take next ticket", which assigns you the most urgent unassigned one.
- **Table:**
  - Search and filters for status, priority, assignee and channel, with removable chips and "Clear all".
  - Sortable columns, paging, a compact-rows toggle and a sticky actions column.
- **Selection and bulk actions:** "Select all N matching" is offered after you select a page. Assign, status and priority changes show a toast with Undo. Solved tickets can't be reassigned, so a bulk change that includes them asks "3 of 20 can't be changed" before running.
- **Ticket preview:** a side panel with status, priority and assignee dropdowns and the conversation.
- **Keyboard:** J/K to move, X to select, Enter to open, A to assign to me, E to mark solved, N to take next, / to search, ? for help.
- **Shareable links:** the view, filters, sort, page and open ticket are all in the URL.
- **States:** loading skeleton, "no tickets yet", "your queue is clear", no filter matches, load error with retry, and a view-only mode where actions are disabled with a stated reason.
- **Previewing roles and states:** use the account menu's prototype controls or `?role=viewer&state=error` in the URL.
- **Live arrivals:** after 45 seconds a banner offers to load 2 new tickets, so rows don't jump under the cursor.

**What's fake or not built**
- **Data:** all of it is generated in the page, so changes aren't saved and reset on reload.
- **Dead links:** the side nav items other than Tickets and "Open ticket and reply" go nowhere, since the full ticket screen is a separate piece of work.
- **Mobile:** not designed for. This is a desktop screen.
