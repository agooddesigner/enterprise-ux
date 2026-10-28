# Onboarding and activation

**Load when:** planning or reviewing first-run, signup, invite, SSO/SCIM join flows, checklists, product tours, first-use empty states, sample data, trials, or "what's new" help in a B2B SaaS product.

## 1. Define activation before designing anything

- Name the activation event first: the one action (or small set) that predicts retention, e.g. "first report shared with a teammate". Every onboarding element must push toward it; cut anything that doesn't. (Appcues, Intercom)
- Anchor the "aha" moment to that event and instrument it as a metric before launch. (Intercom)
- Track time-to-value and checklist completion per account and per segment; trigger a nudge when a user stalls. (Userpilot — vendor claim; treat numbers as unsupported)
- Measure with task-level metrics, not page views: learnability over time, advanced-feature adoption, errors. (NN/g CASTLE)
- B2B has two activations: the **account** activates (admin configured, team invited) and each **user** activates (first real task done). Track both. (general practice)

## 2. Three B2B entry paths — design all of them **[consensus]**

| Path | What happens | Design requirements |
|---|---|---|
| Self-serve signup | User creates account, optionally pending admin approval | Detect corporate domain → offer to join the existing org instead of creating a duplicate; show "awaiting approval" state with who approves. (Auth0) |
| Admin invite | Admin invites → unique email link → login/signup → user lands **inside the right org** | Never drop invitees on a generic home or org picker; name the inviter and org in the email and landing. (Auth0) |
| SSO / JIT | Account auto-created on first corporate SSO login | No password step; land on a role-appropriate first screen; assign default role from IdP groups. (Auth0) |
| SCIM provisioned | Account exists before the user ever visits; no invite | First visit must explain "Your organization set up this account". Non-SSO SCIM users still need a password-setup step. (WorkOS) |

- Let admins stage the rollout: turn off automatic account creation and suppress SCIM invite emails so the customer decides when users are told. (Notion)
- Pre-fill profile fields from the directory; never ask users to re-type what the IdP knows. (WorkOS)

## 3. Admin onboarding vs end-user onboarding

Admin onboarding is a setup sequence; end-user onboarding starts only after it. Show admins a setup task list:

1. Verify domain (unlocks consolidating workspaces, SSO, and control of workspace creation). (Notion)
2. Configure SSO (one IdP per org is a common constraint — say so up front). (Notion)
3. Connect SCIM / directory sync, with self-serve connection status and errors. (WorkOS)
4. Map groups → roles; set defaults (see `saas/accounts-and-permissions.md`).
5. Invite or release users; choose rollout timing. (Notion)

- Use a task-list pattern for setup that spans sessions: verb-first task names, any order where possible, blocked tasks shown as "Cannot start yet", minimal statuses. (GOV.UK)
- Offer "Invite a colleague to configure" when the current user lacks rights for a setup step (e.g. IdP config). (Pajamas)
- End users never see admin setup tasks. If org setup is incomplete, show them an error-type empty state that names who can finish setup. (Carbon)

## 4. Checklists

- 3–5 items; completion drops noticeably past five. (Appcues)
- Items are in-product verbs ("Create your first project"), never "Learn about X". Each item deep-links to the real screen, not a doc. (Appcues)
- Tick an item on the **real domain event** (report created), not page view or tour completion. Credit users who did it on their own. (Appcues)
- Show progress ("3 of 5"); celebrate completion lightly — scale celebration to frequency. (Appcues, Atlassian; goal-gradient per lawsofux)
- Separate checklists per role/persona when activation paths differ (admin vs requester vs approver). (Appcues, Userpilot)
- Always allow minimise/dismiss and a way to bring it back; put a quick win first. (general practice)
- Never fake progress (pre-ticked "Account created" to inflate the bar). (lawsofux goal-gradient misuse)

## 5. Tours and contextual help

- **Never auto-launch a tour or tutorial on first login.** Users skip them and they don't improve performance. No "what's new" card carousels. (NN/g)
- Prefer **pull revelations**: help triggered when the user signals need (hovers a new tool, starts a related action), easy to dismiss, easy to recall from a persistent Help / What's new menu. (NN/g)
- If a walkthrough is justified (genuinely new interaction paradigm), make it learn-by-doing, not view-only. View-only tours are fine for announcements, weak for teaching. (NN/g, Intercom)
- Advance steps on **product state** (element exists, object created), not on "Next" clicks — click-driven tours break when state diverges. (Intercom)
- Keep any tour to a few points, with clear exit and restart. Tours don't fix interaction problems — fix the UI first. (Ant)
- Don't explain conventions users already know (what a search box does). (NN/g)
- Teach faster methods in context, right after the user does it the slow way ("Tip: press E to edit"). (NN/g accelerators)
- Suppress onboarding emails for users already active in-app. (Userpilot)
- Never hide constraints (limits, rules) in tooltips; assume most users never open tips. (NN/g)

## 6. Empty states as onboarding

| Empty-state type | Copy job | CTA |
|---|---|---|
| First use (blank slate) | What will appear here + why it's useful | One action to create the first item |
| User cleared | Neutral, maybe light celebration ("All caught up") | Optional |
| No results | Say nothing matched | "Clear filters" (see `foundations/defaults.md`) |
| Error / permission / missing config | Plain reason, no codes, no jokes | Ranked fixes: request access, finish setup, check log |

(Carbon, Atlassian, Cloudscape, PatternFly)

