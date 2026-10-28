# Forms and saving

**Load when:** designing, critiquing or auditing any data-entry surface — create/edit forms, settings pages, dialogs with inputs, wizards, validation, save/autosave behaviour, or unsaved-changes handling.

If the product already has a design system, its form rules win. Otherwise apply these and `foundations/defaults.md`.

## 1. Decide what to ask (question protocol)

- Ask a field only if you can say: we need it, why, what we do with it, who must answer, how we check it, and how we keep it secure and current. Use this to push back on "nice to have" fields. (GOV.UK)
- Don't ask what the system already knows or can detect — pre-fill it; otherwise offer type-ahead. (Carbon, Ant, Tesler's law)
- Don't make users re-enter data already given in the same process; pre-fill or offer "same as …". (WCAG 3.3.7)
- Put eligibility/blocking questions first; order the rest by the most common scenario; branch so users see only relevant questions. (GOV.UK)
- Eligibility or permission problems are not validation errors — route to a page that explains the outcome and next step. (GOV.UK)
- Accept common formats (phone, postcode, IDs with spaces/dashes) in one field and normalise; strip stray spaces. (GOV.UK, CXP, Postel's law)

## 2. Layout

- **Single column**, top to bottom. Side by side only for tightly related short fields (first/last name, amount + currency). Never multi-column just to save space. (Primer, Pajamas, CXP) **[consensus]**
- Alt: wide object/detail pages in display/edit mode may use responsive columns (4 at XL, 3 at L, 2 at M, 1 at S). (Fiori)
- **Labels above fields.** (see `foundations/defaults.md`) (Carbon, Fiori, Lightning, CXP) Alt: left labels only for <10-field forms on wide screens where vertical density is critical — left-aligned, not right-aligned. (Lightning, CXP; Ant defaults left)
- Labels: sentence case, ~3 words or fewer, no colon or end punctuation. (Primer, Pajamas)
- **Input width matches expected value** on a base-8 scale — max XS 80, S 160, M 240, L 320, XL 560px. A postcode field is not full width. (Pajamas, Primer)
- Group long forms into labelled sections (chunking). (Miller's law, Common region)
- Keep display, edit and create layouts identical so nothing shifts between modes. (Fiori)
- Button placement: in-page forms left-align actions with the fields (primary first, Cancel after); dialogs and wizards right-align (Cancel left of primary). (Carbon, Primer, GOV.UK)
- One primary button per form; Cancel is never primary. (all systems)

## 3. Required vs optional

- Mark the minority: enterprise forms are mostly required → mark optional fields "(optional)". Never asterisks alone. One convention per product. (see `foundations/defaults.md`) (Carbon, Cloudscape, Pajamas, GOV.UK, CXP) Alt: mostly-optional form → mark required fields "(required)". (Primer, Pajamas)
- State the convention once above the form ("All fields are required unless marked optional"). (Carbon, Atlassian)
- Set `required` / `aria-required` in code regardless of visual convention. (Primer) Note: GOV.UK turns off HTML5 validation (`novalidate`) to control messages itself — do the same when you render custom errors.
- On radios/checkbox groups, mark "(optional)" on the legend. (GOV.UK)

## 4. Help text and placeholders

- **Never use placeholder as the label** and never put essential info in it. (see `foundations/defaults.md`) **[consensus]**
- Placeholder only to show an example format. (Lightning)
- Hint/helper text sits under the label, above the input; one short sentence (≤~100 characters), no links. (Carbon, GOV.UK, Lightning)
- Longer explanations: info-icon popover — but never hide constraints (limits, rules, legal text) in a tooltip. (Lightning, Ant, NN/g)
- Put tips beside the field they describe. (CXP)
- Character limits: hard limit → counter always visible, turns danger + negative count when exceeded; soft limit → hidden until exceeded. Counter text "Character count: n/max". (Pajamas, Cloudscape)
- If a form needs lots of help text, fix the labels and questions first. (GOV.UK, NN/g)

## 5. Choose the control

| Choice | Control | Source |
|---|---|---|
| One of 2–~5 options, all worth seeing | Radio group | (Carbon, Ant) |
| One of 6–10 options, or any single choice inside a dense form | Select / picklist | (Ant, Lightning) |
| One of >10 options, or a large/remote set | Combobox with type-ahead | (PatternFly, Fiori) |
| Zero or more independent options | Checkbox group | (Carbon) |
| Single opt-in that's submitted with the form | Single checkbox | (Carbon, ARIA APG switch) |
| Binary setting that **applies immediately** | Toggle/switch — never beside a Submit button or unsaved inputs | (Lightning, Ant, ARIA APG) |
| Many-of-many from a large set | Multi-select combobox with Save/Cancel (doesn't save on close) | (Primer) |
| Precise number on a range | Slider + number input | (Ant) |
| Date | Date picker accepting typed input; 3 fields for memorable dates | (GOV.UK; general practice) |
| Format-constrained value | Typed/masked input | (Fiori) |

- Radio list standalone only for <10 options; inside a larger form prefer a picklist. (Lightning)
- Toggles need a field label and a state label; the accessible name must not change with state. (Lightning, ARIA APG)
- Use the simplest control that works; prevent errors with typed inputs. (Fiori)
- File upload: state size/format limits and show progress; always offer "Browse files" beside any drop zone. (Ant, WCAG 2.5.7)
- Add `autocomplete` tokens on personal-data fields. (WCAG 1.3.5)

## 6. Validation

**Timing** (see `foundations/defaults.md`):
- Never validate before the user interacts or on page load. Validate on submit; once a field shows an error, re-validate it live as the user fixes it. (GOV.UK, Primer; live re-validation once in error is common ground with Cloudscape)
- Alt: long, expert data-entry forms → also validate format on blur. (Carbon, Fiori, Cloudscape, Polaris)
- Validate on the server always; client-side is optional. (GOV.UK)
- If validation takes >1s, show a loader. (Primer)
- Validate a dialog's form before it closes; on error keep it open with inline messages. (Carbon)

**Don't disable submit** to signal errors — keep it enabled and explain on click. Disable only to block double submit (with loading state), for unmet prerequisites with a visible reason, or in a tiny typed-confirmation modal. (see `foundations/defaults.md`) Prevent double submission on the server too. (GOV.UK)

**Error summary:**
- On submit with 2+ errors, show an error summary at the top of the form/main (below breadcrumbs, above the h1): heading "There is a problem", each item a link that focuses its field; move focus to the summary. With 1 error, focus the field. (see `foundations/defaults.md`) (GOV.UK, Primer) Alt: GOV.UK shows the summary even for one error; Cloudscape scrolls to the first error with no summary.
- Summary wording matches the inline message exactly. Prefix `<title>` with "Error: ". (GOV.UK)
- Dense enterprise screens: a message button with a counter in the footer opening a list of all messages is an alternative. (Fiori)

**Inline messages:**
- Directly below the label/hint, above the input (or directly below the input — pick one placement per product); always visible, never in a tooltip; red border + icon + text, never colour alone. (GOV.UK, Pajamas, NN/g, WCAG 1.4.1)
- One message per radio/checkbox group, not per option. (Primer)
- **Connected fields** (amount + currency, postcode + city, date parts) show one shared message and all get the error state. Link a multi-field error to the first broken part. (Fiori, GOV.UK)
- Read-only fields never show error states. (Fiori)
- Messages from sub-pages/line items name the item they belong to. (Fiori)

**Server and general errors:**
- Recoverable (limits, fixable permissions): inline alert directly above the form's buttons. Unrecoverable or success: page-level message after submit. (Cloudscape, Carbon)
- Keep the user on the page during submit with a button loading state; don't redirect before knowing the result. (Cloudscape)
- **Keep all entered data after any error — never clear fields, including valid ones.** (GOV.UK, NN/g, Primer) **[consensus]**

**Copy:** say what's wrong and how to fix it, reusing the label's words; instruction for empty ("Enter a cost centre"), description for broken rules ("Name must be 35 characters or less"). Banned: "invalid", "This field is required", "An error occurred", "please", "sorry", "oops". Full rules: `foundations/writing.md`. (GOV.UK, Cloudscape, Atlassian)

## 7. Container: where the form lives

| Form | Container | Source |
|---|---|---|
| One value | Inline edit (✓/✕) | (Cloudscape, Lightning) |
| Short, focused task the user started, <8 fields, no need to reference the page | Modal dialog | (Fiori, Carbon, NN/g) |
| Edit while referring to the list/page behind | Non-modal side panel / drawer | (NN/g, Ant) |
| ≥8 fields, sections, or shareable/linkable create/edit | Full page | (Fiori, Carbon, Cloudscape) |
| Long, complex or dependent steps | Wizard (§11) | (PatternFly, Cloudscape) |
| Long transaction done over several sessions | Task list (§11) | (GOV.UK) |

- Never put a form in a modal opened from a modal. Avoid tabs, accordions, data tables and links that leave the task inside dialogs. (Carbon, Atlassian)
- Modal initial focus: first input. (see `foundations/defaults.md`)
- Never put checkout-like high-stakes flows in a modal. (NN/g)

## 8. Create forms

- Primary section: only required fields with no good default + fields 80%+ of users need. Everything else in an expandable section with a noun label ("Additional settings"). (Cloudscape) Max two disclosure levels. (NN/g)
- Use **smart defaults** so "Create" works immediately. (Cloudscape, Ant)
- Submit label = "Create [resource]" — never "Submit", "OK" or "Done". (Cloudscape, Carbon, Atlassian)
- Breadcrumb ends "Create [resource]"; side nav closed on create/edit pages. (Cloudscape)
- After create: land on the new resource (no toast needed) or return to the list with the new row highlighted at top. (Lightning, Fiori, Ant)
- After edit: return to where the user started with a success message. Saved with no changes → "No changes were made to [object]." (Cloudscape)

## 9. Save model

- **Explicit Save for forms.** Instant-apply only for imperative controls (toggles, segmented controls, single selects outside a form). **Never mix both in one form** (or on one page with several forms). (see `foundations/defaults.md`) (Primer, Pajamas)
- **Never autosave financial, security or privacy settings** (passwords, payment, permissions, confidentiality flags). (Pajamas)
- Alt: long free-text/document editing or preference lists users forget to save (Slack notification prefs) → autosave per field. (Pajamas, Slack)
- One Save per form and per page; no per-section Save buttons; never hide or disable it; omit it entirely if everything autosaves. Primary style when it saves the whole page, secondary when it saves one segment. (Primer)

**Autosave mechanics** (Pajamas):
- Save per input, never the whole form. Clicks save immediately; typing saves on blur and **3s after the last keystroke**.
- Status inline next to the control: "Saving…" with spinner → "Change saved" / "3 changes saved" (don't stack) → drafts "Saved 1 min ago".
- Undo inline, not in a toast. On failure: persistent inline alert "Failed to save 2 changes" + Retry.
- Optimistic updates: show the new value dimmed (50% opacity) with a spinner until confirmed; keep retrying; warn on leave mid-save.

## 10. Unsaved changes

- Warn only when something actually changed and isn't saved — on Cancel, side-nav links, breadcrumbs and in-app navigation. Never when nothing changed, the link opens a new tab, or it's a disclosure toggle. No "don't show again". (Cloudscape)
- Dialog: "Leave page?" — **Stay** (default focus) / **Leave**. Alt: when the form is valid and saving is cheap, add "Save and leave". (see `foundations/defaults.md`) (Cloudscape, Pajamas)
- Use browser `beforeunload` for tab close, reload, history and URL edits (its text can't be customised). (Cloudscape, Primer)
- Wizards: confirm before closing if anything was entered; exit silently if not. Offer "Save as draft" where possible. (PatternFly, Cloudscape)
- Long data entry: save progress at intervals or offer save-and-return. (Cloudscape, GOV.UK)
- Session timeouts: warn with ≥20s and a one-step extend; preserve form data across re-auth. (WCAG 2.2.1) See `foundations/accessibility.md`.

## 11. Wizards and multi-step

- Use a wizard for long, complex or dependent tasks; single-page create for simple-to-medium forms. Use staged steps only when steps are independent — users bouncing between steps signals one page is better. (PatternFly, Cloudscape, NN/g)
- **≤7 steps, ideally 3–5**; each step fits without scrolling and has a unique, outcome-focused title. (Cloudscape, PatternFly)
- Let users jump back to completed steps without losing data; validate on step change. (NN/g, Cloudscape)
- Progress: step list/stepper with current step; for linear question flows, plain "Step 3 of 5" only if the total is reliable. (PatternFly, GOV.UK)
- Footer: **Back, Next (primary), Cancel**; Back disabled on step 1; final button names the action ("Create network"), never "Finish". Right-aligned. (PatternFly, Carbon)
- Optional steps: group them, enable the review step once required steps are done, offer "Skip to review". (PatternFly)
- **Review step** (always for create/provision flows): same order as the steps, an Edit link per section that jumps to that step and returns to review, no inline editing on review, skipped optional answers shown as "Not provided", submit label is the specific action. (PatternFly, Cloudscape, GOV.UK)
- Required for legal/financial/data-changing submissions: a review/confirm step or reversibility. (WCAG 3.3.4)
- Long apply: progress screen; Cancel only if it really rolls back. Result screen's primary goes to the new resource. Hide the step nav after submit. (PatternFly)
- **Task list** (GOV.UK) for long transactions done across sessions: verb-first task names; any order where possible; blocked tasks "Cannot start yet" (unlinked); fewest statuses (Completed / Incomplete); "Have you completed this section?" Yes / No, I'll come back later. Simplify the transaction first. (GOV.UK)
- One-thing-per-page suits low-frequency, external users; internal staff tools may combine questions when research shows repeat, rapid use. (GOV.UK)

## 12. Degraded forms

- Saving unavailable → keep fields and submit, show the form read-only, and explain in a dialog if they try to submit. (Primer)
- Nothing can be read → remove the form and explain why. (Primer)
- Some data failed to load → disable only those fields with an error under each. (Primer)
- Never disable controls because a backend is down without saying so; tooltips on disabled buttons aren't reachable. (Primer)
- Locked/inherited settings: read-only with a reason ("Managed by your organization"). (Pajamas, Notion) See `saas/accounts-and-permissions.md`.

## 13. Keyboard

- Enter submits single-line inputs (when there are no errors) — not textareas, and not search boxes inside dropdowns. (Pajamas)
- Ctrl/⌘+Enter submits from any control, including textareas. (Pajamas)
- Esc in a dialog form = Cancel (with unsaved-changes check). (ARIA APG dialog)
- Tab order follows visual order; no positive `tabindex`. (WCAG 2.4.3)

## 14. Time zone selector

- Detect and preselect the user's zone; sort by city alphabetically (not by offset); searchable; show country + offset per entry ("New York (Eastern Time) UTC−5"); handle DST automatically. (NN/g)
- Store IANA zone names, not fixed offsets. (Phil Nash; see `saas/global-and-performance.md`)

## 15. Accessibility essentials

- Every input has a programmatic `<label>`; groups use `<fieldset>`/`<legend>`. (WCAG 1.3.1, 3.3.2)
- Errors: `aria-invalid="true"` + `aria-describedby` to the message; move focus to the summary or first error; don't rely on live regions for validation. (Primer, WCAG 3.3.1)
- Fix suggestions when known (WCAG 3.3.3); prevention for legal/financial/data submits (WCAG 3.3.4); no redundant entry (WCAG 3.3.7); paste allowed in auth/OTP fields (WCAG 3.3.8).
- Accessible name contains the visible label. (WCAG 2.5.3)
- Save status ("Saved") announced via `role="status"`. (WCAG 4.1.3)
- Full details: `foundations/accessibility.md`.

## Common AI failures

- Placeholder used as the label; asterisks with no legend; every field marked required.
- Two-column forms of unrelated fields; every input full width.
- Errors shown on page load or on every keystroke before the user finished; Submit disabled with no explanation.
- Errors only in red, only in a toast, or a generic "Please fix the errors" banner with no links.
- Fields cleared after a server error.
- Toggle inside a form with a Save button (does it save now or on Save?).
- Autosave mixed with Save on the same settings page; autosave on billing or permission fields.
- 20-field create form in a modal; wizard with "Finish" and no review step.
- "Leave page?" fires when nothing changed, or never fires at all.
- Generic "Submit" / "OK" buttons instead of "Create project".

## Sources

- https://www.gov.uk/service-manual/design/form-structure
- https://design-system.service.gov.uk/patterns/question-pages/
- https://design-system.service.gov.uk/patterns/validation/
- https://design-system.service.gov.uk/components/error-summary
- https://design-system.service.gov.uk/components/error-message/
- https://design-system.service.gov.uk/components/button/
- https://design-system.service.gov.uk/patterns/check-answers/
- https://design-system.service.gov.uk/patterns/complete-multiple-tasks/
- https://designnotes.blog.gov.uk/2015/07/03/one-thing-per-page/
- https://primer.style/product/ui-patterns/forms
- https://primer.style/product/ui-patterns/saving
- https://primer.style/ui-patterns/degraded-experiences
- https://design.gitlab.com/patterns/forms/
- https://design.gitlab.com/patterns/saving-and-feedback/
- https://design.gitlab.com/patterns/settings-management
- https://cloudscape.design/patterns/general/errors/validation/
- https://cloudscape.design/patterns/general/unsaved-changes/
- https://cloudscape.design/patterns/resource-management/create/single-page-create/
- https://cloudscape.design/patterns/resource-management/create/multi-page-create/
- https://cloudscape.design/patterns/resource-management/edit/page-edit/
- https://cloudscape.design/patterns/general/disabled-and-read-only-states/
- https://patternfly.org/components/wizard/design-guidelines
- https://v5-archive.patternfly.org/patterns/filters/design-guidelines
- https://v10.carbondesignsystem.com/components/form/usage/
- https://carbondesignsystem.com/patterns/dialog-pattern
- https://spring-21.lightningdesignsystem.com/guidelines/data-entry
- https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/form-field-validation/usage
- https://www.sap.com/design-system/fiori-design-web/v1-151/ui-elements/dialog/usage
- https://www.sap.com/design-system/fiori-design-web/v1-71/page-types/floorplans/object-page/usage
- https://ant.design/docs/spec/data-entry
- https://www.cxpartners.co.uk/our-thinking/web_forms_design_guidelines_an_eyetracking_study/
- https://www.nngroup.com/articles/error-message-guidelines/
- https://www.nngroup.com/articles/time-zone-selectors/
- https://www.nngroup.com/articles/progressive-disclosure/
- https://www.nngroup.com/articles/complex-application-design/
- https://nngroup.com/articles/modal-nonmodal-dialog/
- https://www.nngroup.com/articles/info-tips-bad/
- https://slack.engineering/how-slack-rebuilt-notifications/
- https://philna.sh/blog/2021/02/22/display-dates-in-your-users-time-zone/
- https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry
- https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum
- https://w3.org/WAI/ARIA/apg/patterns/switch
- https://w3c.github.io/wai-website/ARIA/apg/patterns/dialog-modal/
