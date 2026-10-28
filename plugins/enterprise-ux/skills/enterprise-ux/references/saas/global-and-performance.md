# Global readiness and performance

**Load when:** designing or auditing for localization (text expansion, scripts, RTL), dates/times/time zones, number and currency formatting, or perceived and measured performance (Core Web Vitals, response times, optimistic UI, motion cost).

## 1. Text expansion

Expansion is inversely proportional to string length (IBM data via W3C; same bands in Spectrum):

| English length | Expect up to | Typical UI strings |
|---|---|---|
| ≤10 chars | 200–300% | Buttons, tabs, badges (~300%) |
| 11–20 | 180–200% | Labels (~200%) |
| 21–30 | 160–180% | Headers |
| 31–50 | 140–160% | Tooltips, short messages |
| >70 | ~130% | Paragraphs |

(W3C, Spectrum)
- The "plan for 30–40%" rule only holds for long text. German/Dutch run ~30% longer overall; Finnish/Hungarian ~50%. (Frontend Checklist, W3C)
- **No fixed widths** on text containers; use `min-inline-size` instead of fixed size. (Frontend Checklist)
- **Never truncate button labels**; never truncate nav items or column headings. (Frontend Checklist, PatternFly)
- If truncation is unavoidable (table cells), expose the full string via tooltip and accessible name; keep ≥4 visible chars. (W3C, PatternFly)
- Let form rows wrap so labels sit above inputs when long (labels-above is the house default — see `foundations/defaults.md`). (Frontend Checklist)
- Size database fields and API limits for expansion; don't abbreviate to fit. (Frontend Checklist, Fiori)
- **Test with a pseudo-locale** (accented, padded strings) in CI/Storybook. (Frontend Checklist)
- Sentence case translates better than title case. (Carbon)

## 2. Scripts and culture

- CJK may use fewer characters but each glyph is ~2 Latin chars wide. (W3C)
- Thai, Devanagari, Arabic (Nastaliq) and similar scripts need more line height (Thai example ~150%); never fix heights on text boxes. (W3C, Spectrum; WCAG 1.4.12)
- **No text inside icons or images.** (Spectrum)
- Culture-specific icons: ✓/✗ read differently in Japan (○ is positive); the mailbox metaphor is US-specific; avoid hand gestures. (Spectrum)
- Colour meanings vary by culture → never rely on colour alone for status. (Spectrum; WCAG 1.4.1)
- Set `<html lang>` and mark other-language passages with `lang`. (WCAG 3.1.1, 3.1.2)

## 3. Right-to-left (RTL)

| Mirror | Don't mirror |
|---|---|
| Overall layout, side nav, reading order | Media playback controls |
| Back/next arrows, chevrons | Clocks and calendars |
| List bullets/indent icons | Checkmarks |
| Button groups, toolbars | Numbers, phone numbers (stay LTR) |
| Sliders, toggles, progress bars | Currency amounts |
| Pagination, steppers | URLs, emails, code |
| — | Timelines and charts where mirroring changes meaning; photos |

(Wikimedia Codex, Frontend Checklist)
- Use **logical CSS properties** (`padding-inline-start`, `margin-inline-end`, `inset-inline`) instead of left/right. (Frontend Checklist)
- Set `dir` on the root and isolate user-generated mixed-direction strings (general practice — `<bdi>` / `dir="auto"`).

## 4. Dates, times, time zones

- **Store UTC ISO 8601 plus the event's original IANA zone.** (Phil Nash)
- Detect the user's IANA zone client-side; let them override it in personal settings. (Phil Nash, NN/g)
- Format with `Intl.DateTimeFormat` using locale + **explicit `timeZone`**; never hard-code offsets (DST). (Phil Nash; see `foundations/defaults.md`)
- Use `navigator.languages`, not `navigator.language`. (Phil Nash)
- UI dates use unambiguous month names ("3 Mar 2026"); exports/APIs use ISO 8601. (see `foundations/defaults.md`)
- **Always show a zone label** where time matters; a date alone can land on the wrong day for another zone. (Phil Nash)
- Zone label choice (lingo.dev):

| Label | Example | Use |
|---|---|---|
| Short abbreviation | CST | Avoid — ambiguous across regions |
| Long name | Central European Standard Time | **Global/enterprise teams** |
| Generic | Pacific Time | Stable year-round, regional audiences |
| Offset | GMT-8 / UTC+05:30 | **Global teams**, numeric clarity; audit logs |

- Relative times in feeds, absolute + zone in audit, billing, security, incidents (see `foundations/defaults.md`).
- Time-zone pickers: preselect detected zone; sort by city alphabetically; search; show country + offset ("New York (Eastern Time)"); handle DST automatically. (NN/g)
- Scheduling across zones: show the time in both the viewer's and the event owner's zone. (general practice)

## 5. Numbers and currency

General practice (MDN page not verified):
- Format with `Intl.NumberFormat` per locale; decimal and grouping separators differ (1,234.5 vs 1.234,5).
- en-IN uses lakh/crore grouping (12,34,567). Respect it for Indian locales; don't force Western grouping.
- Currency: format with the currency's own code and minor units; show ISO code where symbols are ambiguous ("US$", "CA$", or "EUR 1,500"). (PatternFly)
- Right-align numbers in tables; numerals not words. (Ant, Fiori, Pajamas)
- Exports carry raw unformatted values. (general practice)

## 6. Performance targets

### Core Web Vitals (at p75 of page views, mobile and desktop separately, same thresholds)

