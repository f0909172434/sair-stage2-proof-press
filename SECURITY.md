# Security policy

## Supported state

Security fixes apply to the current default publication branch and the four frozen final artifacts. Historical experiment code is retained for reproducibility and may be inactive. A report about historical code should state whether the path remains reachable in a current workflow.

## Reporting

Do not publish credentials, private competition rows, personal identifiers, or exploitable details in a public issue. Contact the repository owner through the GitHub account associated with this repository and request a private channel. If GitHub private vulnerability reporting is enabled after publication, use that interface.

Include the affected path, revision, entry point, realistic attacker, data flow, impact, and any safe reproduction steps. Never attach live keys, raw private datasets, browser sessions, or provider journals.

## Security invariants

- Lean acceptance, not model output, determines a solved row.
- Provider credentials stay in organizer-managed routing, approved secret stores, or process environments and are never committed.
- Private evaluation rows and raw provider journals remain outside the repository with owner-only permissions.
- Research scratch roots that may contain rows, prompts, model responses, certificates, or judge feedback must be owner-only directories. Sensitive files must be owner-readable and owner-writable only; callers must not place them under shared or symlink-controlled paths.
- Public evidence uses repository-relative paths and omits team/account identifiers, authorization quotations, and unnecessary host/provider telemetry.
- Write-enabled self-hosted workflows execute only trusted, hash-bound source.
- Final artifact hashes and portal mappings remain bound to the same four files.

## Publication boundary

The private evidence repository contains historical authorization text, operational metadata, host paths, and personal Git metadata. A public release must use a sanitized tree and sanitized or squashed history. Removing those fields only in a later commit does not remove them from earlier Git objects.
