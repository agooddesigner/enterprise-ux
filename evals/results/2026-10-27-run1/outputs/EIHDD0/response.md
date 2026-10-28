# Approvals inbox for expense claims: planning draft

**Job, user, frequency (my assumption, so please correct it):** A finance manager clears a queue of expense claims, usually daily and sometimes several times a day. Most claims are routine and should take seconds. The rest need a closer look and sometimes a question back to the claimant. Money is at stake, so the screen has to be fast without making mistakes easy. The design should favour speed and density over guidance.

## 1. Questions to settle first

These change the design more than any layout choice.

1. **Claim shape:** Is a claim one receipt or a report with many line items? Can a manager approve some lines and reject others? That decides whether the unit of approval is the claim or the line.
2. **Volume per manager:** Around 10 pending, 100, or 1,000+? Under about 30 you can use a simple list. Above that you need filters, sort and bulk approve.
3. **Policy and flags:** Does the system already detect over-limit amounts, missing receipts, duplicates or out-of-policy categories? If not, the inbox can only show raw data.
4. **Approval chain:** Is the manager the only approver, or one step among several (manager, then finance, then payment)? What happens after they approve?
5. **Delegation:** Do managers have delegates or out-of-office routing? Can they reassign a claim?
6. **Approval limits:** Are there thresholds above which a claim must escalate?
7. **Platform:** Is this desktop only, or do managers also approve from their phones?

## 2. Proposed structure

**Layout: list on the left, detail panel on the right.** The manager can work through claims without leaving the queue. The open claim stays in the URL, so it can be shared.

- **Tabs or segments:** Needs my action | Waiting on claimant | Decided. Show counts. The default is "Needs my action", sorted oldest first or by the pay-run deadline.
- **List row (about 44px, compact option):** claimant, amount (right-aligned, with currency), category, date submitted, age, and flag chips. Flags are icon plus label, never colour alone: "Missing receipt", "Over limit", "Possible duplicate".
- **Detail panel:**
  - Receipt image or PDF, large, with zoom.
  - Line items.
  - Policy checks, with each failure explained.
  - The claimant's history and comments.
  - An audit trail.
- **Actions in the panel:** Approve (the one primary action), Reject (needs a reason), Request changes (a note back to the claimant). Reassign goes in the overflow menu.
- **Keyboard:** `J`/`K` to move through the list, `A` to approve, `R` to reject, `Esc` to close the panel. After a decision the next claim opens automatically. This is the biggest speed gain.

## 3. Safety decisions

- **Approve** should be one click with an undo toast of about 10 seconds, not a confirmation dialog. It is the common action and is reversible until payment.
- **Reject and Request changes** require a reason. This is the claimant's feedback, and it goes into the audit trail.
- **Bulk approve:**
  - Select several rows and the action bar reads "Approve 12 claims · £3,420.00". It names the count and the total.
  - Bulk approve should skip or block flagged claims by default. Otherwise the feature becomes a way to rubber-stamp problems.
  - Bulk reject should probably not exist. Rejection needs a reason per claim.
- **Money that has already moved:** Once a claim is paid, the Approve and Reject buttons are replaced by a read-only state that says so.
- **Conflicts:** If someone else decides the claim first, show "Already approved by Priya N. at 14:02" instead of a generic error.

## 4. States to design

| State | What the user sees | Action available |
|---|---|---|
| First use / empty | "No claims waiting for you" and the date of the last one cleared | Link to Decided |
| Inbox zero | Positive confirmation, not a blank panel | View decided |
| No filter results | "No claims match these filters" | Clear filters |
| Loading | Skeleton rows; the previous list stays visible on refresh | None |
| List fails to load | Message with reference ID | Retry |
| Receipt fails to load | Inline error in the panel; the rest of the claim still works | Retry or download |
| No permission | Explains why and who to ask | Request access |
| Read-only (delegate, or claim already decided) | Buttons disabled with a tooltip giving the reason | None |
| Overflow | Long names and merchants are truncated with the full text on hover; a claim with 40 line items scrolls inside the panel | None |
| Stale data | "New claims arrived" banner instead of the list reshuffling under the cursor | Click to refresh |

## 5. Filters and state in the URL

Filters are claimant, category, amount range, submitted date, flag type and department. Add saved views such as "Over £500" and "Missing receipts". Sort, filters, tab and the open claim all live in the URL.

## 6. Out of scope for a first version

Analytics dashboards, mobile-native approval, auto-approval rules and delegation management. The auto-approval rules are the one most likely to matter later. They should be a separate project, not part of the first version.

## 7. Suggested next steps

1. You answer the questions in section 1, especially 1, 2 and 3.
2. I write a short spec: states table, field list with realistic data, and keyboard map.
3. We build a clickable prototype with seeded data (long names, missing receipts, 80+ claims) so every state can be reached. I can build this as a page you can share.

Which would help most next: answers to the questions, or a prototype built on the assumptions above?

**Audit summary:** This is a plan with no screens yet, so I checked it against the planning rules only. It has a named job and frequency, a state map for every view, the destructive actions covered (undo for approve, reasons for reject, counts in bulk actions), permissions designed, and state kept in the URL. Nothing is built, so I haven't checked visual density, alignment or keyboard order.
