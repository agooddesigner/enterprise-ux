# Visual craft: the premium enterprise look

**Load when:** building or restyling any enterprise UI in HTML/CSS and it must look Linear/Stripe/Vercel-grade rather than template-AI; choosing tokens when no design system exists; styling KPI tiles, tables, nav, charts; or running the final visual polish pass.

Complements `foundations/visual-and-motion.md` (density, spacing rules, motion tokens, response times) and `patterns/dashboards-and-dataviz.md` (what to chart and why). This file is *how it looks*. Accessibility floors: `foundations/accessibility.md`.

**Composition first:** for layout, hierarchy, colour roles and the expressive bento direction, start with `foundations/visual-direction.md` (dials, presets, mixing); this file covers polish details and fallback tokens.

**Existing design system wins.** If the product has tokens/components, map the roles below onto them, fill only the gaps, and never introduce a second palette, radius set or type scale (house; see `foundations/defaults.md`).

---

## 1. What "premium" actually is

- Premium = **restraint + consistency + alignment**, not effects. Monochrome first; colour only for meaning and one accent (Geist, Refactoring UI, Stripe dashboard) **[consensus]**.
- Design in greyscale first, add colour last; hierarchy must already work without it (Refactoring UI).
- Content leads, chrome recedes: dimmer sidebar, softer dividers, fewer and smaller icons (Linear 2026 refresh).
- Structure should be felt, not seen: fewer separators, low-contrast borders, spacing does the grouping (Linear, Refactoring UI).
- Alignment is felt after minutes of use: icons, labels and buttons on shared vertical/horizontal lines (Linear 2024).
- Generate scales in a perceptual space (LCH/OKLCH/Lab) so equal steps look equal across hues (Linear, Stripe, Strom). HSL lightness lies — yellow and blue at the same L differ wildly (Stripe).

## 2. Default token set (use when no design system exists)

Neutral scale follows Radix's 12-step roles: 1–2 app/subtle backgrounds, 3–5 component bg rest/hover/active, 6–8 borders (subtle → interactive → strong/focus), 9–10 solid, 11–12 low/high-contrast text (Radix). Geist uses the same idea on 10 steps (Geist). Values below are house picks, cool-neutral, contrast computed.

