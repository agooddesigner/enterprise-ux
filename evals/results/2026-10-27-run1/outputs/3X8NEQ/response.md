# Design brief: Approvals inbox for expense claims

I haven't seen any evidence about your users or product yet, so everything below is a working assumption. Nothing here comes from research. The questions at the end are the ones that would change the design most if I've got them wrong.

## Outcome
Finance managers clear their approval queue the same day, with fewer wrong approvals and fewer claims that sit untouched until they breach SLA.

Candidate solutions to compare:
1. **Worklist** (list on the left, claim detail on the right). Best for fast triage.
2. **Table with row drill-in.** Best for bulk approvals and scanning many claims.
3. **Email or Slack approve links.** Cheap, but weak on policy context. It's worth supporting later as a channel, not as the core.

My recommendation is option 1, with a table-style list and bulk selection for low-risk claims. Frequent approvers need both.

The riskiest assumption is that managers can decide from the list row plus a detail pane, without opening the receipt. Test this first.

## Audiences and roles
| Role | Cares about | Archetype |
|---|---|---|
| Finance manager (approver) | Clearing the queue fast without approving something wrong | "Time-pressed gatekeeper": 20–60 claims/day, or "Reluctant approver": 5/week |
| Delegate or backup approver | Picking up a queue they didn't build, with context | Learner |
| Employee (submitter) | Knowing the status and why a claim was rejected | Affected user (not the inbox user) |
| Finance admin | Approval rules, limits, delegation, audit | Admin |
| Auditor | Evidence that approvals were legitimate | Read-only |

Test the frequent and occasional approvers as separate groups. Their needs pull in opposite directions: speed and density for one, guidance for the other.

## Top jobs
1. **When** I start my day, **I want to** see what needs my decision, oldest and riskiest first, **so I can** clear it before payroll or close deadlines. *(daily, high volume)*
2. **When** a claim looks routine, **I want to** approve it in one action, or approve many at once, **so I can** spend my attention on the odd ones. *(daily, 70–80% of volume, assumed)*
3. **When** a claim looks off (duplicate, over policy, missing receipt, weekend or vendor anomaly), **I want to** see the reason flagged next to the receipt, **so I can** decide with confidence. *(daily, high criticality: this is money out)*
4. **When** I can't decide, **I want to** reject or return with a reason, or ask the submitter a question, **so I can** resolve it without email. *(several times a day)*
5. **When** I'm away, **I want to** delegate my queue, **so I can** avoid blocking people's reimbursements. *(occasional, needs guidance)*
6. **When** audit or a submitter asks why, **I want to** see who decided what and when, **so I can** defend the decision. *(occasional, high criticality)*

## Data and scale (assumed, to confirm)
- **Volume:** a median approver has roughly 10–30 pending claims. The p95 approver has 200+, especially at month end. Design for 500+, with server-side sort, filter and pagination.
- **Claim:** submitter, amount and currency (with converted amount), category, merchant, date, receipt (image or PDF, which can be multi-page), cost center, project, policy flags, comments and status.
- **Multi-line claims:** one report can hold 1–40 expense lines. Decide whether approvers act on the report, the line, or both. This is a major structural question.
- **Edge values:** very long merchant or description text, foreign currency, missing receipts, nulls for project or cost center, and zero-value or negative amounts (refunds).
- **Sensitivity:** financial data and personal data (mileage, meals, health-adjacent receipts), so audit trail and masking apply.
- **Freshness:** claims arrive continuously. Use polling or live updates without reshuffling the list under the user's cursor. Show "3 new claims" with a refresh affordance.

## Page archetype and structure
**Worklist** with a split view (list plus detail pane).

**List (left or top):**
- Default view is "Needs my decision", sorted by the oldest or most urgent first.
- Saved views and tabs: Needs my decision, Flagged, Waiting on submitter, Decided (last 30 days), Delegated to me.
- Row content: submitter, amount, category, date, age or SLA, and flag icons with text (never color alone).
- Filters: status, amount range, category, submitter, cost center, flag type, age. All filter state lives in the URL.
- Row height 40px, with a compact toggle.

