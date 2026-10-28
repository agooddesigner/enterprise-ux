| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Single-pointer "Move to…" control on every card | 1 | Each card has a labelled "Move to" `<select>`, which moves the card without dragging. |
| 2 | Keyboard-only move; Escape cancels and restores position | 1 | The Escape case calls `move(id, grabbed.status, grabbed.index)`, restoring the original spot. |
| 3 | Persistent live region announcing pick-up, each move and cancel | 1 | `role="status"` `aria-live` div. It announces "Picked up…", `position()` after each move, and "Move cancelled". |
| 4 | Focus stays on the moved card after a move | 1 | `render('[data-handle=id]')` and `render("#"+sid)` refocus the control inside the moved card. |
| 5 | Headed lists; one primary interactive element per card; no application/grid role | 0 | Columns use `h2` and `ul`. Each card has two controls (Move button and select), and the `li` is draggable. |
| 6 | Column headings include an updating count | 1 | `h2` renders `${name} (${items.length} tickets)` and is rebuilt on every render. |
| 7 | `:focus-visible` indicator of at least 2px; focused cards not hidden under a sticky header | 1 | `:focus-visible { outline: 3px … }`. There are no sticky elements in the page. |
| 8 | Move/menu controls at least 24×24 CSS px | 1 | `.handle`, `select` and `.btn` all have `min-height: 44px`. |
| 9 | Reduced motion respected; forced-colors affordances use border/outline | 1 | Transitions are inside `prefers-reduced-motion: no-preference`. Forced-colors uses `outline: 3px solid Highlight`. |
| 10 | Pointer drag still works | 1 | `draggable=true`, with dragstart, dragover and drop handlers calling `move()`. |

TOTAL: 9/10
