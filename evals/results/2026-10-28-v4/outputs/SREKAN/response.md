I designed the dashboard as a single HTML file and sent it to you. I couldn't publish it to claude.ai because those requests were declined. I also haven't opened it in a browser, so the layout and charts are unchecked. The file is `/tmp/claude-0/-tmp-ux-eval-v4-SREKAN/882ebbf6-be06-577b-985f-f27acad8a989/scratchpad/cs-dashboard.html`. If you want it as a hosted artifact, say so and I'll try again.

I assumed the main user is a customer success manager who opens it every morning to decide which accounts to work. All the numbers, accounts and names are made-up examples, labelled "Example data" on the page.

**What's on it**
- **Headline:** the largest card shows how much annual revenue is at risk in renewals over the next 90 days. The page title says how many renewals need attention.
- **Retention numbers:** four tiles for net revenue retention, gross retention, average health score and open escalations. Each shows its change and a small trend line.
- **Accounts table:** it lists accounts needing attention, with health, annual revenue, renewal date and the reason. You can sort it and filter by All, At risk, Watch or Renewing in 30 days. The filter is kept in the page address, so a filtered view can be shared as a link. Clicking a row opens a side panel with details and a suggested next step.
- **Due today:** a task list you can tick off, with an Undo option. It's the one bright lime card.
- **Charts:** a bar showing the book split by health, renewing revenue by month, and a 12-week health trend.
- **Around it:** side navigation, a search box (⌘K), notifications, and a "last updated" line.
- **Other states:** Loading and Error previews, with Retry buttons, sit under the page, plus a dark mode toggle. There's no empty-table state except when a filter matches nothing.
- **Phones:** it should rearrange to a single column on narrow screens, but I haven't tested that.

I haven't hooked up real data. To go further, I need to know where your account and health data lives and how you calculate the health score. Then I can connect it and adjust the thresholds and the columns.
