# Eval cases

8 cases covering all four modes plus accessibility and AI. Each case has:
- **Prompt** — paste exactly, nothing else, into a fresh chat.
- **Checks** — binary (1 = clearly present in the output, 0 = missing, wrong or only vaguely mentioned). Partial credit is not allowed; it makes scores drift between graders.

Score per case = checks passed ÷ total checks. Prompts never mention the skill — the point is to see whether the skill changes what Claude does on its own.

---

## E1 — Design: invoices list (code)

**Prompt**
```
Build an invoices list page for a finance admin who reviews around 200 vendor invoices a day and needs to approve, reject or delete them. Single HTML file with inline JS and CSS.
```

**Checks (20)** — strict: count a check only if the behaviour is actually implemented, not just described.
1. Native `<table>` with a programmatic name (`<caption>` or `aria-label`) and `<th scope="col">` headers
2. Sortable headers are `<button>`s inside `<th>`, with `aria-sort` set only on the currently sorted column
3. Seed data ≥ 50 rows and includes all three: a long vendor name (≥ 40 chars), an empty optional field, and a zero or negative amount (credit note)
4. Empty optional values render as a dash ("—"/"-"), and a real 0 renders as 0 (not a dash)
5. Amounts right-aligned with tabular figures (`font-variant-numeric: tabular-nums` or equivalent), currency and 2 decimals
6. Dates are unambiguous (e.g. "3 Mar 2026" or ISO) — not 03/04/2026 style
7. Search, filters, sort AND page are written to the URL and restored from the URL on page load
8. Applied filters appear as individually removable chips plus a "Clear all"
9. A visible result count reflects filters (e.g. "12 of 200 invoices")
10. Distinct first-use empty state AND no-results state; the no-results state offers a one-click "Clear filters"
11. Initial load shows a skeleton of table rows (not a centred spinner on a blank page), and this state is actually reachable (simulated latency or a toggle)
12. Load-failure state with Retry exists and does NOT show the "no invoices" empty message
13. Header checkbox selects the current page only; a separate explicit "Select all N matching" option exists
14. Selection count is visible with a "Clear selection" control; selection is cleared or explicitly preserved when filters/sort/page change
15. Bulk actions handle ineligible rows (e.g. already approved) by warning before running OR reporting succeeded/skipped/failed counts after
16. Delete uses Undo (soft delete) or a confirmation that names the count and consequence; the confirm dialog's initial focus is not on the destructive button
17. Bulk action buttons name object and count (e.g. "Approve 5 invoices"); no generic "OK"/"Submit"/"Yes" anywhere
18. Action results are announced via a live region (`role="status"`/`aria-live`), and no error is shown only in an auto-dismissing toast
19. Row actions are keyboard reachable with a visible `:focus-visible` style; nothing is hover-only
20. Status uses a small fixed vocabulary of text badges (not colour alone), and the page shows a "last updated" time or refresh control

---

## E2 — Design: user & role management (code or spec)

**Prompt**
```
Design the "Members" page of a B2B SaaS admin console where workspace admins invite people, change their roles and remove them. The company uses SSO. Give me the screen as a single HTML file.
```

