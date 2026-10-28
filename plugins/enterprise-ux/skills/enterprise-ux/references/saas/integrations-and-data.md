# Integrations, API keys and data movement

**Load when:** designing developer settings (API keys, webhooks, OAuth apps), integration catalogs and connection settings, CSV/XLSX import, data export, or a command palette (⌘K).

## 1. API keys

### Key types — show exposure level

| Type | Safe where | Default? |
|---|---|---|
| Publishable | Client-side code | For client SDKs only |
| Restricted (scoped) | Server, with only needed permissions | **Recommended default** |
| Unrestricted secret | Server; full access | Discouraged for new uses |
| Org-level | Across accounts | Admins only |

(Stripe)

- Use **visible prefixes** so keys self-identify: `pk_`, `rk_`, `sk_`, plus `_test_` / `_live_`. (Stripe)
- Separate **test/sandbox vs live** with a clear, persistent mode toggle; objects never cross modes; live mode visually distinct (label, not colour alone). (Stripe; WCAG 1.4.1)

### Creating a key

1. **Step-up auth** (email/SMS code or re-auth) before creating a secret key. (Stripe) Allow pasting codes (WCAG 3.3.8).
2. Name + scope/permission picker (least privilege; preselect read-only). (Stripe best practices)
3. Optional: mark the key as used by an autonomous agent → default approval rules apply to high-risk actions. (Stripe) See `saas/ai-features.md`.
4. **Show once**: full secret with click-to-copy, warning that it can't be retrieved later, and a note field to record where it's stored. (Stripe)
5. Afterwards, list shows only a masked key (prefix + last 4). (general practice)

- Never put the key in a toast — users must copy it. (Fiori; see `foundations/defaults.md`)

### Managing keys

- Key list columns: name, type, prefix…last4, mode, created by, created, last used, expiry. (Stripe; general practice for columns)
- Per-key overflow: edit name/note, **rotate**, expire, manage **access policy** (IP/CIDR, ASN, country, block Tor/VPN/proxies), view **request logs**. (Stripe)
- **Rotation with grace period**: old and new keys both work for a configurable window (up to 7 days), with a visible countdown; advise expiring the old key only once its traffic reaches zero. (Stripe)
- **Leaked key detection**: vendor detects exposed keys, notifies owners, and may deactivate them — the UI shows why a key was disabled and how to rotate. (Stripe)
- Least privilege on who can create or view keys; never ask users to send you their secret. (Stripe)
- Expiring/revoking a key is destructive for integrations → confirmation naming the key and recent usage. (Cloudscape delete tiers)

## 2. Webhooks

- Endpoint list: URL, status (Enabled / Disabled / Failing), subscribed events count, last delivery result. (GitHub, Stripe — UI layout is inference)
- **Event picker**: subscribe to the minimum events needed; searchable, grouped by resource. (GitHub)
- **Signing secret per endpoint**, separate from API keys; reveal on demand with step-up, copy, rotate. (GitHub, Stripe)
- Require HTTPS with SSL verification on by default; warn loudly if a user disables it. (GitHub)
- **Deliveries** view: delivery ID, event type, timestamp, response code, duration, request/response bodies; **Redeliver** button per delivery. (GitHub)
- Document and surface the ack window: receivers must return 2xx fast (GitHub: 30 s) and process asynchronously. (GitHub)
- Unique delivery ID for idempotency and replay protection — display it. (GitHub)
- Notify endpoint owners when deliveries fail repeatedly or an endpoint is auto-disabled. (general practice; Vercel integration notices)
- Test-send button for a sample event. (general practice)

## 3. Integrations and OAuth apps

- Catalog: search, categories, recommended first; installed state visible. (lawsofux choice overload)
- Install flow shows requested **scopes** in plain language before consent, who installed it, and what data it can reach. (PAIR data-scope principle; general practice)
- **Notify owners when an integration's scopes change or it gets disabled.** (Vercel)
- Admins can restrict which apps can be installed (allow-list). (Notion enterprise controls)
- Connection settings page: status, connected account, last sync, errors with fix, disconnect (with consequence). (WorkOS self-serve principle)

## 4. CSV / spreadsheet import

Flow (Flatfile, Dromo):
1. **Before upload**: state requirements (formats, max size/rows, required columns) and offer a **downloadable template**. (Dromo)
2. **Upload** CSV/XLS/XLSX with progress. (Flatfile; Ant upload)
3. **Confirm header row**; auto-label columns if there is none. (Flatfile)
4. **Map columns**: auto-suggested mapping the user confirms or overrides; allow discarding unneeded columns. Resolve unmapped required fields here instead of failing. (Flatfile, Dromo)
5. **Map enum values** (e.g. "NY", "New York" → `new_york`). (Flatfile)
6. **Validate inline**: cell-level, specific errors ("Invalid email in row 37") with suggested fixes. (Dromo)
7. **Fix in place** in a grid; filter "Show only rows with errors"; count of remaining errors. (Flatfile)
8. **Import** → result summary: created, updated, skipped, failed + downloadable **error report** for failed rows. (Dromo; NN/g completion dialog)

