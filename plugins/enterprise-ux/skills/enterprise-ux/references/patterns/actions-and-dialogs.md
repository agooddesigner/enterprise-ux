# Actions and dialogs

**Load when:** placing or labelling buttons, deciding disabled vs hidden, designing delete/destructive or bulk flows, choosing modal vs popover vs side panel vs page, specifying dialog mechanics, or adding keyboard shortcuts.

House defaults for delete friction, disabled submit, modal initial focus and selection scope live in `foundations/defaults.md`.

## 1. Button hierarchy and placement
- **One primary per view/container.** Cancel is never primary. **[consensus]** (Carbon, Atlassian, Fiori, Lightning, Cloudscape, GOV.UK, Ant)
- No obvious primary → all default/secondary buttons. (Ant). Alt: Ant gives Cancel primary styling when the system doesn't recommend the destructive action — the house rule (`foundations/defaults.md`) keeps Cancel non-primary; instead give no button primary emphasis and style the destructive one as danger-secondary.
- Cloudscape header order (left → right): status toggles (Activate/Deactivate) far left → View details → Edit → other actions → Delete → other Creates → primary Create [resource] (rightmost). (Cloudscape)
- Count: **<5 actions → separate buttons. ≥5 → keep the primary, collapse the rest into a button dropdown of 5–15 items** (add filtering if long). (Cloudscape)
- Row and container dropdowns: **≤7 items.** (Cloudscape). ActionMenus cap ~15. (Primer)
- Row actions in the last column, sticky: 1–2 repetitive actions inline (link/icon buttons); >2 → icon-button dropdown. (Cloudscape, Carbon, Fiori, NN/g). Detail in `patterns/tables.md`.
- Fiori placement: global non-finishing actions (Share, Edit, Delete) in the header; table actions in the table toolbar; **finishing actions (Save, Cancel, Submit) only in the footer**. Never a column of buttons. (Fiori)
- In-page forms: buttons left-aligned with fields (Save, then Cancel). Dialogs and wizards: right-aligned, Cancel left of primary. (Carbon, Primer)
- Leave space between adjacent buttons so they don't read as a toggle group. (Ant). Use buttons for actions, links for navigation. (Polaris)

### Overflow (kebab/meatball) menus (NN/g)
- Only for secondary actions; keep frequent actions visible.
- **1–2 actions → skip the menu**, show them.
- Trigger sits next to its object, always visible (not hover-only; touch always shows). (NN/g, Carbon)
- Specific accessible name: "Actions for Invoice 1042", not "Options". (NN/g, APG)
- Never mix global and item actions in one menu. Hamburger = main nav only. (NN/g)
- Use `role="menu"` only for action menus; arrows move, Esc closes and returns focus. (APG)

## 2. Labels
- Specific imperative verb, 1–2 words; verb + object when context is unclear ("Create distribution", "Edit issue"). **[consensus]** (Carbon, Atlassian, Cloudscape, Pajamas, Polaris)
- Never "OK", "Done", "Yes", "Exit", "Submit" when a precise verb exists. (Primer, PatternFly, Carbon)
- Sentence case, no end period, no articles ("Create page"). (Atlassian, see foundations/defaults.md)
- Ellipsis only when the action needs more input before running ("Export…"). (Atlassian)
- No ">", "»", "+" characters in labels; use icons. (Pajamas, PatternFly)
- Same action, same word everywhere. "Create" = new record; "Add" = attach existing. (Fiori, WCAG 3.2.4)
- Wizards: replace "Finish" with the outcome ("Create network"). Multi-step dialog: last button names the final action. (PatternFly, Carbon)
- Icon-only buttons need a tooltip and accessible name containing any visible text. (Ant, WCAG 2.5.3)

## 3. Disabled vs hidden vs read-only vs inactive

| State | Use when | Source |
|---|---|---|
| Hidden | User can never perform it (authorization, irrelevant row action) | Fiori, Cloudscape |
| Disabled + reason | User must do a step first (Delete with nothing selected); or lacks permission but should know it exists | Cloudscape, Pajamas, Fiori |
| Read-only | Value is real and submitted but not editable (inherited, SSO-managed) | Cloudscape, Pajamas |
| Plain text | Review step, display mode | Cloudscape |
| Inactive | Feature temporarily unavailable; looks muted but stays focusable and explains on click/hover | Primer |
| Enabled + validate on click | Save/Submit with incomplete input | see foundations/defaults.md |