```css
:root {
  /* Neutrals — cool grey, faintly blue (Refactoring UI: tint greys; Linear 2026: not too warm or muddy) */
  --bg:            #ffffff;  /* app canvas / content (Geist background-1) */
  --bg-subtle:     #f7f8f9;  /* sidebar, table header, page behind cards (Radix 2) */
  --bg-raised:     #ffffff;  --bg-overlay: #ffffff;  /* cards / menus, modals (+ shadow in light) */
  --bg-hover:      #eff0f3;  /* row/ghost-button hover (Radix 3–4) */
  --bg-active:     #e7e9ed;  /* pressed, selected nav item (Radix 5) */
  --border-subtle: #e7e9ed;  /* dividers, card edges (Radix 6) */
  --border:        #d6d9df;  /* input/button borders at rest (Radix 7) */
  --border-strong: #878d99;  /* hover border; any border that must pass 3:1 */
  --text-1:        #16181d;  /* primary text, values — never pure #000 */
  --text-2:        #5b616e;  /* secondary text, labels, axis labels */
  --text-3:        #6b7079;  /* tertiary/meta — still ≥4.5:1, never lighter */
  /* One accent (brand). Used on: primary button, focus ring, links, selection, single-series charts */
  --accent:        #2457d6;  --accent-hover: #1d47b8;
  --accent-text:   #2050c8;  --accent-subtle: #eef3fe;  /* selected row, active tab bg */
  --on-accent:     #ffffff;
  /* Semantic: text colour + subtle bg from the same hue (Stripe badge rule) */
  --success: #17723f; --success-subtle: #e8f6ee;
  --warning: #8a5300; --warning-subtle: #fdf3dc;  --warning-solid: #f5b544; /* dark text on solid */
  --danger:  #c22f37; --danger-subtle:  #fdeced;  --danger-solid: var(--danger);
  --info:    var(--accent-text); --info-subtle: var(--accent-subtle);
  --ring: 0 0 0 2px var(--bg), 0 0 0 4px var(--accent);  /* only where outline can't be used */
  /* Elevation: light theme = shadow; keep them faint and offset (Refactoring UI, Comeau) */
  --shadow-xs: 0 1px 2px rgb(16 24 40 / .06);
  --shadow-sm: 0 1px 3px rgb(16 24 40 / .08), 0 1px 2px rgb(16 24 40 / .04);
  --shadow-md: 0 4px 12px -2px rgb(16 24 40 / .10), 0 2px 4px -2px rgb(16 24 40 / .06);
  --shadow-lg: 0 16px 32px -8px rgb(16 24 40 / .16), 0 4px 8px -4px rgb(16 24 40 / .06);
  /* Radius by role (Geist: 6 base, 12 menus/modals, 16 fullscreen) */
  --r-sm: 4px;   /* badges, checkboxes, tags, kbd */
  --r-md: 6px;   /* buttons, inputs, selects, nav items */
  --r-lg: 8px;   /* cards, panels, table containers */
  --r-xl: 12px;  /* menus, popovers, modals, drawers */
  --r-full: 9999px; /* avatars, toggles, status pills only */
  /* Spacing: 4px grid (Carbon tokens 2–96) */
  --s-0_5: 2px; --s-1: 4px; --s-2: 8px; --s-3: 12px; --s-4: 16px; --s-5: 20px;
  --s-6: 24px; --s-8: 32px; --s-10: 40px; --s-12: 48px; --s-16: 64px;
  /* Type: productive 14px base (Carbon), Inter or system UI (Linear uses Inter + Inter Display) */
  --font: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, monospace;
  --t-xs: 12px/16px; --t-sm: 13px/18px; --t-base: 14px/20px; --t-md: 16px/24px;
  --t-lg: 20px/28px; --t-xl: 24px/32px; --t-2xl: 30px/36px;
  --w-regular: 400; --w-medium: 500; --w-semibold: 600;
  /* Charts: muted context + one accent; categorical only when categories are equal peers */
  --chart-1: #2457d6; --chart-2: #0f8a7e; --chart-3: #b8650a; --chart-4: #b83f8c; --chart-5: #6b56c9;
  --chart-context: #878d99; --chart-grid: #e7e9ed; --chart-axis: var(--text-2);
}
:root[data-theme="dark"] {           /* also mirror under prefers-color-scheme: dark */
  --bg: #0f1012; --bg-subtle: #16171a; /* canvas darker; panels/cards LIGHTER = higher (Atlassian, WorkOS) */
  --bg-raised: #16171a; --bg-overlay: #1e2024;   /* menus, modals: lighter still */
  --bg-hover: #1e2024; --bg-active: #25282c;
  --border-subtle: #25282c; --border: #34383e; --border-strong: #6a717d;
  --text-1: #eceef1; --text-2: #a8adb7; --text-3: #8a9099;  /* off-white, not #fff (Material, Atmos) */
  --accent: #3565db; --accent-hover: #3a6be0; --accent-text: #8fb0ff; --accent-subtle: #17223d;
  --success: #4cc38a; --success-subtle: #11261b;
  --warning: #f0b44c; --warning-subtle: #2a1f0b; --warning-solid: #f0b44c;
  --danger: #ff6b70;  --danger-subtle: #2e1416;  --danger-solid: #c92f37;
  --shadow-sm: 0 1px 2px rgb(0 0 0 / .4);
  --shadow-md: 0 0 0 1px var(--border-subtle), 0 8px 16px -4px rgb(0 0 0 / .5);
  --shadow-lg: 0 0 0 1px var(--border), 0 16px 40px -8px rgb(0 0 0 / .6);
  --chart-1: #6f95f5; --chart-2: #33b6a8; --chart-3: #e09a3c; --chart-4: #e070b6; --chart-5: #9d8cf0;
  --chart-context: #6a717d; --chart-grid: #25282c;
}
body { font: var(--t-base) var(--font); color: var(--text-1); background: var(--bg);
       -webkit-font-smoothing: antialiased; }
.num, td.num, .kpi-value { font-variant-numeric: tabular-nums; } /* (Tailwind docs, Geist) */
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; } /* (WCAG 2.4.13) */
```

