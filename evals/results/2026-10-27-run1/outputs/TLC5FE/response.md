I wrote the board to `/tmp/ux-eval-e7/TLC5FE/support-kanban.html`. It's one file with no dependencies and has not been run. My attempt to syntax-check the script was blocked, and I haven't opened it in a browser or tested it with a screen reader. Please try the drag, keyboard and Move… paths before relying on it.

**Accessibility decisions**

- **Three ways to move a ticket.** WCAG 2.5.7 says dragging can't be the only way.
  - **Pointer drag:** mouse, pen or touch. On touch you drag by the grip handle, so scrolling the page still works.
  - **Keyboard grab mode:** focus the grip button and press Space to pick up. Arrow keys change column or reorder. Space or Enter drops, and Esc puts the ticket back.
  - **Move… button:** it opens a native `<dialog>` with a radio group of columns. This works with a single click or tap, voice control and switch devices.
- **Screen reader announcements.** A polite live region announces each pick-up, move, drop and cancel with the ticket's new position, for example "Moved TCK-103 to Waiting, position 2 of 3."
- **Structure.** Each column is a labelled `<section>` with an `<h2>`, and each ticket title is an `<h3>`, so heading navigation works. The lists use an explicit `role="list"`, and the count is read as "3 tickets." Empty columns show text, and there is a skip link to the board.
- **Real buttons and labels.** The grip is a `<button>` with `aria-pressed`. Its label names the ticket, and `aria-describedby` points to the keyboard instructions. Every form field has a label. An empty subject shows an inline error, sets `aria-invalid` and moves focus to the field.
- **Focus.** Focus returns to the moved ticket after every move, including after the dialog closes. Dropping on Tab or on a click elsewhere avoids leaving a ticket stuck in grab mode.
- **Not just colour.** Priority shows an icon shape plus text. The picked-up ticket gets a thick dashed outline and visible "Picked up" text. The drop target gets a dashed outline and a drop-position bar.
- **Visual.** Text and controls are meant to meet WCAG AA contrast in both light and dark, though I haven't measured it. Buttons and inputs are at least 44px tall, and focus rings are 3px. Layout reflows from four columns to one with no horizontal scroll. It also handles forced-colors mode and `prefers-reduced-motion`.
- **Persistence.** Tickets are saved to `localStorage`, wrapped in try/catch. The page works without it.

The "How to move tickets" disclosure at the top gives sighted keyboard users the same instructions that screen reader users hear.
