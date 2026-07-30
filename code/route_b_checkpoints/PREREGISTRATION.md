# [v1 — SINGLE-CENTRAL-CHARACTER PROJECTOR] Pre-registration: pipeline checkpoints [H-w′] and [H-Π3] for Q5a route B

Frozen 2026-07-19, BEFORE any measurement was computed.
No value of any a_q(s) or ε_{q,n} defined below has been evaluated at freezing time; only data-store
structure (npz keys/shapes) and generator code were inspected.
Verdicts will be read against the criteria below without post hoc adjustment.
If either checkpoint fails, route T is adopted (stop criterion), with no re-tuning of conventions.

## Data and provenance (fixed)

- Fingerprint/block data: `admissibility/o14/code/o14_pipeline/q{29,61,101,151,211}_o12.npz`
  (keys used: `q`, `seed`, `blocks`, `n0`, `n1`, `shell_sizes`); SHA256 of each file recorded in
  `PROVENANCE.md` at run time, together with the exact git commits of the o14 (data) and o25
  (generator code) repositories.
- Generator code: `admissibility/o25/code/spectral_O12.py` — functions `build_generators`,
  `bfs_shells`, `fingerprint_vectors_batch`, `gram_schmidt_batch` are used as-is (no modification).
- All five available primes are used: q ∈ {29, 61, 101, 151, 211}. No prime may be dropped from the
  verdict for being unfavourable.

## Frozen definitions

**Grid and scale (balanced).** h = sqrt(2π/q); centered grid x_k = h·(k − (q−1)/2), k = 0..q−1.

**Generators.**
- Translation: (ρ_Y f)(k) = f(k+1 mod q); ρ_{Y⁻¹} its inverse.
- Centered modulation: ρ_{X_c} = diag(e^{2πi(k−(q−1)/2)/q}) = diag(e^{i h x_k}); ρ_{X_c⁻¹} its inverse.
  (Centering is a global phase times ρ_X; representative k ∈ {0..q−1}.)

**Admissibility filter Π_q (frozen).** Orthogonal projector onto the Gram–Schmidt span of the
fingerprint vectors of the FIRST stored block c_block = blocks[0], accumulated over shells
n = 0..n_cut with n_cut = n1(q), the stored fitting-window upper end
({29:5, 61:7, 101:10, 151:12, 211:13}), with the pipeline's default EPS_GS.
Shells are rebuilt by `bfs_shells` with the standard generating set of `build_generators(q)`.

**[H-w′] observable.** For s ∈ {Y, Y⁻¹, X_c, X_c⁻¹}:
a_q(s) := mean over the retained fingerprint vectors v (all shells n ≤ n_cut, the block above) of
‖(ρ_s − I) u‖², with u = Π_q v/‖Π_q v‖ (unit-normalised; vectors with ‖Π_q v‖ < 10⁻¹² are skipped
and counted). ℓ² counting norm. This is the scale-free per-unit-vector response; the raw-norm
variant is part of the robustness grid, not of the primary verdict.

**[H-Π3] observable.** For Hermite indices n = 0..6:
ε_{q,n} := ‖(I − Π_q) g_{q,n}‖ / ‖g_{q,n}‖, with g_{q,n}(k) = ψ_n(x_k) (exact sampling on the
balanced grid; normalisation cancels in the ratio). Separately reported error components:
- window error w_{q,n} = (∫_{|x|>qh/2} |ψ_n|²)^{1/2} / ‖ψ_n‖ (quadrature on a fine grid);
- discretisation error d_{q,n} = ‖ι_q ι_q* ψ_n − ψ_n‖/‖ψ_n‖ computed as the L² band-limitation +
  sampling error of ψ_n at bandwidth 1/(2h) (fine-grid quadrature);
- ε itself is a pure C_q-side projection quantity (no window/discretisation error inside it).

## Frozen pass criteria

**[H-w′] passes iff ALL of:**
1. Boundedness: each of the four sequences (a_q(s))_q stays within [10⁻³, 10³] over all five primes.
2. Pair symmetry: r_q(S) := |a_q(s⁺) − a_q(s⁻)| / (a_q(s⁺) + a_q(s⁻)) < 0.10 at q = 211 for each
   sector S ∈ {Y, X_c}, and r is not increasing between q = 151 and q = 211.
3. Convergence to positive limits WITHOUT extra q-dependent renormalisation:
   for each sector, the log-log OLS slope of a_q vs q over q ≥ 61 satisfies |slope| < 0.15
   (a slope of ±1/2 or ±1 indicates a hidden h-power, i.e., a second prefactor: FAIL), and
   max/min of a_q over q ∈ {101, 151, 211} < 2.
4. Robustness: the qualitative verdict of 1–3 is unchanged across the allowed-choices grid:
   {n_cut = n1(q)} vs {n_cut = min(n1(q)+3, computed range)};
   {first block} vs {mean over min(5, m_block) blocks};
   {single character} vs {conjugate-pair average (c, q−c) when a conjugate block is available};
   {EPS_GS default} vs {EPS_GS/10}.
   Diagnostic ratios a_q(s)/h² are recorded for failure-mode identification but CANNOT rescue a
   verdict.

**[H-Π3] passes iff ALL of:**
1. For each fixed n ≤ 6: ε_{q,n} is decreasing in q over the five primes (allowing one inversion
   below 10% relative), and ε_{211,n} < ε_{29,n}/2.
2. Rate: OLS fit log ε_{q,n} = −β_n log q + c_n reported with residual standard deviation; β_n > 0
   for every n.
3. Error separation: w_{q,n} and d_{q,n} each → 0 in q and are reported alongside ε (no
   conflation).

**Global stop criterion (frozen).** If any a_q(s) → 0 or → ∞ per criterion 3's slope test, or if a
second q-dependent prefactor would be required to stabilise A_q or B_q, or if [H-Π3] criterion 1
fails for some n ≤ 6: route T is adopted. No post hoc adjustment of thresholds, grids, or
conventions is permitted after results are seen.

**Epistemic status (frozen).** A pass does NOT promote [H-w′] or [H-Π3] to theorems; in Q5a 3.0
they remain numerically supported hypotheses unless an analytical proof is supplied.

## Archive contract (fixed)

With the results: `PROVENANCE.md` (data SHA256 + repo commits + parameters), the deterministic
script `route_b_pipeline_tests.py` (no randomness beyond the STORED seeds; single reproduction
command), raw CSV of every measured value, figures in PDF only, and the exact reproduction command
line.
