I've written the Members page as one self-contained HTML file with no dependencies. I haven't opened it in a browser or tested it yet.

**File:** `/tmp/claude-0/-tmp-ux-run2-7WRFI6/882ebbf6-be06-577b-985f-f27acad8a989/scratchpad/members.html`

**What's on the page**
- **Header:** A seat meter shows "x of 50 seats used", and Viewers don't count toward it. The primary action is "Invite members".
- **SSO banner:** It says sign-in is enforced through Okta and names the verified domains. This explains why invites work differently from a password-based product.
- **Tabs:** The page has Active and Pending invites tabs, with search and a role filter. The Pending tab offers Resend, Copy invite link and Revoke, and flags invites that are about to expire.
- **Active members table:** Each row has a role dropdown, a last-active column (with a "Never signed in" flag) and a row menu.
- **Bulk actions:** Selecting rows brings up a bar for changing roles or removing several people at once.

**Invite dialog**
- You enter emails as chips, and pasting a list works.
- Addresses outside the verified domains (acme.com, acme.io) are rejected, because those people couldn't sign in through SSO. The error says why.
- Duplicate and malformed addresses are caught too.
- Each role is shown with a one-line description of what it allows.

**Guardrails for roles and removal**
- The last Owner can't be demoted or removed, and you can't change your own role. A tooltip explains each case.
- Members whose role comes from an Okta group show a lock and an "Okta" tag, since the role has to be changed in Okta.
- Making someone an Owner needs confirmation.
- Removing someone needs a confirmation that says what happens: they lose access immediately and their content is reassigned. It also warns that removal doesn't deprovision them in Okta, and that Okta-synced people will be re-added on the next sync.
- Role changes, removals and revoked invites show an Undo toast.

It also has a dark mode that follows the system setting, keyboard navigation in the row menus, and a layout that works on narrow screens.

All data is mock data in the script, so nothing persists. The confirm dialog for making someone an Owner is the one I'd check first once you open it.
