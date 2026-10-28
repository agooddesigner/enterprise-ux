| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Direction stated as lead style + borrowed elements | 0 | Code comment says "4-col bento… then ledger table"; no explicit lead-plus-borrowed statement. |
| 2 | Restrained colour: neutrals + one accent; other colour only status | 0 | Accent blue plus warn/bad on aging bar, sparkline in green/amber; mostly status, but the tile "Failed payments" amber text and good sparkline are used outside status pills. Strictness: ambiguous, though mostly status-related. |
| 3 | Bento KPIs with one larger hero tile | 1 | `.hero{grid-column:span 2;grid-row:span 2}` with the MRR $462,700. |
| 4 | Below KPIs table/list-first | 1 | Invoice table plus renewals list in `.lower`. |
| 5 | Light and dark both implemented | 1 | prefers-color-scheme media query plus `data-theme` toggle button. |
| 6 | Dark avoids #000, lighter surfaces for elevation, no heavy shadows | 1 | `--bg:#0d1016; --surface:#151a22; --shadow:none`. |
| 7 | No clashing effects (glass, hard shadows, decorative gradients) | 0 | Hero chart uses a linearGradient area fill (`id:"hg"`), a gradient. |
| 8 | Tabular numerals, right-aligned money, consistent currency | 1 | `.num` tnum; `th.r, td.r` right-aligned amounts; `fmt` gives "$"+toLocaleString. |
| 9 | Status with text + colour | 1 | `.pill` has label text ("Overdue", "Paid", "Open") plus coloured dot and background. |
| 10 | App shell: nav with current section, search, account | 0 | Header has only brand, chips and theme button; no nav, search or account. |

TOTAL: 5/10
