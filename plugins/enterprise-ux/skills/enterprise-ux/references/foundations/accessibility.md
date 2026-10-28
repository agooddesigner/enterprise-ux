# Accessibility

**Load when:** designing or auditing any UI for keyboard, screen reader, contrast, target size, motion or zoom; choosing ARIA roles or a table vs grid; writing a testing plan; or answering procurement/legal questions (EAA, EN 301 549, Section 508, ADA, VPAT/ACR).

**Target: WCAG 2.2 Level AA.** It is backward compatible with 2.1 AA (except removed 4.1.1) and matches the incoming EU benchmark (WCAG 2.2, EN 301 549 v4.1.1). Items tagged **[K]** are established practice not re-verified against the primary page — re-check before quoting as authority.

---

## 1. WCAG 2.2 A + AA success criteria

**NEW** = added in 2.2. WCAG 2.2 became a Recommendation on 5 Oct 2023 (WCAG 2.2). Use final 2.2 numbering, not the old Candidate Recommendation numbering (WCAG 2.2).

### Perceivable
| SC | Name | Lvl | Do this in a web app |
|---|---|---|---|
| 1.1.1 | Non-text Content | A | Text alternative for meaningful icons, images, charts; decorative ones hidden; icon-only buttons get an accessible name |
| 1.2.1 | Audio-only and Video-only (Prerecorded) | A | Transcript or text/audio alternative for demo/onboarding media |
| 1.2.2 | Captions (Prerecorded) | A | Caption tutorial and release videos |
| 1.2.3 | Audio Description or Media Alternative (Prerecorded) | A | Description or full text alternative where visuals carry info |
| 1.2.4 | Captions (Live) | AA | Caption embedded live webinars/streams |
| 1.2.5 | Audio Description (Prerecorded) | AA | Audio description where visuals aren't narrated |
| 1.3.1 | Info and Relationships | A | Structure in code: headings, lists, `<table>`+`<th>`, `<label>`, fieldset/legend, landmarks |
| 1.3.2 | Meaningful Sequence | A | DOM order = reading order; no meaning via CSS `order` |
| 1.3.3 | Sensory Characteristics | A | No "click the green button on the right" |
| 1.3.4 | Orientation | AA | Don't lock orientation |
| 1.3.5 | Identify Input Purpose | AA | Correct `autocomplete` tokens on personal-data fields |
| 1.4.1 | Use of Color | A | Second cue (icon, text, pattern, underline) for status, required, errors, series, inline links |
| 1.4.2 | Audio Control | A | Autoplay audio >3s can be paused/stopped [K for 3s] |
| 1.4.3 | Contrast (Minimum) | AA | Text 4.5:1, large text 3:1 |
| 1.4.4 | Resize Text | AA | 200% without loss |
| 1.4.5 | Images of Text | AA | Real text, not pictures of text |
| 1.4.10 | Reflow | AA | Works at 320 CSS px wide without 2-D scroll, except genuinely 2-D content (data tables, maps, diagrams, toolbars) |
| 1.4.11 | Non-text Contrast | AA | Component boundaries, states, focus rings, icons, essential chart parts ≥ 3:1 |
| 1.4.12 | Text Spacing | AA | Survives line-height 1.5×, paragraph 2×, letter 0.12×, word 0.16×; no fixed heights/`overflow:hidden` on text |
| 1.4.13 | Content on Hover or Focus | AA | Tooltips/popovers dismissible (Esc), hoverable, persistent |

