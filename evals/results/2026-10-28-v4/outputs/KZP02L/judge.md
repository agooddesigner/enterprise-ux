| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | States direction as lead style plus borrowed elements | 0 | Chat describes contents; never names a lead style plus borrowed bento elements |
| 2 | Restrained UI colour: neutrals + one accent; other colour only status | 1 | Single --accent #533afd; good/warn/bad used for status and deltas |
| 3 | Top KPI bento with one larger hero tile | 1 | .hero grid-column span 6, row span 2; four span-3 tiles |
| 4 | Below KPIs is table/list-first | 1 | "Needs attention" table with tabs, checkboxes, bulk bar; aging list |
| 5 | Light and dark both implemented | 1 | prefers-color-scheme plus data-theme toggle with localStorage |
| 6 | Dark avoids #000, uses lighter surfaces, not heavy shadows | 1 | --canvas #0b1220, --card #121b2e lighter; --shadow:none in dark |
| 7 | No clashing effects (glass, hard shadows, decorative gradients) | 0 | .top uses backdrop-filter:blur(8px) glassmorphism; skeleton gradient too |
| 8 | Money tabular numerals, right-aligned in tables, consistent currency | 1 | .num tnum; Amount th/td .r right-aligned; fmt() "$" en-US |
| 9 | Status with text + colour pill/badge | 1 | .pill with "Overdue"/"Payment failed" text and colour |
| 10 | App shell: nav with current, search, account | 1 | aria-current Billing nav, ⌘K search button, account avatar button |

TOTAL: 8/10
