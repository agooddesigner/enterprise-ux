---
name: enterprise-ux
description: Senior UX judgment and visual craft for B2B / enterprise SaaS — plan, grill, design and audit products, flows and screens that look beautiful and work flawlessly. Covers data tables, filters, forms, bulk and destructive actions, dashboards, every empty/loading/error/permission state, RBAC and admin consoles, onboarding, billing, notifications, audit logs, integrations, AI features, i18n, performance, UX writing, UX laws and heuristics, and WCAG 2.2 AA accessibility. Rules are distilled from Carbon, Atlassian, Salesforce Lightning, SAP Fiori, AWS Cloudscape, GitHub Primer, PatternFly, GitLab Pajamas, Shopify Polaris, GOV.UK, Material, Ant Design, NN/g and W3C. Use for any internal tool, admin panel, back-office, CRM/ERP/ops UI or data-heavy SaaS work — in code, mockups or specs — and whenever asked to review, critique, stress-test or plan such a product. Not for marketing sites or consumer apps.
---

# Enterprise UX

Enterprise users don't browse. They come to finish a job — often the same job 40 times a day, under time pressure, with real money, data or access at stake. They can't switch tools when it's painful; they suffer it. So **speed, clarity, safety and access for everyone** are the product. Pretty is table stakes.

Most AI-generated SaaS UI fails the same way: it designs the happy path with six perfect rows and forgets the 50,000-row tenant, the viewer who can't edit, the API that times out, the screen-reader user, and the "Delete 312 records" button with no undo. This skill exists to stop that.

## Pick a mode

| The user wants to… | Mode | Load first |
|---|---|---|
| Start something new, turn a request/PRD into a plan, define scope, metrics, research | **Plan** | `references/modes/plan.md` |
| Stress-test a requirement, brief or design; "grill me", "poke holes", "what am I missing" | **Grill** | `references/modes/grill.md` |
| Build or redesign a screen, flow or component (code, mockup or spec) | **Design** | `references/modes/design.md` |
| Review, critique, audit, "is it ready", accessibility check | **Audit** | `references/modes/audit.md` |

Modes chain: **Plan → Grill → Design → Audit**. Every Design starts with **Intake** (`modes/design.md` step 0): find the design system, then — if a whole screen/flow is requested and 2+ of {users & frequency, main job, data volume/roles, visual direction} are unknown — **ask ≤5 multiple-choice questions with recommended defaults and stop; don't build in the same reply**, even if your environment encourages starting immediately. If the user said to proceed without them or nobody can answer, open your reply with an `Assumed:` block and build. Always state the direction line (`Direction: lead X; borrow Y`) in your reply. Every Design ends with the Audit self-check.

Load only the references the current task needs. Don't read the whole folder.

## Reference map

**Foundations** — load when making cross-cutting decisions
- `references/foundations/defaults.md` — house rules where major design systems disagree (validation timing, toasts, row height, timestamps, delete friction…). **Read before your first design decision.**
- `references/foundations/ux-laws-and-heuristics.md` — 30 Laws of UX, Nielsen's 10, Shneiderman, Norman, Gestalt, NN/g complex-app guidelines — applied to enterprise, with misuses.
- `references/foundations/accessibility.md` — WCAG 2.2 AA criteria, thresholds, ARIA patterns, enterprise a11y, testing, legal landscape.
- `references/foundations/writing.md` — UX writing: labels, errors, empty states, success, tone, mechanics.
- `references/foundations/visual-direction.md` — **how to make it beautiful AND usable, in any style**: 11 aesthetic dials, 12 presets (Soft bento, Dark precision, Blueprint, Restraint, Classic enterprise, Warm paper, Data-dense, Swiss, Expressive, Neubrutalism, Glass accents, Tactile), mixing rules and clashes, safe layout experiments, composition archetypes, render-and-look loop. Works on any design system. **Load after Intake, before building any screen whose look isn't fixed by a design system.**
- `references/foundations/visual-craft.md` — polish details, generic-AI tells, contrast-checked fallback tokens (only when the product has no design system).
- `references/foundations/visual-and-motion.md` — density, spacing, type, colour, hierarchy, motion, response times.

