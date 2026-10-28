# Tables and collection views

**Load when:** designing, critiquing or auditing any list of records — data tables, grids, tree tables, card/tile collections, row selection, bulk actions, pagination, inline edit, or table preferences.

If the product already has a design system, its table rules win. Otherwise apply these and `foundations/defaults.md`.

## 1. Pick the container

| Situation | Use | Source |
|---|---|---|
| Structured records, many attributes, users compare/sort | Table | (Cloudscape, Ant, Carbon) |
| Item-focused list that must work on every device | Responsive table (collapses to list/tiles on phone) | (Fiori, Lightning) |
| ~1,000+ rows, cell-by-cell comparison, cross-column operations, spreadsheet-like editing | Grid / analytical table (desktop/tablet only) | (Fiori) |
| Hierarchy where parents and children share the same fields | Tree table | (Fiori, Lightning) |
| Hierarchy where parent and child fields differ | Related list or master-detail, not a tree | (Lightning) |
| Fast scanning in a tight container | List | (Ant) |
| Mixed media / items of equal visual weight | Cards | (Ant, Cloudscape) |
| <10 items in a narrow space | Tiles; switch to a table once tiles would need >2 columns | (Lightning) |
| Goal is an overview of a large set | Chart, not a table — see `patterns/dashboards-and-dataviz.md` | (Fiori) |
| Field–value pairs about one object | Form / key-value layout, not a table | (Fiori) |
| Picking one item from very few | Select or combobox, not a table | (Fiori) |
| A few simple columns inside a content page | Plain bordered table, no toolbar | (Cloudscape) |

- Never nest tables, never squeeze a table into a small container, never use a data table as a spreadsheet substitute — use a grid. (Carbon)
- Tiles: act via buttons/links inside the tile, not by clicking the whole tile. (Lightning)
- Inside an object/details page, scale by row count: ≤20 inline; up to ~100 show 5–10 + "More"; ~50–100 up to 400 put the table in its own tab; >400 show 10–20 preview rows + "Show all (n)" to a full list page. (Fiori) Don't put lists >10 items in a details container; link to a hub page. (Cloudscape)

## 2. Density and row height

- Default 40px rows; offer a user-switchable compact 32px; apply density app-wide; never mix densities on one page. Touch → 44px+. (see `foundations/defaults.md`) (Carbon, Fiori, Lightning) **[consensus]** on user-controlled, app-wide density.
  - Alt: data-heavy, mouse/keyboard-only power tool → 32px default. (Fiori)
- Carbon scale for reference: 24 / 32 / 40 (default) / 48 / 64px; use 64px only when a row must hold 2 lines. Header row height = body row height. (Carbon)
- Toolbar, batch bar and pagination bar match row height. (Carbon)
- Font size stays the same across densities; only spacing changes. (Fiori)
- Phones/tablets always get the touch density. (Fiori)
- Use light borders, zebra stripes or row hover to aid comparison. (NN/g)

## 3. Columns

- **Identifier first.** First column = human-readable primary identifier (not an auto-generated ID), rendered as a link to the record; add a 40×40 thumbnail only if it helps recognition. (NN/g, Polaris, Lightning) **[consensus]**
- Order columns by importance left→right; keep related columns adjacent. (Cloudscape, NN/g)
- For create flows, the create-form field order becomes the default column order. (Cloudscape)
- **Alignment by type:** text and status left; numbers and dates right; icons/avatars centred; rows top-aligned. (Fiori, Polaris, Ant) **[consensus]** on right-aligned numbers.
- Put the unit in the header ("Cost (USD)") only when every row shares it; otherwise put the unit in each cell. (Fiori)
- Money: currency code + amount with consistent decimals. (Ant) Format dates per `foundations/defaults.md`.
- **Column count by width:** 1–2 on phone, 3–5 in a split/side-panel layout, ~8 at full desktop width. (Fiori)
- **Personalization:** offer show/hide and reorder when >~5 columns are needed in most cases; provide a non-drag way to reorder; show a count of hidden columns. (Fiori, NN/g)
- Keep the identifier column visible at every size; freeze header row (and first column) when the table exceeds the viewport. (Fiori, NN/g)
- Headers: 1–2 words, sentence case. **Never truncate column headers** — wrap to 2 lines when columns can't resize. (Carbon, PatternFly, Fiori) Alt: Carbon truncates with tooltip after 2 lines; Fiori truncates when columns are user-resizable — if you allow this, the full header must be in a tooltip and accessible name.
- If users can resize columns, scroll the table horizontally rather than reflowing columns. (Lightning)
- Don't change column headers in response to filtering. (Cloudscape)
- Never give buttons a column of their own, except the row-actions column below. (Fiori)

