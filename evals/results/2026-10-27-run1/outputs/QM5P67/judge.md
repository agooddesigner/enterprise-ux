| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Members table with name, email, role, status | 1 | Table: Member (name+email), Role, Status columns in row() |
| 2 | Each role has short explanation | 1 | ROLES descriptions shown in invite dialog role options |
| 3 | Invite flow with email + role selection | 1 | openInvite: chips email input plus Admin/Editor/Viewer radios |
| 4 | Pending status shown distinctly | 1 | "Invitation pending" hollow dot, sent/expires subtext |
| 5 | Acknowledges SSO/SCIM managed | 1 | Okta banner; lock on SCIM roles with group tooltip |
| 6 | Removal confirmation naming person + consequence, or undo | 1 | confirmDlg "Remove {name} from Acme?" loses access; Undo toast |
| 7 | Prevents/warns last admin removal/demotion | 1 | lockReason: sole Owner role can't change; Owner removal disabled |
| 8 | No escalation / self-demotion handled | 1 | changeRole self-demotion confirmDlg "Change your own role" |
| 9 | Seat/billing impact on invite/remove | 1 | Invite dialog "seats free", over-seat error; stats meter |
| 10 | Search or filter | 1 | Search input plus role/status/source filters |
| 11 | Empty/single-member state | 1 | "It's just you here so far" state |
| 12 | Auditable (audit log or last changed by) | 1 | Menu item "View activity in audit log" (placeholder) |
| 13 | Role change feedback without reload | 1 | setRole toast "X is now Role" with Undo |
| 14 | Native form controls with visible labels | 0 | Search, filter, and row role selects use sr-only/aria labels only |
| 15 | Specific verb labels | 1 | "Invite members", "Remove Name", "Send invitations" |

TOTAL: 14/15
