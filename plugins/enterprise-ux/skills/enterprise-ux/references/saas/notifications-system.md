# Notifications system

**Load when:** designing the cross-channel notification system (in-app center, email, push, SMS, digests), notification preferences, routing rules, or auditing notification fatigue. For on-screen toasts/banners/inline messages after a user action, use `patterns/feedback-and-states.md`.

## 1. Notification, validation or indicator? Decide first

| What it is about | Use | Where |
|---|---|---|
| Input the user just entered | Validation | Next to the field, says how to fix |
| State of a dynamic element, no action needed | Indicator (badge, status chip) | In context, only while true |
| A system event, user may not be thinking about it | Notification | Channel per severity (below) |

- Information tied to the user's current goal belongs in context as an indicator, not a notification. (NN/g)
- Essential information never relies on a passive notification alone — add a persistent indicator. (NN/g)
- Don't send validation or routine status as notifications. (Smashing notifications)
- Notifications must stand alone: name the object, the workspace and what happened, because the user lacks context. (NN/g, Carbon)
- Details on toasts, banners and inline messages: `patterns/feedback-and-states.md`.

## 2. Channels

| Channel | Use for | Default |
|---|---|---|
| In-app (bell + panel) | All event types; reviewable history | On for all types (Vercel) |
| Email | Out-of-product events; things needing a record | On, but suppressed if read in-app (Vercel, Pajamas) |
| Push (desktop/mobile) | Time-sensitive, human-originated items | **Opt-in per device** (Vercel, Slack) |
| SMS | Narrow, critical cases only (Vercel: spend alerts) | Off; opt-in (Vercel) |
| Digest (daily/weekly email) | High-volume, low-urgency events | Suggest automatically above a frequency threshold (Smashing notifications) |
| To-do / task inbox | User must act (approval, review) | Separate from FYI notifications (Pajamas, Ant) |

- Intrusiveness order: SMS ≈ push > in-app > email > digest. Above a frequency threshold, offer to switch a type to digest. (Smashing notifications)
- Put ongoing items (approvals, submitted requests) in a notification center, not toasts. (Ant)

### Dedupe

- **Reading in-app suppresses the duplicate email.** Delay email for a short window so in-app can be read first. (Vercel; window length is general practice)
- One event → one notification per recipient, regardless of how many rules match. (general practice)
- Cross-device: don't duplicate the same message on desktop and mobile when one is active. (Lightning messaging principles, Slack)
- Suppress onboarding/marketing emails for users active in-app. (Userpilot)

## 3. Preferences: what vs how

- Split **what I'm notified about** (event types, scopes) from **how I'm interrupted** (channels, timing). Never couple them so one can't change without the other. (Slack)
- Per-scope overrides with three plain choices: **All / Mentions only / Mute**. Mentions + DMs is the dominant sensible default. (Slack)
- Per-device push choice (desktop / mobile / both / none); mobile mirrors desktop by default. (Slack)
- Offer **presets** (Calm / Regular / Power) on top of the per-type grid. (Smashing notifications)
- Quiet hours / Do not disturb, and snooze (e.g. 24h). (Smashing notifications)
- Ask delivery preference once during onboarding, briefly. (Smashing notifications)
- Say scope: "These settings affect only you." (Vercel) See `saas/accounts-and-permissions.md`.
- Show only event types the user's role can receive (Vercel's Developer role sees deployment failures and integration notices only). (Vercel)
- Preferences autosave is acceptable here (personal, low-risk). (Slack) Alt: explicit Save if the product's other settings use it — never mix in one form (see `foundations/defaults.md`).
- Better defaults reduce how often people need overrides — tune defaults before adding toggles. (Slack)

### Critical, non-mutable types

- Some types can't be turned off: security events, role changes, invites, billing failure. (Vercel)
- For critical types, users may drop one channel but not all; disable the last channel's toggle with a reason. (Vercel)
- Mark these in the grid with a lock icon + "Required for security" text. (general practice)

## 4. Fatigue rules

