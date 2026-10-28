I built the page at `/tmp/ux-eval-v4/0CLYEL/usage-billing.html`. It links `acme-ds.css` and takes its colors, type, spacing and radii from the design-system tokens. I haven't opened it in a browser, so the layout is unchecked.

Admins only open it a few times a month. So the top of the page answers "is anything about to cost me money, and what will I be charged?"

- **Warning banner:** it appears only when a limit is close. The sample shows invoice processing at 87%, with the overage rate and a "Change plan" button.
- **Summary row:** estimated bill for this period, next invoice date and card, and plan with renewal date.
- **Usage meters:** invoices processed, seats, bank connections and storage. Each shows the number, the remaining amount and a status badge, so state never relies on color alone.
- **Usage by member:** a table showing who is driving usage, with a find box.
- **Payment method and billing contact:** each with an edit button.
- **Invoice history:** status badges and PDF download links.

The page also has a "Download usage report (CSV)" button. On narrow screens the grids collapse to one column and the tables scroll sideways.

- **Sample data:** all figures are made up. I guessed at the metrics (invoices, seats, bank connections, storage), the Business plan and the pricing, so swap in your real ones.
- **Not wired up:** the buttons, links and find box do nothing yet.
- **Added CSS:** `acme-ds.css` has no progress bar, alert or layout styles. I added a small `<style>` block for those, built only from the design-system tokens. If you want them in the design system itself, move that block there.
