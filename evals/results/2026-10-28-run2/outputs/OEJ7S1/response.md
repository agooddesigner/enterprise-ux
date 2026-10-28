I built the Members page as one self-contained HTML file (`/tmp/ux-run2/OEJ7S1/members.html`). I couldn't open it in a browser here, so I haven't run it. The only checks were a code read-through and fixing one bug where dialogs stacked event listeners. Please click through it before relying on it.

**Assumptions I made, since you didn't specify:**
- The company uses Okta for SSO and directory sync.
- Roles are Viewer, Member, Admin and Owner. Viewers don't use a paid seat.
- The signed-in user is an Admin.
- Seats are capped at 60.
- Invites expire after 7 days.

**How SSO shapes the page:**
- **Directory-managed members:** most of the 52 sample members come from Okta. Their role shows "Okta group `acme-members`", and Change role, Suspend and Remove are disabled with a visible reason. The reason tells the admin where to make the change (Okta or SSO settings).
- **Manually added members:** contractors and guests are marked External if they're outside the company domains. These can be changed, suspended and removed.
- **Invites:** invited people appear as rows with their expiry date and can be resent or revoked.
- **Status panel:** a banner on the page says that Okta SSO and directory sync are on, and how many members the directory manages.

**What admins can do:**
- **Invite:** paste several emails. Each address is checked live, and the page shows the seat impact for the chosen role.
- **Change role:** a role ladder with a description of each role. It warns that Admins can invite and remove people, and shows the seat change. An Undo toast follows.
- **Remove:** a confirmation that names the person and what happens (signed out immediately, seat freed). If they own projects, you must pick who takes them over. Removing several people at once also requires typing "remove".
- **Other actions:** suspend and reactivate are separate from removal and can be undone. Bulk actions skip ineligible people and say how many were skipped.
- **Finding people:** search, three filters, sortable columns and 25-row paging. All of it is kept in the URL hash, so views can be shared.

**Other states:** use the "Design preview" strip at the top to switch between loading, load error, no permission (with a request-access flow) and first use (only you). Filters with no matches show a clear-filters option.

The page is keyboard-operable and uses native dialogs, with dark mode and a narrow-screen layout.

I guessed some behaviour you should confirm: that suspending frees a seat, that an Owner can't be removed until ownership is transferred, and that the page never creates or edits users that Okta manages.