## 4. Cells

- **Empty value:** one dash glyph used app-wide ("—"); never blank, never for a real 0, never for an error. (see `foundations/defaults.md`) (Cloudscape, Ant, NN/g)
- **Status:** badge/label with icon + text, never colour alone. Show a status column whenever row actions depend on status. (Polaris, Cloudscape, WCAG 1.4.1)
- Keep time, status and action cells on one line. (Ant)
- No decorative graphics in table cells; use cards for media-heavy items. (Cloudscape)
- **Truncation:** keep ≥4 visible characters; truncate in the middle when the distinguishing part is at the end (file paths, IDs), at the end otherwise; always expose the full string (tooltip + accessible name); use the single "…" character. (PatternFly)
- Mask sensitive values but keep the character count visible (e.g. `186****1402`). (Ant)
- Make the clickable area the whole cell, not just the glyph. (Ant)
- Relative vs absolute timestamps per `foundations/defaults.md`.

## 5. Sorting

- Sort headers have 3 states: unsorted → ascending → descending. Only the sorted column shows its icon at rest; others reveal it on hover/focus. (Carbon)
- Default sort: the identifier's primary value, or the most task-relevant column (e.g. newest first for activity). (Fiori; general practice)
- Descending must be the exact reverse of ascending. Status columns sort by severity, neutral last when ascending. (Fiori)
- Single-column sort by default; choosing another column replaces it. Multi-sort is opt-in and shows numbered priority badges; put multi-level sort in a settings dialog. (Cloudscape, Fiori)
- Sort the **whole collection** server-side whenever data is paginated or partially loaded; never sort only the visible page. (general practice; Cloudscape applies the same rule to filters)
- Inline edit of a sorted column un-sorts the table so the edited row doesn't jump. (Cloudscape)
- Skip sort/group/column settings for tables of ≤20 rows. Order toolbar view settings: sort, group, columns. (Fiori)

## 6. Pagination vs load more vs progressive loading

| Situation | Use | Source |
|---|---|---|
| Big dataset, users jump between pages | Pagination at the bottom | (Cloudscape, Carbon) |
| Users must see everything in one view to compare | Progressive loading ("growing") | (Cloudscape, Fiori) |
| Feed where top items matter most | Load more | (Ant, Pajamas) |
| Thousands of rows in a grid | Virtualized rendering + `aria-rowcount`/`aria-rowindex` | (ARIA APG grid; general practice) |

- Never combine pagination and progressive loading (child rows excepted). (Cloudscape)
- Fiori responsive table: render ≤200 items at once, grow to ≤1,000 total, never more — beyond that require filtering. (Fiori)
- Paginate tables with >100 rows. (Polaris) Default to pagination. (Ant)
- Simple pagination = page + prev/next; advanced adds items-per-page and jump-to-page. (Carbon)
  - House default: show the pagination control even with one page so page size stays reachable. (Cloudscape) Alt: hide the pager when everything fits on one page. (Ant)
- Load more: centred "Load 20 more"-style button after the last item, only when more exist; move focus to the first new item; size batches by row density; don't combine with pagination. (Pajamas) Show loaded vs total ("50 of 1,240"). (Fiori)
- Prefer load-more over infinite scroll; infinite scroll traps keyboard users and hides the footer. (Pajamas; general practice)
- Remember the user's list position and mark viewed items when they return. (Ant)

## 7. Selection and batch actions

- Multi-select = checkbox column; single-select = radio column. Header checkbox is tri-state: none / some (indeterminate) / all. (Carbon)
- **Header checkbox selects the visible page.** Offer an explicit "Select all N matching" step; always show "N selected". Clear selection on sort/filter/page change unless the UI clearly shows it persists. (see `foundations/defaults.md`) (Cloudscape, Fiori)
  - Alt: high-volume triage → persist across pages with a bulk-selector split button (Select none / Select page / Select all) and a cross-page count. (PatternFly)