**Checks (15)** — strict: count a check only if the behaviour is actually implemented, not just described.
1. Each role shows what it can AND cannot do (description, comparison matrix, or can/can't list) at the point of choosing a role
2. Invite accepts multiple emails; an invalid email gets a specific inline message and the other entered emails are kept
3. Pending invites are distinct from active members and have Resend and Revoke actions plus an expiry date/state
4. SSO/SCIM-managed members or fields are read-only and labelled with their source (e.g. "Managed by Okta")
5. Remove confirmation names the person AND states what happens to their content/ownership and access
6. Removing or demoting the last admin/owner is blocked with an explanation
7. Admin can't grant a role higher than their own OR changing their own role is prevented/warned
8. Seat or billing impact is shown with a number when inviting or removing (e.g. "Uses 3 of 25 seats")
9. Disabled actions show the reason (tooltip/text on a focusable element, not a bare greyed-out control)
10. Suspend/deactivate exists as a separate, reversible state from remove
11. Each member row or detail shows who last changed their role and when, OR an audit log entry is visibly created for role changes
12. Demoting a member (losing permissions) needs confirmation or offers Undo; promoting is immediate with feedback
13. Feedback after role change is announced via a live region and the table updates without reload
14. Form fields in the invite flow have visible labels (not placeholder or sr-only)
15. The page considers a non-admin viewer: what a member/viewer sees if they open this page (read-only view or no-access state)

---

## E3 — Design spec: bulk CSV import (no code)

**Prompt**
```
Write a UX spec for importing up to 50,000 contacts from a CSV file into our CRM.
```

**Checks (12)**
1. Downloadable template or clearly stated file requirements before upload
2. Header-row detection or confirmation step
3. Column-to-field mapping step with auto-suggestions the user can override
4. Value mapping for enum/picklist fields (e.g. "US" → "United States")
5. Validation reports errors at row/cell level with a specific message
6. User can fix errors in place (or exclude bad rows) without re-uploading
7. Duplicate handling strategy (skip / update / create) is chosen by the user
8. Large files process in the background with progress and the user can leave
9. Completion summary: imported / updated / skipped / failed counts
10. Downloadable error report for failed rows
11. Undo or rollback of an import, or a clear statement that it can't be undone before confirming
12. States covered: uploading, processing, success, partial failure, total failure

---

## E4 — Grill: weak PRD

**Prompt**
```
Here's our PRD. Start designing it.

"Managers need a dashboard with all the KPIs. Every action should have a confirmation popup to be safe. We'll add roles and permissions in v2. Make it look like Salesforce. Success metric: page views."
```

**Checks (10)**
1. Does NOT start designing immediately without raising problems (asks or challenges first, or clearly flags issues before proceeding)
2. Challenges "all the KPIs" — asks which decisions/questions the dashboard must answer
3. Challenges confirmation on every action — recommends undo for reversible actions / reserving confirms for destructive ones
4. Challenges deferring permissions to v2 (explains why it's costly or a must-have)
5. Challenges page views as the success metric and proposes an outcome/task metric
6. Questions "look like Salesforce" (asks which job/pattern it solves, or warns against cloning)
7. Asks about users/roles (which managers, what they do, how often)
8. Asks about data (volume, sources, freshness)
9. Questions are prioritised or limited (not an unranked dump of 15+ questions)
10. States default assumptions it would use if questions go unanswered

---

## E5 — Plan: approvals inbox

**Prompt**
```
Help me plan an approvals inbox for finance managers who approve expense claims. We haven't designed anything yet.
```

**Checks (12)**
1. States the job as a job story or equivalent (situation → motivation → outcome)
2. Estimates or asks task frequency/volume (claims per day)
3. Identifies multiple roles (submitter, approver, admin/finance ops, auditor — at least 3)
4. Considers data scale and realistic content (amounts, receipts, policy flags)
5. Lists states to design (empty/inbox zero, loading, error, no permission at minimum)
6. Includes permissions or approval rules (thresholds, delegation, self-approval prevention)
7. Defines success metrics tied to the outcome (e.g. time to approve, backlog) — not just usage
8. Proposes research or validation with real users and roughly how many per role
9. Mentions audit trail for approvals/rejections
10. Mentions bulk approval and/or keyboard efficiency for high volume
11. Mentions accessibility target (e.g. WCAG 2.x AA)
12. Separates v1 scope from later (MVP / walking skeleton / release slice)

---

## E6 — Audit: planted-issue screen

**Prompt** (paste the contents of `fixtures/audit-target.html` from `<html>` to `</html>` — **not** the top comment)
```
Review this screen for UX and accessibility problems. Prioritise them.

<paste HTML here>
```

**Checks (20)** — 18 planted issues + 2 quality checks. Count an issue as found only if the output names that specific problem.
1. Inputs use placeholder instead of visible labels
2. Submit button disabled with no explanation
3. Vague "Submit" button label
4. "Invalid input" error is vague / not tied to a field / no fix suggested
5. Form clears user input on submit/error
6. Focus outline removed (`outline: none`) → no visible focus
7. Status shown by colour dot only
8. Icon-only buttons lack accessible names
9. Icon buttons too small (below 24×24px target size)
10. Row delete has no confirmation or undo
11. "Delete All" is irreversible with no confirmation/scope
12. Table built from divs; rows clickable via `onclick` on non-interactive elements (not keyboard accessible)
13. Numbers centred and/or inconsistent decimals/no currency
14. First column is an opaque system ID
15. Error toast auto-dismisses quickly and shows technical "Error 500"
16. Full-page centred spinner / blocking load
17. Low-contrast muted text (#b5b5b5)
18. Modal opens another modal (or sticky header can obscure focus, or generic page title "App" — any one)
19. Issues are ranked by severity/impact (not a flat list)
20. Each top issue has a concrete fix (not "consider improving")

---

## E7 — Accessibility: kanban board

**Prompt**
```
Build a drag-and-drop kanban board for support tickets (columns: New, In progress, Waiting, Done) as a single HTML file, and make it fully accessible. Briefly explain the accessibility decisions.
```

**Checks (10)** — strict: count a check only if the behaviour is actually implemented, not just described.
1. Every card has a single-pointer "Move to…" control (menu/dialog) that moves it without dragging (WCAG 2.5.7)
2. Cards can be moved with keyboard alone, and Escape cancels an in-progress keyboard move, restoring the original position
3. A persistent live region announces pick-up, each move (card name + column + position) and cancel
4. After a move, focus stays on the moved card
5. Semantics: columns are headed lists (`<h2>`/`<ul>`), each card exposes one primary interactive element; no `role="application"`/`role="grid"`
6. Column headings include an updating count (e.g. "In progress (3)")
7. Visible `:focus-visible` indicator of at least 2px, and focused cards are not hidden under any sticky header (`scroll-padding`/`scroll-margin` or no sticky elements)
8. Move/menu controls are at least 24×24 CSS px
9. Motion respects `prefers-reduced-motion`, and drag affordances still work in forced-colors/high-contrast (border/outline, not background-only)
10. Pointer drag still works for mouse users (the feature isn't removed to achieve accessibility)

---

## E8 — AI feature: auto-categorise expenses

**Prompt**
```
Design an AI feature that automatically categorises company expenses into GL codes for our finance SaaS.
```

**Checks (12)**
1. AI suggestions are labelled as AI-generated
2. User can accept, reject or edit each suggestion
3. Shows confidence, preferably categorical (high/medium/low) rather than raw %
4. Low-confidence items go to human review instead of auto-applying
5. Explains why ("based on vendor and past codes") or shows sources
6. Undo / revert for AI-applied changes
7. Bulk accept for high-confidence items
8. Admin controls: enable/disable, thresholds or scope
9. Audit log records AI vs human changes
10. Explains limits/accuracy to users up front
11. Has a manual fallback path that works without AI
12. Tracks a quality metric (override/correction rate, accuracy)

---

## E9 — Design: operations dashboard (code)

**Prompt**
```
Build a dashboard for the VP of Customer Support at a B2B SaaS company. They check it every morning to decide where to send their 40 agents today. Single HTML file with inline JS and CSS; use realistic data.
```

**Checks (16)** — strict: count a check only if it is actually implemented, not just described.
1. Page states the decisions it supports or is visibly organised around them (e.g. "Where to staff today" / queues needing attention), not a generic chart wall
2. 3–6 KPI tiles at the top, each with a unit and a comparison against a stated baseline (e.g. "vs yesterday", "vs target")
3. KPI change direction is shown with an arrow/icon or text, not colour alone
4. Shows a visible "last updated" / "data as of" timestamp (a refresh control is optional — a timestamp alone passes)
5. All tiles and charts share one stated time window (e.g. "Today, since 00:00 PT") or a single global date filter
6. At least one actionable list (e.g. queues/tickets breaching SLA) that links or drills down to the underlying records
7. Charts use length/position encodings (bars/lines); no pie/donut with >5 slices, no gauges, no 3D
8. Bar charts start at zero and categorical bars are sorted
9. Each data series keeps the same colour across charts; ≤ 6 colours in use
10. Hover/focus gives exact values, or exact values are labelled directly
11. Charts have a text alternative (summary or a "View as table"/data table)
12. Per-widget loading or error state exists and one failing widget doesn't blank the dashboard
13. Uses real domain metrics for support staffing (e.g. backlog, SLA breach risk, first response time, agents online, forecast volume) — not generic "revenue/users"
14. Global filters (team/region/channel) apply to all widgets and are reflected in the URL
15. Layout follows a clear hierarchy: summary at top, detail lower; most important KPI most prominent
16. App shell present: primary navigation with the current section marked, plus global search and account/notifications

---

## E10 — Intake: vague request (interactive)

**Prompt**
```
We need a dashboard for our customer success team. Can you design it?
```

**Checks (9)** — the right behaviour is to ask before building. A full build without questions fails checks 1–8 unless it opens with an explicit assumptions block (then only check 9 can pass).
1. Asks clarifying questions before producing a full design (no complete screen delivered as the first answer)
2. Asks at most 5 questions
3. Questions are multiple-choice or offer concrete options (not only open-ended)
4. Most questions carry a recommended/default option
5. Covers who uses it and how often (or what decisions they make)
6. Covers the main job / decisions the dashboard must support
7. Covers data volume or roles/permissions or data sources (at least one)
8. Asks about visual direction with ≥3 named style options, OR asks whether an existing design system exists first
9. Says what it will do if there is no answer (e.g. proceed with stated defaults)

---

## E11 — Intake: user away (headless build)

**Prompt**
```
Build the agent ticket queue screen for our helpdesk product, Relay. Agents work in it all day. Single HTML file with inline CSS and JS. I'm offline for the next few hours — don't wait for answers, make the calls yourself.
```

**Checks (12)** — strict: count only what is implemented or explicitly written.
1. Output (response or page) states explicit assumptions about users, data volume and/or roles before or alongside the build
2. Output names the visual direction (a named style/preset or explicit dial choices such as density, radius, palette strategy)
3. The direction is justified by context (all-day queue work, power users) rather than taste alone
4. Compact density: table/list rows ≤ 40px or body text ≤ 14px in the CSS
5. Composition is list-detail (queue + open ticket) or table-first — not a KPI/bento dashboard
6. Keyboard shortcuts for triage are implemented and visible (e.g. j/k, e, a, / or ⌘K hints)
7. App shell present: primary navigation with current section, global search, account/notifications
8. At least 40 realistic tickets (real-looking subjects, customers, priorities)
9. Loading, empty and error states exist and are reachable (toggle, param or function)
10. Bulk selection with a selected count and a "select all N matching" step
11. SLA / due time shown, with absolute time + time zone available (hover/title or text)
12. It actually built the screen (did not stop to ask questions)

---

## E12 — Existing design system (don't restyle it)

**Files:** fixtures/acme-ds.css

**Prompt**
```
Our design system is in acme-ds.css in this folder. Build the usage & billing page for workspace admins of our product, Ledgerly, as a single HTML file that links acme-ds.css. Admins open it a few times a month.
```

**Checks (10)** — strict.
1. Links acme-ds.css and uses its tokens (`var(--ds-…)`) for colours; introduces ≤ 3 new hex colours outside status colours
2. Uses the DS radius tokens; no new radius values above 6px (no 16px+ rounded "bento" cards)
3. Uses the DS font; imports no new font family
4. Does not ask the user to choose a visual style and does not propose a different style preset
5. Uses the DS component classes (`.ds-btn`, `.ds-card`, `.ds-table`, `.ds-badge`, `.ds-input`) where they fit
6. Usage vs limit shown with numbers, units and the billing period (e.g. "8,420 of 10,000 API calls · Oct 1–31")
7. Billing shows current plan, next invoice date and amount, and payment method
8. Loading, empty and error states exist and are reachable
9. Permission handling: non-billing roles see a read-only or no-access state with the reason
10. App shell present: primary navigation with current section, account menu

---

## E13 — Mixed visual direction

**Prompt**
```
Build a billing overview page for finance managers at our product, Tally. Style: Stripe-like restraint overall, but I want the top KPIs in a bento layout with one hero number. Must support light and dark mode. Single HTML file.
```

**Checks (10)** — strict.
1. States the direction explicitly as a lead style plus borrowed elements (e.g. "Restraint lead, bento composition for KPIs")
2. UI colour is restrained: neutrals + at most one accent; other colour only for status
3. Top KPI area is a bento grid with one clearly larger hero tile
4. Below the KPIs the page is table/list-first (the whole page is not bento cards)
5. Light and dark both implemented (toggle and/or prefers-color-scheme)
6. Dark mode avoids pure black (#000) and uses lighter surfaces, not heavy shadows, for elevation
7. No clashing effects: no glassmorphism, no hard offset shadows, no decorative gradients
8. Money values use tabular numerals, right-aligned in tables, consistent currency formatting
9. Status shown with text + colour (pill/badge), never colour alone
10. App shell present: primary navigation with current section, search, account
