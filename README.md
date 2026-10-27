# Agent Organization Guide

A generic, reproducible guide for organizing durable AI agents in a messaging workspace.

The first documented example uses Hermes Agent profiles and Discord. The architecture itself is runtime-neutral: one durable role, one messaging identity, one channel as that role's workplace, and one thread per project. Adapting it to another runtime, including OpenClaw, requires a separate runtime mapping and verification. This repository does not claim that mapping is complete.

## Start here

1. Read [docs/architecture.md](docs/architecture.md) for the model and its limits.
2. Read [docs/hermes-discord.md](docs/hermes-discord.md) for the documentation-reviewed Hermes plus Discord reference.
3. Copy the complete repository, then customize [examples/minimal-team](examples/minimal-team) and replace every `YOUR_*` placeholder. Run repository commands from the repository root.
4. Use the templates under [templates](templates) for roles, governance, channels, kickoff, and handoff.
5. Read [docs/optional-plugins.md](docs/optional-plugins.md), [docs/codex-development.md](docs/codex-development.md), and the shareable [Magpie routing example](examples/magpie-routing/README.md).
6. Run `python3 scripts/check_docs.py` before publication.

## What this is

- A documentation project and a set of generic templates.
- A minimal example with `coordinator`, `specialist-alpha`, and `specialist-beta`.
- A record of which behavior was verified against a specific Hermes installation and which behavior remains an adaptation.

## What this is not

- A finished universal product or a hosted service.
- A copy of any private production deployment.
- An operating-system, memory, or permission sandbox.
- Authorization to create accounts, expose credentials, or publish a repository.

## Safety boundary

Use fictional names and placeholders in every file intended for publication. Never commit tokens, `.env` files, private sessions, memories, local absolute paths, account identifiers, or real organization data. Prompt instructions are conventions. They do not provide filesystem, process, or credential isolation.

## Verification basis

- Hermes Agent version observed locally: `v0.22.4+261.gbf0203a.dirty` (`2026.9.24`)
- Official documentation read on 2026-10-27 from <https://hermes-agent.nousresearch.com/docs/>

The local version command proves the installed version string only. Documentation review supports the described configuration fields, but it does not prove the behavior of this modified local build. No live Discord server, bot account, or gateway was created for this guide. Those checks remain operator verification.

## License

MIT. See [LICENSE](LICENSE).
