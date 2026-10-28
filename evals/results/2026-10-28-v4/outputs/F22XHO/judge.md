| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Direction stated as lead style plus borrowed elements | 0 | Chat says "Flat, hairline-bordered cards" and "Bento KPIs"; no explicit lead plus borrowed framing. A code comment mentions "restrained... bento", but it's not stated as a direction. |
| 2 | Restrained colour: neutrals + one accent; other colour only for status | 1 | One blue accent; green/amber/red used for status and aging buckets. |
| 3 | Bento KPI grid with one larger hero tile | 1 | `.hero{grid-column:span 2;grid-row:span 2}` plus four small tiles. |
| 4 | Below KPIs is table/list-first | 0 | Below the KPIs are a chart card, an aging card and a table card; the page is mostly cards, and the table is only one of several. |
| 5 | Light and dark both implemented | 1 | `prefers-color-scheme` media query plus a `data-theme` toggle button. |
| 6 | Dark avoids #000, uses lighter surfaces, no heavy shadows | 1 | Dark `--bg:#0b1220`, `--surface:#121b2d`, `--shadow:none`. |
| 7 | No clashing effects (glass, hard shadows, decorative gradients) | 1 | No backdrop-filter, offset shadows or gradients. The sparkline fill is a flat low-opacity area. |
| 8 | Tabular numerals, right-aligned money, consistent currency format | 1 | `.num` tabular-nums; `td.r` right-aligned; `usd()` formatter. |
| 9 | Status with text + colour | 1 | Pills have text labels like "16 days late" and "Card declined", plus a dot and colour. |
| 10 | App shell: nav with current section, search, account | 0 | Header has a breadcrumb and buttons only; no nav, search or account. |

TOTAL: 6/10
