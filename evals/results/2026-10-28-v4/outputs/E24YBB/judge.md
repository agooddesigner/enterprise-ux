| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Direction stated as lead style + borrowed elements | 0 | Code comment and chat describe "Restraint" but never name a lead style plus a borrowed bento composition. |
| 2 | Restrained colour: neutrals + one accent; other colour for status only | 1 | Indigo is the only accent; ok/bad/warn colours are used for status pills. |
| 3 | Bento KPI grid with one larger hero tile | 1 | `.hero{grid-column:span 6;grid-row:span 2}` beside four `span 3` KPI tiles. |
| 4 | Below KPIs is table/list-first, not all bento cards | 0 | Chart, plan and invoice table are all `.card` tiles in the same bento grid. |
| 5 | Light and dark both implemented | 1 | `prefers-color-scheme` media query plus a `data-theme` toggle button. |
| 6 | Dark avoids #000; lighter surfaces for elevation, not heavy shadows | 1 | Dark bg `#0b0d18`, card `#141828`, `--shadow:none`. |
| 7 | No clashing effects (glass, hard shadows, decorative gradients) | 0 | Hatched bar uses `repeating-linear-gradient`; skeleton shimmer uses `linear-gradient`. These are functional, but the check is literal about gradients, and the toast and tooltip also carry drop shadows. |
| 8 | Tabular numerals, right-aligned money in tables, consistent currency format | 1 | `font-feature-settings:"tnum"`, `.num`, `td.r` on amounts, and `usd()` formatting. |
| 9 | Status as text + colour pill | 1 | `statusPill` renders "Paid 3 Sep", "Overdue · 6 days" and similar text in coloured pills. |
| 10 | App shell: nav with current section, search, account | 0 | Nav has `aria-current` and an avatar, but there is no search. |

TOTAL: 5/10
