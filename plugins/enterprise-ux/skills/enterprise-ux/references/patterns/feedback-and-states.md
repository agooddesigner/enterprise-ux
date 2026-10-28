# Feedback and states

**Load when:** designing or auditing any view's states (empty, loading, error, permission, degraded), choosing a feedback component (inline, toast, banner, modal, notification), writing message copy, or stress-testing a screen with edge data.

House defaults for toasts, loading thresholds, empty cells and zero-results CTAs live in `foundations/defaults.md`. They win over anything below that seems to differ.

## 1. State model: fill this matrix for every view

Design each row explicitly per container (page, table, card, panel). An unspecified state is a bug. **[consensus]** (Carbon, Cloudscape, Primer, NN/g)

| State | Trigger | Show | Never |
|---|---|---|---|
| Ideal | Data present, normal volume | Content, counts, last-updated where data ages | — |
| First-use empty | No objects exist yet | Empty state: what will appear here, why it's empty, one next step (Carbon, Cloudscape) | An empty table shell with headers (Carbon) |
| No results | Filter/search returned 0 | "No results for …" + "Clear filters" secondary button (see foundations/defaults.md) | First-use copy or a Create CTA (Cloudscape, PatternFly) |
| User-cleared | User finished/archived everything | Neutral or lightly celebratory "all done" copy; brief if frequent (Atlassian, Carbon) | Confetti on a daily action (Atlassian) |
| Initial loading | First fetch of container | Skeleton matching the layout after ~300ms (see foundations/defaults.md) | "No records" text (NN/g); skeleton on buttons/menus (Carbon) |
| Refreshing | Re-fetch, filter change | Keep old data visible and usable, mark busy, update "last updated" (Cloudscape, Fiori) | Blanking the view to a spinner |
| Partial error | Some sections/fields failed | Section-level error in that container only; rest stays usable (Cloudscape, Primer) | Whole-page error; generic empty state (Primer) |
| Full error | Core data/function unavailable | Error state with cause + Retry/Reload + report option (Cloudscape, Primer) | "No data" (implies data is gone) (Primer, NN/g) |
| No permission | User lacks access | "Access permissions needed" + request access as top resolution (PatternFly, Carbon); hide CTAs the user can't use (Lightning, Fiori) | "Access denied", error codes (PatternFly) |
| Read-only | User can view, not edit | Values as text/read-only fields, explanation of why ("Managed by your organization") (Pajamas, Cloudscape) | Disabled-looking fields with no reason (Pajamas) |
| Degraded / outage | Backend or dependency down | Degrade per Primer rules (section 5) | Disabling controls silently; removing the global header (Primer) |
| Overflow | Too many items, long values | Pagination/"Show all (n)", truncation with full string available (Fiori, PatternFly) | Rendering >1,000 items in one responsive list (Fiori) |

Plan four states for every async action: initiated, in progress, success (confirm if the user stays on the page), failed (cause + Retry). (Primer)

## 2. Empty states

### Types
- Carbon's three basics: **no data yet**, **after a user action** (no results), **error** (data exists but can't be shown: permission, system, config). Extras (inline docs, starter content, onboarding) always sit on top of a basic state, never replace it — users can skip or delete them. (Carbon)
- Also design: configuration required, no access, backend failure, success (PatternFly); higher tier needed (Pajamas); blank slate vs user-cleared (Atlassian).
- Use rich onboarding empty states only for primary features. See `saas/onboarding.md`. (Carbon)

### Rules
- Replace the whole container, including table headers, toolbar and footer. Never show the empty state and the table together. **[consensus]** (Carbon, PatternFly, Polaris)
- Say why it's empty and offer one next step. No dead ends, no "Nothing here". **[consensus]** (Carbon, Atlassian, Lightning, Fiori, NN/g)
- **Never use an empty state for errors.** Use an error state, flashbar or alert. (Cloudscape, Primer)
- **Never show "No records" while loading.** Show the loader until the fetch resolves. (NN/g)
- Keep the resource counter visible ("Distributions (0)"). (Cloudscape). Alt: hide a count of 0 in Fiori-style tables. (Fiori)