- Keep Create/Add and whole-table Edit always enabled; disable selection-dependent actions until valid. (Fiori)
- **Primer decision tree** for a non-functional control: (1) remove it if removal won't disorient; (2) else use an inactive button that can be focused and explains itself; (3) disable only as a last resort. Never disable because a backend is down. (Primer)
- Tooltips on disabled buttons fail: disabled elements can't take focus. Put the reason in visible text, or use `aria-disabled` so the control stays focusable. (Primer; `aria-disabled` is general practice)
- If a setting is locked or inherited, say so and name who set it — users shouldn't have to guess why it won't change. (Pajamas, Notion)
- **Disabled-reason templates** (Cloudscape): one sentence what + why, optional next step; tooltip for short, inline alert/text for long; no interactive content inside.
  - "Available in [constraint]" — "Available in the Enterprise plan."
  - "Available when [future action]" — "Available when the instance is stopped."
  - "Unavailable due to [technical constraint]" — "Unavailable due to an active export."
  - Locked: "Managed by your organization" / "Restricted by [admin/policy]". (WorkOS, Notion)

## 4. Destructive actions

### Friction tiers (see foundations/defaults.md)
| Tier | When | Mechanics | Source |
|---|---|---|---|
| None + Undo | Reversible, single item, cheap to recreate, no running impact | Act immediately; Undo in message | Cloudscape, Ant, Pajamas |
| Confirmation modal | Irreversible single item, or slow/costly to recreate, or bulk non-critical | Modal naming object + consequence | Cloudscape, Pajamas |
| Typed confirmation | Irreversible + cascading, critical, bulk-critical, deletes contained items | Modal + text input; primary disabled until it matches | Cloudscape, Pajamas |

- Score tiers by severity (outage risk, effect on other resources), recreation cost (include provisioning time) and prerequisites. (Cloudscape)
- Never one-click delete for bulk, running resources, or expensive-to-recreate resources. Alt: Pajamas allows no friction for low-severity bulk actions that **can be undone** — reversibility decides. (Cloudscape, Pajamas)
- Medium severity without undo: add one extra step (bury in a dropdown). (Pajamas)
- Confirm in a modal, never a popover or separate page, for tiers 2–3. (Cloudscape). Alt: Ant Popconfirm next to the trigger for low-stakes confirms (section 6).
- Danger (red) primary only for hard/impossible-to-undo actions; never rely on red alone. (Carbon, GOV.UK, Polaris)

### Typed confirmation variants
- Type the **resource name** when deleting the wrong item is the main risk (Pajamas); show the name as the input's description.
- Type a fixed word ("delete"/"confirm", case-insensitive, localized) when names are long IDs or must localize. (Cloudscape)
- Unmet prerequisite → disable both input and primary until done. (Cloudscape)
- Allow paste into the field. (general practice; avoid cognitive tests, WCAG 3.3.8 spirit)

### Modal content
- Title: "Delete [resource type]?" — domain verb if different ("Terminate instance?"); singular/plural to match. (Cloudscape, PatternFly)
- Body: resource name **in bold**; "You can't undo this action."; consequences and cascades, listing contained items (issues, forks, members). (Cloudscape, Pajamas, Atlassian)
- Alternatives: deactivate, archive, snapshot first; prerequisite links open in new tab. (Cloudscape, Pajamas)
- Duration if not instant. Restore/grace window with exact deadline if one exists. (Cloudscape, Pajamas)
- Emphasis: house default = bold text and a consequence list; Alt: Cloudscape info/warning alert inside the modal. Pajamas forbids alerts in modals.
- Buttons: "Delete" + "Cancel" (Cloudscape, Ant). Alt: Pajamas verb+object on both ("Yes, delete project" / "Cancel, keep project").
- Initial focus: Cancel (least destructive). Never pre-focus the destructive button. (APG, Lightning)
- After: feedback where the user lands (flashbar/inline), with progress if async. (Cloudscape)
- Financial/legal/data-modifying submissions must be reversible, validated, or confirmed. (WCAG 3.3.4)

## 5. Undo, soft delete, bulk actions

