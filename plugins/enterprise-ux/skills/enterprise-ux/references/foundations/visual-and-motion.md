# Visual design and motion

**Load when:** setting density, spacing, layout widths, type, colour, hierarchy, icons or animation for an enterprise UI; auditing visual consistency; or deciding how fast something must respond.

Enterprise visuals serve scanning and repeated use, not first impressions. If the product has a design system, its tokens win; these are the defaults otherwise.

---

## 1. Density

| Rule | Source |
|---|---|
| Density is **app-wide and user-chosen**; never mix densities on one page or within one hierarchy **[consensus]** | Fiori, Lightning, Carbon |
| Set density explicitly; don't rely on component defaults | Fiori |
| Default table row 40px; user-switchable compact 32px; touch 44px+ (see `foundations/defaults.md`) | Carbon, Fiori |
| Default by device: desktop → compact; phones/tablets → cozy (forced); hybrid → cozy with user choice | Fiori |
| Fiori compact = 2rem (32px) rows/toolbars for mouse+keyboard; cozy = 2.75rem (44px) targets for touch; **font size is the same in both** — only spacing changes | Fiori |
| Lightning Compact vs Comfy: card padding 1rem → 0.5rem vertical / 0.75rem horizontal; titles 1rem → 0.875rem; line-height 1.5 → ~1.3; medium spacing token 16px → 8px; left labels only in wide regions. Net ~20% more vertical density (~30% with left labels) | Lightning |
| Material density scale −4…+4, ~4px per step, 0 = default, negative = denser | Material |
| Carbon row scale xs 24 / sm 32 / md 40 / lg 48 / xl 64 (xl only for 2-line rows); toolbars and pagination match row height | Carbon |
| Density is justified by observed expert use, not assumed | GOV.UK, NN/g |
| Compact never drops a target below 24×24px (WCAG 2.5.8) | WCAG, `foundations/accessibility.md` |

## 2. Spacing

- **8px base unit; 4px half-step for tight internals** (icon–label gaps, chip padding, dense tables) (Ant, Pajamas; 4px half-step general practice).
- Ant hierarchy steps: **8 small / 16 middle / 24 large** (8 + 8n); use larger spacing between less-related groups (Ant).
- Spacing communicates grouping: tighter within a group, looser between groups (L-Proximity, `foundations/ux-laws-and-heuristics.md`). Never equal spacing everywhere (Laws of UX).
- Input widths on a base-8 scale, sized to expected value: XS 80, S 160, M 240, L 320, XL 560px max (Pajamas, Primer).
- Avoid nested containers for grouping; use spacing and one level of region (L-CommonRegion).

## 3. Layout widths and window size classes

| Class | Width | Enterprise implication |
|---|---|---|
| Compact | <600dp | Phone: single column, responsive lists not grids (Fiori) |
| Medium | 600–839dp | Tablet portrait: collapse side nav |
| Expanded | 840–1199dp | Most laptops in split view; side nav + content |
| Large | 1200–1599dp | Typical desktop; full tables, detail side panels |
| Extra-large | ≥1600dp | Wide monitors; multi-pane, but cap text measure |

(Material) Enterprise web apps mostly live in Expanded and up (Material) — but still reflow at 320 CSS px (WCAG 1.4.10, `foundations/accessibility.md`).
- 12-column grid collapsing to 1 column at medium width (Pajamas); dashboard item widths 3/6/9/12 of 12 (Cloudscape).
- Form columns by width: 4 at XL, 3 at L, 2 at M, 1 at S on object pages (Fiori); otherwise single-column forms (Primer, Pajamas). Table column counts: ~8 at full desktop, 3–5 in split view, 1–2 on phone (Fiori).
- Modal widths and page vs drawer choices: `patterns/actions-and-dialogs.md`; shell layout: `patterns/navigation-and-layout.md`.

## 4. Typography

- **Carbon productive vs expressive:** productive = compact, fixed headings, for task UI (forms, tables, controls). Expressive = larger, fluid headings, for reading and marketing-style pages. One set per component or region; an expressive moment (home banner) is allowed but **never inside cards or tables** (Carbon).
- Default to the productive set for everything inside the app (Carbon).
- Readable measure for paragraphs: ~45–75 characters per line (general practice); empty-state lines under ~66 characters (Lightning); modal body ~80% of modal width (Carbon).
- Minimum body text in data UI ~14px; don't shrink type for density — tighten spacing instead (Fiori keeps font size across densities; 14px floor general practice).
- Line height ~1.5 for comfortable reading, ~1.3 in compact (Lightning). Layout must survive user text-spacing overrides (WCAG 1.4.12).
- Tabular/monospaced numerals in tables so digits align when right-aligned (general practice); right-align numbers and dates (Fiori, Polaris, Ant).
- Never all caps for labels or tabs (NN/g); sentence case (`foundations/writing.md`).

