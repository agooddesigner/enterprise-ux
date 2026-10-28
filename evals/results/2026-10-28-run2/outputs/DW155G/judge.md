| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Inputs use placeholder instead of visible labels | 1 | Item 10: inputs have only placeholders; use visible labels |
| 2 | Submit button disabled with no explanation | 1 | Item 9: permanently disabled, gives no reason |
| 3 | Vague "Submit" button label | 1 | Item 9: Name it "Add invoice", not "Submit" |
| 4 | "Invalid input" error vague / not tied to field / no fix | 1 | Item 10: unlinked, suggests "Enter an amount like 1200.50" |
| 5 | Form clears user input on submit/error | 1 | Item 8: handler clears all inputs regardless of outcome |
| 6 | Focus outline removed | 1 | Item 4: `outline: none` rule fails WCAG 2.4.7 |
| 7 | Status shown by colour dot only | 1 | Item 11: ● green versus ● red, colour alone |
| 8 | Icon-only buttons lack accessible names | 1 | Item 7: no aria-label on 💾 and 🗑 buttons |
| 9 | Icon buttons too small (<24×24) | 1 | Item 17: `.icon-btn` is 16×16px |
| 10 | Row delete has no confirmation or undo | 1 | Item 2: instant and silent; adds Undo toast |
| 11 | "Delete All" irreversible with no confirmation/scope | 1 | Item 1: no confirmation, no undo, no count |
| 12 | Div table; clickable rows via onclick non-keyboard accessible | 1 | Item 5: divs, onclick on div, not focusable |
| 13 | Numbers centred and/or inconsistent decimals/no currency | 1 | Item 18: `1200.5` and `87`, no currency, centred wrong |
| 14 | First column is an opaque system ID | 1 | Item 20: ID column is raw UUID fragment |
| 15 | Error toast auto-dismisses quickly and shows "Error 500" | 1 | Item 14: disappears after 2s; item 13 "Error 500" |
| 16 | Full-page centred spinner / blocking load | 1 | Item 3: full-screen fixed loader blocks everything |
| 17 | Low-contrast muted text (#b5b5b5) | 1 | Item 12: `.muted` `#b5b5b5` about 2:1 |
| 18 | Modal opens another modal / sticky header / generic title "App" | 1 | Item 15 stacked modals; item 16 title "App" |
| 19 | Issues ranked by severity/impact | 1 | P0/P1/P2/P3 tiers |
| 20 | Each top issue has a concrete fix | 1 | Top issues each carry a specific Fix |

TOTAL: 20/20
