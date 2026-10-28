| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Single-pointer "Move to…" control on every card | 1 | Each card has a `Move to` select and a `Move` button |
| 2 | Keyboard move, and Escape restores the original position | 1 | The Escape case calls `place(id, grabbed.col, grabbed.index)` |
| 3 | Live region announces pick-up, each move (card name + column + position) and cancel | 0 | The `role=status` region is persistent, but arrow-key moves announce only `position(id)`, with no card name |
| 4 | Focus stays on the moved card | 1 | `render({id, sel})` refocuses the handle or select inside the moved card |
| 5 | Semantics: headed lists, one primary interactive element per card | 0 | Each card has three controls (Reorder button, select, Move button) |
| 6 | Column headings include an updating count | 1 | `<h2>` contains `<span class="count">` with the ticket count, re-rendered on each move |
| 7 | 2px+ focus-visible indicator, and focused cards not hidden under sticky elements | 0 | The 3px focus outline is there, but `.status` is `position: sticky` and nothing sets `scroll-padding` |
| 8 | Move/menu controls at least 24×24 CSS px | 1 | `button, select { min-height: 32px; min-width: 32px }` |
| 9 | Reduced-motion respected, and forced-colors affordances work | 1 | Transitions sit under `prefers-reduced-motion: no-preference`; `Highlight` outlines under `forced-colors` |
| 10 | Pointer drag still works | 1 | `draggable` with dragstart, dragover and drop handlers |

TOTAL: 7/10