- Frequency is the top complaint. Fewer, better notifications improved long-term retention in Facebook's cited study, even after an initial dip. **Default slow**; adjust per segment. When in doubt, postpone or don't send. (Smashing notifications)
- Severity tiers: **High** (errors, failures needing action, destructive outcomes) → push/in-app + email; **Medium** (warnings, success of long jobs) → in-app (+ email if opted); **Low** (info, badges) → in-app badge or digest. (Smashing notifications)
- Human-originated (mention, assignment, approval request) earns more attention than automated events. (Smashing notifications)
- **Batch noisy system events**: one grouped notification ("12 domains misconfigured"), rate-limited (Vercel sends schema errors at most hourly). (Vercel)
- **Right recipient**: deployment failure → the person who deployed; billing → billing roles; usage → owners. Never broadcast to everyone in the workspace. (Vercel)
- Don't notify about trivial things — fatigue degrades the whole system. (Pajamas)
- Every time-limited message needs a removal plan and goes only to people who can act on it. (Pajamas)
- No guilt badges or artificial unread counts to drive engagement. (lawsofux Zeigarnik)

## 5. Notification center (panel)

- Opens from a bell in the header utility area, as a panel — not a page navigation. (Carbon header)
- Unread count on the bell; cap the visible number (e.g. "99+") (general practice for the cap). (Vercel)
- Order chronologically, or group by source/urgency; consistent across sessions. (Carbon)
- Each item: actor, verb, object (linked), workspace, relative time with absolute on hover. (Carbon; see `foundations/defaults.md` timestamps)
- Mark read when the panel closes (Vercel) or on click; offer "Mark all as read". (Vercel)
- **Archive** tab; Vercel keeps archived items 365 days. (Vercel)
- Link to preferences from the panel header. (Carbon)
- **Never resend** a notification the user hasn't acknowledged yet; update the existing item instead. (Carbon)
- Empty panel: "You're all caught up" — brief, no celebration on a frequent state. (Atlassian)
- Accessibility: new arrivals announced politely (`role="status"`), never `role="alert"` for non-urgent items; panel reachable by keyboard. (WCAG 4.1.3; see `foundations/accessibility.md`)

## 6. Email and push content

- Subject/title = object + what happened ("Invoice INV-204 payment failed"). (Fiori-style object + action)
- One primary link that deep-links to the exact record in the right workspace. (Auth0 invite principle; general practice)
- Footer: why you got this + one-click link to that type's preference. (general practice)
- Respect the user's locale and time zone in timestamps. (see `saas/global-and-performance.md`)

## 7. Trust rule

- A "no push" (or "off") setting must **never** be violated — not during rollbacks, migrations or incidents. (Slack)
- "Off" means off: no badges, sounds or emails for that type. (Slack)
- Re-enabling notifications after a migration requires the user's action, never a silent reset. (Slack, by implication)

## 8. Admin and org controls

- Org admins may set defaults and mandate certain types, but must show users which settings are locked and by whom. (Notion cascade; Pajamas)
- Integration scope changes or disabled integrations notify the integration owner. (Vercel) See `saas/integrations-and-data.md`.
- Usage-alert disablement shows an inline surprise-charges warning. (Vercel) See `saas/billing.md`.

## Common AI failures

- Every event sends email + push + in-app with no dedupe.
- A wall of 60 per-type toggles with no presets, no what/how split.
- Notifying the whole workspace about one person's failed job.
- Resending the same unacknowledged reminder every hour.
- Security and billing alerts that users can fully mute.
- Toasts used as the notification system — gone after 5 seconds with no history.
- Notification items like "Something changed" with no object, workspace or link.
- `role="alert"` on every incoming notification, flooding screen readers.
- An "Off" toggle that still shows badges.

## Sources

- https://vercel.com/docs/notifications
- https://slack.engineering/how-slack-rebuilt-notifications/
- https://smashingmagazine.com/2025/07/design-guidelines-better-notifications-ux/
- https://carbondesignsystem.com/patterns/notification-pattern
- https://carbondesignsystem.com/components/notification/usage/
- https://carbondesignsystem.com/components/UI-shell-header/usage/
- https://nngroup.com/articles/indicators-validations-notifications
- https://ant.design/docs/spec/research-message-and-feedback.md
- https://design.gitlab.com/patterns/notifications
- https://design-gitlab-com-gitlab-org-gitlab-services-f6beaf2fb7fd4cad76.gitlab.io/patterns/choosing-a-messaging-pattern/
- https://spring-21.lightningdesignsystem.com/guidelines/messaging/overview
- https://atlassian.design/foundations/content/designing-messages/empty-state
- https://userpilot.com/solution/enterprise-saas-onboarding
- https://www.notion.com/en-gb/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
- https://w3c.github.io/wcag/understanding/status-messages.html
- https://lawsofux.com/zeigarnik-effect/
