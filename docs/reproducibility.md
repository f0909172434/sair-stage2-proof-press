# Reproducibility

## Frozen identities

Use these full SHA-256 values when reproducing a final artifact:

| Artifact | SHA-256 |
| --- | --- |
| Solo Safe | `a81025ac454e964365f5b53b1928af3d4e4276f374d62d5b05f34264afada85a` |
| Solo Aggressive | `faf8468e6183638d35607c3bf1ae0685da838f3bfed7009c9bd5b6402071e70a` |
| Marathon Safe | `05e3b837d8cdac8a0299fe66592bde787e57b10c50a0eefe24d6fdf9ae4f3d5c` |
| Marathon Aggressive | `c87e44bda89f08dad7a8a12147b28ba77a2fe288c3c3947c4dfe06b2154b8c21` |

The final audit used:

- official evaluator commit `817a4653bf762584931d49c6714c9fcfab7df66a`;
- Lean 4.33.1;
- Python 3.11 for packet and contract checks;
- repository branch `agent/final-24h-dual-track-sprint` at pre-publication audit base `56684f74569d21da043d4dc4a40e47ff9bae80bd`.

## Verification sequence

1. Clone the official evaluator and check out the exact commit above.
2. Install its pinned Lean/Mathlib toolchain.
3. Verify each final solver hash and byte count against `dist/final/FINAL_ARTIFACT_MANIFEST.json`.
4. Run `scripts/verify_final_upload_packet.py`. The script is an identity and packaging check; its pre-submission state fields are historical.
5. Run the focused final-artifact, layout, fast-path, and note contracts listed in the post-submission audit.
6. Run the official Solo harness for each Solo file and the official Marathon scorer for each Marathon file.
7. Record input source hashes, row counts, environment versions, accepted status counts, model/token use, output hashes, and a second-run projection when the claim depends on determinism.

On macOS, the official `lake env` discovery path once stalled. The recorded successful workaround used direct Lean/Lake 4.33.1 binaries and an explicit `JUDGE_LEAN_PATH` assembled from the official checkout's built dependencies. This is an environment workaround, not a solver change.

## Released sources

The 1,669-row combined study contains:

| Family | Rows |
| --- | ---: |
| `normal` | 1,000 |
| `hard1` | 69 |
| `hard2` | 200 |
| `hard3` | 400 |

Order-5 is a separate released 200-row source. Source roles and opened/blind state are tracked in `experiments/DATASET_ROLE_REGISTRY.json`.

## What cannot be reproduced from this repository alone

- The organizer's private evaluation inputs.
- The production portal and provider routing.
- A private score or rank.
- Exact Docker resource equivalence for every local macOS run.
- Raw protected journals that were deliberately kept outside the repository.

## Evidence hygiene

Do not commit raw private rows, prompts, model responses, request identifiers, browser state, credentials, or local scratch journals. New summaries should use repository-relative paths, omit team/account identifiers, and retain only the minimum provider telemetry needed for the stated claim.

Older sealed evidence includes absolute host paths. These records preserve historical reproducibility but are not publication-safe without a deliberate sanitization or history strategy.
