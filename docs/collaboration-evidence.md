# Evidence and source register

Reviewed on 2026-10-27. Current upstream documentation can change independently of an installed runtime. Each assertion below is limited to its evidence class.

## Version observations

- Hermes CLI reported `v0.22.4+261.gbf0203a.dirty`, build date `2026.9.24`, revision `bf0203a794a0`. This is a local dirty build, not a clean reproducibility pin or evidence that every current upstream feature exists locally.
- Local `hermes profile create --help` confirms `--no-alias`, `--no-skills` and `--description`; `hermes config set --help` confirms leaf key/value syntax. These help commands and the version command were executed. No Profile was created or modified.
- The authorized shared cabinet procedure identifies itself as version `1.4.0`. Its collaboration rules were read through the explicitly named shared source. No linked private roster, deployment record, configuration, session, memory, log, backup or credential store was read.
- Codex CLI `0.163.0` performed independent read-only artifact review. Findings were corrected and checked separately; see [publication review](publication-review.md).

## Source map

- S1: [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation) — official Hermes documentation, retrieved 2026-10-27.
- S2: [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) — official Hermes documentation, retrieved 2026-10-27.
- S3: [Discord](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord) — official Hermes documentation, retrieved 2026-10-27.
- S4: [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security) — official Hermes documentation, retrieved 2026-10-27.
- S5: [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) — official Hermes documentation, retrieved 2026-10-27.
- S6: [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) — official Hermes documentation, retrieved 2026-10-27.
- S7: [Memory providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers) — official Hermes documentation, retrieved 2026-10-27.

S2–S5 were also read from the official repository's raw Markdown, because rendered extraction omitted important settings. Exact source locations and extracted-content fingerprints are listed in [collaboration-sources.json](collaboration-sources.json). These fingerprints identify the retrieved text, not a runtime binary or upstream commit. Raw source documents were not copied into the public candidate.

## Claims ledger

| Claim | Evidence | Classification | Remaining gate |
| --- | --- | --- | --- |
| Separate Profile state, one visible identity per role | S2, shared procedure | Documentation-reviewed; blueprint mapping | Fresh isolated deployment |
| Profiles and prompts do not sandbox host tools | S2, S4, shared procedure | Documented limitation | Separately verify any chosen hard boundary |
| Channel mention and thread/free-response controls | S3 | Documented native controls | Exact selected runtime and Discord tests |
| Reject bot-authored triggers with string `none` | S3 and saved shared rule | Documented control plus saved rule | Effective type, precedence and real bot-message test |
| Channel @ / registered collaboration thread no @ | Shared procedure v1.4.0 | Saved rule | Production settings and historical success unknown |
| Two bots can wake on one unmentioned human turn | S3 and shared procedure | Expected consequence, not observed here | Live fan-out test |
| Ownership, manual relay, independent review and synthesis | Current project requirements and new templates | Proposed project convention | End-to-end human-mediated exercise |
| Memory and Skills support continuity | S5, S6 | Native facilities plus proposed usage | Fresh-session loading and audience tests |
| Hindsight is an optional memory integration | S7 | Third-party integration documented by Hermes | Not installed or tested here |
| Minimal example is structurally repeatable | Local scripts | Offline synthetic check only | See publication report for actual results |

## Source gaps and conflicts

No source establishes the actual production settings or historical observed behavior of the requested collaboration room. The shared rule is sufficient to explain a proposed setup, not to certify that deployment. The formal saved procedure and upstream docs both warn about thread mention shortcuts; the example preserves that warning instead of silently changing the chosen UX.

Standalone gateway guidance uses S2. No multiplexer behavior or separate gateway documentation route is claimed as verified. Runtime differences, installed key/type support, token ownership, private-thread visibility and real message admission remain deployment gates. No private history was consulted to fill these gaps.
