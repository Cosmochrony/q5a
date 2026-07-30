# RESULTS T — toric approximation test (same union-span projector)

Evaluated 2026-07-19 strictly against PREREG-T.md (frozen before measurement).
Raw data: results_T.csv (with ranks), singular_spectra.csv, fig_union_span.pdf, PROVENANCE-V2.md.
Same run as B-v2 (shared script `union_span_tests.py`); separate report per the instruction.

## Measured facts

- ε^T_{q,m} ≤ 1.6×10⁻¹⁵ (machine zero) for every prime and every frozen test vector:
  Fourier modes m = 0..6 and both trigonometric combinations t₁, t₂.
- Sampling error identically 0 by construction (all |m| < q/2); no window error on the torus;
  ε is pure projection deficiency — and it is machine-zero because rank Π_q = q everywhere
  (see RESULTS-B2.md: full rank at depth 0, well-conditioned spectra).

## Verdict per the frozen criteria

Criteria formally satisfied, but **the frozen non-discriminance clause applies identically:
Π_q = I at every prime**.
Test T **PASSES FORMALLY but is NON-DISCRIMINANT**.

## Joint outcome under the frozen decision matrix

The applicable branch is the fifth:
**"projecteur plein pour les deux : checkpoint non informatif ; il faudra revoir ce que
« secteur admissible » signifie dans Q5a."**
Neither route is validated or invalidated by the projector checkpoints.
The route decision cannot be made through Π-approximation tests with this operationalisation;
what "admissible sector" means in Q5a must be reconsidered first (the pipeline's admissibility is
a filtration — per-shell rank increments — not a proper subspace once characters are unioned;
see the structural finding in RESULTS-B2.md).
The v1 result stands, relabelled, as the useful negative: the single-central-character projector
at bounded depth is proper but does not approximate balanced profiles.