## 5. Colour

- **Colour carries meaning, not decoration.** No decorative colour in charts or KPIs (Lightning, NN/g).
- **Never colour alone** — pair every status colour with an icon and/or text (WCAG 1.4.1; Carbon, Atlassian, Lightning, Polaris, PatternFly) **[consensus]**. Colour meanings also vary by culture (Spectrum).
- **Small, consistent status vocabulary**, one meaning per colour app-wide:

| Status | Colour | Pair with |
|---|---|---|
| Error / critical / failed | Red | Error icon + text. Red **only** for errors (GOV.UK task list) |
| Warning / at risk | Yellow/amber | Warning icon + text |
| Success / healthy | Green | Check icon + text |
| Info / in progress | Blue | Info or spinner icon + text |
| Neutral / inactive / draft | Grey | Text |

(Carbon, Primer, Cloudscape, PatternFly; mapping general practice.) Status columns sort by severity (Fiori).
- One colour per data series, kept identical across every chart in a dashboard (Carbon, Lightning) **[consensus]**; ≤5 colours; distinct hues for categories, one-hue gradient for continuous values (Lightning). Colour encodes category, never magnitude (NN/g).
- Contrast: text 4.5:1, large text 3:1, UI parts and chart marks 3:1, no rounding up — `foundations/accessibility.md`. Check every token pair, including themes (Carbon).
- Danger-red buttons only for serious irreversible actions, behind a confirmation step (GOV.UK, Polaris, Carbon).

## 6. Hierarchy

- **One primary action per view or container**; Cancel is never primary (all systems, `foundations/defaults.md`). The single standout is what users notice (L-VonRestorff).
- Build hierarchy with **weight and position before size**: bold, placement, whitespace first; larger type only for page titles (general practice; Carbon productive type keeps headings fixed).
- Most important KPIs top-left with most contrast and area (F-pattern) (Carbon). Remove non-essentials to create salience instead of adding more colour or bold (NN/g CA8).
- Emphasise one or two things per screen; highlight anomalies in tables, not every row (Laws of UX).
- Clickable must look clickable; static text must not look like a button (L-Similarity, N-Signifier).

## 7. Icons

- Primer sizes: 12px filled; 16px or 24px outline, paired with ≥14px text (Primer).
- **Icon-only buttons need an accessible name AND a visible tooltip** (Ant, WCAG 1.1.1, 2.5.3) **[consensus]**. Prefer text labels for anything not universally recognised (general practice).
- Fiori object-page actions use text **or** icon, never both (Fiori). Elsewhere, icon + text is fine for primary nav.
- No decorative icons beside KPI numbers (NN/g). Empty-state illustrations: decorative (`alt=""`), never in small containers (Carbon, Lightning, Fiori).
- Simple, unambiguous shapes (L-Pragnanz). Icons must meet 3:1 non-text contrast (WCAG 1.4.11). SVGs use `currentColor` for forced-colour mode (see `foundations/accessibility.md`).
- No text inside icons; culture-specific metaphors (✓/✗, mailbox, hand gestures) — see `saas/global-and-performance.md` (Spectrum).

## 8. Motion

**Purpose:** show cause, continuity and state change. Never decoration in work tools (Ant "use transition"; general practice).

| Token family | Values | Use |
|---|---|---|
| Short | 50 / 100 / 150 / 200ms | Hovers, toggles, small state changes, fades |
| Medium | 250 / 300 / 350 / 400ms | Panels, drawers, shared-axis transitions (300ms) |
| Long | 450–600ms | Large-area transitions (rare in enterprise) |
| Extra-long | 700–1000ms | Avoid in work UI |

(Material) Larger distance or area → longer duration (Material).

| Easing | Curve | Use |
|---|---|---|
| Standard | cubic-bezier(0.2, 0, 0, 1) | Default for utility UI (enterprise) |
| Standard decelerate | (0, 0, 0, 1) | Elements **entering** |
| Standard accelerate | (0.3, 0, 1, 1) | Elements **exiting** |
| Emphasized decelerate / accelerate | (0.05, 0.7, 0.1, 1) / (0.3, 0, 0.8, 0.15) | Expressive moments only |