| Metric | Good | Poor |
|---|---|---|
| LCP (largest contentful paint) | ≤2.5 s | >4 s |
| INP (interaction to next paint) | ≤200 ms | >500 ms |
| CLS (cumulative layout shift) | ≤0.1 | >0.25 |

(web.dev)
- ~100 ms is when a response still feels caused by the input (INP ideal); 200 ms is achievable on low-end mobile. (web.dev)
- INP counts clicks, taps and key presses (not scroll/hover), input to next paint, across all interactions; it succeeded FID (widely cited as Mar 2024 — verify — as of Oct 2026). (web.dev)

### Human response limits

| Delay | Perception | UI response |
|---|---|---|
| ≤0.1 s | Instant | Direct-manipulation feedback must land here |
| ~0.4 s | Doherty threshold — productivity holds | Aim for full response under this |
| ≤1 s | Flow intact; delay noticed | No spinner needed (container loads still get a skeleton from ~300 ms per `foundations/defaults.md`) |
| 1–10 s | Attention wavers | Spinner with text |
| >10 s | Attention lost | Percent-done + estimate + Cancel + run in background + notify |

(NN/g, Doherty via lawsofux; thresholds align with `foundations/defaults.md` loading row: nothing under ~300 ms, skeleton for container loads)

## 7. Making it feel fast

### INP techniques (web.dev)
- Paint visual feedback in the **next frame**; defer non-critical work (saving, word counts) with `setTimeout`/`requestAnimationFrame`; yield after the UI update.
- Break up long tasks; avoid forced synchronous layout; keep the DOM small; `content-visibility` for off-screen content.
- Virtualize long tables rather than rendering thousands of rows (general practice; Fiori caps responsive tables at 200 rendered rows).

### Optimistic / local-first (Linear)
- UI reads from a local store; writes apply locally, then queue and sync in the background; the server confirms rather than grants permission.
- Validate before enqueueing so rollbacks stay rare; on rollback, restore the value and show an inline error with Retry. (Linear; Pajamas)
- **No spinners for routine actions.** (Linear)
- Not for irreversible, financial or permission-changing actions — wait for the server there. (general practice)

### Fast boot (Linear)
- Route-level code splitting, `modulepreload`, service-worker precache.
- Inline critical CSS + the saved theme so the shell paints first (no flash of wrong theme).
- Preload the app while the user is on the login page.

### Avoid layout shift
- Reserve space for async content; skeletons match final layout; tables use skeleton rows (Cloudscape, Primer; CLS ≤0.1).

## 8. Motion performance

- Animate **transform and opacity only**; 100–250 ms for UI transitions; appear instantly, fade out ~150 ms; skip per-list-item animations. (Linear)
- Material defaults agree: short durations 50–200 ms, fades 150 ms in / 75 ms out; decelerate entering, accelerate exiting. (Material)
- Honour `prefers-reduced-motion: reduce` — replace slides/zooms with fades or none; supports WCAG 2.3.3 (AAA). (general practice)
- See `foundations/visual-and-motion.md`.

## 9. Never look frozen

- Long operations on big data can take 4 s+ at p95 → show progress, never a dead UI. (Figma)
- Skeletons must animate. (Carbon)
- Keep old data visible and usable while refreshing; mark it busy. (Cloudscape, Fiori)
- Announce loading, done and failed to screen readers (`role="status"`, `aria-busy`). (Primer; WCAG 4.1.3)
- Start progress bars slow and finish fast; users notice stalls near the end. (NN/g)

## Common AI failures

- Fixed-width buttons and tabs sized to English, truncating German labels.
- `margin-left`/`padding-right` everywhere; arrows that don't flip in RTL, or phone numbers that do.
- Dates rendered with `toLocaleString()` without `timeZone`, or "CST" labels for a global team.
- Storing local times without zone; date-only fields that shift a day across zones.
- Hard-coded "$" and Western digit grouping for INR.
- Spinner on every click instead of optimistic updates; or optimistic updates for payments.
- Animating `width`/`top`/`height`; 500 ms+ transitions on routine UI.
- Layout jumping as data arrives (CLS), skeletons that don't match the final layout.

## Sources

- https://w3.org/International/articles/article-text-size
- https://spectrum.adobe.com/page/international-design/
- https://frontendchecklist.io/rules/i18n/text-expansion
- https://doc.wikimedia.org/codex/main/style-guide/bidirectionality.html
- https://philna.sh/blog/2021/02/22/display-dates-in-your-users-time-zone/
- https://lingo.dev/en/javascript-i18n/display-time-zone-names
- https://www.nngroup.com/articles/time-zone-selectors/
- https://web.dev/articles/defining-core-web-vitals-thresholds
- https://web.dev/articles/inp
- https://web.dev/articles/optimize-inp
- https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
- https://www.figma.com/blog/making-multiplayer-more-reliable/
- https://nngroup.com/articles/response-times-3-important-limits
- https://www.nngroup.com/articles/progress-indicators/
- https://lawsofux.com/doherty-threshold/
- https://www.patternfly.org/content-design/grammar/numerics
- https://www.patternfly.org/content-design/grammar/truncation
- https://ant.design/docs/spec/data-format
- https://cloudscape.design/patterns/general/loading-and-refreshing/
- https://primer.style/product/ui-patterns/loading
- https://carbondesignsystem.com/patterns/loading-pattern
- https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- https://www.w3.org/TR/WCAG22
- https://design.gitlab.com/patterns/saving-and-feedback/
