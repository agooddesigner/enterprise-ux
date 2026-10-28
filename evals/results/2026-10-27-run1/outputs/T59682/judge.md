| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Members table with name, email, role, status | 1 | Table has Member (name+email), Role, Status columns |
| 2 | Role explanations | 1 | ROLES descriptions shown in invite dialog and role-change confirm |
| 3 | Invite flow with email + role | 1 | Invite dialog: email chips input and role select |
| 4 | Pending distinct from active | 1 | Pills "Invited"/"Invite expired", dashed avatar, sent text |
| 5 | SSO/SCIM acknowledged | 1 | Okta banner; "Set by Okta group", role locked |
| 6 | Remove confirmation naming person + consequence/undo | 1 | "Remove {name}?" with access lost, content stays; Undo toast |
| 7 | Last admin/owner protection | 1 | Last owner remove disabled; demote blocked with toast |
| 8 | No escalation / self-demotion handled | 1 | Own role select disabled: "You can't change your own role" |
| 9 | Seat/billing impact | 1 | Seat note in invite; "paid seats will be freed" on remove |
| 10 | Search or filter | 1 | Search input, status segment, role filter |
| 11 | Empty/single-member state | 1 | Empty div: "No members match… Clear filters"/"No members yet." |
| 12 | Auditable (audit log / last changed by) | 0 | Only "Audit log" nav link; no change attribution shown |
| 13 | Role change feedback without reload | 1 | applyRole re-renders and toasts "is now … (was …)" |
| 14 | Native controls with visible labels | 0 | Search and role filter labels are sr-only; not visible |
| 15 | Specific verb labels | 1 | "Invite members", "Remove member…", "Send invites" |

TOTAL: 13/15