### Undo
- Prefer Undo over confirmation. (Ant, NN/g, Nielsen #3). Over-confirming trains click-through. (Nielsen #5)
- Ant pattern: success message with Undo; remove both after **1 minute** or on Undo. (Ant)
- Undo must also exist outside the toast (menu, history, trash) so a timed message isn't the only path. (Polaris, APG)
- Autosaved fields: undo inline, not in a toast. (Pajamas)
- Multiplayer: undo reverts only *your* changes. (Figma) See `saas/collaboration-and-audit.md`.

### Soft delete
- Move to Trash/Archive with a stated retention ("Deleted items are kept for 30 days"), restore action, and purge as a separate tier-3 action. (general practice; Pajamas restore window)

### Bulk actions
- Scope: header checkbox selects the visible page; explicit "Select all N matching"; always show "N selected". (see foundations/defaults.md; PatternFly, Cloudscape)
- Bulk actions bar replaces the toolbar on selection; row actions disabled in batch mode; Cancel exits. (Carbon)
- Partial applicability: run on every item that can be processed; **before** running, say how many will fail and why, let user continue or cancel; if unknowable, report after. (Fiori)
- Large batches run as background jobs with "Updating 3 of 50", Cancel, "Run in background". (NN/g)
- Report: **succeeded / failed / skipped counts**, reasons for failures, link to failed items, retry failed only. (NN/g, Fiori)
- Keep selection after a global action until the user changes it (PatternFly) — but clear it when items no longer exist.
- Batch confirm copy names the count and scope: "Delete 42 invoices?" (APG alertdialog example)

## 6. Modal vs non-modal vs popconfirm vs side panel vs page

| Need | Use | Source |
|---|---|---|
| Critical warning: irreversible or work could be lost | Modal / alertdialog | NN/g, Carbon |
| Info required to continue; one quick question | Modal | NN/g |
| Short create with <8 fields | Modal | Fiori |
| Low-stakes confirm anchored to trigger, no undo possible | Popconfirm | Ant |
| Edit/inspect a record while referencing the list | Non-modal side panel / drawer | NN/g, Ant |
| Task users switch back and forth from (compose, notes) | Non-modal dialog, minimizable | NN/g |
| Long, complex, many fields, tables, multi-step, high stakes (checkout) | Full page | NN/g, Carbon, Fiori |
| Details shareable/linkable | Page | Ant |
| Explain a term | Tooltip (text) / popover (links, click-opened) | Pajamas, Ant |

**Don't use a modal** for: promotions/unrelated content, complex decisions that need the content it covers, errors easier fixed in place, minor reversible issues, success announcements. (NN/g, Carbon). A modal too long for Large becomes a page. (Carbon). On mobile a non-modal can become blocking — test. (NN/g)

## 7. Dialog mechanics
- **Only user-initiated.** No unprompted system pop-ups (NPS, promos); system alerts go to toasts/notifications. (Carbon)
- **Never a modal on a modal.** **[consensus]** (Carbon, Atlassian)
- One primary on the right, Cancel left; with 3 buttons only the rightmost is primary. (Carbon, Atlassian, Fiori, Lightning)
- Title verb = button verb ("Delete contact?" → "Delete"). **[consensus]** (Carbon, Atlassian, Lightning)
- Focus: move in on open — first input; no inputs → Cancel for destructive, primary for informational; long content → `tabindex="-1"` heading. Trap Tab, Esc closes, return focus to the trigger (or the logical next target if it's gone). (APG, see foundations/defaults.md)
- Close: X and Esc always; backdrop click only on passive dialogs — never discard typed input on backdrop click. (Carbon)
- Unsaved input in a dialog being closed → confirm only if something changed. (Cloudscape)
- Scroll: header and footer fixed, **body only**; never horizontal. (Carbon, Lightning)
- Sizes: default ~50% viewport, large ~90% (Lightning); body text ~80% width (Carbon); 4rem from top/bottom when overflowing; full-screen on phones except message dialogs (Fiori).
- Submit: validate before closing, keep open with inline errors; errors stay inside the dialog under its header (Carbon, Primer). Loading: spinner on the button for short waits, body overlay + disabled primary for longer. (Carbon)
- Avoid inside dialogs: tabs, accordions, links that navigate away, tables with batch actions. (Carbon)
- Semantics: `role="dialog"`/`alertdialog`, `aria-modal`, `aria-labelledby` title, inert background (native `<dialog>.showModal()`). (APG)
- Motion: backdrop fade ~0.1s, scale 0.9→1.0. (Lightning). See `foundations/visual-and-motion.md`.

## 8. Approvals and two-person rule
- Sensitive actions (refunds, bank changes, admin invites, agent-triggered high-risk actions) may require a second approver: requester can't approve own request, requests expire, justification captured, all events audited. Details: `saas/accounts-and-permissions.md`. (Stripe)
- In the UI, the action button becomes "Request approval"; show pending state on the object. (general practice)

## 9. Keyboard shortcuts and accelerators
- Shortcuts only for frequent core actions; always optional, never the only path. (NN/g)
- **Never override Ctrl/⌘+C, V, A, P** or screen-reader/browser keys. (NN/g, general practice)
- Show shortcuts right-aligned in menus and in tooltips; offer a `?` cheat sheet; don't rely on hover-only hints. (NN/g)
- Teach in context: hint right after the user does it the slow way. (NN/g)
- Visible feedback for every shortcut; undo for risky ones. (NN/g)
- Let experts customize. **Single-character shortcuts** must be turn-off-able, remappable to include a modifier, or active only on focus. (WCAG 2.1.4)
- Ctrl/⌘+Enter submits from any field; Enter submits single-line inputs only. (Pajamas)
- Global command palette (⌘K): one shortcut on every screen, shows each command's shortcut so it teaches them, every action still reachable by mouse — see `patterns/filters-and-search.md`. (Superhuman, Linear)

## Common AI failures
- Two or three filled primary buttons in one header or modal.
- "OK"/"Submit"/"Yes" labels and dialog titles that don't match the button verb.
- Kebab menus holding a single action, or hiding the most-used action.
- Disabled Save with no reason, or a reason only in a tooltip on the disabled button.
- "Are you sure?" confirms for reversible actions instead of Undo; no typed confirmation for cascading deletes.
- Delete modals that don't name the resource or list what else gets deleted.
- Bulk actions that report only "Done" without succeeded/failed/skipped counts.
- Complex forms, tabs or tables crammed into modals; modals opening other modals.
- Auto-opened modals (NPS, what's-new) on page load.
- Single-key shortcuts with no off switch; overriding Ctrl+A in tables.

## Sources
- https://carbondesignsystem.com/patterns/dialog-pattern
- https://carbondesignsystem.com/components/modal/usage
- https://carbondesignsystem.com/components/data-table/usage/
- https://atlassian.design/components/modal-dialog/usage
- https://atlassian.design/foundations/content/designing-messages/warning-messages
- https://atlassian.design/foundations/content/language-and-grammar
- https://spring-21.lightningdesignsystem.com/guidelines/messaging/components/modals
- https://www.sap.com/design-system/fiori-design-web/v1-151/ui-elements/dialog/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/usage
- https://cloudscape.design/patterns/resource-management/delete/
- https://cloudscape.design/patterns/resource-management/delete/delete-with-additional-confirmation/
- https://cloudscape.design/patterns/resource-management/delete/delete-with-simple-confirmation/
- https://cloudscape.design/patterns/general/actions/global-actions/
- https://cloudscape.design/patterns/general/actions/incontext-actions/
- https://cloudscape.design/patterns/general/disabled-and-read-only-states/
- https://cloudscape.design/patterns/general/unsaved-changes/
- https://primer.style/ui-patterns/degraded-experiences
- https://primer.style/product/ui-patterns/saving
- https://primer.style/product/ui-patterns/navigation
- https://www.patternfly.org/patterns/bulk-selection/
- https://patternfly.org/components/wizard/design-guidelines
- https://design.gitlab.com/patterns/destructive-actions/
- https://design.gitlab.com/patterns/forms/
- https://design.gitlab.com/patterns/settings-management
- https://cdn.jsdelivr.net/npm/superv5_polarisui@2.0.1/dist/docs/components/Button/README.md
- https://cdn.jsdelivr.net/npm/superv5_polarisui@2.0.1/dist/docs/components/Toast/README.md
- https://design-system.service.gov.uk/components/button/
- https://ant.design/docs/spec/buttons.md
- https://5x.ant.design/docs/spec/stay
- https://ant.design/docs/spec/feedback
- https://ant.design/docs/spec/data-list
- https://nngroup.com/articles/modal-nonmodal-dialog/
- https://www.nngroup.com/articles/contextual-menus-guidelines/
- https://www.nngroup.com/articles/ui-accelerators/
- https://www.nngroup.com/articles/progress-indicators/
- https://nngroup.com/articles/data-tables
- https://w3c.github.io/wai-website/ARIA/apg/patterns/dialog-modal/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/alertdialog/
- https://w3c.github.io/wai-website/ARIA/apg/patterns/menu-button/
- https://docs.stripe.com/account/approvals.md
- https://www.notion.com/en-gb/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
- https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
- https://www.w3.org/TR/WCAG22
- https://blog.superhuman.com/how-to-build-a-remarkable-command-palette/
- https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
- https://www.cs.princeton.edu/courses/archive/spring13/cos436/handouts/Heuristics_explained.pdf
