I couldn't run a syntax check or a render. The sandbox asked for approval on the check command, and I haven't opened the page in a browser.

I built the Ledgerly usage and billing page as `/tmp/ux-eval-v4/7XL6FC/usage-billing.html`. It links `acme-ds.css` and uses only its `ds-*` components and tokens. It has a small amount of page-level layout CSS of its own. Nothing in it has been tested, and I haven't looked at it in a browser at any width.

**What it shows**
- **Main answer first:** the top card is the projected invoice for October, $1,039.36, with a line-by-line breakdown. The "Estimate" label and the "as of 28 Oct 2026, 14:00 UTC" line tell admins how current it is.
- **Overage warning:** a banner says the workspace is over its 5,000 included documents and what that costs so far and by month end.
- **Plan card:** plan, seats, renewal date, payment method and billing owner.
- **Usage section:** four usage meters (documents, bank connections, API calls, storage). Next to them is a day-by-day chart of documents processed, with the projection and the included amount marked, plus a "View as table" option.
- **Spend alert:** an email alert when projected charges pass a set amount. It checks the amount on Save and says plainly that nothing gets paused.
- **Invoices:** the five most recent, with a button to show the older ones and a PDF link on each.
- **Page frame:** side navigation with "Usage & billing" marked as the current page, a workspace switcher, search, alerts, an account menu, and breadcrumbs.
- **Period switcher:** a selector for October, September and August. The choice goes into the URL as `?period=`, so a view can be linked.
- **Other states:** I added `?state=loading`, `empty` (a trial workspace with no usage yet), `error`, and `readonly`. `readonly` is an admin who isn't the billing owner. They see the figures but not the change buttons, with a note saying who can change billing. Links to these states sit at the bottom of the page.

**Assumptions to check:** I made up all the figures, the plan and its limits, the pricing ($24 per seat, $0.08 per extra document), and the names. I assumed only the billing owner can change billing. Replace these with real data and your real rules.

Tell me which of those assumptions are wrong and I'll adjust the page.
