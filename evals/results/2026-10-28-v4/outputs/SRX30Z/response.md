I've designed the dashboard and saved it as a file. I couldn't publish it as a link because both publish attempts were declined. I haven't opened or rendered the page, so I haven't checked how it looks or whether it has layout or console errors.

The file is `/tmp/claude-0/-tmp-ux-eval-v4-SRX30Z/882ebbf6-be06-577b-985f-f27acad8a989/scratchpad/cs-dashboard.html`. Say the word and I'll try the publish again, or you can open the file directly.

I didn't ask you any questions first. I assumed the users are CSMs and CS managers who check it daily, and that the main job is spotting accounts at risk before renewal. All the data is made-up example data, and a banner on the page says so.

**What's on it**
- **Layout:** a left navigation bar (Overview, Accounts, Renewals, Support tickets, Playbooks, Reports), a search box (⌘K), notifications and an account menu.
- **Headline numbers:**
  - ARR at risk is the dark hero card, with the top risk reasons below it.
  - Renewals in the next 90 days is the lime card, with a month-by-month bar chart showing the at-risk portion.
  - Net revenue retention and open P1 tickets are smaller cards.
- **Health bar:** a single bar splitting accounts into at risk, watch and healthy, with counts and ARR for each. The status labels are words as well as colors.
- **Accounts needing attention:** a sortable table showing health score, ARR, days to renewal, the main warning signal and the owner. Clicking a row opens a detail panel with a suggested next step. "Add to my day" and "Snooze 7 days" (with Undo) are the actions there.
- **Your day:** a checklist of today's follow-ups.
- **Filters:** segment, owner and search all update every number on the page. A state switcher on the table previews the loading, no-results and error views.
- **Display:** light and dark themes follow the viewer's setting, and the layout stacks for phones.

Filters and sort aren't kept in the page link, because artifact pages only allow a plain `#name` there.

To make it real, I'd need to know which CRM and support tools feed it and how your team scores health.
