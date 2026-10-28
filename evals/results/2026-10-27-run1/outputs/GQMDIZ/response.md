# Design brief: AI GL-code categorisation

I had no research or customer data to work from, so the assumptions are listed at the end. The brief needs checking against real data before design starts.

## Outcome and approach

**Outcome:** Most expenses reach the ledger with the right GL code without anyone touching them. Reviewers spend their time only on the ones that need judgement, and month-end close gets faster. A wrong code in the ledger costs more than a slow review, so accuracy comes before automation rate.

**Why AI:** Vendor and description text is messy, so rules alone won't cover it. The feature should still be a hybrid, in this order:
1. **Deterministic rules and vendor memory.** Examples are "Vendor X is always 6120" and rules the customer defined.
2. **A model for everything else.** It sees the chart of accounts, the vendor, the description, the amount, the cost centre, receipt text, and past corrections by this tenant.

A manual path always exists. Users can pick a code themselves, and an admin can turn the feature off.

## Audiences and jobs

| Role | Job story | Frequency / stakes |
|---|---|---|
| **AP clerk / bookkeeper** (the main user) | When a batch of expenses arrives, I want to confirm or fix codes quickly, so I can post them without hunting for the right account. | 50 to 500 per day. Needs speed, so keyboard and bulk review. Medium stakes. |
| **Employee submitter** | When I submit an expense, I don't want to pick a GL code. | Occasional. Low stakes. |
| **Controller / finance manager** | When I close the month, I want to know that coding is accurate and auditable, so I can sign off. | Monthly. High stakes. Needs guidance and reports. |
| **Finance admin** | I want to set which accounts the AI may use and how much autonomy it has. | Rare. High stakes. |
| **Auditor** (read-only) | I want to see why each code was assigned and who approved it. | Periodic. |

## How it works

### Autonomy is set per tenant and per rule

It follows the human-in-the-loop ladder, and each tenant earns its way up.

| Level | Behaviour | Default |
|---|---|---|
| 1. Suggest | The AI pre-fills the code, and a human confirms every line. | **Day 1 default** |
| 2. Auto-code high confidence | High-confidence lines are coded and flagged "AI-coded". Everything else goes to the review queue. | Admin opt-in after a trial period |
| 3. Auto-post | Lines post to the ledger without review. | Only for narrow scopes, such as "recurring vendor, same code 12 times in a row, under $500". Each scope needs admin approval. |

Never auto-post anything in a closed period, above an amount cap, or to restricted accounts. Admins configure those exclusions.

### Confidence is categorical, and each level has an action

- **High** is auto-accepted at Level 2 and can be bulk-approved.
- **Medium** goes in the review queue with the top suggestion pre-selected.
- **Low** shows up to 3 ranked alternatives and no pre-selection, so a tired reviewer can't approve by default.
- Don't show raw percentages. The admin calibration view can show them.
- **Calibrate the thresholds on tenant data.** "High" should mean at least 98% accurate on that tenant's backtest, not an arbitrary model score.

## Key screens

### 1. Review queue (a worklist, and where most of the time is spent)

- A dense table with these columns: date, vendor, description, amount, **suggested GL code and name**, confidence, reason, and status.
- Default sort is by confidence ascending, so uncertain lines come first. Saved views include "Needs review", "AI-coded, not yet reviewed", "Corrected by me", and "Auto-posted".
- Filter state lives in the URL, and the table can be exported.
- **Inline accept and edit.** Enter or ✓ accepts. Typing opens a combobox of GL codes searchable by number or name, with the AI alternatives at the top.
- **Bulk actions.** "Accept 84 High-confidence lines" shows a count and a total amount and can be undone. Also bulk recode, and "apply to all from this vendor".
- **Pagination or virtualisation.** Plan for 50,000 rows.
- **Keyboard path:** J/K to move, Enter to accept, E to edit, and a shortcut to open the reason popover.

### 2. "Why this code?" popover

Each row gets an AI label, which is text plus an icon, never colour alone.
- **Evidence:** "Vendor 'Delta Air Lines' was coded 6410 Travel on 23 of 24 past invoices."
- **Matched rule or memory:** a link to the rule, if one applied.
- **Alternatives** with their own reasons.
- **Actions:** Accept, Change, "Always code this vendor to…", and Report wrong.
- If the user edits the code, the AI styling goes away and a "Revert to AI suggestion" action appears.

### 3. Correction capture

When a user changes a code, a one-tap follow-up asks what happened. The options are "Wrong suggestion", "This vendor is different here", and "One-off". The answers separate model error from preference and tell the system whether to learn a vendor rule or ignore the change. Corrections feed tenant-scoped learning, and the UI says so. It must not claim to retrain the model if it only adds a rule.

### 4. Admin settings (the Finance Admin role only)