(Material)
- **Decelerate in, accelerate out** (Material). Default fades **150ms in, 75ms out** (Material).
- Lightning modal: backdrop fades ~100ms; modal scales 0.9 → 1.0 (Lightning).
- Keep most UI motion **100–250ms**; things can appear instantly and fade out ~150ms; skip per-list-item animations (Linear).
- Animate **transform and opacity only** — never width/height/top/left (layout thrash) (Linear).
- Skeletons animate so the page doesn't look frozen; cross-fade skeleton → content, no white flash (Carbon, Lightning).
- Highlight newly added rows/items briefly, then return to normal (Ant, Fiori).
- **`prefers-reduced-motion: reduce`:** replace slides, zooms and parallax with fades or no motion; keep only essential motion (`foundations/accessibility.md`). Auto-moving content always needs pause/stop (WCAG 2.2.2). Nothing flashes >3/s (WCAG 2.3.1).

## 9. Response-time limits

| Limit | Meaning | Design response |
|---|---|---|
| 0.1s | Feels instant | Direct-manipulation feedback (press state, selection) must land here (NN/g) |
| ~0.3s | Below this show nothing | No placeholder <300ms; skeleton from ~300ms (Lightning) |
| ~0.4s | Doherty threshold — productivity holds when the system answers within ~400ms | Optimistic UI for routine saves (Laws of UX, Linear) |
| 1s | Flow of thought holds | Over 1s, show busy state (NN/g) |
| 10s | Attention limit | Determinate progress, estimate, Cancel, run in background (NN/g) |

INP target ≤200ms (web.dev). Full loading and progress rules: `patterns/feedback-and-states.md` and `foundations/defaults.md`; performance budgets: `saas/global-and-performance.md`.

## 10. Aesthetic-usability caution

Attractive UIs are *perceived* as easier, and polish masks problems in testing (Laws of UX). In audits and tests, measure task success, errors and time — not how good it looks. Never trade data density, contrast or legibility for a cleaner screenshot (NN/g CA6).

---

## Common AI failures
- Mixing compact and comfortable components on one page, or per-component density toggles.
- Shrinking font size to "make it dense" instead of tightening spacing.
- Expressive, marketing-scale headings and hero type inside an app or inside cards.
- Decorative gradients, colourful icons beside KPIs, and status shown by colour alone.
- Several primary buttons per view; everything bold.
- Icon-only toolbars with no tooltips or accessible names.
- Off-scale spacing (13px, 22px) instead of 4/8 multiples.
- 400–600ms bouncy animations on routine UI; animating width/height; no reduced-motion handling.
- Spinners flashing on sub-300ms loads; no feedback at all on 2s waits.
- Judging a design by how polished the mockup looks.

## Sources
- https://www.sap.com/design-system/fiori-design-web/v1-139/foundations/visual/cozy-compact
- https://developer.salesforce.com/blogs/2018/08/new-density-settings-for-the-lightning-experience-ui-in-winter-19
- https://carbondesignsystem.com/components/data-table/usage/
- https://carbondesignsystem.com/elements/typography/style-strategies/
- https://carbondesignsystem.com/data-visualization/dashboards
- https://carbondesignsystem.com/patterns/loading-pattern
- https://carbondesignsystem.com/components/modal/usage
- https://carbondesignsystem.com/guidelines/accessibility/overview/
- https://spring-21.lightningdesignsystem.com/guidelines/messaging/components/modals
- https://spring-21.lightningdesignsystem.com/guidelines/data-visualization/charts
- https://spring-20.lightningdesignsystem.com/guidelines/loading
- https://spring-20.lightningdesignsystem.com/guidelines/empty-state
- https://api.flutter.dev/flutter/material/ThemeData/visualDensity.html
- https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes
- https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- https://ant.design/docs/spec/proximity
- https://5x.ant.design/docs/spec/transition
- https://5x.ant.design/docs/spec/reaction
- https://ant.design/docs/spec/buttons.md
- https://design.gitlab.com/patterns/forms/
- https://design.gitlab.com/patterns/dashboards
- https://cloudscape.design/patterns/general/service-dashboard/dashboard-items/
- https://primer.style/product/ui-patterns/forms
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/usage
- https://design-system.service.gov.uk/patterns/complete-multiple-tasks/
- https://design-system.service.gov.uk/components/button/
- https://www.nngroup.com/articles/complex-application-design/
- https://www.nngroup.com/articles/dashboards-preattentive/
- https://www.nngroup.com/articles/tabs-used-right/
- https://nngroup.com/articles/response-times-3-important-limits
- https://lawsofux.com/doherty-threshold/
- https://lawsofux.com/aesthetic-usability-effect/
- https://lawsofux.com/von-restorff-effect/
- https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
- https://web.dev/articles/inp
- https://spectrum.adobe.com/page/international-design/
