# Audit: Vendor Invoices (Acme Ops Console)

**Job assumed:** an ops or finance user reviews, edits and deletes vendor invoices many times a day. Money and destructive actions are involved. I read the code only and did not run it. The `.grid` and `.row` classes have no CSS, so I can't judge the layout, only the markup.

## P0: Blockers (data loss, no access, or unusable)

1. **"Delete All" has no confirmation, no undo and no permission check.**
   - `deleteAll()` fires `DELETE /api/invoices` on one click.
   - It sits as an ordinary button right under the table, with no count and no consequence stated.
   - Fix: name the count in the label, e.g. "Delete 2 invoices…". Open a dialog that states the object, the count and that it can't be undone. For a bulk wipe, require a typed confirmation. Better still, replace it with selection plus bulk delete and an Undo toast.
2. **Per-row delete (`del`) is also instant and silent.**
   - The 🗑 button sits 0px from 💾.
   - The 16px targets make a mis-click likely, and nothing is shown afterwards.
   - Fix: delete, then show "Invoice 8f3a-22c1 deleted · Undo". Move delete into a "⋯" menu away from Save (Fitts's Law).
3. **The full-screen loader never goes away and blocks everything.**
   - `#loader` is `position: fixed; inset: 0` and no script ever removes it.
   - It has transparent or no background, so it overlays the page and may swallow every click. Content shows through it.
   - It has no `role="status"` and no spinner. Fix: remove it when loading completes, show skeleton rows in the table instead, and announce loading politely.
4. **Keyboard focus is removed everywhere.**
   - `button:focus, input:focus, a:focus { outline: none; }` fails WCAG 2.4.7 (Focus Visible) and 2.4.11.
   - Fix: delete the rule and style `:focus-visible` with a ≥3:1 contrast ring.
5. **The table is not keyboard or screen-reader accessible.**
   - It is built from `div`s and `span`s, so there is no table, row or column-header semantics (1.3.1).
   - Rows open a modal through `onclick` on a `div`. It isn't focusable and has no key handler (2.1.1).
   - Fix: use a real `<table>` with `<th scope>`, and put a real link or button in the ID cell to open the invoice.
6. **Row buttons bubble clicks to the row.**
   - Clicking 💾 or 🗑 also fires the row's `openInvoice`, so every Save or Delete opens a modal behind or over it.
   - Fix: `event.stopPropagation()`, or better, drop the row-level click (see 5).
7. **Icon buttons have no accessible names.** The 💾 and 🗑 emoji buttons have no `aria-label` (4.1.2, 1.1.1). Screen readers read emoji names or nothing. Add `aria-label="Save invoice 8f3a-22c1"` and a tooltip.

## P1: Serious (errors, lost input, WCAG failures)

8. **The form wipes input on every click.** The submit handler clears all inputs, regardless of success or failure. That breaks "never lose user input" and WCAG 3.3.7. Clear only after a successful save, and keep values on error. It also doesn't call the API at all, so the form does nothing.
9. **The Submit button is permanently `disabled`.**
   - Nothing ever enables it, and a disabled button gives no reason why.
   - Fix: keep it enabled and validate on submit, or explain what is missing. Name it "Add invoice", not "Submit".
10. **Form labels and errors are inadequate.**
    - Inputs have only `placeholder`s, which vanish on typing and have poor contrast. Use visible `<label>`s (3.3.2, 1.3.1).
    - "Amount" should be `inputmode="decimal"` with a currency shown.
    - The error "Invalid input" is always visible, even before any input, is unlinked to a field, doesn't say which field or why, and isn't announced.
    - Fix: show field-level errors only after validation. Link them with `aria-describedby` and `aria-invalid`. Say what is wrong and how to fix it, e.g. "Enter an amount like 1200.50." Put the summary in a `role="alert"` region.
11. **Status is conveyed by colour alone.**
    - ● green versus ● red fails WCAG 1.4.1, and the colours are invisible to many colour-blind users.
    - Fix: use text plus an icon, e.g. "Paid" or "Overdue" in a badge. Also check contrast: `#2e9e44` on white is about 3.4:1, so it fails 4.5:1 for text.
12. **Several colours fail contrast on white.**
    - `.muted` `#b5b5b5` is about 2:1 (needs 4.5:1).
    - `#d64545` is about 4.1:1, so it fails for small text.
    - Placeholder text is typically below 4.5:1 as well.
13. **Error handling is inaccurate or missing.**
    - `save` only catches network failure. `fetch` doesn't reject on HTTP 4xx or 5xx, so server errors pass as success.
    - `del` and `deleteAll` have no handling at all.
    - There is no success feedback for any action.
    - The toast text "Error 500: Something went wrong" is jargon with no recovery step.
14. **Toasts are inaccessible and too short.**
    - The toast is a bare `div` with no `role="status"` or `alert`, so nothing is announced.
    - It disappears after 2s, which fails WCAG 2.2.1.
    - It has no styling, position or dismiss control, and no way to retry.
    - Fix: use a live region, ≥6s or persistent for errors, with a Retry action.
15. **Modals are unspecified and risky.**
    - The comment says a second modal opens from "Confirm", so stacked modals.
    - Needed: `role="dialog"`, `aria-modal`, a focus trap, Esc to close, focus returned to the trigger, and background `inert`.
    - Avoid stacking by using an inline confirm step.
    - Also, `openInvoice` sets `location.hash = ''`, which wipes any state in the URL. Instead the open record should be in the URL (e.g. `#/invoices/1`) so it is linkable and Back works.
16. **The page is missing basic structure.**
    - There is no `lang` attribute on `<html>` (3.1.1) and no viewport meta, which breaks mobile and zoom (1.4.4, 1.4.10).
    - There is no `<main>`, `<nav>` or `<header>` landmark, and no skip link.
    - The title "App" is useless. Use "Vendor invoices – Acme Ops Console".
    - The header is a `div` with a bold tag rather than a heading or banner.
    - Also remove the stray `down. -->` text, which will render on the page.

## P2: Moderate (usability gaps)

17. **Targets are too small.** `.icon-btn` is 16×16px. WCAG 2.5.8 requires at least 24×24px, and 32–44px is better for frequent use. Add spacing between Save and Delete.
18. **Number formatting is wrong.**
    - Amounts show as `1200.5` and `87`, with no currency, no thousands separator and no fixed decimals.
    - Fix: `$1,200.50`, `$87.00`, right-aligned with tabular numerals. `td.num { text-align: center }` is the wrong alignment (and targets a `td` that doesn't exist).
19. **Long vendor names are not handled.**
    - "Globex International Holdings Private Limited (Asia Pacific Region)" will break the row layout.
    - Fix: truncate with ellipsis plus a tooltip or full text in the detail view, or wrap sensibly.
20. **The table lacks every standard capability.**
    - No sorting, filtering, search or pagination, and none of it is in the URL.
    - "Showing all invoices" tells the user nothing. Show "Showing 1–25 of 312".
    - There is no row selection, so bulk actions need it.
    - The ID column is a raw UUID fragment that users can't scan. Show a human invoice number and date.
    - Missing invoice fields: due date, currency, and a status label.
21. **Missing states.**
    - Empty (first use versus zero results), loading, error and no-permission states all lack designs.
    - Nothing handles a viewer role: Save and Delete should be hidden or disabled with a reason.
22. **The header is sticky but overlaps content.**
    - It is 72px tall and sticky, but content has no scroll padding, so anchored elements and focused fields can hide behind it (WCAG 2.4.11).
    - Add `scroll-padding-top: 72px`, and give the header a real nav and user menu.
23. **Save is unclear.** The 💾 per row implies inline editing, but the cells aren't editable. What gets saved? `PUT` sends no body. Decide whether rows edit inline or in the modal.

## P3: Polish

- Use a dedicated "Add invoice" action with a modal or page, rather than loose inputs above the table.
- Style the buttons: a clear primary, a secondary, and a danger variant for destructive actions.
- Use semantic headings: the `h2` appears with no `h1`.
- Respect `prefers-reduced-motion` for the spinner, and support dark mode and high-contrast modes.
- Add keyboard shortcuts for frequent actions, once the basics work.

## Suggested order of work

1. Fix the loader and the broken form (items 3, 8, 9), so the screen works at all.
2. Make destructive actions safe (1, 2, 6, 13), with confirmation and Undo.
3. Restore focus styles, add real table semantics, names and labels (4, 5, 7, 10).
4. Fix colour, contrast and status text (11, 12).
5. Add error and success feedback, then modals and URL state (13–15).
6. Do the remaining structure, states and table features (16–23).

I can rewrite the page with these fixes applied if you want. That would be one file with a real table, a confirm dialog and Undo.
