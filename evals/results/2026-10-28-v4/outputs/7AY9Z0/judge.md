| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Direction stated as lead style plus borrowed elements | 0 | Describes paper-grey/indigo look and bento KPIs, but never names a lead style with borrowed elements. |
| 2 | Restrained UI colour: neutrals + one accent; other colour only for status | 1 | Indigo accent only; good/warn/bad used for pills and strip. |
| 3 | KPI area is bento with one clearly larger hero tile | 1 | `.hero` spans 6 columns and 2 rows; four tiles span 3 columns each. |
| 4 | Below the KPIs the page is table/list-first | 0 | Below the KPIs are a chart card, a details card and a table card, all in the bento grid. The page is mostly cards. |
| 5 | Light and dark both implemented | 1 | `prefers-color-scheme` block, `[data-theme]` overrides and toggle button. |
| 6 | Dark mode avoids #000; lighter surfaces, not heavy shadows, for elevation | 0 | Dark `--card` (#12151d) is only slightly lighter than `--bg` (#0a0c12), and `--shadow: none`. Hero anchor is a different surface, so this mostly holds, but the check is unclear. Marked strict. |
| 7 | No clashing effects: no glassmorphism, hard offset shadows, or decorative gradients | 0 | Hatched `repeating-linear-gradient` on the projected bar is decorative. The skeleton shimmer is a functional gradient. |
| 8 | Money in tabular numerals, right-aligned in tables, consistent currency formatting | 1 | `font-variant-numeric: tabular-nums` on body; `.r` on Amount column; `usd.format` used. |
| 9 | Status shown with text + colour | 1 | Pills have a dot and text, e.g. "Open", "Paid", "Over by 1.2M". |
| 10 | App shell: primary navigation with current section, search, account | 0 | The top bar has brand, state select, theme toggle and avatar. There is no primary navigation or search. |

TOTAL: 5/10
