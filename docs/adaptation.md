# Adapting this guide

## Documentation-reviewed reference

The Hermes plus Discord reference is the only implementation path checked for this release. It still needs live-server validation by each operator because no Discord account or server is bundled here.

## Another messaging service

Replace Discord channels and threads with the closest native equivalents. Before calling it compatible, test:

- Distinct identities and credentials.
- A durable room or channel permission boundary.
- A project conversation boundary equivalent to a thread.
- Mention or direct-address behavior.
- Whether multiple users share one transcript.
- Revocation: removing access, stopping the process, and rotating credentials.

## OpenClaw mapping

OpenClaw can implement the architecture without using Hermes commands. Map the objects explicitly:

| Architecture object | Required OpenClaw answer |
|---|---|
| Durable role | Which persisted agent, workspace, or instruction file represents one role |
| Messaging identity | Which chat account belongs to that role and where its credential is stored |
| Workplace | Which room or channel is normally used to address that role |
| Project thread | Which conversation, topic, or session is dedicated to one project |
| Shared handoff | Which document all assigned roles can read |
| Role memory | Which memory namespace belongs to one role and is excluded from the others |

Do not describe OpenClaw as tested by this repository. After the mapping is written, run the fictional-data separation test below and record the OpenClaw version and every failed assumption.

Test the runtime with fictional data:

1. Create two roles.
2. Give them separate credentials and workplaces.
3. Start one project and one unrelated control project.
4. Ask each role for the other's private marker.
5. Confirm that no private marker crosses unless the operator explicitly shared it.
6. Record the runtime version and every failed assumption.

## What not to copy

Do not copy a working private deployment wholesale. Rebuild it from the templates, using new fictional or operator-owned values. Copying a profile also copies credentials, memories, sessions, and local paths.
