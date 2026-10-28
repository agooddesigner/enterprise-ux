| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Role choice shows can and cannot | 0 | ROLE_DESC gives short text, but no matrix; the Viewer text states only what it can do. Only the Editor text has "Can't manage members", so most roles show no can't. |
| 2 | Multi-email invite, specific inline error, valid kept | 0 | Multi-email and specific errors are present, but the code keeps only the bad addresses (`ta.value=bad.map...`). Valid ones are sent and removed, so "other emails are kept" is not met. |
| 3 | Pending invites distinct, with Resend, Revoke, expiry | 1 | Separate Pending invites tab; Resend button, Revoke in menu, "Pending · expires" status. |
| 4 | SSO-managed read-only and labelled with source | 1 | Role cell is locked with a lock icon, and the "Role managed by" column shows "Okta group ws-…". |
| 5 | Remove confirm names person and states content and access | 1 | "Remove ${m.name}"; "loses access immediately… projects transferred to you". |
| 6 | Last admin block with explanation | 1 | Dialog "Can't remove the last admin" with explanation. |
| 7 | Can't grant higher than own, or self-change prevented/warned | 1 | Self-demotion shows a "Remove your own admin access?" warning; the role select is locked for self. |
| 8 | Seat impact with a number | 1 | "${left} of ${SEAT_LIMIT} seats left" in the invite dialog. |
| 9 | Disabled actions show reason on a focusable element | 1 | Menu item with aria-disabled shows a hint; the locked role has a title. |
| 10 | Suspend/deactivate separate from remove | 0 | No suspend or deactivate feature. |
| 11 | Who last changed the role and when, or audit log | 0 | No last-changed-by display; the audit log is only mentioned in text. |
| 12 | Demote needs confirm or Undo; promote immediate with feedback | 0 | Demotion has Undo, but promotion to Admin requires a confirm dialog, not immediate. The check wants promote immediate, so this fails. |
| 13 | Live region announcement and table updates without reload | 1 | `#toasts` has role="status" aria-live="polite"; `render()` updates the table. |
| 14 | Invite form fields have visible labels | 1 | `label.l` visible labels for the emails and role fields. |
| 15 | Non-admin viewer considered | 1 | Editor viewer mode: no checkboxes, invite disabled with a title, "View only". |

TOTAL: 9/15
