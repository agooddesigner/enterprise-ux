# Design brief: AI expense categorisation to GL codes

I've assumed the details below because I haven't seen your product. Correct any that are wrong and the design will shift.

## 1. Outcome and the AI question

**Outcome:** Most expenses reach the ledger with the right GL code without anyone touching them, and the ones that need a human are cheap to review. Target: 70% or more straight-through at under 1% post-approval recoding. The 70% is a starting guess to validate in the pilot.

**Does AI earn its place?** Partly. Most spend comes from repeat vendors, so deterministic rules and vendor history should handle that first. AI is for the long tail: new vendors, ambiguous merchants (Amazon, Uber), line-item context, and receipt text.

**Architecture:** use a cascade, with the model last.
1. Explicit company rules, which always win.
2. Vendor history for this tenant.
3. The model, given the tenant's chart of accounts, past coded transactions, and receipt or memo text.

Every suggestion carries its source (**Rule / History / AI**). This also makes it easy to explain.

## 2. Audiences

| Audience | Cares about |
|---|---|
| **Controller or finance lead (buyer)** | Audit defensibility, close speed, no ledger corruption |
| **Finance admin** | Controlling autonomy, mapping the chart of accounts, rollout |
| **AP clerk / bookkeeper (daily user)** | Clearing the review queue fast |
| **Employee submitter** | Never sees GL codes. At most picks a category, with a "not sure" option. |
| **External accountant / auditor** | Read-only history showing who or what coded each item and why |

## 3. Jobs

1. **When** a batch of transactions or reports lands, **I want** the obvious ones coded automatically, **so I can** spend time only on the doubtful ones. (Daily, 50–500 items, medium criticality)
2. **When** I'm reviewing the queue, **I want** to accept, change or reject a suggestion in one keystroke, **so I can** clear 100 items in minutes. (Daily, power-user pace)
3. **When** month-end close approaches, **I want** to see what is uncoded or low-confidence and why, **so I can** close on time. (Monthly, high criticality)
4. **When** the AI is repeatedly wrong on one vendor, **I want** to fix it once as a rule, **so I can** stop correcting the same thing. (Weekly)
5. **When** an auditor asks why a transaction was coded to 6140, **I want** the decision trail, **so I can** answer without digging. (Quarterly, high criticality)

## 4. Autonomy: set per confidence band and per tenant

This follows the autonomy ladder in the AI-features reference. Posting to a ledger is a financial record, so **default is level 1–2 (suggest and propose), never silent auto-posting.**

| Band | Default behaviour | Admin can raise to |
|---|---|---|
| **High** (rule match, or strong history) | Pre-filled, grouped in "Ready to approve", bulk-approvable | Auto-apply, undoable until the period closes |
| **Medium** | Pre-filled, needs a glance, shows the reason | Keep as is |
| **Low / no fit** | **Shows the top 3 alternatives, nothing pre-selected**, so nobody rubber-stamps a guess | Keep as is |

Use words (High / Medium / Low), each tied to an action, not "87%". Bands are calibrated against the tenant's actual correction data. Check that band names match real accuracy before launch, or users will learn to ignore them.

**Hard guardrails**
- Never code into a closed period, an inactive GL account, or one the submitter's entity or department can't use.
- Anything above an admin-set amount always needs a human, whatever the confidence.
- Splits (one receipt to several GL codes) are proposed, never auto-applied.
- Prompt-injection safety: text in receipts or memos is data, never instruction.

## 5. Key screens

### A. Review queue (the core screen, a worklist)
A dense table, one row per transaction. Columns: Date · Vendor · Description · Amount (right-aligned, currency shown) · **Suggested GL** · Confidence · Source · Status.

