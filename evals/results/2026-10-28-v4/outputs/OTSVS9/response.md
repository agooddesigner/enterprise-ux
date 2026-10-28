I built the page, but I haven't seen it rendered. This environment has no browser, and my script syntax check was blocked. Open it once and check the layout before you rely on it.

It's at `/tmp/ux-eval-v4/OTSVS9/usage-billing.html` and links `acme-ds.css`. The design system's own radii, type scale and components are used throughout. All figures are made-up sample data for Northwind Logistics.

**Who it's for:** a workspace admin who opens it a few times a month. The page answers three questions, in this order:
1. What will I be charged?
2. Am I near any limit?
3. Where are my invoices?

**Layout:**
- **Charge card:** a dark card at top-left shows the projected charge of $1,178.20, with the line items. It is labelled as an estimate, with the bill date and the card it will go to.
- **Limits:** five meters (invoices, seats, bank connections, API requests, storage). Each shows its numbers and a text badge, so colour is never the only signal. Invoices are marked "Projected over", with a tick on the bar for the projected month-end volume.
- **Warning strip:** it says the invoice allowance will be passed and what that adds in cost, and it links to plan options.
- **Daily chart:** invoices per day, starting from zero, with weekends and today's partial day marked. A "View as table" toggle gives the same data as text.
- **Plan and payment:** the plan, next invoice date, card, and a single primary action, "Change plan".
- **Invoices:** the last six, with absolute dates, text status badges and PDF downloads.
- **Timing:** the page shows "Usage as of 28 Oct 2026, 08:10 PT" rather than when it loaded.

**States and URL:** a small "Prototype controls" row at the bottom switches state, and the choice is written to the URL (`?state=` and `?role=`).
- **State:** ready, loading, error in two cards only, a new workspace with no usage, and payment failed.
- **Role:** an admin without billing access sees the billing buttons disabled, with a note naming the billing owner to ask. They can still view usage and download invoices.

**Assumptions to check:**
- **Plan and pricing:** the Business plan at $299 a month, $18 per seat, and $0.04 per invoice over 10,000.
- **Data scope:** the page shows only the current period, with past periods reachable through the invoice list.
- **Dead links:** the "View all invoices", "Change plan" and "Update payment method" links are placeholders.
- **Cancel:** there is no cancel-subscription entry point yet. Say if you want one added.
- **Refresh:** the button reloads the sample data, so the "as of" time stays fixed.
