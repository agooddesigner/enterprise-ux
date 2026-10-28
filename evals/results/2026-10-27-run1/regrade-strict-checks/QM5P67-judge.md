| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Roles show can/cannot at choice point | 1 | Invite radios show descriptions, e.g. "Cannot manage members or settings" for Editor. |
| 2 | Multi-email invite, specific inline error, others kept | 1 | Chips; per-chip error list names address and reason; valid chips retained. |
| 3 | Pending distinct, Resend/Revoke, expiry | 1 | "Invitation pending", "expires in N d"; menu has Resend invitation, Revoke invitation. |
| 4 | SSO/SCIM read-only, labelled with source | 1 | Lock with tooltip "Role comes from the Okta group…"; Sign-in column "Okta (SCIM)". |
| 5 | Remove confirm names person and content/access effects | 1 | Title names person; "lose access immediately… content stays and is reassigned to you". |
| 6 | Last admin/owner removal/demotion blocked with explanation | 1 | Sole Owner role locked with reason; Remove disabled "Owners can't be removed". |
| 7 | Can't grant higher role OR self-change prevented/warned | 1 | Changing own role opens confirmation "Change your own role to…". |
| 8 | Seat impact shown with a number | 1 | "Seats 48 of 75 used"; invite hint "N valid · N seats free". |
| 9 | Disabled actions show reason on focusable element | 1 | Invite wrapper tabindex=0 data-tip; lock span tabindex=0; menu `.why` text. |
| 10 | Suspend/deactivate separate reversible state | 0 | No suspend/deactivate; only remove. |
| 11 | Last role change by/when or audit entry visible | 0 | No per-row changer info; audit log only a placeholder. |
| 12 | Demote needs confirm or Undo; promote immediate with feedback | 1 | setRole applies immediately with "is now X" toast and Undo. |
| 13 | Live region announcement and table updates without reload | 1 | `#toasts` role=status aria-live=polite; render() updates table. |
| 14 | Invite form fields have visible labels | 1 | Visible "Email addresses" label and "Role" legend. |
| 15 | Non-admin viewer considered | 1 | "Viewing as Editor" shows view-only banner, no controls, disabled Invite with reason. |

TOTAL: 13/15
