# Billing and monetization

**Load when:** designing or auditing pricing pages, plan matrices, usage meters, spend caps, upgrade prompts, paywalls, seat management, billing portals, invoices, cancellation/retention flows, or billing notifications. Legal notes here are design inputs, not legal advice — get counsel.

## 1. Pricing page

- Few tiers. One plan + Enterprise is a valid model. With many plans use tabs, a plan picker or wrapping — **never horizontal scroll**. (Smashing pricing)
- Highlight one recommended plan (centre, stronger CTA); mark it with text ("Recommended"), not colour alone. (Smashing pricing; lawsofux choice overload; WCAG 1.4.1)
- Billing-period toggle (monthly/annual) at the top, sticky with plan headers on long pages; show the annual discount explicitly. Annual default is common. (Smashing pricing)
- Explain **how price is calculated** with a worked example; show add-ons early (seat/usage sliders); state what's not included. (Smashing pricing)
- Show recurring amount **and** frequency before purchase ("$24 per seat per month, billed annually: $2,880"). (Latham & Watkins — design rule)
- Keep "Contact sales" for Enterprise separate and lower in emphasis than self-serve CTAs. (Smashing pricing)
- Watch anchoring on pricing screens; never invent a crossed-out "original" price. (lawsofux cognitive bias)

## 2. Plan matrix

- Top: 3–6 key differentiators per plan. Below: full matrix with sticky plan headers, category accordions, and a "Show differences only" filter. (Smashing pricing)
- Users hunting a must-have feature conclude no plan has it if they can't find it fast → make the matrix **searchable** (Ctrl-F friendly, real text) and scannable. (Baymard)
- Cells: ✓ / ✗ / limit with text ("Up to 5 projects"), never icon colour only; use "—" for not applicable. (WCAG 1.4.1; see `foundations/defaults.md`)
- Mobile: stacked plan cards or tabs; replace hover tooltips with tap-to-expand. (Smashing pricing)
- Enterprise checklist items (SSO, SCIM, audit log retention, custom roles, approvals) belong in the matrix — buyers look for them. (Notion, GitHub, Stripe)

## 3. Usage meters and projected cost

- Usage page per line item: consumed vs included (allotment bar + numbers), **projected cost** for the period, breakdown by project/region; default to a 30-day view. (Vercel)
- Label units in billing units ("32 hours", not "1 day 8 hours"). (Cloudscape timestamps)
- Show the measurement timestamp ("Usage as of 14:00 UTC"), not page-load time. (Lightning metrics)
- Meters need text values and thresholds, not colour alone; warn at defined levels (e.g. 75/90/100%) (general practice for the levels).
- Scope usage to the selected team/workspace and say so. (Vercel)

## 4. Spend caps and alerts

- Spend management is opt-in: a dollar cap that triggers a notification, a webhook, or pausing projects — the admin chooses the action. (Vercel)
- Usage alerts at configurable % or $ thresholds; owner-only to configure. (Vercel)
- When a user disables usage alerts, warn inline that this may lead to surprise charges. (Vercel)
- Pausing on cap is destructive to production — explain what stops and how to resume before saving. (Vercel; see `patterns/actions-and-dialogs.md`)
- Treat spend governance as an enterprise expectation, not an SMB nicety. (Vercel)

## 5. Upgrade prompts and paywalls — no dark patterns

- Show an upgrade path **where the limit is hit**, as a plan-limit empty state or inline message: what's limited, which plan unlocks it, price, and a non-upgrade way forward (remove items, contact admin). (Pajamas "higher tier needed")
- Distinguish plan limits from permission limits. Non-billing users get "Ask your admin to upgrade" with who; only billing roles get the Upgrade button. (Atlassian, Vercel)
- Feature discovery: prefer nothing, then a badge/popover; a modal only as last resort and never unprompted on load. (Pajamas, Carbon)
- Upsell banners use the "upsell" variant, are dismissible, and stay dismissed for the session. (Primer, Polaris)
- **Never**: fake scarcity or fake countdowns, pre-checked add-ons, confirmshaming ("No, I like losing data"), hiding the downgrade path, or exploiting biases in upgrade modals. (lawsofux cognitive bias; FTC Act §5 per Latham & Watkins)
- Never block a user's own data behind a paywall without notice — downgrade keeps read/export access. (general practice)

