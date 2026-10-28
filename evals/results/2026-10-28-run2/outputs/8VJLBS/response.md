The board is written to `/tmp/ux-run2/8VJLBS/kanban.html`. I haven't run it in a browser or screen reader. The syntax check was denied, so I haven't confirmed the script parses either.

It has four columns (New, In progress, Waiting, Done), six sample tickets, and an "Add ticket" form.

## Accessibility decisions

- **Three ways to move a ticket.**
  - Mouse drag works, but dragging alone fails WCAG 2.5.7 (dragging movements) and doesn't work on touch.
  - A native "Move to" `<select>` on every card works with any assistive technology and on touch.
  - A "Reorder" button gives keyboard drag. Press <kbd>Space</kbd> to pick up, use the arrow keys to move across columns or up and down, press <kbd>Space</kbd> to drop, or <kbd>Esc</kbd> to cancel and return the ticket to where it started.
- **Keyboard drag state is exposed.** The Reorder button uses `aria-pressed`, and the picked-up card is also highlighted visually. Focus moves away from the button and the ticket is dropped, so it can't get stuck "held".
- **Moves are announced.** A polite `role="status"` live region reads out pick-up, each move, drop, cancel, and "can't move further". It reports position as "position 2 of 4 in Waiting". Focus stays on the control you used after every move, even though the board re-renders.
- **Semantic structure.**
  - Each column is a `<section>` labelled by its `<h2>`, which includes a visually hidden "tickets" count.
  - Cards sit in real `<ul>`/`<li>` lists, with the ticket title as an `<h3>`.
  - Screen-reader users can jump by heading or landmark and hear "list, 3 items".
  - A skip link jumps to the board.
- **Visible labels and names.**
  - Every control has a real `<label>` or a hidden suffix with the ticket name, so "Move to" and "Reorder" aren't ambiguous across cards.
  - The add form's validation error is inline, linked with `aria-describedby`, marked `aria-invalid`, announced via `role="alert"`, and focus returns to the field.
- **Not colour alone.** Priority shows as text ("High priority") as well as a colour. Drop targets use a dashed outline and an insertion bar, not just a tint.
- **Visual robustness.**
  - Colours were chosen for AA contrast in both light and dark (`prefers-color-scheme`).
  - `:focus-visible` outlines are 3px.
  - Controls are at least 44px tall.
  - The grid reflows to one column on narrow screens with no horizontal scrolling.
  - Transitions respect `prefers-reduced-motion`.
  - Forced-colors (high contrast) mode gets system-colour outlines.
- **Instructions in the page.** The keyboard instructions are visible, and each Reorder button references them through `aria-describedby`.

The mouse drag uses the browser's built-in HTML5 drag-and-drop, which doesn't fire on touch screens. Touch users rely on the "Move to" menu.
