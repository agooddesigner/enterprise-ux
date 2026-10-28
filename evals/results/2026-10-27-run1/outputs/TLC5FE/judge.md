| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Single-pointer alternative to dragging | 1 | "Move…" button opens dialog with radio group of columns |
| 2 | Keyboard operation for moving cards | 1 | Space grabs, arrow keys move, Space/Enter drops, Esc cancels |
| 3 | Notes keyboard-only drag isn't enough / provides both paths | 1 | "WCAG 2.5.7 says dragging can't be the only way"; provides both keyboard and Move… |
| 4 | Live region announcements of moves | 1 | `role="status" aria-live="polite"`; "Moved TCK-103 to Waiting, position 2 of 3" |
| 5 | Appropriate semantics, no grid misuse | 1 | section+h2 columns, ul role="list", h3 titles, button handles |
| 6 | Visible focus indicator on cards | 1 | `:focus-visible { outline: 3px solid }`; handle button inside card is focusable |
| 7 | Target size ≥ 24×24px | 1 | `button { min-height: 44px; min-width: 44px }`; "at least 44px tall" |
| 8 | Status/priority not by colour alone | 1 | Priority has icon shape plus text label; grabbed shows "Picked up" text |
| 9 | Focus managed after a move | 1 | `render({id})` refocuses handle or `.move` button after each move |
| 10 | Mentions testing with keyboard and screen reader | 0 | Says it has not been tested and asks the user to try paths; no test plan for screen reader |

TOTAL: 9/10
