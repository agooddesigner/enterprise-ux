# Approvals inbox: plan for finance managers

**Job, user, frequency (working assumption):** A finance manager clears a queue of expense claims, deciding approve, reject, or ask for more info. They do it daily, often 20–60 claims in a sitting, usually between other work. This is a high-frequency triage screen, so I'd optimise for speed, density, and not approving the wrong thing. I'd also treat the audit trail as part of the screen.

## 1. Core design decisions

| Decision | Recommendation | Why |
|---|---|---|
| Layout | Table on the left, **side panel (drawer)** for the open claim, with prev/next. | Triage means keeping list context. The panel is URL-addressable (`/approvals?open=EXP-20418`). |
| Container | Dense table, 40px rows, compact toggle at 32px. Don't use cards. | Managers compare claims across the same attributes. |
| Default view | **"Needs my approval"**, sorted oldest-submitted first (or by SLA due date). | The default should be the job, not "All". |
| Primary action | **Approve** in the panel, with **Reject** and **Request changes** beside it. | One primary action per view. |
| Reject | Requires a reason, which is sent to the claimant. | Reject is high-friction by design and Approve isn't. |
| Keyboard | `J/K` move, `Enter` open, `A` approve, `R` reject, `Esc` close, `?` shortcuts. | Made for people doing 40 of these a day. |

## 2. Table columns

Left to right, ordered by decision value:

1. Claim ID, which is the link and the sticky column (`EXP-20418`)
2. Claimant, with team underneath
3. Merchant / description (truncates, full text on hover)
4. Category (Travel, Meals, Software…)
5. **Amount (USD)**, right-aligned with tabular figures. Show the original currency in the panel or on hover when the claim isn't in USD.
6. Submitted, relative with the absolute date on hover
7. **Flags**: policy breach, missing receipt, duplicate suspected, over limit
8. Age / SLA, such as "5 days · due in 2d"

Status is colour + label, and the vocabulary stays small: *Pending · Changes requested · Approved · Rejected · Escalated*.

## 3. Side panel (the decision surface)

Everything a manager needs sits on one screen, so they don't need to open a second page:

- **Header:** claim ID, status, amount, claimant, Approve / Reject / Request changes
- **Receipt preview** (large, zoomable). This is the most important thing in the panel.
- **Line items** with category and per-line amount
- **Policy check:** a list of what passed and what failed, in plain words. Example: "Meal over $75 per-person limit ($112.40)".
- **Context:** the claimant's spend this month against budget, plus similar or duplicate claims
- **Activity:** comments, previous approvers, and absolute timestamps with timezone
- **Comment box** for notes to the claimant

## 4. Filters and saved views

Segmented tabs: **Needs my approval · Delegated to me · Waiting on others · Decided**.

Filter bar with chips for Claimant, Team, Category, Amount range, Submitted (presets), and Flag. Search by claim ID, claimant, or merchant, and a pasted claim ID jumps straight to the claim. Saved views are personal vs. shared ("Flagged > $1,000"). Everything lives in the URL.

## 5. Bulk approval

This is where the risk is, so I'd constrain it:

- Select rows, then a toolbar: "**12 selected** · Approve · Reject · Clear".
- **Flagged claims are excluded from bulk approve.** The dialog says "Approve 9 claims ($1,840.20)? 3 flagged claims will be skipped. Review them".
- The confirmation names the **count and the total amount**.
- The result is a summary ("Approved 9 · Skipped 3"), plus **Undo for 10 seconds**. Payment shouldn't start until the undo window closes.
- "Select all matching" is an explicit second step and **doesn't apply to approve**. Approving unseen claims at scale is the failure mode to design out.

## 6. State matrix

| State | Trigger | What the user sees | Action |
|---|---|---|---|
| Ideal | Claims loaded | Table + count ("23 need your approval") | Open, approve, reject |
| First-use empty | New manager or no approvers set up | "No claims routed to you yet. Claims appear when your team submits them." Link to approval rules. | View rules |
| Cleared | Queue finished | "All caught up. Next claim is due Fri." | Switch to Waiting on others |
| No results | Filters hide everything | "No claims match Category: Travel, Amount > $5,000" | Clear filters |
| Initial loading | First fetch | Skeleton rows matching the columns | — |
| Refreshing | Filter change or new claim arrives | Old rows dimmed with a progress bar. New claims show a "3 new claims · Refresh" chip instead of reshuffling rows under the cursor. | Refresh |
| Receipt failed | Image fetch error | Inline error in the panel only, with retry. The decision buttons still work, with a warning. | Retry |
| Partial error | Policy check or budget widget fails | Error in that section only | Retry |
| Full error | Query fails | "Couldn't load your approvals. Your decisions so far are saved." Retry and reference ID. | Retry |
| Action failed | Approve call fails | Persistent toast with Retry. The row rolls back. | Retry |
| Concurrent change | Another approver acted first | "Priya Sharma approved this 2 min ago", and the row updates | Next claim |
| No permission | Role can't approve | Controls disabled with "You can view but not approve. Ask Dana Whitlock (Finance Director)." | Request access |
| Over my limit | Amount above the manager's authority | Approve becomes **Escalate to Finance Director**, with the reason shown | Escalate |
| Read-only | Already decided | Values as text, decision and timestamp shown | Reopen (if allowed) |
| Overflow | Long merchant name, 40 line items, non-USD, null receipt | Truncate with tooltip, "—" for blanks, receipt shows "Missing" as a flag | — |

## 7. Edge cases to decide early

- **Delegation and out-of-office:** who sees claims when a manager is away, and is it shown clearly on both sides?
- **Self-approval and conflicts:** a manager's own claims never route to them.
- **Multi-level approval:** show where this claim sits in the chain ("Step 2 of 3").
- **Currency:** show original + converted, with the rate date.
- **Mobile:** approving simple, unflagged claims on a phone is realistic. I'd plan a stripped-down mobile view (list → receipt → approve/reject) and keep the full table for desktop.
- **Audit:** every decision logs who, what, when (absolute, with timezone), and the reason. This will matter to your auditors.

## 8. Suggested build order

1. Data model and states table, signed off with a few real finance managers
2. Table + filters + URL state
3. Side panel with receipt and policy checks (the most valuable part)
4. Single approve/reject with undo
5. Bulk approve with its guardrails
6. Delegation, escalation, mobile

## Questions that would change the design

1. How many claims does a manager see per week: 20 or 2,000? That decides whether bulk approval is essential.
2. Is there a policy engine, or do flags need to be built?
3. Single approver, or multi-level chains?
4. Does approval trigger payment immediately? That changes how I'd treat undo.
5. Is there an existing design system or component library?

**Audit note:** I haven't built anything yet, so this is a spec-level check against the enterprise checklist. It covers states, permissions, destructive-action safety, URL state, keyboard, and copy. Accessibility details like contrast and focus order, and tests against 0, 1, and 200+ rows, come once there's a build.

I can turn this into a shareable page for your team, or build a clickable prototype with realistic seeded data (long names, flagged claims, mixed currencies) and all of these states reachable. Which would be more useful?