### Operable
| SC | Name | Lvl | Do this |
|---|---|---|---|
| 2.1.1 | Keyboard | A | Everything works by keyboard |
| 2.1.2 | No Keyboard Trap | A | Focus can always leave; modals trap on purpose and close on Esc |
| 2.1.4 | Character Key Shortcuts | A | Single-key shortcuts can be turned off, remapped with a modifier, or only active on focus |
| 2.2.1 | Timing Adjustable | A | Turn off, adjust ≥10×, or warn with ≥20s and extend ≥10 times |
| 2.2.2 | Pause, Stop, Hide | A | Auto-updating feeds, carousels, tickers can be paused [K for 5s threshold] |
| 2.3.1 | Three Flashes or Below Threshold | A | ≤3 flashes per second |
| 2.4.1 | Bypass Blocks | A | Skip link and/or landmarks |
| 2.4.2 | Page Titled | A | Descriptive `<title>` on every view, including SPA route changes |
| 2.4.3 | Focus Order | A | Logical order; sensible focus after modal close/route change |
| 2.4.4 | Link Purpose (In Context) | A | No bare "Click here"/"View" |
| 2.4.5 | Multiple Ways | AA | Nav plus search or sitemap |
| 2.4.6 | Headings and Labels | AA | Descriptive |
| 2.4.7 | Focus Visible | AA | Always visible; never `outline:none` without replacement |
| 2.4.11 | Focus Not Obscured (Minimum) **NEW** | AA | Focused element never *entirely* hidden by sticky headers, banners, chat widgets, toasts; use `scroll-padding` |
| 2.5.1 | Pointer Gestures | A | Single-pointer alternative to multipoint/path gestures |
| 2.5.2 | Pointer Cancellation | A | Act on up-event; allow abort by moving off |
| 2.5.3 | Label in Name | A | Accessible name contains the visible label |
| 2.5.4 | Motion Actuation | A | Shake/tilt has UI alternative and can be disabled |
| 2.5.7 | Dragging Movements **NEW** | AA | Every drag has a single-pointer click/tap alternative; keyboard alone doesn't satisfy it |
| 2.5.8 | Target Size (Minimum) **NEW** | AA | ≥24×24 CSS px or an exception (spacing, equivalent, inline, user agent, essential) |

### Understandable
| SC | Name | Lvl | Do this |
|---|---|---|---|
| 3.1.1 | Language of Page | A | `<html lang>` |
| 3.1.2 | Language of Parts | AA | `lang` on foreign-language passages |
| 3.2.1 | On Focus | A | Focus never changes context |
| 3.2.2 | On Input | A | Changing a value doesn't change context unannounced |
| 3.2.3 | Consistent Navigation | AA | Repeated nav in the same relative order |
| 3.2.4 | Consistent Identification | AA | Same function = same label/icon everywhere |
| 3.2.6 | Consistent Help **NEW** | A | Repeated help (contact, chat, help link) in the same relative order; help isn't required to exist |
| 3.3.1 | Error Identification | A | Error described in text, field identified |
| 3.3.2 | Labels or Instructions | A | Visible labels and format hints; placeholder is not a label |
| 3.3.3 | Error Suggestion | AA | Say how to fix when known |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | Reversible, or validated with correction, or confirmed — bulk delete, billing, contracts |
| 3.3.7 | Redundant Entry **NEW** | A | Don't make users re-type data within one process; auto-fill or offer to select. Browser autofill alone doesn't count |
| 3.3.8 | Accessible Authentication (Minimum) **NEW** | AA | No cognitive test at login without alternative: allow paste and password managers, paste OTPs, offer passkeys/SSO/magic links |

### Robust
| SC | Name | Lvl | Do this |
|---|---|---|---|
| 4.1.1 | Parsing | — | **Obsolete, removed in 2.2.** For 2.0/2.1, treat as always satisfied for HTML; its issues now fall under 1.3.1/4.1.2 (WCAG 2.2, Deque) |
| 4.1.2 | Name, Role, Value | A | Custom widgets expose role, name and states (expanded, selected, checked, pressed) and update them |
| 4.1.3 | Status Messages | AA | Non-focus status updates announced via `role="status"`/`alert`/`log` |

AAA new in 2.2, for reference: 2.4.12 Focus Not Obscured (Enhanced), 2.4.13 Focus Appearance, 3.3.9 Accessible Authentication (Enhanced) (WCAG 2.2).

---

## 2. Thresholds cheat sheet

