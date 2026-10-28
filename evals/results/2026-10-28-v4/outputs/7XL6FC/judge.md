| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Links acme-ds.css, uses `var(--ds-…)` tokens, ≤3 new hex colours | 0 | Uses tokens, but hex colours exceed 3: #134E4A, #F3D08A, #F4B4B4, #E8EEF5, #fff. |
| 2 | DS radius tokens; no new radius >6px | 0 | Uses `var(--ds-radius-lg)` on banners/toast, but also hard-coded 5px, 3px, and 50% radii. Only the 5px and 3px values are ≤6px. |
| 3 | Uses DS font; no new font family | 1 | Only `var(--ds-font)`; no @import or new font-family. |
| 4 | No style question or alternate style preset | 1 | No style question; the "classic enterprise on Acme tokens" comment is not a proposed preset. |
| 5 | Uses DS component classes where they fit | 1 | Uses `ds-btn`, `ds-card`, `ds-table`, `ds-badge`, `ds-input`. |
| 6 | Usage vs limit with numbers, units, billing period | 1 | "Usage, 1–31 Oct 2026"; "5,412 of 5,000 docs" meters. |
| 7 | Plan, next invoice date and amount, payment method | 1 | Hero: $1,039.36, billed 1 Nov 2026 to Visa 4242; plan card shows Business plan. |
| 8 | Loading, empty, error states exist and are reachable | 1 | `?state=loading`/`empty`/`error` render skeleton, trial empty, and alert banner; linked at the bottom. |
| 9 | Non-billing roles see read-only state with reason | 1 | Readonly banner: "Billing is managed by Priya Raman"; inputs disabled. |
| 10 | App shell: primary nav with current section, account menu | 1 | `aria-current=page` on "Usage & billing"; account menu button "DO". |

TOTAL: 8/10
