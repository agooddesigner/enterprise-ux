| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Inputs use placeholder instead of visible labels | 1 | #11: "Inputs have no `<label>`s, only placeholders"; add visible labels |
| 2 | Submit button disabled with no explanation | 1 | #12: Submit permanently `disabled`, no explanation, no code enabling it |
| 3 | Vague "Submit" button label | 0 | Only mentions the button being disabled; label wording not flagged |
| 4 | "Invalid input" error vague / not tied to field / no fix | 1 | #13: static "Invalid input", unassociated; use "Amount must be a number" |
| 5 | Form clears user input on submit/error | 1 | #3: `value=''` on every input wipes all input |
| 6 | Focus outline removed | 1 | #4: `outline: none` rule; use visible `:focus-visible` |
| 7 | Status shown by colour dot only | 1 | #10: status conveyed by colour alone (green/red ●) |
| 8 | Icon-only buttons lack accessible names | 1 | #8: add `aria-label="Save invoice 8f3a-22c1"` |
| 9 | Icon buttons too small (<24×24) | 1 | #9: touch targets are 16×16px, WCAG 2.5.8 minimum 24px |
| 10 | Row delete has no confirmation or undo | 1 | #2: per-row delete unconfirmed and silent |
| 11 | "Delete All" irreversible, no confirmation/scope | 1 | #1: no confirmation, no undo; confirm dialog naming consequence |
| 12 | Table of divs; rows clickable via onclick, not keyboard accessible | 1 | #6: clickable `div`s with `onclick`, not focusable, no key handler |
| 13 | Numbers centred and/or inconsistent decimals/no currency | 1 | #18: amounts unformatted, no currency; #17 right-align not centred |
| 14 | First column is an opaque system ID | 1 | #25: truncated IDs have no meaning for users; human-readable number |
| 15 | Error toast auto-dismisses quickly, shows "Error 500" | 1 | #14: toasts vanish after 2s; "Error 500: Something went wrong" |
| 16 | Full-page centred spinner / blocking load | 1 | #5: loader overlay `position: fixed; inset: 0`, never removed, blocks input |
| 17 | Low-contrast muted text (#b5b5b5) | 1 | #15: `.muted` (#b5b5b5 on white) about 2.0:1 |
| 18 | Modal opens modal / sticky header obscures focus / generic title "App" | 1 | #16 modal opens second modal; #22 title "App" |
| 19 | Issues ranked by severity/impact | 1 | P0–P3 tiers plus suggested fix order |
| 20 | Each top issue has a concrete fix | 1 | Top issues each state a specific fix, e.g. remove rule, add confirm dialog |

TOTAL: 19/20
