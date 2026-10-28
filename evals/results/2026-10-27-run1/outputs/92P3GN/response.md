**Context:** This is an ops console for reviewing and managing vendor invoices, probably used many times a day, with money at stake. Safety and clarity matter most.

## Top 3 (fix first)

**1. A full-screen loader that never goes away, and it blocks everything.**
- `.spinner-page` is `position: fixed; inset: 0`, and nothing ever removes `#loader`.
- It covers the page and intercepts every click. It has no background, so the page shows through the text, and no `role="status"` or `aria-live`.
- **Fix:** hide it when data arrives, and give it `role="status"`. Prefer skeleton rows inside the table over a page-level blocker. Add an error state with Retry for when loading fails.

**2. Destructive actions are unsafe.**
- **No confirmation:** "Delete All" and the per-row 🗑 call `fetch(DELETE)` immediately, with no confirmation, no undo and no count. One misclick wipes every invoice.
- **No feedback:** `del` and `deleteAll` don't check the response or update the UI.
- **Misclick risk:** "Delete All" sits in the same visual weight as everything else.
- **Row-click collision:** the buttons sit inside a row with `onclick="openInvoice"`. Clicking Save or Delete also opens the modal, because there is no `stopPropagation`.
- **Fix:**
  - Use a confirmation that names the object and count: "Delete invoice 91bd-07aa (Globex, 87.00)?" or "Delete all 2 invoices?". For "all", require typing the count.
  - Prefer soft-delete with an Undo toast.
  - Make the button label say what it does ("Delete all invoices"), give it danger styling, and move it away from the normal controls.
  - Add `stopPropagation` on the row buttons.
  - Gate the actions by permission.

**3. The form destroys input and gives no useful error.**
- **Input wiped:** the Submit click handler clears every input unconditionally, so the user's data is lost whether or not it was valid.
- **Disabled forever:** the button is `disabled` with no explanation and nothing ever enables it.
- **Unhelpful error:** "Invalid input" is always visible. It doesn't say which field or why, and it isn't tied to a field or announced to screen readers.
- **Unlabelled fields:** the inputs have placeholders only, so there's no persistent label. The label vanishes on typing and fails WCAG 1.3.1 and 3.3.2.
- **Fix:**
  - Add real `<label>`s.
  - Keep the values on error.
  - Show a per-field message ("Amount must be a number, e.g. 1200.50") with `aria-describedby` and `aria-invalid`.
  - Keep the error hidden until there is one, and give it `role="alert"`.
  - Use an enabled button that validates on submit, or explain why it's disabled.
  - Use a specific verb: "Add invoice".
  - Give Amount `inputmode="decimal"` and a currency.

## Accessibility blockers (high)

- **Focus is removed.** `button:focus, input:focus, a:focus { outline: none }` leaves keyboard users unable to see where they are (WCAG 2.4.7). Delete the rule, or replace it with a visible `:focus-visible` ring.
- **Rows are mouse-only.** `div onclick` has no role, tabindex or key handler, so keyboard and screen-reader users can't open an invoice. Make the ID a real link or button, and keep the row click as a convenience only.
- **Icon buttons have no accessible name.** 💾 and 🗑 are emoji with no `aria-label`. They are announced inconsistently, and Save and Delete are indistinguishable between rows. Use `aria-label="Delete invoice 91bd-07aa"`.
- **Touch targets are too small.** `.icon-btn` is 16×16. WCAG 2.5.8 requires at least 24px, and 32–44px is better. Add padding, and space Save and Delete apart so a misclick is less likely.
- **Status is colour-only.** The ●s are red or green with no text, which fails WCAG 1.4.1 and excludes colour-blind users. Use a label such as "Paid" or "Overdue", plus an icon.
- **Low contrast.**
  - `.muted` #b5b5b5 on white is about 2:1, so it fails 4.5:1.
  - `.status-ok` #2e9e44 is about 3.4:1, which fails for text.
  - Darken both.
- **Table is not a table.** The `.grid`/`.row` divs have no CSS at all, so the layout is unstyled. They also have no semantics: use `<table>` with `<th scope="col">`, or add `role="table"` and the matching row and cell roles. The empty `<span></span>` header needs a visually hidden "Actions".
- **Toast is not announced.** The error toast is a bare `div` with no `role="status"` or `role="alert"`. It also vanishes after 2s, which is too short to read and violates WCAG 2.2.1 (time limits). Use at least 5–8s, pause on hover, and add a dismiss button.
- **Modals are unspecified.**
  - Opening a modal from inside a modal is a stacked-dialog antipattern. Replace the second one with an inline confirmation step.
  - Whatever you build needs `role="dialog"`, `aria-modal`, a focus trap, Esc to close, and focus returned to the trigger.
  - `location.hash = ''` clears state, so the open record is not in the URL and can't be shared or restored with Back.
- **Page structure.**
  - The `<html>` has no `lang`. The document has no `<meta viewport>` (breaks mobile), no `<main>`, no `<nav>` and no skip link.
  - There is a stray "down. -->" fragment before `<html>`.
  - The `<title>` "App" is meaningless: use "Vendor Invoices – Acme Ops Console".
  - The sticky header has a fixed 72px height and is not a `<header>` landmark. A sticky header can also obscure focused elements (WCAG 2.4.11), so add `scroll-padding-top`.

## Data and layout (medium)

- **Numbers.** Amounts are centred (`td.num`, which doesn't even match `<span>`s), unformatted (`1200.5`, `87`) and have no currency. Right-align them, use `font-variant-numeric: tabular-nums`, use a fixed 2 decimals and show the currency, e.g. `1,200.50 USD`.
- **Long values.** The Globex name will wrap or break the layout. Truncate with an ellipsis and give the full name in a `title` or tooltip. Set min and max column widths.
- **Silent failures.**
  - `save` only handles network errors. `fetch` doesn't reject on a 500, so the error toast almost never fires.
  - The toast text "Error 500: Something went wrong" is hard-coded and not actionable. Say what failed and what to do ("Couldn't save invoice 8f3a-22c1. Your changes are still here. Try again").
  - There is no success feedback for Save, and no unsaved-state indication. Check `res.ok`.
- **Row save.** A per-row Save button implies inline editing, but nothing is editable. Remove it or make the editing explicit.
- **Missing table features.**
  - There is no empty state, loading state or error state, so a blank list is a bug.
  - The footer says "Showing all invoices" without a count, sort, filter, search or pagination. That won't survive hundreds of rows.
  - There is no way to find an invoice or filter by status.
  - There is no selection, so the only bulk action is "delete everything".
  - Sort, filter and page should live in the URL.
- **Header.** "Acme Ops Console" is bold text with no navigation, no user menu and no link home.
- **Page layout.** The content sits full-width against the viewport edge with no padding or container, and there is no primary action hierarchy.

## Suggested fix order

1. Remove or resolve the blocking loader.
2. Add delete confirmation or undo, and stop the row-click propagation.
3. Restore focus outlines.
4. Make the form retain input and give field-level errors.
5. Fix semantics: labels, button names, table, keyboard access to rows.
6. Fix contrast, status text and target sizes.
7. Fix number formatting, truncation, response handling, and the empty, loading and error states.
8. Add search, filter and pagination state in the URL.

**Audit summary:** I read the code only and didn't run it in a browser, so the contrast ratios are estimates. I checked every state against the enterprise checklist (empty, loading, error, permission, overflow), destructive-action safety, keyboard access, WCAG 2.2 A and AA basics, number and text alignment, and data-loss risks. Permissions and URL state are both absent. I haven't proposed code yet, but I can produce a corrected version if you'd like.
