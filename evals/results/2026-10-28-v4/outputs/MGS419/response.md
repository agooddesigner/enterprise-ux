I built the page as `/tmp/ux-eval-v4/MGS419/usage-billing.html`. It links `acme-ds.css` and uses its tokens and `ds-*` components. I haven't opened it in a browser, and my attempts to syntax-check the script were blocked, so treat it as unchecked. Please open it once and look.

It's written for an admin who opens it a few times a month. The top answers "what will I be billed on 1 Nov?" before anything else.

- **Hero:** the projected invoice (seats plus estimated transaction overage) is the largest element on the page. It has a line-item breakdown, the card charged, and a note that the final amount is set on 1 Nov.
- **Usage meters:**
  - Transactions, bank connections, API requests and seats each show used, included and percent as text, with a status badge, so colour is never the only signal.
  - Each meter says whether going over is billed, blocked or rate-limited.
  - Usage is scoped to the workspace, with a "usage as of" timestamp.
- **Chart:** cumulative transactions against the included amount, with a dashed projection to month end. A "view daily numbers as a table" disclosure serves as the text alternative.
- **Spend limit and alerts:**
  - Thresholds are at 75, 90 and 100%, with an optional dollar limit.
  - There is an explicit Save and inline validation.
  - Turning every alert off shows a warning about surprise charges.
  - Syncing is never paused automatically.
- **Plan and payment:** seats, payment method and billing contact, with proration stated. "Cancel subscription" is a visible link.
- **Invoices:** a table with status badges and PDF links, in absolute dates and UTC.
- **Shell:** side nav with "Usage & billing" marked as current, a workspace switcher, ⌘K search, notifications, account menu and breadcrumbs. It collapses on narrow screens.
- **States:** a "Preview state" dropdown at the bottom switches between ready, loading, error, new workspace (empty), payment failed and not a billing admin (read-only). The choice is stored in `?state=…`, so each state has a link.

The figures are made up: Northwind Trading, a $18/seat Business plan, 250,000 included transactions and $4 per 1,000 over. Daily usage is generated in the script and the totals are derived from it, so the numbers stay consistent. Swap in real API data.

I used the design system as is and didn't add dark mode, since it has no dark tokens. "Update payment method", "Change seats" and "Compare plans" are placeholders with no flows behind them. The cancel link, the invoice and PDF links and the nav links go to `#`.
