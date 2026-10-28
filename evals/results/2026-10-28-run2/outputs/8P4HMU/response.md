# UX and accessibility review: Vendor Invoices screen

**Job:** an ops/finance user triaging, editing and deleting vendor invoices. They probably do this many times a day, with real money at stake.

## Top 3 problems

**1. Destructive actions have no safety net (Critical)**
- `Delete All` and the 🗑 button fire `fetch(DELETE)` immediately. There is no confirmation, no undo, no loading state and no feedback.
- `Delete All` sits unguarded at the bottom of the page, next to nothing that explains its scope. It would wipe every invoice.
- A row-level delete next to a save button, in a 16px target, will get mis-clicked. Hitting the row as well opens a modal, because the click bubbles.
- **Fix:**
  - Name the object and the count in the confirmation, for example "Delete invoice 91bd-07aa (Globex…, 87.00)?" or "Delete all 2 invoices?".
  - For Delete All, require typing the count or "DELETE".
  - Prefer soft-delete with an undo toast.
  - Put bulk delete behind row selection and an overflow menu, not a loose page-level button.
  - Check the response, and show success or failure.
  - Add permission handling: disable with a tooltip explaining why.

**2. Keyboard and screen-reader users are locked out (Critical, WCAG 2.4.7, 2.1.1, 4.1.2)**
- `button:focus, input:focus, a:focus { outline: none; }` removes all focus indication, with no replacement.
- Rows are `div`/`span` with `onclick`. They can't be focused, aren't announced as interactive, and have no Enter or Space handling. Opening an invoice is mouse-only.
- The grid is built from divs with no `role="table"`, `row`, `columnheader` or `cell` roles. A real `<table>` would be better, since `td.num` CSS already exists for one.
- The icon buttons contain only emoji, so they have no accessible name. Screen readers will read "floppy disk" and "wastebasket", or nothing.
- The inputs have only placeholders as labels. The placeholder disappears on typing and has poor contrast.
- The loader and error have no live region.
- **Fix:**
  - Use a visible `:focus-visible` ring (2px, 3:1 contrast).
  - Use real `<table>`, `<th scope>` and `<label>` elements.
  - Make the vendor name a link or button that opens the invoice, and stop propagation on the action buttons.
  - Add `aria-label="Save invoice 8f3a-22c1"` on the icon buttons.
  - Use `role="status"` for the loader and toasts, and `role="alert"` for errors.

**3. The form destroys user input and gives no guidance (High)**
- The Submit click handler wipes every input unconditionally, even on error. That breaks the "never lose user input" rule.
- Submit is `disabled` with no explanation of what's missing.
- "Invalid input" is permanently visible, before any interaction. It is red only (colour alone), generic, not tied to a field, and not announced.
- The Amount field is a plain text input with no numeric type, format or currency.
- Nothing is actually submitted, so there is no success or failure path.
- **Fix:**
  - Keep values on failure and clear only on success.
  - Show inline per-field errors only after blur or submit, for example "Amount must be a number, like 1200.50".
  - Link each error with `aria-describedby` and mark the field `aria-invalid`.
  - Use `inputmode="decimal"` and a currency hint.
  - Keep Submit enabled and validate on click, or say why it's disabled.
  - Rename Submit to "Add invoice".

## High priority

- **Loader never goes away, and blocks the page.** `.spinner-page` is `position: fixed; inset: 0` with no background, no removal logic and no `aria-busy`. It overlays the content, intercepts clicks and shows plain "Loading…" text. Remove it on load, or use skeleton rows and a non-blocking indicator. Add timeout and error states.
- **Status is communicated by colour only.** Both statuses are a "●" in green or red. That fails WCAG 1.4.1 and is invisible to colour-blind users. The meaning is also never stated. Use a labelled badge such as "Paid" or "Overdue" with an icon. The green `#2e9e44` on white is about 3.5:1, which also fails for text.
- **Error toast is poor.** "Error 500: Something went wrong" is a dead end: it says nothing about why or what to do, and has no reference ID.
  - It disappears after 2s, which is too short to read (WCAG 2.2.1), is not announced, and has no styling or position.
  - `.catch` also only fires on network failure. A 500 response resolves the promise, so the error toast never shows for server errors.
  - Delete has no error handling at all.
  - Fix: use `res.ok` checks, persistent errors with dismiss, a retry action, and `role="alert"`.
- **Two stacked modals with no specified focus management.** On open, focus should move into the modal. It needs a focus trap, Esc to close, and focus should return to the trigger. `aria-modal` and `role="dialog"` are also needed. Prefer a side panel or inline confirmation over a second modal.
- **`openInvoice` clears `location.hash`.** This destroys state in the URL. The open record should be deep-linkable (`#/invoices/8f3a-22c1`), and Back should close the modal.

## Medium priority

- **Numbers.** They're centre-aligned, unformatted (`1200.5`, `87`) and have no currency. Right-align them, use `tabular-nums`, fix 2 decimals, and show the currency (`1,200.50`, `87.00`).
- **Long vendor name.** "Globex International Holdings Private Limited (Asia Pacific Region)" has no truncation rule. Use ellipsis with the full value in a tooltip, and set column widths.
- **Tap targets.** The icon buttons are 16×16px. WCAG 2.2 (2.5.8) wants at least 24px, and 32–44px is practical. Save and delete are adjacent, which makes errors likely. Show a Save button only when a row is dirty, and move delete into a `⋯` menu.
- **No table essentials.** There is no sort, filter, search, pagination or selection, and "Showing all invoices" would not hold for thousands of rows. Add the empty, no-results and error states, and a row-count label ("2 of 2 invoices").
- **Raw IDs.** `8f3a-22c1` is shown in full. It's fine as a monospace, copyable reference, but make it secondary to vendor name or invoice number.
- **No `<html lang>`, viewport meta or `<main>`/`<h1>`.** The title is just "App", and `<h2>` is the first heading. The doc also starts with a stray comment fragment (`down. -->`) before `<html>`, which puts the browser in quirks mode. Add `<!doctype html>`, `lang="en"`, a viewport meta tag, a landmark structure and a meaningful title.
- **Sticky header.** The header is fixed at 72px, but nothing offsets in-page anchors or focus (scroll-padding), and the header holds only the app name. It has no nav landmark, user menu or environment indicator.

## Low priority

- `.muted` text (`#b5b5b5` on white, about 2:1) fails the 4.5:1 minimum. It should be about `#767676` or darker.
- The "Showing all invoices" copy is vague. Make it a count plus the active filters.
- The emoji icons render inconsistently across platforms. Use an SVG icon set with accessible labels.
- Add a unit and a size to the base font (`sans-serif` and no size). Add `box-sizing`, and use a spacing scale rather than the default margins.
- Add a `<caption>` or an accessible name for the table.
- Consider optimistic updates with rollback, and disabled and pending states on save and delete so double-clicks can't double-submit.
- Confirm that there's a permissions design for view-only users.

## Audit summary

Checked against the enterprise checklist: states (empty, loading and error are missing or broken), destructive-action safety (fail), permissions (not designed), data formatting (fail), input preservation (fail), URL state (fail), keyboard and focus (fail), status and colour (fail), copy specificity (fail). The three critical and high items above should be fixed first, in the order listed.

I can rewrite this as a corrected, accessible version if that would help.
