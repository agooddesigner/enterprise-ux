# Mode: Design

**Load when:** building a screen, flow or component (as code, mockup or written spec) for an enterprise/B2B product, or redesigning one.

Goal: produce a design that works for the real job, real data, every state and every role — not just the happy path in a screenshot.

---

## Step 0 — Intake (do this before drawing anything)

A senior designer asks before designing. So does this skill. The goal is the few answers that change the design, not a questionnaire.

### 0a. Look before you ask (silent)
- **Find the design system**: tokens/theme files, component library, Tailwind config, CSS variables, an existing screen, a Figma library. If found, the visual direction is **its own look** — don't ask style questions; only composition is open.
- **Read the request for answers already given** (users, data, roles, style words like "dark", "minimal", "playful", a reference product). Never re-ask what's stated.

### 0b. Ask what's still unknown — max 5 questions, in one go
**When to stop and ask:** the request is a whole screen, page or flow AND two or more of these are unknown — users & frequency, main job, data volume/roles, visual direction (when no design system). A one-line request like "design a dashboard for our CS team" always qualifies. In that case **ask and stop — don't build in the same reply**, even if your environment encourages starting immediately: a full build on wrong assumptions is expensive to redo, and the questions take the user ten seconds. Skip asking only when the request already answers them, the user said to proceed without them ("don't wait", "just build", "I'm away"), or nobody can answer (headless/scheduled run) — then go to 0c.

Ask only questions whose wrong answer is expensive. Multiple choice, each with a **recommended default** first. Use the host's question tool (e.g. AskUserQuestion) if available, otherwise a short numbered list.

**UX questions (pick the ones still open):**
| Question | Options (default first) | What the answer switches |
|---|---|---|
| Who uses this and how often? | Daily power users · Weekly operators · Occasional/admin · Execs/buyers (first look) | D1 density, shortcuts, guidance level, hero vs table-first |
| What's the main job on this screen? | Monitor & spot problems · Process a queue · Find & edit records · Configure · Present/report | Composition archetype (D8), primary action |
| How much data at p95? | Tens · Hundreds · Thousands+ · Unknown | Pagination vs virtual scroll, server filtering, bulk "select all N" |
| Who else sees it, with what rights? | Single role · Admin + member · Admin + member + viewer · Custom roles | Permission states, disabled-with-reason, hidden actions |
| Any hard constraints? | None · Must match existing product · Light+dark · Mobile too · Strict a11y/regulated | Modes, breakpoints, audit depth |

**Visual question (only if no design system was found):**
| Question | Options |
|---|---|
| Which direction? | Show 3–4 presets from `foundations/visual-direction.md` §2 that fit the context, each with a one-line description; recommended first. Also allow: "Mix" (lead preset + borrowed dials) and "Match a reference" (product name or screenshot). |

If the user picks a mix or reference, translate it into the dial notation from visual-direction §3 and confirm it in one line.

### 0c. If nobody can answer (headless run, user away, "just build it")
Don't stall. Pick defaults — UX from the request's context, direction from visual-direction §5 — and **start your reply with an Assumptions block** (its first lines, before anything else; also as a comment at the top of any file you write):
```
Assumed: daily operators · find & edit records · ~5k rows · admin + member + viewer
Direction: Classic enterprise (no design system found; CRM context) · light + dark
```
The user can correct one line instead of re-briefing.

### 0d. Lock it
Write the brief (purpose line + assumptions/answers) and the 3-line direction (visual-direction §7) at the top of the work. **Repeat the direction line in your reply to the user** — e.g. `Direction: lead Restraint; borrow Soft-bento composition (D8) for the KPI row. Mode: light + dark.` — so they can correct it in one line. Everything after is held to it.

---

## The design sequence

Do these in order. Each step names the reference to load.

### 1. Pick the page archetype → `patterns/navigation-and-layout.md`
List report, worklist, object/detail page, wizard, settings, dashboard, analytical page. Place it in the existing navigation; decide what lives in the URL.

### 2. Lay out structure before style
- Primary action and its placement; secondary actions; overflow. → `patterns/actions-and-dialogs.md`
- Content regions in order of decision value (what the user needs to decide *what to act on* comes first).
- Container choices: table vs list vs cards → `patterns/tables.md`; inline vs side panel vs modal vs page → `patterns/actions-and-dialogs.md`, `patterns/forms-and-saving.md`.

### 3. Fill with realistic data
- 50–200+ rows, long names, nulls, huge and negative numbers, non-Latin text, a 0, a 1.
- Real domain vocabulary ("Invoice INV-2041", "Acme Corp"), never lorem ipsum, "Item 1" or "Test User".

