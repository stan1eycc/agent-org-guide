# Collaboration extension example

This example is inert. It contains no credentials, real identifiers or executable provisioning. Read it directly; the optional check script only verifies structure and synthetic behavior.

## Topology

- `coordinator` owns `coordinator-workplace` and `sample-project` under `project-workplace`.
- `specialist-alpha` owns `alpha-workplace` and leads synthesis in `sample-collaboration`.
- `specialist-beta` owns `beta-workplace` and independently checks evidence in `sample-collaboration`.
- `sample-collaboration` sits under `collaboration-workplace`. Its participants are alpha and beta only.
- The human is the only authorized message author in this minimal fixture. Additional people require explicit audience and admission review.

All five workplaces are private to the intended audience. Both threads are private and have explicit members. Project and collaboration parents are not specialist private workplaces. Discord permissions, Hermes channel admission and thread membership must agree.

## Files and placeholders

[team.json](team.json) is a project convention, not Hermes configuration. [coordinator.json](coordinator.json), [specialist-alpha.json](specialist-alpha.json) and [specialist-beta.json](specialist-beta.json) are non-secret Hermes setting fragments, expressed as JSON-form YAML-compatible mappings. Placeholders intentionally cannot connect to Discord.

- `YOUR_OPERATOR_ID`: one locally approved human actor.
- `YOUR_COORDINATOR_CHANNEL_ID`, `YOUR_ALPHA_CHANNEL_ID`, `YOUR_BETA_CHANNEL_ID`: dedicated workplaces.
- `YOUR_PROJECT_PARENT_ID`, `YOUR_COLLABORATION_PARENT_ID`: shared parent workplaces.
- `YOUR_PROJECT_THREAD_ID`, `YOUR_COLLABORATION_THREAD_ID`: the two exact threads.

Replace identifiers only in a separate private disposable deployment, never in this public example. No bot-token field is included. Keep `allow_bots` as the string `none`. Use CSV strings for admission and free-response settings to avoid assuming that a CLI parses list literals. Verify the effective types on the selected runtime.

The coordinator has strict thread mentions. Both specialists have relaxed joined-thread mentions and explicitly registered collaboration-thread free response. Shared parents are never free-response. This difference is intentional and documented in [collaboration](../../docs/collaboration.md).

## Synthetic exercise

The fictional task is to choose between two invented document outlines. Alpha compares clarity; beta checks whether all requested sections exist. The human provides both outputs to alpha for synthesis, then carries the accepted handoff to the coordinator. No external research, private file, paid model or automatic relay is needed to understand the process.

```sh
python3 -B scripts/check_collaboration.py
```

Run that command from the project root, not this subdirectory. It tests an explicit proposed contract, not Hermes runtime code. See [verification](../../docs/verification.md) for the unexecuted live matrix.