| Topic | Value |
|---|---|
| Text contrast (1.4.3) | ≥ 4.5:1 |
| Large text (1.4.3) | ≥ 3:1; large = ≥18pt or ≥14pt bold ≈ 24px / 18.66px bold [K conversion] |
| Enhanced (1.4.6 AAA) | 7:1 / 4.5:1 large [K] |
| Non-text contrast (1.4.11) | ≥ 3:1 |
| Rounding | Never round up: 4.49:1 fails [K] |
| Resize (1.4.4) | 200% |
| Reflow (1.4.10) | 320 CSS px wide (≈1280px at 400%); 256 CSS px tall for horizontal content |
| Text spacing (1.4.12) | 1.5× / 2× / 0.12× / 0.16× |
| Target size (2.5.8 AA) | 24×24 CSS px; spacing exception = 24px circle on each small target doesn't overlap another |
| Target size (2.5.5 AAA) | 44×44 CSS px |
| Timing (2.2.1) | ≥10× adjust; ≥20s warning; ≥10 extensions; >20h exempt |
| Flashing (2.3.1) | ≤ 3 per second |
| Focus appearance (2.4.13 AAA) | ≥ 2px perimeter-equivalent area, ≥ 3:1 change |

**Recommended focus ring (design-system default):** 2px solid outline, 2px `outline-offset`, ≥3:1 against both the component and the page background. Satisfies 2.4.7, 1.4.11 and AAA 2.4.13. Inset rings need >2px (e.g. 3px); on variable backgrounds use a two-colour ring (WCAG technique C40). Use `outline`, not `box-shadow`, so it survives forced colours [K].

---

## 3. ARIA: rules before patterns

- **"No ARIA is better than bad ARIA."** A role is a promise: `role="button"` on a `<div>` means *you* must script focus and keys; browsers won't (WAI-ARIA APG).
- **Native first:** `<button>`, `<a href>`, `<input type=checkbox>`, `<select>`, `<dialog>`, `<details>`, `<table>`. Add ARIA only where no native element exists (APG) **[consensus]**.
- APG keyboard conventions are informative, not normative; APG examples are not production code (APG).
- Pages using ARIA tend to have more detected errors (WebAIM Million) [K — re-verify current figure].

### Table vs `role="grid"`

| Situation | Use |
|---|---|
| Read-only tabular data, even with sorting, links, row checkboxes | Native `<table>` + `<caption>` + `<th scope>`; focusables stay in normal Tab order |
| Spreadsheet-like editable cells, arrow-key cell navigation expected, tab stops would explode | `role="grid"` |
| Unsure | `<table>`. Grid is frequently misapplied (often a component-library default) and breaks screen-reader table commands, headers and counts (Roselli) |

(APG, Roselli) See `patterns/tables.md`.

### Pattern quick reference

