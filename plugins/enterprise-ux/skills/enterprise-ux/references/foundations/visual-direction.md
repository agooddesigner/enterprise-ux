# Visual direction: beautiful screens that are also great to use

**Load when:** building or redesigning any screen whose look hasn't been fixed by an existing design system — dashboards, overviews, first-impression screens, new products — or when the user asks for a style, a mix of styles, or a layout experiment. Read this **after Intake** (`modes/design.md` step 0) and **before** writing layout or CSS.

This file is not a kit. It describes taste as **dials** that any design system can express, **presets** that are known-good dial settings, and **rules for mixing and experimenting** without breaking usability. Apply it with the product's own tokens and components; use `foundations/visual-craft.md` fallback tokens only when there is no design system.

Never assume a style. People differ (Google's expressive-design research found a strong minority prefer calmer UIs even when expressive ones test faster). Ask during Intake; if nobody can answer, pick by product context (section 5) and say which you picked.

---

## 1. The 11 dials

Every aesthetic is a setting of these. Choose each dial deliberately; write them down.

| # | Dial | Range (low → high) | What it signals | Choose by |
|---|---|---|---|---|
| D1 | **Density** | Airy (16px body, 48–56px rows) → Comfortable (14px, 40–44px) → Compact (13px, 32–36px, 4px grid) | Calm guidance ↔ expert speed | **Usage frequency, not style.** Daily power use → compact; occasional → comfortable/airy. May differ by zone on one screen |
| D2 | **Shape** | Square 0–4px → Soft 6–10px → Round 16–28px → Pill | Serious ↔ friendly/playful | Brand personality. One radius family per product: cards / inner panels / controls |
| D3 | **Depth / material** | Hairline borders → Tonal steps (each surface ~2% lighter) → Soft low shadow → Glass (blur) → Hard offset shadow (no blur) | Precise ↔ tactile ↔ loud | Pick one primary depth method. Dark mode: lighter = higher, not shadows |
| D4 | **Canvas temperature** | Cool grey → Pure white → Warm paper (#f6f5f4-ish) → Near-black (never #000; e.g. #0b0b0f / brand at 1–10% lightness) | Clinical ↔ human ↔ focused | Brand + context; warm suits docs/collab, cool suits data, near-black suits dev/pro tools |
| D5 | **Colour strategy** | Status-only (UI monochrome, colour = status) → Mono + 1 accent → Neutral + brand + 1 highlight → Bold flat 2–3 colours | Trust/restraint ↔ energy | Domain risk: money/security → restraint; creator/consumer-ish → bolder |
| D6 | **Type voice** | Neutral grotesk (Inter, Geist, SF) → Humanist (IBM Plex, SAP 72, Open Sans) → Geometric/display heavy → Serif accent → Mono accent | Neutral ↔ institutional ↔ editorial ↔ technical | Serif only for content/headlines, never dense chrome. Mono for IDs, code, eyebrows |
| D7 | **Scale contrast** | Low (all 12–20px) → High (page title 40–56px, hero number 56–72px, units at ~half size) | Utility ↔ "wow" | Overviews and first-impression screens high; work screens low-to-medium |
| D8 | **Composition** | Uniform grid → Bento → List-detail → Table-first → Canvas → Editorial asymmetric → Document/feed | The layout's DNA | The job (section 6), not taste |
| D9 | **Ornament** | None → Blueprint grid lines (1px, 10–20% opacity) → Subtle gradient → Illustration → Texture/material | Austere ↔ expressive | Less on work screens; ornament never carries meaning |
| D10 | **Motion** | Functional only (state change, 100–200ms) → Subtle polish (hover lift, 150–250ms) → Expressive/spring | Instant ↔ alive | High-frequency flows stay functional; always honour reduced-motion |
| D11 | **Data-viz voice** | Hairline minimal (thin lines, light grid) → Monochrome + status colour (Stripe) → Chunky shapes (pill bars on tracks, thick rings, rounded heatmap cells) | Analytical ↔ friendly | Must match D2/D3; honesty rules always win |

Plus **mode**: light, dark, or both. Shipping dark only is an accessibility gap (glare/astigmatism users need light); shipping light only is fine for most enterprise products but power-user tools increasingly expect dark.

## 2. Presets (known-good dial settings)

Each preset is a starting point, not a costume. Map its roles onto the product's tokens.

| Preset | D1 Density | D2 Shape | D3 Depth | D4 Canvas | D5 Colour | D6 Type | D7 Scale | D8 Comp. | D9 Orn. | D10 Motion | D11 Viz | Fits | Avoid for |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Soft bento** | Comfortable | Round 20–28 + pills | Canvas/card contrast, soft shadow | Cool/lilac grey | Neutral + 1 accent + 1 highlight (lime/violet) + ink anchor | Grotesk/geometric display numbers | High | Bento | None | Subtle | Chunky | Overviews, demos, first-impression dashboards | Dense daily queues |
| **Dark precision** (Linear-style) | Compact | Soft 6–8 | Tonal steps + hairlines | Near-black (+ real light mode) | Mono + 1 accent used only on brand, focus, primary | Neutral grotesk, 13px body | Low–medium | List-detail / table-first | None | Functional | Hairline | Dev & power tools, keyboard-first | Occasional users; light-only contexts. Over-copied — differentiate |
| **Blueprint** (Vercel-style) | Comfortable | Soft 6–8 | Hairlines | White / near-black | B/W + ≤1 accent | Grotesk + mono | Medium | Grid / table | Blueprint lines | Functional | Hairline | Infra, AI, technical SaaS | Lifestyle, health, consumer-ish |
| **Restraint** (Stripe-style) | Comfortable | Soft 6–8 | Hairlines / soft shadow | White | Status-only: UI mono, colour = status | Neutral grotesk, ~6 sizes | Medium–high on numbers | Opinionated KPI home + tables | None | Subtle | Monochrome sparklines + status | Fintech, billing, trust-heavy | Teams needing heavy customisation |
| **Classic enterprise** (Carbon / Fiori Horizon / SLDS 2) | Comfortable + compact mode | Square–soft 0–8 | Borders + low elevation | White / light grey | Neutral + brand + semantic | Humanist (Plex, 72) | Low–medium | Table-first / object page | None | Functional | Hairline | ERP, CRM, regulated, large orgs | Startup "wow" pitches |
| **Warm paper** (Notion-style) | Comfortable–airy | Soft 8–12 (16–20 large shells) | Hairlines (10% black) | Warm paper | Neutral + 1 action blue | Grotesk; serif for quotes only; mono eyebrows | Medium | Document / list-detail | Light illustration | Subtle | Minimal | Docs, knowledge, collaboration | Heavy analytics |
| **Data-dense utility** | Compact | Square 0–4 | Hairlines | Light grey or near-black | Status-only | Grotesk + tabular/mono numbers | Low | Table-first / multi-pane | None | Functional | Hairline, sparklines | Ops, monitoring, trading, support queues | Onboarding, buyers' first look |
| **Swiss** | Comfortable | Square 0–4 | None/hairlines | White | 2–3 colours, one strong | Flush-left grotesk, large type hierarchy | High | Strict grid, asymmetric | None | Functional | Minimal, direct labels | Analytics, editorial dashboards, reports | Playful brands |
| **Expressive** (Material 3 Expressive) | Comfortable | Mixed shapes, round | Containment + colour fills | Tinted | Brand + tonal palette | Grotesk, size used for emphasis | High on key actions | Any | Shape accents | Spring | Chunky | Consumer-ish SaaS, key-action flows | Banking, established enterprise patterns |
| **Neubrutalism** | Comfortable | Square 0–4 (occasional pills) | Thick borders + hard offset shadow | Off-white / beige | Bold flat 1–3 | Heavy grotesk display + calm sans/mono | High | Bordered modular grid | Flat illustration | Abrupt, short | Chunky, outlined | Creator, startup, youth brands | Enterprise trust, dense tables |
| **Glass accents** | Any | Round | Glass only on floating chrome (nav, toasts, popovers) | Gradient/tinted | Brand | Grotesk | Medium | Any | Gradient | Subtle | Any | Brand-forward layers | Data surfaces (contrast unpredictable); always a solid fallback |
| **Tactile** | Comfortable | Round | Layered surfaces, physical cues | Warm | Brand | Grotesk | Medium | Any | Material | Subtle | Chunky | Explaining unfamiliar controls | Dense screens |

## 3. Mixing directions

1. **One preset leads**: it owns D5 colour strategy, D6 type voice and D3 depth — the "voice". Borrow at most 2–3 other dials from a second preset. Write it as: *"Lead: Restraint. Borrow: Soft bento composition (D8) + scale (D7); Dark-precision density (D1) for the table zone."*
2. **Density can vary by zone** on one screen (airy overview, compact table). That's a legitimate mix, not inconsistency — but shape, depth, colour and type must not vary.
3. **Clashing combos — don't, unless you state why:**

| Combo | Why it fails |
|---|---|
| Glass on data surfaces / dense tables | Contrast changes with what's behind; fails AA unpredictably |
| Hard offset shadows + 20px+ soft radius | Two personalities fighting (brutal vs soft) |
| Serif body text + compact density | Serifs slow scanning of labels and numbers |
| Bold multi-colour palette + status colours | Status colour stops meaning anything |
| Expressive/spring motion + high-frequency workflow | Delays and distracts on the 200th use |
| Neumorphism anywhere operable | Low-contrast controls by design |
| Dark-only + long-form reading | Text bleed/glare for some users; ship light |
| Blueprint ornament + illustration + gradient | Ornament stack; the grid only works when everything else is restrained |

4. **Invariants — never change with direction:** WCAG 2.2 AA contrast (check text on every loud surface separately), status colours used only for status, app shell and navigation, visible focus, real data, every state, honest charts, one primary action per view.

## 4. Experimenting with new layouts or styles

Allowed and encouraged — inside guard rails:
- **Change one layer at a time.** Keep shell, reading order, states and copy constant; vary composition (D8) or one dial. Then compare.
- **Name the hypothesis**: "Putting the queue as a 2-pane list-detail will cut clicks to triage vs a table + drawer."
- **Test with p95 data**, the longest names, an empty tenant and an error — a layout that only works with six rows isn't a layout.
- **Keep familiar patterns where users rely on them** (labels on actions, table conventions, back/escape). Google's research: breaking familiar patterns (e.g. icon-only actions, scattered layouts) lowered usability even when it looked modern.
- **Offer 2–3 variants** side by side when the user is choosing a direction; label each with its dial settings so they can say "this one, but with D2 from that one".

## 5. Default choice when nobody can answer

| Context signal | Default preset |
|---|---|
| Existing design system / tokens found | Its own look — map roles, change no dials except composition |
| Dev tool, infra, AI platform | Dark precision or Blueprint (ship both modes) |
| Finance, billing, security, healthcare | Restraint or Classic enterprise |
| ERP / CRM / back-office at large orgs | Classic enterprise |
| Docs, knowledge, collaboration | Warm paper |
| Ops / monitoring / queues | Data-dense utility |
| Overview / analytics dashboard / demo / pitch | Soft bento (current house default) |

State the pick in one line at the top of the work: *"Assumed direction: Soft bento (no design system found, overview dashboard)."*

## 6. Composition archetypes (D8)

| Archetype | Use when | Structure |
|---|---|---|
| **Bento overview** | 5–10 mixed widgets, one main answer | 12-col grid, size = importance, hero top-left, rows end together |
| **Opinionated KPI home** | 3–5 numbers matter most | Big numbers + previous period + sparkline, then one list |
| **Table-first workspace** | Daily processing of records | Toolbar + filters + table; detail in drawer or page |
| **List-detail, 2-pane** | Queues (issues, tickets, inbox) | List left, selected record right, resizable divider |
| **List-detail, 3-pane** | Only if a nav/filter column earns its space | Nav · list · detail |
| **Stacked drill-down** | Narrow screens | List → full-screen detail with back + next/prev |
| **Object page** | One record with sections | Header with key facts + actions, tabs/sections below |
| **Canvas** | Spatial thinking, agent outputs, diagrams | Free surface, selection-based actions, minimap |
| **Document / feed** | Collaboration, notes, activity | Reading column, comments in margin |
| **Kanban / timeline** | Status-driven or time-driven work | Columns or swimlanes; always a list/table alternative |
| **Customisable widget grid** | Different roles need different views | Saved layouts per role, global filters apply to all widgets |

AI placement (when the screen has an assistant): right-panel copilot (help while working), left-panel co-create (iterative outputs beside chat), inline prompts (micro-edits in content), centre chat (open-ended), grid/agent cells (structured research). See `saas/ai-features.md`.

## 7. Composition and craft that apply to every preset

- **Write the direction first** (3 lines, before code):
  ```
  Direction: <lead preset> [+ borrowed dials]. Mode: <light/dark/both>.
  Dials: D1 … D11 (only the ones that differ from the preset).
  Hero: <the single decision this screen exists for> shown as <big number / anchor card / first column>.
  ```
- **Size = importance.** The thing that answers the screen's question is largest and read first (top-left in LTR).
- **Three tiers:** decision (hero + 2–4 KPIs) → explanation (the chart that says why) → action (the list/table where work happens).
- **At most one anchor surface** (inverted/ink) and **one highlight** per screen; more loud surfaces = no hierarchy.
- **Scale contrast:** with D7 high — title 40–56px, hero number 56–72px, KPI numbers 36–48px, units/decimals ~40–55% of the number, labels 12–13px but ≥4.5:1. Tabular numerals for anything compared or updating.
- **Colour roles from a 12-step scale** (Radix model): 1–2 backgrounds, 3–5 component states (normal/hover/pressed), 6–8 borders (subtle/interactive/strong+focus), 9–10 solid fills, 11–12 text (low/high contrast). Map any brand onto these roles; derive dark mode as its own scale (desaturate ~20 points, surfaces get lighter as they rise, off-white text, no pure black).
- **Real content texture:** real names, logos, domain labels, realistic numbers (1,284 not 1,000), a human sentence under key numbers.
- **UX parts styled in the same language:** filters as chips/segmented controls, a quiet freshness line, incidents as tinted strips, per-widget skeletons and errors, undo toasts, focus rings that match the shape language.
- **Type count ≤ 4–5 sizes on screen; colour count:** canvas, surface, text, one accent, ≤1 highlight, status.

## 8. Render-and-look loop

If you can render (browser, screenshot, Figma), **look before presenting** and fix:
1. Squint: does the hero read first? One anchor, ≤1 highlight?
2. Do the chosen dials actually show? (A "Swiss" screen with 24px rounded cards isn't Swiss.)
3. Rows end together; no half-empty cards; nothing overlaps or clips.
4. Number formatting: no raw floats, consistent decimals, units present.
5. Contrast spot-check on every loud surface (ink, highlight, glass, dark mode).
6. States (loading, empty, one-widget error, no permission) look as designed as the ready state.
7. Mixes: does any combo from the clash table appear without a stated reason?

## Common AI failures
- Assuming one style (dark + gradients, or rounded bento) for every product without asking.
- Copying a preset's costume (colours, radius) but not its logic (Linear without keyboard-first, Stripe without restraint).
- Inventing a palette on top of an existing design system instead of mapping roles.
- Mixing dials so every surface has a different personality.
- Beautiful hero, generic everything else; or beautiful ready state, ugly states.
- Choosing density by look instead of usage frequency.
- Dark-only output; pure black canvases; glass behind tables.
- Experiments that change shell, layout and style at once, so nothing can be compared.

## Sources
- Google Design — Expressive Material research (46 studies, 18k+ participants): https://design.google/library/expressive-material-design-google-research
- Radix Colors — 12-step scale: https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale
- SAP Fiori Horizon visual foundations: https://www.sap.com/design-system/fiori-design-web/v1-142/foundations/visual/look-feel-and-wording
- Salesforce SLDS 2 / Cosmos: https://www.salesforce.com/blog/what-is-slds-2/
- Refactoring UI personality model (via RFUI docs): https://rfui-docs.onrender.com/choose-a-personality
- Linear style analysis: https://blog.logrocket.com/ux-design/linear-design ; tokens: https://www.buildmvpfast.com/blog/linear-aesthetic-tokens-density-keyboard-first-ux-2026
- Vercel/blueprint grid: https://www.setproduct.com/blog/complete-guide-to-blueprint-grid-design
- Stripe dashboard breakdown: https://www.925studios.co/blog/stripe-dashboard-design-breakdown
- Notion tokens analysis: https://webdesignhot.com/design.md/notion/
- Glass/neumorphism/Liquid Glass: https://setproduct.com/blog/liquid-glass-vs-glassmorphism
- Neubrutalism tokens: https://trends.daisyui.com/trend/neubrutalism/ ; 2026 trend catalogue: https://trends.daisyui.com/ui-design-trends-2026/
- Swiss style: https://justinmind.com/blog/swiss-style-web-design-everything-you-need-to-know
- Bento grids: https://www.saasframe.io/blog/designing-bento-grids-that-actually-work-a-2026-practical-guide
- Dark mode practice: https://atmos.style/blog/dark-mode-ui-best-practices
- List-detail variants: https://www.saasui.design/blog/saas-list-detail-master-detail-ux-patterns
- AI placement: https://uxdesign.cc/where-should-ai-sit-in-your-ui-1710a258390e
- Serif usage: https://fontalternatives.com/blog/text-serifs-comeback-2026/
- Aesthetic–usability effect (Kurosu & Kashimura 1995): https://en.wikipedia.org/wiki/Aesthetic%E2%80%93usability_effect
- Note: product breakdowns (Linear, Stripe, Notion, Mercury) are third-party analyses — treat their values as taste references, not specs.
