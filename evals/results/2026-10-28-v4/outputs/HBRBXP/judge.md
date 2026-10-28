| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Links acme-ds.css, uses var(--ds-…) colours, ≤3 new hex outside status | 1 | Links acme-ds.css; new hex: #99F6E4, #134E4A (teal), amber ones are status |
| 2 | DS radius tokens; no new radius >6px | 1 | Uses var(--ds-radius-sm/md/lg); no raw radius values; chat says 4–6px |
| 3 | DS font; no new font family | 1 | No font-family declared or imported |
| 4 | Doesn't ask for style choice or propose different preset | 1 | No style question; kept the DS look |
| 5 | Uses DS component classes where they fit | 1 | ds-btn, ds-card, ds-table, ds-badge, ds-input all used |
| 6 | Usage vs limit with numbers, units, billing period | 1 | "6,240 of 10,000 included"; meta shows "15 Oct – 14 Nov 2026" |
| 7 | Billing shows plan, next invoice date and amount, payment method | 1 | Business annual; Billed 15 Nov $1,352.68 projected; Visa ending 4242 |
| 8 | Loading, empty, error states exist and are reachable | 1 | Preview state select: loading/error/empty; skeletons, Retry, empty notice |
| 9 | Non-billing roles see read-only state with the reason | 1 | readonly state: "Billing is managed by Priya Raman. Ask them to change…" |
| 10 | App shell: primary navigation with current section, account menu | 0 | Only breadcrumb; no nav or account menu |

TOTAL: 9/10
