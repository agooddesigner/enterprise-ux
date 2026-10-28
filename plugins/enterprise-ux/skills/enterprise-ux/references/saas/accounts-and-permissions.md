# Accounts, tenancy and permissions

**Load when:** designing org/workspace/team structure, workspace switchers, domain verification, SSO/SCIM admin, roles and permission screens, permission-aware UI, request-access flows, approvals, user management tables, or settings information architecture.

## 1. Tenancy hierarchy

- Model three levels plus users: **Organization** (verified domains, SAML SSO, SCIM, security policy, audit log, analytics, billing) → **Workspace** (feature enablement, who can create teams, allowed domains) → **Team/teamspace** (sharing, publishing, exports) → User. (Notion)
- Settings **cascade down and can only be tightened** below. A lower-level owner can't enable what a higher level disabled. (Notion)
- Show locked settings as disabled-with-reason: "Restricted by your organization" + who set it + link for admins. Never just grey it out. (Notion, Pajamas)
- Prefer admin-configurable policies that cascade over per-customer custom code. (Notion — framing is inference)

### Workspace / team switcher

- The switcher is the primary context selector: top-left, always visible, shows current org/workspace name + plan badge. (Vercel)
- Everything below — settings, usage, billing, notifications — is scoped to the selected context; label pages with that context ("Acme Prod · Usage"). (Vercel)
- Switching keeps the user on the equivalent page in the new context where it exists; otherwise lands on that workspace's home. (general practice)
- Search inside the switcher when users belong to many workspaces; show recent first. (general practice)

## 2. Identity: domain verification, SSO, SCIM

