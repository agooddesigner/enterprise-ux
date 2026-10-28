| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Inputs use placeholder instead of visible labels | 1 | Item 7: "Placeholders are the only labels"; use visible `<label>` |
| 2 | Submit button disabled with no explanation | 1 | Item 8: disabled with no explanation; keep enabled or explain |
| 3 | Vague "Submit" button label | 0 | Submit is mentioned but its label is never flagged as vague |
| 4 | "Invalid input" error vague / not tied to field / no fix | 1 | Item 9: generic, doesn't say which field; make specific |
| 5 | Form clears user input on submit/error | 1 | Item 6: wipes input on any error; keep values |
| 6 | Focus outline removed | 1 | Item 2: `outline: none` removes focus indicator; use :focus-visible |
| 7 | Status shown by colour dot only | 1 | Item 10: ● green/red with no text; add label |
| 8 | Icon-only buttons lack accessible names | 1 | Item 5: 💾/🗑 no accessible name; add aria-label |
| 9 | Icon buttons too small (<24×24px) | 1 | Item 5: 16×16px below 24px minimum |
| 10 | Row delete has no confirmation or undo | 1 | Item 3: row 🗑 does same; prefer undo for single deletes |
| 11 | "Delete All" irreversible, no confirmation/scope | 1 | Item 3: fires DELETE immediately; confirm dialog naming consequence |
| 12 | Table from divs; onclick rows not keyboard accessible | 1 | Item 4 and 12: div rows with onclick, no tabindex/key handler |
| 13 | Numbers centred and/or inconsistent decimals/no currency | 1 | Item 16: no currency, inconsistent decimals; right-align |
| 14 | First column is an opaque system ID | 1 | Item 17: IDs are opaque (`8f3a-22c1`) |
| 15 | Error toast auto-dismisses quickly, shows "Error 500" | 1 | Item 13: disappears after 2 seconds; "Error 500" message |
| 16 | Full-page centred spinner / blocking load | 1 | Item 1: loader fixed inset 0 blocks the whole screen |
| 17 | Low-contrast muted text (#b5b5b5) | 1 | Item 11: `.muted` #b5b5b5 about 2.1:1 |
| 18 | Modal opens another modal / sticky header / generic title "App" | 1 | Item 14: stacked modals; item 19: generic title "App" |
| 19 | Issues ranked by severity/impact | 1 | P0/P1/P2/P3 severity tiers |
| 20 | Each top issue has a concrete fix | 1 | Each P0 item has an explicit *Fix:* line |

TOTAL: 19/20