**Why these choices**
- Three text tiers only: dark-not-black / grey / lighter grey (Refactoring UI). Tier 3 is clamped at ≥4.5:1 — the "light grey meta text" that fails AA is the most common premium-look failure (house, computed).
- Body weight 400, emphasis 500–600; never below 400 for UI text (Refactoring UI). Two to three weights total.
- Two shadow layers (soft ambient + tight contact) look real; offset vertically, light from above (Refactoring UI, Comeau). Cards at rest get **border OR shadow, never both plus a tint** (Laith AI-slop guide).
- Dark mode is a separate palette, not an inversion: lighter surface = higher elevation; borders do the work shadows can't; accents lighter/less saturated so they don't vibrate (Atlassian, WorkOS, Material, Atmos). Pure black canvas and pure white text are both avoided (Material, Atmos).
- Stripe's rule of thumb for any scale you generate: steps ≥5 apart pass small text; ≥4 apart pass icons/large text — design the scale so pairing is arithmetic (Stripe, Strom).
- Mono only for code, IDs, paths, timestamps-as-data (Geist).

**Computed contrast (WCAG 2.x, sRGB)** — re-run if you change a value:

| Pair | Light | Dark | Need |
|---|---|---|---|
| text-1 on bg / bg-subtle | 17.8 / 16.7 | 16.4 / 15.4 | 4.5 |
| text-2 on bg / bg-subtle | 6.2 / 5.8 | 8.0 (on raised) / 7.2 (overlay) | 4.5 |
| text-3 on bg / bg-subtle | 5.0 / 4.7 | 5.6 / 5.1 (overlay) | 4.5 |
| on-accent on accent (primary button) | 6.2 | 5.2 | 4.5 |
| accent-text on accent-subtle | 6.2 | 7.4 | 4.5 |
| success / warning / danger on own subtle | 5.4 / 5.7 / 4.9 | 7.2 / 8.7 / 6.2 | 4.5 |
| white on danger (light) / danger-solid (dark) | 5.6 | 5.3 | 4.5 |
| border-strong on bg (inputs needing 3:1) | 3.3 | 3.7 | 3.0 |
| focus ring (accent) on bg | 6.2 | 6.6 | 3.0 |
| chart-1…5 on bg | 6.2 / 4.2 / 4.3 / 5.1 / 5.5 | 6.2 / 7.2 / 7.6 / 6.1 / 6.4 | 3.0 |
| chart-context on bg | 3.3 | 3.7 | 3.0 |

`--border` (1.4:1) and `--border-subtle` are decorative separators; any boundary that is the *only* cue for a control (input edge, checkbox) uses `--border-strong` or another cue (WCAG 1.4.11, `foundations/accessibility.md`). Light text-3 on bg-hover is 4.4:1 — on hovered/selected rows switch meta text to text-2 (computed). Dark accent hover goes *lighter* only to #3a6be0 — #4572e4 drops white text to 4.4:1 (computed).

## 3. Type scale in use

| Role | Token | Weight | Colour | Notes |
|---|---|---|---|---|
| Page title | 20/28 (24/32 on sparse pages) | 600 | text-1 | letter-spacing −0.01em; one per page |
| Section / card title | 14/20 or 16/24 | 600 | text-1 | Not bigger — weight, not size (Refactoring UI) |
| Body, table cells, inputs | 14/20 | 400 | text-1 | Most common style (Geist copy-14, Carbon productive) |
| Secondary line, metadata | 13/18 | 400 | text-2 / text-3 | Geist label-13 is the tabular-number style |
| Column headers, field labels | 12/16 or 13/18 | 500 | text-2 | Sentence case, never all caps (NN/g, Atlassian dropped caps) |
| KPI value | 24/32 or 30/36 | 600 | text-1 | tabular-nums, −0.02em |
| Badge, kbd, helper | 12/16 | 500 | role colour | Carbon 12px adds +0.32px tracking |

- **Max 4–5 sizes per screen**; scale steps grow toward the top (Refactoring UI: 12/14/16/18/20/24/30…). Tighten tracking on large headings, loosen slightly on 12px (Refactoring UI, Carbon).
- Labels are a last resort: when a value's format is self-evident (email, date, currency), style it rather than labelling it; when a label is needed, make the **value** the emphasised part and the label quiet (Refactoring UI).

## 4. Hierarchy recipes

