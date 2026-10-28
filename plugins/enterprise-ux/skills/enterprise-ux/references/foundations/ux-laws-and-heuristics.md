# UX laws and heuristics

**Load when:** auditing or critiquing a screen and you need to cite a specific law, heuristic or principle, rating the severity of a finding, or arguing a design decision from first principles.

How to cite: use the ID in the first column (e.g. "H5 Error prevention", "L-Fitts", "SG6", "N-Gulf-E", "CA3"). Every finding = ID + what you saw + severity (0–4) + fix. A violation is not automatically a fix; context decides (NN/g).

---

## 1. Audit lookup: symptom → what to cite

| Symptom on screen | Cite |
|---|---|
| No feedback after an action; spinner with no estimate or Cancel; stale dashboard with no "last updated" | H1, SG3, N-Feedback, L-Doherty |
| Database or engineering terms in labels ("AR_DOC", enum values) | H2, L-MentalModel |
| No undo, no cancel on long imports, no trash/restore | H3, SG6 |
| Same action named differently across modules ("Archive" vs "Deactivate") | H4, SG1, WCAG 3.2.4 (`foundations/accessibility.md`) |
| Destructive tenant-wide action with one click; or confirm dialogs on everything | H5, SG5, L-Fitts |
| User must remember IDs, filters or values from another screen | H6, SG8, L-WorkingMemory |
| Only a slow path exists, or only an expert path exists | H7, CA2, NNG user types |
| Decorative clutter competing with data; or needed data removed in the name of "clean" | H8, L-CognitiveLoad, CA6, CA8 |
| Raw error codes, stack traces, "Invalid input" | H9 (`foundations/writing.md`) |
| UI only usable after reading docs | H10, L-ActiveUser |
| Tiny adjacent edit/delete icons in dense rows | L-Fitts, WCAG 2.5.8 |
| Many equal-weight buttons, no primary | L-VonRestorff, L-Hick |
| Hover-only row actions, flat buttons that look like labels | N-Signifier, L-Similarity |
| Label floating between two fields; uniform spacing everywhere | L-Proximity |
| Boxes inside boxes ("card soup") | L-CommonRegion |
| Pretty prototype tested well, real task success low | L-AestheticUsability |
| Accepted input silently rewritten | L-Postel |
| Critical notice styled like a banner ad, or several simultaneous changes | L-SelectiveAttention |
| Forced tour or modal interrupting core work | L-Flow, CA1 |
| Wizard that can't skip back/forward without losing data | CA3, SG7 |
| Nav capped at 7 items "because Miller" | L-Miller (misuse) |

---

## 2. Laws of UX (all 30)

Format: law → enterprise application → misuse. Source: Laws of UX unless noted.