- The empty state replaces the whole container (table + headers), never sits above an empty grid. (Carbon) **[consensus]**
- Short sentence-case title, 1–2 sentence body, 1–2 word imperative CTA; no "OK", no "Nothing here". (Atlassian, Fiori)
- Hide the CTA from users who lack permission to act; for them, show who can. (Lightning, Fiori)
- Several empty states on one page → tertiary/secondary CTAs, no illustrations. (Carbon, Fiori)
- Guided onboarding and starter content sit on top of a basic empty state — they never replace it, because users skip or delete them. (Carbon)
- Rich onboarding (inline docs, starter content) only for primary features. (Carbon)
- Never show "No data" while loading or when loading failed. (NN/g, Primer)
- Track empty-state CTA conversion. (Pajamas)

## 7. Sample and starter data

- Offer "Load sample data" / templates as a second path from first-use empty states; learners need sandboxes and templates. (NN/g)
- Label sample records clearly as sample, keep them out of billing, reports and exports, and offer one-click "Remove sample data". (general practice)
- After removal, the normal first-use empty state must still work. (Carbon)
- Prefer templates built from the customer's domain (e.g. "Quarterly vendor review") over lorem ipsum. (general practice)

## 8. Progressive disclosure

- Initial view = the features most users need; advanced options behind a clearly labelled, predictable control. (NN/g)
- Decide what's "primary" from evidence: task analysis for new products, usage analytics for existing ones. (NN/g)
- **Max two levels** of disclosure; three or more confuses users. (NN/g)
- Wizards (staged disclosure) only when steps are independent; if users bounce between steps, use one page. Defer late-stage inputs (payment, advanced config) until needed. (NN/g)
- Create forms: primary section = required fields with no good default + fields 80%+ need; rest under "Additional settings". (Cloudscape)
- Don't remove capability in the name of simplicity — legends and compliance users need the long tail. (NN/g, lawsofux Tesler)

## 9. Trials

| Model | Use when | Note |
|---|---|---|
| Reverse trial (paid features for a limited time → buy or drop to free) | Value is visible within ~14 days; you want both conversion and a free floor | Show a persistent, non-alarming "Trial: N days left" with what changes at the end |
| Free trial (time-boxed, then pay) | Clear, fast time-to-value | Ask for payment as late as possible (NN/g staged disclosure) |
| Freemium | Network-effect products, or value needs >14–30 days to appear | Wins on signup volume |

- Vendor-cited figures (not independently verified): free trials convert free→paid ~2–3x freemium; median time-to-purchase ~14 days for trials vs 60–90 days for freemium. (Poyar — verify — as of Oct 2026)
- Before a trial ends, tell the user exactly which features and data they'll lose, and never delete data at downgrade without notice. (general practice)
- Trials longer than 31 days that auto-convert may trigger California notice rules — see `saas/billing.md`. (Cooley — verify — as of Oct 2026)

## 10. Design for all three complex-app users (NN/g)

| User | Needs | Onboarding implication |
|---|---|---|
| Learner (domain expert, new to tool) | Inline, just-in-time help, templates, sandbox, actionable errors | Pull help, sample data, templates |
| Legacy (long-time, inefficient) | Gradual change, early notice, old views kept during transition | Announce redesigns early; "switch back" for a period; surface shortcuts |
| Legend (power user) | Speed, advanced features, shortcuts | Never block with forced tours; show shortcuts in menus and ⌘K |

## 11. Returning users

- On login, show "Continue where you left off" with recent items and previews. (NN/g)
- Show "continue setup" and draft indicators for unfinished work — without guilt-driven red badges. (lawsofux Zeigarnik)
- Remember simple state across sessions (last workspace, last sort, last view). (NN/g)

## Common AI failures

- Auto-launching a 7-step modal tour on first login with "Next/Next/Next" buttons.
- Checklist items like "Watch the intro video" or "Explore the dashboard" that tick on page view.
- One onboarding flow for everyone — ignoring the admin setup sequence, SSO/JIT and SCIM arrivals.
- Invite links that land on a generic org picker or a blank home.
- Empty table with headers plus a floating "No data" line, or an empty state showing a Create button the user can't use.
- Sample data that leaks into reports, billing counts or exports, with no remove action.
- Three-level nested "Advanced" sections.
- Trial banners using red alarm styling and countdown timers from day one.
- Celebratory confetti on routine, repeated actions.

## Sources

- https://docs.appcues.com/checklist-best-practices
- https://www.intercom.com/blog/building-product-tours
- https://userpilot.com/solution/enterprise-saas-onboarding
- https://auth0.com/blog/user-onboarding-strategies-b2b-saas/
- https://workos.com/docs/directory-sync.md
- https://www.notion.com/en-gb/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
- https://kylepoyar.substack.com/p/your-guide-to-reverse-trials
- https://www.nngroup.com/articles/progressive-disclosure/
- https://www.nngroup.com/articles/onboarding-tutorials/
- https://www.nngroup.com/articles/complex-apps-users/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://www.nngroup.com/articles/designing-for-waits-and-interruptions/
- https://www.nngroup.com/articles/info-tips-bad/
- https://www.nngroup.com/articles/ui-accelerators/
- https://www.nngroup.com/articles/castle-framework/
- https://carbondesignsystem.com/patterns/empty-states-pattern/
- https://atlassian.design/foundations/content/designing-messages/empty-state
- https://cloudscape.design/patterns/general/empty-states/
- https://cloudscape.design/patterns/resource-management/create/single-page-create/
- https://design.gitlab.com/patterns/empty-states/
- https://www.patternfly.org/components/empty-state/design-guidelines
- https://primer.style/product/ui-patterns/empty-states
- https://design-system.service.gov.uk/patterns/complete-multiple-tasks/
- https://5x.ant.design/docs/spec/invitation
- https://lawsofux.com/goal-gradient-effect/
- https://lawsofux.com/zeigarnik-effect/
- https://www.cooley.com/news/insight/2025/2025-06-04-california-automatic-renewal-law-amendments-take-effect-on-july-1-2025
