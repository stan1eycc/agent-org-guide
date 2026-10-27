# Codex development lanes

This is an optional development architecture. Hermes remains the coordinator. Codex performs the repository work. Magpie optionally routes Codex to a configured model provider. None of these tools grants publication or deployment approval.

## Verification basis

Checked on 2026-10-27:

- Codex CLI `0.163.0`, from `codex --version` and `codex exec --help`
- Magpie `0.1.1657`, from `magpie --version`, `magpie --help`, and `magpie group --help`

The commands below were read from local help output. A live coding task and a live model route were not run as part of this documentation.

## Responsibilities

| Component | Responsibility | Does not do |
|---|---|---|
| Hermes coordinator | Writes scope, acceptance, prohibitions, and stop conditions | Implement from an ambiguous thread message |
| Codex CLI | Edits and tests inside the assigned Git repository | Accept its own completion message as approval |
| Magpie | Selects or routes the model used by Codex | Store task authorization or replace Git history |
| Specialist reviewer | Reviews the resulting diff and evidence | Treat Magpie routing metadata as code evidence |

## Lane contract

Every Codex task needs:

1. One repository and working directory.
2. The files or behavior that may change.
3. Acceptance checks.
4. Files, services, credentials, and external actions that are prohibited.
5. A stop condition for missing inputs or failed checks.

A task prompt must not contain credentials or private data. Codex receives the task, not unrestricted access to the operator's files.

## Reviewed command shape

Run Codex from the assigned repository:

```bash
codex exec --sandbox workspace-write \
  --cd YOUR_REPOSITORY_PATH \
  "Implement the assigned change, run the named checks, and do not commit or publish."
```

The installed CLI also supports:

- `--sandbox read-only` for review or investigation.
- `--sandbox workspace-write` for implementation inside the workspace.
- `--sandbox danger-full-access` only inside an external sandbox chosen by the operator. The CLI labels this mode dangerous.
- `codex exec review` for a repository review.
- `--json` and `--output-last-message FILE` for capturing machine-readable output.
- `--worktree` for a separate Git worktree.
- `--ephemeral` when the operator does not want a persisted Codex session.

Use the default workspace boundary unless a documented reason requires another mode. Do not add directories with `--add-dir` merely because a task is inconvenient to decompose.

## Acceptance after Codex

The specialist role must inspect the Git diff and rerun the named checks. Codex's final message can identify claimed results, but it is not evidence. The handoff records:

- Codex version.
- Command and sandbox mode.
- Files changed.
- Checks actually rerun and their results.
- Any unverified statement from Codex.

## Magpie routing

Magpie is optional. It provides a local model catalog, provider routing, profiles, and usage reporting for supported agents, including Codex. It is useful when the operator wants one place to select a model or distribute requests across configured providers.

The shareable three-role design is [examples/magpie-routing](../examples/magpie-routing/README.md). An AI can follow that document directly. Its optional script only prints the same commands and does not read or change a Magpie installation.

Generic read-only checks are:

```bash
magpie --version
magpie codex
magpie models codex
magpie usage 7d
```

Changing a route, provider, account, key, or backup is a configuration change and needs separate operator approval. Do not place provider keys in the project repository, task prompt, or handoff.

Magpie usage output can contain account identifiers and cost data. Summarize the relevant model and status; do not publish raw usage exports.

## Failure and rollback

- If Codex exits without a diff, report the exit state and do not invent the intended change.
- If Codex changes files outside the assignment, revert only those known files after inspection or stop for operator review.
- If Magpie routing fails, stop that lane. Do not silently switch to another provider or account.
- Removing Magpie from the route does not revert repository edits. Revert those separately with Git.

## Minimal sequence

1. The coordinator records the task and acceptance criteria.
2. The operator confirms the repository and whether Magpie routing is already configured.
3. The implementation specialist starts Codex in that repository.
4. The specialist reviews and reruns checks.
5. The reviewer checks scope, privacy, and evidence.
6. The coordinator writes the handoff. Commit and publication remain separate approvals.
