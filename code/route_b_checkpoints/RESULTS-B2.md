# RESULTS B-v2 — exact paper projector (union span, all central characters)

Evaluated 2026-07-19 strictly against PREREG-B2.md (frozen before measurement).
Raw data: results_B2.csv, singular_spectra.csv, robustness_union_stored.csv, fig_union_span.pdf,
PROVENANCE-V2.md. Reproduction: `PYTHONPATH=<numpy+matplotlib> python3 union_span_tests.py`.

## Measured facts

- **Rank**: rank Π_q = q (rank/q = 1.000) at every prime q ∈ {29, 61, 101, 151, 211}, reached at
  **depth 0** (the identity shell alone): the 64 fingerprint vectors per character, unioned over
  all central characters, already span all of C_q.
  Termination reason "full rank" at every prime; budgets untouched (1 792–13 440 vectors used).
- **Conditioning**: the full singular spectra show NO near-tolerance values —
  σ_min/σ_max = 0.361 (q = 29) down to 0.137 (q = 211), many orders above the frozen tolerance
  q·√ε_mach·σ_max ≈ 10⁻⁶·σ_max. The full-rank verdict is robust, not a numerical artefact.
- **ε_{q,n}**: ≤ 1.3×10⁻¹⁵ (machine zero) for every prime and every Hermite index n = 0..6;
  window and discretisation errors as in v1 (≤ 10⁻¹¹, ≤ 10⁻¹⁵), separation clean.
- **Robustness variant** (union over the STORED blocks instead of canonical blocks): identical —
  full rank at depth 0 at every prime.

## Verdict per the frozen criteria

Criteria 1–3 are formally satisfied (ε identically machine-zero).
**The frozen non-discriminance clause applies: Π_q = I at every prime.**
B-v2 therefore **PASSES FORMALLY but is NON-DISCRIMINANT**: it demonstrates no admissible
selection of balanced profiles, and validates nothing about route B.
Announced as such, per the pre-registration.

## Structural finding (recorded for the reconceptualization step)

The paper's Π_q, operationalised as "projector onto the span of all-character fingerprints", is
NOT a filter: the all-character fingerprint family is a well-conditioned frame of the entire
space already at depth 0.
The admissibility content of the O-series pipeline resides in the *filtration* (per-shell,
per-character rank increments — the σ_c(n) observable), not in a proper subspace of C_q.
The only proper projector among the operationalisations tested so far is the v1
single-central-character span at bounded depth — which failed on balanced profiles
(ε ≈ 0.4–0.75 at q = 151, 211).
