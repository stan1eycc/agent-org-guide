# Multi-bot collaboration contract

This runtime-neutral collaboration pattern extends the existing role/workplace/project model. Hermes and Discord provide the concrete setting reference; another runtime must verify its own equivalents. No private conversations or historical deployment outcomes are reconstructed.

## Evidence classes

- **Saved rule:** an authorized shared procedure records globally required mentions, explicit registration of collaboration thread IDs, thread replies without mentions, and rejection of bot-authored triggers.
- **Actual settings:** unknown in this task. No production configuration was inspected.
- **Verified live behavior:** unknown in this task. No Discord message was sent or observed.
- **Proposed design:** the ownership, task allocation, synthesis and delivery protocol below is newly authored for this guide.
- **Locally checked:** the example's structure and synthetic decision cases can be checked offline; this is not a Hermes adapter test.

## Participants and triggers

Dedicated workplace: only its assigned bot may answer authorized human messages without a mention.

Shared project parent: mention the coordinator. Shared collaboration parent: mention the intended specialist. Neither parent belongs in a free-response list.

Project thread: coordinator only; require a mention in the example. Collaboration thread: alpha and beta, with alpha responsible for synthesis. Register the exact collaboration thread placeholder in both specialists' free-response lists. Do not substitute its parent. The specialists use `thread_require_mention: false` to reflect the saved rule: this can also relax mentions in other threads they have already joined. Constrain permitted threads and test this wider shortcut; do not describe the setting as applying only to one thread.

An unmentioned authorized human message in the registered collaboration thread may wake both specialists. A human mention aimed only at alpha should suppress beta under the documented ignore-other-mentions behavior. Replies, multiple mentions and first messages in manually created threads require real adapter tests. Free-response and thread settings interact; do not assume setting `thread_require_mention: true` overrides an explicit free-response exception.

Bot-authored messages, including bot messages mentioning another bot, are ignored with `allow_bots: "none"`. Do not enable `mentions` or `all` to make a conversation proceed. A visible bot response can still appear in historical context; absence of a trigger does not mean absence from every possible context source.

## A complete work round

1. The human posts the collaboration kickoff, naming the project, alpha as owner, both participants, one task for each, evidence requirements and acceptance criteria.
2. Alpha returns the analysis; beta independently returns checks and disagreement. Neither waits for a bot post to trigger its turn. If beta needs alpha's output, the human supplies that artifact in a fresh, explicitly addressed review request.
3. Contributions contain findings, evidence, assumptions, failures and a proposed next action. A participant with missing evidence reports the gap rather than reading another Profile's state.
4. The human requests synthesis from alpha, supplying both contributions if needed. Alpha resolves supported differences, records unresolved issues and identifies tests performed. An addressed synthesis request should not trigger beta; confirm this live.
5. The human accepts or requests changes. After acceptance, the human transfers the compact handoff to the coordinator's project thread. The coordinator checks it against project acceptance and delivers one final result.
6. Close the collaboration with status and next owner. Do not create a watcher, retry, new assignment or external write from the closed record.

## Loops, duplicates and stop conditions

The transport bot-author filter breaks Discord bot-to-bot response loops. Role prompts add a behavioral rule: no recursive invitations, acknowledgements of acknowledgements or self-assigned follow-up. These are separate controls; a prompt is not an enforced filter.

Human messages waking two bots is intended fan-out, not proof of a loop. Two replies from the same bot to one request may indicate duplicate runtime ownership; check it before trying again. Stop on an unknown participant, ambiguous owner, missing scope, unintended audience, inconsistent evidence or uncertain external result. Preserve the last known status and return control to the human. No automatic retries or time-based monitoring are part of this design.

An internal relay could replace manual transfer only after its exact sender, recipient, scope, delivery result and loop controls are separately approved and tested. Native delegation does not necessarily invoke a persistent named Profile; this guide assumes no such integration.

## Relation to the existing project example

The original [minimal team](../examples/minimal-team/README.md) retains explicit mentions for every role in its shared project thread. The [collaboration extension](../examples/collaboration-team/README.md) adds a second thread under a separate private parent. Both are supported policies; neither turns a thread into a sandbox.

The extension uses a coordinator-only project thread and two specialists in the collaboration thread. A runtime with no bot-author filter must implement and verify an equivalent transport control before using this design. A prompt that says “do not loop” is insufficient. No special plugin, relay, scheduler or script is required to understand or operate the human-mediated procedure.

See [collaboration evidence](collaboration-evidence.md), [installation](installation.md), and [verification](verification.md) for sources, version limits and unexecuted gates.
