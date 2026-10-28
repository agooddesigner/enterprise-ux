# UX writing

**Load when:** writing or reviewing any UI text: button labels, errors, success and warning messages, confirmations, empty states, toasts, headings, labels, tooltips, timestamps, numbers. Also when auditing copy consistency across modules.

First rule: **if it needs explaining, redesign it.** Fix the flow or label before adding help text. Good UI copy is plain and unremarkable (GOV.UK). A long label usually signals a design problem (Pajamas).

---

## 1. Voice and tone by user state

| User state | Tone | Example move |
|---|---|---|
| New or confused | More directive; tell them exactly what to do next | "To add teammates, select **Invite**" |
| Blocked, stressed, error | Practical, calm, zero jokes, zero personality | "Payment failed. Update your card to keep access." |
| Routine success | Brief, neutral | "Invoice sent" |
| Rare milestone (first project, setup done) | Light warmth allowed, once | "Your workspace is ready" |
| Frequent action | Shortest possible; no celebration | "Saved" |

(Atlassian) Personality never beats clarity; delight only after trust and in small doses (Atlassian). No humour in errors (GOV.UK, NN/g) **[consensus]**.
- Address the user as "you"; use "I/my" only where the user is speaking (a consent checkbox) (GOV.UK).
- Say "we" only when the product is at fault (Polaris). Never blame the user: "We're having trouble connecting", not "You lost connection" (Atlassian).
- Active voice; present tense for instructions, past tense for completed actions (Atlassian, Fiori, Carbon) **[consensus]**.

## 2. Capitalisation

**Sentence case everywhere** — buttons, headings, labels, tabs, menus, column headers, nav (Carbon, Atlassian, PatternFly, Pajamas, Cloudscape, GOV.UK) **[consensus]**. Keep the user's own capitalisation for names they created (PatternFly). Alt: title case only if the product already follows SAP Fiori (see `foundations/defaults.md`). Never all caps for labels or tabs (NN/g).

## 3. Button and action labels

| Rule | Source |
|---|---|
| Start with a specific verb; 1–2 words: Save, Delete, Create, Export | Carbon, Atlassian, Fiori, Polaris **[consensus]** |
| Verb + object when context is ambiguous: "Edit issue", "Create distribution", "Save theme" | Pajamas, Cloudscape, Polaris |
| Drop articles: "Create page", not "Create a page" | Atlassian |
| Avoid OK, Done, Yes, Exit, Submit, Finish — name the result: "Accept and send", "Create network" | Carbon, Atlassian, Primer, PatternFly, GOV.UK |
| Dialog primary button repeats the title verb: "Delete contact?" → **Delete** | Carbon, Atlassian, Lightning |
| Add qualifiers only to tell options apart: "Apply now" / "Apply later" | GOV.UK |
| Ellipsis only when the action asks for more input before running ("Export…" opens options) | Atlassian. Alt: Cloudscape bans ellipses — follow the product's system |
| "Continue" over "Next" in question-by-question flows | GOV.UK. Alt: "Next" in stepper wizards with paired Back/Next (PatternFly) |
| No ">", "»" or "+" characters in labels; use icons | Pajamas, PatternFly |
| Buttons for actions, links for navigation | Polaris |
| Same action = same word app-wide (see §11) | Fiori, WCAG 3.2.4 |

## 4. Error messages

**Formula:** what happened + why (only if it helps and you know it) + how to fix — most likely fix first (Atlassian, Carbon, Fiori, PatternFly, Pajamas, Polaris, Cloudscape) **[consensus]**.
- Put the message next to the field, reusing the label's words; read it aloud to check (GOV.UK).
- **Empty field → instruction:** "Enter your first name", "Select a billing country" (GOV.UK).
- **Rule broken → description of the rule:** "Name must be 35 characters or less", "Date must be in the past", "Enter a date in the format 31 3 2026" (GOV.UK).
- Required pattern alt: "[Label] is required." (Cloudscape) — acceptable, but the instruction form is clearer.
- One specific message per failure type (empty, too long, too short, bad characters, wrong format) (GOV.UK).
- Title (where used): 3–4 words, no instruction, not repeated in the body; body 1–2 sentences (Atlassian). Carbon: terse phrases over full sentences.
- Raw codes and machine text go in an expandable "Details" section; include codes when they help users search for a fix (Cloudscape). With several errors, list each fix, not just a count (Polaris).
- When no fix exists, still give a next step: retry, refresh, contact support (Polaris, PatternFly). Don't promise what you can't do ("Our team has been notified") (Cloudscape).
- Don't guess at causes (Atlassian). Don't use validation messages for eligibility or permission problems — explain on a dedicated page or empty state (GOV.UK).

