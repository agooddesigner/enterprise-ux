# AI GL-code categorisation: feature spec

**Job:** An AP clerk or bookkeeper clears the uncoded-expense queue. Month-end close is the high-stakes window. They do this daily, at 50–500 items a day, and the reviewer is accountable to the controller.
**Principle:** AI proposes, humans approve, and the system learns. Confident items are cleared in bulk and uncertain ones get real attention. Nothing is posted to the ledger without a recorded decision.

## 1. How it works

**Inputs per expense:** merchant (normalised), description or line items, amount and currency, card or employee, department and cost centre, receipt OCR text, and the past coding of the same merchant.

**Pipeline (cheapest first):**
1. **Rules.** Explicit customer rules, such as "Uber → 6420 Travel", always win. They are deterministic and auditable.
2. **History match.** If this vendor was coded to one GL in at least 90% of the last N entries, use that code. It needs no LLM call.
3. **LLM classifier.** Used for everything else. It is given the customer's own chart of accounts (code, name, description, active status), the expense, and 3–5 retrieved similar past entries as few-shot examples. It returns structured output: the top 3 codes, a one-line reason, and the evidence used. Only active, postable accounts from that tenant's chart are allowed, so it can't invent a code.
4. **Calibration.** Raw model confidence is mapped to a calibrated score using each tenant's accept and override history. The thresholds below are tuned per tenant against measured precision, not guessed.

| Band | Calibrated score | Behaviour |
|---|---|---|
| **High** | ≥ 0.92 | Pre-filled, grouped for one-click bulk approval. Optional auto-post only once the tenant enables it (see §5). |
| **Medium** | 0.60–0.92 | Suggested, needs individual review. Alternatives are shown. |
| **Low** | < 0.60 | No suggestion is pre-selected. The top 3 are offered and the item is flagged "Needs a human". |

**Forced review, regardless of score:** amount above a tenant threshold, a closed or locked period, a restricted account (equity, intercompany, tax), a new vendor, or a split-worthy receipt (multiple line items with different categories).

**Learning loop:** Every approve or override is logged. Overrides feed the tenant's few-shot retrieval immediately, so the same correction is not needed twice. After two consistent overrides for a vendor, the UI offers "Always code {vendor} to {GL}?" and turns the answer into a rule. Nothing is trained across tenants, and each tenant's data stays isolated.

## 2. Main screen: Review queue (`/expenses/coding`)

- **Layout:** a dense table at 40px row height with a compact toggle, plus a right-hand detail panel for the focused row. It is not a card layout.
- **Columns:** Date · Merchant · Description (truncated, full text on hover) · Amount (right-aligned, tabular figures, with currency) · Department · **Suggested GL** (inline editable combobox) · Confidence · Status.
- **Confidence:** shown as a labelled chip (High / Medium / Low), never colour alone. The number is on hover.
- **Header summary:** "212 to review: 164 high confidence, 38 medium, 10 need a human". Each count is a filter shortcut.
- **Primary action:** **Approve 164 high-confidence** opens a confirmation naming the count and total value, e.g. "Approve 164 expenses totalling $48,213.40?". It includes a "Review sample" link that filters to the lowest-scored 10 of those.
- **Filters:** confidence, status, department, vendor, amount range, date, "AI changed since last time". Saved views are supported, and all filter state is in the URL.
- **Keyboard:** `J/K` to move, `A` to approve, `E` to edit the code, `Space` to select, `⇧A` to approve the selection, `?` for the shortcut list.

**Detail panel (the explainability part):**
- Receipt image next to the extracted fields.
- **Why this code:** one plain sentence, e.g. "Last 11 payments to Delta were coded to 6420 Travel – Air" plus the evidence chips (rule, history, receipt text). It does not show raw model reasoning.
- Alternatives with their scores, one click to switch.
- **Split line** for multi-category receipts.
- Optional note on override ("Why did you change it?"), with quick-pick reasons that improve the learning loop.
- History: who approved it, when, from which suggestion. Timestamps are absolute with timezone, since this is audit data.

## 3. Trust and control