### 4. Design every state → `patterns/feedback-and-states.md`
Fill the state matrix for each view: ideal, first-use empty, no results, cleared, initial loading, refreshing, partial error, full error, no permission, read-only, degraded, overflow. Make each one reachable in the build (dev toggle, story, prop).

### 5. Design the interactions
- Filtering, search, saved views → `patterns/filters-and-search.md`
- Forms, validation, save model, unsaved changes, wizards → `patterns/forms-and-saving.md`
- Bulk actions, destructive actions, undo, confirmations, dialogs → `patterns/actions-and-dialogs.md`
- Dashboards and charts → `patterns/dashboards-and-dataviz.md`
- SaaS surfaces as needed: `saas/onboarding.md`, `saas/accounts-and-permissions.md`, `saas/billing.md`, `saas/notifications-system.md`, `saas/collaboration-and-audit.md`, `saas/integrations-and-data.md`, `saas/ai-features.md`, `saas/global-and-performance.md`

### 6. Write the copy → `foundations/writing.md`
Specific verb buttons, errors that say how to fix, no "successfully", sentence case, consistent terms.

### 7. Build accessibility in, not on → `foundations/accessibility.md`
Native elements first; keyboard paths; focus management for overlays; labels; contrast; status messages announced; target size ≥24px; click alternative for every drag.

### 8. Make it beautiful → `foundations/visual-direction.md` (+ `visual-craft.md` for polish, `visual-and-motion.md` for density/motion)
Apply the direction locked in Intake (preset or mix, written as dials) **before step 2's layout is coded**: composition by the job, hero first, size = importance, scale contrast and colour roles mapped onto the product's own tokens, UX states as designed as the ready state, then the render-and-look loop. When the user is still choosing, offer 2–3 labelled variants. Fallback tokens only if there's no design system.

### 9. Self-audit → `modes/audit.md`
Run the pre-ship checklist. Fix failures before presenting. Report a 3–5 line summary.

---

## Non-negotiables (break only with a stated reason)

1. Every list/view has empty, loading and error states — a blank area is a bug.
2. Every destructive action has Undo or a specific confirmation naming object + count + consequence.
3. Permissions are designed: hidden or disabled-with-reason, and say who can help.
4. Desktop tables stay tables (no card conversion "for a modern look"); numbers right-aligned with tabular figures.
5. Never lose user input: keep it after errors, warn on unsaved changes, autosave long drafts.
6. Errors: what happened + how to fix, near the source, no blame.
7. State in the URL: filters, sort, page, tab, open record.
8. Fully keyboard operable with visible focus; WCAG 2.2 AA.
9. One primary action per view; specific verb labels.
10. Unambiguous timestamps — absolute + time zone where it matters.
11. Colour never carries meaning alone.
12. Feedback within 100ms for every action; progress + cancel beyond 10s.

---

## Output requirements

### When writing code
- Use the project's components and tokens; match existing patterns.
- Seed realistic data (≥50 rows where lists exist, edge values included).
- Expose all states (prop, story or dev toggle) so they can be reviewed.
- Semantic HTML first: `<button>`, `<a href>`, `<table>`, `<label>`, `<dialog>`, landmarks; ARIA only where native doesn't exist.
- Filters/sort/pagination/open record reflected in the URL.
- No placeholder copy; real labels and messages.

### When writing a spec or mockup brief
Include:
- **Purpose line**: user, job, frequency.
- **Layout** with regions and action placement.
- **States table**: state × trigger × what the user sees × available action.
- **Interaction notes**: validation timing, save model, keyboard shortcuts, focus behaviour on open/close.
- **Permissions table**: role × visible/enabled/hidden per action.
- **Copy deck**: every label, message, empty state and error.
- **Accessibility notes**: roles/patterns used, focus order, announcements.
- **Acceptance criteria** written as testable statements.

### When reviewing your own output
End with the audit summary from `modes/audit.md` (what was checked, what was fixed, what's knowingly left).

## Common AI failures
- Skipping Intake: assuming the users, the data volume and the visual style instead of asking (or stating assumptions).
- Asking 10 open questions instead of ≤5 multiple-choice ones with defaults; re-asking what the request already said.
- Designing only the ideal state with perfect seed data.
- Inventing a new visual style next to an existing design system.
- Modal for everything; modals on top of modals.
- Centred spinner on a blank page for every load.
- Hover-only actions with no keyboard or touch path.
- Placeholder copy shipped as final.
- Treating accessibility as a closing checklist instead of building with native semantics.

## Sources
This mode routes to other files; each rule cites its source there. Full list: `references/sources.md`.
