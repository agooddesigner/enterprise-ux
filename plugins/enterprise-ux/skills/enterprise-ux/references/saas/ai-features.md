# AI features and agents

**Load when:** deciding whether to add AI, designing AI-generated content, assistants, copilots, recommendations, confidence/explanations, human-in-the-loop review, autonomous agents, agent permissions and logs, or AI transparency/compliance.

## 1. Should this be AI at all?

- Use AI only where it adds unique value; even a great model fails if a filter, default or rule would do. Don't bolt a chatbot on where a filter works. (PAIR)
- Name the user need and success metric first (see §11). (PAIR)
- Always keep a **non-AI fallback path** to complete the task manually. (PAIR)
- Explain the benefit, not the technology; say plainly that output is algorithmic. (PAIR)
- Onboard in stages: what it can and can't do, how it changes, how users can improve it. (PAIR)

## 2. Microsoft HAX guidelines (18), applied

| Phase | Guidelines | Enterprise application |
|---|---|---|
| Initially | G1 make clear what it can do · G2 make clear how well | State scope and known accuracy on first use ("Categorizes invoices from 40 known vendors; review low-confidence ones") |
| During interaction | G3 time to context · G4 show relevant info · G5 match social norms · G6 mitigate social biases | Suggest at the moment of the task, not on load; neutral, professional tone; test outputs across user groups |
| When wrong | G7 efficient invocation · G8 efficient dismissal · G9 efficient correction · G10 scope when in doubt · G11 explain why | One-click accept/reject inline; edit in place; ask before acting when confidence is low; "Why?" popover |
| Over time | G12 remember recent interactions · G13 learn from behaviour · G14 adapt cautiously · G15 granular feedback · G16 convey consequences · G17 global controls · G18 notify about changes | Admin on/off and data controls; announce model changes in the changelog; feedback that the model can actually use |

(Microsoft HAX)
- Don't apply all 18 equally — prioritize by risk with the HAX workbook approach. (Microsoft HAX)

## 3. Disclosure and labelling

- Label AI-generated or AI-assisted content **everywhere it appears**. (Carbon) **[consensus]** with Salesforce disclosure.
- **Focused label** per item when users act on individual items; **broad label** per section when they don't; both when needed. (Carbon)
- The AI label is **never decorative and never disabled**. AI actions (regenerate, refine) get their own icons, not the label. (Carbon)
- The label opens an **explainability popover**: overview, supporting details, sources/artifacts, additional actions. Explanations on demand, not inline noise. (Carbon)
- When a user edits AI content, drop the AI styling and show **"Revert to AI"** — the original suggestion is always recoverable. (Carbon)
- Disclose when AI **autonomously** produced content seen by others (e.g. a bot reply to a customer). (Salesforce)
- Label with text + icon, not a colour or gradient alone. (WCAG 1.4.1)

## 4. Confidence

- Show confidence **only if testing shows it improves decisions**. (PAIR)
- Prefer **categorical** (High / Medium / Low), each tied to an action ("Low — review before approving"), over raw percentages. (PAIR)
- When confidence is low, show **N-best alternatives** instead of one answer. (PAIR)
- Numeric scores and error bars mostly suit expert users. (PAIR)
- Don't show numeric confidence without context. (PAIR)

## 5. Sources, citations and calibrated trust

- Aim for **calibrated** trust, not maximum trust; showing the AI may be wrong reduces over-reliance. (PAIR)
- Scale explanation to stakes; **always** explain high-stakes outputs; full explanations when law or accountability requires. (PAIR)
- Provide citations/sources for verification; highlight claims that need checking (stats, dates, recommendations). (Salesforce, Smashing agentic AI)
- Express uncertainty rather than hiding it in fluent prose; say when key information is missing. (Salesforce, PAIR)
- Trust rests on ability, reliability and benevolence — design for all three. (PAIR)

## 6. Human-in-the-loop autonomy ladder

Set per task type, not per product (Smashing agentic AI):

| Level | AI does | User does | Use when |
|---|---|---|---|
| 1. Observe & suggest | Recommends | Decides and acts | High stakes, new feature, low trust |
| 2. Plan & propose | Drafts a full plan | Edits/approves plan | Multi-step work with external effects |
| 3. Act with confirmation | Executes after approval | Confirms each risky step | Reversible-but-costly actions |
| 4. Act autonomously | Executes within pre-approved bounds | Reviews history; can undo | Low-risk, high-volume, well-tested tasks |

- Users want control when stakes are high or the task is meaningful. (PAIR)
- Never auto-apply AI changes to records without consent in high-stakes workflows. (Shneiderman rule 7; PAIR)

## 7. Intent preview, undo, pause

