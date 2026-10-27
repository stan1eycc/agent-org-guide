# Project kickoff: sample-project

- Thread: `sample-project`
- Operator: `YOUR_OPERATOR_NAME`
- Assigned roles: coordinator, specialist-alpha, specialist-beta
- Status: example

## Outcome

Create a small documentation change in `YOUR_REPOSITORY_PATH`, review it, and produce a handoff without publishing it.

## Scope

- Included repository: `YOUR_REPOSITORY_PATH`
- Included work: update the named document and verify its local checks.
- Explicitly excluded work: commits, pushes, deployment, credential changes, and edits outside the named repository.

## Inputs

- The public task statement posted in this thread.
- The repository files named in the assignment.

## Acceptance

1. The requested document change is visible in the assigned repository.
2. The named local check has been run, with its result recorded.
3. The review states `pass`, `pass with evidence gaps`, or `fail`.
4. No secret or personal information appears in the project thread.

## Prohibitions

- Do not read or copy credentials, private sessions, memories, or unrelated business files.
- Do not widen filesystem or channel access to work around a missing input.
- Do not treat this example as approval to publish.

## Stop conditions

Stop if the repository path, assigned role, or acceptance check is missing. Report the missing item and wait for the operator.

## Assignment

| Role | Task | Output | Done when |
|---|---|---|---|
| specialist-alpha | edit the assigned document | change summary and check result | requested change and named check are recorded |
| specialist-beta | review the change | review result | findings and evidence gaps are explicit |
| coordinator | maintain this project record | handoff | decision, evidence, and approvals are separated |
