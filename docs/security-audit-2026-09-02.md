# Security and publication audit, 2026-09-02

## Scope and result

A Standard Codex Security review audited repository revision `56684f74569d21da043d4dc4a40e47ff9bae80bd` for publication risks. All 1,850 tracked files received pattern scanning. Publication-relevant runners, governance records, manifests, workflows, provider evidence, and final artifact contracts received focused source review.

The scan completed with five reportable findings:

| Severity | Finding | Current disposition |
| --- | --- | --- |
| Medium | H20-H22 historical raw scratch journals inherit process permissions and can be readable by another local account under a permissive umask. | Historical tools are inactive and hash-bound. Keep private or omit from a public export; use 0700 directories and 0600 files in any replacement. |
| Medium | Governance evidence contains verbatim private authorization text and one conversation identifier. | Requires sanitized or rewritten history before publication. |
| Low | Manifests, handoffs, and readback contain personal absolute paths and a stable team identifier. | Replace with relative paths in a clean public export. |
| Low | Self-hosted evidence exposes runner names, installation layout, and full platform fingerprints. | Retain only normalized reproducibility fields in a public export. |
| Low | Provider evidence retains more timestamps, latency, token, spending, and credential-store metadata than public claims need. | Publish a minimum allowlisted projection. |

No literal API key, provider token, private key, password, or private evaluation row was found. The scan reports partial semantic coverage because the repository contains many generated evidence blobs; every tracked path was pattern-scanned, but not every blob received complete semantic review.

## Separate Git history audit

The current private history contains personal email and workstation-derived Git metadata. A normal cleanup commit or `.mailmap` does not remove the raw commit-object fields. Remote branches and tags also retain old evidence bytes.

The preferred release route is:

1. keep this hash-bound evidence repository private;
2. treat the official Contributor Network's live solver-sharing surface as the publication authority, while retaining `EVALUATING` only as a limit on private-result claims;
3. create a new, squashed public repository from an allowlisted tree;
4. retain a private provenance map from public files to original evidence hashes;
5. verify anonymous access only after the sanitized repository passes the same secret, metadata, license, link, hash, and test gates.

A history rewrite of this repository would change sealed commit identities and requires an explicit destructive-change decision.

## Claim boundary

This audit establishes publication risks and the absence of common literal-secret signatures in the reviewed material. It does not prove that no undiscovered secret exists, and it does not establish a private competition score or rank.