| ID | Law (core idea) | Apply in enterprise SaaS | Misuse to flag |
|---|---|---|---|
| L-AestheticUsability | Attractive UIs are perceived as easier to use (Kurosu & Kashimura 1995) | Polish earns trust in pilots and demos; still measure task success objectively | Looks hiding broken flows; polished prototypes masking problems in tests |
| L-ChoiceOverload | Too many options slow decisions and lower satisfaction | Plan/tier pickers, integration catalogs: side-by-side, recommended default, filters + search up front | Deleting options power users need; fix structure first |
| L-Chunking | Group content into meaningful units | Section a 40-field vendor form; format IDs/IBANs in groups | Arbitrary chunks; chunks with no hierarchy between them |
| L-CognitiveBias | Mental shortcuts cause systematic errors | Watch anchoring on pricing/quota screens; guard your own research synthesis with disconfirming questions | Using biases as dark patterns (fake scarcity in upgrade modals) |
| L-CognitiveLoad | Intrinsic load = the task; extraneous load = UI noise | Cut decoration and duplicate KPIs; keep intrinsic complexity experts need | "Simplifying" by removing data the analyst needs |
| L-Doherty | Productivity rises when response ≤ ~400ms (Doherty & Thadani 1982) | Optimistic saves in grids, skeletons for reports, background jobs + progress for long exports | Fake delays to look "thorough" (deliberate delay only, sparingly) |
| L-Fitts | Target time depends on distance and size | Primary row actions big enough; bulk actions next to the selection; destructive actions away from frequent ones | Tiny adjacent edit/delete icons → mis-clicks |
| L-Flow | Deep focus when challenge matches skill | Keyboard triage queues, low-friction inline edit, clear progress | Modals, nags, forced tours mid-task |
| L-GoalGradient | Effort speeds up near the goal | Onboarding checklist "3 of 5 done"; stepper progress | Fake progress; note human evidence is thinner than animal |
| L-Hick | Decision time grows with number/complexity of choices | Highlight the recommended option; split long config into steps | Over-simplifying into abstraction; doesn't apply to experts scanning familiar ordered lists |
| L-Jakob | Users expect your product to work like others they use | Follow table, filter, ⌘K and settings conventions (Salesforce, Jira, Workspace users); let users keep the old version during a redesign | Copying a convention that doesn't fit the domain; excuse never to innovate |
| L-CommonRegion | Items in a shared border/background read as a group | Panels to separate filters from results; form sections | Nested cards ("card soup") |
| L-Proximity | Close items read as related | Label tight to its field; row actions close to the row | Equal spacing everywhere; label halfway between fields |
| L-Pragnanz | Ambiguous shapes are read in their simplest form | Simple icons and chart shapes; no decorative complexity in data viz | Icons simplified until ambiguous |
| L-Similarity | Look-alike items read as a group | One link style; one status-chip colour+shape system | Static text styled like buttons; unlike items styled alike |
| L-UniformConnectedness | Visually connected items seem more related | Connector lines in workflow builders, approval chains, steppers | Decorative lines implying relationships that don't exist |
| L-MentalModel | Users carry a working model between systems | Model objects the way the customer's domain does; research via interviews and journey maps | Designing around the database schema |
| L-Miller | Working memory ~7±2, varies by person/context | Argument for chunking (grouped IDs, sectioned forms) | **Don't use "magic 7" to cap nav or menu length** — menus are recognised, not recalled |
| L-Occam | Fewest assumptions; remove until function breaks | Audit each settings element; remove what serves no job | Removing minority-critical features (audit, export) |
| L-ActiveUser | Users skip manuals and start doing (Carroll & Rosson 1987) | In-context help, teaching empty states, learn-by-doing onboarding (NN/g) | Assuming admins read a 40-page setup guide |
| L-Pareto | ~80% of effects from ~20% of causes | Polish the 20% of features driving most usage and tickets | Treating 80/20 as exact; dropping the compliance long tail |
| L-Parkinson | Work expands to fill time | Autofill org data, smart defaults, one-click repeat of last config | Citing it as science — it's satire, not research |
| L-PeakEnd | Experiences judged by peak and end (Kahneman 1993) | Make first-value moment and setup/migration end great; handle payment/import failures carefully | Polishing only the end; daily tools are judged on repeated use |
| L-Postel | Liberal in what you accept, conservative in what you send | Accept many date/phone/CSV formats, normalise, state limits, show what changed | Silently changing input in unexpected ways |
| L-SelectiveAttention | People filter out what seems irrelevant (banner/change blindness) | Don't style system alerts like ads; signal state changes clearly | Several simultaneous changes competing |
| L-SerialPosition | First and last items remembered best | Key nav items at start and end | Reordering stable nav to exploit it — breaks muscle memory (L-Jakob) |
| L-Tesler | Irreducible complexity only moves between system and user | System absorbs it via smart defaults, inference, validation | Hiding settings so users file tickets to change them |
| L-VonRestorff | The one different item is remembered | One primary CTA per view; highlight anomalies in tables | Emphasising many things; colour-only emphasis; motion that bothers sensitive users |
| L-WorkingMemory | ~4–7 chunks, fade in ~20–30s; recognition beats recall | Keep context visible across steps, side-by-side comparison, visited marks, breadcrumbs | Copy an ID on screen A to paste on screen B |
| L-Zeigarnik | Unfinished tasks are remembered | "Continue setup", draft indicators, cues that more content exists | Artificial incompleteness; guilt-driven red badges |

---

## 3. Nielsen's 10 usability heuristics

