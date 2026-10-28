| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Inputs use placeholder instead of visible labels | 1 | "inputs have only placeholders as labels"; fix: real `<label>` elements |
| 2 | Submit button disabled with no explanation | 1 | "Submit is `disabled` with no explanation of what's missing" |
| 3 | Vague "Submit" button label | 1 | "Rename Submit to 'Add invoice'" |
| 4 | "Invalid input" error vague / not tied to field / no fix | 1 | Generic, not tied to a field; fix "Amount must be a number" |
| 5 | Form clears user input on submit/error | 1 | "Submit click handler wipes every input unconditionally, even on error" |
| 6 | Focus outline removed | 1 | `button:focus, input:focus, a:focus { outline: none; }` |
| 7 | Status shown by colour dot only | 1 | Status is a "●" in green or red; fails WCAG 1.4.1 |
| 8 | Icon-only buttons lack accessible names | 1 | Emoji-only icon buttons have no accessible name; add aria-label |
| 9 | Icon buttons too small (<24×24px) | 1 | "The icon buttons are 16×16px"; WCAG 2.5.8 |
| 10 | Row delete has no confirmation or undo | 1 | 🗑 button fires DELETE immediately, no confirmation, no undo |
| 11 | "Delete All" irreversible, no confirmation/scope | 1 | `Delete All` unguarded; "wipe every invoice"; name the count |
| 12 | Table from divs; rows clickable via onclick, not keyboard accessible | 1 | Rows are div/span with onclick; can't be focused; no Enter/Space |
| 13 | Numbers centred and/or inconsistent decimals/no currency | 1 | Centre-aligned, unformatted (`1200.5`, `87`), no currency |
| 14 | First column is an opaque system ID | 1 | "Raw IDs. `8f3a-22c1` is shown in full." |
| 15 | Error toast auto-dismisses quickly, shows "Error 500" | 1 | "Error 500: Something went wrong"; disappears after 2s |
| 16 | Full-page centred spinner / blocking load | 1 | `.spinner-page` fixed inset 0; overlays content, intercepts clicks |
| 17 | Low-contrast muted text (#b5b5b5) | 1 | `.muted` text `#b5b5b5` on white, about 2:1 |
| 18 | Modal opens another modal / sticky header / generic title "App" | 1 | "Two stacked modals"; title is just "App" |
| 19 | Issues ranked by severity/impact | 1 | Critical, High, Medium, Low sections; Top 3 ordered |
| 20 | Each top issue has a concrete fix | 1 | Each top 3 issue has a Fix with specific actions |

TOTAL: 20/20
