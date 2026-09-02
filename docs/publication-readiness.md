# Publication readiness

## Decision

The full evidence repository and its existing Git history are not safe to make public as-is. A sanitized companion repository is ready to proceed through the release gate below.

Competition status is not itself a publication blocker. On 2026-09-02 the overview still displayed `EVALUATING`, while the official Contributor Network exposed a `Publish Item` flow and publicly displayed Stage 2 Solo and Marathon solver source posted from 2026-05-11 through 2026-09-01. That is direct official-platform evidence that solver sharing is supported during this period. It does not imply evaluation completion or disclose a private score or rank.

The remaining blocker applies to this repository's history, not to a clean release. Git metadata contains non-noreply personal/local email addresses, and old commits and remote branches retain team identifiers, absolute home paths, private authorization text, credential-store metadata, provider telemetry, and runner fingerprints. Cleaning only the current branch would not remove them from a public repository.

## Completed checks

- Current tracked tree: 1,850 files scanned for common key, token, private-key, personal-path, team, and authorization markers.
- Git patch history: 1,537 commits scanned for common private-key and provider/cloud token signatures.
- Strong secret signatures found: 0.
- Current absolute home-path references: 1,255 occurrences in 368 tracked files.
- Current team-identifier references: 13 occurrences in 13 tracked files.
- Git author/committer metadata: five unique addresses, including GitHub noreply, one Gmail address, and one local machine address.
- Standard source security scan: three independent review packets found two medium and several low publication risks. No literal credential was found.

## Validated publication risks

- Medium: H20-H22 research runners can create raw scratch journals with group/world-readable defaults under a permissive umask. This matters to shared local machines and must be fixed in the current code.
- Medium: sealed evidence preserves verbatim private authorization text and one source-conversation identifier. A later deletion commit cannot remove those bytes from public Git history.
- Low: current manifests, handoffs, and evidence expose personal absolute paths, a stable team identifier, runner names, exact installation layouts, and unnecessary host fingerprints.
- Low: committed provider evidence contains more timing, token, spending, and credential-store metadata than public reproducibility needs.
- Low: reachable Git history contains a personal Gmail address and a workstation-derived local address in addition to noreply identities.

These checks do not prove the absence of every possible secret. They establish that the known risks are metadata/privacy and old local-journal controls, not a detected live API key.

## Required release gate

Before publishing a clean companion repository:

1. Record the live Contributor Network publication evidence and keep `EVALUATING` separate from publication permission and private-result claims.
2. Finish the Standard security scan and close or document every finding.
3. Build a sanitized, squashed repository from an explicit allowlist while keeping this evidence repository private and preserving a provenance map offline.
4. Exclude historical branches and tags; the new public repository starts from one reviewed root commit.
5. Exclude team identifiers, authorization quotations, credential-store service details, personal absolute paths, source-conversation identifiers, and unnecessary runner/provider telemetry.
6. Verify all four frozen solver hashes are unchanged.
7. Run final code, website, document, license, link, secret, and metadata checks.
8. Push the clean snapshot, verify the repository reports `PUBLIC`, and read back representative files from GitHub.
9. Deploy GitHub Pages and verify the site, assets, and paper through anonymous HTTPS requests.

## Historical evidence policy

Sealed scientific records should not be silently rewritten because their hashes and remote readbacks are part of the research record. A public release should either:

- keep the private evidence repository intact and publish a sanitized, provenance-linked release repository; or
- perform a documented history rewrite that replaces sensitive fields while preserving an offline private archive and a mapping of old to new evidence identities.

The user authorized a public GitHub release, but did not request a destructive force-push or deletion of historical branches. The security review found enough hash-bound private metadata that a clean public export is safer than changing this evidence repository's visibility.