Final list 1994; unchanged at the 30th anniversary (NN/g).

| ID | Heuristic | Enterprise example | Misuse to flag |
|---|---|---|---|
| H1 | Visibility of system status | Sync status, job queues, "last updated" on dashboards | Spinner with no estimate or Cancel |
| H2 | Match between system and real world | "Invoice", not "AR_DOC"; natural task order | Internal/engineering jargon in labels and errors |
| H3 | User control and freedom | Undo after bulk edit, cancel long import, restore from trash | Confirm dialogs used instead of real undo |
| H4 | Consistency and standards | One design system across modules; same word = same action | Internal consistency that clashes with platform conventions |
| H5 | Error prevention | Constraints, inline validation, typed confirm for tenant-wide destructive actions | Over-confirming everything → users click through |
| H6 | Recognition rather than recall | Recent items, saved filters, autocomplete for entity IDs | Command-only UI with no discoverability |
| H7 | Flexibility and efficiency of use | Shortcuts, bulk actions, saved views, API | Expert-only paths as the only paths |
| H8 | Aesthetic and minimalist design | Progressive disclosure of advanced fields | "Minimalist" = stripping the density analysts need |
| H9 | Help users recognize, diagnose, recover from errors | "Row 42: date format not recognised. Use YYYY-MM-DD" + link to fix | Raw codes, stack traces |
| H10 | Help and documentation | Contextual help panels; admin docs linked from the screen | Docs used to excuse a bad UI |

### Severity scale (Nielsen)

| Score | Meaning | Action |
|---|---|---|
| 0 | Not a usability problem | None |
| 1 | Cosmetic | Fix if time allows |
| 2 | Minor | Low priority |
| 3 | Major | High priority |
| 4 | Catastrophe | Fix before release |

Rate on three factors: **frequency** (how often it occurs), **impact** (how hard to overcome), **persistence** (one-off or recurs every time). Nielsen also weighs market impact (verify — as of Oct 2026). Heuristic: an issue that is frequent + hard to overcome + persistent on a core workflow is a 3–4; a rare, easily bypassed, one-time annoyance is 1 (general practice).

### Running a heuristic evaluation (NN/g)
- Scope first: one task, area, user group or device. Pick a logging format.
- 3–5 evaluators, independently, ~1–2h each: pass 1 to learn the product, pass 2 to log violations. No sharing until done.
- Consolidate by affinity clustering; debrief on agreements, worst and business-critical issues, and what needs user testing.
- It complements user testing; it never replaces it. Don't present findings as validated user data. Always rate severity — an unrated list is unprioritised.
- When you (an AI) audit alone, say so: a single-evaluator pass misses many problems (NN/g; classic coverage figures verify — as of Oct 2026).

---

## 4. Shneiderman's 8 Golden Rules

| ID | Rule | Enterprise application |
|---|---|---|
| SG1 | Strive for consistency | Shared table, filter, bulk-action patterns across modules |
| SG2 | Seek universal usability | Novices and experts, all abilities and cultures: role-based density, localisation, WCAG |
| SG3 | Offer informative feedback | Proportional: toast for a save; summary report for a tenant migration |
| SG4 | Design dialogs to yield closure | Import wizard ends on a results summary with next steps |
| SG5 | Prevent errors | Block invalid options; on error give the specific fix and name the fields |
| SG6 | Permit easy reversal | Undo, version history, soft delete |
| SG7 | Keep users in control | Predictable layouts; no AI changes auto-applied without consent |
| SG8 | Reduce short-term memory load | Persistent context panes; don't carry info between screens |

(Shneiderman.) Rule 2 was "enable shortcuts for frequent users" in earlier editions (verify — as of Oct 2026). Misuse: ticking the list without task context. Note SG5's "grey out invalid options" conflicts with the house rule on submit buttons — keep Save/Submit enabled and explain errors on click (see `foundations/defaults.md`).

---

## 5. Norman's principles