**Banned in errors** (union of sources):

| Banned | Source |
|---|---|
| "An error occurred", "This field is required", "Select an option" (alone, generic), "invalid"/"valid", "forbidden", "illegal", "you forgot", "please", "sorry", "oops", jargon | GOV.UK |
| "sorry" (inflates severity), "please" for required steps (makes them sound optional) | Atlassian |
| "invalid", jargon; over-apologising | Polaris |
| "Oops", "Uh oh"; error codes as the main message | PatternFly |
| "please", "thank you" | Cloudscape |

House rule: no "please" in errors (see `foundations/defaults.md`). Alt: Carbon and Pajamas allow "please" only when the user is genuinely inconvenienced (e.g. a maintenance window). Apologise only for serious failures such as outages or data loss (GOV.UK, NN/g).

| Bad | Good |
|---|---|
| Invalid input | Enter an amount between 1 and 10,000 |
| Error 500 | Couldn't save changes. Try again in a few minutes. |
| Oops! Something went wrong | Report didn't load. Refresh the page. |
| You entered the wrong password | Wrong password |

(GOV.UK for the last row: key words first.)

## 5. Success copy

- **Object + past-tense verb:** "Sales order created", "3 invoices approved" (Fiori); "Product updated", ≤3 words for toasts (Polaris); `Contact "Acme Ltd" was saved` with the record linked (Lightning).
- **Never** "Success!", "successfully" or exclamation marks (Atlassian, Fiori, PatternFly) **[consensus]**.
- No technical IDs in toasts; don't list multiple names — use the count (Fiori). If the user may need to copy an ID, use a persistent message, not a toast (Fiori).
- Offer "View [object]" after creation and Undo where possible (Atlassian).
- Show nothing if the result is already visible (Pajamas, Primer). Result-page titles: Object + Action + Status (Ant).
- No changes made → "No changes were made to [object]" (Cloudscape).

## 6. Warning copy (before the action)

Warnings appear **before** the action, not after (Atlassian). Include: what will happen if they proceed, an alternative, and a timeline if relevant (Atlassian).
- "Changing the billing cycle takes effect on 1 Dec. Your next invoice will be prorated."
- "Deactivating this user signs them out of all sessions. To keep their data, transfer ownership first."

## 7. Confirmation copy

- **Title = direct question with object and count:** "Delete 312 invoices?", "Approve order 12345?" — never "Are you sure?" (Fiori, PatternFly).
- Body: name the object in bold, state permanence ("You can't undo this action."), list cascading effects, suggest the safer alternative (deactivate, snapshot), and the restore deadline if a grace period exists (Cloudscape, Pajamas, Atlassian).
- Buttons: domain verb + Cancel ("Delete" / "Cancel") (Cloudscape, Ant). Alt: verb + object on both ("Yes, delete project" / "Cancel, keep project") when the object type is ambiguous (Pajamas).
- Typed confirmation instruction: "To confirm, type **confirm**" or the resource name (Cloudscape, Pajamas; choose per `foundations/defaults.md`).
- Friction tiers and dialog mechanics: `patterns/actions-and-dialogs.md`.

## 8. Empty-state copy

| Element | Limit | Source |
|---|---|---|
| Heading | 1 line, ≤5 words, gives the reason, no ending punctuation | Fiori, Pajamas, Cloudscape |
| Description | ≤3 lines, full sentences, lines under ~66 characters; only if it explains why | Fiori, Lightning, Cloudscape |
| CTA | 1 action, verb 1–2 words, matches the page's create label; secondary weight | Cloudscape, Fiori, Atlassian |

- Say what will appear and how to fill it ("Star reports to list them here") (NN/g). Never "Nothing here" or "No data" alone (Atlassian, NN/g).
- Wording: "No service accounts yet" (not "not found"); "Access permissions needed" (not "Access denied"); "Unable to connect" (not an error code); "Configure your system" (not "You haven't configured…") (PatternFly).
- Zero results: "No results for "acme"" + "Clear filters" (see `foundations/defaults.md`). Fiori pre-filter text: "To start, set the relevant filters."
- Don't repeat the heading in the CTA or body (Carbon, Atlassian). More in `patterns/feedback-and-states.md`.

## 9. Toast and notification copy

| Pattern | Example | Source |
|---|---|---|
| Object + past verb | "Sales order created"; "[n] [objects] [verb]" for many | Fiori |
| Type + record name + "was" + verb | `Contact "Ravi Kumar" was saved.` 1–2 full sentences, never truncated | Lightning |
| Noun + verb, ≤3 words, no Dismiss/OK text button (house default still keeps a close ×, see `foundations/defaults.md`) | "Product updated" | Polaris |

