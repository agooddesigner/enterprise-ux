I built the billing overview as a single HTML file, but I haven't opened it in a browser. This machine has no browser, and my syntax check on the script needed approval that wasn't granted. Open it once to confirm the layout and the script run cleanly.

**File:** `/tmp/ux-eval-v4/7AY9Z0/tally-billing.html`

**Design direction:** a cool paper-grey canvas with white 16px-radius cards, hairline borders and almost no shadow, plus one indigo accent. It uses Geist, loaded from Google Fonts with a system-font fallback.

**Bento KPIs:**
- **Hero:** one dark card shows the projected October invoice, **$43,525.16**, in a 72px number with the cents smaller. It carries a "▲ 11.8% vs September" pill and a segmented bar breaking down the charges. Below that is a plain-text line-item list and the estimated tax. It is the only dark card.
- **Tiles:** four KPI tiles sit beside the hero in a 2×2 block:
  - outstanding balance
  - seats in use (212 of 250)
  - events this period (37.2M against 36M included)
  - days to contract renewal
- **Colour use:** status colours appear only as small labelled pills, so colour is never the only signal.

**Below the tiles:**
- A six-month invoice trend chart, with the projected month hatched.
- A billing-details card: card on file with its expiry warning, bill-to address, PO number, tax ID and plan.
- An invoices table with filter chips (All / Open / Paid) and a CSV export of the visible rows.
- One amber strip above the grid about the overage, linking to "Set a spend cap".

**Light and dark:** both themes work. With no choice made, the page follows the system setting; the moon button overrides it. In dark mode the hero turns deep indigo, so it stays distinct from the cards around it.

**States:** a "Preview state" dropdown in the header switches between ready, loading, error and new account. The loading and error states apply per card, and retry works. The chosen state and the invoice filter are written to the URL. The chart has a hidden table version for screen readers.

**Placeholder content:** the customer ("Harbor & Pine Logistics"), the invoice numbers, the rates and the contract dates are invented. The figures are internally consistent: the line items sum to $40,208.00, plus 8.25% estimated tax. Swap in real data before showing it to anyone.

**Not wired up:** only the invoice filter chips and CSV export work. Edit, Change plan, the PDF buttons, Set a spend cap and View all invoices are placeholders.

I didn't publish it as an Artifact since you asked for a file. I can publish it if you want a shareable link.