| Pattern | Role / structure | Required keys |
|---|---|---|
| **Grid** | `grid` (labelled) > `row` > `columnheader`/`rowheader`/`gridcell`; `aria-sort`, `aria-selected`, `aria-readonly`; `aria-rowcount`/`aria-rowindex` when virtualised. **One tab stop** | Arrows move cell (no wrap); Home/End row; Ctrl+Home/End grid; PgUp/PgDn; Enter/F2 edit, F2/Esc exit; Ctrl+Space col, Shift+Space row, Ctrl+A. Focus via roving `tabindex` or `aria-activedescendant` [K] |
| **Combobox** | `combobox` on input; `aria-expanded`, `aria-controls`, `aria-autocomplete`, `aria-activedescendant`; popup `listbox` (default) / `grid` / `tree` / `dialog` | Down opens/moves in; Alt+Down open; Alt+Up close; Enter accept; Esc close. **DOM focus stays on input** unless popup is a dialog |
| **Listbox** | `listbox` > `option` (opt. `group`); `aria-selected` (single) or `aria-checked` (multi), `aria-multiselectable` | Up/Down; Home/End (>5 options); type-ahead (>7); multi: Space toggle, Shift+Arrows, Ctrl+A. No interactive content inside options |
| **Dialog (modal)** | `dialog` + `aria-modal="true"` + `aria-labelledby`; background inert (`<dialog>.showModal()` or `inert`) | Tab/Shift+Tab wrap inside; Esc closes; focus returns to trigger. Initial focus per `foundations/defaults.md` |
| **Alert dialog** | `alertdialog` + `aria-modal` + `aria-labelledby` + `aria-describedby` → message | As dialog. Use for "Delete 42 records?" |
| **Tabs** | `tablist` > `tab` (`aria-selected`, `aria-controls`); `tabpanel` (`aria-labelledby`) | Arrows move (wrap); Home/End opt.; Tab goes to panel. Auto-activate only if panels render instantly; else manual (Enter/Space). Not for nav links |
| **Menu / menu button** | `<button aria-haspopup="menu" aria-expanded>` → `menu` > `menuitem`/`menuitemcheckbox`/`menuitemradio` | Enter/Space/Down open on first item; Up/Down; Home/End; Esc closes and returns focus; Tab leaves menu. Reserve for action menus; use `<nav>` + links for navigation [K] |
| **Disclosure** | `<button aria-expanded>` (+ opt. `aria-controls`); or `<details>` [K] | Enter/Space toggle |
| **Accordion** | Heading > sole child `<button aria-expanded aria-controls>`; panel opt. `region` (skip if ~6+ can be open) | Enter/Space toggle; normal Tab |
| **Tree** | `tree` > `treeitem`, children in `group`; `aria-expanded` on parents; `aria-level`/`setsize`/`posinset` when lazy | Right expand/child; Left collapse/parent; Up/Down; Home/End; Enter action; type-ahead; `*` expand siblings. A side nav of links is usually not a tree [K] |
| **Toolbar** | `toolbar` (labelled), only with **3+ controls** | Single tab stop; Left/Right between controls; Home/End opt. |
| **Breadcrumb** | `<nav aria-label="Breadcrumb">` + list of links; `aria-current="page"` on last | None custom. `<ol>`, separators `aria-hidden` [K] |
| **Switch** | `switch` + `aria-checked`, or `<input type=checkbox role=switch>` | Space toggles. Label never changes with state. Immediate-effect settings only [K] |

(APG)

### Live regions and toasts
- `role="status"` = polite: "Saved", "128 results", "Export ready". `role="alert"` = assertive: only urgent, time-sensitive info — using it for non-urgent content is a 4.1.3 failure pattern. `role="log"` for feeds, chat, audit streams (WCAG 4.1.3, APG).
- The live-region container must **already be in the DOM**; inject text into it. Separate regions for status vs errors; a polite message can be dropped if an assertive one fires at once (WCAG 4.1.3 techniques).
- `aria-busy="true"` while a region updates (Primer).
- Toasts never steal focus; if a response is required, use an alertdialog (APG). Persistent toast container from page load (PatternFly). Toasts with actions don't auto-dismiss, or pause on hover/focus and offer the action elsewhere [K]. Fast auto-dismiss can breach 2.2.x (APG). Toast policy: `foundations/defaults.md`, `patterns/feedback-and-states.md`.
- A results-count message counts as a status message; the results list itself doesn't (WCAG 4.1.3).

---

## 4. Enterprise specifics