- ≤2 lines; one action, label ≤2 words; title has no end period and the body doesn't repeat it (Carbon). No vague links like "Learn more" (Atlassian).
- When and how long to show toasts: `foundations/defaults.md`.

## 10. Mechanics

| Rule | Source |
|---|---|
| Numerals, not words: "3 new commits" | Atlassian, Fiori, Carbon, Pajamas, PatternFly **[consensus]** |
| Oxford comma | Atlassian, PatternFly, Pajamas |
| Write "and", never "&" | Atlassian, Cloudscape, PatternFly, Pajamas |
| No "e.g.", "i.e.", "etc." — write "for example", "that is", or finish the list | Atlassian, Cloudscape, GOV.UK |
| "Select" or "choose", never "click" (device-neutral) | Cloudscape |
| No "above"/"below" — use "previous"/"following" or name the section | Cloudscape |
| No colour or position references ("the green button", "menu on the left") | GOV.UK, WCAG 1.3.3 |
| Numeric ranges: en dash, no spaces: "3–5 users", "1–10 Jan" | Pajamas. Alt: "to" in running prose (Atlassian) |
| Counts: "3 of 50", not "3/50" | Atlassian |
| Thousands separators from 1,000; format per locale with `Intl` | Atlassian, PatternFly, `foundations/defaults.md` |
| Currency: ISO code for non-dollar ("EUR 1,500"); US$/CA$/AU$ to disambiguate dollars | PatternFly. Ant: code + 2 decimals ("CNY 1,123.00") |
| No "account(s)" — use the plural | PatternFly |
| "might" for possibility, not "may" | Carbon |
| No exclamation marks in UI copy | Atlassian, Cloudscape |
| Bold UI element names in instructions, don't quote them: select **Save** | PatternFly |
| Lists ≤6 items | Atlassian |
| Loading text: single "…" glyph, no articles: "Downloading report…" — and pair with a real indicator | Pajamas, Cloudscape, Atlassian |
| Lead with the goal: "To see what changed, choose a branch" | Pajamas, PatternFly |
| Cut "in order to" and filler; one idea per sentence | Pajamas, GOV.UK |

### Punctuation by element

| Element | Rule | Source |
|---|---|---|
| Headings, titles | No period, no colon, not phrased as a question (dialog titles that ask a real question may end in "?") | Atlassian, PatternFly |
| Form labels | ~3 words or fewer, no colon, no period | Primer, Pajamas |
| Buttons, tabs, menu items | No punctuation | Pajamas, PatternFly |
| Tooltips, field descriptions (fragments) | No period | Atlassian |
| Hint text | One short sentence, no links | GOV.UK |
| Full sentences in messages and help | End with a period | Atlassian, Pajamas |
| Lists | Don't mix sentences and fragments | Pajamas |

### Tense (Pajamas)
- Just finished: present perfect or noun + verb — "Pipeline scheduled".
- Older events: simple past — "Deployed 3 days ago".
- Scheduled events: present tense, not "will" — "Backup runs at 02:00 UTC".
- Instructions: imperative — "Enter a name".

### Truncation (PatternFly)
- Avoid it (Atlassian). If unavoidable: keep ≥4 visible characters; truncate in the **middle** when the distinguishing part is at the end (file names, IDs: `invoice-2026…-0042.pdf`), at the **end** otherwise.
- Always expose the full string (tooltip for strings under ~150 characters) and in the accessible name.
- Never truncate nav items, column headers or button labels (PatternFly, `saas/global-and-performance.md`). Use the single "…" glyph.

## 11. Links and terminology

- Link text makes sense out of context — never "click here", "learn more" alone, or "View" (GOV.UK, WCAG 2.4.4). Repeated visible text ("Change") gets hidden text naming the item (GOV.UK). External links say "(opens in new tab)" (Polaris).
- **Same action, same word, everywhere.** Keep a glossary: Fiori's "Create" = make a new record, "Add" = attach an existing one; don't call it "Archive" in one module and "Deactivate" in another (Fiori, NN/g H4, WCAG 3.2.4) **[consensus]**.
- Use the user's domain words, not internal or schema names ("Invoice", not "AR_DOC") (NN/g H2). Field labels in the UI should match labels in exports and docs (general practice).
- Tabs: parallel grammar — all nouns or all verbs (Lightning).

## 12. Timestamp labels

- Pattern "[Noun] [verb]": "Instance launched", "Invoice paid" — past or future tense to match (Cloudscape).
- Drop "date", "time", "timestamp" from labels, except table columns: "Launch time" (Cloudscape).
- "Last" only for recurring events: "Last synced" (Cloudscape). Attribution: "Updated by [linked name]" (Cloudscape).
- Billing durations in the billing unit: "32 hours", not "1 day, 8 hours" (Cloudscape).
- Relative vs absolute and formats: `foundations/defaults.md`.

