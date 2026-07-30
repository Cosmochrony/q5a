# RESULTS CANONICAL — filtration stage of the fixed pair sector

Evaluated 2026-07-19 strictly against PREREG-CANONICAL.md (frozen before measurement).
Raw data: results_canonical.csv, sensitivity_canonical.csv, conjugation_control.csv,
spectra_canonical.csv, fig_canonical.pdf.
Reproduction: `PYTHONPATH=<numpy+matplotlib> python3 canonical_sector_test.py`.

## Availability and consistency

- All frozen inputs were available as published: c = 1 (textual), v₀ = uniform (pipeline
  convention), B_n (deterministic BFS), n₁(q) = {4, 8, 11, 13, 14} (CC-Note Table / O28).
- **Analytic prediction confirmed exactly**: dim H_q = 2n₁(q)+1 = {9, 17, 23, 27, 29}, equal to
  the number of distinct b-coordinates in B_{n₁} at every prime.
  The canonical stage is EXACTLY the Fourier-mode window span {e^{2πibx/q} : |b| ≤ n₁(q)} — with
  v₀ uniform, the orbit of the Weil action is a pure-mode family; the filtration is a Fourier
  bandwidth filtration, of physical (balanced-units) bandwidth
  n₁(q)·h = √(2π)·(x₁(q)/C_Heis)^{1/4}.
- Rank fractions dim/q = 0.310, 0.279, 0.228, 0.179, 0.137: non-trivial at q ∈ {151, 211}
  (frozen window [0.05, 0.95]) and decreasing — the dim/q → 1 branch does NOT apply.
- Conjugation control: max |dist(g, Ω^{(1)}) − dist(ḡ, Ω^{(q−1)})| = 2.0×10⁻¹² over all test
  vectors and primes. PASS.

## Verdicts per the frozen criteria

**T family — CONVERGES (all members).**
m = 0..4, t₁: ε ≡ 0 at every prime (trivially convergent — inside the window from n₁ ≥ 4 on).
m = 5, 6: ε = 1 at q = 29 (outside the window, n₁ = 4), then ε ≡ 0 for all q ≥ 61: decreasing,
ε_211 = 0 < ε_29/2. t₂: 0.0342 then 0. Every fixed torus mode is captured permanently once
n₁(q) ≥ m, and n₁(q) → ∞.

**B family — DOES NOT CONVERGE.**
Every Hermite member shows a U-shape with minimum at q = 101 and a rising tail:
ψ₀: 0.0506, 0.0100, 0.0067, 0.0096, 0.0197 (two inversions > 10%);
ψ₂: 0.3722, 0.1158, 0.0849, 0.1117, 0.1905; up to ψ₆: 0.746 → 0.742 (flat at ~0.74).
The frozen decreasing-condition fails for every member (the plateau clause does not apply: the
tail RISES by > 10%).
Depth sensitivity (n₁ ± 1, frozen): same U-shape at both neighbouring depths — the verdict is
not a threshold artefact.

## Decision per the frozen matrix

**"T seul converge → route T."**
T converges alone, with non-trivial rank at the two largest primes. **ROUTE T** is selected by
the canonical interface at the measured primes.

## Structural reading (recorded)

The mechanism is now transparent and exact: the canonical stage's physical bandwidth is
n₁h = √(2π)·(x₁/C_Heis)^{1/4}, numerically {1.86, 2.57, 2.74, 2.65, 2.42} — non-monotone with a
peak at q = 101, falling thereafter because the published critical coverage x₁(q) falls.
Fixed torus modes need only DEPTH (n₁ ≥ m, always eventually true); balanced profiles need
BANDWIDTH bounded below (x₁ bounded away from 0), which the current data contradict.
**Hence the route question and the CC-Note's open problem are the same question:**
x₁(q) → const > 0 would stabilise the bandwidth and could revive the balanced/oscillator
picture; the observed fall (x₁ ~ q^{-0.76}) yields the torus picture.
The verdict is therefore at the measured primes, conditional on the published depth trajectory;
it would be revisited only if the CC-Note's analytical programme establishes a non-vanishing
asymptotic coverage — a corpus-internal question, not a Q5a convention.

## Standing constraints

Per the interface contract: Q5a is to be reformulated as convergence of FILTERED systems on the
pair sector (no final projector), now with target the torus limit; no Q5a 3.0 scaffolding was
started under this run; v1 / B-v2 / T diagnostics remain archived as distinct results.
