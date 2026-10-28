| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Roles show can AND cannot at choosing point | 0 | Invite descriptions mostly say what's allowed; only "No billing", "Can't manage people" partial. Owner not offered; row dropdown has no descriptions. |
| 2 | Multi-email; invalid gets specific inline message; others kept | 1 | Chips; domain error names address; other chips retained |
| 3 | Pending distinct, Resend/Revoke, expiry | 1 | Pending tab; Resend button, Revoke in menu; "Expires tomorrow" pill |
| 4 | SSO-managed read-only and labelled with source | 1 | Lock plus "Okta" tag, title "Role is set by the Okta group" |
| 5 | Remove confirm names person AND content/access | 1 | "Remove ${name}?"; lose access, content reassigned to you |
| 6 | Last admin/owner block with explanation | 1 | "Can't remove every Owner"; lock title "need at least one Owner" |
| 7 | Can't grant higher role OR own role change prevented | 1 | Own role locked: "You can't change your own role." |
| 8 | Seat number shown on invite/remove | 0 | Seat meter in header only; not shown in invite or remove flow. |
| 9 | Disabled actions show reason | 1 | Disabled menu item has title "Promote another Owner first"; lock titles |
| 10 | Suspend/deactivate separate reversible state | 0 | No suspend feature present. |
| 11 | Last role change by/when or audit entry | 0 | No such display; "View activity" is just a toast stub. |
| 12 | Demotion confirm/Undo; promotion immediate with feedback | 1 | Role change shows Undo toast; Owner promotion confirmed |
| 13 | Live region feedback; table updates without reload | 1 | toasts aria-live="polite"; render() updates the table |
| 14 | Invite form visible labels | 1 | Visible `<label for="invIn">Email addresses`; Role legend |
| 15 | Non-admin viewer considered | 0 | No read-only or no-access view for non-admins. |

TOTAL: 9/15
