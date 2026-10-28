| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Single-pointer alternative to dragging | 1 | Native "Move to" `<select>` on every ticket |
| 2 | Keyboard operation for moving cards | 1 | Reorder button: Space grabs, arrow keys move, Space drops |
| 3 | Notes keyboard-only drag isn't enough, or provides both paths | 1 | Provides both select (pointer) and keyboard Reorder paths |
| 4 | Live region announcements of moves | 1 | `role="status" aria-live="polite"`; announce() "Ticket X moved to…" |
| 5 | Appropriate semantics, not grid misuse | 1 | section/h2, ul/li, article/h3, buttons; no role=grid |
| 6 | Visible focus indicator on cards | 1 | `:focus-visible` 3px outline; grabbed card gets box-shadow |
| 7 | Target size ≥ 24×24px | 1 | min-height 2.5rem/2.25rem; "at least 36px tall" |
| 8 | Status/priority not by colour alone | 1 | Priority shown as text "Priority: High" |
| 9 | Focus managed after a move | 1 | render(`[data-grab="${id}"]`) refocuses the moved ticket's control |
| 10 | Mentions testing with keyboard and screen reader | 1 | "try the drag, keyboard and screen-reader paths before relying on it" |

TOTAL: 10/10