## 6. Seat management

- Show seats purchased / assigned / available, cost per seat, and next renewal date in one place. (Stripe portal)
- Adding users that consume seats shows the cost **before** confirming — inviting, approving access requests, and SCIM auto-provisioning alike. (Atlassian)
- Proration: say whether changes apply now (prorated) or at period end; schedule downgrades for period end. (Stripe portal)
- Removing a user: say whether the seat is released now or at renewal. (general practice)

## 7. Self-serve billing portal baseline

Customers can, without contacting sales: update payment method; billing details and tax ID; view and download invoice history; switch plans; change quantity (seats); apply promo codes; cancel. (Stripe portal)
- After cancelling, access continues to period end and the customer can renew until then — show that date. (Stripe portal)
- Restrict the portal to billing-capable roles; others see a read-only summary + "Billing is managed by [name]". (Vercel)
- Never autosave payment or billing details; explicit Save. (see `foundations/defaults.md`)

## 8. Invoices

- Invoice list: number, issue date, period, amount + currency, status (Paid / Open / Failed / Void as text badges), download PDF. (Stripe portal; WCAG 1.4.1)
- Absolute dates with time zone in billing (see `foundations/defaults.md`); currency formatted per locale with ISO code where ambiguous (see `saas/global-and-performance.md`).
- Failed payment: persistent banner for billing roles with the reason, the deadline before service impact, and "Update payment method". (Vercel; Polaris critical banner)

## 9. Cancellation flow

1. **Cancel entry point is prominent and online** if signup was online — a direct link/button, same medium as signup. (Cooley, KTS — California)
2. Optional reason survey: too expensive, missing features, found an alternative, no longer needed, customer service, ease of use, quality, other + free text. (Stripe)
3. **At most one save offer** — one discount *or* one downgrade, targeted by reason/tenure/spend. Retention discounts are single-use per customer. Downgrade offers show the lower plan's features and take effect at period end. (Stripe retention)
4. The "Cancel subscription" option stays **prominently and continuously visible alongside** the offer. (California ARL per Cooley/KTS)
5. Confirmation: end date of access, what happens to data and how long it's retained, how to export, "Renew" until period end. (Stripe portal)

- No phone-only cancellation, no chat-agent gate, no multi-page offer gauntlet. (Latham & Watkins — design to strictest standard)

## 10. Legal context (verify — as of Oct 2026; not legal advice)

- **FTC "click-to-cancel" rule vacated**: the 2024 Negative Option amendments were vacated in full by the 8th Circuit on 8 Jul 2025 (*Custom Communications v. FTC*), days before the 14 Jul 2025 compliance date, on procedural grounds; merits not decided. (Latham & Watkins — verify — as of Oct 2026)
- **ANPRM, Mar 2026**: the FTC restarted rulemaking (announced 11 Mar, published 13 Mar 2026, comments due 13 Apr 2026). It asks about obstructed cancellation **including B2B deals**, whether save offers in place of honouring a cancel are unfair, and about consent-record retention, recurring-charge disclosure and simple cancellation. It is an ANPRM, not a proposed rule. (Greenberg Traurig, Subscription Insider — verify — as of Oct 2026)
- Unknown: whether any NPRM followed or Supreme Court review was sought. (verify — as of Oct 2026)
- **Still binding**: ROSCA, FTC Act §5 (deceptive/unfair practices), state auto-renewal and UDAP laws. Counsel's advice: don't roll back compliant flows; design to the strictest state. (Latham & Watkins — verify — as of Oct 2026)
- **California ARL** (effective 1 Jul 2025 for new/renewed contracts) (Cooley, KTS — verify — as of Oct 2026):
  - Online signup → fully online cancel via prominent direct link/button, or a pre-written termination email.
  - Save offers allowed only while "click to cancel" stays prominently and continuously visible.
  - Express affirmative consent to renewal terms (unticked checkbox); keep consent records ≥3 years or 1 year after termination, whichever is longer.
  - Annual reminder; price-change notice 7–30 days before it applies.
  - Free trial >31 days → notice 3–21 days before conversion; terms ≥1 year → notice 15–45 days before renewal.
  - **B2B scope is unclear** — sources frame it around consumers. Treat as uncertain; get counsel.
