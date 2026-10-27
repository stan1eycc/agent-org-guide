# Minimal team example

This example is intentionally generic. It shows one operator, three durable roles, three workplaces, and one project thread. Replace every placeholder before use.

```text
operator
  |-- coordinator -------- #coordinator
  |-- specialist-alpha --- #specialist-alpha
  |-- specialist-beta ---- #specialist-beta
  +-- all assigned roles - #sample-project (private parent)
                              +-- private thread: sample-project
```

## Use the templates

- [coordinator role](../../templates/roles/coordinator.md)
- [specialist-alpha role](../../templates/roles/specialist-alpha.md)
- [specialist-beta role](../../templates/roles/specialist-beta.md)
- [shared governance](../../templates/governance/shared-governance.md)
- [channel configuration](../../templates/messaging/channel-configuration.md)
- [sample kickoff](docs/projects/sample-project-kickoff.md)
- [sample handoff](docs/projects/sample-project-handoff.md)

## Expected flow

1. The operator creates three Discord applications and three Hermes profiles.
2. Each profile receives only its own bot token and starts only after an allowlist exists.
3. The operator creates the private `#sample-project` parent channel and a private `sample-project` thread, then posts the kickoff.
4. The operator invites only the three assigned bots.
5. The operator mentions one role at a time and keeps assignments inside the kickoff.
6. Alpha reports implementation evidence. Beta reviews it. The coordinator completes the handoff.

## Pass condition

A newcomer can identify who owns each action, where it happens, what evidence finishes it, and which actions still require operator approval. No real account, token, path, or private history is required to understand the example.
