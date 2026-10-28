# Mode: Audit

**Load when:** reviewing, critiquing or auditing an existing screen, flow, prototype, codebase UI or a design you just produced ("review this", "what's wrong with…", "audit for accessibility", "is this ready to ship?"). Also used as the final step of Design mode.

Goal: find the problems that cost users the most, rate them honestly, and say exactly how to fix each one — with the rule or source behind it.

---

## Pick the depth

| Request | Depth | Output |
|---|---|---|
| "Quick look", screenshot, single screen | **Quick review** | Top 3 issues (impact-ranked) + up to 5 minor notes |
| "Audit", "ready to ship?", a flow or feature | **Full audit** | Findings table with severity, grouped by lens, + summary |
| "Accessibility audit" | **A11y audit** | WCAG 2.2 AA pass by SC + keyboard + screen-reader checks |
| Your own design in Design mode | **Pre-ship self-check** | 3–5 line summary of checked / fixed / knowingly left |

---

## Process (full audit)

1. **Scope.** Which screens/flows, which roles, which devices, which standard (WCAG 2.2 AA by default).
2. **Name the tasks.** 3–5 key jobs per role. You're evaluating whether *those* get done well, not judging taste.
3. **First pass — learn the product.** Walk each task as each role. Note where you hesitated.
4. **Second pass — through the lenses below.** Log every violation separately, with location.
5. **Cognitive walkthrough for new-user tasks.** At each step ask: Will the user try to do this? Will they notice the correct control? Will they understand it does what they want? Will they see progress after acting? (Wharton et al.)
6. **Locate the gulf.** For each failure decide: can't figure out *how* to act (gulf of execution) or can't tell *what happened* (gulf of evaluation)? The fix differs. (Norman)
7. **Rate severity** (scale below), consolidate duplicates, rank.
8. **Prescribe fixes** — specific, with the reference file/rule.

Heuristic review complements user testing; it doesn't replace it. Recommend testing with ~5 users per distinct role for anything rated 3–4. Single-reviewer audits miss problems — say so when you're the only evaluator. (NN/g)

---

## Severity scale (Nielsen 0–4)

Rate by **frequency** (how many users/how often), **impact** (how hard to overcome), **persistence** (one-time or every time).

| Score | Meaning | Typical enterprise examples |
|---|---|---|
| 4 Catastrophe | Fix before release | Irreversible bulk delete with no confirm/undo; data loss on error; keyboard trap; core task impossible for a role |
| 3 Major | High priority | No empty/error state; filters lost on refresh; errors with no fix; contrast failures on primary text; disabled button with no reason |
| 2 Minor | Low priority | Inconsistent labels; misaligned numbers; vague button verbs; missing hover timestamp |
| 1 Cosmetic | Fix if time | Spacing off-scale; icon inconsistency |
| 0 Not a problem | — | Reviewer preference only |

Never inflate severity to sound thorough; never deflate a 4 to be polite.

---

## Lenses (checklist)

Work through the lenses relevant to the scope. Each item names where the rule lives.

