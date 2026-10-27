# Optional plugins and tools

Hermes can run the core organization with profiles, messaging, and project threads alone. Plugins add capabilities, but each one adds installation, credentials, data storage, and failure modes. Enable only what the operator needs.

## Hindsight: recommended for durable projects

Hindsight is an optional Hermes memory-provider plugin maintained outside Hermes core. It is not required to create profiles or Discord bots, but it is recommended when a role must recall decisions across many project sessions.

Official Hermes documentation describes these Hindsight tools:

- `hindsight_retain`: store a memory and extract entities.
- `hindsight_recall`: search stored memories with multiple retrieval strategies.
- `hindsight_reflect`: synthesize an answer across related memories.

This is broader than Hermes built-in `MEMORY.md` and `USER.md`, which remain bounded prompt memory. Hindsight is useful for project decisions, rejected approaches, handoff facts, and long-running preferences. It does not replace the project thread or handoff record. The thread remains the shared human-readable record; Hindsight is role-owned recall.

### Boundary

- Activate it per profile with `hermes memory setup` or `memory.provider: hindsight`.
- Keep one memory bank per role unless the operator explicitly wants shared recall.
- Do not retain credentials, private transcripts, or unrelated business data.
- A recalled memory is evidence to check, not authorization to act.
- Cloud mode sends data to the provider. Local mode keeps the database under operator control but still requires a model provider for its processing.

The exact setup and configuration reference is the upstream Hermes integration documentation: <https://hindsight.vectorize.io/sdks/integrations/hermes>.

## HeartBeat 2.0: optional follow-up

HeartBeat can schedule a bounded follow-up or watch a file, process, URL, or command. It is useful when a role promises to return after a long job. It is not part of the minimal organization and must not be used as continuous monitoring.

Use it only with an explicit purpose, deadline, and maximum number of wakes. A wake is another model turn; it is not a free background process.

## Jev: optional decision aid

Jev is an optional plugin for classifying or choosing among non-sensitive options. It can help compare public evidence or generic project choices. It is not required for routing work, and its output is not approval or proof.

Do not send it credentials, private project data, personal records, or complete private transcripts. If it is unavailable, continue with local reasoning.

## Coding tools

The examples do not require a particular coding CLI. A specialist role may use Codex, Claude Code, Antigravity, Grok, or another tool available to Hermes or OpenClaw when the operator has installed and authorized it. The role must still report the diff and test results itself. A coding tool's completion message is not acceptance.

For the Codex lane, use [Codex development](codex-development.md). Hermes writes the bounded task, Codex works in the assigned Git repository, and Magpie is an optional model router. Magpie does not authorize file changes, commits, or publication.

## Selection rule

Add an optional component only when it provides a capability the core model lacks. Record its version, data location, credential requirement, and removal procedure before using it in a durable role.