**Patterns** — load for the component/flow you're working on
- `references/patterns/tables.md` — tables, grids, columns, sorting, pagination, selection, row actions, inline edit.
- `references/patterns/filters-and-search.md` — filter types, chips, saved views, search, zero results, URL state.
- `references/patterns/forms-and-saving.md` — form structure, controls, validation, save models, unsaved changes, wizards.
- `references/patterns/feedback-and-states.md` — state matrix, empty/loading/error/degraded, toasts vs banners vs modals.
- `references/patterns/actions-and-dialogs.md` — button hierarchy, disabled states, destructive actions, undo, bulk, dialogs, shortcuts.
- `references/patterns/navigation-and-layout.md` — app shell, page archetypes, detail pages, tabs, breadcrumbs, responsive.
- `references/patterns/dashboards-and-dataviz.md` — dashboards, KPI tiles, chart choice, data honesty.

**SaaS domains** — load when the feature touches these
- `references/saas/onboarding.md` — activation, admin vs end-user onboarding, checklists, tours, trials.
- `references/saas/accounts-and-permissions.md` — tenancy, SSO/SCIM, roles, permission UI, request access, approvals, settings.
- `references/saas/billing.md` — pricing, usage, upgrades, seats, cancellation, auto-renewal law.
- `references/saas/notifications-system.md` — channels, preferences, fatigue, notification center.
- `references/saas/collaboration-and-audit.md` — audit logs, history, concurrent editing, presence.
- `references/saas/integrations-and-data.md` — API keys, webhooks, CSV import, export, command palette.
- `references/saas/ai-features.md` — Human-AI guidelines, disclosure, confidence, agents, human-in-the-loop.
- `references/saas/global-and-performance.md` — i18n, RTL, time zones, Core Web Vitals, perceived speed.

`references/sources.md` lists every source behind these rules.

## Non-negotiables

Break one only with a stated reason.

1. **Name the job first.** Who, what job, how often — one line before any layout. Frequency decides density vs guidance.
2. **Design for real data.** p95 volume, longest values, nulls, zero, one. Never ship lorem ipsum or "Item 1".
3. **Screens live inside a product.** Always render the app shell unless only a component was asked for: primary navigation with the current section highlighted, product/workspace switcher, global search (⌘K), notifications, account menu, and breadcrumbs when deeper than one level. A dashboard with no way to get anywhere is broken UX. See `references/patterns/navigation-and-layout.md`.
4. **Every view has every state.** Empty (first-use ≠ no-results), loading, error, no-permission, read-only. A blank area is a bug; "No data" while loading or after a failed load is a lie.
5. **Undo beats confirm.** Reversible → act + Undo. Irreversible → confirm naming object, count and consequence. Critical/cascading → typed confirmation.
6. **Permissions are designed, not hidden by accident.** Hidden if never available to that role; otherwise disabled with the reason and who can help.
7. **Never lose user input.** Keep it after errors, warn on unsaved changes, never clear a form on failure.
8. **Errors say what happened and how to fix it** — next to the source, in plain words, without blame.
9. **State lives in the URL.** Filters, sort, page, tab, open record are shareable links.
10. **WCAG 2.2 AA by default.** Native elements first, full keyboard path, visible un-obscured focus, 24px targets, click alternative to drag, colour never alone.
11. **One primary action per view**, labelled with a specific verb ("Send invoice", not "Submit").
12. **Respect the existing design system.** Its rules beat these defaults. Never add a second button/table/modal style.
13. **Respond fast, show progress.** Feedback within 100ms; progress, cancel and background run beyond 10s.
14. **Beautiful and usable, never one without the other — and never an assumed style.** Enterprise buyers judge quality in the first screenshot; users judge it on the 200th use. Ask the direction in Intake (or use the design system / context default and say so), write it as a preset or mix of dials, then compose: one hero, size = importance, scale contrast, ≤1 anchor + ≤1 highlight, colour roles mapped onto the product's tokens, honest charts. See `references/foundations/visual-direction.md`.
15. **Honest by default.** No dark patterns in upgrades or cancellation; AI output labelled and correctable; uncertain or legal claims flagged "verify".

## Making it beautiful (read this even if you load nothing else)

Taste is not one look. **Never assume a style**: the existing design system wins; otherwise ask the direction in Intake (offer 3–4 presets from `references/foundations/visual-direction.md` that fit the context, plus "mix" and "match a reference"); if nobody can answer, pick by context (visual-direction §5) and state it. Then read visual-direction.md and write the 3-line direction (preset/mix · dials · hero) at the top of the work.