- Design rule: cancellation as easy as signup, same medium; ≤1 save offer with persistent cancel; explicit auto-renew consent checkbox; charge amount and frequency shown before purchase; renewal and price-change reminders. (Latham & Watkins synthesis)

## 11. Billing notifications

- Billing notices go to people who can manage billing; "Invoice payment failed" is non-configurable for billing roles. (Vercel)
- Usage alerts go to owners; renewal and price-change notices to billing contacts with dates and amounts. (Vercel; California ARL)
- Use email for out-of-product billing events plus an in-app banner for billing roles; SMS only for spend alerts if offered. (Vercel) See `saas/notifications-system.md`.

## 12. White-label

- Billing portal, invoices and billing emails need at minimum: logo, icon, colours, font, button shape, custom domain — so resellers' customers never see your brand. (Stripe portal)

## Common AI failures

- Pricing table that scrolls horizontally on mobile, or colour-only ✓ cells.
- "Contact sales" as the loudest CTA on a self-serve product; price shown without frequency.
- Upgrade modal popping on load with a fake countdown or "Only 3 seats left at this price".
- Paywall shown to non-billing users with an Upgrade button they can't use.
- Cancel buried under Settings → Help → Chat, or a three-offer retention gauntlet with cancel hidden.
- Pre-ticked auto-renew consent.
- Seat-consuming invites with no cost shown.
- Usage meter with a red bar and no numbers or projected cost.
- Treating the vacated FTC rule as either fully in force or as meaning "no rules apply".

## Sources

- https://smashingmagazine.com/2022/07/designing-better-pricing-page
- https://baymard.com/ecommerce-design-examples/plan-matrix
- https://docs.stripe.com/customer-management/configure-portal
- https://docs.stripe.com/customer-management/cancellation-page
- https://docs.stripe.com/billing/retention/rules
- https://vercel.com/docs/pricing/manage-and-optimize-usage
- https://vercel.com/docs/notifications
- https://confluence.atlassian.com/cloud/access-request-improvements-978205737.html
- https://www.lw.com/en/insights/eighth-circuit-vacates-ftc-click-to-cancel-rule
- https://www.gtlaw.com/en/insights/2026/3/ftc-seeks-comment-on-potential-updates-to-negative-option-rule
- https://www.subscriptioninsider.com/article-type/news/ftc-restarts-negative-option-rulemaking-after-click-to-cancel-vacatur-signaling-subscription-rules-are-back-in-play
- https://www.cooley.com/news/insight/2025/2025-06-04-california-automatic-renewal-law-amendments-take-effect-on-july-1-2025
- https://ktslaw.com/insights/alert/2024/10/california-latest-automatic-renewal-law-amendments-take-effect-in-july-2025
- https://lawsofux.com/cognitive-bias/
- https://lawsofux.com/choice-overload/
- https://design-gitlab-com-gitlab-org-gitlab-services-f6beaf2fb7fd4cad76.gitlab.io/patterns/choosing-a-messaging-pattern/
- https://design.gitlab.com/patterns/empty-states/
- https://primer.style/ui-patterns/notification-messaging
- https://shopify.dev/docs/apps/design-guidelines/user-experience/alerts
- https://cloudscape.design/patterns/general/timestamps/
- https://spring-21.lightningdesignsystem.com/guidelines/data-visualization/metric-display
