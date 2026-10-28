| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Inputs use placeholder instead of visible labels | 1 | "inputs have placeholders only, so there's no persistent label"; add real labels |
| 2 | Submit button disabled with no explanation | 1 | "button is `disabled` with no explanation and nothing ever enables it" |
| 3 | Vague "Submit" button label | 1 | "Use a specific verb: 'Add invoice'" |
| 4 | "Invalid input" error vague / not tied to field / no fix | 1 | "doesn't say which field or why"; per-field message with example fix |
| 5 | Form clears user input on submit/error | 1 | "click handler clears every input unconditionally"; keep values on error |
| 6 | Focus outline removed | 1 | "`button:focus, input:focus, a:focus { outline: none }`"; use :focus-visible ring |
| 7 | Status shown by colour dot only | 1 | "The ●s are red or green with no text"; use label |
| 8 | Icon-only buttons lack accessible names | 1 | "💾 and 🗑 are emoji with no `aria-label`" |
| 9 | Icon buttons too small (<24×24) | 1 | "`.icon-btn` is 16×16. WCAG 2.5.8 requires at least 24px" |
| 10 | Row delete has no confirmation or undo | 1 | "per-row 🗑 call `fetch(DELETE)` immediately, with no confirmation, no undo" |
| 11 | "Delete All" irreversible with no confirmation/scope | 1 | "Delete all 2 invoices?"; no confirmation, no count, type the count |
| 12 | Table of divs; rows clickable via onclick, not keyboard accessible | 1 | "`div onclick` has no role, tabindex or key handler"; `.grid`/`.row` divs |
| 13 | Numbers centred and/or inconsistent decimals/no currency | 1 | "Amounts are centred… unformatted (`1200.5`, `87`)… no currency" |
| 14 | First column is an opaque system ID | 0 | IDs used in examples, but never flagged as an opaque first column. |
| 15 | Error toast auto-dismisses quickly, shows technical "Error 500" | 1 | "vanishes after 2s"; "Error 500: Something went wrong" hard-coded, not actionable |
| 16 | Full-page centred spinner / blocking load | 1 | "`.spinner-page` is `position: fixed; inset: 0`"; blocks every click |
| 17 | Low-contrast muted text (#b5b5b5) | 1 | "`.muted` #b5b5b5 on white is about 2:1" |
| 18 | Modal opens another modal / sticky header obscures focus / generic title "App" | 1 | "Opening a modal from inside a modal"; title "App" is meaningless |
| 19 | Issues ranked by severity/impact | 1 | "Top 3 (fix first)", then high and medium sections, plus fix order |
| 20 | Each top issue has a concrete fix | 1 | Each top issue has a "Fix:" with specific changes |

TOTAL: 19/20