### A. Job fit & IA
- [ ] Primary action for the main job is the most prominent element; one primary per view. (`patterns/actions-and-dialogs.md`)
- [ ] Page archetype fits the job (list report, worklist, object page, wizard, dashboard). (`patterns/navigation-and-layout.md`)
- [ ] User always knows where they are (active nav, title = last breadcrumb). 
- [ ] High-frequency tasks are fast: density, keyboard, bulk, saved views; low-frequency tasks are guided.
- [ ] Domain vocabulary, not system/database terms. (Nielsen #2)

### B. Nielsen's 10 heuristics (cite the number)
1 Visibility of status · 2 Match real world · 3 User control & freedom · 4 Consistency & standards · 5 Error prevention · 6 Recognition over recall · 7 Flexibility & efficiency · 8 Aesthetic & minimalist · 9 Error recovery · 10 Help & docs. (`foundations/ux-laws-and-heuristics.md`)

### C. Data realism
- [ ] Works with 0, 1, and p95 volume; pagination/virtualisation present. (`patterns/tables.md`)
- [ ] Long values truncate with full value available; nulls show a consistent "—"; real 0 shows 0.
- [ ] Numbers right-aligned, tabular figures, consistent decimals and units; dates unambiguous.

### D. States (`patterns/feedback-and-states.md`)
- [ ] First-use empty, no-results, loading, refreshing, error, no-permission, read-only all exist and are distinct.
- [ ] "No data" is never shown while loading or when loading failed.
- [ ] Partial failure is contained to the failing section; page still usable.
- [ ] Refresh keeps old data visible; long jobs show progress, cancel and run in background.

### E. Actions & safety (`patterns/actions-and-dialogs.md`)
- [ ] Destructive actions: Undo, or confirmation naming object + count + consequence; typed confirm for critical/cascading.
- [ ] Destructive controls separated from frequent ones (Fitts's Law); never styled like Save.
- [ ] Bulk actions state scope and report succeeded/failed/skipped.
- [ ] Disabled controls explain why; hidden only when never available to that role.
- [ ] No modal on modal; dialog focus in, trapped, returned on close.

### F. Forms & saving (`patterns/forms-and-saving.md`)
- [ ] Visible labels (no placeholder-as-label); optional/required convention consistent.
- [ ] Validation timing sensible; error summary + focus on submit; input kept after errors.
- [ ] Submit not disabled to signal errors; double-submit prevented.
- [ ] One save model per form; unsaved-changes warning only when changed.

### G. Filters & navigation state (`patterns/filters-and-search.md`)
- [ ] Applied filters visible as removable chips with Clear all; result count shown.
- [ ] Filters, sort, page, tab, open record in the URL; Back works.

### H. Permissions & SaaS surfaces (`saas/*`)
- [ ] Each role walked through; locked/managed settings say who controls them.
- [ ] Current org/workspace (and test vs production environment) always visible; scope stated on admin pages.
- [ ] Session timeout warns and preserves unsaved input (2.2.1).
- [ ] Audit trail for sensitive changes; timestamps absolute + zone there.
- [ ] Notifications respect preferences; no critical info only in a toast.
- [ ] AI output labelled, explainable, correctable, undoable.
- [ ] Billing/cancellation free of dark patterns.

### I. Accessibility — WCAG 2.2 AA (`foundations/accessibility.md`)
- [ ] Keyboard: everything reachable and operable, logical order, visible focus, no traps, Esc closes overlays.
- [ ] Focus not obscured by sticky headers, toasts, banners (2.4.11).
- [ ] Targets ≥24×24 CSS px or spaced (2.5.8); drag has single-pointer alternative (2.5.7).
- [ ] Contrast: text 4.5:1 (large 3:1); UI parts, focus, chart elements 3:1.
- [ ] Names/roles/states correct; native elements first; tables use `<table>` unless truly spreadsheet-like.
- [ ] Status messages announced without moving focus (4.1.3); errors identified in text with fix (3.3.1, 3.3.3).
- [ ] Reflow at 320px / 400% zoom; text spacing overrides don't break layout.
- [ ] No re-entry of info already given in the same process (3.3.7); login allows paste/password managers (3.3.8).
- [ ] Automated scan run **and** manual keyboard + screen-reader smoke test — automated tools catch only part of the issues.

### J. Content (`foundations/writing.md`)
- [ ] Specific verb buttons; no OK/Submit/Yes; sentence case.
- [ ] Errors: what + how to fix; no "invalid", "oops", "please", blame.
- [ ] No "successfully"; no lorem ipsum; consistent terms across screens.

### K. Visual quality & performance (`foundations/visual-craft.md`, `foundations/visual-and-motion.md`, `saas/global-and-performance.md`)
- [ ] Looks premium: one focal point, ≤4 type sizes, neutrals + one accent, aligned grid, subtle consistent surfaces, no generic-AI tells (`visual-craft.md` checklist).
- [ ] Density consistent app-wide; spacing on 4/8px scale; colour used for meaning.
- [ ] Feedback within 100ms; motion restrained; `prefers-reduced-motion` honoured.
- [ ] Layout survives text expansion; time zones labelled.

---

## Output format

### Quick review
```
Top issues
1. <Problem> — <who it hurts and how> → <fix>. (<rule/source>) [Sev 3]
2. …
3. …

Also: <up to 5 one-line minor notes>
```

### Full audit
```
# UX audit: <product/flow> — <date>
Scope: <screens, roles, standard>   Evaluator(s): <n>

Summary: <3–5 lines: overall readiness, the 3 biggest risks, recommendation>

| # | Sev | Location | Problem | Why it matters (rule) | Fix |
|---|---|---|---|---|---|
| 1 | 4 | Invoices › Bulk delete | Deletes 1–10k rows with no confirm or undo | Irreversible data loss (Nielsen #3, #5; Cloudscape delete tiers) | Soft delete + 30-day restore, or typed confirm naming count |
| … |

Accessibility: <pass/fail by SC for A/AA issues found>
What works well: <max 3 bullets — only if genuinely useful to keep>
Recommended next steps: <fix order; what to user-test, with which roles>
```

Lead with impact, not with praise. Don't pad. If something is a matter of taste, say so or leave it out.

## Common AI failures
- Listing 40 equal-weight nitpicks instead of ranking by severity.
- Aesthetic opinions presented as usability problems.
- Saying "consider improving X" with no concrete fix.
- Citing a heuristic number without explaining the user impact.
- Declaring a screen "accessible" from an automated scan alone.
- Softening a catastrophic issue to be polite.

## Sources
This mode routes to other files; each rule cites its source there. Full list: `references/sources.md`.
