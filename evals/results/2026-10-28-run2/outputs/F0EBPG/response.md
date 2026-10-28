# AI GL Code Categorisation: Feature Design

**Job, user, frequency:** An AP clerk or bookkeeper codes 50–300 expenses a day and wants to clear the queue fast. The controller reviews exceptions weekly and owns the audit trail. Optimise for speed and density, and make a wrong code hard to push through unnoticed.

## 1. Product principles
1. **Suggest first, automate once it has earned trust.** The AI never posts to the ledger without either a human accept or a customer-defined auto-approve rule.
2. **Confidence is calibrated and visible.** Three tiers drive the workflow, not a raw percentage.
3. **Every suggestion shows its reasoning** in one line, such as "Matched vendor 'Delta Air Lines' → 6200 Travel, 14 prior coded identically".
4. **Corrections are the training signal.** Fixing a code takes one keystroke and teaches the system.
5. **Deterministic rules beat the model.** Customer rules run first, then history, then the LLM.

## 2. How it works

**Pipeline per expense**
1. **Normalise.** Clean the vendor name, merchant category code (MCC), amount, memo, receipt OCR text, card holder, department and cost centre.
2. **Rules.** Customer-defined rules, such as "vendor = AWS → 6410 Hosting". A match gives confidence 100% and source = Rule.
3. **History.** Nearest neighbours by vendor and description embedding, scoped to this tenant's coded transactions.
4. **LLM classifier.** Gets the tenant's chart of accounts (code, name, description, active flag), the top historical matches as few-shot examples, and the expense. It returns the top 3 codes, each with a confidence and a one-line rationale. It is constrained to codes that exist and are active, and a post-check rejects anything outside the chart.
5. **Policy check.** Flags the expense when the code is restricted by department or role, the amount exceeds a threshold, or the category is sensitive (such as gifts or entertainment). A flag forces review whatever the confidence.
6. **Route by tier** (thresholds set per tenant, backtested before activation):

| Tier | Default | Behaviour |
|---|---|---|
| **High** (≥ 95% and corroborated by history or rule) | Auto-approve is **off** by default | Pre-filled, bulk-acceptable |
| **Medium** (70–94%) | Pre-filled, needs a glance | Reviewed in the queue |
| **Low** (< 70%) or policy-flagged | Left blank, top 3 shown | Must be chosen by a human |

Auto-approval is an opt-in per-tenant setting. Admins first see a backtest on their last 90 days ("Would have auto-coded 71% of expenses; 99.2% would match the final code"). Changes to it are audit-logged.

**Calibration:** Measure confidence against actual acceptance rates per tenant, and show tiers rather than raw model scores. A cold-start tenant with fewer than 200 coded transactions starts with the auto-approve option unavailable and a "Learning" badge.

## 3. Key screens

### A. Review queue (the main surface)
A dense table at 40px rows with a compact option. Columns, with numbers right-aligned in tabular figures:

`☐ | Date | Vendor | Description | Amount (right) | Suggested GL | Confidence | Source | Status`

- **Suggested GL** is an inline combobox showing `6200 · Travel & Lodging`. Typing searches code and name. The top 3 alternatives sit above the full list.
- **Confidence** is a labelled chip (High, Medium or Low) with an icon, never colour alone. Hover shows the one-line rationale.
- **Source** is a chip: Rule, History or AI.
- **Filters:** status, tier, source, vendor, department, amount range, date, "changed by me". Saved views include "Needs review", "Low confidence" and "Policy flagged". All filter, sort and selection state is in the URL.
- **Keyboard:** `J/K` move rows, `A` accepts the suggestion, `E` edits the code, `1/2/3` pick an alternative, `Shift+A` accepts the selection, `/` searches and `?` shows shortcuts. Focus advances to the next row after an action.
- **Bulk bar** (on selecting rows): "Accept 48 suggestions", "Set GL code…", "Create rule from selection…". Bulk accept shows the count and total value ("Accept 48 suggestions ($31,204.50)"), and a confirmation dialog appears only when the batch includes Medium rows. It offers **Undo for 30 seconds** via toast.
- **Row detail side panel** (open with Enter, URL-addressable): receipt preview, extracted fields, full rationale, the matched historical transactions, the alternatives with confidences, the split-line editor, and the audit trail for this expense.

### B. Correction flow
Changing a code opens a small inline prompt, never a modal: *"Apply to future Delta Air Lines expenses?"* with the options **Just this one**, **Always (create rule)** and **Ask me later**. Choosing Always opens a pre-filled rule for review, with a preview of how many existing uncoded items it would affect.

### C. Rules & AI settings (admin only)
- Rules table with condition, GL code, hit count, last hit, creator and enabled toggle.
- Thresholds, auto-approve toggle, restricted codes and the backtest report.
- Chart-of-accounts sync status, since the model reads from the live chart.
- **Accuracy dashboard** with first-pass acceptance rate, override rate by GL code and by tier, auto-approved volume, and the codes the AI most often gets wrong. A calibration chart shows whether High really means ≥ 95% accurate.

