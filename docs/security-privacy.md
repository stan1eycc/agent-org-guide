# Security and privacy

## Publication rules

- Use fictional role names such as `coordinator`, `specialist-alpha`, and `specialist-beta`.
- Use placeholders such as `YOUR_DISCORD_CHANNEL_ID` for every operator-specific value.
- Do not include real names, usernames, IDs, hostnames, addresses, paths, emails, organization names, or account identifiers.
- Do not include private prompts, memories, schedules, business workflows, or operational history.
- Omit a field rather than replacing a secret with a shortened or disguised real value.
- Keep live `.env`, tokens, sessions, and credentials outside this repository.

## Authorization model

An allowlist determines who may invoke a role. Channel permissions determine where that identity can read and post. Profile separation determines which Hermes state is loaded. None of these replaces the others.

Set the narrowest policy that still lets the operator run the workflow:

- Prefer specific user IDs over allowing everyone.
- Prefer one workplace channel per role over server-wide access.
- Prefer explicit mentions over free response.
- Prefer a project thread with only assigned roles over a public channel.
- Keep direct bot-to-bot messages disabled until a separate design explains how loops and shared context are controlled.

## Instruction limits

Role text can tell a model what it should refuse, but it cannot prevent code or a person from reading a file available to the process. Mount only the data required for the assigned project. Run untrusted or high-impact work in a separate OS user, container, or host where that isolation has actually been verified.

## Secrets

Discord bot tokens, model provider keys, OAuth files, and session stores are credentials. Do not place them in `config.yaml`, command arguments, screenshots, handoff records, or prompts. Rotate a token immediately if it appears in a transcript or Git history.

## Shared threads

A shared project thread is visible to every participant invited to it. Do not paste private debugging output there. Summarize the result and keep raw evidence in the authorized private location.

## Threat checks before publication

The automated scan detects common credential formats, private-key blocks, IP addresses, home paths, Discord snowflakes, and email addresses in content or paths. It also rejects prohibited filenames in the working tree and Git index. It does not understand private prose, organizational context, or whether a name is real. A passing scan does not replace human review or Git history inspection.

For the collaboration candidate, `python3 -B scripts/audit_candidate.py` additionally inventories ignored and hidden working files, rejects unreviewed opaque payloads and symlinks, checks local links and extended attributes, and scans all local Git object paths before opening content; path-bound non-prohibited blobs plus commit/tag messages, index entries and tree paths. Its URL-domain exceptions are reviewed public-source categories, not proof that a URL path contains no private identifier. Review file names, source URLs and prose manually. Credential-like working and historical paths are refused without opening their contents. Unbound local objects outside refs and index are inventoried without reading or deleting; a normal explicit ref push does not transmit them, and the report does not claim their contents were scanned.

The inherited public repository has author/committer/tagger identity metadata. The auditor reports its category and object location without printing identities. Those records are not erased or reclassified as anonymous by adding this feature. No history rewrite is authorized. A future publication must explicitly retain or remediate that known metadata according to the owner's approved privacy scope.

The optional collaboration thread uses relaxed human reply triggers. Transport-level rejection of bot authors is required; a prompt alone does not enforce it. The existing strict-mention project example remains available. See [collaboration](collaboration.md) for scope, fan-out and version-sensitive behavior.
