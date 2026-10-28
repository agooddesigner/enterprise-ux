I couldn't run the script syntax check because the command needed approval, so I haven't checked the page or loaded it in a browser.

The page is at `/tmp/ux-eval-v41/ANTON1/tally-billing-overview.html`. It's one self-contained file and loads only the Inter and JetBrains Mono fonts from Google Fonts.

You didn't answer intake questions, so I assumed finance managers check this page daily, to see what's owed, what's late, and what the next payout will be.

- **Look:** Stripe-style restraint, with a quiet slate and white palette, an indigo accent, thin borders and almost no shadows. Green, amber and red appear only on status pills.
- **Hero number:** MRR is $482,310 at 64px, spanning half the top bento with a sparkline underneath.
- **Other KPI tiles:** Collected, Outstanding, Overdue, Collection rate and Next payout sit in a 3-column grid beside the hero. Most tiles link through to the underlying records.
- **Below the KPIs:** a bar chart of collected revenue over six months (zero baseline, one highlighted bar, hover or keyboard focus shows the exact figure), a "Needs attention" list with Send reminder and Retry now actions, and a status-filterable invoice table.
- **Navigation and filters:** the page has a side nav, search (⌘K), notifications and an account menu. A This month / Last month / Quarter switch changes the figures.
- **Light and dark:** it follows your system theme by default, and the moon button in the top bar overrides it either way.
- **States:** add `#loading`, `#empty` or `#error` to the URL to see those versions. Use `#ready` to go back.
- **Placeholder data:** all figures and customer names are invented examples.
- **Not built:** the invoice filters and period don't write to the URL, and the table has no sorting or pagination.
