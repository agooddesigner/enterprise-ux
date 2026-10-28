| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Roles show can/can't at point of choosing | 0 | ROLES descs mostly say can; only Viewer "Can't edit", Admin "Can't manage billing or SSO"; Member lacks cannot. |
| 2 | Multi-email invite; invalid gets specific inline message, others kept | 1 | Textarea parses many; err names invalid addresses; tokens/textarea retained. |
| 3 | Pending invites distinct with Resend/Revoke and expiry | 1 | Invited badge, "Expires <date>", menu Resend invite / Revoke invite. |
| 4 | SSO-managed read-only and labelled with source | 1 | "Okta group acme-members" with lock; actions disabled with Okta reason. |
| 5 | Remove confirm names person and states content/access consequences | 1 | Title names person; "signed out immediately", project transfer to heir. |
| 6 | Last admin/owner removal/demotion blocked with explanation | 0 | Owners can't be removed (explained), but demoting last Admin not blocked; no last-admin check. |
| 7 | Can't grant higher role or self-change prevented | 1 | canChangeRole blocks own role; Owner grant disabled "Only an owner can grant Owner". |
| 8 | Seat impact shown with number | 1 | "Uses 2 seats: X of 60 after sending"; "Frees 1 seat". |
| 9 | Disabled actions show reason on focusable element | 1 | Menu items aria-disabled buttons with visible reason text. |
| 10 | Suspend separate reversible state from remove | 1 | setSuspended/Reactivate with Undo; separate from Remove. |
| 11 | Shows who last changed role/when or audit entry visible | 0 | Audit log link only a stub toast; no entry created or shown. |
| 12 | Demotion confirm/Undo; promotion immediate with feedback | 1 | setRole toast with Undo; dialog applies immediately with toast. |
| 13 | Live-region feedback and table updates without reload | 1 | Toast role="status"; renderAll updates table. |
| 14 | Invite form fields have visible labels | 1 | Visible "Email addresses" label and "Role" legend. |
| 15 | Non-admin viewer considered | 1 | "noperm" view: "You need admin access" with request flow. |

TOTAL: 11/15
