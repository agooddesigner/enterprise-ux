| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Inputs use placeholder instead of visible labels | 1 | Finding 9: "Placeholders are the only labels"; add visible labels |
| 2 | Submit button disabled with no explanation | 1 | Finding 3: button `disabled` with no way to enable it |
| 3 | Vague "Submit" button label | 1 | Finding 9: button label "Submit" is vague; use "Add invoice" |
| 4 | "Invalid input" error vague / not tied to field / no fix | 1 | Finding 9: doesn't name a field; show next to field |
| 5 | Form clears user input on submit/error | 1 | Finding 3: Submit clears every input; keep values on failure |
| 6 | Focus outline removed | 1 | Finding 5: `outline:none` with no replacement; use `:focus-visible` |
| 7 | Status shown by colour dot only | 1 | Finding 10: coloured ● with no text; use text badge |
| 8 | Icon-only buttons lack accessible names | 1 | Finding 6: no accessible name; use `aria-label` |
| 9 | Icon buttons too small (<24×24px) | 1 | Finding 6: 16×16px emoji buttons; minimum 24px |
| 10 | Row delete has no confirmation or undo | 1 | Finding 6/7: Delete gives no feedback; use confirmation or Undo |
| 11 | "Delete All" irreversible with no confirmation/scope | 1 | Finding 1: no confirmation, count, undo; act on selected rows |
| 12 | Table of divs; onclick rows not keyboard accessible | 1 | Findings 4 and 11: `<div onclick>`, no tabindex/key handler |
| 13 | Numbers centred and/or inconsistent decimals/no currency | 1 | Finding 11: right-align amounts, consistent decimals and currency |
| 14 | First column is opaque system ID | 1 | Finding 18: "IDs are raw hashes"; aria-label uses ID |
| 15 | Error toast auto-dismisses quickly, shows "Error 500" | 1 | Finding 8: disappears after 2s; "Error 500: Something went wrong" |
| 16 | Full-page centred spinner / blocking load | 1 | Finding 2: fixed inset:0 "Loading..." overlay blocks everything |
| 17 | Low-contrast muted text (#b5b5b5) | 1 | Finding 15: `#b5b5b5` on white about 2.1:1 |
| 18 | Modal opens another modal / sticky header / generic title "App" | 1 | Finding 13 nested modal; Finding 16 title "App" |
| 19 | Issues ranked by severity/impact | 1 | Findings table with Sev column, ranked 4 down to 2 |
| 20 | Each top issue has a concrete fix | 1 | Each finding has a specific Fix, e.g. `:focus-visible` 2px outline |

TOTAL: 20/20
