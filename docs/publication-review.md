# Publication review — v0.2.0

Reviewed on 2026-10-27. This report describes the source candidate before its version commit. Remote publication is verified separately after the approved push; this report does not predeclare that operation successful.

## Scope and authority

Extend the existing Agent Organization Guide with a generic multi-bot collaboration pattern. Preserve the runtime-neutral architecture, original strict-mention example and existing MIT license. The owner approved completing the work, committing and pushing to the existing repository, and assigning the next version. No live Profile, core, gateway, service, model route or production configuration was changed. No new project or remote is part of this release.

## Delivered content

- Collaboration contract: participants, accountable owner, channel/thread mentions, human-trigger fan-out, bot-trigger rejection, bounded contributions, independent review, synthesis and final delivery.
- Three-role example: coordinator-only project thread, two-specialist collaboration thread under separate private parents, non-secret setting fragments and an ownership manifest.
- Collaboration kickoff/handoff templates, architecture diagram, disposable installation procedure, verification matrix and troubleshooting/recovery guide.
- Evidence register separating saved rules, actual settings, observed behavior, proposed conventions and locally checked synthetic behavior.
- Optional offline checks, complete candidate inventory, Git object/path audit and sanitized failure reporting.

## Executed checks

- Existing publication-manifest scanner: PASS, 9 pattern groups.
- Extended candidate auditor: PASS for reviewed source content, local links, JSON/Python syntax, hidden/ignored-file inventory, reviewed source-domain categories and extended attributes; 11 pattern groups.
- Fresh synthetic example: PASS, 24 admission cases plus three setting fragments, ownership assertions and byte-identical copy into a fresh temporary directory. This checks a proposed contract, not Hermes adapter code.
- Targeted synthetic audit probes: PASS for eight protected path categories, historical and legacy-entrypoint refusal before content reads, sanitized diagnostics and unreferenced-object exclusion. No real secret payload was used.
- Git whitespace check: PASS.
- Manual content review: generic role labels, consistent placeholders, official public citations, no private production roster, channel name, workflow history, credential, local deployment path, attachment, image or opaque payload introduced. Existing optional-tool and MIT content retained.

The final candidate inventory and object counts are recorded by executing the commands in [verification](verification.md), rather than frozen here before this report itself is added. A scan is evidence within its stated scope, not a proof that every possible secret format is detectable.

## Independent review and repairs

Independent read-only review used Codex CLI 0.163.0. It identified historical blob screening order, unsafe path diagnostics, incomplete protected path categories, the legacy scanner opening refused paths, inconsistent gateway-source attribution and an obsolete example command. These were corrected. A further focused review identified protected category filenames and symlink ancestors in the legacy entrypoint; those were also corrected and exercised with fresh synthetic refusal probes. Independent review did not issue a blanket approval; the final repairs were verified by the owning agent with targeted execution. Offline checks were rerun. No CLI completion message is treated as runtime acceptance.

## Historical and metadata limitations

All local Git objects are inventoried. Blob content is read only after path classification. Path-bound allowed blobs, commit/tag messages, index entries and historical tree paths are checked. Known inherited author/committer/tagger identity records are reported by category and object location, without echoing identities; they remain in the already-public history under the owner's existing publication identity policy. The entire repository is therefore not claimed to have anonymous Git metadata. No history rewrite was performed or authorized.

One local blob has no binding in any inventoried tree/index and is not reachable from a ref. It is inventoried without reading or deleting it. It is not included by the approved explicit commit/tag push. This is an explicit content-audit gap for local storage, not an unscreened object in the selected publication ancestry. Re-inventory before any later publication; do not import arbitrary loose objects.

No extended attributes or opaque working payloads were observed in the reviewed candidate. Git's local operational files, reflogs, hooks, remotes and credential configuration are not distributed source artifacts and are not copied into this release. Object contents and publishable commit/tag metadata are assessed separately.

## Runtime limitations

Hermes reports a modified local build, not a reproducible clean runtime pin. Official documentation may be ahead of that build. No installation, credentials, live Discord permission, inbound reply, thread membership, bot-author rejection, private-audience enforcement, service recovery or third-party memory integration was tested. The full live matrix remains NOT RUN.

Relaxed thread mentions may affect other joined threads. Human messages can wake both specialists. Per-user and per-bot sessions may differ; explicit human-mediated handoffs are required. Profiles, threads, prompt rules and synthetic guards are not OS security isolation. OpenClaw remains an unverified adaptation.

## Release disposition

Suitable for publication as a documentation-reviewed v0.2.0 with the above limitations, after the final source/index scan and version commit. It is not certified as a live reproduced deployment. Push only the reviewed commit and corresponding annotated tag to the existing approved remote, then read back both exact refs. No separate GitHub Release page or unrelated deployment is required by this change.
