I built the Ledgerly usage and billing page at `/tmp/ux-eval-v4/9WLYAN/usage-billing.html`. It links `acme-ds.css` and takes its colors, type, spacing and radii from that file's tokens, apart from a few small layout rules in the page itself. I haven't opened it in a browser, so none of the layout or chart rendering has been checked.

All figures are sample data, so you'll need to swap in real numbers.

**What's on the page**
- **Status banner:** a one-line "You're on track" that gives the projected month-end usage against the plan. This is the thing an admin visiting a few times a month most wants to know.
- **Summary cards:** estimated next invoice with its date and card, seats used out of the limit, and transactions used out of the limit.
- **Usage table:** seats, transactions, connected bank accounts and API requests, each with used, included, a progress bar and a status badge. Bank accounts show "Near limit" in the warning color. A note underneath explains what overage costs.
- **Daily chart:** transactions synced per day, with weekends in a lighter shade. It's drawn by a short inline script from a sample data array.
- **Estimated charges:** a line-item breakdown that adds up to the invoice estimate ($1,055.00).
- **Invoices:** recent invoices with status and PDF links.
- **Payment and billing contact:** card, billing email and tax ID, with Update and Edit buttons.

**Things to know**
- **Missing styles:** the design system has no meter or dark-mode styles, so I wrote a small meter and the chart styling in the page, using the same tokens.
- **Status wording:** status is always shown as text in the badge, not only as a color.
- **Placeholders:** buttons and PDF links don't go anywhere yet. The company name, plan, prices and overage rates are made up.