**Detail pane:**
- Receipt viewer (zoom, rotate, multi-page) beside the claim fields.
- Policy flags with plain-language reasons ("Exceeds $75 meal limit by $12").
- Submitter's history for this category.
- Comments and the audit trail.
- Actions: **Approve** (the single primary), Reject, Return for changes, Reassign.

**Bulk:**
- Checkboxes with an "N selected" bar and an explicit "Select all N matching" step.
- Bulk approve is allowed only on unflagged claims, or it requires a confirmation that names the count and the total value.
- Bulk reject requires one shared reason.

## Key interaction decisions
- **Approve is reversible for a short window.** Act immediately, then offer Undo for about 10 seconds and hold the payment-batch handoff until the window closes. This beats a confirm dialog on a 40-a-day task. If approval triggers an irreversible payout immediately, change this to a confirm that names the amount and the payee. **This depends on a finance rule I don't know yet.**
- **Reject and return require a reason.** Offer common reason templates plus free text. Keep what the user typed if the action fails.
- **Advance to next claim after a decision**, with focus management so keyboard users don't lose their place.
- **Keyboard shortcuts for power users:** J/K to move, A to approve, R to reject, with a visible cheat sheet. All of it must also be reachable by mouse and screen reader.
- **Concurrency:** if another approver decides first, show "Already approved by Priya, 2 min ago" instead of an error, and remove the row gracefully.
- **Limits and segregation of duties:** approvers can't approve their own claims. If a claim is over their authority limit, show it as "Escalate to {name}" rather than hiding it, so the queue doesn't look wrong.
- **Never autosave decisions.** Every decision is explicit.

