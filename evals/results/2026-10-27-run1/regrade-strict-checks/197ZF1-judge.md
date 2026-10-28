| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Roles show can/can't when choosing | 1 | Invite radios carry role descriptions, e.g. "Cannot create or edit". "Compare roles" matrix also exists. |
| 2 | Multi-email invite, specific inline error, other emails kept | 1 | Textarea accepts many addresses. Error lists the bad ones. Input is not cleared. |
| 3 | Pending invites distinct, Resend/Revoke, expiry | 1 | "Invited" badge, "Expires <date>", and menu items Resend invitation and Revoke invitation. |
| 4 | SSO/SCIM-managed read-only and labelled | 1 | Synced rows show a lock plus "Okta group eng-leads". |
| 5 | Remove confirmation names person, states content and access | 1 | The title names the person. The body covers sign-out, the project reassignment select, and the seat freed. |
| 6 | Last admin/owner removal or demotion blocked | 0 | No last-admin guard. Only self and owner restrictions exist. |
| 7 | No higher-role grant or self-role change | 1 | Own role shows "You can't change your own role"; the role select is not rendered. |
| 8 | Seat impact shown as a number | 1 | "Uses ${n} of ${free} available seats" on invite. "Removing frees N seats" on remove. |
| 9 | Disabled actions show the reason | 1 | Menu buttons use `aria-disabled` with `<small>` reason text, e.g. "You can't suspend yourself". |
| 10 | Suspend separate from remove and reversible | 1 | Suspend access and Restore access are separate menu actions, and suspend has an Undo toast. |
| 11 | Who changed a role and when, or visible audit entry | 0 | No actor/timestamp on role changes and no audit log entry is created. |
| 12 | Demote confirm or Undo; promote immediate with feedback | 1 | Role changes apply immediately and show a toast with Undo. |
| 13 | Live-region announcement and no-reload update | 1 | `#toasts` has `role=status` and `aria-live=polite`. `render()` updates the table. |
| 14 | Visible labels in invite form | 1 | Visible `<label>` for "Email addresses" and "Message", plus a Role legend. |
| 15 | Non-admin viewer considered | 1 | "No permission" state: "You need admin access to manage members". |

TOTAL: 13/15
