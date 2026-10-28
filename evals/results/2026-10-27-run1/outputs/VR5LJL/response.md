I wrote the board to `/tmp/ux-eval-e7/VR5LJL/kanban.html`. I haven't opened it in a browser or run any checks on it. A syntax check on the script was blocked by a permission prompt, so it's untested.

Open the file in a browser. It has four columns (New, In progress, Waiting, Done), seven sample tickets, and an "Add ticket" form.

## Accessibility decisions

- **Three ways to move a ticket.**
  - **Pointer:** drag with a mouse or finger.
  - **Keyboard:** the same move works from the keyboard.
  - **Move button:** each ticket has a "Move…" button that opens a dialog with the columns as radio buttons. This is the alternative for people who can't drag at all (WCAG 2.5.7), and it also works for voice control and switch users.
- **Keyboard drag follows the usual pick-up and drop pattern.**
  - Space or Enter picks up a ticket.
  - Left and Right change column, and Up, Down, Home and End reorder it within the column.
  - Space or Enter drops it, and Escape puts it back.
  - Moving away from a held ticket (tab or click elsewhere) drops it where it is.
  - Pick-up uses the button's `click` event, so it also works with screen-reader activation, not just physical key presses.
- **Screen readers hear every step.** A polite live region announces each change, for example "TCK-103 now in Waiting, position 2 of 3." Pick-up, drop, cancel and "already at the top" are announced too. The grab button reports its state with `aria-pressed`, and focus returns to the moved ticket after every change.
- **Semantic structure.** The page has `main`, an `h1`, and one `section` per column labelled by its `h2`. The `h2` includes the ticket count, and each column's ticket list uses the same label. Empty columns say "No tickets". Dialog focus handling comes from the native `<dialog>`.
- **Nothing relies on colour alone.**
  - Priority shows as a shape plus a word (▲ High, ■ Medium, ▼ Low).
  - A grabbed ticket gets a dashed border and a visible "Grabbed" message.
  - Drop positions show as a dashed placeholder.
  - Text and borders are meant to meet WCAG AA contrast, but I haven't measured them. There is a dark theme through `prefers-color-scheme`, and forced-colors (high-contrast) mode is handled.
- **Visible focus and target size.** There is a 3px `:focus-visible` outline, and every control is at least 44px high. The grab handle sets `touch-action: none` so touch dragging doesn't fight page scrolling.
- **Forms and reflow.** Every input has a visible `<label>`. An empty title gets an error message linked with `aria-describedby` and `aria-invalid`, and focus moves back to the field. The columns stack at narrow widths, so the page works at 320px or 400% zoom with no horizontal scroll. Sizes are in `rem`, so text scaling works.
- **Pointer drags can be cancelled.** Escape cancels a drag in progress, and nothing moves until the pointer is released.

A real screen-reader pass (NVDA, VoiceOver) is still worth doing, because announcement timing differs between them.
