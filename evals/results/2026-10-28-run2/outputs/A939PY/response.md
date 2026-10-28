# UX & Accessibility Review: Vendor Invoices screen

## P0: Blocking / data-loss

1. **"Delete All" has no confirmation, no undo, no error handling, and sits beside normal content.** One click calls `DELETE /api/invoices`. Add a confirm dialog that names the consequence ("Delete 2 invoices permanently?"), separate the button from routine actions, and style it as destructive. Prefer soft-delete or undo.
2. **Per-row delete (🗑) is also unconfirmed and silent.** There is no feedback on success or failure, and the row isn't removed from the UI.
3. **The form wipes all input on any submit click** (`value=''` on every input). A user who makes one typo loses everything. Reset only on success, and keep values on error.
4. **Focus outlines are removed** (`button:focus, input:focus, a:focus { outline: none }`) with no replacement. Keyboard users can't see where they are. This is a WCAG 2.4.7 failure. Remove the rule, or use a visible `:focus-visible` style.
5. **The loader overlay is never removed and covers the page.** `.spinner-page` is `position: fixed; inset: 0` with no hide logic, no background and no `role="status"`. It intercepts all pointer input, so the page may be unusable. Hide it when loading finishes, and announce it.

## P1: Serious accessibility failures

6. **Rows are clickable `div`s/`span`s** (`onclick` on `.row`). They're not focusable and have no role or key handler, so keyboard and screen-reader users can't open an invoice. Use a real link or button in the ID cell, or `tabindex`, `role` and Enter/Space handling.
7. **Nested interactive controls inside a clickable row.** Clicking 💾 or 🗑 also fires `openInvoice`, because there's no `stopPropagation`. Save or delete will therefore open a modal as well.
8. **Icon-only buttons have no accessible name.** The emoji are read inconsistently ("floppy disk", "wastebasket"). Add `aria-label="Save invoice 8f3a-22c1"` and so on.
9. **Touch targets are 16×16px.** The WCAG 2.5.8 minimum is 24px and the recommended size is 44px. The two adjacent destructive and non-destructive buttons are easy to mis-hit. Enlarge them and add spacing.
10. **Status is conveyed by colour alone** (green or red ●). This fails for colour-blind users and is invisible to screen readers. Add text or an icon ("Paid" / "Overdue") and `aria-label`.
11. **Inputs have no `<label>`s**, only placeholders. Labels vanish on typing, the placeholder contrast is typically weak, and screen-reader support is poor. Add visible labels, and `inputmode="decimal"` for Amount.
12. **The Submit button is permanently `disabled`** with no explanation and no code that enables it. The user can't submit at all, and there's no hint why.
13. **The error message is static and always visible** ("Invalid input"). It's unassociated with a field, has no `role="alert"`/`aria-live`, and doesn't say what's wrong. Show it only on error, with specific text ("Amount must be a number"), `aria-describedby` and `aria-invalid`.
14. **Toasts disappear after 2s and aren't announced.** There's no `aria-live` region, and 2s is too short (WCAG 2.2.1) to read. The message "Error 500: Something went wrong" is unhelpful and has no retry. Also, `del` and `deleteAll` don't call `toast` at all, and `save` only handles network failure, not HTTP 4xx/5xx, since `fetch` doesn't reject on those.

## P2: Significant usability and structure problems

15. **Contrast failures.** `.muted` (#b5b5b5 on white) is about 2.0:1, and `.status-ok` (#2e9e44) is about 3.4:1. Both fail the 4.5:1 requirement. `.status-bad` (#d64545) is borderline at about 4.3:1.
16. **The modal flow is risky.** A modal opens from a modal ("Confirm" opens a second one). Stacked modals are confusing, and nothing is specified for focus trapping, Esc to close, focus return, `role="dialog"`/`aria-modal` or scroll lock. Collapse to one dialog with a clear primary action. `location.hash = ''` is an unexplained side effect that can break back-button behaviour.
17. **The "table" is a div grid with no semantics.** The `.grid` and `.row` classes have no CSS defined, so the layout is unstyled and columns won't align. Use `<table>` with `<th scope>`, or ARIA grid roles. The `td.num` rule targets an element that doesn't exist, and numeric columns should be right-aligned, not centred.
18. **Amounts are unformatted** (`1200.5`, `87`). There's no currency or thousands separator, and no fixed decimals. Use `$1,200.50` through `Intl.NumberFormat`.
19. **The long vendor name** ("Globex International Holdings…") has no truncation or wrapping rules, so it will break the layout. Use wrapping or ellipsis with a `title` or tooltip.
20. **The sticky header (72px) has no landmark.** It uses a `div` where `<header>` or `<nav>` belongs, and the page has no `<main>`. The sticky header can also obscure focused elements, so add `scroll-padding-top`. WCAG 2.4.11 applies.

## P3: Polish and hygiene

21. **Missing `lang`, `viewport` meta, and a charset.** Without `lang`, screen readers may mispronounce content, and without a viewport meta the page is unusable on mobile. The `<html>` start is also malformed: a stray `down. -->` comment fragment precedes it, and a `<!DOCTYPE html>` is missing, which triggers quirks mode.
22. **The page title "App" is non-descriptive.** Use "Vendor Invoices – Acme Ops Console".
23. **The heading hierarchy starts at `<h2>`** with no `<h1>`. The app name in the header is a `<b>`, not a heading.
24. **"Showing all invoices"** is uninformative filler. Show a count and total instead, and add filter, sort and search, since there's no way to find an invoice in a long list.
25. **Truncated IDs** (`8f3a-22c1`) can't be copied reliably and have no meaning for users. Consider a copy affordance or a human-readable invoice number.
26. **There's no empty state, no loading state per action and no success feedback.** Add a disabled or busy state on buttons during requests, and double-submit protection.
27. **Emoji as icons** render differently per platform. Use consistent SVG icons with accessible names.

## Suggested fix order
1. Remove the loader overlay or its blocking behaviour; restore focus outlines.
2. Add confirmation and error feedback to every destructive action, and stop the form from clearing on submit.
3. Make rows and icon buttons keyboard-operable, labelled and large enough to hit.
4. Fix labels, error semantics, status text and contrast.
5. Rebuild the grid as a real table, and fix the document scaffolding (doctype, lang, viewport, title, landmarks).

I reviewed the code statically and didn't render it, so the layout points (especially #17 and #19) are inferred from the markup and CSS.
