I built the billing overview as one HTML file. I haven't opened it in a browser or checked it at phone width, so the layout and both themes are untested.

File: `/tmp/ux-eval-v4/F22XHO/tally-billing-overview.html`

- **Bento KPIs:** The hero is cash collected this month, $412,860, which is +3.7% on September. It spans two columns and two rows and has a 12-month sparkline. Four smaller tiles sit beside it: outstanding, overdue (the only one with a red-tinted border), failed payments, and next payout.
- **Below the KPIs:**
  - An invoiced-vs-collected line chart for the last 12 months, with a hover crosshair and tooltip.
  - A receivables aging breakdown: not yet due, 1–30 days late, and 31+ days late.
  - An invoice table with status pills and All / Overdue / Failed / Paid filters.
- **Light and dark:** Colors follow the system setting, and a Theme button overrides it and remembers your choice.
- **Style:** Flat, hairline-bordered cards, system fonts, one blue accent. Green, amber and red appear only for payment status, and the pills carry a text label as well as a color.
- **Phone width:** The bento grid collapses to two columns and then one, and the table scrolls sideways inside its own container.

All numbers are sample data I made up. The KPIs, aging buckets and chart points add up to each other, but none of it is real Tally data. The chart series and invoice rows are plain arrays in the script at the bottom, so you can replace them with your own.
