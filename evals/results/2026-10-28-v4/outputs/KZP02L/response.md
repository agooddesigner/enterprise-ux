I built the billing overview as one HTML file, but I couldn't open it in a browser here. It hasn't been rendered or run, so I haven't seen the layout and I can't confirm the script is free of errors. Please open it and check the chart, the table and the dark mode.

I couldn't screenshot it because no browser was available, and the shell blocked the Node syntax check I tried. The first thing to look at is the top bento, then the "Needs attention" table. If something is off, tell me what you see and I'll fix it.

**What's on the page**
- **Hero number:** monthly recurring revenue ($482,310) sits in a large dark card spanning the left half of the top bento. It has a +4.2% delta, ARR, active subscriptions and net revenue retention, and a 6M/12M line chart. The chart has hover and arrow-key tooltips and a "View as table" toggle.
- **Four smaller tiles:** collected this month, outstanding, overdue, and failed payments. Each has a delta (favorable or unfavorable) and links to the underlying records.
- **Work queue:** a "Needs attention" table with All / Overdue / Failed tabs. Checkboxes lead to a bulk bar with "Select all N matching" and an Undo toast.
- **Right column:** a receivables-by-age bar and the next payout.
- **App shell:** side navigation with Billing marked as current, a workspace switcher, breadcrumbs, ⌘K search, notifications and an account menu.
- **Restraint:** one accent color, status colors used only for status, and tabular numbers throughout.
- **Light and dark:** it follows your system setting, and the moon button overrides it and remembers the choice.

**Things I assumed**
- The viewer is a billing admin looking at October 2026 in USD, with USD figures and a fixed "Updated 08:10 UTC" line. All the figures are made-up sample data, so replace them with real data.
- Most buttons and links are placeholders. Remind, Retry, Export CSV and bulk actions only show a toast.
- The hero card is dark navy in both themes, and the other cards stay white or dark navy to match the theme.

**Other states and URL**
- **States:** add `?state=loading`, `?state=error` or `?state=empty` to the URL to see those states.
- **Shareable view:** the selected tab and chart range are written to the URL, for example `?tab=failed&range=6`.

The file is at `/tmp/ux-eval-v4/KZP02L/tally-billing-overview.html`.
