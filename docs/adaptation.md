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

## Another agent runtime

For OpenClaw or any other runtime, write an explicit mapping from each architecture object to a runtime object. At minimum, identify where role configuration, conversation history, memory, credentials, and tool permissions are stored. If those stores are shared, say so plainly and do not describe the setup as profile-isolated.

Test the runtime with fictional data:

1. Create two roles.
2. Give them separate credentials and workplaces.
3. Start one project and one unrelated control project.
4. Ask each role for the other's private marker.
5. Confirm that no private marker crosses unless the operator explicitly shared it.
6. Record the runtime version and every failed assumption.

## What not to copy

Do not copy a working private deployment wholesale. Rebuild it from the templates, using new fictional or operator-owned values. Copying a profile also copies credentials, memories, sessions, and local paths.