## Permissions matrix
| Action | Approver | Delegate | Admin | Auditor | Submitter |
|---|---|---|---|---|---|
| View assigned queue | ✓ | ✓ (delegator's) | ✓ all | ✓ read-only | ✗ |
| Approve within limit | ✓ | ✓ (within delegator's limit) | ✗ (assumed) | ✗ | ✗ |
| Approve over limit | Escalate | Escalate | Configurable | ✗ | ✗ |
| Approve own claim | ✗ (disabled, with reason) | ✗ | ✗ | ✗ | ✗ |
| Reject / return | ✓ | ✓ | ✗ | ✗ | ✗ |
| Reassign | ✓ | ✓ | ✓ | ✗ | ✗ |
| Edit approval rules | ✗ | ✗ | ✓ | ✗ | ✗ |

Hide controls the role can never use (for example admin rule editing, from approvers). Disable with a reason and a contact for things that are situationally unavailable ("You can't approve your own claim. Ask {manager}").

## States to design
- **First use / empty:** "You're all caught up" with the next-due date and one useful action. Distinguish this from a filtered view with no results ("No claims match. Clear filters").
- **Loading:** skeleton rows that match the list layout, with a separate loading state for the receipt.
- **Receipt failed to load:** an error with retry, never a blank pane. The approver must not be able to approve a claim they couldn't see evidence for without an explicit acknowledgement.
- **List load error:** an error with retry and last-updated time, not "No claims".
- **Partial failure in bulk:** "47 approved, 3 failed", with reasons and a way to retry only the failed ones.
- **Conflict:** already decided by someone else, or edited by the submitter while you were reviewing ("Claim changed since you opened it. Review changes").
- **Delegated or out-of-office** banner. **Read-only** for auditors. **No-permission** screen.
- **Offline or degraded** (policy engine down): show claims without flags and say so plainly, because silently hiding flags is dangerous.
- **Overflow:** very long merchant names, 40-line reports, 20-page receipts.

## Notifications (the inbox's front door)
- Offer digest and real-time options per user, plus a reminder before SLA breach. Avoid per-claim email floods.
- Email or Slack deep links open the exact claim in the inbox, with the URL carrying that state.

## Success metrics
Use task efficiency and errors, which is the right lens for a tool people can't opt out of (NN/g CASTLE):
- **Time to decision** per claim (median, and p90), and **queue age** (percent decided within SLA).
- **Task success and errors:** wrong-approval rate (later reversed or clawed back), undo rate after approve, and rejection reversals.
- **Efficiency:** share of claims decided in bulk or from the list without opening detail, and claims decided per active hour.
- **Learnability:** time to first decision for new or occasional approvers. SEQ per task and SUS each release.
- **Guardrail:** policy-violating claims that got approved, which should not rise as speed rises.

Baselines come from current email or spreadsheet workflows, which we don't have yet.

## Non-functional
- **Accessibility:** WCAG 2.2 AA. Full keyboard path for triage, visible un-obscured focus, 24px minimum targets, a click alternative to any drag, and no color-only flags. A split pane must still work with a screen reader (landmarks, live-region announcement when advancing to the next claim). Receipts need extracted text or an alternative where possible.
- **Performance:** feedback within 100ms. Prefetch the next claim and its receipt so advancing feels instant. INP at or under 200ms.
- **Localization:** multiple currencies and locale-aware amounts, with time zones on timestamps. Use absolute timestamps with a time zone for approval records, since they're audit evidence.
- **Devices:** desktop-first (1280px+). Approving from a phone is a real need for managers on the move, so plan at least a lightweight mobile approve and reject view for v1.5.
- **Compliance:** immutable audit log of every decision (who, when, what the approver saw, on whose behalf), export, and retention rules.

## Release slices
**Walking skeleton (v1):** worklist with "Needs my decision", the detail pane with the receipt, approve, reject with a reason, a basic flag display, the full state set, audit log entries, URL state, and keyboard basics.

**v1.1:** bulk approve (unflagged only), saved views and filters, undo window, delegation, concurrency handling.

**Later:** mobile view, Slack or email actions, smart sorting by risk, AI-suggested flags (if used, label them, show the reason, and keep the decision human), and analytics for admins.

**Must-be items that should not slip to "later":** roles and limits, audit trail, export, all states, and accessibility.

## Risks and open questions (ranked)
1. **Report vs line-level approval.** It changes the data model and the whole list design. *Owner: product plus finance.*
2. **What approval triggers.** An immediate payout, a batched payment run, or an ERP sync decides whether Undo is possible. *Owner: finance ops, engineering.*
3. **Where flags come from.** If the policy engine doesn't exist, the "flagged" experience in v1 will be thin.
4. **Bulk approval risk.** Fast clicking raises the odds of rubber-stamping. We need a guardrail agreed with compliance.
5. **Existing tools.** If managers work in Concur, Expensify, Slack or email today, we need to know what they'd expect to carry over (Jakob's Law).
6. **Delegation and escalation rules** (limits, chains, out-of-office) are probably more complex than they look.

## Research plan
- Interview and observe 5–6 real approvers, split across frequent and occasional, plus 2 delegates and 1–2 admins and auditors. Watch them clear a real queue, including the interruptions.
- Collect 30–50 real (anonymized) claims to design with, including the ugly ones.
- Run a cognitive walkthrough before building. Then moderated tests (about 5 per role group) on a clickable prototype of triage, a flagged claim, and bulk approve. If real approvers are scarce, use internal finance staff and say so.

## Assumptions I made
- Roughly 10–30 claims per approver per day for the median approver, with month-end spikes.
- Most claims (70–80%) are routine and unflagged.
- Approval doesn't pay out immediately, so a short undo window is feasible.
- Desktop is primary. Approvers can't approve their own claims.
- A policy-flagging capability exists or is planned.

## Questions I'd answer first
1. **Do approvers decide on whole reports or individual lines?**
2. **What happens the moment someone clicks Approve?** Is it an immediate payment, a batch run, or a sync to another system? This decides undo versus confirm.
3. **Roughly how many claims does a typical approver handle per day or week, and what do they use today?** This sets the balance between speed and guidance.

If you can answer those, I'd run **Grill** mode on this brief next, and then move to designing the worklist screen with all its states. I can also publish this as a shareable page if you want to circulate it.
