# Example Magpie routing design

An AI can follow this document directly. The optional script only prints the same commands for an operator who wants them generated; it is not required to understand or apply the design.

## Roles

| Group ID | Role | Requested effort | Purpose |
|---|---|---|---|
| `dev-worker` | Implementation specialist | `high` | One writer edits and tests the assigned repository. |
| `dev-review` | Architect and reviewer | `high` | Read-only direction review or frozen-candidate review. |
| `dev-research` | Explorer and researcher | `medium` | Bounded investigation. |

Use one group per kind of work. Architect and reviewer may share `dev-review`, but each task still needs a separate session and context. A routing group selects models; it does not grant file access, commit permission, or publication approval.

## Routing choices

Use `routing=order` and `stays=session` for the basic example. Ordered routing tries the first configured member and then the next. Session affinity keeps one coding session with the account or key that answered it while that member can answer.

Magpie also documents `smart`, `rotate`, `usage`, `pace`, `weight`, and `fast`. They are valid alternatives, not proven cost or reliability improvements. If a response fails after partial output, stop and review it; do not assume that failover preserves the work.

## Model placeholders

Replace the fictional IDs below with IDs shown by the operator's own `magpie models` output:

- `PROVIDER_A/MODEL_STRONG`
- `PROVIDER_B/MODEL_ALTERNATE`
- `PROVIDER_C/MODEL_REVIEW`
- `PROVIDER_D/MODEL_FAST`

Do not invent IDs from marketing names. Do not include account names, API keys, tokens, host names, usage exports, or an existing private group configuration.

## Commands an AI can adapt

Check whether a group already exists before creating one. `magpie group add` replaces a group with the same name.

```bash
magpie group dev-worker
magpie group dev-review
magpie group dev-research
```

Create the three groups only after that check is clear:

```bash
magpie group add "Dev Worker" \
  "models=PROVIDER_A/MODEL_STRONG:high,PROVIDER_B/MODEL_ALTERNATE:high" \
  routing=order stays=session
magpie group set dev-worker id=dev-worker

magpie group add "Dev Review" \
  "models=PROVIDER_C/MODEL_REVIEW:high,PROVIDER_A/MODEL_STRONG:high" \
  routing=order stays=session
magpie group set dev-review id=dev-review

magpie group add "Dev Research" \
  "models=PROVIDER_D/MODEL_FAST:medium,PROVIDER_B/MODEL_ALTERNATE:medium" \
  routing=order stays=session
magpie group set dev-research id=dev-research
```

Read each result back:

```bash
magpie group dev-worker
magpie group dev-review
magpie group dev-research
```

The expected result is three distinct groups, each with its own member order, effort, `routing=order`, and `stays=session`.

## How Hermes uses the groups

A Hermes coordinator assigns work. The coding leaf selects one group for that invocation:

- Implementation uses `group/dev-worker`.
- Review or architecture uses `group/dev-review`.
- Investigation uses `group/dev-research`.

The task still needs a repository, scope, acceptance checks, prohibitions, and stop conditions. Magpie may choose among the selected group's configured members. The requested group is not proof of which model served the request; record the observed provider and model separately.

## Optional command printer

`generate_groups.py` prints these commands without running Magpie or reading its configuration. From the repository root:

```bash
python3 examples/magpie-routing/generate_groups.py --print
```

An operator can pass their own model IDs with `--worker-models`, `--review-models`, and `--research-models`. This is a convenience, not another routing design.

## What this does not prove

This example was checked against Magpie `0.1.1657` local help and the public Magpie routing documentation on 2026-10-27. No group was created and no live model request was sent. Group creation, Codex compatibility, quota failover, and actual served-model reporting remain operator verification.
