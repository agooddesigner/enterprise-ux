# Filters and search

**Load when:** designing, critiquing or auditing search boxes, filter bars, faceted filters, query builders, applied-filter chips, saved views, zero-result states or result counts on any collection view.

If the product already has a design system, its rules win. Otherwise apply these and `foundations/defaults.md`. Table mechanics live in `patterns/tables.md`; global search and ⌘K live in `saas/integrations-and-data.md`.

## 1. Search vs filter

- **Search** finds a specific known item by keyword across attributes. **Filter** narrows a set by parameters. Pick by whether users know exactly what they want. (Pajamas, Ant)
- Most enterprise list pages need both: one in-context search box plus filters. Frequent queries deserve the most efficient control. (Ant)
- Three query modes: *inquire* (several conditions submitted together), *filter* (live update), *search* (one keyword box). (Ant)
- Filters apply to the **whole collection**, never only the loaded/visible page. (Cloudscape) **[consensus]** with server-side sort in `patterns/tables.md`.

## 2. Choose the filter UI by complexity

Escalate only as far as the data needs. (Pajamas, Cloudscape, PatternFly, Lightning) **[consensus]** on staged escalation.

| Need | Control | Source |
|---|---|---|
| Few properties, user knows the exact term | Text filter / in-context search | (Cloudscape) |
| Search + ordering | Search + sort control (sort right-aligned) | (Pajamas) |
| A few fixed views of the same data | Tabs (with counts) or segmented button ≤3 views; select for more | (Pajamas, Fiori) |
| 1–2 properties, one value each, always AND | Collection select / filter dropdowns (3–5 max inline) | (Cloudscape, Pajamas) |
| Many properties, multiple values per property, mixed operators | Property filter / full filter component (token-based) | (Cloudscape, Pajamas) |
| Attributes with different selection types | Attribute-value filter (pick attribute, then value) | (PatternFly) |
| Users browse by facet counts | Faceted filters (sidebar when many) | (PatternFly, Ant) |
| Users write their own rules with changeable AND/OR | Expression/logic builder | (Lightning) |

- More than 3–5 inline dropdowns → switch to the filter component. (Pajamas)
- Layout: search left, filter dropdowns after it, sort right-aligned; filters above the list, general → specific. (Pajamas, Ant)
- Many conditions → filter sidebar. (Ant)
- Mobile: filters behind a "Filters" button with a count badge. (Pajamas)
- Single-select filters include an "All [items]" reset option. (PatternFly)
- Filters live in the filter bar, never in the table toolbar. (Fiori)
- Mandatory filters always have defaults. (Fiori)
- Placeholders: "Filter by [attribute]" for one column, "Filter" for all. (PatternFly)

## 3. AND / OR semantics

- Default logic: all conditions met (AND). (Lightning)
- **Across** different attributes/facets: AND. **Within** one attribute (multi-select values): OR. (PatternFly) **[consensus]**
- Collection selects are always AND; show operators (AND / OR / AND NOT / OR NOT) only when 2+ filter tokens exist. (Cloudscape)
- Hide the logic toggle when logic can't change; show it only in a builder where users control it. (Lightning)
- Make the logic visible in the applied-filter summary when it isn't the default (e.g. "Status: Open **or** Blocked"). (general practice)

## 4. Applied filters, chips and Clear all