**Page header** — bg, no card. Row: title (20/600) + optional status badge; right: secondary actions (ghost/secondary, 32px) then one primary. Below: one meta line 13/text-2 ("Updated 3 min ago · Owner Priya Shah"). 24px below header to content; tabs sit on the header's bottom border (house; one primary per view — `foundations/defaults.md`).

**KPI tile** — bg, 1px border-subtle, r-lg, padding 16–20, no shadow, no icon (NN/g). Stack: label 13/500 text-2 → 8px → value 30/600 tabular text-1 → 4px → delta row: "↑ 12.4%" 12/500 in success/danger *with arrow and sign* + "vs prior 30 days" 12 text-3. Optional sparkline 28–32px tall, full width, below (Stripe: prior period in small text under the main figure). Tiles in a row share height, window, padding (`patterns/dashboards-and-dataviz.md`).

**Card / panel** — bg (on a bg-subtle page) or bg-subtle (on bg page), border-subtle, r-lg. Header 48px: title 14/600, optional 13/text-2 description, ghost actions right. Body padding 16 (20 in sparse layouts). No nested cards — use a divider or spacing inside (Fountain, Hallmark). Accept depth from lightness, not shadow, at rest (Linear, Geist, Atlassian default surface).

**Table** — container r-lg + border-subtle, or edge-to-edge in a page. Header row 36–40px, bg-subtle, 12–13/500 text-2. Rows 40px (32 compact), 14 text-1; secondary columns text-2. Horizontal hairlines border-subtle only, **no vertical rules, no zebra unless >8 columns** (Refactoring UI fewer borders; zebra general practice). Numbers right-aligned, tabular, same decimals per column; units in header not cells. Hover bg-hover; selected accent-subtle + checked box. Primary column text-1/500 as the link; row actions appear in a fixed last column (always visible kebab, not hover-only — Laith). Full rules: `patterns/tables.md`.

**Side nav** — 240–256px, bg-subtle (dimmer than content, Linear 2026), right border-subtle. Items 32px, r-md, 8px inset, 14/500 text-2, 16px icon text-3; hover bg-hover; active bg-active + text-1 + icon text-1 (no coloured stripe). Group labels 12/500 text-3 sentence case, 16px above. Counts right-aligned 12 tabular text-3. Workspace switcher top, user menu bottom.

**Toolbar** (above table/list) — 32px controls, gap 8: search (240px, left) → filter chips → spacer → view options (ghost icon buttons with tooltip) → one primary. Active filters as removable chips (bg-active, 12–13/500). Same height as the controls it sits with (Carbon).

**Empty state** — replaces the container, centred *inside it* (the one place centring is right). Optional 24–32px line icon text-3 (no illustration in small containers — `foundations/visual-and-motion.md`); title 14–16/600; one sentence 14 text-2 ≤60ch; one primary or secondary action. Hide toolbars/filters that can't act yet (Refactoring UI). Copy rules: `patterns/feedback-and-states.md`.

**Buttons** — 32px (28 compact, 36 large), padding 12, 14/500, r-md. Primary solid accent; secondary bg + border + text-1; ghost transparent → bg-hover; tertiary as link. Hierarchy by style, not by colour per meaning; red only as the primary inside a destructive confirm (Refactoring UI).

## 5. Data-viz styling recipe

