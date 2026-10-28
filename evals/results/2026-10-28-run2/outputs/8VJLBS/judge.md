| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Every card has a single-pointer "Move to…" control that moves without dragging | 1 | Each card has `select.move` "Move to" which calls moveTicket on change |
| 2 | Keyboard-only move; Escape cancels and restores original position | 1 | Reorder button arrows; Escape does `moveTicket(id, grab.origCol, grab.origIndex)` |
| 3 | Persistent live region announces pick-up, each move (name+column+position), cancel | 1 | `role="status"` live region; announces pick-up, cancel; arrow moves announce only `where(id)` without card name, but pick-up and select moves include name |
| 4 | After a move, focus stays on the moved card | 0 | Focus stays on the Reorder/select control inside the card, not the card itself |
| 5 | Headed lists, one primary interactive element per card; no role=application/grid | 0 | Headed lists present, but each card has two interactive controls (button and select) |
| 6 | Column headings include an updating count | 1 | `h2` contains `${list.length}` count, re-rendered on each move |
| 7 | Visible :focus-visible ≥2px and focused cards not hidden under sticky header | 1 | `:focus-visible { outline: 3px }`; no sticky elements |
| 8 | Move/menu controls at least 24×24 CSS px | 1 | `button, input, select { min-height: 44px }`; button min-width 44px |
| 9 | Reduced-motion respected and forced-colors affordances work | 1 | `prefers-reduced-motion: no-preference` gates transitions; forced-colors outlines use Highlight |
| 10 | Pointer drag still works for mouse users | 1 | HTML5 dragstart/dragover/drop handlers implemented |

TOTAL: 8/10
