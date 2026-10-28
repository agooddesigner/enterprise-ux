| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Links acme-ds.css, uses var(--ds-…) tokens, ≤3 new hex colours | 1 | `<link rel="stylesheet" href="acme-ds.css">`; all colours via var(--ds-color-*); no hex |
| 2 | DS radius tokens; no new radius >6px | 0 | Uses var(--ds-radius-lg) on alert and bar; its value is unknown, so ≤6px can't be confirmed |
| 3 | DS font, no new font family | 1 | No font-family declared or imported; inherits DS |
| 4 | Doesn't ask for visual style or propose another preset | 1 | No style question or alternative preset in response |
| 5 | Uses DS component classes where fitting | 1 | Uses .ds-btn, .ds-card, .ds-table, .ds-badge, .ds-input |
| 6 | Usage vs limit with numbers, units, billing period | 1 | "4,350 of 5,000"; "38 GB of 100 GB"; "Billing period Oct 1 – Oct 31, 2026" |
| 7 | Billing: plan, next invoice date+amount, payment method | 0 | Next invoice date Nov 1 shown, but amount is "Estimated bill $612.00" in a separate card, not tied to the invoice. Card is shown. Partial, scored strictly. |
| 8 | Loading, empty, error states exist and reachable | 0 | None present; only the populated state |
| 9 | Permission handling for non-billing roles | 0 | No read-only or no-access state |
| 10 | App shell: primary nav with current section, account menu | 0 | No nav or account menu; only `<main>` |

TOTAL: 5/10
