| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Links acme-ds.css, uses `var(--ds-…)` tokens, ≤3 new hex colours | 0 | Links CSS and uses tokens, but adds many hexes: #CBD5E1, #334155, #5FA9A1, #A7CFCA, #78350F, #7F1D1D, #F5D98B, #FCA5A5. |
| 2 | DS radius tokens; no new radius above 6px | 1 | Uses `--ds-radius-*`; custom radii are 4px, 3px, 2px, and 50% on a 20px icon. |
| 3 | Uses DS font; no new font family | 1 | No font-family or font import; `select` uses `font:inherit`. |
| 4 | Doesn't ask user to choose visual style or propose another preset | 1 | The prototype controls switch state and role, not style. |
| 5 | Uses DS component classes where they fit | 1 | Uses `.ds-btn`, `.ds-card`, `.ds-table`, `.ds-badge`; no `.ds-input`, since selects are custom-styled. |
| 6 | Usage vs limit with numbers, units, billing period | 1 | "9,380 of 10,000", "38.2 of 100 GB", with "Billing period 1–31 Oct 2026" in the meta line. |
| 7 | Billing shows plan, next invoice date and amount, payment method | 0 | Plan, "Next invoice 1 Nov 2026" and Visa 4242 are shown. The amount is not in that row; the $1,178.20 projection sits in the hero card. |
| 8 | Loading, empty, error states exist and are reachable | 1 | The state select offers loading, error, and empty; skeletons and error boxes with retry are rendered. |
| 9 | Non-billing roles see read-only state with reason | 1 | Admin role gets aria-disabled buttons and "Billing is managed by Dana Okafor… Ask…". |
| 10 | App shell: primary nav with current section, account menu | 0 | Topbar nav has `aria-current="page"`, but there is no account menu. |

TOTAL: 6/10
