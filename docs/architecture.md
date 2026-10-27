# Architecture

## Core model

Use four separate objects, each with one job:

| Object | Responsibility | Must not be confused with |
|---|---|---|
| Durable role | A long-lived agent identity, instructions, memory, and configuration | One conversation or one task |
| Messaging identity | The account visible in the messaging service | The role's private files or credentials |
| Workplace channel | The normal place where humans address that role | A shared context for every role |
| Project thread | One bounded project conversation and its handoff record | Memory, authorization, or filesystem isolation |

```text
human operator
    |
    +-- coordinator identity ---- coordinator channel ---- project thread
    |
    +-- specialist-alpha -------- alpha channel --------- same project thread
    |
    +-- specialist-beta --------- beta channel ---------- same project thread
```

Each role keeps its own durable state. A thread gives the participants a visible project boundary. It does not automatically synchronize their private memories or grant one role access to another role's files.

## Minimal organization

The included example has:

- `coordinator`: routes work, records decisions, and checks acceptance.
- `specialist-alpha`: implements inside an explicitly assigned repository.
- `specialist-beta`: reviews evidence and reports gaps.

One project, `sample-project`, has one thread. Its kickoff states scope, inputs, acceptance, prohibitions, and stop conditions. Its handoff records only facts that were checked.

## Runtime-neutral contract

Any runtime can implement this model if it can provide all of the following:

1. A durable, separately addressable role with its own configuration and conversation state.
2. A distinct messaging identity for that role.
3. Channel-level access control and a way to keep normal work out of unrelated channels.
4. A thread or equivalent conversation boundary for one project.
5. An explicit human approval point for external publication, credentials, and destructive actions.
6. A written handoff that is independent from model memory.

If a runtime cannot provide one of those objects, document the substitute and the capability that is lost. Do not rename a weaker mechanism and describe it as equivalent.

## Separation is not security

A separate conversation does not isolate memory, permissions, or files.

- Conversation separation means participants do not automatically share one transcript.
- Memory separation exists only where the runtime stores role state separately and no process copies it.
- Permission separation exists only where the runtime and operating system enforce it.
- Filesystem separation does not exist merely because two agents were told to use different directories.

The same user account, container, or mounted filesystem can make private files visible to every role. Treat role instructions as policy and user guidance, not as a sandbox.

## Shared versus role-owned information

Shared project information belongs in the project thread and its handoff record. It should be short, reviewed, and safe for every participant.

Role-owned information includes private memory, credentials, session transcripts, and local working files. Another role receives it only when the operator explicitly authorizes that transfer and the content is minimized.

## Optional and experimental features

Scheduling, voice, bots talking directly to bots, Hindsight and other external memory providers, browser automation, and cross-runtime adapters are optional. They are not required to operate the minimal organization and should be disabled until separately verified. Hindsight is the recommended optional memory layer for long-lived project recall; see [optional plugins](optional-plugins.md).

## Failure rules

Stop and ask the operator when:

- A requested action needs credentials, account creation, publication, or deletion.
- The project thread conflicts with the written task.
- A role cannot access an input without widening its file or network access.
- A verification command was not actually run.
- Another role's private state would have to be read or modified.
