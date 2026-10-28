# UX & Accessibility Review: Acme Ops Console, Vendor Invoices

## P0: Blockers (fix before release)

1. **Loader overlay never goes away and covers the page.** `#loader` is `position: fixed; inset: 0` and nothing hides it. It blocks pointer interaction with the whole screen. It also has no `role="status"` or `aria-live`, so screen readers get no loading announcement. *Fix:* remove it when data loads, and use `role="status"` with a visible spinner.

2. **Focus outlines are removed everywhere.** `button:focus, input:focus, a:focus { outline: none }` leaves keyboard users with no focus indicator (WCAG 2.4.7). *Fix:* delete the rule, or replace it with a visible `:focus-visible` style.

3. **Destructive actions have no confirmation, undo or feedback.**
   - "Delete All" sits next to ordinary content and fires `DELETE /api/invoices` immediately.
   - The row 🗑 button does the same for a single invoice.
   - `del()` and `deleteAll()` have no `.catch`, no success state and no row removal.
   
   *Fix:* use a confirm dialog that names the consequence ("Delete all 2 invoices?"). Prefer undo for single deletes. Style Delete All as a danger button, separated from other actions.

4. **Rows are mouse-only and nest interactive controls.**
   - Rows are `div`s with `onclick`. They have no `tabindex`, role or key handler, so keyboard and screen-reader users can't open an invoice.
   - The save and delete buttons are inside the clickable row, and their clicks bubble up. Clicking 💾 or 🗑 also calls `openInvoice` and opens a modal.
   
   *Fix:* put a real link or button in the ID or vendor cell, and call `stopPropagation` (or drop the row handler).

5. **Icon buttons have no accessible name.** The 💾 and 🗑 buttons contain only emoji, which are read inconsistently ("floppy disk", "wastebasket"). The 16×16px size is far below the 24px minimum (WCAG 2.5.8), and well below the 44px recommended for touch. Adjacent destructive and save buttons make mis-taps likely. *Fix:* add `aria-label="Save invoice 8f3a-22c1"`, make targets at least 32–44px, and add spacing.

6. **The form wipes the user's input on any error.** The submit handler clears every input when clicked, whatever the result. Users must retype the vendor name and amount after each mistake. It also never validates or submits anything. *Fix:* keep the values, flag only the invalid field, and clear after success.

## P1: Serious

7. **Placeholders are the only labels.** "Vendor name" and "Amount" disappear when the user types, and placeholder contrast is typically too low. *Fix:* use visible `<label>` elements. Use `inputmode="decimal"` for Amount.

8. **The Submit button is disabled with no explanation.** Disabled buttons can't be focused, so keyboard and screen-reader users never learn why. *Fix:* keep it enabled and validate on submit, or explain the requirement next to it.

9. **The error message is always visible and not announced.**
   - "Invalid input" shows on load, before any interaction.
   - It is generic: it doesn't say which field is wrong or how to fix it.
   - It has no `role="alert"`, and it isn't linked to the inputs with `aria-describedby` and `aria-invalid`.
   - It is red, and the only other cue is colour.
   
   *Fix:* hide it until there's an error, make it specific, and place it next to the field.

10. **Status is conveyed by colour alone.** The ● in green or red has no text or accessible name (WCAG 1.4.1), so colour-blind and screen-reader users can't tell paid from unpaid, or whatever the states mean. Green `#2e9e44` on white is about 3.4:1, below the 4.5:1 needed for text. *Fix:* use text or an icon plus a label ("Paid", "Overdue"), with darker colours.

11. **Contrast failures.**
    - `.muted` `#b5b5b5` on white is about 2.1:1 (needs 4.5:1).
    - Red `#d64545` is about 4.1:1, which also fails for text.
    - Use roughly `#767676` or darker for muted text.

12. **The table is built from `div`s and spans.** `.grid` and `.row` have no CSS in the file (no grid layout is defined), and there are no table semantics. Columns won't line up, and screen readers can't navigate by header. The stylesheet also defines `td.num`, but the markup has no `td`, so the number styling never applies. *Fix:* use `<table>` with `<th scope="col">`, or add `role="table"`, `role="row"` and so on. Right-align numbers.

13. **The toast is inaccessible and unhelpful.**
    - It disappears after 2 seconds, which is too fast to read (WCAG 2.2.1).
    - It isn't in a live region (`role="status"` or `alert`), so it isn't announced.
    - "Error 500: Something went wrong" is unhelpful. It also doesn't say which invoice failed or what to do.
    - `fetch` doesn't reject on HTTP 500, so `.catch` only fires on network failure and this message would rarely appear. You need to check `response.ok`.
    
    *Fix:* use a persistent, dismissible, announced message such as "Couldn't save invoice 8f3a-22c1. Try again."

14. **Modal handling is risky.** Two stacked modals ("Confirm" opens a second) are confusing. Check these:
    - Focus must be trapped and returned to the trigger.
    - Esc must close the modal.
    - Use `role="dialog"`, `aria-modal` and a label.
    - `location.hash = ''` in `openInvoice` can scroll to the top or break back-button behaviour.
    
    *Fix:* merge the confirmation into one step, or use inline confirmation.

## P2: Moderate

15. **Long vendor names have no overflow strategy.** "Globex International Holdings Private Limited (Asia Pacific Region)" will wrap, or break the layout. Use truncation with a tooltip or `title`, or let the column wrap with a sensible `min-width`.

16. **Amount formatting is inconsistent.** `1200.5` and `87` show no currency, no thousands separator and no fixed decimals. Use `Intl.NumberFormat` (e.g. "$1,200.50"), and right-align.

17. **The IDs are opaque** (`8f3a-22c1`) and may be hard to scan or copy. Consider showing a short invoice number or date, and make the ID selectable.

18. **No empty, loading or error states.** The table is hardcoded. There's also no sorting, filtering or pagination, and "Showing all invoices" gives no count. Say "Showing 2 invoices", and add search once the list grows.

19. **Page structure is weak.**
    - There's no `lang` on `<html>`, no viewport meta, and a generic `<title>` ("App").
    - There's no `<main>` or `<header>` landmark (the header is a `div`).
    - The comment `down. -->` before `<html>` is a stray fragment.
    - The sticky header has a fixed 72px height and doesn't offset anchor or focus scroll targets. Use `scroll-padding-top` so focused elements aren't hidden (WCAG 2.4.11).
    - The `<h2>` appears with no `<h1>`.

20. **Fixed sizes may not reflow.** Fixed pixel heights and no responsive rules suggest poor behaviour at 320px width or 200% zoom (WCAG 1.4.10).

## P3: Polish

21. Emoji icons render differently across platforms. Use a consistent SVG icon set.
22. The form has no `<form>` element, so Enter doesn't submit. Wrap the inputs and use `type="submit"`.
23. The `font-family: sans-serif` is generic. Add spacing, hover and active states, and a consistent button style. The muted text and the plain buttons look unfinished.
24. Add `autocomplete` attributes where relevant, and `prefers-reduced-motion` handling for the spinner.

## Suggested fix order
1. Loader, focus outlines, row and button semantics (items 1, 2, 4, 5).
2. Destructive confirmation and error handling (items 3, 6, 9, 13).
3. Labels, status and contrast (items 7, 10, 11).
4. Table semantics, modals, then the P2 and P3 polish.

I can turn this into a corrected HTML version if you'd like.
