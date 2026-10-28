# Mode: Plan

**Load when:** the user is starting a feature, product, or redesign and there is no agreed brief yet — "we need a…", "help me plan…", "how should we approach…", a PRD to turn into UX, or any build request too vague to design safely.

Goal: turn a request into a **Design Brief** that names the job, the people, the data, the risks and how success is measured — before anyone draws a screen. In enterprise software the expensive mistakes are made here, not in the pixels.

---

## The planning sequence

Work through these in order. Skip a step only when the answer is already known and stated; write down what you assumed.

### 1. Frame the outcome, not the feature
- Restate the request as an outcome the team can influence ("approvers clear their queue same-day"), not a feature ("add a dashboard"). (Opportunity Solution Tree, Torres)
- Map outcome → opportunities (user needs/pain points, from evidence) → candidate solutions (compare ~3, don't marry the first) → the riskiest assumption to test. (Torres)
- Check that the problem is worth software at all. For AI features, check AI adds unique value over a rule, filter or default. (PAIR, see `saas/ai-features.md`)

### 2. Identify every audience
Enterprise products have at least three, with different surfaces and goals: (Notion, Stripe, Vercel docs)

| Audience | Cares about | Typical surface |
|---|---|---|
| Buyer / economic decision-maker | Risk, compliance, cost, vendor trust | Pricing, security page, admin reports |
| Admin / IT / security | Control, SSO/SCIM, roles, audit, rollout | Org console, settings, audit log |
| End user (often several roles) | Getting the daily job done fast | Core workflow screens |

- Split end users by **role** (requester, approver, analyst, ops) — each is a distinct user group for testing. (NN/g, 5-users-per-group)
- Describe users as **archetypes** by behaviour and goal ("Reluctant approver", "Power configurer"), not demographic personas. (Yale/NN/g)
- Account for the three complex-app user types: **Legacy** (long-time, inefficient workarounds — change gradually), **Legend** (power users — keep them fast), **Learner** (domain experts new to the tool — inline help, templates). (NN/g)

### 3. Write the jobs
- Use job stories: **When** [situation], **I want to** [motivation], **so I can** [outcome]. (Intercom JTBD)
- Bad: "I want a dashboard." Good: "When a renewal is 30 days out and usage dropped, I want to see which teams went inactive, so I can intervene before the QBR."
- For each job record: **frequency** (per day/week/quarter), **criticality** (cost of an error), **time pressure**, **interruptions**. Frequency decides density and speed vs guidance:
  - High-frequency (10+/day): optimise for speed — density, keyboard, bulk, saved views, few confirmations, undo.
  - Low-frequency (monthly/quarterly): optimise for guidance — wizards, defaults, inline help, review step.

### 4. Understand the domain and constraints
- Learn the domain vocabulary, roles, hand-offs and regulations **before** ideating; observe real work (interruptions, noise, multitasking). (NN/g strategies for complex apps)
- Set **viability criteria** up front: regulatory/compliance rules, audit needs, data residency, risk tolerance. (NN/g)
- Ask where users work today (Excel, email, another SaaS) — design export/copy/integration paths so they don't re-key data. (NN/g complex apps #5, Jakob's Law)

