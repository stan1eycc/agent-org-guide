# Hermes and Discord reference

This is the first concrete reference for the architecture. It describes Hermes Agent and Discord behavior verified against the sources listed below. It is not a claim that every Hermes version or deployment behaves identically.

## Verification sources

Checked on 2026-10-27:

- Installed Hermes Agent: `v0.22.4+261.gbf0203a.dirty` (`2026.9.24`)
- Profile behavior: <https://hermes-agent.nousresearch.com/docs/user-guide/profiles>
- Discord behavior: <https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord>
- Multiple gateways: <https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways>
- Sessions and configuration: official Sessions, Security, Configuration, Context Files, and Skills pages

The version command was run locally. The documentation pages were read from the official site. No live Discord server, bot account, or gateway was created while validating this guide.

## Documentation-reviewed Hermes behavior

- A profile is a separate Hermes home. Official documentation describes separate configuration, credentials, memory, sessions, skills, cron state, and state database for each profile.
- `hermes profile create NAME` creates a profile. With the normal alias behavior, that name becomes a command such as `coordinator setup` and `coordinator gateway start`.
- Official multi-gateway documentation shows one gateway service per profile, using that profile's own bot credentials and state.
- Discord requires the Message Content intent. Server Members intent is required for username or role-based authorization.
- Without an access policy, current Hermes documentation says Discord connects but denies inbound users. The supported controls include `DISCORD_ALLOWED_USERS`, `DISCORD_ALLOWED_ROLES`, and `DISCORD_ALLOWED_CHANNELS`.
- Discord threads have session history separate from the parent channel. Mention rules still apply unless the thread or parent is explicitly configured as free-response.
- `group_sessions_per_user` defaults to `true`, isolating users who share a channel. Set it to `false` only when a project thread intentionally shares one transcript.
- `discord.thread_require_mention: true` disables the shortcut that otherwise lets later messages in a participated thread bypass a fresh mention. This is the setting used by the minimal example.
- Secrets belong in `.env`; non-secret settings belong in `config.yaml`. `hermes config set` routes uppercase secret-style names to `.env`.

## Unverified or version-sensitive behavior

- This repository was not tested end to end against a live Discord server.
- Profile command aliases depend on shell initialization after profile creation. Verify the resulting command with `command -v`.
- Gateway service names and process supervision vary by operating system. Use `hermes gateway --help` on the target machine.
- Discord permission changes can require re-inviting a bot or editing its role. The exact permission result must be checked in Discord.
- Documentation can move ahead of an older installation. Recheck these pages after upgrading Hermes.

## Generic setup sequence

After `ROLE setup`, copy the text of that role's template and the shared governance document into the profile's `SOUL.md` at `~/.hermes/profiles/ROLE/SOUL.md`. Hermes loads this file as text from the profile home; it does not automatically load or expand references to files in this repository. Start a fresh session and ask the role to state its allowed scope before exposing it to a project.

```bash
hermes profile create coordinator
hermes profile create specialist-alpha
hermes profile create specialist-beta

coordinator setup
specialist-alpha setup
specialist-beta setup
```

Put each bot token directly into that profile's ignored `.env` file. Do not pass the token as a command argument or store it in shell history. `hermes config set` can route an uppercase secret-style name to `.env`, but only use it through an input method that does not expose the value in process arguments. Set the non-secret Discord user allowlist separately:

```bash
hermes -p coordinator config set DISCORD_ALLOWED_USERS YOUR_OPERATOR_DISCORD_USER_ID
```

Set non-secret Discord behavior in `config.yaml`:

```yaml
group_sessions_per_user: false
discord:
  require_mention: true
  thread_require_mention: true
  free_response_channels: []
  auto_thread: false
```

The shared value `group_sessions_per_user: false` applies to the whole profile, not only the project thread. Use it only when that role is reserved for shared project work. Otherwise leave the default `true` and explicitly record that each human has a separate session.

Invite each bot only to its workplace channel and to the project threads it needs. A bot invited to every channel can receive more context even when instructions tell it not to answer.

## Recommended channel map

| Channel | Participants | Purpose |
|---|---|---|
| `#coordinator` | operator, coordinator bot | Decisions, assignments, acceptance |
| `#specialist-alpha` | operator, alpha bot | Implementation requests and results |
| `#specialist-beta` | operator, beta bot | Review requests and findings |
| project thread | only the roles assigned to that project | Project context and handoff |

Do not use one public channel as every role's workplace. A shared project thread is intentional shared context; a shared workplace quickly becomes accidental shared context.

## Project thread boundary

Create a dedicated private project parent channel, then create the project as a private thread inside it. Do not place the shared thread under one role's workplace. Discord thread access inherits from the parent channel, and a bot needs permission to view that parent before it can participate in the thread.

A public thread is visible to everyone who can view its parent. A private thread is visible to its explicit members and users with thread-management permission. Before assigning work, test with an unassigned account that it cannot view the thread, and record every moderator who can. This repository does not include a live Discord test.

## Rollback

1. Stop the affected gateway: `hermes -p ROLE gateway stop`.
2. Remove the bot from the Discord server or restrict it to no channels.
3. Revoke or reset its Discord token through the Discord Developer Portal.
4. Preserve the profile directory until the operator confirms that no session or handoff needs export.
5. Delete the profile only with `hermes profile delete ROLE` after that confirmation.

Stopping a gateway does not revoke a token or remove a bot from Discord. Complete all three layers.

## Other runtimes

OpenClaw or another agent runtime can use the same organization only after its own objects are mapped:

| Architecture object | Hermes object | Other runtime |
|---|---|---|
| Durable role | Hermes profile | Verify its actual state boundary |
| Messaging identity | One Discord bot token | Verify account and token ownership |
| Workplace | Discord channel permissions | Verify platform-native access control |
| Project boundary | Discord thread and session | Verify its transcript and mention behavior |
| Approval boundary | Hermes approvals and operator review | Verify its enforcement, not its prompt text |

Until that mapping is tested, label the runtime adaptation unverified.
