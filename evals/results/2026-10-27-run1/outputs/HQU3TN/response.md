I wrote the board to `/tmp/ux-eval-e7/HQU3TN/kanban.html`. I haven't run it in a browser, and the syntax check was blocked, so none of it is tested. Open it in a browser and try the drag, keyboard and screen-reader paths before relying on it.

It has four columns (New, In progress, Waiting, Done), seeded with five sample tickets, and an "Add ticket" form that puts new tickets in New. The board saves to `localStorage`.

**Accessibility decisions**
- **Three ways to move a ticket, so drag isn't required.**
  - Mouse drag-and-drop works, but HTML5 drag doesn't work on touch or with a keyboard.
  - Every ticket has a native "Move to" `<select>`, which covers touch, voice control and screen readers.
  - Every ticket has a "Reorder" button for keyboard use. Space or Enter picks the ticket up, arrow keys move it between columns or up and down, Space drops it, and Escape cancels and puts it back. The button uses `aria-pressed` to show whether the ticket is held.
- **Screen-reader announcements.** A polite live region says what happened, for example "Ticket 103 … In progress, position 2 of 3." It does this for pick-up, moves, drops, cancels, blocked moves and new tickets.
- **Structure.** Each column is a labelled `<section>` with an `<h2>` that includes a visually hidden "tickets" after the count. Tickets are `<li>` items in a `<ul>`, so a screen reader announces "list, 3 items". Each ticket is an `<article>` with an `<h3>`. A skip link jumps to the board.
- **Focus management.** The board is rebuilt after each move, so the code puts focus back on the moved ticket's control. Without that, keyboard and screen-reader users would be dropped to the top of the page. Tabbing away mid-grab drops the ticket and leaves focus where you moved it.
- **Not colour alone.** Priority shows as text ("Priority: High"). The picked-up ticket has a thicker outline plus the pressed state. The drop target has a dashed outline and a tinted background.
- **Visuals.** Focus rings are 3px. Contrast should meet WCAG AA in both light and dark mode, though I haven't measured it. Controls are at least 36px tall. Forced-colors mode is handled. The layout stacks to one column on narrow screens and doesn't scroll sideways. Animation is used only when the user hasn't asked for reduced motion.
- **Plain controls.** Every input has a visible `<label>`, there are no custom widgets, and instructions are linked to the buttons with `aria-describedby`.