- **Domain verification is step one**; it unlocks SSO, workspace consolidation and control over who can create workspaces. Show DNS record, copy button, status (Pending / Verified / Failed + reason) and "Check again". (Notion)
- SSO: state constraints up front (one IdP per org in Notion's case). Show connection status, last successful login, test-connection action. (Notion, WorkOS)
- SCIM / directory sync: the directory is the source of truth. Accounts arrive with attributes filled; never ask admins to re-enter them. (WorkOS)
- Render directory-synced fields **read-only** with "Managed by your organization" (and the IdP name), so edits that fail don't look like bugs. (WorkOS — inference flagged by source)
- Offer self-serve setup with connection status and actionable errors so customers don't need support. (WorkOS)

### Group → role conflicts

- Users often sit in several IdP groups. Define one explicit resolution rule (e.g. highest role wins, or union) and **show the resulting role plus where it came from**: "Admin — from group `eng-leads`". (WorkOS)
- Show a preview of affected users before saving a mapping change. (general practice)

### Deprovision vs suspend

| State | Access | Sessions | Data | Seat |
|---|---|---|---|---|
| Suspended | Blocked, reversible | Revoked | Kept, still owned | Decide and state it |
| Deprovisioned / removed | Blocked | Revoked immediately | Retain or reassign — ask admin to choose a new owner | Released |
| Deleted | Gone | — | Per retention policy | Released |

- Treat suspension as a separate state from deletion; design lockout, session revocation and data reassignment explicitly. (WorkOS — source leaves specifics open)
- Removing a user who owns resources → prompt to reassign before confirming (see `patterns/actions-and-dialogs.md` for confirmation tiers).

## 3. Displaying roles

- Present roles as an **ordered ladder**, each with a one-line "who it's for" (GitHub: Read → Triage → Write → Maintain → Admin). (GitHub)
- Each role gets **can do** and **can't do** lists. (Stripe)
- Offer a **permission matrix**: rows = concrete actions in user language ("Issue refunds"), columns = roles, ✓/✗ with text (not colour alone), link to docs. (GitHub, WCAG 1.4.1)
- Expose a stable **role ID** per role for SSO/IdP mapping, with copy button. (Stripe)
- When a user holds several roles, warn that permissions are the **union**, which can create unintended authority; show the effective permission set. (Stripe)
- **Separate IAM administration from business power**: an access-admin role can invite/remove users but can't move money or grant super-admin. (Stripe)
- Flag that any role able to invite users is an account-takeover vector if compromised; require step-up auth for it. (Stripe)
- **Least privilege**: default new users to the lowest useful role; org-wide base permissions set the floor; custom roles are typically an enterprise-tier feature. (GitHub, Stripe)
- Role also changes what notifications a user sees — reflect that in notification settings. (Vercel)

## 4. Designing the UI for permissions

| Situation | Treatment |
|---|---|
| User can never perform this (role lacks it, by design) | **Hide** it — clutter otherwise. (Fiori, Cloudscape) |
| User lacks permission but should know it exists | **Disable + reason** ("Only workspace admins can change this") + who can help. (Pajamas, Cloudscape) |
| Blocked by a higher-level policy | Disabled + "Restricted by your organization" + who set it. (Notion) |
| Whole page/section inaccessible | Error-type empty state: "Access permissions needed" + **Request access** primary. (Carbon, PatternFly) |
| Plan/tier limit, not permission | Upgrade path — see `saas/billing.md`. (Pajamas) |

- Disabled-reason copy: one sentence, what and why, optional next step; templates "Available for [role]" / "Available when [condition]". (Cloudscape)
- Tooltips on disabled buttons don't reach keyboard users — use an inactive (focusable) control or visible text. (Primer) See `patterns/actions-and-dialogs.md`.
- Say who can help by name or role, with a link ("Ask an admin: Priya S., Leo M."). (general practice)
- Hide chevrons/links into detail pages the user can't open. (Fiori)
- Never return a generic "No data" when the real reason is permission. (Primer)

## 5. Request access flow

- Put "Request access" exactly where access is blocked; allow requesting for self or for someone else, with an optional message. (Atlassian)
- Admins get an **Access requests** queue with a "Review request" detail: requester, resource, requested role, justification. (Atlassian)
- **Show the approver the cost**: approving adds the user to a default group *and bills a seat* — "Approving adds 1 seat ($X/mo)". (Atlassian)
- Denial can include a message; requester is notified either way. (Atlassian)
- Requester sees pending state on the blocked screen ("Request sent to admins on 3 Mar") instead of a fresh button. (general practice)

## 6. Two-person approval for sensitive actions

Model on Stripe approval rules:
- Admin picks the **action** (refund, bank-account change, admin invite…), optional **conditions** (amount threshold, actor type, rate), the **control** (require approval or block), and **reviewers** (person or role). (Stripe)
- Optional justification instructions shown to the requester. (Stripe)
- **Nobody approves their own request.** Requests **expire after 14 days.** (Stripe)
- Every rule change and request event goes to security history / audit log. (Stripe) See `saas/collaboration-and-audit.md`.
- Requester sees a "Pending approval" state with reviewer and expiry, not a success message. (general practice)
- Agent-initiated actions should hit the same rules — see `saas/ai-features.md`.

## 7. User management table

- Columns: name + email (identifier first), role (with source: "SSO group" / "manual"), status (Active / Invited / Suspended / Deactivated as text badges), last active, auth method (SSO / password / 2FA), teams. (NN/g data tables, Stripe, WorkOS)
- Filters for role, status, auth method; search by name/email; filter state in URL. (Cloudscape) See `patterns/tables.md`.
- Bulk actions: change role, resend invite, suspend, remove. Removing in bulk → confirmation naming count and consequences (seat release, ownership transfer). (Cloudscape)
- Invited rows: resend, revoke, show invite expiry. (general practice)
- Synced users: role/name cells show "Managed by your organization", edit disabled with reason. (WorkOS)

## 8. Settings architecture

- Three scopes, never blended on one page: **Personal** (my profile, my notifications), **Workspace**, **Organization**. (Vercel, Notion)
- Say whose settings these are: "These settings affect only you. You can't change other members' preferences." (Vercel)
- Admin pages say the blast radius: "Applies to all 340 members of Acme". (general practice)
- Save model: explicit Save for forms; toggles and single selects outside a form apply instantly; never mix in one form; never autosave security, financial or privacy settings. (see `foundations/defaults.md`; Primer, Pajamas)
  - Alt: Slack moved notification prefs to autosave because people forgot to click Save — acceptable for low-risk personal preferences. (Slack)
- **"Off" must mean off.** If a setting says Off, nothing related may still fire (Slack's legacy "off" still showed badges). (Slack)
- Separate **what** (which events) from **how** (which channel/interruption); avoid coupled settings that can't change independently; sync settings across devices. (Slack)
- Give advanced controls a clear hierarchy (≤2 levels of disclosure). (Slack, NN/g)
- Deep-link "Configure in settings" from feature pages to the exact section. (Pajamas)
- Explain inherited or locked values inline, with who set them, so nobody has to guess why a value won't change. (Pajamas)
- **Support access / "view as user"**: only with the customer's time-boxed consent, a persistent banner naming whose account is being viewed with an Exit control, read-only by default, and every session in the audit log. (general practice)
- **Environment indicator**: test/sandbox modes carry a persistent, non-colour-only label so nobody mistakes them for production (and vice versa). (general practice)

## Common AI failures

- One flat "Settings" page mixing personal, workspace and org settings with no scope labels.
- Role dropdown with bare names ("Member", "Editor", "Admin") and no description, ladder or matrix.
- Greyed-out controls with no reason and no person to ask; tooltips on disabled buttons only.
- Editable name/email fields for SCIM users that silently revert on next sync.
- "Admin" bundling user management with billing and data deletion; no split IAM role.
- Approval flows where the requester can approve their own request, or requests never expire.
- Request access that doesn't show the approver the seat cost.
- Removing a user with no prompt to reassign their resources; suspend and delete merged into one action.
- Permission matrix using coloured dots only.

## Sources

- https://www.notion.com/en-gb/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
- https://vercel.com/docs/notifications
- https://vercel.com/docs/pricing/manage-and-optimize-usage
- https://workos.com/docs/directory-sync.md
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization
- https://docs.stripe.com/get-started/account/teams/roles.md
- https://docs.stripe.com/keys-best-practices.md
- https://docs.stripe.com/account/approvals.md
- https://confluence.atlassian.com/cloud/access-request-improvements-978205737.html
- https://carbondesignsystem.com/patterns/empty-states-pattern/
- https://cloudscape.design/patterns/general/disabled-and-read-only-states/
- https://cloudscape.design/patterns/general/filter-patterns/filter-persistence-in-collection-views/
- https://cloudscape.design/patterns/resource-management/delete/
- https://primer.style/ui-patterns/degraded-experiences
- https://primer.style/product/ui-patterns/saving
- https://design.gitlab.com/patterns/settings-management
- https://design.gitlab.com/patterns/forms/
- https://www.patternfly.org/components/empty-state/design-guidelines
- https://www.sap.com/design-system/fiori-design-web/v1-84/page-types/floorplans/list-report-floorplan-sap-fiori-element/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://slack.engineering/how-slack-rebuilt-notifications/
- https://nngroup.com/articles/data-tables
- https://www.nngroup.com/articles/progressive-disclosure/
