| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Links acme-ds.css, uses var(--ds-…) tokens, ≤3 new hex colours | 1 | `<link href="acme-ds.css">`; all colours via var(--ds-color-*); no hex values |
| 2 | DS radius tokens; no new radius >6px | 0 | `.banner` uses `--ds-radius-lg`; value unknown, could exceed 6px. Not shown to be ≤6px. |
| 3 | DS font, no new font family | 1 | Uses `var(--ds-font)`; no font import or new family |
| 4 | Doesn't ask user to choose style or propose different preset | 1 | Uses design system as is; no style choice asked |
| 5 | Uses DS component classes | 1 | Uses ds-btn, ds-card, ds-table, ds-badge, ds-input throughout |
| 6 | Usage vs limit with numbers, units, billing period | 0 | Shows "X of Y · %" and the period in the header, but units are absent (`unit:""`); transactions meter has no unit label beyond its name |
| 7 | Plan, next invoice date and amount, payment method | 1 | "Projected invoice · 1 Nov 2026" $; Business plan; Visa ending 4242 |
| 8 | Loading, empty, error states reachable | 1 | `?state=` select offers loading, error, empty, with skeleton and retry |
| 9 | Non-billing roles see read-only state with reason | 1 | readonly banner: "workspace admin but not a billing admin"; controls disabled |
| 10 | App shell: primary nav with current section, account menu | 1 | `aria-current="page"` on Usage & billing; Account menu button |

TOTAL: 8/10