| ID | Concept | Use in an audit |
|---|---|---|
| N-Affordance | What actions the environment makes possible (Gibson); Norman says the term is widely misused | Don't argue "it affords clicking" — argue whether it's *signified* |
| N-Signifier | Any perceivable cue telling users what's possible; designers provide signifiers | Flag hover-only actions, flat buttons indistinguishable from labels, missing drag handles, no scroll cue |
| N-Mapping | Controls' relation to effects is obvious | Filter panel order mirrors column order; spatial controls for spatial layouts |
| N-Constraints | Limit actions to those that make sense now | Date pickers blocking invalid ranges; role-based disabling *with* a reason |
| N-Feedback | Full, continuous feedback about actions and state | Pair with H1 |
| N-Model | The system image lets users form a correct conceptual model | Flag UIs mirroring the schema instead of the user's model (L-MentalModel) |
| N-Gulf-E | Gulf of execution: gap between intent and the actions the system allows | "User knows what they want but can't find how" |
| N-Gulf-V | Gulf of evaluation: how well the system shows its state for interpretation | "User acted but can't tell what happened" |

**7 stages of action:** goal → plan → specify → perform (bridge execution) → perceive → interpret → compare (bridge evaluation). For each failing task, name the stage and gulf that broke (Norman).

---

## 6. Gestalt principles

| Principle | Enterprise use | See |
|---|---|---|
| Proximity | Label–field spacing, row-action grouping | L-Proximity |
| Similarity | Consistent link, chip, button styling | L-Similarity |
| Common region | Panels, form sections | L-CommonRegion |
| Uniform connectedness | Workflow connectors, steppers | L-UniformConnectedness |
| Prägnanz | Simplest reading wins; simple icons and charts | L-Pragnanz |
| Continuity | Eye follows lines: aligned columns and form edges | (general practice) |
| Closure | Mind completes shapes: skeleton loaders work because of it | (general practice) |

(Laws of UX groups these as Proximity, Similarity, Continuity, Closure, Connectedness, with Common Region and Prägnanz.)

---

## 7. NN/g: 8 guidelines for complex applications

| ID | Guideline | Don't |
|---|---|---|
| CA1 | Promote learning by doing: safe exploration, no lost work, quick results (live preview) | Make trial-and-error the only path in safety-critical domains |
| CA2 | Teach faster methods in context (tooltip mentioning the shortcut) | Count on manuals — users keep slow habits |
| CA3 | Flexible pathways: skip, loop back, jump between steps without losing progress | Rigid linear flows |
| CA4 | Let users annotate data, charts and models to resume after interruptions | Force users to keep notes elsewhere |
| CA5 | Connect to tools users have: export to Excel/PPT, copy chart as image | Make users screenshot or re-key data |
| CA6 | Reduce clutter without reducing capability: staged disclosure | Remove features for "simplicity" |
| CA7 | Show secondary details in place (hover a chart point for the exact value) | Send users to another screen for a detail |
| CA8 | Make important things salient by removing non-essentials (no decorative icons on KPIs) | Rely only on more colour or bold |

(NN/g)

### NN/g complex-app user types — design for all three

| Type | Who | Design for them | Trap |
|---|---|---|---|
| Legacy | Long-time users who never got efficient; rely on workarounds | Gradual rollouts, early announcements, old views kept during transition, discoverable shortcuts | Big-bang redesigns |
| Legend | Expert power users | Keep optimising; add advanced features without hurting core usability | Letting their preferences override everyone else |
| Learner | Domain experts new to the tool | Inline/just-in-time help, sandboxes, templates, errors with next steps | Leaning on training and docs |

(NN/g) Also: research the domain (terms, roles, constraints, interruptions, handoffs) before the tool; test how users reason, not just whether they finish (NN/g).

---

## 8. Ant Design's 4 values

| Value | Means | Check |
|---|---|---|
| Natural | Lower cognitive and physical effort | Pre-filled defaults, suggested next action, automated repetition |
| Certain | Low "cooperative entropy" | Shared components/tokens; only what each screen needs; consistent across products |
| Meaningful | Primary task obvious; complex work split into sub-goals; immediate feedback | Is the main job of the screen clear in 5 seconds? (general practice) |
| Growing | Advanced features discoverable | Hints and progressive disclosure, not hidden menus |