Mixing rule in one line: one preset leads (colour strategy, type voice, depth); borrow ≤3 dials from another; density may vary by zone; never break the invariants (AA contrast, status-only status colours, app shell, focus, real data, every state, honest charts).

**House default — Soft bento** (used for overviews, demos and first-impression dashboards when nothing else decides):
- Softly tinted canvas (cool grey / lilac-grey), **white cards with 20–28px radius**, 20–24px gaps, on a 12-column bento grid; size = importance, hero card top-left, rows end at the same line.
- **One anchor card in ink/near-black** carrying the screen's main answer, and **at most one highlight card** in a bright secondary (e.g. lime or soft violet). One data accent colour for emphasis and primary actions.
- **Scale contrast:** page title 40–56px, hero number 56–72px, KPI numbers 36–48px, all tabular; units/decimals at ~half size; labels 12–13px, quiet but ≥ 4.5:1.
- **App shell in the same language:** either a dark pill top nav (logo · sections · search · notifications · avatar) or a slim side nav with icons + labels and a pill-highlighted current item; the current section is always visible.
- **Pill and round shapes:** dark pill nav with a light active pill, pill chips for filters, pill buttons and deltas, 40–44px circular icon buttons, avatars.
- **Charts as calm shapes:** rounded bars on pale tracks with one highlighted bar, thick rings for a single ratio, rounded heatmap cells, sparklines in KPI cards — still zero-based, labelled and with a text alternative.
- **Contrast on loud cards:** text on ink cards uses near-white (primary) and a light grey ≥ 7:1 (secondary); text on the highlight card is near-black. Status colours: only good / warn / bad (+ neutral), as soft pills with a dot and a word.
- **UX parts styled to match:** filters as chips, a quiet freshness line under the title, incidents as soft tinted strips, per-card skeletons and errors, dark pill Undo toast.

With an existing design system: keep its tokens, fonts and components; apply the same composition, scale contrast and colour *roles* using its tokens.

## Ship gate — run before presenting ANY screen (even if you loaded nothing else)

Intake
- [ ] Design system looked for; Intake questions asked (≤5, with defaults) or an Assumptions block written at the top
- [ ] Direction written as a preset or mix of dials, matching what the user chose, and stated in the reply as `Direction: lead X; borrow Y`

UX
- [ ] App shell present: primary nav with the current section marked, workspace/product context, global search, notifications, account; breadcrumbs if nested
- [ ] Every data region has loading, empty (first-use and no-results), and error states — reachable via a state toggle/prop/query param
- [ ] Filters, sort, page, tab and selected record are written to and restored from the URL
- [ ] Lists/charts lead somewhere: rows and KPIs drill down to the underlying records
- [ ] Bulk actions: "select all N matching", count shown, skipped/failed items reported
- [ ] Destructive actions have Undo or a confirm naming object + count; no generic OK/Submit labels
- [ ] Data shows freshness ("Updated 08:10 PT") and a single stated time window where relevant
- [ ] Keyboard path, visible focus, labels, live-region announcements, colour never alone

Visual
- [ ] The locked direction is visible in the result (the chosen dials actually show); the product's design system tokens are used where they exist; no combo from the clash table without a stated reason
- [ ] The hero (the screen's main answer) reads first: largest card/number, top-left
- [ ] Scale contrast: numbers 2.5–5× body size, units/decimals smaller, labels quiet but ≥ 4.5:1
- [ ] One anchor (inverted) card and at most one highlight; one data accent; semantic colours only for status
- [ ] Cards snap to a 12-col grid, rows end together, no half-empty cards, nothing overlaps or floats over content
- [ ] Charts are calm and honest (rounded bars/tracks, zero baseline, direct labels, text alternative)
- [ ] Loading, error and empty states look as designed as the ready state
- [ ] If you can render it, you looked at a screenshot and fixed what you saw

Fix every unchecked item, then say in 2–3 lines what you checked.

## How to work

- **Be specific.** "Move Delete into the ⋯ menu, away from Save (Fitts's Law)" — not "consider improving action hierarchy".
- **Cite the rule** (system, heuristic, law or WCAG SC) when it settles a decision or a disagreement.
- **Say when something is taste**, not usability.
- **Ask, then assume.** Ask the few questions whose wrong answer is expensive; if nobody's there, state assumptions and proceed.
- **Show the work product**, not a lecture: a brief, a grill log, a built screen with states, or a ranked audit.
