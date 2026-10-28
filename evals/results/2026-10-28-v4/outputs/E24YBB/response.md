I built the billing overview as one HTML file, but I haven't opened it in a browser. This sandbox has no browser and I couldn't run a script check, so layout and JavaScript are untested. Open it once and check the bento row heights, the chart, and the dark-mode contrast.

**Layout**
- **Hero:** the "Next invoice" estimate ($52,184.60) is a 68px number on the one dark card, top-left. Under it is a seats / usage / add-ons breakdown bar with values listed beside it, and a one-line explanation of why it's up from October.
- **KPI tiles:** four tiles sit beside the hero. They show outstanding balance with an overdue pill, 12-month invoiced total with a sparkline, seats in use, and usage against the included amount.
- **Below the bento:** a monthly invoiced bar chart (zero-based, November hatched as an estimate, hover and focus tooltips, Chart/Table toggle). Next to it is a plan and payment card, then an invoice table.
- **Restraint:** one indigo accent, white cards with hairline borders, no gradients, and the type scale carries the hierarchy.

**Light and dark:** it follows the system setting and has a toggle in the top bar that remembers your choice. I picked the dark-mode colours by eye and haven't measured their contrast.

**Finance-manager details**
- A persistent overdue alert shows the reason (expired card) and the date the workspace would go read-only if unpaid.
- Invoice statuses are text pills, not colour alone. Dates are absolute and amounts are right-aligned.
- The filter chips (All, Open, Overdue, Paid) and the date and amount sorting are saved in the URL. So are the page state and the chart/table view.
- Each card has loading, error with Retry, and new-account states. A "Preview state" dropdown in the header switches between them.

**Prototype limits**
- All figures are invented (Northwind Finance, Business plan at $75 per seat). I made the numbers reconcile, for example the estimate's parts sum to the total and the open and overdue invoices sum to the balance.
- Buttons like Pay and Update payment method show a toast saying what would open, because the underlying flows don't exist yet.
- The "6 days overdue" text is hard-coded for the 28 Oct 2026 date.

The file is at `/tmp/ux-eval-v4/E24YBB/tally-billing-overview.html`.

If you tell me Tally's real plan structure, such as seats, usage or flat pricing, I'll swap the sample figures for it.
