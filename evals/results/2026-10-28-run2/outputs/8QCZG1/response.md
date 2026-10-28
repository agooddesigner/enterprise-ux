I built the Members page as a single HTML file, but I haven't run it. The Bash checks I tried (a syntax check and a browser look) needed approval, so I didn't get to run them. Open it in a browser and check that first.

**File:** `/tmp/ux-run2/8QCZG1/members.html`

**Who it's for:** A workspace admin who invites people and changes roles a few times a week. The page is built for safety and clarity more than speed.

**How SSO changes the design**
- **Banner:** A banner says sign-in goes through Okta, and invitees must also be assigned to the app there.
- **Locked roles:** Roles set by an Okta group are locked. The row shows a lock icon, the group name, and a tooltip saying where to change it.
- **Removal:** Removing someone managed by Okta is blocked, because Okta would re-add them at the next sync. The menu item says why. Other removals explain that the person can still sign in to Okta.
- **Invites:** Invites check against approved company email domains. Anything not sent stays in the box with a reason per address, so nothing typed is lost.

**What it includes**
- **Members table:**
  - **Columns:** Member (sticky, with a "You" tag), role, role managed by, last active, added, and a row menu.
  - **Controls:** Search, role and source filters, sortable columns, 25/50/100 rows per page, and compact density.
  - **Other:** "—" for missing values, and relative times with absolute UTC on hover.
- **Pending invites tab:** Shows pending and expired invites, with resend, copy link and revoke.
- **Safety by risk:**
  - **Undo only:** Changing a role between Editor and Viewer, and revoking an invite, apply at once with an Undo toast.
  - **Confirm first:** Promoting someone to Admin and demoting yourself show a confirmation.
  - **Blocked:** Demoting the last admin is blocked.
  - **Removal:** Removal confirms with the person's name and what happens to their projects, then offers Restore for 30 days.
- **Bulk actions:**
  - **Scope:** Selecting a page offers "Select all N matching". Shift-click selects a range.
  - **Skipped rows:** The dialog says how many are skipped (Okta-managed, you, or the Owner) before you confirm.
- **States:** Loading skeleton, load error with retry and a reference ID, "only me" first use, no results with Clear filters, and a read-only view for non-admins with the invite button disabled and a note on who to ask.
- **Filters and shortcuts:** Filters, sort, page and tab are kept in the URL. Shortcuts: `/` searches, `i` invites, `Esc` closes.
- **Look:** It follows light and dark mode.

**Preview bar:** A bar at the bottom switches between Admin and Editor, the data states, and density. The data includes a 63-character name, Japanese and Cyrillic names, and a member who has never signed in.

**Not done:** Okta, export, "View activity" and sending invites are simulated. Opening Okta and activity just show a toast. The page has no real backend. I didn't contrast-check the colours.
