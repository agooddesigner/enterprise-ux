| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Single-pointer alternative to dragging | 1 | "Move…" button opens dialog with column radio buttons |
| 2 | Keyboard operation for moving cards | 1 | Space/Enter grab, arrow keys move, Home/End, Escape (kbMove) |
| 3 | Notes keyboard-only drag isn't enough, or provides both paths | 1 | Provides both keyboard grab-and-move and the Move dialog path |
| 4 | Announces moves via live region | 1 | `role="status" aria-live="polite"`; announce("TCK-103 now in …") |
| 5 | Appropriate semantics, no grid misuse | 1 | main, h1, section with h2, ul/li, buttons; no role=grid |
| 6 | Visible focus indicator on cards | 1 | `:focus-visible { outline: 3px solid }`; card buttons are focusable |
| 7 | Target size ≥24×24px | 1 | min-height 2.75rem on controls, and the response states 44px |
| 8 | Status/priority not by colour alone | 1 | Priority uses ▲/■/▼ shape plus word text |
| 9 | Focus managed after a move | 1 | render({id, what:'grab'}) refocuses the moved card's button |
| 10 | Mentions testing with keyboard and screen reader | 0 | It only recommends a screen-reader pass (NVDA, VoiceOver). It doesn't mention keyboard testing, and says it ran no checks. |

TOTAL: 9/10