- **Intent preview**: before anything external happens, show the full plan with consequences; let users edit or reject individual steps. (Smashing agentic AI)
- Confirmations carry enough information to prevent **blind approval** (what, which records, how many, reversible?). (Why Johnny Can't Use Agents)
- Easy, visible **undo** with predefined recovery paths; after an undo, ask a one-tap reason to separate model error from preference. (Smashing agentic AI)
- **Pause / stop / kill switch**, checkpoints and rollback for running agents. (Why Johnny Can't Use Agents)
- Explicit hand-off points for logins and credentials — never ask users to paste passwords into chat. (Why Johnny Can't Use Agents)
- When stuck, the agent stops and asks rather than looping. (Why Johnny Can't Use Agents)
- Checklist-only patterns from a low-quality catalog (use for review, not as authority): dry-run / blast-radius preview, reversibility labels, cancelable countdown before high-impact actions, autonomy budgets, persistent "agent running" indicator, editable memory. (aiuxplayground)

## 8. Agent permissions

- Agents get their own identity and scoped credentials, never a human's session. (Stripe)
- Stripe model: tag keys used by agents at creation → two-party approval auto-applies to refunds, cancellations, payouts and transfers; approvals expire; requester can't self-approve; justification field. Use as the template for "agent RBAC". (Stripe) See `saas/accounts-and-permissions.md`.
- Grant per-capability permissions (read invoices ≠ issue refunds); default read-only. (Stripe best practices; least privilege)
- Admin global controls: enable/disable AI per workspace, choose data sources, set autonomy ceilings. (Microsoft HAX G17)

## 9. Agent states and logs

- Show **completed / blocked / uncertain / running / paused / failed** as distinct states with text labels. (Why Johnny Can't Use Agents)
- Progress logs surface **milestones**, with raw detail collapsed — not a dense stream. (Why Johnny Can't Use Agents)
- Never silently freeze; show progress for long runs and a stall warning. (Why Johnny Can't Use Agents; NN/g 10 s)
- Each agent action has a unique ID and lands in the audit log with actor = agent, on behalf of = user. (Smashing agentic AI) See `saas/collaboration-and-audit.md`.
- Real user problems found in a 31-person study: unclear capabilities, reluctance to hand over credentials, agents assuming minimal involvement, dense logs, silent freezes/loops. Design against each. (Why Johnny Can't Use Agents)

## 10. Data scope and feedback

- Explain **data scope** (what's used and why), **reach** (personal vs aggregate) and **removal** (can it be reset/deleted). (PAIR)
- Implicit signals (logs) need disclosure and an opt-out; explicit feedback (thumbs) needs clear options; ask only for feedback the model can learn from; acknowledge it and set realistic timing for its effect. (PAIR)
- Let users edit, reset or erase what the AI remembers. (PAIR)
- A "show less" control must not pretend to retrain the model if it only filters. (PAIR)

## 11. Metrics

Track (Smashing agentic AI, Why Johnny Can't Use Agents):
- Intervention rate (how often humans step in).
- Unintended actions per 1,000 tasks.
- Undo/rollback rate, with reasons.
- Time to recover after an error.
- Stall/loop rate.
- Plus acceptance rate and edit distance of accepted suggestions (general practice).

## 12. EU AI Act Article 50 transparency (verify — as of Oct 2026)

Single law-firm source (Goodwin); not legal advice:
- Applied from **2 Aug 2026**: tell people they're interacting with AI unless obvious; machine-readable marking of synthetic audio/image/video/text (systems on the market before 2 Aug 2026 have until 2 Dec 2026); deployers disclose deepfakes; inform people exposed to emotion recognition/biometric categorisation.
- Fines up to €15M or 3% of turnover.
- The Digital Omnibus (Reg. 2026/1744) delayed high-risk obligations (to 2 Dec 2027 / 2 Aug 2028) but **not** transparency. Commission transparency guidelines adopted 20 Jul 2026.
- Design implication: chat/agent surfaces carry a persistent "AI" disclosure; generated files carry metadata marking.

## Common AI failures

- Sparkle icon used as decoration with no label, no popover, no explanation.
- "92% confident" badges with no action tied to them.
- Agents that act on records with no plan preview, no undo, no stop button.
- Confirmation dialogs like "Run agent? OK" with no detail.
- Agent logs that dump raw tokens/tool calls with no milestones.
- Agents reusing the user's full session permissions; no approval rules for money movement.
- No manual path once the AI feature ships.
- Edited AI text still styled as AI, or no way back to the original.
- Thumbs up/down that go nowhere.
- Chatbot added where a filter or saved view would solve the task.

## Sources

- https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/
- https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/
- https://www.microsoft.com/en-us/haxtoolkit/about/
- https://pair.withgoogle.com/guidebook-v2/chapters
- https://pair.withgoogle.com/chapter/explainability-trust/
- https://pair.withgoogle.com/chapter/People%20+%20AI%20Guidebook%20-%20Mental%20Models.pdf
- https://pair.withgoogle.com/chapter/People%20+%20AI%20Guidebook%20-%20Feedback%20+%20Control.pdf
- https://carbondesignsystem.com/components/ai-label/usage/
- https://carbondesignsystem.com/guidelines/carbon-for-ai/
- https://www.salesforce.com/news/stories/generative-ai-guidelines/
- https://smashingmagazine.com/2026/01/beyond-generative-rise-agentic-ai-user-centric-design/
- https://arxiv.org/pdf/2509.14528
- https://aiuxplayground.com/patterns/agents
- https://docs.stripe.com/keys
- https://docs.stripe.com/keys-best-practices.md
- https://docs.stripe.com/account/approvals.md
- https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force
- https://www.cs.umd.edu/~ben/goldenrules.html
- https://nngroup.com/articles/response-times-3-important-limits