- **Enable or disable** per entity.
- **Autonomy level** per scope, with amount caps and excluded accounts or vendors.
- **Eligible accounts:** which GL codes the AI may suggest. Inactive and restricted accounts are never offered.
- **Data use:** what is sent to the model, retention, and whether tenant data is used for training (default off). Link to the data processing terms.
- **Rules and vendor memory:** view, edit and delete what the system has learned.
- **Roll-out preview:** run the AI on the last 90 days of already-coded history and show the accuracy before enabling. This is the main trust builder.

### 5. Performance dashboard (for controllers)

Show these trends, with a small line chart for each and the numbers beside it:
- Acceptance rate and edit rate.
- Override rate by account and by vendor, to surface systematic errors.
- Auto-coded share and unintended-posting count.
- A sample audit: "Review 25 random auto-coded lines" for spot checks.

### 6. Submitter experience

Employees see a suggested category in plain language, such as "Travel", rather than a GL number. They can change it. Finance still sees the GL mapping.

## States to design

Each view needs all of these, not just the happy path.
- **First use:** an empty queue explains what the AI does, what it can't do, and its measured accuracy on the customer's history.
- **Model unavailable or timed out:** fall back to rules and vendor memory, and show a banner saying "AI suggestions unavailable, manual coding still works". Don't block posting.
- **No suggestion:** the model has nothing useful, so show an empty field with the reason.
- **Chart of accounts changed:** suggestions that point to a now-inactive code get flagged as stale and re-evaluated.
- **No permission:** viewers see codes and reasons but have no edit controls. Controls an editor never gets are hidden. Controls that are blocked for now are disabled with the reason and who can help.
- **Closed period:** disabled with an explanation.
- **Loading:** show the row first and fill in the suggestion as it arrives. Batches over about 10 seconds get progress and can run in the background.
- **Partial failure:** "412 of 450 coded, 38 failed. Retry failed."

## Permissions

| Action | Submitter | AP clerk | Controller | Finance admin | Auditor |
|---|---|---|---|---|---|
| See suggestion and reason | Category only | ✓ | ✓ | ✓ | ✓ |
| Accept or change a code | – | ✓ | ✓ | ✓ | – |
| Bulk accept | – | ✓ up to a cap | ✓ | ✓ | – |
| Create vendor rules | – | Propose | ✓ | ✓ | – |
| Change autonomy level | – | – | – | ✓ | – |
| Edit eligible accounts | – | – | – | ✓ | – |

Raising the autonomy level is the highest-risk change, so it needs a second approver.

## Audit and compliance

- Every line records the assigned code, its source (rule, vendor memory, or model), the model version, the confidence band, who accepted or changed it, and when. Auto-posted lines record actor = AI and the approving policy.
- Keep this history immutable and exportable, since auditors will ask for it.
- Disclose AI use wherever it appears. Verify with legal what the EU AI Act transparency rules require for this surface.
- Don't send PII or card data to the model unless it's needed. Mask what isn't.
- Keep an undo path after posting where the accounting system allows reversal. If it doesn't, say so before auto-post can be enabled.

## Success metrics

| Metric | Why |
|---|---|
| **Accuracy** (post-review agreement with the final code) | Core quality. Track by band, because High must stay at least 98%. |
| **Acceptance rate and median edit distance** | Whether suggestions save work. |
| **Time per line and lines per hour** | The task-efficiency outcome. |
| **Intervention rate and unintended posts per 1,000** | Safety. |
| **Overrides after posting** | Catches bad auto-posts. |
| **Close-cycle days** | The business outcome. |
| **Admin escalation to higher autonomy** | A trust signal. |

## v1 release slice

1. **Walking skeleton:** suggestions with a reason, a review queue, accept and edit, correction capture, an audit trail, and admin on/off.
2. **Next:** vendor memory and rules, bulk accept, the history backtest, and the controller dashboard.
3. **Later:** auto-post scopes, receipt-based coding, multi-entity charts of accounts, and ERP write-back extras.

## Risks and open questions

1. **Automation bias.** Reviewers rubber-stamp pre-filled fields. Mitigations are no pre-selection on Low confidence, random spot-check prompts, and tracking accept-time per line to catch blind approval.
2. **Each tenant's chart of accounts is different**, and many are messy. Quality depends on the mapping. Decide whether the model uses fine-tuning, retrieval over the account descriptions, or both.
3. **Cold start.** A new tenant has no history. Offer a bulk import of past coded transactions, and consider a prior based on industry.
4. **Which ERP is the system of record,** and does it support write-back and reversal? This decides what undo can be.
5. **Who is liable for a mis-code,** and what the contract says about it.
6. **Multi-entity and multi-currency:** whether the same vendor can be coded differently per entity.

## Assumptions

- The product already has an expense list, a chart of accounts, and roles. If its design system has a worklist pattern, I'd reuse that.
- Review is the main workflow, so I've optimised for speed over hand-holding.
- The default accuracy target for High is 98%. Confirm it with finance customers.
- I haven't done any user research. Run it with a few AP clerks and a controller before locking this.

## Next steps

I can do any of these:
- Stress-test this brief with the Grill pass.
- Build clickable mockups of the review queue and the "Why this code?" popover, with all the states.
- Publish this brief as a shareable page for your team.