- **Ink budget:** keep data ink, delete the rest within reason — no 3D, gradients, shadows, textures, chart borders or background fills (Tufte, NN/g).
- **Gridlines:** horizontal only, 1px `--chart-grid`, 3–5 at round values; lighter than axis labels (Datawrapper). Drop them when bars carry data labels (NN/g). No y-axis line; x-axis baseline 1px border-strong at zero.
- **Axis labels:** 12px text-2, horizontal (never rotated — truncate or thin ticks instead), two-level dates on two lines (Datawrapper). Units in the title or first tick, not every tick.
- **Labels over legends:** label series directly at line ends; legend only when direct labels collide (NN/g).
- **Accent rule:** one series that matters in `--chart-1`, everything else `--chart-context` grey; grey is a storytelling tool, not "unimportant data you forgot" (Datawrapper). Brand accent is for single-series charts; in multi-series categorical charts don't let the brand hue imply "most important" (Datawrapper/finn.no).
- **Categorical:** ≤5 hues in fixed order, same series = same colour on every chart (Carbon, Lightning); vary lightness too so it survives colour-blindness and greyscale (Datawrapper). Sequential: one hue, light = low, dark = high; diverging: two hues meeting at light grey (Datawrapper).
- **Marks:** lines 1.5–2px, round joins; bars r-sm on the value end only, 60–70% band fill; points 6–8px only on hover/last value (general practice). Area under a line ≤10% opacity of the series colour or none (general practice).
- **Sparklines:** word/row-sized, ~5:1 or wider, no axes/grid/frame; 1.5px text-2 or accent line; dot + value on the last point; optional faint grey band for the normal range; min/max dots only if they matter (Tufte). Same y-scale when comparing rows, or label that scales differ.
- **Tooltips:** bg-overlay, r-md, shadow-md, 12–13px; header = x value in text-2, rows = swatch + series + right-aligned tabular value (general practice). Behaviour rules: `patterns/dashboards-and-dataviz.md`.
- **Number formatting:** `Intl.NumberFormat` — `notation:'compact'` for tiles/axes (1.2K, 123M, 2 significant digits), exact on hover; `signDisplay:'exceptZero'` for deltas (+12.3%, 0%); `currencySign:'accounting'` for finance negatives; `style:'unit'` for units (V8 Intl). Fixed decimals per metric; percentages ≤1 decimal; thin non-breaking space before units (general practice).

## 6. Polish details checklist

- **Alignment:** every element snaps to a few vertical lines; text baselines align across adjacent columns (Refactoring UI); icon centred to the cap height of its label, not the box (general practice).
- **Optical spacing:** buttons with leading icon get ~2px less padding on the icon side; padding inside > gap between siblings inside < gap between groups (Refactoring UI).
- **Icons:** one set, one stroke width (1.5px at 16px or 2px at 20/24), sizes 16 in UI / 20 in nav-headers only; never scale a 16px icon up — use the set's larger size or put it in a shape (Refactoring UI). Icons text-2/text-3, not brand colour.
- **States for every interactive element:** rest / hover (bg one step up or border-strong) / active (bg-active or scale 0.98) / focus-visible (2px outline + 2px offset) / disabled (text-3, no pointer, still readable) / loading (spinner replaces label, width locked) (Radix 3-4-5, WCAG 2.4.13).
- **Hover only on hover devices:** wrap hover styles in `@media (hover:hover) and (pointer:fine)` (Kowalski).
- **Transitions:** colour/bg 120–150ms ease; transform/opacity only; menus 150–200ms ease-out from scale .96–.98 + opacity 0, never from scale 0; exits faster than enters; no animation on keyboard-triggered or 100×/day actions (command palette) (Kowalski). Durations/easing tokens: `foundations/visual-and-motion.md`.
- **Tooltips:** delay first open (~400–600ms), then neighbours open instantly (Kowalski; delay value general practice).
- **Avatars:** 20/24/32px; people round, orgs/workspaces r-md square; initials 500 weight on a hashed muted bg; 1px inner ring `rgb(0 0 0 / .08)` so photos don't bleed into the surface (Refactoring UI inner shadow). Stacks overlap −4px with a 2px bg ring, "+3" chip after 3–4.
- **Badges:** 20px high, 12/500, padding 0 6–8, r-sm (or r-full for status pills — pick one app-wide); subtle bg + same-hue text; status badges carry a dot or icon + word, never colour alone (Stripe, WCAG 1.4.1). No status dot without a real state (Fountain).
- **Numbers:** tabular everywhere numbers stack or update; right-align; consistent precision; "—" for unknown (`foundations/defaults.md`); real-looking data, never 99.9%/10,000+ placeholder stats or "Acme/John Doe" (Hallmark, Laith).
- **Truncation:** single-line `text-overflow: ellipsis` with full value in `title`/tooltip; middle-truncate IDs and file paths; never truncate numbers — widen or abbreviate (general practice). Buttons never wrap to two lines (Hallmark).
- **Loading:** skeleton blocks in bg-active, radii matching the real content (text 4px), reserving exact space; one synchronised shimmer direction or a slow opacity pulse, no colourful gradients; on large desktop screens a static skeleton is fine for short loads (eBay Playbook). Under reduced motion: static.
- **Hairlines:** borders 1px, never 2px except focus/selected; dividers inset to content padding, not edge-to-edge inside cards (Linear 2026 softened dividers).
- **Scrollbars and sticky:** sticky table headers and page headers get a border-subtle or overflow shadow only once scrolled (Atlassian overflow shadow).
- **Z-index and layers:** named scale (base, sticky, dropdown, overlay, modal, toast), no 9999 (Hallmark).