| Topic | Rule |
|---|---|
| **Sortable tables** | Header text inside a `<button>` filling the cell; `aria-sort` only on the sorted `<th>`, moved on change; arrow glyphs `aria-hidden`; explain sortability once in the caption (APG). Announce sort change via polite status [K]. Row checkbox names "Select row: Invoice 1042"; row menu "Actions for Invoice 1042" [K]. Table scrolls horizontally inside a labelled, focusable container while the page reflows (WCAG 1.4.10 exception) |
| **Charts** | Short summary (what + key takeaway) plus data access ("View as table") [K]; no colour-only series — direct labels, patterns, markers (1.4.1); lines, bars, points, legend keys ≥3:1 (1.4.11); tooltips meet 1.4.13 and are keyboard-reachable; legend toggles are buttons with `aria-pressed` [K]. See `patterns/dashboards-and-dataviz.md` |
| **Form errors** | Text error naming the field (3.3.1) + fix (3.3.3); `aria-invalid="true"` + `aria-describedby`; on submit, summary with links + focus moved to it (2+ errors) or first invalid field (see `foundations/defaults.md`); inline errors that appear without focus moving must be announced (4.1.3); icon + text, not red alone (1.4.1) |
| **Drag alternatives (2.5.7)** | Sortable list → Move up/Move down; kanban → "Move to…" menu; slider → click track + numeric input; column resize/reorder → menu + numeric input / Move left/right [K]; file drop → always a "Browse files" button. Keyboard drag satisfies 2.1.1, **not** 2.5.7 |
| **Single-key shortcuts (2.1.4)** | Settings panel to turn off/remap; `?` help dialog; `aria-keyshortcuts`; don't override screen-reader/browser keys [K]. Ctrl/Cmd/Alt combos are outside 2.1.4. Reason: speech-input users trigger them by dictating [K] |
| **Session timeouts (2.2.1)** | Warning alertdialog that takes focus, ≥20s, single action to extend, ≥10 extensions — or let admins/users turn off or set ≥10× default. Preserve unsaved data across re-auth (AAA 2.2.5, good practice) [K] |
| **Reduced motion** | Honour `prefers-reduced-motion: reduce` — swap slides/zooms/parallax for fades or none [K]. Auto-moving content still needs pause/stop (2.2.2) regardless. See `foundations/visual-and-motion.md` |
| **Forced colours** | `@media (forced-colors: active)`; backgrounds and `box-shadow` vanish → use real `outline`/`border` (transparent ones become visible); SVG icons `currentColor`; don't show selection by background colour only; `forced-color-adjust: none` sparingly (swatches, charts) with system colours [K] |
| **Zoom 200% / 400%** | 200%: no loss (1.4.4). 400% at 1280px = 320px: side nav → menu button, multi-column forms → single column, toolbars wrap or overflow to "More", sticky headers shrink so they don't hide focus (2.4.11), modals scroll internally; only tables/diagrams scroll in 2-D within their container |
| **Redundant entry (3.3.7)** | Multi-step wizards (onboarding, checkout, provisioning) reuse earlier answers: "Same as billing address", pre-filled review step. Exceptions: essential, security re-entry (confirm new password), stale data |
| **Accessible auth (3.3.8)** | Allow paste + password managers; allow pasting OTP (manual transcription isn't compliant); offer passkey/SSO/magic link; puzzle/math/distorted-text CAPTCHAs need a non-cognitive alternative — audio-CAPTCHA transcription doesn't count; applies even when CAPTCHA appears only after failed attempts. See `saas/accounts-and-permissions.md` |
| **Target size** | 24×24 minimum; size dense-table icon buttons to the cell or space them per the exception (2.5.8). Pair with Fitts's Law (`foundations/ux-laws-and-heuristics.md`) |

---

## 5. Testing method

**Automated catches only part of it** — roughly a third to a half of issues depending on how you count (by volume vs by SC) [K — Deque and UK GDS studies not re-verified; don't quote exact %]. A Lighthouse 100 ≠ conformant [K].
- Run axe (jest-axe / @axe-core/playwright) in CI on every **state** — open menus, error states, modals — not just page load [K].
- Check token contrast pairs with a WCAG 2.x tool; APCA is not normative for 2.x [K].

**Keyboard test (per view)** (WebAIM, APG)
1. Mouse away. Tab from the address bar: skip link first; order follows reading order; no positive `tabindex`.
2. Focus always visible and never fully covered by sticky bars, toasts, chat widgets (2.4.7, 2.4.11).
3. Expected keys: Enter links; Enter/Space buttons; Space checkbox/switch; arrows in radios, tabs, menus, listboxes, trees, grids, toolbars; Esc closes menus, dialogs, tooltips.
4. Modals: focus in on open, Tab wraps, Esc closes, focus returns to trigger.
5. No traps; composite widgets are single tab stops.
6. Drag/resize/reorder have keyboard AND single-click alternatives (2.5.7).
7. Single-key shortcuts can be disabled/remapped (2.1.4).
8. Repeat at 400% / 320px and with forced colours on.
9. On mobile, test with an external keyboard.

**Screen-reader smoke test** [K]
- Pairings: NVDA + Firefox/Chrome; JAWS + Chrome (enterprise-dominant); VoiceOver + Safari (macOS/iOS); TalkBack + Chrome (Android).
- NVDA: H/D/K/F/T/B jump heading/landmark/link/field/table/button; Insert+F7 elements list; Insert+Space browse/focus mode; Ctrl+Alt+Arrows in tables. VoiceOver: Cmd+F5; VO = Ctrl+Option; VO+U rotor.
- Checklist per flow: page title announced on route change · landmarks and heading outline make sense · every control announces name + role + state (expanded/selected/checked/sorted) · form errors announced · status messages (save, results, toasts) announced without focus moving · dialogs announce title on open · tables announce column headers when moving cells.
- Include users with disabilities in research on critical workflows; expert audit before publishing an ACR [K].

---

## 6. Legal landscape — not legal advice

| Regime | What it means for B2B SaaS |
|---|---|
| **European Accessibility Act** (Directive (EU) 2019/882) | Applies from **28 Jun 2025**, via national laws (e.g. DE BFSG). Covers consumer-facing services: e-commerce, consumer banking, e-books, e-communications, audiovisual access, passenger transport booking. **B2B SaaS used only professionally is generally out of scope**, but is pulled in by a consumer-facing component (customer portal), plans sold to individuals, consumer e-commerce signup — and in practice when it powers a client's covered service (bank portal, booking engine, storefront) (vendor/law-firm interpretation; confirm with counsel). **Microenterprise exemption** for services: <10 staff AND turnover or balance sheet ≤ €2M. Disproportionate-burden claims must be documented per requirement. **Transition:** pre-28 Jun 2025 service contracts may run unchanged until expiry, no later than **28 Jun 2030**. Penalties set nationally; reported maxima vary by source (verify — as of Oct 2026) |
| **EN 301 549** | v3.2.1 (2021) = WCAG 2.1 A/AA. **v4.1.1 published 2 Sep 2026** = WCAG 2.2 A/AA plus reworked user-preference and real-time-text clauses and EAA mapping annexes. Presumption of conformity with the EAA only once cited in the OJEU — **citation status unverified** (expected ~30 Nov 2026 per Deque). Some national laws cite it undated. WCAG 2.2 AA ≠ full EN 301 549 conformance (non-web, documentation, support clauses) (verify — as of Oct 2026) |
| **Section 508** (US federal) | Revised 508 Standards incorporate **WCAG 2.0 A/AA** for web, software, documents. Federal buyers expect a 508 ACR [K] (verify — as of Oct 2026) |
| **ADA Title II** (US state/local government, DOJ 2024 rule) | **WCAG 2.1 AA**. Deadlines extended by interim final rule (effective 20 Apr 2026): population ≥50,000 → **26 Apr 2027**; <50,000 and special districts → **26 Apr 2028**. Covers content provided through contractors, so SaaS sold to state/local government must meet it. DOJ may revisit cost provisions. Related HHS Section 504 deadlines are reported inconsistently (verify — as of Oct 2026) |
| **ADA Title III** (private businesses) | No DOJ web technical rule; litigation uses WCAG as the de facto benchmark [K] (verify — as of Oct 2026) |
| **VPAT / ACR** | ITI's VPAT, once completed, is an Accessibility Conformance Report. Editions: 508, EU (EN 301 549), WCAG, INT (all). Terms: Supports / Partially Supports / Does Not Support / Not Applicable. Publish one per product + version, dated, with a remediation roadmap; enterprise and public-sector procurement asks for it. Check itic.org for a WCAG 2.2 / EN 301 549 v4 edition [K] (verify — as of Oct 2026) |

**Practical rule:** build to WCAG 2.2 AA now — it covers 2.0/2.1 AA buyers (508, ADA Title II) and the EU benchmark.

---

## Common AI failures
- `<div onClick>` buttons and custom selects with ARIA bolted on instead of native elements.
- `role="grid"` on read-only data tables (usually from a component library default).
- `outline: none` on focus, or a `box-shadow`-only ring that disappears in forced colours.
- Icon-only row actions with no accessible name, or every row's menu named just "Actions".
- Drag-and-drop with no click alternative, or claiming keyboard drag satisfies 2.5.7.
- Status/error colour with no icon or text; chart series distinguished only by hue.
- Toasts with `role="alert"` for routine success, injected along with a new live region (never announced), or auto-dismissing with an action inside.
- Single-key shortcuts (`j`, `k`, `e`) with no off switch.
- Sticky headers/footers or cookie and chat widgets covering the focused element (2.4.11).
- Login that blocks paste or OTP paste; CAPTCHA with no non-cognitive alternative.
- Citing 4.1.1 Parsing as a 2.2 failure; quoting exact automated-coverage percentages.
- Stating EAA/EN 301 549/ADA dates as settled law without the verify flag.

## Sources
- https://www.w3.org/TR/WCAG22
- https://www.w3.org/TR/2023/REC-WCAG22-20231005/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22
- https://www.w3.org/WAI/WCAG22/implementation-report
- https://www.w3.org/WAI/WCAG22/Understanding/parsing
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum
- https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry
- https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum
- https://www.w3.org/WAI/WCAG22/Understanding/consistent-help
- https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance
- https://w3c.github.io/wcag/understanding/status-messages.html
- https://w3c.github.io/wai-website/ARIA/apg/patterns/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/grid/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/combobox/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/listbox/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/dialog-modal/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/alertdialog/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/menu-button/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/menubar/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/treeview/
- https://w3.org/WAI/ARIA/apg/patterns/tabs/
- https://www.w3.org/WAI/ARIA/apg/patterns/accordion
- https://www.w3.org/WAI/ARIA/apg/patterns/disclosure
- https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb
- https://w3.org/WAI/ARIA/apg/patterns/switch
- https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/
- https://www.w3.org/WAI/content-assets/wai-aria-practices/shared/templates/read-this-first.html
- https://www.w3.org/WAI/ARIA/apg/example-index/table/sortable-table.html
- https://www.w3.org/TR/2021/NOTE-wai-aria-practices-1.2-20211129
- https://webaim.org/standards/wcag/checklist
- https://webaim.org/techniques/keyboard/
- https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html
- https://htmhell.dev/adventcalendar/2023/22/
- https://www.uxpin.com/studio/blog/aria-live-regions-for-dynamic-content/
- https://patternfly.org/2022.05/components/alert/accessibility
- https://www.deque.com/fr/blog/wcag-2-2-removes-4-1-1-parsing-and-how-axe-core-is-impacted/
- https://primer.style/product/ui-patterns/loading
- https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web
- https://www.adatitleiii.com/2026/04/doj-extends-ada-title-ii-website-accessibility-deadlines-for-governmental-entities-but-litigation-and-compliance-risks-remain/
- https://www.reedsmith.com/articles/doj-extends-digital-accessibility-compliance-dates-under-title-ii-of-the-ada/
- https://www.barrierbreak.com/ada-title-ii-hhs-accessibility-deadline-extensions/
- https://www.dwt.com/insights/2026/09/european-accessibility-act-ict-standards-update
- https://www.deque.com/blog/en-301-549-v4-1-1-is-final-what-changed-what-it-means-and-what-you-should-do/
- https://accessible.org/what-is-en-301-549/
- https://lawplayer.com/eu/article/32019L0882/art_32
- https://sota.io/blog/european-accessibility-act-2019-882-saas-web-app-compliance-guide-2026
- https://askem.com/compliance/eaa/
- https://www.xictron.com/en/blog/accessibility-act-exemptions-microenterprises-2026/
- https://testparty.ai/blog/eaa-timeline-deadlines
