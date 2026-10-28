# Approvals inbox plan for finance managers

I've assumed you want the design problem framed before any screens exist. The plan below makes some assumptions, and the questions at the end could change it.

## 1. Who and what
- **User:** a finance manager clearing a queue of expense claims, probably in batches between other work, on desktop mostly and on mobile for quick approvals.
- **Core job:** decide approve, reject, or ask for more info on each claim, quickly and with confidence.
- **Success measures:** time per decision, queue age (oldest pending claim), and the rate of wrongly approved or later-reversed claims.

## 2. The decision the manager makes
Most claims should be easy. The inbox should make the easy ones fast and the odd ones obvious. For each claim the manager needs, at a glance:
- Who submitted it, the amount, the category, and the date
- Whether the receipt is attached and readable
- Whether it complies with policy (limits, missing receipt, duplicate, weekend or out-of-policy spend)
- Context: the submitter's history, the budget remaining, and the claim's age against an SLA

## 3. Core structure
**Layout:** a list and detail split view.
- **Left, the list:** a row shows submitter, amount, category, age, and flag chips (policy, duplicate, missing receipt).
- **Right, the detail:** the receipt image, line items, policy checks, comments, and the action bar.

**Actions:** Approve, Reject (reason required), Request info (message to submitter), and Reassign or Delegate.

**Bulk actions:** select multiple claims and approve them together. Offer this only for claims with no flags, so the manager can't bulk-approve an exception by accident.

**Views:**
- Needs my action (default)
- Flagged
- Waiting on submitter
- Decided (history and audit)

**Sort and filter:** oldest first by default, then amount, submitter, department, category, and flag type.

## 4. Key design decisions
1. **Auto-surface risk, don't hide it.** Put the flags in the list row so the manager never has to open a claim to find the problem.
2. **Keyboard-first on desktop.** Use J/K to move, A to approve, R to reject, and auto-advance to the next claim. This is the biggest speed gain for people who clear dozens of claims at a time.
3. **Reasoned rejections.** Require a reason from a preset list plus optional free text, so submitters get clear feedback and finance can analyse patterns.
4. **Undo.** Give a short undo window after approval, since mistakes at speed are inevitable.
5. **Audit trail.** Record every decision with who, when, and why. Finance will need this.
6. **Delegation and out of office.** Managers go on leave, so decide early how claims reroute.

## 5. States to design
- Empty queue ("all caught up")
- Loading and error states
- Receipt missing or unreadable
- A claim someone else already decided (a concurrency conflict)
- Policy-blocked claims that can't be approved without an override and a justification

## 6. Notifications
Keep these light: a daily digest, plus an immediate alert only for high-value or SLA-breaching claims. Avoid one email per claim.

## 7. Suggested sequence
1. **Research:** shadow 3–5 finance managers and sample real claims to learn what actually slows decisions.
2. **Rules:** write down the policy and flag rules, since the UI depends on what the system can detect.
3. **Wireframes:** the split view, the bulk flow, and the reject and request-info flows.
4. **Prototype and test:** time decisions against the current process.
5. **MVP:** list, detail, approve, reject, and request info. Defer delegation, bulk approval, and analytics to a later release.

## Questions that would change the plan
- Is this a new product or part of an existing finance or ERP tool, and do we have a design system to follow?
- How many claims does a manager handle per week, and how many arrive flagged?
- Are there multi-level approvals (manager, then finance, then CFO), or a single approver?
- Does policy checking exist today, or does the inbox need to build it?
- Is mobile a priority, or is desktop enough for the first release?

If you answer even a few of these, I can turn this into a one-page brief, a list of user stories, or low-fidelity wireframes. I can publish any of those as a shareable page if you'd like.
