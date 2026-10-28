| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Every card has a "Move to…" control (dialog) that moves without dragging | 1 | Each card has `.move` "Move…" button opening dialog with radio columns |
| 2 | Keyboard-only move; Escape cancels and restores original position | 1 | `cancelGrab()` calls `place(id, from.col, from.idx)` on Escape |
| 3 | Persistent live region announces pick-up, each move (name + column + position), cancel | 1 | `#live` role=status; "TCK-103 now in ${where(id)}", picked up, cancelled messages |
| 4 | After a move, focus stays on moved card | 1 | `render({id, what:'grab'})` refocuses grab button; the dialog path focuses `.move` |
| 5 | Headed lists (h2/ul), one primary interactive element per card, no role=application/grid | 0 | Each card has two buttons (grab and Move…), not one primary element |
| 6 | Column headings include updating count | 1 | h2 contains `.count` with n and "tickets" for screen readers, re-rendered on change |
| 7 | Visible :focus-visible ≥2px; focused cards not hidden under sticky header | 1 | 3px `:focus-visible` outline; no sticky elements in the page |
| 8 | Move/menu controls ≥24×24 CSS px | 1 | `.move` min-height/min-width 2.75rem (44px) |
| 9 | Respects prefers-reduced-motion and forced-colors affordances | 0 | forced-colors block present, but no prefers-reduced-motion handling anywhere |
| 10 | Pointer drag still works | 1 | Pointer-event drag with ghost, marker, and drop implemented |

TOTAL: 8/10
