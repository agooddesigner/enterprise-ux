# Navigation and layout

**Load when:** designing the app shell, side/top nav, breadcrumbs, page templates (list, detail, wizard, overview), tabs, choosing side panel vs page vs modal for records, URL state, or responsive behaviour.

## 1. App shell
- **Side nav is the enterprise default** once there are >5–6 destinations or users switch often; top nav only for 2–7 items, 1–2 levels. (Carbon >5, Ant >6)
- **Max 2 levels** in the side nav (parent + child). At 3+, move deeper pages to in-page links + breadcrumbs, or rethink IA. Ant tolerates 3 — don't. (Cloudscape, Carbon)
- **Exactly one active item always.** On a detail page the parent resource-type link stays active. (Cloudscape)
- Order general → specific. No sections with only 2 links; don't mix sections with expandable groups. (Cloudscape)
- No "New"/"Beta" badges, no links to create/edit flows, no unbounded user-created lists in the shell — use drill-down. (Cloudscape, Carbon)
- Collapsed icon rail only when icons unambiguously represent every destination. (Cloudscape)
- Closed by default on create/edit pages; open elsewhere. (Cloudscape)
- Dashboard (if any) is the first nav link and the returning-user landing page. (Cloudscape)
- Nav labels never truncate. (PatternFly)
- Hamburger icon is for main navigation only. (NN/g)

### Header and utilities
- Left → right: menu toggle (only if collapsible side nav), product name, product links, then utilities right-aligned. (Carbon)
- Utility icon order, fixed so it never moves between products: **search (leftmost) → help → notifications → account → app switcher (rightmost)**. (Carbon)
- Utilities open panels, not new pages; header links never open new tabs or jump domains. In-page actions never go in the utility area. (Carbon, Ant)
- Keep repeated help in the same relative position on every page. (WCAG 3.2.6)
- Never remove the global header in degraded mode; drop only failing items. (Primer)

### Skip link and landmarks
- "Skip to main content" is the first focusable element. Each `<nav>` landmark has a unique label. Visual order = DOM order. (Carbon, Primer, WCAG 2.4.1, 1.3.2)
- Each view sets a descriptive `<title>`, including SPA route changes, based on its single `<h1>`. (WCAG 2.4.2, GOV.UK)

### Workspace / tenant switcher
- The team/org switcher is the primary context selector, top-left near the product name; show plan badge next to the tenant name; settings, usage and data are scoped to the selected tenant. (Vercel)
- Always show the current tenant on every page; changing tenant resets to that tenant's landing page, never a 404. (general practice)
- Hierarchy (org → workspace → team) and cascading settings: see `saas/accounts-and-permissions.md`. (Notion)

## 2. Breadcrumbs
- Show at **≥3 levels** of hierarchy; don't also add a header back button. (Ant)
- Show hierarchy, not browsing history. (Lightning)
- Format: service/app → resource type → resource name. **Page title matches the last crumb**; no "details" suffix. (Cloudscape)
- Create flows end in "Create [X]" and don't change during the flow. (Cloudscape)
- Truncation: when >3 levels, show the last 2 and collapse the rest behind an ellipsis menu. (Lightning)
- Breadcrumbs change the URL. (Primer)
- Markup: `<nav aria-label="Breadcrumb">` + `<ol>`; current item `aria-current="page"`; separators hidden from AT. (APG)
- Test: land users on a random deep page — they should know where they are and what's above. (Ant)

## 3. Page archetypes (floorplans)
Pick one archetype per job; don't invent hybrids. (Fiori)

