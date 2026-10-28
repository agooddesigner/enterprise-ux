I wrote the board to `/tmp/ux-run2/UL95UQ/kanban.html`. It's one file with no dependencies and it has the four columns (New, In progress, Waiting, Done). I couldn't run it: the syntax check on the script was blocked, and I didn't open it in a browser. Please try the mouse drag, the keyboard moves and a screen reader before you rely on it.

**Accessibility decisions**

- **Dragging isn't the only way to move a ticket.** Mouse drag-and-drop excludes keyboard, screen-reader, voice and many touch users. Each ticket has two other routes, which satisfies WCAG 2.5.7 (dragging movements).
  - **Keyboard:** the **Reorder** button picks the ticket up. ←/→ change column, ↑/↓ change position, Space or Enter drops it, and Esc puts it back where it started.
  - **Move to list:** a **Move to** list with a **Move** button works on any device. It's a separate button because moving a ticket as soon as you arrow through the list would change the page unexpectedly (WCAG 3.2.2) and drop focus.
- **Structure is semantic.** Each column is a `<section>` labelled by its `<h2>`. Tickets are `<li>`s in a `<ul>` with an `<h3>` title, so screen-reader users can jump by heading or list. The ticket count in each heading is read as "3 tickets". An empty column shows "No tickets. Drop one here."
- **Every move is announced.** A polite live region says "Picked up T-101… Moved to In progress, position 2 of 3… Dropped." It also reports when you hit an edge ("Already in the last column").
- **Focus is kept after a move.** The board redraws after each move, so I put focus back on the control you were using. Without that, keyboard users would be dropped at the top of the page.
- **Pick-up state is clear in text and visually.**
  - The Reorder button uses `aria-pressed`.
  - The held card gets a thick outline plus a fill, so it doesn't rely on colour alone.
  - Moving focus away from a held ticket drops it where it is.
- **Priority is written out** as "Priority: Urgent", not shown only as a colour. Urgent also gets an underline.
- **The visual side is covered:**
  - Text and borders are meant to have enough contrast in both light and dark mode, following the system setting. I didn't measure the ratios.
  - Focus rings are 3px.
  - Buttons and lists are at least 32px tall.
  - The layout reflows to one column on narrow screens.
  - A "Skip to board" link and a collapsible "How to move tickets" help section are included.
  - Windows high-contrast mode and reduced-motion preferences are handled.
- **Drop targets are visible.** While you drag, the target column gets a dashed outline and a line shows where the ticket will land.

**Limitation:** the mouse drag uses the browser's built-in drag-and-drop, which doesn't work on most touch screens. Touch users have the Move to list instead.