### D. Splits and multi-line expenses
The AI proposes line-level splits when the receipt has line items, such as a hotel bill with room, meals and tax. Splits must sum to the total, and the editor shows the remainder live.

## 4. States

| View | State | Trigger | User sees | Action available |
|---|---|---|---|---|
| Queue | Empty, first use | No expenses imported | "No expenses yet" with a connect-card/import explanation | Connect source, Import CSV |
| Queue | Empty, all done | Queue cleared | "All 214 expenses coded this period" with accuracy summary | View posted, Change period |
| Queue | No results | Filters match nothing | "No expenses match these filters" | Clear filters |
| Queue | Loading | Initial fetch | Skeleton rows at real row height | None |
| Row | Pending AI | Just imported | Per-row spinner with "Suggesting…", row still editable | Code manually |
| Row | AI failed or timed out | Model error or > 8s | "Couldn't suggest a code (ref ERR-4F21)" and the row falls back to the Low tier | Retry, Code manually |
| Queue | Partial failure | Some rows errored | Banner: "12 of 300 weren't categorised" | Retry failed |
| Row | Code inactive | Suggested code was archived since | Suggestion cleared with "GL 6150 is inactive" | Pick another code |
| Row | Policy flagged | Restricted code or threshold | Flag chip with the reason | Request approval, Choose another code |
| Any | No permission to edit | Viewer role | Controls disabled, tooltip "Only AP Clerks and Admins can change codes" | Request access |
| Any | Locked period | Period closed | Rows read-only with "Period closed 30 Sep by M. Okafor" | Controller can reopen |
| Settings | No permission | Non-admin | Read-only view naming who can edit | Contact admin |
| Bulk | Undo window | After bulk accept | Toast "48 accepted · Undo" for 30s | Undo |
| Bulk | Partial conflict | Another user changed a row | "45 accepted, 3 skipped (changed by another user)" with a link to them | Review skipped |
| Chart | Sync failed | ERP unreachable | Banner with last-synced time | Retry sync |

## 5. Trust, safety and governance
- **Audit trail on every code:** who or what set it, source (Rule, History or AI), model version, confidence, rationale, timestamp with timezone, and every change after that.
- **Data isolation:** Suggestions and few-shot examples come from the tenant's own data only. No cross-tenant training without explicit contractual opt-in.
- **PII minimisation:** Strip card numbers and employee identifiers from prompts, and send only the fields the classifier needs.
- **Prompt-injection defence:** Receipt text and memos are untrusted. They go in a delimited data block, output is schema-validated, and the code must exist in the chart.
- **Period locks and approvals:** The AI can't touch closed periods, and posting follows the existing approval workflow.
- **Drift monitoring:** Alert admins when the override rate for a code rises more than 10 points over four weeks, or when the chart of accounts changes materially, and suggest re-running the backtest.
- **Explainability on request:** "Why this code?" always works, even for Rule matches.

## 6. Metrics
- **Primary:** Touchless rate (accepted without edit), median time to code per expense, and accuracy at each tier against the final posted code.
- **Guardrails:** Auto-approved override rate (target < 1%), post-close reclassification journals, and Low-tier volume.
- **Adoption:** Share of tenants with auto-approve on, and rules created per tenant.

## 7. Rollout
1. **Shadow mode:** Run silently for 2–4 weeks and show the admin a backtest.
2. **Suggest-only** for all users, with the High tier bulk-acceptable.
3. **Opt-in auto-approve** for High-tier rows meeting the tenant's own accuracy bar, starting with low-value expenses (for example under $500) and widening from there.
4. **Later:** Split proposals, policy-violation detection, and anomaly flags (duplicate or unusual vendor-code pairs).

## 8. Open questions
- Which ERPs does the chart sync from, and is it real-time or batch?
- Are cost centres and departments separate dimensions from the GL code, or part of the code?
- Is there a regulatory need for human sign-off above a given value, regardless of confidence?
- Is your target tenant size closer to 500 or 500,000 expenses a month? That decides batch vs. streaming inference and the queue's virtualisation.

## Audit summary
- **States:** Empty, loading, error, partial-failure, no-permission, read-only and locked-period states are specified for the queue, row and settings.
- **Safety:** Bulk accept names the count and value, has a 30s undo, and never auto-posts unless the admin opts in after a backtest. Every change is audit-logged.
- **Table conventions:** Numbers are right-aligned, status chips pair colour with a label, and filters, sort and the open record live in the URL. Keyboard shortcuts cover the frequent actions.
- **Gaps:** I haven't checked mobile, i18n or multi-currency display. The specified thresholds are starting defaults and need calibration on real data.

If you want this as a shareable page with a mockup of the queue, I can build one.
