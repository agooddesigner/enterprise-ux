| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Direction stated as lead style plus borrowed elements | 0 | Describes hero/bento/tiles but never names a lead style plus borrowed elements. |
| 2 | Restrained UI colour: neutrals + one accent; other colour only for status | 0 | Mostly yes, but navy hero-bg and warn amber used as a non-status breakdown swatch. |
| 3 | Top KPI area is bento with one larger hero tile | 1 | `.hero{grid-column:span 6;grid-row:span 2}` beside four span-3 tiles. |
| 4 | Below KPIs is table/list-first, not all bento cards | 0 | Below the KPIs are card-wrapped chart, breakdown, table and account cards. |
| 5 | Light and dark both implemented | 1 | prefers-color-scheme media query plus `data-theme` toggle with localStorage. |
| 6 | Dark avoids #000; lighter surfaces for elevation, not heavy shadows | 1 | Dark bg #0b0f1a, surface #131826 lighter, `--shadow:none`. |
| 7 | No clashing effects: glass, hard shadows, decorative gradients | 1 | No blur, offset shadows or gradients; only a 1px soft shadow. |
| 8 | Money tabular numerals, right-aligned in tables, consistent currency format | 1 | `.num` uses tabular-nums; Amount column `class="r"`; `usd()` formats to 2 decimals. |
| 9 | Status shown with text + colour | 1 | `.pill` with a text label ("Overdue", "Paid", "Open") plus colour and dot. |
| 10 | App shell: primary nav with current section, search, account | 1 | Tabs with `aria-current="page"`, `.search` box, avatar PR. |

TOTAL: 6/10