- **Default view:** "Needs review", sorted by amount, high to low. Saved views: Ready to approve, Low confidence, Uncoded, Recently auto-coded.
- **Inline edit:** the GL cell is a combobox, searchable by code or name ("6140 Software subscriptions"). Low-confidence rows show the alternatives as radio chips.
- **Keyboard:** ↑↓ move, **Enter** accept, **E** edit, **R** reject (leave uncoded), **A** accept all selected, ? shows shortcuts. Every action also has a visible button.
- **Bulk:** "Approve 212 high-confidence" shows count, total amount and a sample, then runs. It is undoable (toast with Undo) until the period closes.
- **Row detail panel (side drawer, not a modal):** receipt image, extracted fields, and "Why this code?" — e.g. *"Matches rule 'AWS → 6140'"* or *"4 of your last 5 Notion invoices were coded 6140; the memo says 'team plan'."* It also has **"Always code [vendor] to [GL]"** to create a rule, and a thumbs-down with reason chips (Wrong account / Should be split / Policy / Other).
- **AI label:** an icon plus the text "AI suggested" on each AI-sourced cell, opening the explanation popover. When a user edits the value, the AI styling drops and a "Revert to suggestion" link appears. Rule and History sources get their own labels, so AI doesn't take credit for rules.
- **Filter and URL state:** all filters, sort and selection scope live in the URL.
- **Export:** CSV of the filtered view, including source and approver.
- **Manual path:** everything works with the AI switched off. The columns are simply empty.

### B. Rules and mapping (admin)
- Chart-of-accounts sync status (ERP connection, last sync, errors). If the sync is stale, banner: "Chart of accounts last synced 3 days ago. Suggestions may use outdated codes."
- Rules table with a priority order, a "Test against last 90 days" preview showing how many transactions would change, and conflict warnings.
- Per-GL-account setting "Allow AI to suggest this account" (off for sensitive ones, such as intercompany or owner draws).

### C. AI settings (admin)
- Enable or disable per entity.
- Autonomy per band, with a plain-language consequence line: "High-confidence items will post automatically. You can undo until the period closes."
- Amount ceiling, excluded GL accounts and vendors.
- Data use: what is sent to the model (vendor, description, amount, receipt text), what is not (employee names and bank details are stripped), retention, and that tenant data is not used to train shared models. **Confirm this with legal and engineering before shipping the copy.**
- Changing autonomy needs the admin role and is audit-logged.

### D. Close dashboard (small, for the controller)
Counts for uncoded, low-confidence and awaiting-approval items, a trend, and a link to the filtered queue. Four numbers and one chart are enough.

## 6. States to design

| View | States |
|---|---|
| Queue | First-use empty ("Connect your chart of accounts to get suggestions"), all-clear ("Nothing to review — 148 coded automatically"), no filter results, loading skeleton, partial failure (some rows uncategorised, the rest usable), model down (banner, **manual coding still works**), refreshing |
| Row | Pending, suggested, edited, approved, rejected, posted/locked (read-only with reason), failed |
| Batch run | Progress with count, cancel, background run, stall warning. The first backfill of 50k+ items runs async and sends a notification. |
| Permissions | Clerk: review and approve. Viewer/auditor: read-only, controls disabled with the reason. Admin only: autonomy, rules, exclusions. |
| Edge data | Foreign currency, refunds (negative amounts), missing vendor, a 200-character memo, duplicate receipts, an account deactivated after suggestion |

## 7. Permissions

| Action | Submitter | AP clerk | Controller | Admin | Auditor |
|---|---|---|---|---|---|
| See GL suggestions | – | ✓ | ✓ | ✓ | ✓ (read) |
| Accept, edit, reject | – | ✓ | ✓ | ✓ | – |
| Bulk approve | – | ✓ (cap by amount) | ✓ | ✓ | – |
| Recode after posting | – | – | ✓ (reason required) | ✓ | – |
| Create rules | – | propose | ✓ | ✓ | – |
| Change autonomy / AI settings | – | – | – | ✓ | – |

Controls a role can never use are hidden. Controls it might get with a different role are disabled, with "Ask an admin" and a request-access link.

## 8. Audit and trust

Every coding event records: who or what acted (user, rule, or AI model and version), the previous value, the new value, the source, the reason shown, a timestamp, and "on behalf of". Recoding after posting needs a reason. The audit view is filterable and exportable. Model changes are announced in the changelog, and band calibration is rechecked after any model change.

## 9. Learning loop