## 13. Plain language and acronyms

- Spell out acronyms on first use on every page; parentheses only to define them (GOV.UK, Pajamas).
- No clipped forms ("Proj. Fcst."); standard abbreviations like ID, API, URL, OK, FAQ are fine (Fiori, Carbon).
- Key words first; cut filler: "Wrong password" (GOV.UK).
- Prefer "cannot"/"do not" in critical instructions (GOV.UK avoids negative contractions). Alt: "can't" is fine in conversational products (Cloudscape uses it).
- Never hide constraints (limits, rules, legal text) in tooltips — put them in visible hint text (NN/g, Cloudscape).
- Leave room for translation; short strings can grow 200–300% (`saas/global-and-performance.md`).

---

## Common AI failures
- "Submit", "OK", "Done", "Yes" on primary buttons instead of the specific verb.
- Title Case Headings And Buttons in a sentence-case product.
- "Successfully saved!" toasts, exclamation marks, "Oops!" errors.
- Generic errors ("Invalid input", "Something went wrong") with no fix.
- "Please" and "sorry" in routine validation messages.
- "Are you sure?" confirmations that don't name the object or count.
- "Click here" / "Learn more" links; "click the button below"; references to colour or position.
- Mixing "Create"/"Add"/"New" for the same action across screens.
- Empty states saying "No data" when the load failed.
- Truncating button labels or column headers; "e.g." and "&" in UI text.
- Explaining a confusing UI with a tooltip instead of fixing the label.

## Sources
- https://atlassian.design/foundations/content/voice-tone
- https://atlassian.design/foundations/content/language-and-grammar
- https://atlassian.design/foundations/content/designing-messages
- https://atlassian.design/foundations/content/designing-messages/error-messages
- https://atlassian.design/foundations/content/designing-messages/warning-messages
- https://atlassian.design/foundations/content/designing-messages/success-messages
- https://atlassian.design/foundations/content/designing-messages/empty-state
- https://atlassian.design/components/flag/usage
- https://carbondesignsystem.com/guidelines/content/overview
- https://v10.carbondesignsystem.com/guidelines/content/writing-style
- https://carbondesignsystem.com/components/notification/usage/
- https://carbondesignsystem.com/patterns/empty-states-pattern/
- https://spring-21.lightningdesignsystem.com/guidelines/messaging/components/toasts
- https://spring-20.lightningdesignsystem.com/guidelines/empty-state
- https://spring-21.lightningdesignsystem.com/guidelines/navigation
- https://www.sap.com/design-system/fiori-design-web/v1-148/foundations/writing-and-wording/ux-writing/ux-writing-guidelines/ui-text
- https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/message-toast/usage
- https://www.sap.com/design-system/fiori-design-web/v1-96/foundations/best-practices/global-patterns/designing-for-empty-states
- https://cloudscape.design/patterns/general/errors/error-messages/
- https://cloudscape.design/patterns/general/timestamps/
- https://cloudscape.design/patterns/general/empty-states/
- https://cloudscape.design/patterns/resource-management/delete/delete-with-simple-confirmation/
- https://cloudscape.design/patterns/resource-management/edit/page-edit/
- https://primer.style/product/ui-patterns/forms
- https://www.patternfly.org/ux-writing/capitalization
- https://www.patternfly.org/content-design/writing-guides/error-messages
- https://www.patternfly.org/content-design/grammar/numerics
- https://www.patternfly.org/content-design/grammar/punctuation
- https://www.patternfly.org/content-design/grammar/truncation
- https://www.patternfly.org/components/empty-state/design-guidelines
- https://patternfly.org/components/wizard/design-guidelines
- https://design.gitlab.com/content/ui-text/
- https://design.gitlab.com/content/punctuation/
- https://design.gitlab.com/content/verb-tenses
- https://design.gitlab.com/patterns/destructive-actions/
- https://polaris-react.shopify.com/content/error-messages
- https://cdn.jsdelivr.net/npm/superv5_polarisui@2.0.1/dist/docs/components/Toast/README.md
- https://gov.uk/service-manual/design/writing-for-user-interfaces
- https://design-system.service.gov.uk/components/error-message/
- https://design-system.service.gov.uk/patterns/question-pages/
- https://design-system.service.gov.uk/patterns/check-answers/
- https://design-system.service.gov.uk/patterns/validation/
- https://www.nngroup.com/articles/error-message-guidelines/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://www.nngroup.com/articles/info-tips-bad/
- https://ant.design/docs/spec/research-result
- https://ant.design/docs/spec/buttons.md