| Archetype | Use for | Key traits |
|---|---|---|
| List report | Find and act on items in a large set | Mandatory filter bar applying to all tables/charts; saved views; header collapses on scroll (Fiori) |
| Worklist | Work through a smaller queue | Tabs as filters with counts; return to list after each item; confirm with toast (Fiori) |
| Object page | One object: display, edit, create | Dynamic header, anchor bar/tabs, footer finishing actions (Fiori) |
| Analytical list page | Root-cause analysis | Chart and table interact (Fiori) |
| Overview page | Card-based entry to a domain | Cards; skeleton clears once first card loads (Fiori) — see `patterns/dashboards-and-dataviz.md` |
| Initial page | Retrieve one known item by ID | Single search/ID field (Fiori) |
| Wizard | Guided, branching, dependent creation | ≤7 steps, ideally 3–5, review step (Cloudscape, PatternFly) — see `patterns/forms-and-saving.md` |
| Details as hub | Resource with many related collections | Detail page linking to related lists; any list >10 items gets its own view, not a container (Cloudscape) |
| Single-page create | Simple to medium create | Required fields first, "Additional settings" expandable (Cloudscape) |

## 4. List page anatomy
Top to bottom:
1. Breadcrumbs (if ≥3 levels).
2. Page header: `<h1>` title + count ("Invoices (1,284)"), page actions right with primary "Create [resource]" rightmost. (Cloudscape)
3. Optional info/flashbar region. (Cloudscape)
4. Filter bar / search + saved view selector, above the content it filters; applied-filter chips + "Clear all"; filter state in the URL. (Fiori, Baymard, see foundations/defaults.md) — `patterns/filters-and-search.md`.
5. Collection header: refresh, settings (columns/density), export, bulk actions on selection. (Cloudscape, Carbon)
6. Table/cards: identifier column first as a link. (NN/g, Polaris) — `patterns/tables.md`.
7. Pagination directly under the list. (Primer, Carbon)
- New items appear at the top, briefly highlighted. (Fiori, Ant)
- Remember position in the list and mark viewed items. (Ant)

## 5. Detail page anatomy
- **Header:** title (object name, matches last crumb), subtitle, status badge, key KPIs/attributes (1–5 label-value pairs), breadcrumbs. Collapsible on scroll. (Fiori, Cloudscape)
- **Actions on the whole resource in the header** (Edit, Delete, Share), ordered per `patterns/actions-and-dialogs.md`. Actions use text or icon, not both. (Cloudscape, Fiori)
- **Finishing actions (Save, Cancel, Submit) in a sticky footer**, never the header; message button with error counter at footer left. (Fiori)
- Same layout in display, edit and create modes so nothing shifts. (Fiori)
- **Section navigation:** anchor bar (scroll-spy) by default when users read across sections; tabs when sections are independent or heavy to load. (Fiori)
- **Related records:** inline ≤20 items; 5–10 then "More" up to ~100; own tab ~50–400; >400 → 10–20 preview rows + "Show all (n)" to a list report. (Fiori). Cloudscape: lists >10 leave containers → details-as-hub.
- References to other objects open a quick-view popover; drill-down rows show a chevron only if the user can open them. (Fiori)
- **Activity / history:** chronological feed with relative timestamps (absolute on hover); audit-grade history uses absolute time + zone. See `saas/collaboration-and-audit.md` and foundations/defaults.md.
- Settings shortcut: icon button top-right under breadcrumbs, "Configure in settings", deep-linking to the right section. (Pajamas)
- Don't dump every field on the object page; stay role-based. (Fiori)

## 6. Tabs
- Use only for clearly grouped, independent content where users **don't need to compare across tabs**; never for sequential steps. (NN/g, Lightning)
- Default tab = most important content. (NN/g, Lightning)
- One row, never stacked; above the panel; 1–2 word plain labels, sentence case, no all caps. (NN/g)
- **Parallel labels**: all nouns or all verbs. (Lightning)
- Selected state uses **≥2 cues** (underline + bold/colour). (NN/g)
- Overflow → "More" menu in the last position. Never nest global tabs; use a tree for deep hierarchies. (Lightning)
- **Don't mix navigation tabs (change URL) and panel tabs (switch content) in one bar or app.** (Primer, NN/g)
- Worklist tabs show counts. Views of the same data: segmented button ≤3 views, select for more; tabs when sort/actions differ. (Fiori)
- Panel tabs: `tablist`/`tab`/`tabpanel`; arrows move; automatic activation only if panels render instantly, else manual. Don't style nav links as ARIA tabs. (APG, WebAIM)

