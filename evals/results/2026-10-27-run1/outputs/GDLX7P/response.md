# AI Expense → GL Code Categorisation

## 1. Goal and principles
Turn raw expense lines into correct GL codes with minimal human touch. Accuracy matters less than **knowing when it's unsure**. A confidently wrong posting costs more than a slow one.

- **Auto-post only when confident.** Everything else goes to a review queue.
- **Every suggestion is explainable.** Users see why a code was chosen.
- **Per-tenant by design.** Each company's chart of accounts (CoA) and habits differ, so the model never assumes a universal mapping.
- **Humans stay accountable.** AI proposes and people can override. Every decision is audited.

## 2. How it works

```
Expense in (card feed, receipt OCR, bill, reimbursement)
   │
   ▼
1. Normalise: clean merchant name, extract amount, currency, date, MCC code,
   line items, employee, department, project, memo
   │
   ▼
2. Rules layer (deterministic, customer-owned): "Vendor = AWS → 6210"
   ├── match → code + source "Rule" (skips AI)
   ▼
3. History lookup: same vendor/MCC/dept coded before? → strong prior
   │
   ▼
4. LLM classifier, given:
   • the tenant's active CoA (code, name, description, rules of use)
   • top-k similar past transactions (retrieval)
   • the expense context above
   → returns top 3 codes, confidence, one-line rationale, flags
   │
   ▼
5. Calibration + policy gate → route by confidence and risk
```

**Why retrieval + LLM, not a trained classifier per tenant:** a new customer gets useful results on day one from CoA descriptions alone, with no training data. Retrieval over their own history makes it sharper over time. Structured output is constrained to valid, active GL codes only, so the model can't invent a code.

## 3. Confidence and routing

| Tier | Condition | Action |
|---|---|---|
| **Auto-apply** | Calibrated confidence ≥ threshold (default 95%) and low risk | Code posted, marked "AI", visible in audit view |
| **Suggest** | 70–95% | Pre-filled, one-click confirm in queue |
| **Needs human** | <70%, or the model says ambiguous | Top 3 options shown, no pre-selection |

**Risk overrides** always force review regardless of confidence:
- Amount above a tenant-set limit
- Capital vs. expense ambiguity (e.g. laptop, software licence)
- Closed or locked period
- Intercompany, tax-sensitive, or related-party items
- Restricted accounts (equity, loans, payroll liabilities)
- First time a vendor is seen

Confidence is **calibrated** on held-out feedback, not taken from raw model self-reports. When it says 95%, it should be right about 95% of the time. Track this per tenant.

## 4. User experience

**Review queue (main surface)**
- Table: merchant, amount, suggested GL code, confidence chip, rationale on hover
- Keyboard-first: `Enter` accept, `1/2/3` pick an alternative, `E` edit
- Bulk accept for groups ("Accept all 42 high-confidence AWS items")
- Group by vendor so one correction fixes many

**Explainability panel** (one line, not a paragraph)
> "Coded to 6210 Software & Subscriptions: Notion was coded here in 14 of 14 prior transactions."

**Correction → learning prompt**
When a user changes a code: *"Always code Notion to 6210? [Create rule] [Just this once]"*. This turns corrections into deterministic rules that finance owns.

**Admin settings**
- Auto-apply threshold, per-account exclusions, amount limits
- "Shadow mode" for onboarding (see rollout)
- Rule manager and CoA descriptions editor. Good descriptions are the biggest lever on accuracy, so prompt admins to fill in weak ones.

**Splits:** the model can propose a split (e.g. a hotel bill into lodging, meals, and tax). Splits always require confirmation.

## 5. Learning loop
- Every accept, edit, and override is stored as a labelled example.
- Retrieval pulls from this corpus, so improvements apply immediately with no retraining.
- Corrections are weighted by role (controller > employee) and recency.
- **Drift handling:** when the CoA changes, retire dead codes, re-run suggestions on open items, and flag rules pointing to inactive accounts.
- Cross-tenant learning only on anonymised, non-identifying signals such as global merchant → category priors, and only with contract permission. Never expose one tenant's data to another.

## 6. Trust, safety, compliance
- **Audit trail:** each posting records the model version, inputs hash, suggestion, confidence, rationale, who accepted or overrode it, and the timestamp. SOX-friendly.
- **Segregation of duties:** auto-apply respects approval workflows. AI never approves, only codes.
- **Data privacy:** redact PII (card numbers, personal identifiers) before the LLM call. Use zero-retention LLM endpoints. Keep tenant data isolated at retrieval.
- **Prompt-injection defence:** merchant names, memos, and receipt text are untrusted. Treat them as data only, and validate output against the CoA schema.
- **Kill switch:** an admin can disable auto-apply instantly and bulk-revert AI-coded items in a date range.

## 7. Metrics

| Metric | Target |
|---|---|
| Auto-apply precision (not later changed) | ≥ 99% |
| Straight-through rate (no human touch) | 60% → 80% over 90 days |
| Top-3 hit rate on suggestions | ≥ 95% |
| Median review time per item | < 5 s |
| Calibration error | < 3 pts |
| Post-close reclassification journals | Down vs. baseline |

Also watch the **override rate by account**, since a spike signals a bad CoA description or drift. Monitor cost and latency per transaction.

## 8. Rollout
1. **Shadow mode (weeks 1–2):** AI predicts silently and is compared against what humans actually coded. Show the customer their projected accuracy.
2. **Suggest-only:** pre-fill, but nothing is auto-posted.
3. **Auto-apply for opted-in vendors and accounts:** start with the high-volume, low-risk ones (SaaS, utilities, travel).
4. **Widen thresholds** based on measured precision, not time elapsed.

Ship an offline eval set first: a few thousand labelled historical transactions across 5–10 design-partner companies. This is the regression gate for any prompt or model change.

## 9. MVP scope vs. later

**MVP:** card and bill expenses, rules + LLM + retrieval, confidence routing, review queue, create-rule-from-correction, audit log, shadow mode.

**Later:** receipt line-item splitting, multi-entity and intercompany logic, project/class/department dimension suggestions (not just GL), anomaly flags (duplicates, out-of-policy spend), natural-language rule creation ("code all Uber rides under $50 to Travel – Local"), and a month-end "what changed" summary for controllers.

## 10. Key risks and open questions
- **Poorly described CoAs** are the top accuracy risk. A CoA health check at onboarding is worth building.
- **Customers' inconsistent historical coding** can teach the model bad habits. Offer a way to exclude or down-weight old data.
- **Where to set the default auto-apply threshold.** It should be conservative until measured precision justifies raising it.
- Questions for you: which ERPs do you sync GL data with (NetSuite, QuickBooks, Xero)? Are you multi-entity? And do customers need approval before auto-posting? Those answers change the sync and permission design.

I can turn this into a shareable page or PRD, wireframe the review queue, or draft the LLM prompt and output schema. Which would help most?
