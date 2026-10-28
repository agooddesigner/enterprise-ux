| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Explicit direction as lead style + borrowed elements | 0 | Chat mentions "Bento KPIs" and "Stripe-like restraint" as bullets, but never states a lead style plus borrowed elements. |
| 2 | Restrained UI colour: neutrals + one accent; other colour only status | 1 | Indigo `--accent` only; green/amber/red used in pills, deltas, banner. |
| 3 | Bento KPI grid with one larger hero tile | 1 | `.hero{grid-column:span 6;grid-row:span 2}` beside four `span 3` KPIs. |
| 4 | Below KPIs table/list-first | 1 | Invoice table with tabs/sort plus "Needs attention" list below KPIs. |
| 5 | Light and dark both implemented | 1 | `prefers-color-scheme` media query plus `data-theme` toggle with localStorage. |
| 6 | Dark avoids #000, lighter surfaces for elevation, no heavy shadows | 1 | `--bg:#0b1220`, `--surface:#121a2b`, `--shadow:none`. |
| 7 | No clashing effects (glass, hard shadows, decorative gradients) | 0 | `.sk` skeleton uses `linear-gradient` shimmer. It's functional, but a literal check finds a gradient. Strictly, none of it is decorative; the toast has a soft shadow only. Marked 0 for strictness. |
| 8 | Tabular numerals, right-aligned money, consistent currency format | 1 | `.num` tnum; Amount column `num r`; `fmtC` gives `$48,000.00`. |
| 9 | Status shown with text + colour | 1 | `.pill` has dot plus label text ("Overdue", "Payment failed"). |
| 10 | App shell: nav with current section, search, account | 1 | Sidebar `aria-current="page"` on Billing, ⌘K search, avatar account button. |

TOTAL: 7/10