### CTA weight
- One action. House default: **secondary** button whose label matches the page's create label ("Create distribution"). (Cloudscape, Fiori, Carbon)
- Alt: Pajamas uses one primary and hides the page-header primary while the empty state shows — choose this when the empty state is the only content on the page. (Pajamas)
- Several empty states on one screen → tertiary buttons, text only, no illustrations. (Carbon)
- Hide the CTA if the user lacks permission to perform it. (Lightning, Fiori)
- Docs go as text links; a "Learn more" or "Load sample data" second path is fine. (Pajamas, NN/g). Lightning allows up to 2 CTAs.

### PatternFly sizes, icons, wording
- Size by context: XS in cards, S in tables/modals/wizards, L full page, XL getting-started/success. (PatternFly)
- Grey icon by default: rocket = first use, search = no results, wrench = configuration, lock = no access, plus-circle = creation; red exclamation = error; green check = success. (PatternFly)
- Wording: "No service accounts yet" (not "not found"), "Access permissions needed" (not "Access denied"), "Unable to connect" (not a code), "Configure your system" (not "You haven't configured…"). (PatternFly)
- No illustrations in small containers or when several empty states share a screen; illustrations are decorative (`alt=""`). **[consensus]** (Carbon, Lightning, Fiori)
- Error empty states are never playful; use the alert icon. (Primer)

### Copy limits
- Title: ≤5 words, no period (Pajamas); 1 line giving the reason (Fiori); bold, no end punctuation (Cloudscape).
- Body: ≤3 lines (Fiori), each line <66 characters (Lightning), 1–2 sentences (Atlassian). Don't repeat the headline. (Carbon, Atlassian)
- Lightning starts the headline with a verb; Fiori/Cloudscape use a noun phrase ("No distributions"). Pick one per product.

## 3. Loading

### Thresholds (see foundations/defaults.md)
| Wait | Show | Source |
|---|---|---|
| <~300ms | Nothing | Lightning, NN/g |
| Initial load of a container | Skeleton matching layout; tables = skeleton rows | Cloudscape, Carbon, Lightning |
| 1–10s in-component | Spinner with text ("Loading comments…") | NN/g, Cloudscape |
| >10s | Determinate progress, padded time estimate, Cancel, "Run in background", notify on completion | NN/g, Cloudscape |
| Batch over known count | "Updating 3 of 50" even when short | NN/g |

Alt: Primer switches to determinate from ~3s when progress is knowable — choose it for imports/exports with reliable counts. (Primer)

### Skeleton vs spinner
- Skeletons: initial/full load of containers (tables, cards, tiles). Spinners: async updates inside one component and user-started actions. **[consensus]** (Carbon, Lightning, Fiori, Cloudscape)
- Never skeleton action controls, toasts, menus, dropdown items or the modal itself. Animate skeletons. (Carbon)
- Skeleton shapes: simple, consistent height, load top-left → bottom-right; table skeleton ~20 rows fading 5%/row; skip skeletons for components that only render when they have data. (Lightning)
- One indicator per group of adjacent items, not one each. Avoid layout shift. (Primer)
- A spinner overlays content only with a mask between them. (Lightning)
- No ellipsis-in-text as a loader; use a real indicator. (Atlassian). In-progress labels use the single "…" character ("Downloading…"), no articles. (Pajamas, Cloudscape)

### Progressive loading
- Load structure and text skeletons first, then images, below-the-fold content, interactive parts. Show items as they arrive, most important first. (Carbon, Primer)
- Overview pages clear skeletons once the first card loads. (Fiori)

### Refresh keeps old data
- One refresh button per collection, in its header. Keep current data visible and usable; show "Last updated" after; announce via live region. Don't scatter refresh buttons. (Cloudscape)
- While filter results load, keep old content marked busy; grey out content that no longer matches. (Fiori)
- Near-real-time views may auto refresh (example 10s); auto-updating content must be pausable. (Cloudscape, WCAG 2.2.2)

### Background jobs
- >10s: let users leave. Offer "Run in background"; track in a notification center/task list. (NN/g, Ant)
- On completion show a **completion dialog or result view that stays until dismissed**: start, end, elapsed time, outcome counts (created, failed, skipped), link to logs. (NN/g)
- Result page title: Object + Action + Status; ≤2 next-step actions. (Ant)
- Give long processes a Stop/Cancel; offer Cancel only if it really rolls back. (NN/g, PatternFly)

