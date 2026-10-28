# Dashboards and data visualization

**Load when:** planning or auditing a dashboard, overview page, KPI tiles, or any chart; choosing chart types, colours, interactions, or how to show data freshness and per-widget states.

For chart colour formulas and mark specs, also load the `dataviz` skill if available. Accessibility detail: `foundations/accessibility.md`.

## 1. Purpose
- A dashboard is an **at-a-glance view on one screen so users can act fast** — not an exploration tool or a portal to many tools. (NN/g)
- Decide the type first: **operational** (live, time-sensitive, monitoring) or **analytical** (trends, comparison). Don't blend both on one page. (NN/g)
- **Static vs configurable — never mix on one dashboard.** Static when order of importance is critical (monitoring); configurable when users choose what to see (troubleshooting). (Cloudscape)
- Dashboards are for analysis/monitoring. Action-heavy lists, boards, long logs, resource creation and advanced queries belong on normal pages. (Pajamas, Cloudscape)
- Keep the metric count low; remove anything that doesn't serve a decision. (Carbon, NN/g)
- Must still make sense as a screenshot or screen share. (Pajamas)
- Make the dashboard the first nav link / landing page for returning users when it's the main entry. (Cloudscape)

## 2. Start with the questions
Before any layout, write:
1. Who looks at it, how often, and what decision follows. (NN/g strategies; general practice)
2. The 3–5 questions it must answer ("Are we within SLA right now?", "Which accounts are at risk?"). (general practice)
3. For each question: metric, unit, time window, comparison baseline, threshold that triggers action, and where the user goes next (drill-down). (Lightning, general practice)
4. Data source and refresh cadence for each metric. (Lightning)
- Use HEART/Goals-Signals-Metrics to pick product metrics; don't track everything by default. See `foundations/ux-laws-and-heuristics.md`. (Google HEART)
- Every widget serves one goal with one primary action. (Cloudscape)

## 3. Layout
- **KPIs at the top**, most important with the most contrast and area; follow F-pattern scanning (top-left most important). (Carbon)
- Summary on top, detail lower down; show trends over time, not only snapshots. (Pajamas)
- If users must act, include one actionable list (top N items needing attention) linking to the full page — not a long table on the dashboard. (Cloudscape, Pajamas; general practice)
- Bring compared numbers physically close together. (NN/g)
- **12-column grid**; collapse to 1 column at medium width / small screens. (Pajamas, Cloudscape)
- Widget widths (static layout): **S 3/12, M 6/12, L 9/12, XL 12/12.** (Cloudscape)
- One visualization per panel (Pajamas); max 2 visualization types per item (Cloudscape). House default: one.
- Identical layout, spacing and legend position across charts. (Carbon)
- Widget actions: one primary; others in an icon dropdown ordered Preferences → others → Remove; optional "View all" link. (Cloudscape)
- Configurable dashboards: add/remove/move/resize widgets with a non-drag alternative (Move/Resize menu). (WCAG 2.5.7)

## 4. KPI tiles
| Rule | Source |
|---|---|
| Always show the unit | Lightning |
| User-facing label, not backend field name | Lightning |
| State the comparison baseline ("vs previous 7 days"); show change as absolute, %, or both | Lightning |
| Show when the value was **measured**, not when it was received | Lightning |
| Direction via ↑ ↓ → icon + text; better/worse via icon or text, **never colour alone** | Lightning, WCAG 1.4.1 |
| Drop the trend arrow if a sparkline already shows direction | Lightning |
| **All tiles share the same time window** | Lightning |
| **Don't mix data sources** on one dashboard | Lightning |
| Don't mix measurement systems | Carbon |
| No decorative icons next to KPI numbers | NN/g |
| Tile drills down to the underlying list/report; aggregated numbers link to the breakdown | Fiori |
| Large numbers abbreviated (1.2M) with exact value on hover/focus | Ant, NN/g |
| Unknown/failed value: "—" or unavailable state, never 0 | Primer, see foundations/defaults.md |

## 5. Chart choice
Encode quantities with **length and 2-D position** (bars, lines, scatter). Angle and area read poorly. **[consensus]** (NN/g, Lightning)

| Question | Chart | Rules |
|---|---|---|
| Compare categories | Bar (horizontal for long labels) | Start at 0; sort by value unless order is inherent (Lightning) |
| Change over time | Line | ≤4 series; more → small multiples or filter (Lightning) |
| Progress to target | Bullet chart | Use instead of radial gauges (NN/g) |
| Part-to-whole | Stacked bar or 100% bar | Prefer to pie (NN/g) |
| Part-to-whole, if pie insisted | Pie | 2–5 slices, largest first, clockwise from 12 o'clock; only for big disparities (Lightning, NN/g) |
| Correlation | Scatter | Label axes with units (general practice) |
| Distribution | Histogram / box plot | (general practice) |
| Single current value | KPI tile (+ sparkline) | Section 4 |
| Overview of a large data set | Chart, not table (Fiori) | Table for exact lookup |
| Exact values / lookup | Table | `patterns/tables.md` |

**Avoid:** pie/donut (except huge disparities), gauges, 3D anything, treemaps on simple dashboards. (NN/g)

### Colour
- **≤5–6 colours** per chart (Lightning ≤5). Categories → distinct hues; continuous values → one-hue gradient. (Lightning)
- Colour encodes category, never magnitude alone, and reinforces other cues; ~8% of men are colour-blind. (NN/g)
- **Same colour per series across every chart** on the dashboard. **[consensus]** (Carbon, Lightning)
- No decorative colour. Pair colour with direct labels, markers or patterns. (Lightning, WCAG 1.4.1)
- Use a colour-safe palette that meets contrast. (Lightning)

