# Methodology

[繁體中文](zh-TW/methodology.md) · [English](methodology.md)

## Task contract

Each input contains two equations over a magma. A true verdict requires Lean code proving that every magma satisfying the first equation also satisfies the second. A false verdict requires a Lean-checkable countermodel. The official judge accepts a certificate or returns one of four non-accepted states; model confidence and heuristic scores never count directly.

The final artifacts target two execution contracts:

- Solo launches a fresh solver process for each problem and communicates through JSON lines on standard input and output.
- Marathon sends a manifest of problems to one persistent process. The solver shares a global time and token budget and appends answers to a JSONL output file.

Both tracks submit one `solver.py` file below 500 KB.

## Certificate pipeline

The solver parses equations into an abstract syntax tree, renames variables canonically, normalizes equation orientation, and routes the row through an ordered set of bounded strategies. Every strategy either returns a replayable certificate candidate or abstains.

### Direct proof rules

The first lane handles reflexivity, direct substitution, singleton and constant consequences, and fixed rewrite templates. These checks are cheap and provide short proofs.

### Finite countermodels

The solver exhaustively searches small operations over `Fin 2` and `Fin 3`, then tests structured operations over larger finite carriers. One important family has the form

```text
x * y = a x + b y + c (mod n).
```

Candidate 6 added 645 deduplicated finite magmas from a public, revision-pinned Equational Theories source. The builder discarded equation identifiers and implication mappings, embedded only operation tables, and recorded a provenance hash. A table is used only after the solver checks that it satisfies the hypothesis and refutes the goal.

### Proof-producing search

Candidate 5 introduced bounded paramodulation. It standardizes parent variables apart, retains a proof DAG, bounds depth, term size, retained rules, processed candidates, and queue size, and renders Lean only after a universal target has been derived.

Candidate 7 added goal-directed paramodulation. It seeks a direct or symmetric target instance while replaying every proof edge from its AST parents. Fixed scoring and serial tie-breaks keep the search deterministic.

Symbolic narrowing and a goal-guided beam run after the paramodulation lanes. They use occurs-checked unification, bounded symbolic depth, proof-edge revalidation, and fixed pruning rules.

### H19 demodulating goal paramodulation

H19 combined an expanded replay-checked search with ordered forward/backward demodulation, tautology deletion, unit-equation subsumption, and deterministic goal-distance selection. It passed discovery, a one-shot disjoint validation, the 1,669-row public no-refit safety gate, and the released Order-5 no-refit safety gate. Those passes justified reuse of the mechanism; they did not authorize a private result claim by themselves.

### H22 waypoint controller

H22 tested a bounded controller that asks a model for typed proof waypoints, compiles the response into a constrained plan, and sends only generated certificates to Lean. Calibration and evaluation gates passed in its governed research lineage, followed by released-input safety checks. A later protected promotion attempt ended without terminal scientific evidence because the execution capacity was exhausted.

The final Aggressive artifacts include this bounded fallback. The Safe artifacts do not depend on it. Released final runs made zero model calls because deterministic lanes solved every row.

## Safe and Aggressive variants

Safe variants preserve the conservative deterministic production path and fail closed when no vetted certificate is available. Aggressive variants add validated deterministic payloads and the bounded H22 fallback. The variants share the same judge authority and cannot turn unverified model text into an accepted result.

On the released Order-5 Marathon study, Safe abstained on two rows and accepted 198/200. Aggressive accepted 200/200. On the combined 1,669 released rows, both accepted every row with zero tokens.

## Marathon adaptation

Marathon keeps one process alive for the full manifest. The Aggressive adapter deduplicates IDs, runs a deterministic first pass, sorts residuals, reserves time and token budget, and verifies model-derived certificates through Lean before appending them. The Safe adapter uses deterministic attempts only.

The process flushes and synchronizes appended answers so partial progress survives termination. Batch execution also allows caches and imported proof payloads to be reused across rows.

## Governed research workflow

Candidate 26 used a sequential gate system:

1. record the hypothesis, source roles, caps, splits, metrics, and terminal rule;
2. commit, push, and read back the frozen record;
3. implement provider-free contracts;
4. materialize only the authorized source or fixture;
5. run calibration once;
6. open a disjoint evaluation only when the frozen gate permits it;
7. preserve failures, invalid instrumentation, timeouts, and source shortages without relabeling them as scientific evidence.

This procedure reduced post-hoc tuning, but it also exposed the cost of weak measurement infrastructure. H51-H63 mostly investigated whether reliable, identity-bound trace data existed before attempting another ranking mechanism. Most ended blocked or unscored; H57 passed only its measurement-reliability and label-capacity questions.

## Cost and model use

The deterministic Candidate 1-19 work and final released-public runs used no paid provider calls in their recorded executions. Provider-backed H20-H27 research has ten positive-cost ledger entries totaling US$0.918012780. Model selection, request counts, and gate outcomes are preserved in the private governance evidence. No repository-wide zero-cost claim is valid.

## Soundness boundary

The official Lean judge is the result authority. Search heuristics, model outputs, cached tables, and public implication data are candidate generators. They cannot replace certificate checking. A run that never receives an accepted judge response contributes no solved row, even if its heuristic verdict was correct.