- **Accessibility:** `role="status"` region always rendered; `aria-busy` during partial updates; one announcement per group; announce result counts ("5 items match"). (Primer, WCAG 4.1.3). See `foundations/accessibility.md`.

## 4. Errors and degraded experiences

### Error boundaries
- **Page-level** boundary replaces the page only when the core experience is gone. **Section-level** boundary replaces one container; the rest stays usable. Both offer Reload and Report. (Cloudscape, Primer)
- Default to section-level. A failing widget must never blank a dashboard or detail page. (Cloudscape)

### Copy
- What happened + why (if it helps) + how to fix. Lead with the likely fix. No blame, no "oops/sorry/please/invalid". **[consensus]** (Atlassian, PatternFly, Polaris, GOV.UK; see foundations/defaults.md)
- Raw codes and details go in an expandable section; include codes when they help users search. (Cloudscape)
- Never promise what you can't do ("the team was notified"). (Cloudscape)
- No fix available → still give a next step: retry, refresh, contact support. (Polaris, PatternFly)
- Keep the user's input after any error. (GOV.UK, NN/g, Primer). Form errors: `patterns/forms-and-saving.md`.

### Primer degraded rules
- Degrade rather than fail; at most **5 outage messages per page** — beyond that, consolidate. (Primer)
- Small elements: warning icon + message. Panels: blankslate with muted alert icon; primary action only if it can fix the problem. (Primer)
- Hide unknown counts and activity badges (don't show 0). Never suppress the whole global header; drop only failing items. (Primer)
- Never disable controls because a backend is down; never ship UI missing critical information. (Primer)
- Forms: saving down → keep fields and Save, explain in a dialog on submit; nothing readable → remove form and explain; some fields failed → disable those with an error under each. (Primer)

### 404 / 403 / service pages
- Dedicated pages, not validation messages, for "Page not found", "There is a problem with the service", "Service unavailable", and eligibility/permission outcomes. (GOV.UK)
- 404: plain heading (no bare "404"), next steps beyond "go back", optional suggested links, always a home link. (PatternFly)
- 403: "Access permissions needed", who can grant it, "Request access" in place. Show approver the seat cost. (PatternFly, Atlassian) See `saas/accounts-and-permissions.md`.

### Session expiry
- Warn before inactivity timeout with an accessible alertdialog that takes focus, ≥20s to respond, single "Stay signed in" action, extendable ≥10 times — or let users/admins turn off or set ≥10× the default. (WCAG 2.2.1)
- Preserve unsaved form data across re-authentication and return users to where they were after sign-in. (general practice; WCAG 2.2.5 AAA)

## 5. Choosing a feedback component

Pajamas order first: Does it need to exist? Is it the immediate result of an action? A system condition? An async event? (Pajamas)

| Need | Use | Persistence |
|---|---|---|
| Problem with one field | Inline field error under the input | Until fixed (GOV.UK, Ant) |
| Problem/info tied to a section or form | Section/inline message, above the form's buttons or below the trigger | Until resolved (Carbon, Primer, Cloudscape) |
| Non-critical success the user can't see | Toast | Auto-dismiss ≥5s (defaults) |
| Result of an action after redirect; service-wide status | Flashbar / page banner at top of content | Until dismissed (Cloudscape, Primer) |
| Critical, system-wide condition | Banner, one at a time, pushes content | While condition lasts (Carbon, Atlassian, Lightning) |
| Decision required, blocking | Modal / alertdialog | Until answered (all) |
| Context before a task starts | Callout (info/warning, not dismissible, links only) | Persistent (Carbon) |
| Events to review later; async completions | Notification panel / center | Until archived (Carbon, Ant) — see `saas/notifications-system.md` |
| Many field/table errors | Message popover with counter in footer | Until fixed (Fiori) |
| Result is already visible | **Nothing** (screen readers still get status) | — (Pajamas, Primer) |

### Cross-system names
| Role | Carbon | Atlassian | Lightning | Fiori | Cloudscape | Primer | Pajamas | Ant |
|---|---|---|---|---|---|---|---|---|
| Transient success | Toast | Flag | Toast | Message toast | Flashbar (success) | (avoid) InlineMessage | Toast | Message |
| In-context | Inline notification | Section message | Inline text | Message strip | Alert | InlineMessage | Alert | Alert |
| System-wide | Banner | Banner | Alert | — | Flashbar | Banner | Alert | — |
| Blocking | Modal | Modal dialog | Modal/prompt | Message box | Modal | Dialog | Modal | Modal |
| Pre-task context | Callout | — | — | Message strip | — | — | — | — |
| Review later | Notification panel | — | Notification | — | — | — | Notifications/To-Do | Notification center |

Messages from the user's own action appear where they work; system messages go to toasts or the notification panel with enough context to stand alone. (Carbon)

## 6. Toast rules (see foundations/defaults.md)
- Only non-critical success the user can't already see. Never errors, never the only place for info, never content to copy (record IDs → success message box). **[consensus]** (Carbon, Fiori, Pajamas, Polaris)
- ≤2 lines, close button, auto-dismiss ≥5s scaled to length, pause on hover/focus, `role="status"`, never steal focus. (Carbon, Lightning, Fiori, WCAG 2.2.1)
- One position app-wide, top-right default (Carbon; systems disagree on position). Max 3 visible, queue the rest; clear on navigation. (Lightning)
- Copy: "[Object] [past-tense verb]" ("Sales order created"), "[n] [objects] [verb]" for many; no "successfully", no IDs, no list of names. Polaris caps at ≤3 words. (Fiori, Polaris)
- Skip the toast after create-then-open, inline edit, or when navigating — if navigating, show feedback on the destination. (Lightning, Fiori)
- An action in a toast (Undo) must also exist elsewhere and keeps the toast ≥10s or until dismissed. (Polaris, Carbon)
- Alt: Primer avoids toasts entirely — acceptable house choice; use banner after redirect, inline message otherwise. (Primer)

## 7. Banner rules
- One at a time, never stacked; push content down, never overlay. **[consensus]** (Carbon, Atlassian, Lightning)
- Critical/system-wide only (data or function loss, outages, plan blockers). Critical banners include troubleshooting and a support path. (Atlassian, Polaris)
- Dismissibility conflict: Carbon dismissible; Atlassian and Lightning not. **House default:** non-dismissible only while the condition actually blocks the user; otherwise dismissible and don't return in the same session (Polaris). Planned maintenance heads-ups may be dismissible. (Lightning)
- Remove automatically when the condition clears. (Atlassian). Every time-limited message needs a removal plan and is shown only to users who can act. (Pajamas)
- Don't style system notices like ads — banner blindness. (Selective Attention)
- `role="alert"` only for truly urgent banners; it interrupts. (Atlassian, WCAG 4.1.3)

## 8. When to show no message
- Result is visible on screen (inline edit saved, toggle flipped, new row highlighted). (Primer, Pajamas, Lightning)
- User navigated to the created record. (Lightning)
- Message only repeats what the UI already says, or the problem could be prevented instead (Fiori); an unread notification would repeat (Carbon); the event is trivial (Pajamas).
- Still announce status to screen readers via a polite live region. (Primer)

## 9. Copy length limits
| Element | Limit | Source |
|---|---|---|
| Inline notification / toast | ≤2 lines (toast 3 if no timestamp); longer → short version + "View more" | Carbon |
| Notification action | 1 action, label ≤2 words | Carbon |
| Flag | ≤2 links, no "Learn more"; scrolls past 5 lines | Atlassian |
| Error title / body | 3–4 words, no instruction / 1–2 sentences | Atlassian |
| Message title | No end period; body adds 1–2 sentences, doesn't repeat title | Carbon |
| Polaris toast | ≤3 words | Polaris |
| Empty-state title / body | ≤5 words / ≤3 lines, <66 chars per line | Pajamas, Fiori, Lightning |
| Helper text | ~100 characters | Carbon |

More in `foundations/writing.md`.

## 10. Edge-data test list
Run every view against these before sign-off. (general practice unless tagged)
- **0 rows, 1 row, exactly one page, page+1, 10k+ rows.** Check empty state, singular copy ("1 item"), pagination shown even with one page (Cloudscape), Fiori limits (render ≤200, grow ≤1,000).
- **Long names:** 255-char names, unbroken strings (URLs, IDs), user-named items in other scripts. Truncate keeping ≥4 chars, middle-truncate when the distinctive part is at the end, full string in tooltip (PatternFly). Never truncate buttons, nav, column headers (PatternFly, W3C i18n).
- **Translation:** short strings expand 200–300%. (W3C i18n). See `saas/global-and-performance.md`.
- **Nulls:** "—" for missing, never blank, never for a real 0. (see foundations/defaults.md)
- **Huge/tiny numbers:** 1,000,000 grouping (PatternFly), M/B abbreviations with exact on hover (Ant), negatives, currency codes, 0.0001.
- **Dates:** time zones, DST boundary, future dates, "just now".
- **Permissions:** viewer, editor, admin, no access, SSO-managed fields.
- **Failure:** slow 3G, timeout, partial API failure, 500 on save, offline.
- **State combos:** filtered + empty, selected + refreshing, editing + session expiry.

## Common AI failures
- One generic "No data" for every state, including errors and loading.
- Empty state rendered under live table headers and a toolbar.
- Full-screen spinner on every refresh, wiping visible data.
- Toast for errors, or the only copy of a record ID in a toast.
- "Successfully saved!" toast after an inline edit that already shows the new value.
- Stacked banners and multiple primary CTAs across empty states.
- A single failed widget crashing the whole page.
- Showing "0" for counts that failed to load.
- Long jobs with an indeterminate spinner, no Cancel, no completion summary.
- Never testing 1 row, 10k rows or 255-character names.

## Sources
- https://carbondesignsystem.com/patterns/notification-pattern
- https://carbondesignsystem.com/components/notification/usage/
- https://carbondesignsystem.com/patterns/loading-pattern
- https://carbondesignsystem.com/patterns/empty-states-pattern/
- https://atlassian.design/foundations/content/designing-messages/empty-state
- https://atlassian.design/foundations/content/designing-messages/error-messages
- https://atlassian.design/components/banner/usage
- https://atlassian.design/components/flag/usage
- https://spring-21.lightningdesignsystem.com/guidelines/messaging/components/toasts
- https://spring-20.lightningdesignsystem.com/guidelines/messaging/components/alerts
- https://spring-20.lightningdesignsystem.com/guidelines/loading
- https://spring-20.lightningdesignsystem.com/guidelines/empty-state
- https://www.sap.com/design-system/fiori-design-web/v1-151/foundations/best-practices/global-patterns/messaging/messaging
- https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/message-toast/usage
- https://www.sap.com/design-system/fiori-design-web/v1-145/ui-elements/placeholder-loading/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/foundations/best-practices/global-patterns/designing-for-empty-states
- https://cloudscape.design/patterns/general/user-feedback/
- https://cloudscape.design/patterns/general/loading-and-refreshing/
- https://cloudscape.design/patterns/general/empty-states/
- https://cloudscape.design/patterns/general/errors/error-messages/
- https://primer.style/ui-patterns/degraded-experiences
- https://primer.style/ui-patterns/notification-messaging
- https://primer.style/product/ui-patterns/loading
- https://primer.style/product/ui-patterns/empty-states
- https://www.patternfly.org/components/empty-state/design-guidelines
- https://www.patternfly.org/content-design/writing-guides/error-messages
- https://www.patternfly.org/content-design/grammar/truncation
- https://design.gitlab.com/patterns/empty-states/
- https://design.gitlab.com/patterns/loading/
- https://design.gitlab.com/patterns/saving-and-feedback/
- https://design-gitlab-com-gitlab-org-gitlab-services-f6beaf2fb7fd4cad76.gitlab.io/patterns/choosing-a-messaging-pattern/
- https://shopify.dev/docs/apps/design-guidelines/user-experience/alerts
- https://cdn.jsdelivr.net/npm/superv5_polarisui@2.0.1/dist/docs/components/Toast/README.md
- https://design-system.service.gov.uk/patterns/validation/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://www.nngroup.com/articles/progress-indicators/
- https://www.nngroup.com/articles/designing-for-waits-and-interruptions/
- https://nngroup.com/articles/indicators-validations-notifications
- https://ant.design/docs/spec/research-message-and-feedback.md
- https://ant.design/docs/spec/research-result
- https://www.w3.org/WAI/WCAG21/Understanding/status-messages
- https://w3.org/International/articles/article-text-size
