# Default decisions (where the big design systems disagree)

**Load when:** you hit a choice where reasonable systems differ, or you need one consistent house rule. If the product already has a design system, **its rule wins** — these are the defaults for when it doesn't say.

Each row: the default, why, and when to pick the other side. Sources in brackets.

| Decision | Default | Pick the alternative when | Sources |
|---|---|---|---|
| **Validation timing** | Never validate before the user interacts. Validate on submit; move focus to an error summary (2+ errors) or the first invalid field. Once a field shows an error, re-validate it live as the user fixes it. | Long, expert data-entry forms where late errors cause expensive rework → also validate format on blur. | On submit: GOV.UK, Primer. On blur: Carbon, Fiori, Cloudscape, Polaris |
| **Disabling submit/save to signal errors** | Don't. Keep it enabled, explain errors on click. | Disable only to block a double submit (show loading state), for unmet prerequisites with a visible reason, or inside a tiny typed-confirmation modal. | Cloudscape, Primer, Pajamas, GOV.UK; Polaris allows with explanation |
| **Required vs optional marking** | Mark the minority. Enterprise forms are mostly required → mark optional fields "(optional)". Never asterisks alone. One convention per product. | Mostly-optional forms → mark required fields "(required)". | Carbon, Cloudscape, Pajamas, GOV.UK; Primer marks required |
| **Label position** | Labels above fields. | Left labels only for short (<10 field) forms on wide screens when vertical density is critical; left-align them. | Carbon, Fiori, Lightning, CXP eye-tracking; Ant defaults left |
| **Capitalization** | Sentence case everywhere (buttons, headings, labels, tabs, menus). | Only if the product's existing system is title case (e.g. SAP Fiori). | Carbon, Atlassian, PatternFly, Pajamas, Cloudscape, GOV.UK; Fiori uses title case |
| **Table row height** | 40px default, user-switchable compact (32px), applied app-wide, never mixed on one page. | Data-heavy power-user tool with mouse/keyboard only → 32px default. Touch → 44px+. | Carbon (40 default), Fiori (32 compact / 44 cozy), Lightning (user density) |
| **Toasts** | Only for non-critical success the user can't already see. ≤2 lines, close button, auto-dismiss ≥5s (longer for longer text), pause on hover/focus, `role="status"`. Never errors, never the only place for info, never something the user must copy. One position app-wide (top-right default). | Skip the toast entirely when the result is visible on screen (inline edit, navigated to new record). Primer avoids toasts altogether — acceptable choice. | Carbon, Atlassian, Lightning, Fiori, Polaris, Pajamas, Primer, Ant |
| **Loading indicator thresholds** | <~300ms: nothing. Initial load of a container: skeleton matching the layout (tables = skeleton rows). In-component wait 1–10s: spinner with text. >10s: determinate progress, time estimate, Cancel, "run in background", notify on completion. | Batch jobs over known counts: "Updating 3 of 50" even when short. | Lightning (300ms), Cloudscape, Primer, NN/g (0.1/1/10s), Carbon |
| **Timestamps** | Relative in feeds, lists, notifications ("12 min ago") with absolute on hover/`<time title>`. Absolute with time zone in audit logs, security, billing, incidents, exports, legal. | Users must correlate events across tools → absolute everywhere. | Cloudscape (relative default), Pajamas (absolute default), PatternFly |
| **Empty value in a cell** | Em dash "—" (or one other dash glyph — pick one, use everywhere). Never for a real 0. Never blank. | — | Cloudscape "-", Ant "--", NN/g |
| **Selection across pages** | Header checkbox selects the visible page; offer an explicit "Select all N matching" step; always show "N selected". Clear selection when sort/filter/page changes unless the UI clearly shows it persists. | High-volume triage tools → persist selection across pages with a visible count and "Clear". | Cloudscape (clear), PatternFly (persist), Fiori |
| **Delete friction** | Reversible → act immediately + Undo. Irreversible single item → confirmation dialog naming object + consequence. Irreversible, cascading, bulk-critical → typed confirmation. | Typed text = the resource name when deleting the wrong item is the main risk; = a fixed word ("delete") when names are long IDs or must localize. | Cloudscape, Pajamas, Ant, GOV.UK, NN/g |
| **Unsaved-changes prompt** | Warn only when something actually changed. Dialog: "Leave page?" with Stay (default focus) / Leave. Browser `beforeunload` for tab close/reload. | Form is valid and saving is cheap → offer "Save and leave" as well. | Cloudscape (Stay/Leave), Pajamas (Save/Discard) |
| **Save model** | Explicit Save for forms. Instant-apply only for imperative controls (toggles, single selects outside a form). Never mix both in one form. Never autosave financial, security or privacy settings. | Long free-text/document editing → autosave per field with "Saved 1 min ago" status. | Primer, Pajamas, Slack, Lightning |
| **Modal initial focus** | First input. If no inputs: the least destructive action (Cancel) for destructive confirms; the primary action for informational dialogs. Never pre-focus a destructive button. | — | WAI-ARIA APG, Carbon, Lightning |
| **Zero-results CTA** | "No results for …" + "Clear filters" secondary button. | — | Cloudscape, PatternFly (Pajamas omits CTA) |
| **Filters apply** | Live update for cheap/local data; explicit Apply/Go only when queries are expensive or fields are interdependent. Filter state always in the URL. | — | Fiori, Lightning, Carbon, Cloudscape |
| **Dates in UI** | Locale-formatted via `Intl` with explicit time zone; unambiguous month names in UI ("3 Mar 2026"); ISO 8601 in exports/APIs. | — | Cloudscape, PatternFly, Pajamas |

## Universal agreements (no conflict — treat as law)

- One primary action per view/container; Cancel is never primary. (all systems)
- Never use colour alone to convey meaning. (all systems, WCAG 1.4.1)
- Never nest a modal inside a modal. (Carbon, Atlassian, Ant)
- Never use placeholder text as the label. (Carbon, Atlassian, Primer, Pajamas, Cloudscape, GOV.UK)
- Errors say what happened + how to fix, never blame, no "oops/sorry/please/invalid". (GOV.UK, NN/g, Atlassian, Polaris, PatternFly)
- Success messages never say "Success!" or "successfully". (Atlassian, Fiori, PatternFly)
- Keep the user's input after any error. (GOV.UK, NN/g, Primer)
- An empty state replaces the whole container, says why it's empty and offers one next step. (Carbon, Cloudscape, NN/g, Fiori)
- Don't show a generic "No data" when data failed to load — that tells users their data is gone. (Primer, NN/g)

## Common AI failures
- Applying these defaults over a product's existing design system instead of following its rules.
- Mixing both sides of a row in one product (on-blur validation in one form, on-submit in another; "—" in one table, blank in the next).
- Citing a default as universal law when the table marks it as a disputed choice.

## Sources
Listed per row above; full URLs in `references/sources.md` and the pattern file each row points to.