## 6. Interaction
- Keep interaction minimal. (NN/g)
- **Hover/focus shows exact values in place** rather than navigating away. (NN/g)
- Exploration views: **linked charts** — filtering or zooming one updates related ones. (Carbon, Fiori analytical list page)
- Dashboard-level filters (date range, scope) at the top; panel filters may narrow but **never override the dashboard date range**; a fixed-range panel states its range under its title. (Pajamas)
- **Export and copy:** CSV/Excel for data, copy/download chart as image; don't force screenshots. (NN/g)
- Let users annotate charts/data to resume later. (NN/g)
- Compact chart popovers open on click, not hover alone. (Lightning)
- Tooltips: dismissible with Esc, hoverable, persistent; keyboard reachable. (WCAG 1.4.13, 2.1.1)
- Annotations never hide data. (Carbon)
- Legend toggles are real buttons with `aria-pressed`. (general practice)

## 7. Data honesty
- **Freshness:** "Updated 3 min ago" per dashboard (or per widget if sources differ), absolute time on hover; manual refresh in the header; auto-refresh announced politely. (Cloudscape, Lightning)
- **Partial periods:** mark the current incomplete period ("Oct 1–27, partial") — dashed line or label, never compared as if complete. (general practice)
- **Definitions:** each metric has an info popover with definition, formula, source, filters applied. (general practice; Lightning user-facing labels)
- **Baselines** stated on every comparison; same window across tiles. (Lightning)
- Bars start at 0; don't truncate axes to exaggerate change. (Lightning)
- Mark AI-generated insights/summaries as AI with sources. See `saas/ai-features.md`. (Carbon AI label)
- **Per-widget states:** each widget has its own loading, empty ("No incidents in the last 24 hours"), error (section-level, with Retry) and no-permission state; one widget failing never blanks the dashboard. (Cloudscape, Primer) — `patterns/feedback-and-states.md`.
- Unknown counts hidden or "—", never 0. (Primer)

## 8. Progressive loading
- Load structure + text skeletons first, then charts, below-the-fold widgets, then interactivity. (Carbon)
- Skeleton per widget (Pajamas default: 3 cards); clear page skeleton once the first card renders. (Pajamas, Fiori)
- Widgets render as their data arrives, most important first; reserve their size to avoid layout shift (CLS ≤0.1). (Primer, web.dev)
- Slow queries (>10s): show progress in the widget, keep the rest usable. (NN/g, Cloudscape)

## 9. Accessible charts
- **Text alternative for every chart:** short name + key takeaway, plus access to the data via a visible "View as table" toggle or long description. (WCAG 1.1.1; W3C complex-images tutorial (verify — as of Oct 2026))
- **Non-text contrast ≥3:1** for lines, bars, points and legend keys needed to read the chart. (WCAG 1.4.11)
- **Not colour alone:** direct labels, shapes, patterns, markers. (WCAG 1.4.1)
- Metric time series reachable by keyboard and labelled for AT. (Lightning)
- Charts respect `prefers-reduced-motion`; auto-updating charts can be paused. (WCAG 2.2.2)
- Forced-colors mode: series still distinguishable (patterns/markers); use `forced-color-adjust: none` only with system colours supplied. (general practice)
- Full rules: `foundations/accessibility.md`.

## Common AI failures
- Dashboards that are a wall of 12 equal tiles with no hierarchy or question behind them.
- KPI tiles with no unit, no baseline, no timestamp, and red/green as the only signal.
- Mixed time windows across tiles ("Today" next to "Last 30 days") without labels.
- Donuts, gauges and 3D charts for everything; pie with 9 slices.
- Line charts with 8+ series and a different colour for the same series on each chart.
- Bar charts with truncated y-axes or unsorted bars.
- Long action tables and create forms embedded in the dashboard.
- One failing query blanks the whole dashboard; failed values shown as 0.
- No "View as table", no text summary, hover-only values.
- Decorative gradients, icons and colours that carry no meaning.

## Sources
- https://www.nngroup.com/articles/dashboards-preattentive/
- https://www.nngroup.com/articles/complex-application-design/
- https://www.nngroup.com/articles/strategies-complex-application-design/
- https://nngroup.com/articles/data-tables
- https://www.nngroup.com/articles/progress-indicators/
- https://carbondesignsystem.com/data-visualization/dashboards
- https://carbondesignsystem.com/patterns/loading-pattern
- https://carbondesignsystem.com/components/ai-label/usage/
- https://spring-21.lightningdesignsystem.com/guidelines/data-visualization/charts
- https://spring-21.lightningdesignsystem.com/guidelines/data-visualization/metric-display
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/usage
- https://www.sap.com/design-system/fiori-design-web/v1-145/ui-elements/placeholder-loading/usage
- https://cloudscape.design/patterns/general/service-dashboard/
- https://cloudscape.design/patterns/general/service-dashboard/dashboard-items/
- https://cloudscape.design/patterns/general/loading-and-refreshing/
- https://design.gitlab.com/patterns/dashboards
- https://primer.style/ui-patterns/degraded-experiences
- https://primer.style/product/ui-patterns/loading
- https://ant.design/docs/spec/data-format
- https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/
- https://web.dev/articles/defining-core-web-vitals-thresholds
- https://www.w3.org/TR/WCAG22