### 5. Model the data honestly
For each object in the feature record:
- Realistic volume (median and p95: 10? 10k? 10M rows), growth rate.
- Longest realistic value per field, nullable fields, multi-valued fields.
- Identifier users recognise (name, invoice #) vs system IDs.
- Hierarchy/relationships (parent-child, many-to-many).
- Freshness: real-time, polled, batch? How stale can it be?
- Sensitivity: PII, financial, security — affects masking, autosave, audit, export.
Volume drives the pattern: Fiori switches from responsive table to grid at ~1,000 rows; >400 related items need their own list page (see `patterns/tables.md`).

### 6. Map flows and slice the release
- Build a **story map**: user activities left→right (the backbone), tasks beneath, then cut horizontal release slices. Each slice must be a usable end-to-end path — the **walking skeleton** first. (Patton)
- For cross-team or service-heavy work, sketch a **service blueprint** (frontstage, backstage, support processes) — most enterprise failures live backstage (provisioning, approvals, data migration). (Shostack)
- Mark decision points, approvals, async waits and hand-offs between roles.

### 7. Plan the information architecture
- Fit new screens into existing navigation patterns (Jakob's Law; see `patterns/navigation-and-layout.md`).
- Choose a page archetype per job (list report, worklist, object page, wizard, dashboard…).
- Large or contested IA → plan an open card sort (15–30 people) then a tree test (~50 per task) before building. (NN/g, CleverX)

### 8. Inventory states and permissions up front
- List every state per view (see the matrix in `patterns/feedback-and-states.md`): first-use empty, no results, loading, refreshing, partial error, full error, no permission, read-only, degraded, overflow.
- Draft a **permission matrix**: rows = actions, columns = roles, ✓/✗. Decide for each ✗ whether the control is hidden or disabled-with-reason. (GitHub, Stripe; see `saas/accounts-and-permissions.md`)

### 9. Define success measures
- Pick only the **HEART** categories that match the goal (Happiness, Engagement, Adoption, Retention, Task success), then Goal → Signal → Metric. Don't track all five by default. (Google HEART)
- For workplace tools users can't opt out of, prefer **CASTLE**: Cognitive load, Advanced-feature adoption, Satisfaction, Task efficiency, Learnability, Errors. (NN/g)
- Behavioural first: task success, time on task (median, successful attempts), error rate. Attitudinal second: SEQ per task (avg ≈5.5/7), SUS per release (avg 68; not a percentage). (MeasuringU)
- Treat NPS with caution in B2B — the respondent is often not the buyer, and it measures intent not behaviour. (UIE)
- AI features: add intervention rate, undo/rollback rate with reasons, unintended actions per 1,000 tasks. (see `saas/ai-features.md`)

### 10. Prioritise
- **Kano**: in enterprise, SSO/SAML, SCIM, RBAC, audit log, export and accessibility are **Must-be** — missing them blocks the sale regardless of delighters. (Kano model)
- **RICE** = (Reach × Impact × Confidence) ÷ Effort to compare items; it starts a discussion, it doesn't end one — one big customer can distort Reach. (Intercom/ProductPlan)
- Pareto: make the top 20% of workflows flawless before polishing the long tail — but don't cut long-tail compliance features enterprise buyers require. (Pareto)

### 11. Plan the research
Choose methods by question (NN/g research landscape):

| Question | Method | Notes |
|---|---|---|
| What do users actually do / need? | Field study, contextual inquiry, interviews, diary study | Discovery; go to real work |
| How should content be grouped? | Open card sort | 15–30 participants |
| Can people find things in this IA? | Tree test | ~50 per task |
| Is the first step obvious? | First-click test | Correct first click → ~87% success |
| Can people complete the task? | Moderated usability test, think-aloud | ~5 per distinct role, iterate in rounds |
| Is it learnable without help? | Cognitive walkthrough (expert) | Before code exists |
| How usable vs last release? | Benchmark: task success, time, SEQ, SUS | 20+ participants for numbers |
| Which variant performs better? | A/B test | Often underpowered in B2B — check traffic |

If real users are scarce (common in enterprise), test with knowledgeable internal staff and domain experts, and say so. (NN/g)

### 12. Non-functional requirements (state them explicitly)
- Accessibility target: **WCAG 2.2 AA** (see `foundations/accessibility.md`; legal drivers there).
- Performance: INP ≤200ms, LCP ≤2.5s at p75; feedback within 100ms. (web.dev; see `saas/global-and-performance.md`)
- Localization: locales, RTL, time zones, text expansion budget.
- Devices: primary viewport (usually 1280–1440px laptops), touch needs, minimum supported width.
- Security/compliance: audit logging, data masking, retention, two-person approval for sensitive actions.

---

## Enterprise "Must-be" checklist (flag any that are missing)

- [ ] Roles & permissions designed (not "later")
- [ ] SSO / SCIM implications considered (synced read-only fields, JIT users)
- [ ] Audit trail for create/update/delete and permission changes
- [ ] Export of data the user can see (respecting filters)
- [ ] Bulk actions for anything done to many records
- [ ] All states designed (empty, loading, error, no-access)
- [ ] Undo or confirmation for every destructive action
- [ ] Shareable URLs for views, filters and records
- [ ] Keyboard operability and WCAG 2.2 AA
- [ ] Time zones and locale formats handled
- [ ] Admin controls/rollout for anything that changes behaviour org-wide

---

## Output: the Design Brief

Produce this (as a document, or inline if short). Keep it to what the team will actually use.

```
# Design brief: <feature>

Outcome: <measurable outcome>
Problem evidence: <what we know and how; what's assumed>

Audiences & roles: <buyer / admin / end-user roles, archetypes>
Top jobs (job stories) with frequency & criticality:
1. When … I want to … so I can …  — 40×/day, high criticality
2. …

Data model & scale: <objects, volumes p50/p95, longest values, sensitivity>
Key flows & release slice: <walking skeleton, what's in v1 vs later>
Page archetypes: <list report / object page / wizard …>
Permissions matrix: <table>
States to design: <list per view>
Success metrics: <HEART/CASTLE goals → signals → metrics, baselines>
Non-functional: <WCAG 2.2 AA, perf, locales, devices, compliance>
Risks & open questions: <ranked; owner; how we'll resolve>
Research plan: <method, participants per role, timing>
Assumptions made: <explicit list>
```

Then recommend running **Grill** mode (`modes/grill.md`) on the brief before design starts.

## Common AI failures
- Jumping straight to screens without naming the job, frequency or user role.
- One generic "user" persona; the admin and the buyer are forgotten.
- Seed-data thinking: designing for 6 tidy rows when production has 50,000.
- Metrics that are page views or "engagement" with no link to the outcome.
- Treating SSO, RBAC, audit and export as v2 extras instead of Must-be.
- Inventing user research findings — always label assumptions as assumptions.

## Sources
This mode routes to other files; each rule cites its source there. Full list: `references/sources.md`.
