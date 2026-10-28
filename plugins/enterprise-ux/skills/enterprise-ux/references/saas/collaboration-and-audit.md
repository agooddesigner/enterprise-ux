# Collaboration, history and audit

**Load when:** designing audit logs, record activity history, "last edited by", versioning, real-time multiplayer editing, conflict handling, offline sync, presence, save/reconnect states, or comments and mentions.

## 1. Audit log — what to record

Every entry has (Pangea, GitHub):

| Field | Notes |
|---|---|
| Timestamp | Absolute, with time zone (see `foundations/defaults.md`); ISO 8601 in exports |
| Actor | User, API key, integration or **agent** — typed and linked; show "on behalf of" for delegated/agent actions |
| Source | IP, user-agent, location/country |
| Action | Stable `category.operation` key (e.g. `repo.create`) + human label |
| Target | Record + owner IDs, org/workspace, affected user |
| Status | Success / Failed (with reason) |
| Message | Short human description |
| Old value → New value | Lets admins reconstruct and revert |

- Log security-relevant **configuration** changes too: role changes, SSO/SCIM changes, approval-rule edits and approval requests (Stripe's "Security history"). (Stripe)
- Each AI/agent action gets a unique ID and an audit trail; an action counts as accepted if not reversed within a set window. (Smashing agentic AI) See `saas/ai-features.md`.

## 2. Audit log — UI

- **Default to a recent window** (GitHub shows the last 3 months; older needs an explicit date range). (GitHub)
- Search and filters: action, actor, target/owner, status, source, date range; filter state in the URL. (GitHub, Pangea; Cloudscape persistence)
- Table: timestamp, actor, action, target, status, source; row opens a side panel with full details and old/new diff. (NN/g data tables) See `patterns/tables.md`.
- Show old → new values side by side; long JSON in a collapsible, monospaced block. (Pangea; general practice for layout)
- **Export** filtered results as CSV/JSON + API access. (inference — general practice)
- **Retention** configurable by an owner (GitHub default: indefinite); show the policy on the page. (GitHub)
- **Streaming / forwarding to SIEM** for enterprise tiers, with destination status and last delivery. (GitHub)
- **Immutability**: state plainly that entries can't be edited or deleted by anyone in the product. (general practice — not covered by fetched sources)
- Access: owners and security/IAM admins only; viewing the audit log is itself logged. (general practice)
- Never use relative times as the only timestamp in audit views. (Pajamas, see `foundations/defaults.md`)

## 3. Activity history on records

- Per-record "Activity" tab or side panel: who did what, when, old → new, newest first. (Pangea fields applied per record)
- Relative times with absolute on hover in activity feeds. (see `foundations/defaults.md`)
- Group bursts of edits by the same actor within a short window into one entry ("Priya edited 4 fields"). (general practice)
- Link to the full audit log filtered to this record for admins. (general practice)
- Attribution pattern: "[Noun] [verb] by [linked name]" ("Status changed by Leo M."). (Cloudscape)

### "Last edited by"

- Show "Edited 12 min ago by Priya S." near the record title or in the header metadata. (Cloudscape timestamp pattern)
- Absolute time on hover; link the name to the person; link "Edited" to history. (Pajamas, Cloudscape)

## 4. Versioning

- Use versions for documents, configs and policies where reverting a whole state matters; use field-level history for structured records. (general practice)
- Version list: timestamp, author, optional name/label, change summary; "Restore this version" creates a **new** version rather than deleting later ones. (general practice)
- Compare two versions side by side with additions/removals marked by text or symbol, not colour alone. (WCAG 1.4.1)
- Version history UI specifics were not covered by fetched sources — treat this section as general practice.

## 5. Real-time collaboration and conflicts

### Pick a conflict strategy per field type

| Field type | Strategy | Behaviour |
|---|---|---|
| Structured fields (status, assignee, numbers, dates, shape properties) | Server-ordered **last-writer-wins** per property | Edits to different properties never conflict; same-property edits replace atomically (Figma, Linear) |
| Long-form rich text (descriptions, docs) | **CRDT or OT** | Concurrent typing merges character by character (Google Docs OT; Linear uses CRDTs only for descriptions) |
| Lists/order | LWW on position key, or CRDT list (general practice) | Avoid reordering under a user mid-drag |

(Figma multiplayer, Liveblocks)

- Local edits apply instantly; ignore incoming server values that conflict with your own **unacknowledged** local edits, to prevent flicker. (Figma)
- Conflicts are rare in issue-tracker-style data; don't build merge UIs for structured fields. (Liveblocks on Linear)
- For non-real-time forms where two people edit the same record, detect staleness on save and show what changed and by whom, offering to review before overwriting (general practice).

### Multiplayer undo

- Undo reverts **your** changes only and must not overwrite others' later edits. (Figma)
- Invariant: undo many steps, copy something, redo all → document unchanged. (Figma)

### Offline and reconnect

- Queue edits locally; on reconnect, fetch fresh state and replay the queue. (Figma, Liveblocks)
- Client-generated IDs let users create objects offline. (Figma, Liveblocks)
- Tell users when they're offline and how many changes are pending; never silently drop edits. (general practice)

### Presence

- Presence (cursors, selections, "typing…", avatars of who's viewing) is a separate broadcast channel from document data. (Liveblocks)
- Show avatars of current viewers in the record header; overflow to "+3". (general practice)
- Indicate when someone else is editing the same field (outline/label with their name). (general practice)
- Presence is decoration on top of data — it must never block editing. (general practice)

### Saving and connection states

- Figma cut worst-case data loss from ~60 s to <1 s with a write journal; 95% of changes persisted in ~600 ms. (Figma reliability)
- Show "Saving…" only while changes are pending; then "Saved" (or nothing). (Figma — UI is inference; Pajamas autosave states)
- Show a short "Reconnecting…" / "Catching up…" state, then return to normal. (Figma — inference)
- Long operations on large files can take 4 s+ at p95 → show progress, never look frozen. (Figma)
- Failed save: persistent inline alert "Failed to save 3 changes" + Retry; warn if the user tries to leave. (Pajamas)
- Announce save/connection status via `role="status"`. (WCAG 4.1.3)

## 6. Comments and @mentions

Not covered by fetched sources — the following are general practice:
- Anchor comments to the object (record, field, region) they discuss; show a count indicator on that object.
- Threads with resolve/reopen; resolved threads collapse but stay searchable.
- @mention autocomplete scoped to people who **can access** the object; warn when mentioning someone without access and offer to share or request access (ties to `saas/accounts-and-permissions.md`).
- A mention is human-originated → high-priority notification (Smashing notifications); see `saas/notifications-system.md`.
- Let users leave notes on data and charts so they can resume after interruptions. (NN/g complex apps)

## Common AI failures

- Audit log with relative-only times, no time zone, no actor type, no old/new values.
- Audit log that loads "all time" by default and times out.
- No distinction between human, API-key and agent actors.
- Audit entries editable or deletable by admins in the UI.
- "Saving…" indicator that flickers on every keystroke, or never resolves after a failure.
- Whole-record last-writer-wins that silently overwrites a teammate's field edit.
- Global undo that reverts other people's edits.
- Offline edits dropped without notice on reconnect.
- @mention list that includes people who can't open the record.

## Sources

- https://pangea.cloud/blog/audit-log-field-guide-time-travel-and-humblebrags/
- https://docs.github.com/ja/enterprise-server@3.5/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/about-the-audit-log-for-your-enterprise
- https://docs.stripe.com/account/approvals.md
- https://smashingmagazine.com/2026/01/beyond-generative-rise-agentic-ai-user-centric-design/
- https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
- https://www.figma.com/blog/making-multiplayer-more-reliable/
- https://development.liveblocks.io/blog/understanding-sync-engines-how-figma-linear-and-google-docs-work.md
- https://cloudscape.design/patterns/general/timestamps/
- https://cloudscape.design/patterns/general/filter-patterns/filter-persistence-in-collection-views/
- https://design.gitlab.com/content/date-and-time/
- https://design.gitlab.com/patterns/saving-and-feedback/
- https://nngroup.com/articles/data-tables
- https://www.nngroup.com/articles/complex-application-design/
- https://smashingmagazine.com/2025/07/design-guidelines-better-notifications-ux/
- https://w3c.github.io/wcag/understanding/status-messages.html