- **Settings → AI coding** (admin only): enable per entity, confidence thresholds, auto-post toggle (off by default), excluded accounts, amount cap for forced review, and rule management.
- **Accuracy dashboard:** acceptance rate, override rate by GL and by vendor, time saved, and a trend line. It also lists the top 10 most-overridden vendors, which feeds suggested rules.
- **Audit trail:** every posting stores the suggestion, score, source (rule, history or model), model version, reviewer, and final code. It is exportable and immutable.
- **Undo:** bulk approvals can be undone for 30 seconds via a toast, and afterwards from "Recent activity" until the period closes. Posted entries in a closed period require a reversing entry, and the UI says so.
- **Privacy:** the AI acts only on the tenant's own data, receipt text is redacted of card numbers before it reaches the model, and the model call is logged without personal data.

## 4. Edge cases

- **Chart of accounts changes:** if a suggested account becomes inactive, the suggestion is invalidated and re-run. The row shows "Account 6310 was archived. Choose a replacement."
- **Duplicates:** a likely duplicate is flagged and not auto-approved.
- **Multi-currency and tax:** the code is proposed along with a tax code where the tenant has tax configured.
- **Unknown merchant, e.g. "SQ *JOES"**: normalised first. If still unknown, it falls to Low.
- **Cold start:** with fewer than 50 coded historical entries, the feature shows "Learning mode": suggestions are labelled Low and there are no bulk approvals. Admins can import 12 months of history to skip this.

## 5. Rollout

1. **Shadow mode.** Suggestions are computed but not shown, and compared with what humans actually coded. The admin sees "On your last 90 days, we'd have matched 91%" before enabling anything.
2. **Suggest mode** (default). Humans approve everything.
3. **Auto-post for High** is opt-in per vendor or per GL once the measured accuracy for that slice exceeds a threshold. It is disabled again automatically if the override rate rises.

**Success metrics:** the share of entries approved without edits (target 70%+ at launch), the override rate within High (target under 2%), median time to clear the queue, the number of post-close reclassification journals (should fall), and reviewer trust measured by how often they open the "Review sample" link.

## 6. States

| View | State | Trigger | User sees | Action |
|---|---|---|---|---|
| Queue | Empty, first use | No expenses synced | "No expenses to code yet" and a card-feed connect link | Connect source |
| Queue | Empty, cleared | All approved | "Queue clear. 212 coded this week" | View coded history |
| Queue | No results | Filters exclude all | "No expenses match these filters" | Clear filters |
| Queue | Loading | Initial fetch | Skeleton rows | none |
| Row | Suggesting | Model running | Per-row spinner, the rest stays usable | Edit manually |
| Row | AI failed or timed out | Model error | "Couldn't suggest a code. Try again or choose one." Includes a reference ID | Retry / pick GL |
| Queue | AI service down | Outage | Banner: "Suggestions are unavailable. Manual coding still works." | Continue manually |
| Bulk approve | Partial failure | 3 of 164 fail validation (e.g. closed period) | "161 approved. 3 need attention", with those rows filtered | Fix the 3 |
| Page | Read-only | Viewer role | Approve and edit disabled, with a tooltip naming who can | Request access |
| Page | No permission | No coding access | Explains the access needed and who the admins are | Contact admin |
| Settings | Unsaved changes | Navigating away | Prompt to save | Save / discard |

## 7. Audit summary
I checked this against the enterprise checklist and found these points covered:
- **States:** every list and bulk operation has empty, loading, error, partial-failure and permission states.
- **Safety:** bulk approvals name the count and value and can be undone, and auto-post is opt-in and off by default.
- **Density and state:** the queue is a dense table with right-aligned numbers, URL-persisted filters, and keyboard shortcuts.
- **Trust:** each suggestion has a reason, an alternative and an audit trail, and the model can only choose from the tenant's own active accounts.

I haven't validated the thresholds (0.92 and 0.60) or the accuracy targets. They need to be tuned against your real data during shadow mode.

Two questions would sharpen this: which ERP or ledger do you post to (that decides how reversals and period locks work), and do you need split coding at launch? I can also turn this into a clickable prototype or a shareable page for your team.