- Don't offer multi-select actions when the table usually has <10 rows. Never disable a row's selection checkbox. (Fiori)
- **Batch bar replaces the toolbar** while rows are selected; disable row-level actions/overflow in batch mode; exit via Cancel at the far right or by deselecting all. (Carbon) Sticky header when actions depend on selection. (Cloudscape)
- Selection-dependent actions disabled until valid; actions the user can never perform (authorization) hidden. Create/Add always enabled. (Fiori)
- **Partial failure:** run the action on every eligible item. Before running, say how many will fail and why ("3 of 20 can't be archived: already closed"), then Continue / Cancel. If unknown in advance, report per-item results after. (Fiori)
- Batch over a known count: show "Updating 3 of 50". (NN/g)
- Bulk delete friction per `patterns/actions-and-dialogs.md` and `foundations/defaults.md`; easy-to-undo bulk actions need no confirmation. (Pajamas)
- Checkbox names are row-specific ("Select Invoice 1042"). (WCAG 4.1.2; general practice)

## 8. Row actions

- ≤2 frequent actions inline (text or labelled icon buttons); the rest in an overflow menu. (Carbon, Fiori, Cloudscape, NN/g) **[consensus]**
- Put row actions in the **last column and make it sticky** so they stay reachable on wide tables. (Cloudscape)
- Overflow trigger visible at rest, never hover-only (always visible on touch); label it per row ("Actions for Invoice 1042"). (Carbon, NN/g)
- Row overflow menus hold ≤7 items. (Cloudscape) Don't mix global and row actions in one menu. (NN/g)
- Hide row actions that don't apply to that row instead of disabling them. (Fiori)
- Table-wide actions (Create, Export, settings) go in the toolbar above the table — ≤5 visible, rest in overflow. Filters do not go in the table toolbar. (Carbon, Fiori)
- Separate destructive icons from frequent ones to prevent mis-clicks on dense rows. (Fitts's law)
- Show a chevron on rows that drill into details only if the user can open them. (Fiori)

## 9. Inline edit vs side panel vs page

| Edit scope | Use | Source |
|---|---|---|
| One frequently changing value, or one property across many rows | Inline edit | (Cloudscape, Lightning) |
| Several fields while the user still needs neighbouring rows | **Non-modal side panel / drawer** | (NN/g, Ant) |
| Short, focused add with ≤8 fields | Dialog | (Fiori) |
| Complex, shareable or many-field record | Full page | (Ant, Fiori) |
| Rapid switching between items | Two-pane master-detail | (Ant) |

- Don't use a modal for deep row edits — it hides the rows users refer to. (NN/g)
- Inline edit: pencil affordance in header and on hover; enter via click/double-click or pencil; explicit ✓ confirm / ✕ cancel; keep column widths stable; edit mode visibly different. (Cloudscape, Lightning, Ant, NN/g)
- After an inline save: show a success icon in the cell, no toast. On failure, stay in edit mode with the error on the cell. (Lightning, Cloudscape)
- Keep display, edit and create layouts identical so nothing shifts. (Fiori)

## 10. Expandable rows

- Use for supplementary or slow-to-fetch detail under one screen tall; if it feels cramped, move it to a side panel or page. (Carbon, Ant)
- Expand-all off by default; accordions in tables get left open and clutter — use sparingly. (Carbon, NN/g)
- Spinners (not skeletons) are fine while an expanded row loads. (Cloudscape)
- The expand control is a `<button aria-expanded>`. (ARIA APG disclosure)

## 11. Adding rows

- Rank: inline add for simple tables → dialog for ≤8 fields → separate page. (Fiori)
- New rows appear at the top, briefly highlighted. (Fiori, Ant)
- "Create" makes a new record; "Add" attaches an existing one. Don't swap them. (Fiori)
- After a dialog add, return focus to the new row's first cell. (ARIA APG dialog)

## 12. Refresh and last updated

- One manual Refresh button in the table header — not scattered around the page. Keep current data visible and usable while refreshing; show "Last updated …" afterwards; announce it via a polite live region. (Cloudscape)
- Auto-refresh only for near-real-time views (e.g. every 10s), with a way to pause (WCAG 2.2.2). (Cloudscape, WCAG)
- Highlight newly arrived rows for a few seconds, or offer click-to-load new items, instead of shifting rows under the cursor. (Ant)
- Initial load: skeleton rows matching columns, not a spinner. (see `foundations/defaults.md`) (Cloudscape, Lightning) Never show "No data" while loading or after a load failure — see `patterns/feedback-and-states.md`.

## 13. Export

- Offer export where users take data to Excel/BI tools; don't force screenshots or re-keying. (NN/g)
- State the scope in the control: "Export 1,240 filtered rows" vs "Export selected (12)". (general practice)
- Exports use absolute timestamps with time zone and ISO 8601 dates. (see `foundations/defaults.md`)
- Long exports run in the background with progress and a completion notification. (NN/g, Carbon; general practice) — see `saas/integrations-and-data.md`.

## 14. Persist user preferences

- Persist per user: page size, visible columns, column order, sticky columns, density, table vs card view, last sort. (Cloudscape, Fiori, NN/g)
- Filter/sort state belongs in the URL — see `patterns/filters-and-search.md`.
- Saved views bundle filters + columns + sort — one page-level variant control, not per table. (Fiori)
- Defaults must work without customization; most users never change them. (NN/g)

## 15. Accessibility essentials

- **Native `<table>` by default** — with `<caption>`, `<th scope="col">`, and the identifier as `<th scope="row">` — even with sorting, links and checkboxes. Use `role="grid"` only for spreadsheet-like editable data where arrow-key cell navigation is expected. (ARIA APG, Roselli) Full rules: `foundations/accessibility.md`.
- Sortable header = `<button>` inside `<th>`; `aria-sort` only on the sorted column; arrows `aria-hidden`. (ARIA APG sortable table)
- Wide tables scroll inside a labelled, focusable container; the page itself still reflows at 320px. (WCAG 1.4.10)
- Announce result counts, page changes and refresh completion via `role="status"`. (WCAG 4.1.3, Primer)
- Sticky headers/action columns must not fully cover the focused cell. (WCAG 2.4.11)
- Column reorder/resize needs a non-drag alternative (menu or buttons). (WCAG 2.5.7)
- Row action targets ≥24×24px. (WCAG 2.5.8)

## Common AI failures

- Auto-generated ID as the first column, or no link from the identifier to the record.
- Numbers and currency left-aligned; units repeated in every cell when they're uniform (or missing entirely).
- Five icon-only row actions, revealed only on hover, with no accessible names.
- Header checkbox silently selects all 10,000 rows, or selection silently survives a filter change.
- Blank cells for missing values; "0" and "—" used interchangeably.
- Spinner over an empty table on load, then "No data" when the request actually failed.
- Truncated column headers with no tooltip; status shown only as a coloured dot.
- Client-side sort/filter applied to only the current page of server data.
- `role="grid"` on a read-only table (breaks screen-reader table navigation).
- Toast after every inline edit; modal for editing a row that hides the rows users compare against.

## Sources

- https://carbondesignsystem.com/components/data-table/usage/
- https://www.sap.com/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/usage
- https://www.sap.com/design-system/fiori-design-web/v1-84/page-types/floorplans/list-report-floorplan-sap-fiori-element/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://www.sap.com/design-system/fiori-design-web/v1-139/foundations/visual/cozy-compact
- https://spring-21.lightningdesignsystem.com/guidelines/displaying-data
- https://spring-21.lightningdesignsystem.com/guidelines/data-entry
- https://developer.salesforce.com/blogs/2018/08/new-density-settings-for-the-lightning-experience-ui-in-winter-19
- https://cloudscape.design/patterns/resource-management/view/table-view/
- https://cloudscape.design/patterns/resource-management/edit/inline-edit/
- https://cloudscape.design/patterns/general/actions/global-actions/
- https://cloudscape.design/patterns/general/actions/incontext-actions/
- https://cloudscape.design/patterns/general/loading-and-refreshing/
- https://cloudscape.design/patterns/general/empty-states/
- https://cloudscape.design/patterns/resource-management/details/details-page/
- https://cloudscape.design/patterns/resource-management/create/single-page-create/
- https://www.patternfly.org/patterns/bulk-selection/
- https://www.patternfly.org/content-design/grammar/truncation
- https://design.gitlab.com/patterns/loading/
- https://design.gitlab.com/patterns/destructive-actions/
- https://shopify.dev/docs/api/app-home/patterns/templates/resource-index.md
- https://nngroup.com/articles/data-tables
- https://www.nngroup.com/articles/contextual-menus-guidelines/
- https://www.nngroup.com/articles/complex-application-design/
- https://www.nngroup.com/articles/flexibility-efficiency-heuristic/
- https://www.nngroup.com/articles/progress-indicators/
- https://ant.design/docs/spec/data-list
- https://ant.design/docs/spec/data-format
- https://5x.ant.design/docs/spec/data-display
- https://5x.ant.design/docs/spec/direct
- https://5x.ant.design/docs/spec/lightweight
- https://5x.ant.design/docs/spec/reaction
- https://w3c.github.io/wai-website/ARIA/apg/patterns/grid/
- https://www.w3.org/WAI/ARIA/apg/example-index/table/sortable-table.html
- https://www.w3.org/TR/2021/NOTE-wai-aria-practices-1.2-20211129
- https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html
- https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum
