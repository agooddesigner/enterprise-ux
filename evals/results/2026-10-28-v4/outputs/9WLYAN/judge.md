| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Links acme-ds.css, DS tokens, ≤3 new hex | 1 | `<link href="acme-ds.css">`; all colours via var(--ds-color-…); no hex |
| 2 | DS radius tokens; no new radius >6px | 0 | Uses `--ds-radius-lg` on notice (value unknown); chart rect rx:2 raw; unverifiable ≤6px |
| 3 | Uses DS font; no new family | 1 | `var(--ds-font)` only; no font import |
| 4 | No style question / no alternate preset | 1 | Response never asks about style or proposes a preset |
| 5 | Uses DS component classes | 1 | `.ds-btn`, `.ds-card`, `.ds-table`, `.ds-badge` used throughout |
| 6 | Usage vs limit with numbers, units, period | 1 | "412,300 of 500,000", "Current period Oct 1 – Oct 31, 2026" |
| 7 | Plan, next invoice date/amount, payment method | 1 | Business plan; $1,055.00 Nov 1; Visa ending 4242 |
| 8 | Loading, empty, error states reachable | 0 | No loading, empty or error states present |
| 9 | Non-billing roles read-only/no-access with reason | 0 | No role handling at all |
| 10 | App shell: primary nav with current section, account menu | 0 | Only `<main>`; no nav or account menu |

TOTAL: 5/10
