# Claim boundaries

## Evidence hierarchy

Use the narrowest applicable label.

| Label | Required evidence | Allowed claim |
| --- | --- | --- |
| Released-public verified | Exact solver hash, released source identity, official evaluator identity, Lean-accepted output | The cited solver accepted the cited released rows. |
| Compatibility pass | Exact toolchain/protocol/package contract | The artifact ran under that environment or contract. |
| Measurement-only pass | Frozen instrumentation question and valid result | The measurement substrate answered that bounded question. |
| Scientific fail | Preregistered scientific metric, valid source, valid execution, terminal gate | The scoped mechanism failed the stated gate. |
| Governance blocked | Missing or contradictory authority/identity/gate | No scientific conclusion. |
| Source or capacity blocked | Required rows or labels did not exist | No scientific conclusion about the mechanism. |
| Instrumentation invalid | Observer, identity, or schema did not measure the frozen target | No scientific conclusion. |
| Preregistration-only | Remotely sealed plan without authorized execution | Only the planned hypothesis and decision rule are established. |
| Formal submission readback | Portal-visible matching entry | The entry was submitted. |
| Official result | Organizer-published score or rank | No such evidence is present yet. |

## Claims supported now

- Four exact final artifacts were submitted and later appeared in the portal.
- All four accepted 1,669/1,669 released rows under the recorded official local evaluator with zero model use.
- Marathon Aggressive accepted 200/200 released Order-5 rows; Marathon Safe accepted 198/200 and abstained twice.
- H45 and H49 are valid scoped scientific negative results.
- H57 passed its bounded measurement-reliability and label-capacity questions.
- Candidate 28 was preregistered and remotely read back but not implemented or evaluated.

## Claims not supported

- Any private score, rank, prize, or final leaderboard position.
- Evaluation completion, a private score, or rank while the official page says `EVALUATING`. This does not prohibit solver publication: the official Contributor Network separately exposes Stage 2 solver sharing.
- General hidden-distribution superiority of Aggressive over Safe.
- A positive solver gain from Candidate 28.
- A model-capability conclusion from H10, H21, H22 protected promotion, H32, or any invalid/blocked execution.
- A repo-wide zero-cost research program.
- Equivalence between a local compatibility smoke and the production sandbox.

## Negative-result integrity

A source shortage, timeout, governance contradiction, or invalid observer does not falsify the proposed mathematical mechanism. The correct terminal description is the recorded operational failure. This distinction is retained throughout the ledger and the paper.

Compatibility passes also remain narrow. H35, H37, and H43 show that specific evaluator, dependency, or Marathon paths functioned; they do not measure accepted count on hidden rows.

## Submission-state precedence

`dist/final/FINAL_ARTIFACT_MANIFEST.json` and `dist/final/SUBMISSION_HANDOFF.md` were frozen before formal submission. Their `external_actions` fields describe that earlier moment. For whether submission later occurred, the authoritative repository record is `dist/final/benchmarks/formal_submission_readback_20260830_2023.json`.
