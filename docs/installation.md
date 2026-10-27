# Installation in a disposable environment

This procedure extends the [Hermes reference](hermes-discord.md) for a future separately approved disposable deployment. **No installation, authentication, Profile creation or service activation was performed for this candidate.** The executed local checks only assemble inert files and evaluate synthetic examples.

## Preconditions

Use a new disposable OS account, container or machine with no production Hermes state or credentials mounted. Merely changing the working directory or `HERMES_HOME` does not isolate host tools, configuration discovery or credentials. Obtain approval for the environment, identities, model access, potential cost and service lifecycle before continuing. If any are missing, record the missing prerequisite and stop the deployment path; offline document checks remain possible.

Install Hermes by following source S1 in [collaboration evidence](collaboration-evidence.md). This guide does not pin or execute an installer. Choose an explicit release or revision, record its version, and compare that version's help and documentation with the commands below. The locally observed dirty build is not a reproducible release pin.

## Create roles from scratch

These commands were checked for syntax against local help; they were not executed:

```sh
hermes profile create coordinator --no-alias --no-skills --description "Owns project intake and final delivery."
hermes profile create specialist-alpha --no-alias --no-skills --description "Owns analysis and collaboration synthesis."
hermes profile create specialist-beta --no-alias --no-skills --description "Checks evidence and assumptions independently."
```

Do not use clone options. In the disposable environment, place each role template's text in that Profile's `SOUL.md`, and adapt [shared governance](../templates/governance/shared-governance.md) into a locally reviewed governance Skill or place its full text in each SOUL. If using a Skill, explicitly instruct the agent to load it at session start; a repository link alone does not cause Hermes to load it. Maintain one authoritative version and verify each Profile received it. The `--no-skills` choice avoids unrelated bundled integrations during bring-up; add reviewed procedures explicitly later.

Use the profile-scoped interactive setup for model/provider access, then Discord:

```sh
hermes -p coordinator setup
hermes -p coordinator gateway setup
```

Repeat for each specialist with its own identity. Enter credentials only in the local interactive flow. Never copy a credential store. Profile names and CLI syntax must be rechecked against the selected version before use.

## Discord topology and non-secret policy

Create three distinct applications and bot identities. Enable the documented Server Members and Message Content intents. Grant only required View Channel, Send Messages, Read Message History, Send Messages in Threads, Embed Links and Attach Files permissions; grant thread creation only if the bot must create threads. Do not grant Administrator for ordinary participation.

Create the five workplaces and two private threads described by [the example](../examples/collaboration-team/README.md). Give each bot its own workplace, and only its assigned shared parent/thread. Deny unrelated workplaces. Add bots to private threads as required by Discord; verify membership and parent visibility separately.

The three `*.json` configuration fragments are JSON-form YAML-compatible documents with real Hermes setting names and deliberately invalid identifier placeholders. They are **non-secret fragments, not full runtime configurations**. Resolve placeholders locally and apply their leaf settings with the selected version's native configuration commands; do not overwrite an existing configuration with a fragment.

For example, after checking help:

```sh
hermes -p specialist-alpha config set discord.require_mention true
hermes -p specialist-alpha config set discord.thread_require_mention false
hermes -p specialist-alpha config set discord.auto_thread false
hermes -p specialist-alpha config set discord.allow_bots none
```

Read back effective types: the bot-author gate must contain the string `none`, not null; IDs must resolve into the intended sets. The guide does not prescribe `--force` as a fix for an unknown key. If a key or type is unsupported, stop and record the version mismatch. Equivalent environment settings can override YAML; a deployment operator must verify their non-secret effective values without printing credential stores. `group_sessions_per_user: true` preserves the documented per-user separation.

## Activate and accept

Choose exactly one supported gateway owner per bot identity. Select standalone per-Profile gateways or an explicitly reviewed multiplexer. Do not run both. The official Profiles documentation covers standalone service commands; this guide does not infer a working multiplexer from it. Start only the approved disposable gateway through its version-supported lifecycle.

Verify identity, real inbound and negative-channel behavior, bot-author rejection, thread rules, no duplicate replies, and fresh-session governance loading using [verification](verification.md). Record settings on disk, loaded runtime policy and observed responses separately. Until these pass, the topology is configured at most, not reproduced. Use [recovery](troubleshooting-recovery.md) to stop only the disposable resources on failure.
