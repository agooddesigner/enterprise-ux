I couldn't run any checks on the page, so I haven't seen it rendered. There's no browser in this environment, and the shell blocked my attempt to syntax-check the script. Please open it in a browser before relying on it.

The page is built: `/tmp/ux-eval-v4/KYZWII/tally-billing-overview.html`. It's a single file with no dependencies.

- **Bento KPIs:** one hero card, "Collected this month, $482,310", takes the left half at 68px. It shows an 8.2% increase against September and a bar chart of daily collections. Four smaller cards sit beside it: Outstanding, Overdue, Failed payments and Avg. days to pay. The first three link through to the invoice table filtered to that status.
- **Stripe-like restraint:** white cards on a pale grey background, thin borders, one indigo accent, and status colours only on status pills. Each pill carries a dot and a word, so colour is never the only signal.
- **Below the KPIs:**
  - **Invoice table:** status tabs, search, sortable columns and row selection with a bulk "Send reminder" that has an Undo toast.
  - **Needs attention:** a side list of failed payments and upcoming renewals.
  - **Payout banner:** a notice about a delayed payout.
- **Light and dark:** it follows your system setting, and the toggle in the top bar overrides it and remembers the choice.
- **Every state:** use the "Preview state" links at the bottom of the page to see loading, empty and error.
- **Shareable links:** the status filter, search, sort and state are kept in the URL.
- **Accessibility:** a skip link and visible focus. You can read the chart with the arrow keys, and "View as table" gives the same data as text.

The page is a prototype with made-up Northwind Trading data, not a connected product:
- Only the status tabs, search, sort, selection and Undo actually work. Retry, Remind, Export, ⌘K search and "Create invoice" just show a message or do nothing.
- The KPI totals are hard-coded for the whole company, and the table shows only the 14 latest invoices. That's why the tab counts won't match the KPI counts.

I chose USD, an Oct 1–28, 2026 window and a "Billing" section in the side nav; change any of those if they're wrong.
