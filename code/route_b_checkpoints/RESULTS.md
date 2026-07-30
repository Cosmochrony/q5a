# [v1 — SINGLE-CENTRAL-CHARACTER PROJECTOR] Results and verdict — pre-registered checkpoints [H-w′] and [H-Π3]

Evaluated 2026-07-19 strictly against PREREGISTRATION.md (frozen before measurement).
Raw data: results_hw.csv, robustness_hw.csv, results_hpi3.csv; figure fig_hw_hpi3.pdf;
provenance (data SHA256, repo commits, slopes): PROVENANCE.md.
Reproduction: `PYTHONPATH=<numpy+matplotlib> python3 route_b_pipeline_tests.py`.

## [H-w′] — PASSES all four frozen criteria

1. Boundedness: the four sequences lie in [1.52, 2.01] over all five primes. PASS.
2. Pair symmetry: a_q(s⁺) = a_q(s⁻) exactly at every q (this is in fact an identity:
   ‖(ρ⁻¹−I)u‖ = ‖(ρ−I)u‖ for unitary ρ); r_211 = 0 < 0.10. PASS (vacuously strong).
3. Convergence without extra renormalisation: log-log slopes (q ≥ 61) are +0.072 (Y-sector,
   residual std 0.095) and +0.000 (X-sector); max/min over {101, 151, 211} is 1.315 (Y) and
   1.000 (X), both < 2. PASS.
4. Robustness: verdicts unchanged across n_cut+3, EPS_GS/10, and 5-block means (all values in
   [1.52, 2.01]); conjugate blocks unavailable in the stores for q ≥ 61 (allowed by the
   pre-registration). PASS.

Measured limits: B = a(X_c) = 2.000 exactly at every q; A = a(Y) fluctuates in [1.52, 2.00]
with no q-power trend.
Diagnostic (recorded, non-verdictal): a_q/h² grows ≈ linearly in q, i.e. the admissible
fingerprint vectors are NOT balanced-smooth — the weights are O(1) because the vectors are
asymptotically decorrelated at lattice scale (the value 2 is the full-decorrelation value).

## [H-Π3] — FAILS criterion 1, unambiguously

- q ∈ {29, 61, 101}: the Gram–Schmidt span has FULL rank (rank = q), so Π_q = I and
  ε_{q,n} ≈ 10⁻¹⁶ — a vacuous pass (the filter is not yet a proper projection at these q).
- q = 151 (rank 77): ε_{151,n} ∈ [0.52, 0.75] for n = 0..6.
- q = 211 (rank 157): ε_{211,n} ∈ [0.40, 0.54].
- Frozen criterion 1 requires ε decreasing in q and ε_{211,n} < ε_{29,n}/2: FAIL for every n.
- Error separation is clean: window errors ≤ 10⁻¹¹ and discretisation errors ≤ 10⁻¹⁵ at all
  (q, n) — the deficiency is pure projection: the admissible span at the stored shell depths
  does not contain the balanced-smooth profiles.

## Verdict per the frozen stop criterion

[H-Π3] fails ⟹ **route T is adopted** ("retour à la route T sans ajustement post hoc").

## Design-flaw disclosure (transparency, not a rescue)

The frozen operationalisation of Π_q used the Gram–Schmidt span of the FIRST stored block only
(one central character c₁).
The paper's Π_q averages/spans over ALL characters c ∈ (ℤ/qℤ)^×; a union-span over many
characters would have strictly larger rank and could behave differently on balanced profiles.
Under the binding pre-registration this cannot alter today's verdict.
If a corrected operationalisation is wanted, it requires a NEW pre-registration (v2: union-span
Π_q over all stored blocks/characters, same frozen thresholds), explicitly authorised, with
today's failure reported alongside whatever v2 yields.

## Two route-agnostic facts worth keeping

1. The weight measurement is scale-blind and feeds route T equally: with a_q(s) → ≈2, the
   torus form (q^{+2} prefactor, Y-sector) has a positive coefficient; the X-sector converges
   unrescaled to the multiplication operator with coefficient ≈ 2.
2. The [H-Π3] failure is specific to BALANCED (width √q) profiles; route T's analogous
   recovery-sequence question concerns O(1)-DFT-frequency (torus-smooth) vectors, which this
   run did not test and which require their own pre-registered test before Q5a 3.0 (route T)
   can rely on a Π-approximation property.