- A correction updates the tenant's history immediately, so the same vendor is right next time.
- After 3 identical corrections for a vendor, prompt: "Create a rule for [vendor]?" The user confirms. The system never creates rules on its own.
- The thumbs-down reasons feed evaluation only. Say so, and don't promise "the AI will learn from this" when it won't.

## 10. Metrics (CASTLE, with AI additions)

| Metric | What it tells you |
|---|---|
| Straight-through rate (accepted without edit) | Value delivered |
| Acceptance rate by band | Whether High really means high |
| Correction rate after approval, and recoding after posting | Rubber-stamping, or silent errors |
| Median seconds per item reviewed | Whether the queue is fast |
| Time to close (days) | Business outcome |
| Undo rate, with reasons | Trust and error type |
| Unintended postings per 1,000 | Safety, and the number that gates raising autonomy |
| Rule creation rate | Whether the learning loop is used |

**Calibration check:** if High-band items are accepted without a glance more than 95% of the time but 3% are later recoded, reviewers are not actually reviewing. Add friction, such as random spot-checks.

## 11. Non-functional

- WCAG 2.2 AA: native table or grid semantics, and a combobox that works with screen readers. Confidence is conveyed by text plus icon, never colour alone. Targets are 24px or larger.
- Performance: the queue handles 50k rows (virtualised, server-side sort and filter). Feedback within 100 ms. Suggestions are precomputed at ingestion, not generated when the screen opens.
- Localisation: multi-currency formats, locale-aware numbers and dates, and GL code names that may be translated.
- EU AI Act Art. 50: label AI involvement and mark generated content. This is likely low-risk, but have legal confirm it. Verify the current requirements.
- Security: PII minimisation before model calls, tenant isolation, and a SOC 2-friendly audit trail.

## 12. Release slices

1. **Walking skeleton:** ERP chart-of-accounts sync → suggestions on new transactions → review queue with accept, edit and reject → audit trail. Suggest-only, no autonomy.
2. **Rules and learning:** "Always code vendor to GL", rule testing, bulk approve.
3. **Autonomy:** admin-controlled auto-apply for High confidence, with undo, ceilings and exclusions.
4. **Depth:** split suggestions, receipt-text understanding, close dashboard, accountant access.

## 13. Risks and open questions (ranked)

1. **Wrong codes silently posted.** This is the worst case, and the main reason autonomy is off by default. The tradeoff is that it limits the time saved at first.
2. **Chart-of-accounts quality.** Messy or overlapping accounts will cap accuracy whatever the model. Do we need a "chart health check" onboarding step? I'd say yes.
3. **Cold start.** A new tenant has no history, so early suggestions are weaker. Can we import historical coded transactions at onboarding?
4. **Reviewer fatigue and automation bias.** See the calibration check above.
5. **Which ERPs do we need to write back to** (NetSuite, QuickBooks, Xero), and do they allow edits after posting?
6. **What data are customers' security teams willing to send to a model?** This drives the whole architecture.
7. **Do you need dimensions beyond the GL code** (department, class, project)? This brief covers the GL code only.

## 14. Research plan

- Five interviews or observations per role (AP clerk, controller, admin, external accountant). Use internal finance staff if customers are hard to reach, and flag that limitation.
- Run a backtest first: 10k historical transactions per pilot tenant, measuring accuracy by band before anyone sees a UI.
- Moderated test of the queue with 5 AP clerks, timing items per minute.
- Shadow-mode pilot with 3–5 tenants (suggestions shown, nothing auto-applied) for 4–6 weeks, then decide on autonomy.

## Assumptions I made
- Your ERP or accounting system holds the chart of accounts, and we sync it.
- Transactions come from cards, bank feeds and expense reports, with receipts attached to some.
- The product is multi-tenant and multi-entity.
- Sending vendor and description text to a hosted model is acceptable to customers.

## Suggested next steps
I'd run **Grill mode** on this brief before screens are drawn. The riskiest assumptions are autonomy defaults, calibration and data policy. I can also build the review queue as an interactive prototype with all its states, using realistic data (long vendor names, refunds, foreign currency, 1,000+ rows). Tell me which you'd like, and whether to publish it as a shareable page.