## 7. Generic AI UI tells → do instead

Krebs' review of 500 Show HN sites found gradient backgrounds/titles (28%), untouched default shadcn (23.5%), centred titles (23.5%), always-dark with grey text and uppercase labels (20%), identical icon-card grids (20%), glass panels (17%), accent side-stripes (13%), purple/indigo CTAs (11%) (Krebs via Gigazine). The problem is shipping defaults unexamined, not any single pattern (Krebs).

| Tell | Do instead |
|---|---|
| Purple→indigo gradients on hero, buttons, headings | Solid brand accent on primary action only; neutrals everywhere else (Fountain, Laith) |
| Several neon/rainbow accents competing | One accent + neutrals + semantic colours with fixed meanings (Fountain) |
| Emoji as icons/bullets/nav | One consistent SVG icon set, `currentColor` (Fountain, Hallmark) |
| Big radius + drop shadow + tinted bg on every card | Radius by role (§2); one depth cue per surface (Laith) |
| Cards inside cards | Spacing, dividers, type weight; cards only for independently actionable items (Fountain) |
| Coloured left stripe on every card/alert | Neutral surfaces; status via badge/icon + text (Fountain, Hallmark) |
| Everything centred | Left-aligned app layouts; centre only empty states and tiny dialogs (Hallmark, Refactoring UI) |
| Grey-on-grey 3:1 meta text, uppercase tracking labels | text-3 ≥4.5:1, sentence-case 12–13/500 labels (Krebs, NN/g) |
| 6+ font sizes, semibold body | ≤5 sizes, body 400, 2–3 weights (Laith, Refactoring UI) |
| Glassmorphism / blur panels / glows / blobs | Opaque surfaces; elevation by lightness + faint shadow (Geist, Hallmark) |
| Rainbow multi-series charts, donut for everything | Grey context + one accent; bars/lines (§5, `patterns/dashboards-and-dataviz.md`) |
| Status dots on everything | Dots only for a defined live state, always with a label (Fountain) |
| Decorative icon-in-circle beside every KPI | No KPI icons; label, value, delta, baseline (NN/g) |
| Animate-on-scroll, bouncy easing | Still by default; motion only for state change (Geist, Hallmark) |
| Hover-only row actions, `outline:none` | Always-visible affordance; `:focus-visible` ring (Laith) |
| Dark mode = inverted light mode | Separate dark palette (§2) (Laith, WorkOS) |
| Inline hex/px values bypassing tokens | Only tokens; add a token if one is missing (Hallmark) |
| Proportional digits in tables | `tabular-nums` (Hallmark) |

## 8. Visual polish pass (run in order before presenting)

1. **Squint test in greyscale:** is there exactly one focal point per view, and does hierarchy hold without colour? Fix with weight/position before size (Refactoring UI).
2. **Token audit:** every colour, size, radius, shadow, space is a token; no off-scale values (13px gaps, 22px padding) (Hallmark, Carbon).
3. **Colour budget:** accent appears only on primary action, focus, links, selection, single highlighted series; status colours only where a status exists (Geist, Fountain).
4. **Type audit:** count sizes (≤5) and weights (≤3); labels quiet, values loud; no all caps; tabular numerals on every number column/tile (Refactoring UI, Hallmark).
5. **Alignment and spacing:** check left edges and baselines line up across header, toolbar, table, cards; within-group < between-group spacing; remove one border or divider wherever spacing already separates (Linear, Refactoring UI).
6. **Surface audit:** no nested cards; one depth cue per surface; sidebar dimmer than content; overlays the only things with real shadow (Linear, Atlassian).
7. **States:** hover, active, focus-visible, disabled, loading, empty, error exist for every interactive element and container (Laith, `patterns/feedback-and-states.md`).
8. **Charts:** gridlines faint, direct labels, grey + one accent, formatted numbers, no junk (§5).
9. **Content realism:** realistic names, values, lengths (incl. long names and 0/empty cases); no placeholder stats (Hallmark).
10. **Dark mode pass:** switch theme; check elevation reads (lighter = higher), accents don't vibrate, borders visible, charts legible (WorkOS, Atlassian).
11. **Contrast pass:** text ≥4.5:1, UI/chart marks ≥3:1 on their actual surface in both themes; re-run the computation for any changed token (WCAG 1.4.3/1.4.11, `foundations/accessibility.md`).
12. **Reduced motion and zoom:** `prefers-reduced-motion` honoured; layout survives 200% zoom/320px reflow (`foundations/accessibility.md`).

