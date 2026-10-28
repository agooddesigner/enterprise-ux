# Approvals inbox for expense claims: a starting plan

## 1. Who and what
- **User:** a finance manager who clears a queue of claims in batches, often between meetings. Volume is high and most claims are routine.
- **Core job:** decide approve, reject, or ask a question on each claim, quickly and with confidence, and spend the extra time only on risky claims.
- **Success measures:** time per decision, queue age (oldest pending claim), and the share of approved claims that audit later flags.

## 2. Core design principle
Triage first, then review. The inbox shouldn't make every claim cost the same effort. Sort and flag so that clean claims are one-click and unusual ones get attention.

## 3. Structure (a list/detail split)
**Left, the queue**
- Rows show the claimant, amount and currency, category, submitted date, and age. A policy-status chip reads Clear, Needs review, or Violation.
- Tabs or filters: Needs my action, Waiting on employee, Decided, and Delegated or Escalated.
- Sort options: oldest first (the default), amount, and risk.
- Bulk select with approve for clean claims only.

**Right, the claim detail**
- A summary header with who, how much, what for, and which policy rules were checked.
- Line items with receipt thumbnails side by side. Flags such as duplicates, over-limit amounts, missing receipts, weekend spend, and FX mismatch sit next to the line they apply to.
- Context: the claimant's recent history, the budget remaining for the cost centre, and the approval chain so far.
- A sticky action bar with Approve, Reject (reason required), Request info, and Reassign.

## 4. Key flows to design
1. **Quick approve:** keyboard-driven (J/K to move, A to approve), with undo for a few seconds.
2. **Partial approval:** approve some line items and reject others.
3. **Request info:** a comment thread with the claimant, and the claim moves to "Waiting on employee" until they reply.
4. **Delegation and out-of-office:** reassign claims, with a visible SLA clock.
5. **Escalation:** claims over your authority limit route upward.

## 5. States and edge cases
- Empty queue ("Inbox zero"), a loading state, and an offline or failed-save state.
- Claims another approver has already actioned, or ones the claimant withdrew while you were viewing them.
- Multi-currency claims, and receipts that are unreadable or missing.
- Accessibility: full keyboard operation, and a status that doesn't rely on colour alone.

## 6. Open questions that change the design
1. **Volume:** roughly how many claims per manager per week? Below about 20 you can skip bulk actions. At 200 or more they're essential.
2. **Policy engine:** does something already auto-check claims against policy? If not, the flags in section 3 mean extra backend work.
3. **Where do they work today?** Is it email, an ERP, or a spreadsheet? That tells us what to match and what to replace.
4. **Platform:** is it desktop-only, or do managers need to approve from their phones? I'd recommend a mobile-friendly single-column version (queue, then detail) even if desktop comes first.
5. **Authority rules:** are there approval limits, multi-level chains, or separation-of-duties rules?
6. **Audit needs:** do you need an immutable decision log, and must rejections carry a reason?

## 7. Suggested next steps
1. Answer the open questions above, especially 1, 2 and 4. If you can, interview 3–5 finance managers.
2. Write the problem statement and success metrics.
3. Sketch low-fidelity wireframes of the list/detail layout and the quick-approve flow.
4. Test the flagging logic with real, anonymised claims before polishing visuals.

I can turn this into a one-page brief or a clickable wireframe prototype if you'd like either.
