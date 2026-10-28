| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Per-card "Move to…" control moving without drag | 1 | Native `<select data-move>` per card; change handler calls place() |
| 2 | Keyboard-only move; Escape cancels and restores original position | 1 | Reorder button arrows; Escape calls place(origCol, origIndex) |
| 3 | Live region announces pick-up, each move (name+column+position), cancel | 1 | `role=status` polite; announces pick-up with title, where(), cancel |
| 4 | Focus stays on moved card after move | 1 | render(`[data-grab=id]`) refocuses the moved card's control |
| 5 | Headed lists, one primary interactive per card, no role=application/grid | 0 | h2/ul used, but each card has button plus select (two controls) |
| 6 | Column headings include updating count | 1 | h2 contains `.count` span with items.length, re-rendered |
| 7 | Focus-visible ≥2px, not hidden under sticky header | 1 | `:focus-visible` 3px outline; no sticky elements, no sticky header |
| 8 | Controls ≥24×24 px | 1 | min-height 2.5rem/2.25rem on buttons and selects |
| 9 | Reduced-motion respected; forced-colors handled with outline/border | 1 | `prefers-reduced-motion: no-preference` transition; forced-colors Highlight outlines |
| 10 | Pointer drag still works | 1 | HTML5 draggable, dragstart/dragover/drop handlers implemented |

TOTAL: 9/10
