# Reproducibility

[繁體中文](zh-TW/reproducibility.md) · [English](reproducibility.md)

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

## Start with the public snapshot

Python 3.11+ and the standard library are sufficient; no model, API key, or Lean installation is needed:

```bash
python3 tools/verify_public_snapshot.py --replay-candidates
python3 tools/test_public_snapshot.py
```

This checks all four frozen solver hashes, byte counts and Python syntax against `public-snapshot.json`, then replays three tiny synthetic candidate-generation cases. Generated candidate text is not Lean acceptance or a new competition evaluation.

## Rerun with the official evaluator

1. Clone the [official evaluator](https://github.com/SAIRcompetition/equational-theories-lean-stage2), check out the full commit above, and install its documented Lean/Mathlib environment.
2. Run the public identity check, then use the appropriate `dist/final/` solver with the official Solo harness or Marathon scorer and evaluation inputs you can access.
3. Record input hashes, row counts, environment versions, accepted statuses, model/token use and output hashes. Repeat when making a determinism claim.

The historical full workspace's `FINAL_ARTIFACT_MANIFEST.json`, `verify_final_upload_packet.py`, contract tests and dataset role registry are not included in this public snapshot. They are not executable reproduction steps for this checkout.

On macOS, the official `lake env` discovery path once stalled. The recorded successful workaround used direct Lean/Lake 4.33.1 binaries and an explicit `JUDGE_LEAN_PATH` assembled from the official checkout's built dependencies. This is an environment workaround, not a solver change.

## Released sources

The 1,669-row combined study contains:

| Family | Rows |
| --- | ---: |
| `normal` | 1,000 |
| `hard1` | 69 |
| `hard2` | 200 |
| `hard3` | 400 |

Order-5 is a separate released 200-row source. The full source-role and opened/blind registry belongs to the historical workspace and is not included in this public snapshot.

## What cannot be reproduced from this repository alone

- The organizer's private evaluation inputs.
- The production portal and provider routing.
- A private score or rank.
- Exact Docker resource equivalence for every local macOS run.
- Raw protected journals that were deliberately kept outside the repository.

## Evidence hygiene

Do not commit raw private rows, prompts, model responses, request identifiers, browser state, credentials, or local scratch journals. New summaries should use repository-relative paths, omit team/account identifiers, and retain only the minimum provider telemetry needed for the stated claim.

Older sealed evidence includes absolute host paths. These records preserve historical reproducibility but are not publication-safe without a deliberate sanitization or history strategy.
