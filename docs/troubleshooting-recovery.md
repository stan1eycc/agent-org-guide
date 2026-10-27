# Troubleshooting and recovery

| Symptom | Read-only distinction | Scoped response |
| --- | --- | --- |
| Bot offline | Identity, token validity and required intents are separate from role text | Operator verifies the disposable application and local setup; never post a token or raw diagnostic dump |
| Mention ignored | Check actor admission, parent visibility, thread membership, channel admission and mention rules separately | Correct only the intended disposable resource after understanding the failing gate |
| First unmentioned thread message ignored | A manually created thread may not have participation state | Register the exact permitted collaboration thread for both participants; do not make the whole parent free-response |
| Both specialists answer | An unmentioned human message in the collaboration thread intentionally fans out | Address one participant for a single-owner turn, and run the mention-specific test |
| Bot posts trigger more bots | Bot-author filter is wrong, stale or overridden | Stop the affected test gateway; restore bot rejection and verify effective runtime state before resuming |
| Same bot answers twice | More than one runtime may own the identity | Identify the duplicate owner; do not restart a whole fleet or blindly retry the message |
| Saved settings disagree with behavior | Environment precedence, old adapter snapshots or old session prompts may differ | Compare disk, effective loader and live behavior; never treat a config write as activation proof |
| A participant lacks context | Per-user and per-bot sessions are separate; backfill is bounded | Supply the approved kickoff or handoff; do not read private sessions to fill gaps |
| A setting is rejected | Installed schema/help may differ from current docs | Stop, record version and setting category, and obtain a reviewed version-specific adaptation |

## Recovery procedure

1. Stop issuing new test prompts and mark the last operation completed, failed or unknown. Do not resend an uncertain external write.
2. Stop only the gateway/service created for the disposable test, using the selected version's documented lifecycle. Record that local shutdown does not prove cancellation of any remote request.
3. Remove the test bot's access to the test channels if necessary and separately authorized. If any credential was exposed, the operator revokes it through the provider; do not put it in a report or repository.
4. Restore only the reviewed non-secret template revision, with native configuration commands. Never restore a production backup or copy an existing Profile. Re-provision a fresh disposable environment when isolation is uncertain.
5. Create a fresh test session when prompt/tool policy changes require it. Re-run the failing positive and negative cases before declaring recovery. Do not reset active production work.
6. Preserve sanitized evidence and the unresolved gate. Deletion of test accounts, channels or files requires explicit scope; this guide includes no destructive cleanup automation.

If a future publication exposes a secret, removing the current file is insufficient. Stop publication, revoke the secret, inventory historical objects and distributed artifacts, and seek a separately approved remediation plan. This repository already has public history. Review all inherited objects and metadata as well as the new content before a later publication.
