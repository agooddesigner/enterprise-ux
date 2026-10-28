| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Members table with name, email, role, status | 1 | Table columns Member (name+email), Role, Status badge |
| 2 | Each role has short explanation | 1 | ROLES desc in invite radios; Compare roles matrix |
| 3 | Invite flow with email entry + role selection | 1 | inviteDialog: textarea emails, radio role options |
| 4 | Pending status shown distinctly | 1 | `.badge.invited` with ✉ icon, "Expires" date |
| 5 | Acknowledges SSO/SCIM | 1 | Banner; synced roles locked with "Okta group" label |
| 6 | Remove confirmation naming person + consequence, or undo | 1 | "Remove X from Acme Corp?" signed out, lose access |
| 7 | Prevents/warns removing/demoting last admin | 0 | No last-admin check; only self/owner blocks |
| 8 | No escalation or self-demotion handled | 1 | "You can't change your own role"; only owners touch owners |
| 9 | Seat/billing impact on invite/remove | 1 | "Uses n of N available seats"; "Removing frees 1 seat" |
| 10 | Search or filter | 1 | Search input plus role/status/sign-in filters |
| 11 | Empty/single-member state | 1 | "You're the only member" state |
| 12 | Auditable (audit log / last changed by) | 0 | Only sidebar "Audit log" link; no change attribution |
| 13 | Role change feedback without reload | 1 | changeRole shows toast "role is now…" with Undo |
| 14 | Native form controls with visible labels | 0 | Table role selects and filters use sr-only labels |
| 15 | Specific verb labels | 1 | "Invite members", "Remove member", "Make admin" |

TOTAL: 12/15
