# Pre-registration CANONICAL: filtration stage of the fixed pair sector

Frozen 2026-07-19, BEFORE any canonical-sector measurement was computed.
Implements the authorised canonical test after the interface audit
(INTERFACE-AUDIT-oseries-q5a.md) and its three conceptual corrections.
No distance, dimension, or sensitivity value defined below has been evaluated at freezing time.

## Availability audit (required; all items published, none reconstructed)

- **Character c = 1**: textual — Q5a Appendix A and the O-series pipeline fix the central
  character e^{2πi/q}; Foundation fixes only c ≠ 0 (Stone–von Neumann uniqueness), the concrete
  c = 1 is the corpus-wide published convention. Partner: q − 1, handled by conjugation only
  (O17: ρ_{q−1} = conj(ρ_1)); never linearly mixed.
- **v₀ = uniform vector**: Foundation Level 3 leaves v₀ "given"; the published operational
  convention is the uniform state (O12 pipeline, `weil_batch_lut` acting on |uniform⟩). Recorded
  as the pipeline convention, not a new choice.
- **B_n**: BFS balls of the Cayley graph with the standard generating set (deterministic).
- **n₁(q)**: the PUBLISHED auto-calibrated saturation depths, CC-Note Table (reproducing O28):
  n₁ = {29: 4, 61: 8, 101: 11, 151: 13, 211: 14}. No recalibration, no threshold re-tuning.
  Honest note: n₁ was calibrated on the fingerprint-novelty curve (the pipeline estimator); it is
  nevertheless the corpus's only published depth and is imported as-is.

## Frozen objects

H_q = Ω_{n₁(q)}^{(1)} = span{ρ₁(g) v₀ : g ∈ B_{n₁(q)}} ⊂ C_q — TRUE orbit vectors of the Weil
action on v₀; fingerprint estimator vectors are excluded by construction.
Rank/basis: Gram-matrix accumulation over the orbit vectors of B_{n₁}, eigendecomposition,
tolerance σ > q·√ε_mach·σ_max (same frozen rule as B-v2); full singular spectrum stored.

## Analytic consistency prediction (derived before running; falsifiable by the run)

With v₀ uniform, (ρ₁(a,b,γ)v₀)(x) = q^{-1/2} e^{2πi(γ+bx)/q}: each orbit vector is a pure
Fourier mode e^{2πibx/q} times a scalar phase, so
Ω_n^{(1)} = span{ e^{2πibx/q} : b ∈ b(B_n) } with b(B_n) = {−n, …, n} (each generator step
changes the b-coordinate by at most 1), hence the prediction
**dim H_q = min(2·n₁(q)+1, q)**, i.e. {29: 9, 61: 17, 101: 23, 151: 27, 211: 29}.
The run must confirm this; a mismatch invalidates the implementation, not the corpus.

## Observables (frozen)

For each q ∈ {29, 61, 101, 151, 211}: dim H_q; dim H_q / q; relative distances
ε(g) = dist(g, H_q)/‖g‖ for:
- **B profiles**: Hermite ψ_n, n = 0..6, sampled on the balanced centered grid
  x_k = √(2π/q)(k − (q−1)/2) (same as v1/B-v2);
- **T profiles**: Fourier modes e^{2πimk/q}, m = 0..6, plus t₁ = 1 + cos(2πk/q) and
  t₂ = Σ_{|m|≤5} 2^{−|m|} e^{2πimk/q} (same as PREREG-T).

## Controls (frozen)

1. **Conjugation control**: build Ω_{n₁}^{(q−1)} from ρ_{q−1} and verify
   dist(conj(g), Ω^{(q−1)}) = dist(g, Ω^{(1)}) to machine precision for every test vector.
2. **Depth sensitivity**: depths n₁(q) − 1 and n₁(q) + 1, FIXED here, reported for all
   observables — sensitivity information ONLY; the main verdict is read at n₁(q) exclusively.

## Frozen convergence criteria (same numeric rules as v1/B-v2/T)

A profile family "converges" iff for every member: ε_{q,·} decreasing in q over the five primes
(at most one inversion < 10% relative) AND ε_{211,·} < ε_{29,·}/2; OLS rates reported with
residual std. Members with ε identically < 10⁻¹² at all q count as (trivially) convergent.
- "Rank non-trivial": dim H_q/q ∈ [0.05, 0.95] at q ∈ {151, 211}.
- "dim H_q/q → 1" branch applies if dim/q > 0.95 at both q = 151 and q = 211.
- **Plateau clause**: if for a family the values ε_{151} and ε_{211} differ by < 10% relative
  while both exceed 0.1, the family receives NO asymptotic verdict (plateau indistinguishable
  from slow convergence at available primes).

## Decision matrix (frozen, as authorised)

- B converges alone → route B.
- T converges alone → route T.
- both converge with non-trivial rank → the interface does not decide; return to the
  limit-operator comparison.
- neither converges → Q5 stays open at this interface.
- dim H_q/q → 1 → test asymptotically non-discriminant.
- data insufficient to distinguish convergence from plateau (plateau clause) → no asymptotic
  verdict for the affected branch; state it, do not force it.

## Archive contract

Deterministic script `canonical_sector_test.py`; raw CSVs (dims, distances, sensitivity,
conjugation control, singular spectra); PDF figure; provenance appended (same data commits;
published n₁ table cited); separate report RESULTS-CANONICAL.md. No modification of Q5a.
