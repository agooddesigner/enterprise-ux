I built the page at `/tmp/ux-eval-v4/HBRBXP/usage-billing.html`. It links `acme-ds.css` and takes its colours, radii, spacing and type sizes from that file's tokens. I couldn't run it. Both the script syntax check and a headless render needed approval that wasn't granted. I also never looked at a rendered screenshot, so layout and visual polish are unchecked. Please open it once in a browser.

**Who it's for:** a workspace admin who opens it a few times a month. They want to know what this cycle's invoice will be, whether anything needs action, and where to find an invoice. It leads with the answer and explains each line in plain words.

**Layout, top to bottom**
- **Warning strip.** It says you're on pace to pass the 10,000-invoice allowance around 5 Nov, with the extra cost and a "Compare plans" link.
- **Projected invoice (highlighted card).** The big number is $1,352.68. Below it, an itemised table shows seats, invoice overage, bank connection overage and storage. The spend-alert threshold sits underneath.
- **Plan & payment.**
  - Plan, renewal date, card and billing contact.
  - Update payment method and Change plan buttons.
  - A permanently visible "Cancel subscription" link.
- **Invoices processed.**
  - Used so far, projected and included allowance on one meter.
  - A per-day bar chart with a zero baseline.
  - A "view as table" fallback for screen readers.
- **Seats, bank connections, document storage.** Each has numbers, a status badge, and a link to manage it.
- **Invoice history.** Absolute dates, a text status badge, a download link per row, and a "View all 18" link.

**States, using the "Preview state" menu in the footer**
- Loading, with skeletons in each card.
- Usage failed to load, with a Retry button on each affected card. Plan and invoice history stay live.
- New workspace with no usage yet.
- An admin without billing access, who sees a read-only view naming who manages billing.
- Billing cycle: the current one or the previous, closed one.
- State and cycle are saved in the URL (`?state=…&period=…`).

**Things you should know**
- **Placeholder data.** The workspace "Harbor & Finch LLP", the plan prices ($24/seat, $0.04 per extra invoice, $15 per extra bank connection), the allowances, invoice numbers and the billing contact are all invented. Swap in real values.
- **Dead links.** Links like "Compare plans", "Edit spend alert" and "Download PDF" point to `#` placeholders. The Update payment method and Change plan buttons do nothing yet.
- **Style choices.** I kept the DS's 4–6px radii instead of rounder shapes. The 44px headline number is the one size outside the DS type scale.
- **Billing compliance.** The cancel link is always visible, and billing is the part to check with counsel.