## 7. Record views: side panel vs page vs modal

| Situation | Use | Source |
|---|---|---|
| Quick look, content <1 screen | Inline expand / expandable row | Ant, Carbon |
| Edit/inspect while keeping list context, longer than a screen | Non-modal side panel / drawer | NN/g, Ant |
| Rapid switching between items | Two-pane master–detail | Ant |
| Shareable, complex, many sections or actions | Full page with its own URL | Ant, Carbon |
| Create with <8 fields | Modal | Fiori |
| Create with ≥8 fields or sub-objects | Page | Fiori |

Cramped expandable rows graduate to a side panel, then a page. (Carbon). Side panels need their own URL param if users share them. (general practice)

## 8. URL-addressable state
- URL is the single source of truth for filters, sort, page, view, selected tab, open record; write on change, read on load. (Cloudscape)
- Validate/discard bad URL values; never put sensitive data in URLs. (Cloudscape)
- Breadcrumbs, nav, pagination and nav-tabs change the URL; Back must work. (Primer, GOV.UK)
- Don't persist state when it's unclear which of several tables it belongs to. (Cloudscape)
- Remember simple user settings (last sort, density, columns) across sessions. (NN/g, Fiori)

## 9. Responsive targets
| Class | Width | Enterprise behaviour |
|---|---|---|
| Compact | <600dp | Single column; nav behind menu; tables → list/tiles; dialogs full-screen (M3, Fiori, Lightning) |
| Medium | 600–839dp | Dashboards 1 column (Pajamas); 1–2 table columns (Fiori) |
| Expanded | 840–1199dp | Side nav collapsible; 3–5 table columns in split layouts (M3, Fiori) |
| Large | 1200–1599dp | **Primary design target 1280–1440px**; ~8 table columns at full width (M3, Fiori) |
| Extra-large | ≥1600dp | Cap line length; use space for side panels, not stretched forms (M3; general practice) |

- 1280–1440 as primary desktop target is (general practice); enterprise web mostly lives in Expanded and up. (M3)
- **Reflow at 320 CSS px** (= 1280px at 400% zoom): side nav → menu button, multi-column forms → one column, toolbars wrap or overflow to "More", sticky headers shrink. Only data tables, maps, diagrams may scroll 2-D inside their own container. (WCAG 1.4.10)
- 200% text zoom with no loss; focused elements never fully hidden by sticky headers/footers (use `scroll-padding`). (WCAG 1.4.4, 2.4.11)
- Grid/tree tables are desktop/tablet only; phones get a responsive table or list. (Fiori)
- Header links collapse into the left panel on narrow screens. (Carbon)

## 10. NN/g complex-app layout guidelines
- **Show secondary detail in place** (hover a chart point, quick-view popover) instead of sending users to another screen. (NN/g)
- **Flexible pathways:** users skip ahead, loop back, jump between steps without losing work; no rigid linear flows. (NN/g)
- **Staged disclosure, max 2 levels:** advanced options appear only when relevant, behind a clearly labelled control; 3+ levels confuse. (NN/g)
- Reduce clutter without removing capability; make the important things stand out by removing non-essentials. (NN/g)
- Let users annotate data and resume after interruption; offer "Continue where you left off" with recent items. (NN/g)
- Keep multi-step processes on one page where possible; each page switch breaks flow. (Ant)
- Keep context visible across steps; don't make users copy an ID between screens. (Working Memory)

