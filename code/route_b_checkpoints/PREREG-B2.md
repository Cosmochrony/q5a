# Pre-registration B-v2: exact paper projector (union span over all central characters)

Frozen 2026-07-19, BEFORE any B-v2 measurement was computed.
Distinct from v1 (single-central-character projector, kept in full as a labelled negative result).
No ε value, rank value, or singular value defined below has been evaluated at freezing time.

## Projector (frozen)

**Character set.** All central characters c₁ ∈ {1, …, q−1} (the full (ℤ/qℤ)^×).
For each c₁, the canonical block is (c₁, c₂, c₃) with the deterministic rule
c₂ = 1, c₃ = 1 if c₁ + 2 ≢ 0 (mod q), else c₃ = 2 (enforcing the pipeline constraint
c₁ + c₂ + c₃ ≢ 0).
Robustness variant (reported, non-verdictal): union over all STORED blocks of the npz stores.

**Depths.** Shells d = 0, 1, 2, … accumulated up to the stored campaign maximum
n_max(q) = len(ns) − 1 from the npz store, with two exactness-preserving termination rules,
declared here:
1. early stop when the numerical rank reaches q at the frozen tolerance (the span is then all of
   C_q; adding vectors cannot change any ε);
2. a compute budget of 5·10⁶ fingerprint vectors per prime; if the budget is reached before the
   rank trajectory stabilises (rank unchanged over the last two depths) the run is declared
   BUDGET-TRUNCATED and reported as such (not silently passed).

**Orthonormalisation method (frozen).** Gram-matrix accumulation: G = Σ_chunks VᴴV (exact q×q),
eigendecomposition of G; the projector Π_q is the projector onto the span of eigenvectors with
σ_i = √λ_i above tolerance.
Rank tolerance (frozen, machine-precision based, Gram squaring acknowledged):
σ_i > τ_q := q · ε_mach^{1/2} · σ_max, with ε_mach = 2⁻⁵².
The FULL singular spectrum (all q values σ_i) is stored per prime; no block and no singular value
may be discarded after inspection.

## Observables and thresholds (frozen — identical to v1)

Same primes q ∈ {29, 61, 101, 151, 211}; same balanced grid h = √(2π/q),
x_k = h(k − (q−1)/2); same Hermite indices n = 0..6; ε_{q,n} = ‖(I−Π_q) g_{q,n}‖/‖g_{q,n}‖ with
g_{q,n}(k) = ψ_n(x_k).
Report simultaneously: ε_{q,n}, rank Π_q, rank Π_q / q, and the singular-value spectrum.
Window and discretisation errors: identical definitions to v1, reported separately.

**Pass criteria (identical to v1):**
1. for each n ≤ 6, ε_{q,n} decreasing in q (one inversion < 10% relative allowed) and
   ε_{211,n} < ε_{29,n}/2;
2. OLS rate β_n > 0 with residual std reported;
3. error separation reported.

**Non-discriminance clause (frozen, per instruction).** If Π_q = I (rank = q) at every prime, or
rank/q → 1 along the available primes, the test PASSES FORMALLY but is declared NON-DISCRIMINANT:
it demonstrates no admissible selection of balanced profiles, and will be announced as such — it
cannot on its own validate route B.

## Decision matrix (frozen, joint with Test T)

- B-v2 fails, T passes → route T.
- B-v2 passes non-trivially, T fails → route B.
- both pass → projectors do not discriminate; return to the limit-operator comparison.
- both fail → no route validated; Q5 stays open.
- projector full for both → checkpoint uninformative; the meaning of "admissible sector" in Q5a
  must be reconsidered.

## Archive contract

PROVENANCE-v2 section (data SHA256 identical to v1, generator commits, parameters), deterministic
script `union_span_tests.py`, raw CSVs (ε, ranks, singular spectra), PDF figure, reproduction
command. Separate report RESULTS-B2.md.
