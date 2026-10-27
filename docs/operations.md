# Operations

## Setup

1. Install and authenticate Hermes using its official installation and setup flow.
2. Create one profile per durable role. Do not reuse a profile for two roles.
3. Create one Discord application and bot per role. Enable Message Content intent and, if usernames or roles are used for authorization, Server Members intent.
4. Store each bot token only in that profile's `.env` or secret store.
5. Configure a user, role, or channel allowlist before starting its gateway.
6. Create the workplace channels and invite only the required bot.
7. Start each gateway and send one direct test message from an authorized user.
8. Create the sample project thread and run the acceptance checks below.

Record the Hermes version with `hermes --version` and the documentation date before using this guide operationally.

## Verification

- `hermes profile list` shows the expected roles and no accidental extra profile.
- Each role responds only in an authorized DM, workplace, or assigned project thread.
- A message in another role's channel does not receive a response from the wrong bot.
- A fresh project thread does not contain another project's private transcript.
- `group_sessions_per_user` has the intended value, and its consequence was tested with two users when shared context is enabled.
- A role cannot describe another role's token, `.env`, session history, or local files.
- The project handoff distinguishes completed checks from unchecked claims.

## Troubleshooting

| Observation | First checks |
|---|---|
| Bot is offline | Gateway process, token validity, and Discord privileged intents |
| Bot is online but silent | Allowlist, channel permission, mention requirement, and gateway log |
| Bot answers in the wrong place | Channel invitations, `ignored_channels`, and `free_response_channels` |
| Users unexpectedly share context | `group_sessions_per_user` and whether the platform supplied distinct user IDs |
| A thread continues without a new mention | `discord.thread_require_mention` and free-response configuration |
| A role appears to know private information | Profile reuse, copied memory, shared filesystem, or text pasted by the operator |

Do not paste tokens or private logs into a public issue. Reproduce the problem with fictional IDs and redact logs before sharing them.

## Rollback

Rollback is complete only when all applicable layers are reversed:

1. Stop and disable the gateway service.
2. Remove channel and server access in Discord.
3. Reset or revoke the bot token.
4. Remove scheduled jobs created for the role.
5. Export any required handoff, then delete the Hermes profile only after operator approval.

A Git revert of this documentation does not change a live Hermes profile, Discord application, or gateway service.