- **Always show an applied-filters summary** above results — never only a count like "Filters (3)". (Baymard #488 "Essential", NN/g)
- Each chip removable with its own ×; "Clear all" / "Clear filters" sits after the last chip. (Baymard, PatternFly)
- Include the attribute name in the chip when the value is ambiguous ("Owner: Me", "Region: EU"); apply consistently. (Baymard)
- Show chips whenever the current value isn't visible on the control itself. (PatternFly)
- Chips wrapping onto many rows on desktop: show the first row, collapse the rest behind a "Show all (n)" toggle. (Baymard)
- Collapsed filter bar summary: "Filtered by (n): value, value, … " (≤5 values, then ellipsis); "Not filtered" when none. (Fiori)
- Clear buttons are real `<button>`s labelled "Clear" and return focus to the input. (Pajamas)

## 5. Live update vs Apply

- **Live update** for cheap/local data; explicit **Apply/Go** only when queries are expensive or fields are interdependent. (see `foundations/defaults.md`) (Fiori, Lightning, Carbon, Cloudscape)
- Active (as-you-type) search only for small data sets; no Go button, has a clear (×). For slow/expensive search, submit on Enter. (Carbon, PatternFly)
- Never mix live and Apply in one filter bar. (general practice)
- While results reload: keep previous results visible and mark them busy (`aria-busy`), dim rows that no longer match; don't blank the table. (Fiori, Primer)
- Keep keyboard focus where it was after results reload. (Carbon)

## 6. Debounce values

| Work | Debounce | Source |
|---|---|---|
| Cheap, live results (local search, type-ahead) | ~250ms | (Pajamas) |
| Expensive queries or validation | ~500ms | (Pajamas) |
| Anything slower than ~1s | Submit-on-Enter or Apply instead of live | (Carbon, NN/g) |

- Show a loading indicator only when the response exceeds ~300ms–1s (thresholds in `foundations/defaults.md`).

## 7. URL is the source of truth

- Write filter, search, sort, page and (optionally) page size and visible columns to the URL on every change; read it on load. (see `foundations/defaults.md`) (Cloudscape)
- Validate URL values on load; silently drop invalid ones and show the valid remainder. (Cloudscape)
- Never put sensitive data in the URL. (Cloudscape)
- Don't persist to the URL when multiple tables on a page make ownership ambiguous; use saved views instead. (Cloudscape)
- Back/Forward must restore prior filter states. (general practice; Primer requires nav state in URL)

## 8. Saved views (variants)

- One **page-level** saved-view control covering filters, tabs, sort, columns and charts; avoid a separate table-level variant. (Fiori)
- Users save, rename, set default and share views; mark the active view and show "modified" when the current state differs from the saved one. (Fiori; general practice for the modified marker)
- Remember the last-used view/sort across sessions. (NN/g)
- Ship good default views per role; most users never customise. (NN/g)

## 9. Search types and fields

| Type | Behaviour | Use for | Source |
|---|---|---|---|
| Basic | Runs on submit, goes to a results page | Global search | (Carbon) |
| Active | Filters as you type, no Go, × to clear | Small, local data sets | (Carbon) |
| Focused / scoped | Searches the current scope, can widen | In-app sections | (Carbon) |

- **In-context search** sits directly above the content it filters, stays visible (never hidden behind an icon), is visually smaller than global search, and its placeholder **names the scope** ("Search invoices", not "Search…"). (Lightning)
- Search fields may omit a visible label if they have a search icon, a scope-specific placeholder and an accessible name. This is the only exception to "no placeholder as label". (Carbon)
- Scoped search: scope dropdown defaults to "All" and shows a count per scope. (Carbon)
- On focus show recent/trending searches; replace with type-ahead suggestions once typing starts; group live suggestions by category when categories are few. (Carbon, Ant)
- Highlight matched terms in results. (Lightning)
- Accept liberal input (case, spacing, punctuation in IDs) and normalise it. (Postel's law, GOV.UK)

## 10. Result counts

- Always show the result count, including 0 ("128 results", "0 results"). (Carbon)
- Announce counts via `role="status"` after each change ("5 items match"). (Primer, WCAG 4.1.3)
- Tabs used as filters show item counts. (Fiori)
- Count the whole matching set, not the loaded page. (Cloudscape, Fiori)

## 11. Zero results

- Heading "No matches" / "No results for '[term]'" + one-line hint + **"Clear filters" secondary button**. (see `foundations/defaults.md`) (Cloudscape, PatternFly) Alt: Pajamas uses fixed text with no CTA.
- Zero results is not the first-use empty state: keep the filter bar and chips visible so users can edit them. (Cloudscape, Carbon, PatternFly)
- Before any filter is set on a filter-first page: "To start, set the relevant filters." (Fiori)
- Never show "No results" while still loading, or when the query failed — show the error instead. (NN/g, Primer) See `patterns/feedback-and-states.md`.

## 12. Edited items that no longer match the filter

- **House default: keep the edited item visible**, marked as no longer matching, until the user refreshes, re-filters or changes page. (Cloudscape, Fiori continuous mode)
- Alt — **worklist / queue** (process-and-remove, ~80% of Fiori cases): remove the item immediately and confirm with a toast so the queue visibly shrinks. (Fiori)
- Choose worklist removal only when "done" means "leaves the queue"; otherwise items vanishing after an edit look like data loss. (Fiori; general practice)

## 13. Date filters

- Offer presets for common ranges (e.g. Today, Last 7 days, Last 30 days, This month, Custom range) above a range picker. (general practice)
- Always state the time zone used for date filters; show absolute dates in the chip ("Created: 1–31 Oct 2026"). (see `foundations/defaults.md`; Pajamas)
- Panel-level date filters never silently override a page/dashboard date range. (Pajamas)

## 14. Type-ahead and value pickers

- Selects with **>10 options get type-ahead** (combobox). (PatternFly)
- Short lists: plain select rather than a value-help dialog. (Fiori)
- Combobox keyboard and ARIA: DOM focus stays in the input, options via `aria-activedescendant`, Esc closes. (ARIA APG combobox) Details in `foundations/accessibility.md`.

## 15. Faceted filters keyboard

- Tab moves between facet groups, arrow keys between facets, Enter/Space toggles; focus stays put after results reload. (Carbon)

## 16. Global search and command palette

- Global search is basic (submit) search across object types with scoped results. ⌘K palettes, fuzzy matching, aliases and recent items: see `saas/integrations-and-data.md`. (Carbon, Superhuman)

## Common AI failures

- Generic "Search…" placeholder with no scope, or the in-context search hidden behind an icon.
- "Filters (3)" badge with no visible chips; no per-chip × and no Clear all.
- Filters or search applied only to the current client-side page of server data.
- Filter state lost on reload/Back because it isn't in the URL.
- Live per-keystroke queries against an expensive backend with no debounce; or an Apply button on a tiny local list.
- Results area blanks to a spinner on each keystroke, and focus jumps.
- Zero-results state replaces the filter bar, so users can't undo what caused it; or shows "No results" when the request failed.
- Ambiguous OR/AND: multiple values in one facet silently ANDed.
- Edited row disappears instantly from a non-queue list, looking like it was deleted.
- Date filter with no time zone, or relative presets with no absolute dates shown.

## Sources

- https://cloudscape.design/patterns/general/filter-patterns/
- https://cloudscape.design/patterns/general/filter-patterns/filter-persistence-in-collection-views/
- https://cloudscape.design/patterns/resource-management/edit/inline-edit/
- https://cloudscape.design/patterns/general/empty-states/
- https://design.gitlab.com/patterns/filtering/
- https://design.gitlab.com/patterns/saving-and-feedback/
- https://design.gitlab.com/patterns/dashboards
- https://design.gitlab.com/content/date-and-time/
- https://v5-archive.patternfly.org/patterns/filters/design-guidelines
- https://www.patternfly.org/components/empty-state/design-guidelines
- https://primer.style/product/ui-patterns/loading
- https://primer.style/product/ui-patterns/navigation
- https://www.sap.com/design-system/fiori-design-web/v1-84/page-types/floorplans/list-report-floorplan-sap-fiori-element/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/work-list/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/usage
- https://carbondesignsystem.com/patterns/search-pattern
- https://spring-21.lightningdesignsystem.com/guidelines/search/in-context
- https://spring-21.lightningdesignsystem.com/guidelines/rules-filters-logic
- https://baymard.com/blog/how-to-design-applied-filters
- https://baymard.com/guidelines/488-applied-filters-on-desktop
- https://nngroup.com/articles/data-tables
- https://www.nngroup.com/articles/flexibility-efficiency-heuristic/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://ant.design/docs/spec/data-list
- https://ant.design/docs/spec/research-list
- https://5x.ant.design/docs/spec/reaction
- https://w3c.github.io/wai-website/ARIA/apg/patterns/combobox/
- https://w3c.github.io/wcag/understanding/status-messages
- https://blog.superhuman.com/how-to-build-a-remarkable-command-palette/
