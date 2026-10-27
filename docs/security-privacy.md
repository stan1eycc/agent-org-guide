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
