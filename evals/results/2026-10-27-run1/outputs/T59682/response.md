I built the Members page as one self-contained HTML file: `/tmp/ux-eval-results/T59682/members.html`. I haven't opened it in a browser. My automated syntax check on the script was blocked, so no check of any kind has run.

**How SSO shapes the page**
- **Sign-in banner:** it says sign-in is managed by Okta, that there are no passwords, and that only @acme.com and @acme.io addresses can join.
- **Okta-synced members:** their role is locked and shows "Set by Okta group …". Their remove action is disabled and points to Okta instead.
- **Invites:** the invite dialog checks each address against the verified SSO domains and flags outsiders in red. The send button stays off until every address is valid.
- **Removal:** the confirmation notes that a removed member can't sign back in unless re-invited, even if they're still in Okta.

**Inviting**
- You enter addresses as chips; you can paste a list or separate them with commas or spaces.
- You pick a role and see its description.
- A seat note shows how many seats are free, and sending is blocked if there aren't enough. Viewers don't use a seat.

**Changing roles**
- Each row has an inline role dropdown. Changes to or from Owner or Admin ask for confirmation first; others apply immediately.
- Every change shows a toast with Undo.
- You can't change your own role. You can't demote or remove the last owner.

**Removing**
- Removal goes through a confirmation that says what happens: access ends immediately, their content stays, and the seat is freed.
- You can select several members and remove them in one go.
- Pending invitations get Resend, Copy link and Cancel instead.
- Removals also have an Undo toast.

**Finding people:** search by name or email, filter by status (All / Active / Invited) and by role. An empty result offers a "Clear filters" button.

**Display:** it follows the system light or dark setting and adapts down to phone width. Dialogs use the native `<dialog>` element, menus close with Esc, and controls have labels for screen readers.

The data is made-up sample data held in memory, so changes reset on reload.

I wrote the file directly instead of publishing it as an Artifact, since you asked for the HTML file.
