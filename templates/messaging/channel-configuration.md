# Channel configuration

Replace placeholders. Do not put real tokens in this file.

## Workplaces

| Role | Channel | Channel ID | Authorized users | Bot identity |
|---|---|---|---|---|
| coordinator | `#coordinator` | `YOUR_COORDINATOR_CHANNEL_ID` | `YOUR_OPERATOR_USER_ID` | `YOUR_COORDINATOR_BOT_NAME` |
| specialist-alpha | `#specialist-alpha` | `YOUR_ALPHA_CHANNEL_ID` | `YOUR_OPERATOR_USER_ID` | `YOUR_ALPHA_BOT_NAME` |
| specialist-beta | `#specialist-beta` | `YOUR_BETA_CHANNEL_ID` | `YOUR_OPERATOR_USER_ID` | `YOUR_BETA_BOT_NAME` |

## Access rules

- Invite each bot only to its workplace and assigned project threads.
- Enable the messaging platform's message-content capability required to read inbound messages.
- Configure an allowlist before starting the role.
- Require a fresh mention in shared channels and threads.
- Leave bot-to-bot messaging disabled in the minimal setup.

## Hermes non-secret defaults

```yaml
group_sessions_per_user: false
discord:
  require_mention: true
  thread_require_mention: true
  free_response_channels: []
  auto_thread: false
```

Set `group_sessions_per_user` to `false` only for a role dedicated to shared project work. Otherwise retain Hermes's default value, `true`.

## Secret placement

Store `DISCORD_BOT_TOKEN` through the runtime's secret mechanism, never through a command argument. `DISCORD_ALLOWED_USERS` is an operator user ID, not a bot token, and may be configured with `hermes config set`. Never place either value in this template or a project handoff.
