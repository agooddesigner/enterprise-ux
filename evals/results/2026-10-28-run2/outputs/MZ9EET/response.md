# Design brief: Approvals inbox for expense claims

You haven't designed anything yet and I haven't seen your product, so what follows is a draft built on assumptions. Please correct the ones in "Questions" first, because they change the design most.

## Outcome
Finance managers clear their approval queue the same day, accurately, without opening a spreadsheet or chasing context.

Possible measures: median time per claim, share of claims decided within the SLA, and the rate at which approved claims are later reversed or flagged by audit.

## Audiences
| Role | Cares about |
|---|---|
| **Finance manager (approver)** | Clearing the queue fast, and not approving something wrong. This is the primary user. |
| Claimant (employee) | Knowing the status and what to fix when a claim is rejected or returned. |
| Finance admin | Approval rules, delegation, thresholds and audit. |
| Auditor / controller | A trail showing who decided what, when and why. |
| Buyer | Control and compliance (SoD, audit log, export). |

The archetype I'd design for is the **batch approver**. They sit down once or twice a day to work through 20–80 claims. Most are routine, and a few need real scrutiny. The design problem is making the routine ones very fast while the odd ones stand out.

## Top jobs
1. When I open the inbox, I want to see what needs me now, ordered by urgency, so I can clear what's due first. *(daily, high frequency)*
2. When a claim looks routine and within policy, I want to approve it without opening it, so I can get through the batch quickly. *(dozens a day)*
3. When a claim looks off (over limit, duplicate, missing receipt, odd category), I want to see why it was flagged and the evidence beside it, so I can decide with confidence. *(a few a day, high criticality)*
4. When I can't decide yet, I want to return it with a question or reject it with a reason, so the claimant knows what to do. *(daily)*
5. When I'm away, I want to delegate my queue, so claims don't stall. *(occasional)*
6. When an auditor asks, I want to show who approved what and why. *(rare, critical)*

## Data and scale to confirm
- Queue size is probably a median of 20–40 and a p95 of a few hundred, which is table territory, not cards.
- A claim has a claimant, amount and currency, category, date, merchant, receipt images or PDFs, multiple line items, policy flags, and the approval chain.
- Edge cases to design for: a multi-currency claim, a claim with 30 line items, a missing or illegible receipt, a very long merchant or description, a zero-value line, and a claim that is withdrawn or already decided by someone else while you're looking at it.
- Money and receipts are sensitive. Nothing here should autosave a decision.

## Structure
The main pattern is a **worklist with a split view**: a dense table on the left or top, and a detail pane showing the receipt and policy checks on the selected row. Reviewing a claim shouldn't mean leaving the list.

**List**
- Columns: claimant, amount (right-aligned, with currency), category, submitted date, age or SLA, flags, and status.
- Default sort by SLA or age, oldest first.
- Saved views and tabs: Needs my decision, Flagged, Waiting on claimant, Decided.
- Filters for claimant, team, category, amount range and date, all kept in the URL.
- Row height 40px with a compact toggle. Use "—" for empty cells.

**Detail pane**
- The receipt next to the extracted fields. A flag explains why it was flagged ("Over the €75 meal limit by €12") instead of showing a bare red icon.
- The claimant's history and the approval chain.
- Primary action is **Approve**. Secondary actions are **Return with comment** and **Reject**, which both require a reason.

**Bulk actions**
- Select several rows and approve them in one go. The confirmation names the count and the total ("Approve 14 claims, €2,310.40").
- Exclude flagged claims from bulk approval by default, or call them out so approving them is a deliberate choice.
- Clear the selection when the filter changes, and always show "N selected".

**Keyboard**
- Arrow keys to move, `A` to approve, `R` to reject or return, `Enter` to open. Keep the shortcuts discoverable, since power users will live in this view.

**Decisions**
- Approve is reversible within a short window, so act immediately and show an Undo.
- Reject and Return need a reason and notify the claimant. Rejection is hard to reverse, so confirm it, naming the claim and the consequence.
- Because it's money, approvals shouldn't be fully undoable after the payment run, so say what happens after Undo expires.

## Permissions to decide
| Action | Approver | Delegate | Finance admin | Auditor |
|---|---|---|---|---|
| View assigned claims | ✓ | ✓ | ✓ (all) | ✓ (read-only) |
| Approve / return / reject | ✓ within limit | ✓ | ✓ | ✗ |
| Approve own claim | ✗ | ✗ | ✗ | ✗ |
| Approve above their limit | Escalate | Escalate | ✓ | ✗ |
| Reassign / delegate | ✓ | ✗ | ✓ | ✗ |
| Export | Own queue | Own queue | All | All |

Where an action is blocked, the control should be **disabled with a reason and who can help** ("Over your €5,000 limit. Escalated to Dana Reyes"), not hidden. Never let someone approve their own claim, and make sure that holds through delegation and rule changes.

## States to design
- First use or empty queue ("You're all caught up", plus when the next claim is due if known). This differs from no results under filters, which gets "Clear filters".
- Loading (skeleton rows) and refreshing.
- Load failed, shown as an error with Retry, never as "No data".
- Partial failure on bulk approve ("11 approved, 3 failed", with reasons and a way to retry the 3).
- Claim changed while open (withdrawn, decided by another approver, amount edited). Show a banner and block a stale decision.
- No permission, read-only (auditor), and delegated mode.
- A very long list, an offline receipt or one that failed to load, and a receipt that is a PDF or HEIC.

## v1 slice
The thinnest useful end-to-end path:
1. Worklist with sort, filters and saved tabs.
2. Detail pane with receipt, flags and approval chain.
3. Approve, Return and Reject with reasons.
4. Notifications to the claimant.
5. Audit trail of each decision.

Later: bulk approve, keyboard shortcuts, delegation, mobile approve-on-the-go, policy auto-approval, and AI flagging. If you add automated flagging, label it, show the reason, and let managers correct it.

## Must-be items to flag
Roles and a segregation-of-duties rule, an audit trail, an export that respects filters, all states designed, URLs for views and records, WCAG 2.2 AA with a full keyboard path, and time zones and currency formats. Treat these as scope for v1, not extras.

## Success measures
- Task success and median time per claim, compared with the current process.
- Percentage of claims decided within SLA.
- Error rate (approved claims later reversed or flagged).
- Share of approvals made from the list without opening the detail.
- Satisfaction per task (SEQ), measured after the first release.

## Risks and open questions
1. **Rubber-stamping.** A fast approve flow raises the risk of approving bad claims, so flags need to be clear and not noisy.
2. **Notification fatigue.** Decide between an immediate alert, a daily digest and an SLA reminder.
3. **Where the claim data comes from.** Receipt OCR quality sets how much the detail pane can be trusted.
4. **Multi-level approval chains.** These change what "my queue" means.

## Questions that change the design
1. What's the real queue size per manager per day (median and worst case), and is the work done in batches or throughout the day?
2. Are there approval limits, multi-step chains or delegation today, and who sets the rules?
3. Where do managers approve now (email, ERP, spreadsheets, chat), and do they need mobile approval?

## Assumptions I made
Desktop-first at 1280px or wider, a single company and currency pair per tenant, an existing design system to follow, and approvals in the same tool as claim submission.

## Next step
Answer the three questions (or tell me to keep the assumptions), and I'd suggest a **Grill** pass on this brief to stress-test it before design. After that I can build a clickable prototype of the worklist and detail pane with every state, as an Artifact if you want a link to share.
