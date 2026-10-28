| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Every card has single-pointer "Move to…" control | 1 | Each card has `.move` button opening native dialog with radio columns |
| 2 | Keyboard move; Escape cancels and restores original | 1 | Esc handler calls `place(t.id, grab.origin.col, grab.origin.index)` |
| 3 | Persistent live region announces pick-up, moves, cancel | 1 | `#status` role=status aria-live; announces picked up, position, "Move cancelled" |
| 4 | Focus stays on moved card after move | 1 | `render({id})` refocuses `.handle` / `.move` of the moved card |
| 5 | Semantics: headed lists, one primary interactive element per card, no application/grid | 0 | Each card has two buttons (handle and Move…); not one primary element |
| 6 | Column headings include updating count | 1 | `<h2>` contains `.count` span with items.length, re-rendered each move |
| 7 | Focus-visible ≥2px, not hidden under sticky header | 1 | `:focus-visible` 3px outline; no sticky elements in the page |
| 8 | Move/menu controls ≥24×24 | 1 | `button { min-height:44px; min-width:44px }` |
| 9 | Reduced-motion and forced-colors handled with border/outline | 1 | `prefers-reduced-motion` block; `forced-colors` block; grabbed uses outline/border |
| 10 | Pointer drag still works | 1 | pointerdown/move/up handlers implement ghost drag with drop placement |

TOTAL: 9/10
