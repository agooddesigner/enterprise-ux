# AI Expense → GL Code Categorisation

## 1. Goal and principles
Cut manual coding time and month-end cleanup without ever letting the AI quietly misstate the books.

- **Auto-post only when precision is very high.** Everything else becomes a suggestion.
- **Every decision is explainable, auditable and reversible.**
- **Learn per customer.** Each company's chart of accounts (COA) and habits differ.
- **Cheap and deterministic first, LLM last.**

## 2. User experience

**Where it appears**
- **Expense/transaction list:** a GL code chip on each row, with a state of *Auto-coded*, *Suggested* or *Needs review*.
- **Review queue:** the main working surface. It is sorted by amount × uncertainty, with bulk approve for groups of similar items (for example, all "Uber" rows).
- **Detail drawer:** shows the suggested code, the top 2–3 alternatives, a one-line reason ("Matches 14 past Zoom charges → 6240 Software Subscriptions") and the receipt. Actions: Accept, Change, "Always do this for this vendor".
- **Settings (admin):** auto-post threshold, accounts excluded from automation, and a rules view where learned rules can be edited or disabled.

**Trust-building rollout per customer**
1. **Shadow mode** (2–4 weeks): the AI suggests and nothing is posted. The customer sees their own accuracy score.
2. **Suggest mode:** one-click accept.
3. **Auto-post mode:** opt-in, per account group, once measured precision clears the bar.

## 3. How it works

```
Transaction + receipt OCR + metadata
        │
 1. Normalise (merchant cleanup, currency, line items)
        │
 2. Deterministic layer ── customer rules, vendor→GL history ──► hit? done (high confidence)
        │ miss
 3. Candidate retrieval (embedding search over this tenant's COA descriptions + past coded transactions)
        │
 4. LLM classifier (structured output, restricted to retrieved valid codes)
        │
 5. Confidence calibration + policy checks
        │
 6. Route: auto-post / suggest / human review
        │
 7. Feedback capture → rules + few-shot memory
```

**Inputs:** merchant, description, amount, MCC code, receipt line items, employee, department/cost centre, entity, date, and the tenant's COA with account descriptions.

**Output (strict JSON):** `gl_code`, `tax_code`, `cost_center`, `confidence`, `reason`, `alternatives[]`. The code must exist in the tenant's active COA. Anything else is rejected and re-asked.

**Model approach**
- Step 2 should handle 60–80% of volume at near-zero cost, since most spend is repeat vendors.
- The LLM uses a small, fast model with retrieved examples as few-shot context. A larger model is a fallback for low-confidence cases only.
- **Calibrated confidence:** don't trust the model's self-reported score. Combine rule hit, agreement between retrieval and the LLM, and historical accuracy for that account. Calibrate it on held-out corrections.
- **Split transactions:** if line items map to different accounts (a hotel bill with room, meals and parking), propose a split.

## 4. Guardrails
- **Never auto-post** for: capex or fixed-asset thresholds, intercompany, payroll, tax, equity, related-party, or amounts above a customer-set limit.
- **Hard blocks:** locked periods, inactive accounts, and entities the user can't access.
- **Prompt-injection defence:** receipt and description text is treated as untrusted data and never as instructions. The output is schema-validated.
- **Tenant isolation:** no customer data is shared across tenants. Cross-customer learning is opt-in and anonymised, or limited to generic merchant→category priors.
- **Audit log:** every decision records model version, inputs hash, rule or example used, confidence, who accepted or overrode it, and when.
- **Undo:** bulk recode with one click, as long as the period is open.

## 5. Feedback loop
- An override is stored as a labelled example.
- The same correction made 2–3 times proposes a rule: "Always code *WeWork* to 6310 Rent?" The admin approves it.
- A COA change (new or retired accounts) triggers re-embedding and flags affected rules.
- Weekly drift check: if accuracy for an account drops, lower its automation level automatically.

## 6. Metrics

| Metric | Target |
|---|---|
| **Auto-post precision** (not overridden or reversed) | ≥ 99% |
| **Suggestion acceptance rate** | ≥ 85% |
| **Automation coverage** (% of transactions needing no human touch) | 60–75% by month 3 |
| **Time to close** / manual coding minutes per 100 transactions | −50% |
| **Reversal rate after period close** | Near zero (alert if it rises) |
| **Cost per transaction** | Tracked by layer |

**Offline evaluation:** build a golden set from each customer's last 6–12 months of coded history. Test the model on it before enabling it for that customer, and report accuracy by account.

## 7. Phasing
1. **MVP:** rules plus history lookup, LLM suggestions, review queue and shadow mode.
2. **v2:** auto-post with thresholds, learned-rule proposals, and split transactions from receipts.
3. **v3:** multi-entity and tax-code coding, anomaly flags (duplicates, out-of-policy spend), and a natural-language "why was this coded here?" Q&A.

## 8. Key risks

| Risk | Mitigation |
|---|---|
| Wrong auto-posts erode trust | Shadow mode, conservative thresholds, per-account opt-in, easy undo |
| Poorly described COAs | Onboarding step that suggests clearer account descriptions |
| Auditor or compliance pushback | Full audit trail, human-approved rules, model-version pinning |
| Cost at scale | Deterministic layer first, cache by merchant, small model by default |
| Model updates changing behaviour | Regression-test against each customer's golden set before rollout |

## Open questions for you
- Which ERPs or ledgers do you sync with (this affects how COA changes arrive)?
- Is the customer base mostly SMB or mid-market? That decides how much to invest in multi-entity and approval workflows.
- Do customers have an auditor-facing requirement, such as SOC 2 evidence, for AI-made entries?

I can turn this into a shareable page, with a flow diagram and review-queue mockup, or a PRD with user stories. Do you want either?
