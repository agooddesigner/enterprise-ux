| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Direction stated as lead style plus borrowed elements | 0 | "Stripe-style restraint" and bento mentioned, but not framed as lead plus borrowed elements |
| 2 | Restrained colour: neutrals + one accent; other colour for status only | 1 | Slate/white + indigo accent; green/amber/red only on pills/deltas/banner |
| 3 | KPI bento with one larger hero tile | 1 | `.hero{grid-column:span 6;grid-row:span 2}` with 64px MRR |
| 4 | Below KPIs table/list-first | 0 | Chart, attention list and table are all cards; page is still largely card-based |
| 5 | Light and dark both implemented | 1 | prefers-color-scheme block plus data-theme toggle button |
| 6 | Dark avoids #000; lighter surfaces for elevation, not shadows | 1 | bg #0b1220, surface #121a2b; `--shadow:none` in dark |
| 7 | No glassmorphism, hard shadows or decorative gradients | 0 | Hero has `linear-gradient(surface,surface)` (no visible effect); sparkline fill and skeleton shimmer are functional. Strictly, no decorative gradient is visible, so this is borderline, but the hero gradient declaration counts against it. |
| 8 | Tabular numerals, right-aligned money, consistent currency | 0 | Amount column right-aligned with `.num`, but cells show "$48,200" while the KPI row mixes "$482,310", "$0" and "$320k"-style chart labels. Also, the Amount `th.r` is right-aligned and the numbers are tabular, but the formats are inconsistent. |
| 9 | Status shown with text + colour | 1 | `.pill` with label text and dot, e.g. "Overdue", "Payment failed" |
| 10 | App shell: nav with current section, search, account | 1 | Side nav with `aria-current="page"` on Billing, search input, avatar "MR" |

TOTAL: 5/10