- Cache mappings for repeat imports from the same source. (Flatfile)
- Large files: chunk/stream (e.g. 5–10k rows per chunk), process in the background with progress, and notify on completion. (Dromo)
- Be liberal in accepted formats (dates, phone numbers), normalize, and tell users what you changed. (lawsofux Postel)
- Never silently drop rows. (general practice)
- Vendor sources; their performance stats are marketing — don't cite them.

## 5. Export

General practice (no fetched source on export UX):
- Export **respects current filters, sort and visible columns**, and says so ("Export 1,204 filtered rows"); offer "All rows" as an explicit alternative.
- Small exports download directly; large ones run **async**: confirm start, show in a jobs list, notify on completion with a link that expires after a stated time. (NN/g >10 s rule: run in background + notify)
- Formats: CSV for spreadsheets, JSON for systems; ISO 8601 dates, raw numbers without locale grouping, UTF-8 with BOM for Excel compatibility (general practice). (see `foundations/defaults.md`)
- Admin-controlled export permissions; exports of sensitive data are audit-logged. (Notion; see `saas/collaboration-and-audit.md`)
- Connect to the tools users already use: Excel, PPT, copy chart as image. (NN/g complex apps)

## 6. Command palette (⌘K)

- One global shortcut (⌘K / Ctrl+K) available on every screen; pressing it again closes the palette and **returns focus** where it was. If an editor already uses ⌘K (insert link), a second press opens the palette. (Superhuman)
- **Every action is a command**, navigation included ("Go to Billing"); register commands independent of UI. (Superhuman)
- Case-insensitive **fuzzy matching** with a tuned cutoff; **aliases/synonyms** including competitors' terms, shown as "Title (matched alias)" so users learn your vocabulary. (Superhuman)
- Before typing: useful default list; boost recent, frequent and context-relevant commands; hide commands only when wholly irrelevant; contextual actions only when they can run. (Superhuman)
- **Context awareness**: on a record page, "Assign" targets that record. (Solomon)
- Show each command's **keyboard shortcut** in results so the palette teaches shortcuts. (Superhuman; NN/g accelerators)
- ~5 visible results with the last one cut off to hint at scroll; icon per command. (Superhuman)
- Decide whether search lives inside the palette (small apps) or is a peer of it (search-centric apps); define where the palette hands off to normal UI. (Solomon)
- Use the palette for actions too many or too situational for dedicated shortcuts. (Solomon)
- Linear pattern: single-key shortcuts for frequent actions, two-key sequences for navigation (G then I), palette searches the local store instantly, every action still reachable by mouse. (Linear)
- Never override Ctrl/⌘ + C/V/A/P; shortcuts are optional, never the only path. (NN/g accelerators)
- Accessibility: combobox + listbox semantics, arrow-key navigation, announced result count. (WAI-ARIA APG combobox; see `foundations/accessibility.md`)
- Respect permissions: commands the user can't run are hidden, not shown-then-failed. (Fiori)

## Common AI failures

- Showing the full secret key in the list forever, or never showing it with a copy button at creation.
- No test/live separation; one "API key" with full access as the only option.
- Rotate = instant revoke, breaking production integrations with no grace period.
- Webhook settings with no delivery log or redeliver button.
- CSV import that rejects the whole file on the first bad row with "Invalid file".
- No mapping step — requiring exact header names.
- Export that ignores active filters, or blocks the UI for a 2-minute export.
- ⌘K palette that only searches pages, shows no shortcuts, and loses focus on close.

## Sources

- https://docs.stripe.com/keys
- https://docs.stripe.com/keys-best-practices.md
- https://docs.stripe.com/account/approvals.md
- https://docs.github.com/en/enterprise-server@3.18/webhooks/using-webhooks/best-practices-for-using-webhooks
- https://vercel.com/docs/notifications
- https://workos.com/docs/directory-sync.md
- https://www.notion.com/en-gb/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
- https://flatfile.com/blog/optimizing-csv-import-experiences-flatfile-portal/
- https://dromo.io/blog/5-best-practices-to-streamline-your-csv-import-process
- https://blog.superhuman.com/how-to-build-a-remarkable-command-palette/
- https://solomon.io/designing-command-palettes/
- https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
- https://www.nngroup.com/articles/ui-accelerators/
- https://www.nngroup.com/articles/complex-application-design/
- https://www.nngroup.com/articles/designing-for-waits-and-interruptions/
- https://pair.withgoogle.com/chapter/explainability-trust/
- https://cloudscape.design/patterns/resource-management/delete/
- https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/message-toast/usage
- https://lawsofux.com/postels-law/
- https://lawsofux.com/choice-overload/
- https://ant.design/docs/spec/data-entry
- https://w3c.github.io/wai-website/ARIA/apg/patterns/combobox/
- https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum
