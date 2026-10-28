The Members page is written as a single HTML file, but I haven't run it. My syntax check needed approval and didn't run, and I haven't opened the page in a browser. Treat it as unverified until you've loaded it once.

Open `/tmp/ux-eval-results/QM5P67/members.html` in a browser.

**Who it's for:** a workspace admin who invites, re-roles and removes people a few times a week and wants to do each in under a minute without breaking anyone's access.

**What the SSO setup changes**
- **Banner:** a banner says sign-in is managed by Okta SSO and that invites only work for the verified domains acme.com and acme.io.
- **Invite check:** the invite dialog rejects other domains with the reason, plus duplicates, existing members and addresses beyond your free seats. Pasting a list of addresses works.
- **Role locks:** people synced from Okta get their role from an Okta group, so their role shows as locked. The tooltip names the group and says to change it in Okta.
- **Removal warning:** removing a synced person warns that Okta will re-add them on the next sync unless they're unassigned from the app there.
- **Invites:** pending invites sit in the same list, with resend, copy link and revoke.

**Safety**
- **Role changes:** a role change applies immediately and shows an Undo toast.
- **Removal:** removing someone opens a confirmation that names the person and what they lose, with Cancel focused by default. After you confirm, an Undo toast appears.
- **Bulk actions:** the bar says how many are selected and lets you "Select all N matching". The bulk dialog lists who will be skipped.
- **Guards:** you can't remove yourself or the sole Owner. Lowering your own role asks for confirmation first.

**States and permissions**
- **Prototype toggle:** a toggle at the bottom-left switches between Loaded, Loading, Server error and First use (you're the only member). It also switches between Admin and Editor, where the Editor sees a read-only page with an explained, disabled Invite button.
- **Filtering and sorting:** search, filters, sort and page number are kept in the URL. Filtering to nothing shows a different empty state with "Clear filters".
- **Shortcuts:** `/` focuses search and `I` opens the invite dialog.

The data has 56 rows, including very long names, a non-Latin name, people who have never signed in, and invites that haven't been accepted yet. The page follows light and dark mode.

**Not built, by choice:** creating a new Okta group, ownership transfer and the audit log page. The menu links to the audit log, but that link is only a placeholder message.
