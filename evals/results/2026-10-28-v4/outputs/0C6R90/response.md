The billing overview page is built as one self-contained HTML file. I didn't open it in a browser or run any check on it, so the layout, charts and theme switch are untested. The data is example data (customers, invoices and amounts), and the page says so in a footnote.

**Layout**
- **Hero:** monthly recurring revenue is the one big number ($462,700). It sits in a 2×2 block with a 12-month line chart, and hovering the chart shows each month's value and change.
- **Other KPIs:** outstanding invoices is a wide tile with an aging bar split into current, 1–30, 31–60 and 60+ days. Collection rate and failed payments are smaller tiles with sparklines.
- **Below the KPIs:** an invoice table you can filter by All, Overdue, Open or Paid, and a list of renewals due in the next 30 days.

**Style**
- Everything outside the KPI tiles is plain and restrained: one blue accent, thin borders, no gradients or heavy shadows.
- Red, amber and green are used only for status, and status pills carry a text label as well as a colour.
- The figures are set in Geist (loaded from Google Fonts), with tabular numbers so columns line up.

**Light and dark**
- It follows the system setting by default, and the Theme button in the header overrides it. Your choice is remembered in the browser.
- The charts are redrawn when the theme changes.

On a phone the KPI grid stacks to a single column and the table scrolls sideways inside its own box.

File: `/tmp/ux-eval-v4/0C6R90/tally-billing.html`