---

## Common AI failures
- Shipping the framework's default theme unmodified, with indigo primary and gradients — the single strongest "AI made this" signal.
- Pale grey secondary text (#9ca3af on white ≈2.5:1) to look "clean"; it fails AA and reads cheap on real monitors.
- Shadow + border + tint + large radius on every card; cards nested two or three deep.
- A different accent colour per section or per KPI; status colours used decoratively.
- Too many type sizes, semibold body text, uppercase tracked labels everywhere.
- Charts with full gridboxes, legends instead of direct labels, rainbow series, unformatted numbers (1234567.891).
- Dark mode by inverting, pure black canvas, saturated accents and invisible borders.
- Hover-only actions, `outline: none`, no disabled/loading/empty states.
- Ignoring the product's existing design system and pasting this token set over it.
- Judging success by the screenshot instead of running the polish pass and contrast check.

## Sources
- https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale
- https://www.radix-ui.com/colors/docs/palette-composition/composing-a-palette
- https://vercel.com/geist/colors
- https://vercel.com/geist/typography
- https://vercel.com/geist/materials
- https://vercel.com/design.md
- https://linear.app/now/how-we-redesigned-the-linear-ui
- https://linear.app/now/behind-the-latest-design-refresh
- https://linear.app/changelog/2026-03-12-ui-refresh
- https://stripe.com/it-ca/blog/accessible-color-systems
- https://mattstromawn.com/writing/generating-color-palettes/
- https://mattstromawn.com/projects/stripe-dashboard/
- https://www.925studios.co/blog/stripe-dashboard-design-breakdown
- https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886
- https://dev.to/updivision/book-review-refactoring-ui-by-adam-wathan-steve-schoger-2f7m
- https://dev.to/juanemilio31323/12-lessons-for-a-better-ui-refactoring-ui-the-book-4ea1
- https://primer.style/foundations/color/overview
- https://atlassian.design/foundations/elevation
- https://atlassian.design/foundations/typography/product-typefaces-and-scale
- https://www.atlassian.com/blog/design/implementing-typography-at-scale-the-journey-behind-the-screens
- https://carbondesignsystem.com/elements/typography/type-sets/
- https://carbondesignsystem.com/elements/spacing/overview/
- https://codelabs.developers.google.com/codelabs/design-material-darktheme/
- https://workos.com/blog/5-lessons-we-learned-adding-dark-mode-to-our-platform
- https://atmos.style/blog/dark-mode-ui-best-practices
- https://uxcel.com/blog/mastering-elevation-for-dark-ui-a-comprehensive-guide-342
- https://www.joshwcomeau.com/css/designing-shadows
- https://www.nngroup.com/articles/clutter-charts/
- https://data.europa.eu/apps/data-visualisation-guide/chart-junk-and-data-ink-origins
- https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/
- https://www.datawrapper.de/blog/emphasize-with-color-in-data-visualizations
- https://www.datawrapper.de/blog/colors-for-data-vis-style-guides
- https://www.datawrapper.de/academy/what-to-consider-when-choosing-colors-for-data-visualization
- https://www.datawrapper.de/blog/new-axis-ticks
- https://v8.dev/features/intl-numberformat
- https://tailwindcss.com/docs/font-variant-numeric
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance
- https://tessl.io/registry/skills/github/emilkowalski/skill/emil-design-eng
- https://playbook.ebay.com/design-system/components/loading-skeleton?tab=design
- https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui
- https://www.gigazine.net/gsc_news/en/20260423-design-slop
- https://instagit.com/Nutlope/hallmark/hallmark-anti-patterns-detected/
- https://github.com/Laith0003/ux-skill/wiki/How-to-detect-AI-slop-in-your-design
