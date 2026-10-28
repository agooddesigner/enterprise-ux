| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Each role shows can AND cannot at point of choosing | 0 | Invite role shows one-line description; only some mention "Can't"; no systematic can/can't |
| 2 | Multi-email invite; invalid gets specific inline message; others kept | 1 | Chips; "Not a valid email address"/"Not in a verified SSO domain"; valid chips retained |
| 3 | Pending distinct, Resend/Revoke, expiry | 1 | "Invited" pill, "expires in 5 days", Resend invite / Cancel invitation menu |
| 4 | SSO/SCIM members read-only and labelled with source | 1 | "Set by Okta group …", disabled select, "Okta" tag |
| 5 | Remove confirm names person and states content/access | 1 | Names person; "Content they created stays"; "lose access immediately" |
| 6 | Last admin/owner demote/remove blocked with explanation | 1 | "Last owner. Assign another owner first." disabled; toast on demotion |
| 7 | Can't grant higher role OR self-role change prevented | 1 | Own role select disabled: "You can't change your own role" |
| 8 | Seat impact with number | 1 | "This invite uses N"; "14 seats available"; removal "N paid seats freed" |
| 9 | Disabled actions show reason on focusable element | 0 | Reasons are in small text/title; disabled buttons/select not focusable; the checkbox title is also on a disabled control |
| 10 | Suspend/deactivate separate reversible state | 0 | No suspend state exists |
| 11 | Last changed by/when or audit log entry | 0 | No audit info shown |
| 12 | Demote confirm or Undo; promote immediate with feedback | 1 | Undo toast on all role changes; Owner/Admin changes confirmed |
| 13 | Live region announcement and table updates without reload | 1 | `#toasts` aria-live="polite"; render() updates table |
| 14 | Visible labels in invite flow | 1 | Visible "Email addresses" and "Role" labels (label.l) |
| 15 | Non-admin viewer considered | 0 | No read-only or no-access view for non-admins |

TOTAL: 9/15
