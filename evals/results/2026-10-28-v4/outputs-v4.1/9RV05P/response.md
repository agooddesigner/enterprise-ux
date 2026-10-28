I built the billing overview as one HTML file: `/tmp/claude-0/-tmp-ux-eval-v41-9RV05P/882ebbf6-be06-577b-985f-f27acad8a989/scratchpad/tally-billing.html`. I never rendered it or looked at a screenshot, so the layout and both themes are untested. The publish to claude.ai was held for approval, so there is no hosted link.

**Assumptions**
- I read "finance managers at our product" as customers who use Tally and look after their own account's billing. If you meant Tally's internal revenue billing, the tiles and hero need to change.
- You didn't give a job or data volume, so I used sample data for a fictional customer, Northwind Logistics. All figures are made up.

**Design**
- **Hero:** the hero number is the balance due, $27,114, on a dark card. It sits above a two-invoice list and a "Pay" button, with a red "1 overdue" chip and an overdue banner above the grid.
- **Bento:** four smaller tiles sit beside the hero in a 12-column grid. They cover next invoice estimate, spend this month (with a sparkline), seats used (412 of 450), and contract renewal. Everything below the grid is plain white cards with hairline borders and one indigo accent.
- **Below the tiles:**
  - A 12-month invoiced bar chart with hover and keyboard tooltips.
  - A breakdown of the next invoice.
  - An invoice table with working status filters.
  - Payment method and billing contact cards.
- **Themes:** it follows the system light or dark setting, and a header toggle overrides it and is remembered per browser.
- **Fonts:** Geist and Geist Mono from Google Fonts. Without a connection it falls back to system fonts.
- **Phones:** tiles stack to one column on phone widths, and the table scrolls sideways inside its own card.

The Pay, View, Export and tab links don't do anything yet, and the table filter isn't saved in the URL.