(Ant) Ant's 10 interaction principles: proximity, alignment, contrast, repetition, make it direct, stay on the page, keep it lightweight, provide an invitation, use transition, react immediately (Ant).

---

## 9. GOV.UK government design principles

1. Start with user needs — evidence, not assumptions.
2. Do less — reuse platforms and patterns; build only what's unique.
3. Design with data — let usage data shape decisions.
4. Do the hard work to make it simple — absorb complexity (pairs with L-Tesler).
5. Iterate — ship small, improve continuously.
6. This is for everyone — design for the hardest-to-serve first.
7. Understand context — where, when and on what device people use it.
8. Build digital services, not websites — the whole journey, including offline steps.
9. Be consistent, not uniform — shared patterns, adapted where context demands.
10. Make things open — share code, designs and decisions.
11. Minimise environmental impact.

(GOV.UK)

---

## Common AI failures
- Citing a law with no observation ("violates Hick's Law") — always state what on the screen breaks it and the fix.
- Using Miller's 7±2 to cap nav items, tabs or menu options.
- Treating "minimalist" (H8) as licence to strip data density experts need (CA6, L-CognitiveLoad).
- Recommending confirm dialogs everywhere as "error prevention" instead of undo (H3, H5).
- Optimising only for Legends or only for Learners; ignoring Legacy users in redesigns.
- Listing findings without severity, or rating everything 3–4.
- Claiming a heuristic review "validates" a design; it doesn't replace user testing.
- Citing Parkinson's Law or Goal-Gradient as hard science.
- Confusing affordance with signifier ("this button has no affordance" — it lacks a signifier).
- Citing SG5 to disable Submit; the house rule keeps it enabled with explained errors (`foundations/defaults.md`).

## Sources
- https://lawsofux.com/index.md
- https://lawsofux.com/millers-law/index.md
- https://lawsofux.com/jakobs-law/index.md
- https://lawsofux.com/articles/2018/the-psychology-of-design
- https://lawsofux.com/doherty-threshold/
- https://lawsofux.com/teslers-law/
- https://lawsofux.com/fittss-law/
- https://lawsofux.com/hicks-law/
- https://lawsofux.com/peak-end-rule/
- https://lawsofux.com/aesthetic-usability-effect/
- https://lawsofux.com/postels-law/
- https://lawsofux.com/von-restorff-effect/
- https://lawsofux.com/goal-gradient-effect/
- https://lawsofux.com/zeigarnik-effect/
- https://lawsofux.com/cognitive-load/
- https://lawsofux.com/choice-overload/
- https://lawsofux.com/selective-attention/
- https://lawsofux.com/serial-position-effect/
- https://lawsofux.com/chunking/
- https://lawsofux.com/flow/
- https://lawsofux.com/parkinsons-law/
- https://lawsofux.com/pareto-principle/
- https://lawsofux.com/occams-razor/
- https://lawsofux.com/mental-model/
- https://lawsofux.com/working-memory/
- https://lawsofux.com/cognitive-bias/
- https://lawsofux.com/law-of-common-region/
- https://lawsofux.com/law-of-proximity/
- https://lawsofux.com/law-of-similarity/
- https://lawsofux.com/law-of-uniform-connectedness/
- https://lawsofux.com/law-of-pr%C3%A4gnanz/
- https://www.nngroup.com/articles/paradox-of-the-active-user/
- https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/
- https://www.dsoergel.com/794/NielsenUsability.pdf
- https://www.cs.princeton.edu/courses/archive/spring13/cos436/handouts/Heuristics_explained.pdf
- https://jakobnielsenphd.substack.com/p/usability-heuristics-history
- https://www.cs.umd.edu/~ben/goldenrules.html
- https://jnd.org/signifiers-not-affordances/
- https://community.mis.temple.edu/mis3506sec750spring2023/files/2023/02/UXFall-2022-Gulfs-1.pdf.pdf
- https://www.nngroup.com/articles/complex-application-design/
- https://www.nngroup.com/articles/complex-apps-users/
- https://www.nngroup.com/articles/strategies-complex-application-design/
- https://ant.design/docs/spec/values
- https://ant.design/docs/spec/introduce
- https://gov.uk/guidance/government-design-principles
