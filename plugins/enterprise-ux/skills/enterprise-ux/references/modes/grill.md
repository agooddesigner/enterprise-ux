# Mode: Grill

**Load when:** the user asks to "grill", stress-test, poke holes in, challenge or pressure-test a requirement, brief, PRD, flow or design — or before building anything expensive whose requirements look thin. Also run a short grill automatically at the end of Plan mode.

Goal: find the questions that, if answered wrong, would make the team build the wrong thing — and force answers (or explicit assumptions) before design or code starts. Grilling is respectful but relentless: you are the senior designer in the review who has seen this fail before.

---

## Rules of engagement

1. **Read everything first.** Don't ask what the brief, the codebase, the existing design system or a quick lookup already answers.
2. **Rank by cost of a wrong guess.** Ask the questions whose wrong answer would force a rebuild first (data volume, roles, irreversibility, compliance). Cosmetic questions last or never.
3. **Batch, don't drip.** Ask at most 5 questions per round, numbered, each with *why it matters* in one line and a *default assumption* you'll use if there's no answer.
4. **Push back with evidence.** When a requirement conflicts with a known rule, name the rule and the source ("A confirm dialog on every delete trains click-through — NN/g, Ant recommend Undo instead").
5. **Separate facts, assumptions and opinions.** Label each answer as confirmed, assumed, or needs research.
6. **If the user is away, don't stall.** Record your default assumptions in the grill log and proceed; mark them for review.
7. **Don't grill for sport.** Stop when remaining unknowns are cheap to change later.

---

## Question bank (pick the relevant ones; don't dump the whole list)

### Problem & outcome
- What outcome changes if this ships? How will we know in 30/90 days?
- What evidence says this is a real problem — tickets, observation, data, or one loud customer?
- What do users do today instead (spreadsheet, email, another tool)? What's wrong with it?
- What happens if we build nothing?
- Is this a feature disguised as a job ("users want a dashboard")? What decision does the dashboard support?

### Users, roles & frequency
- Which roles touch this? Who creates, who approves, who only views, who administers?
- How often does each role do this job (per day/week/quarter)? Under what time pressure?
- Are there external users (guests, customers, vendors) with different permissions?
- Who is the buyer, and what will they check in a demo or security review?
- Which users are legacy power users whose habits we'll break?

### Data & scale
- How many records at p50 and p95 per tenant? In two years?
- What's the longest realistic value for each displayed field? Which fields can be empty?
- Which identifier do users recognise — name, number, or system ID?
- How fresh must the data be? What happens when it's stale?
- Is any of it sensitive (PII, financial, security)? Who may see it masked vs unmasked?

### States & failure
- What does a brand-new tenant see on day one (first-use empty)?
- What happens when filters return nothing? When the API times out? When one widget fails but others work?
- What happens to work in progress if the session expires or the network drops?
- What's the slowest operation? Does it need background processing, progress and cancel?

### Permissions & governance
- For each action, which roles can do it? Hidden or disabled-with-reason for others?
- Can permissions be inherited or locked from org level? How does the UI explain a locked setting?
- Which actions need an audit trail? Which need two-person approval?
- Are any fields managed by SSO/SCIM (read-only in our UI)?
- Will support staff need to view a customer's account ("view as user")? Under what consent, and is it logged?
- Any data-residency, retention or deletion (privacy-request) obligations that change what we show, export or keep?

### Destructive & irreversible actions
- What can be deleted, overwritten, sent or published? Is it reversible? For how long?
- What's the blast radius of a bulk action (10 records? 10,000? other tenants' data?)
- Could Undo / soft delete replace a confirmation dialog here?

### Workflow & edge cases
- What interrupts this task? Can users leave and resume (drafts, save-and-return)?
- Two people editing the same record at once — what happens?
- What's the most common error users will make? Can we prevent it instead of messaging it?
- What's the path for keyboard-only and screen-reader users? For drag-and-drop steps, what's the click alternative?

### Global, legal & compliance
- Which locales, languages, RTL, time zones? Are timestamps used for audit or billing?
- Which accessibility standard do contracts require (WCAG 2.1/2.2 AA, Section 508, EN 301 549)? Do buyers need a VPAT/ACR?
- Any consumer-facing part (portals, signup, checkout) that pulls the product into EAA or auto-renewal law scope? (see `foundations/accessibility.md`, `saas/billing.md`)
- Any AI output shown to users or customers — does it need disclosure? (see `saas/ai-features.md`)

### AI features (if any)
- What can it do, and how well? How do users find out? (HAX G1–G2)
- What happens when it's wrong — how does the user dismiss, correct, undo?
- Does it act or only suggest? Who approves actions? What's logged?
- Is there a non-AI path for users who don't trust it?

### Success & scope
- What's the walking skeleton — the thinnest end-to-end slice that's useful?
- What are we explicitly *not* doing in v1?
- How will we test it, with which roles, and how many participants per role?

---

## Red flags (call these out directly)

| Red flag | Why it hurts | Push back with |
|---|---|---|
| "Make it like [competitor]" with no job behind it | Copies their constraints and mistakes | Ask which job their pattern solves; Jakob's Law supports conventions, not cloning |
| "Users want a dashboard" | Dashboards without questions become chart walls | Name the 3–5 decisions it must support (NN/g) |
| Only one persona / no admin | Admin, buyer and approver flows get bolted on later | Role list + permission matrix |
| "We'll add permissions later" | Retrofitting RBAC changes every screen's states | Must-be in enterprise (Kano) |
| Demo data of 5–10 rows | Pagination, filters, performance, truncation all untested | p95 volume, longest values |
| "Add a confirmation dialog" for everything | Click-through blindness; slows experts | Undo for reversible actions; typed confirm only for critical |
| "Just disable the button" | Users can't tell why; tooltips on disabled elements fail a11y | Keep enabled + explain, or disabled-with-reason pattern |
| "AI will figure it out" | No scope, no error path, no trust calibration | HAX guidelines, autonomy ladder |
| Success = "engagement" / page views | Can't tell if the job got easier | HEART/CASTLE goal → signal → metric |
| Toast for important errors | Disappears, unreachable by keyboard | Inline or persistent message |
| "Accessibility in a later phase" | Retrofitting costs more; legal/procurement risk | WCAG 2.2 AA from the start |
| Wizard for a task users repeat 30×/day | Forces slow path on experts | Single dense form + saved defaults |

---

## Output: the grill log

```
# Grill log: <feature> — round <n>

| # | Question | Why it matters | Answer / default assumption | Status | Risk if wrong |
|---|---|---|---|---|---|
| 1 | p95 rows per tenant? | Decides pagination, virtualisation, filter design | Assume 20k | Assumed | High — rebuild table |
| 2 | … | … | … | Confirmed | … |

Pushbacks raised:
- <requirement> → <concern> → <recommended change> (source)

Ready to design? <Yes / Yes with assumptions flagged / No — blockers: …>
```

Close each round with the single most dangerous open question. When ready, move to **Design** mode (`modes/design.md`).

## Common AI failures
- Asking 20 generic questions instead of the 5 that matter.
- Asking things already answered in the brief or visible in the codebase.
- Accepting "make it like X" or "add a dashboard" without asking which job it serves.
- Being agreeable instead of honest — not naming a bad requirement as bad.
- Stalling when the user is away instead of proceeding with logged assumptions.

## Sources
This mode routes to other files; each rule cites its source there. Full list: `references/sources.md`.
