I couldn't run a syntax check on the script, because the command needed approval and I didn't retry it. So the board is written but untested in a browser.

The file is `/tmp/ux-run2/0SZBHN/kanban.html`. It has four columns (New, In progress, Waiting, Done), six sample tickets and an "Add ticket" form. It works with mouse drag, keyboard and a menu.

## Accessibility decisions

- **Dragging isn't the only way to move a ticket** (WCAG 2.5.7). Every ticket has a native **"Move to" select** and a **keyboard "Move" button**. The select also works with touch, voice control and screen readers.
- **Keyboard moving**
  - **Pick up and drop:** pressing Move picks the ticket up. The button shows this with `aria-pressed`, a filled style and a border.
  - **Moving:** ←/→ change column and ↑/↓ reorder. Enter or Space drops the ticket, and Esc puts it back.
  - **Focus:** it stays on the same ticket after every move, even though the board redraws.
  - **Walking away:** tabbing off a picked-up ticket drops it where it is.
- **Screen reader announcements**
  - **Live region:** a polite live region says things like "Picked up X", "In progress, position 2 of 3", "Move cancelled" and "Ticket added".
  - **Edges:** it also says when you're at an edge, for example "No column in that direction" or "Already at top".
- **Structure**
  - **Page layout:** each column is a labelled `section` with an `h2` that includes the ticket count, and each ticket is a list item with an `h3`. Screen reader users can jump by heading or region.
  - **Instructions:** the keyboard instructions are visible text, and each Move button points to them with `aria-describedby`.
- **Accessible names**
  - **Move buttons:** they read "Move: <title>", which keeps the visible word "Move" in the name for voice control.
  - **Selects:** each has a real `<label>` with the ticket title added as hidden text, so "Move to" isn't repeated identically on every card.
- **Visual**
  - **Priority:** it is written out ("High priority") rather than shown only by color.
  - **Colors and focus:** text uses high-contrast colors with a dark theme. Focus rings are a 3px outline, and picked-up and drop-target states have borders as well as color.
  - **Forced colors:** forced-colors (high-contrast) mode has its own styles.
  - **Touch targets:** all controls are at least 44px.
  - **Motion:** transitions switch off for `prefers-reduced-motion`.
  - **Small screens:** below 900px the columns stack into one column instead of scrolling sideways.
- **Forms:** the add form uses visible labels, `required` on the title, and returns focus to the title field after adding.

**Known limitation:** mouse drag uses the HTML5 drag-and-drop API, which doesn't work on touch screens. Touch users use the "Move to" menu instead. I haven't tested with a real screen reader.