### User types (NN/g)
| Type | Who | Layout implications |
|---|---|---|
| Legacy | Long-time users with workarounds | Roll out layout changes gradually, announce early, keep the old view available during transition, don't reorder stable nav (Serial Position, Jakob's Law) |
| Legend | Expert power users | Density options, keyboard paths, saved views, customizable layouts — without breaking defaults |
| Learner | Domain experts new to the tool | Inline/just-in-time help, clear labels, templates, sensible defaults; no reliance on training |

Defaults must work because most users never customize. (NN/g)

## Common AI failures
- Top nav with 12 items, or 3–4 levels of nested side nav.
- No active nav item on detail pages, or two highlighted at once.
- Breadcrumbs on 2-level pages, or breadcrumbs that mirror history; page title differing from the last crumb.
- Save/Submit in the page header next to Edit/Delete.
- Tabs used for wizard steps, comparisons, or mixing route-tabs and panel-tabs.
- Every record opening in a modal, including long ones with related lists.
- Filters, sort, open tab and selected record not in the URL; Back breaks.
- Designed only at 1920px; nothing reflows at 320px; sticky headers cover focused fields.
- Utility icons in arbitrary order, or in-page actions in the global header.
- Redesigns that move every nav item with no transition for legacy users.

## Sources
- https://carbondesignsystem.com/components/UI-shell-left-panel/usage/
- https://carbondesignsystem.com/components/UI-shell-header/usage/
- https://carbondesignsystem.com/patterns/global-header
- https://carbondesignsystem.com/components/data-table/usage/
- https://spring-21.lightningdesignsystem.com/guidelines/navigation
- https://spring-21.lightningdesignsystem.com/guidelines/displaying-data
- https://www.sap.com/design-system/fiori-design-web/v1-84/page-types/floorplans/list-report-floorplan-sap-fiori-element/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/work-list/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/usage
- https://www.sap.com/design-system/fiori-design-web/v1-151/ui-elements/dialog/usage
- https://cloudscape.design/patterns/general/service-navigation/side-navigation/
- https://cloudscape.design/patterns/resource-management/details/details-page/
- https://cloudscape.design/patterns/resource-management/create/single-page-create/
- https://cloudscape.design/patterns/resource-management/create/multi-page-create/
- https://cloudscape.design/patterns/general/filter-patterns/filter-persistence-in-collection-views/
- https://cloudscape.design/patterns/general/actions/global-actions/
- https://cloudscape.design/patterns/general/service-dashboard/
- https://primer.style/product/ui-patterns/navigation
- https://primer.style/ui-patterns/degraded-experiences
- https://www.patternfly.org/content-design/grammar/truncation
- https://patternfly.org/components/wizard/design-guidelines
- https://design.gitlab.com/patterns/settings-management
- https://design.gitlab.com/patterns/dashboards
- https://ant.design/docs/spec/research-navigation
- https://ant.design/docs/spec/detail-page
- https://ant.design/docs/spec/data-list
- https://5x.ant.design/docs/spec/stay
- https://www.nngroup.com/articles/complex-application-design/
- https://www.nngroup.com/articles/complex-apps-users/
- https://www.nngroup.com/articles/tabs-used-right/
- https://www.nngroup.com/articles/contextual-menus-guidelines/
- https://www.nngroup.com/articles/progressive-disclosure/
- https://www.nngroup.com/articles/designing-for-waits-and-interruptions/
- https://www.nngroup.com/articles/flexibility-efficiency-heuristic/
- https://nngroup.com/articles/modal-nonmodal-dialog/
- https://nngroup.com/articles/data-tables
- https://gov.uk/service-manual/design/writing-for-user-interfaces
- https://design-system.service.gov.uk/patterns/question-pages/
- https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes
- https://vercel.com/docs/notifications
- https://www.notion.com/en-gb/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
- https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb
- https://w3.org/WAI/ARIA/apg/patterns/tabs/
- https://www.w3.org/TR/WCAG22
- https://lawsofux.com/jakobs-law/index.md
- https://lawsofux.com/serial-position-effect/
