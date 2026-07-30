# Pre-registration T: toric approximation test (same union-span projector)

Frozen 2026-07-19, BEFORE any T measurement was computed.
Companion to PREREG-B2.md (same projector Π_q, same tolerance, same termination rules, same
decision matrix); distinct report.

## Test vectors (frozen before computation)

Torus grid x = k/q, k = 0..q−1 (native scale for route T; no window, no centering needed).

1. **Pure Fourier modes**: g_m(k) = e^{2πi m k/q} for the fixed list m ∈ {0, 1, 2, 3, 4, 5, 6}.
   These sample e^{2πi m x} exactly; aliasing is exactly zero for |m| < q/2, so the sampling
   (discretisation) error is identically 0 by construction — reported as such.
2. **Smooth trigonometric combinations** with frozen coefficients:
   - t₁(x) = (1 + cos 2πx)/‖·‖ (coefficients (1, ½, ½) on m = 0, ±1);
   - t₂(x) = Σ_{|m|≤5} 2^{−|m|} e^{2πi m x}/‖·‖.
   Sampled at x = k/q; again exact (all |m| < q/2), so ε is a pure projection quantity.

## Observables and thresholds (frozen)

ε^T_{q,m} = ‖(I − Π_q) g_m‖/‖g_m‖ for the seven Fourier modes, and ε^T_{q,tⱼ} for t₁, t₂;
same primes q ∈ {29, 61, 101, 151, 211}; ranks and rank/q reported (same run as B-v2).

**Pass criteria (same rules as v1/B-v2):**
1. for each fixed m (and each tⱼ): ε^T_{q,·} decreasing in q (one inversion < 10% relative
   allowed) and ε^T_{211,·} < ε^T_{29,·}/2;
2. OLS rate β > 0 with residual std reported;
3. error separation: sampling error is exactly 0 (stated above); window error not applicable on
   the torus; ε is pure projection deficiency.

**Non-discriminance clause.** Identical to B-v2: if Π_q = I at every prime or rank/q → 1, the
test passes formally but is NON-DISCRIMINANT and must be announced as such.

**Decision matrix.** As in PREREG-B2.md (joint, frozen).

## Archive contract

Shared deterministic script `union_span_tests.py` (one run produces both tests' raw data — the
tests are conceptually parallel but reported separately); raw CSV results_T.csv; PDF figure;
separate report RESULTS-T.md.
