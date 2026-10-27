# Agent Organization Guide

Use this repository to build a small team of durable AI agents without copying anyone's private deployment.

The design is runtime-neutral. Hermes plus Discord is the first concrete reference. An OpenClaw bot can use the same operating model by mapping each object below to its own agent, channel, session, memory, and tool facilities. This repository gives the bot the rules and records it needs; it does not need to run the optional scripts.

## The operating model

Create four separate objects:

| Object | What it means | Minimal example |
|---|---|---|
| Durable role | A long-lived agent with its own instructions, memory, tools, and credentials | `coordinator`, `specialist-alpha`, `specialist-beta` |
| Messaging identity | The account people mention in chat | One bot or agent account per role |
| Workplace | The normal room for talking to that role | `#coordinator`, `#specialist-alpha`, `#specialist-beta` |
| Project thread | One shared conversation for one bounded project | Private parent `#sample-project` plus thread `sample-project` |

```text
operator
  |-- coordinator -------- workplace --------+
  |-- specialist-alpha --- workplace --------+--> sample-project thread
  +-- specialist-beta ---- workplace --------+
```

The coordinator decides who does what and records the result. Alpha implements in one assigned repository. Beta checks the evidence and looks for gaps. All three can participate in the same project thread, but none receives another role's private memory, credentials, or files merely because it can see that thread.

A project starts from [templates/projects/project-thread-kickoff.md](templates/projects/project-thread-kickoff.md). It names the scope, inputs, acceptance checks, prohibitions, and stop conditions. It ends with [templates/records/handoff-record.md](templates/records/handoff-record.md), which records checked facts rather than relying on model memory.

## What an OpenClaw bot should do

Read this file first, then [docs/architecture.md](docs/architecture.md), [docs/optional-plugins.md](docs/optional-plugins.md), and [docs/adaptation.md](docs/adaptation.md).

1. Create the three durable roles from [templates/roles](templates/roles).
2. Give every role a distinct messaging identity, credential store, workplace, and memory store.
3. Put the shared governance rules from [templates/governance/shared-governance.md](templates/governance/shared-governance.md) where that runtime loads durable role instructions.
4. Create one private project conversation and post a kickoff copied from the template.
5. Invite only the roles assigned to that project.
6. Address one role at a time. Do not let one implementation agent write the same files while another implementation agent is writing them.
7. Require the implementing role to report the diff and the checks it actually ran. Require the reviewing role to inspect that evidence.
8. Keep commit, push, repository creation, publication, deployment, credential changes, and deletion as separate operator approvals.

OpenClaw must supply its own equivalents for a Hermes profile, a Discord bot account, a channel, and a thread. The generic mapping is:

| Guide object | Hermes plus Discord reference | OpenClaw adaptation |
|---|---|---|
| Durable role | Hermes profile and `SOUL.md` | The OpenClaw agent or workspace that persists its instructions |
| Messaging identity | Discord application and bot account | The OpenClaw-controlled chat account |
| Workplace | Discord channel | The OpenClaw room, channel, or direct-message boundary |
| Project thread | Discord thread under a private parent channel | The OpenClaw conversation or topic used for one project |
| Shared record | Markdown kickoff and handoff | The same Markdown files, or the runtime's equivalent shared document |
| Role memory | Optional Hindsight bank | A separate memory namespace owned by one role |

If OpenClaw cannot keep one of those stores separate, state that limitation in the handoff. Do not rename a shared memory, shared credential file, or shared workspace and call it isolation.

The Hermes-specific commands in [docs/hermes-discord.md](docs/hermes-discord.md) are a reference implementation, not instructions for OpenClaw. Use [docs/adaptation.md](docs/adaptation.md) for the checks required before calling another runtime compatible.

## Optional capabilities

The base team works with durable roles, messaging, project threads, and Markdown records. Add a capability only when its benefit is clear, then record its version, data location, credential requirement, and removal procedure.

| Capability | Use it for | Do not treat it as |
|---|---|---|
| [Hindsight](docs/optional-plugins.md) | Recommended long-term recall of project decisions and rejected approaches | A shared project record or an authorization source |
| HeartBeat | One bounded follow-up with a deadline and wake limit | Continuous monitoring |
| Jev | Choosing among non-sensitive, already retrieved options | Approval, proof, or permission to receive private data |
| Codex or another coding tool | Implementation or review inside one assigned repository | Acceptance of its own completion message |
| [Magpie](examples/magpie-routing/README.md) | Optional model routing for development roles | Permission to edit, commit, or change providers automatically |

Use one Hindsight memory bank per role. Recall can help reconstruct context, but the project thread and handoff remain authoritative. A recalled fact must be checked before it is acted on.

For development, the coordinator writes the task boundary, the coding tool works in the named repository, and the reviewer checks the diff and reruns the relevant tests. The optional Magpie design uses separate `dev-worker`, `dev-review`, and `dev-research` routes. Its command script is only a convenience; the prose design is sufficient for another bot to adapt.

## Privacy and authority

- Replace every `YOUR_*` placeholder with values owned by the operator.
- Do not publish tokens, `.env` files, sessions, memories, absolute local paths, account identifiers, or private organization data.
- Do not copy a working private deployment to create a new one. Rebuild from the templates.
- Prompt instructions are operating conventions. They do not create filesystem, process, memory, or credential isolation.
- A clean privacy scan is one release check, not approval to publish.

## Verification status

Reviewed against Hermes documentation and these local command surfaces on 2026-10-27:

- Hermes Agent `v0.22.4+261.gbf0203a.dirty` (`2026.9.24`)
- Codex CLI `0.163.0`
- Magpie `0.1.1657`

No live Discord server, OpenClaw installation, Codex coding task, or Magpie model route was created for this guide. Those remain operator-specific verification. The Hermes version string identifies a modified local build, so documentation review does not prove that build's runtime behavior.

## Repository map

- [docs/architecture.md](docs/architecture.md) — model, limits, and failure rules
- [docs/hermes-discord.md](docs/hermes-discord.md) — Hermes plus Discord reference
- [docs/operations.md](docs/operations.md) — day-to-day operation
- [docs/security-privacy.md](docs/security-privacy.md) — publication and privacy checks
- [docs/adaptation.md](docs/adaptation.md) — OpenClaw and other runtime adaptations
- [docs/optional-plugins.md](docs/optional-plugins.md) — Hindsight, HeartBeat, Jev, and coding tools
- [docs/codex-development.md](docs/codex-development.md) — optional Codex development lane
- [examples/minimal-team](examples/minimal-team) — three roles and one project
- [examples/magpie-routing](examples/magpie-routing) — optional model-routing design
- [templates](templates) — role, governance, channel, kickoff, and handoff templates

Before publishing a derived repository, run `python3 scripts/check_docs.py` when Python is available. The script is a scanner, not part of the agent architecture.

## License

MIT. See [LICENSE](LICENSE).
