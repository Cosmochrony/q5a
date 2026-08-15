# Q5a route analysis: balanced scaling (B) versus torus scaling (T)

Working note — not for deposit. 2026-07-19.

**Purpose.**
The adversarial review of Q5a (branch 2.1) established that the \(1/q\)-spaced sinc identification cannot
support the stated \(L^2(\mathbb R)\) limits: the form's prefactor produces the zero form, the modulation
generator diverges, and the uniform-gap hypothesis contradicts the free-Laplacian conclusion.
This note evaluates the two coherent repair routes and provides a prototype proof for route B, against the
seven adoption criteria and the stop criterion fixed for this decision.
Route B is adopted only if the criteria pass; otherwise route T is the mathematically natural fallback for
the \(k/q\) scale.

## 1. The two routes

Both routes keep the finite model: \(C_q = L^2(\mathbb Z/q\mathbb Z)\) (counting norm
\(\|f\|^2 = \sum_k |f(k)|^2\) unless stated), Weil generators
\((\rho_X f)(k) = e^{2\pi i k/q} f(k)\), \((\rho_Y f)(k) = f(k{+}1 \bmod q)\), admissibility filter
\(\Pi_q\), weighted form built from \(\|(\rho_s - I)f\|^2\).

**Route T (torus).**
Keep the sample scale \(x = k/q \in [0,1)\).
Then \(\rho_X\) converges *without rescaling* to multiplication by \(e^{2\pi i x}\) on \(L^2(\mathbb T)\),
\(q(\rho_Y - I)/(2\pi i) \to -(i/2\pi)\partial_x\), and the \(q^{+2}\)-rescaled translation form converges
to \(A \int_{\mathbb T} |f'|^2\).
This is the \(\theta \to 0\) limit of the noncommutative torus (Rieffel's continuous fields); the Poincaré
inequality, Rellich compactness, and the equivalence "tightness ⟺ frequency control" all hold on
\(\mathbb T\).
Lost: the metaplectic target, \(L^2(\mathbb R)\), and the free-line operator consumed by Q5b.

**Route B (balanced).**
Sample scale \(h = \sqrt{2\pi/q}\), centered window of length \(qh = \sqrt{2\pi q} \to \infty\).
Both generators converge after the *same* \(1/(ih)\) rescaling; the limit operator is the harmonic
oscillator \(-A\partial_x^2 + Bx^2\) on \(L^2(\mathbb R)\), with compact resolvent and spectral gap.
This is the Hannay–Berry/finite-oscillator regime (Atakishiyev–Wolf; discrete-Fourier eigenvectors →
Hermite functions; Harper Hamiltonian at flux \(2\pi/q\) near its band edge).

## 2. Route B: prototype proof

### 2.1 Criterion 1: explicit isometric embeddings, spacing \(q^{-1/2}\), window \(\sqrt q\)

Fix \(h := \sqrt{2\pi/q}\) and the centered grid \(x_k := h\,(k - \tfrac{q-1}{2})\), \(k = 0,\dots,q-1\),
so that \(x_k\) ranges over a window of length \(qh = \sqrt{2\pi q}\) with spacing \(h\); the frequency side
has window \(1/h = \sqrt{q/2\pi}\) and spacing \(1/(qh)\) — both sides open to \(\mathbb R\) symmetrically.

**Definition (balanced sinc embedding).**
Let \(e_k(x) := h^{-1/2}\operatorname{sinc}\bigl((x - x_k)/h\bigr)\).
The family \((e_k)_{k=0}^{q-1}\) is orthonormal in \(L^2(\mathbb R)\), and
\(\iota_q f := \sum_k f(k)\, e_k\) defines an isometry \(C_q \to L^2(\mathbb R)\) onto a \(q\)-dimensional
subspace of the Paley–Wiener space \(\mathcal H_{1/2h}\).
Its adjoint on band-limited \(F\) is exact sampling, \((\iota_q^* F)(k) = h^{1/2} F(x_k)\), and
\(\|\iota_q^* F\|^2 = h \sum_k |F(x_k)|^2 \to \int_{\mathbb R} |F|^2\) (Riemann sum, spacing \(h \to 0\),
window \(\to \mathbb R\)); in particular \(\iota_q^* \iota_q = I\) and \(\|\iota_q^*\| = 1\), repairing the
adjoint defect of branch 2.1.

**Remark (Kuwae–Shioya frame instead of an inductive limit).**
The node sets \(h\mathbb Z\) are not nested across primes, so no directed system is claimed.
None is needed: Mosco convergence on varying Hilbert spaces (Kuwae–Shioya) requires only the isometries
\(\iota_q : C_q \to L^2(\mathbb R)\) together with asymptotic density,
\(\|\iota_q \iota_q^* \psi - \psi\|_{L^2(\mathbb R)} \to 0\) for \(\psi\) in a dense class, which holds for
\(\psi \in \mathscr S(\mathbb R)\) by the sampling theorem on growing windows (the window tail contributes
superpolynomially little for Schwartz \(\psi\)).
This removes the entire H1/Weil-block-embedding apparatus of branch 2.1 from the critical path: the
identification of the limit space is analytic, and the representation-theoretic content moves to
Criterion 2.

### 2.2 Criterion 2: both generators, exact constants

Centering is representation-theoretically innocent: conjugating \(\rho_X\) by \(\rho_Y^{(q-1)/2}\) replaces
its phase by the centered character, \((\rho_{X_c} f)(k) = e^{i h x_k} f(k)\), using
\(2\pi/(qh) = h\) — the identity that singles out \(h = \sqrt{2\pi/q}\).

**Definition (balanced rescaled generators).**
\(Q_q := \dfrac{\rho_{X_c} - I}{ih}\), \(\qquad P_q := \dfrac{\rho_Y - I}{ih}\).

**Proposition 1 (generator convergence on the Schwartz core).**
For every \(\psi \in \mathscr S(\mathbb R)\), with \(f = \iota_q^* \psi\):

$$
  \bigl\| \iota_q Q_q f - x\psi \bigr\|_{L^2(\mathbb R)} = O(q^{-1/2}), \qquad
  \bigl\| \iota_q P_q f - (-i\partial_x\psi) \bigr\|_{L^2(\mathbb R)} = O(q^{-1/2}),
$$

with no residual constant: the targets are exactly \(Q = x\) and \(P = -i\partial_x\).

*Proof sketch.*
Modulation: \((Q_q f)(k) = \frac{e^{ihx_k}-1}{ih} f(k)\) and
\(\bigl|\frac{e^{ihx}-1}{ih} - x\bigr| \le \tfrac{h}{2} x^2\), so the error is bounded by
\(\tfrac h2\|x^2\psi\|\) plus window tails (superpolynomially small).
Translation: \((P_q f)(k) = \frac{\psi(x_k + h) - \psi(x_k)}{ih} = -i\psi'(x_k) + O(h\|\psi''\|_\infty)\)
at interior nodes; the single cyclic seam term is
\(h^{-1}|\psi(x_{\max}{+}h) - \psi(x_{\min})|\), superpolynomially small: the wraparound obstruction of the
\(1/q\) scale disappears because the window endpoints \(\pm\sqrt{2\pi q}/2\) escape to \(\pm\infty\) where
Schwartz functions vanish.
The factor \(2\pi\) is absorbed exactly because \(h\) appears both in the phase (\(e^{ihx}\)) and in the
step (shift by \(h\)); no mismatch remains.
Commutator check with the paper's own convention \(\rho_Y \rho_X = e^{2\pi i/q} \rho_X \rho_Y\):
\([Q_q, P_q] = -h^{-2}(e^{-ih^2}-1)\,\rho_Y\rho_{X_c} \to +i\,I\) strongly, matching
\([x, -i\partial_x] = i\). ∎

### 2.3 Criterion 3: the exact form limit and the coefficients \(A, B\)

**Definition (balanced admissibility form).**
On the form domain \(\operatorname{ran}(\Pi_q)\),

$$
  \mathcal E_q(f) := \frac{h^{-2}}{2} \sum_{s \in \{X_c^{\pm1}, Y^{\pm1}\}} a_q(s)\,
  \bigl\| (\rho_s - I) f \bigr\|^2 .
$$

Restricting the domain to \(\operatorname{ran}(\Pi_q)\) (rather than inserting \(\Pi_q\) inside the norm on
all of \(C_q\)) removes the zero-energy kernel directions that generated the review's inconsistency
argument.

**Proposition 2 (limsup limit on the Schwartz core).**
Assume the balanced weight hypothesis **[H-w′]**: \(a_q(Y^{\pm1}) \to A_Y > 0\) and
\(a_q(X_c^{\pm1}) \to A_X > 0\), the weights being re-measured in the balanced normalisation.
Then for \(\psi \in \mathscr S(\mathbb R)\), with recovery family \(f_q = \Pi_q \iota_q^* \psi\) and the
filter approximation hypothesis **[H-Π3]** below,

$$
  \mathcal E_q(f_q) \;\longrightarrow\;
  A \int_{\mathbb R} |\psi'|^2\,dx \;+\; B \int_{\mathbb R} x^2 |\psi|^2\,dx,
  \qquad A = A_Y,\; B = A_X .
$$

*Proof sketch.*
\(\|(\rho_Y - I) \iota_q^*\psi\|^2 = h^2\|\psi'\|^2(1 + O(h))\) (interior Taylor + negligible seam) and
\(\|(\rho_{X_c} - I)\iota_q^*\psi\|^2 = h^2 \|x\psi\|^2 (1 + O(h))\) from
\(|e^{ihx}-1|^2 = h^2x^2(1+O(h^2x^2))\); each inverse generator contributes identically; the common
prefactor \(h^{-2}/2\) then yields \(A_Y\|\psi'\|^2 + A_X\|x\psi\|^2\).
The two coefficients arise from one normalisation (\(h^{-2}\)) applied to one weight family: the stop
criterion's "common coherent normalisation" requirement is satisfied structurally.
Status of \(A, B > 0\): conditional on [H-w′] — an empirical checkpoint, not a theorem; the branch-2.1
weight values were computed in the \(1/q\) reading and cannot be reused (see §5). ∎

**Hypothesis [H-Π3] (filter approximation).**
\(\| \Pi_q \iota_q^* \psi - \iota_q^* \psi \| \to 0\) for every \(\psi \in \mathscr S(\mathbb R)\).

This makes the previously implicit use of shell locality explicit and numerically testable on the O-series
pipeline; it replaces the vague appeal to [H-Π2] in the limsup step.

### 2.4 Criterion 4: Mosco liminf and limsup

**(M2)** is Proposition 2 plus strong convergence \(\iota_q f_q \to \psi\) (sampling + [H-Π3]), extended
from \(\mathscr S(\mathbb R)\) to the form domain \(\{f \in H^1(\mathbb R) : xf \in L^2\}\) by density and
diagonal extraction; cyclic seam terms are superpolynomially small as in Proposition 1.

**(M1)** follows from the compactness of §2.5 together with lower semicontinuity of both integrands
(\(|\psi'|^2\) via weak \(L^2\) convergence of embedded discrete gradients, \(x^2|\psi|^2\) via Fatou on the
moment bound); no step assumes the conclusion.

### 2.5 Criterion 5: gap, resolvent compactness, and tightness without circularity

The route-B geometry supplies two *global, uniform* elementary bounds.
At the window edge \(|x| = qh/2\) one has \(h|x|/2 = qh^2/4 = \pi/2\) exactly; hence over the whole grid
\(h x_k/2 \in [-\pi/2, \pi/2]\) and \(\sin\theta \ge 2\theta/\pi\) gives

$$
  h^{-2}\,\bigl|e^{ihx_k} - 1\bigr|^2 = h^{-2}\,4\sin^2(hx_k/2) \;\ge\; \frac{4}{\pi^2}\, x_k^2
  \qquad\text{for every grid point, uniformly in } q .
$$

Dually, on the frequency window the translation term satisfies
\(h^{-2}\,4\sin^2(\pi\xi/q) \ge \frac{4}{\pi^2}\,\xi_{\mathrm{phys}}^2\) with \(\xi_{\mathrm{phys}}\) the
balanced frequency.
Therefore, for \(f \in \operatorname{ran}(\Pi_q)\) with \(\mathcal E_q(f) \le E\) and \(\|f\| \le 1\)
(given the [H-w′] lower bounds \(a_q(s) \ge a_- > 0\)):

$$
  \sum_k x_k^2 |f(k)|^2 \;\le\; \frac{\pi^2 E}{4 a_-}, \qquad
  \sum_\xi \xi_{\mathrm{phys}}^2 |\hat f(\xi)|^2 \;\le\; \frac{\pi^2 E}{4 a_-} .
$$

Uniform second moments in *both* position and frequency give, via Riesz–Kolmogorov, relative compactness of
\((\iota_q f)\) in \(L^2(\mathbb R)\): the former Conjecture C becomes a **lemma** conditional only on the
weight lower bound, with no tightness assumed.
The former uniform-gap hypothesis becomes a **theorem**: from the commutator of Proposition 1, the discrete
uncertainty inequality
\(\langle f, (Q_q^*Q_q + P_q^*P_q) f\rangle \ge |\langle f, [Q_q, iP_q] f\rangle| = (1 - o(1))\|f\|^2\)
yields \(\lambda_{\min}(L_q) \ge c > 0\) uniformly — consistent with the numerics below, where the gap is
≈ 2 at every tested \(q\).
The limit operator \(L_\Pi^{B} = -A\partial_x^2 + Bx^2\) has compact resolvent and spectrum
\(\sqrt{AB}\,(2n+1)\), \(n \ge 0\); gap \(2\sqrt{AB}\).

### 2.6 Criterion 6: reproducible numerics at genuine width \(O(\sqrt q)\)

Deterministic script `route_b_prototype.py` (this repository, numpy only, no pipeline data, no randomness):
Hermite profiles \(\psi_0, \psi_2\) of width \(O(1)\) in \(x\), i.e. genuinely \(O(\sqrt q)\) lattice
sites; unit weights; four generators; exact drivers as in this note.

| \(q\) | \(\|Q_q{-}x\|_\psi\) | \(\|P_q{+}i\partial\|_\psi\) | \(\mathcal E_q(\psi_0)\) | \(|\cdot-1|\) | \(\mathcal E_q(\psi_2)\) | \(|\cdot-5|\) |
|---|---|---|---|---|---|---|
| 29 | 1.99e-1 | 1.99e-1 | 0.97340 | 2.7e-2 | 4.65988 | 3.4e-1 |
| 61 | 1.38e-1 | 1.38e-1 | 0.98723 | 1.3e-2 | 4.83535 | 1.6e-1 |
| 101 | 1.08e-1 | 1.08e-1 | 0.99226 | 7.7e-3 | 4.89991 | 1.0e-1 |
| 151 | 8.81e-2 | 8.81e-2 | 0.99482 | 5.2e-3 | 4.93283 | 6.7e-2 |
| 211 | 7.46e-2 | 7.46e-2 | 0.99629 | 3.7e-3 | 4.95184 | 4.8e-2 |
| 401 | 5.41e-2 | 5.41e-2 | 0.99804 | 2.0e-3 | 4.97460 | 2.5e-2 |

Measured rates: generator errors \(\propto q^{-1/2} = h\) (ratio 0.272 against predicted 0.269 across
\(q = 29 \to 401\)); energy errors \(\propto q^{-1}\); cyclic seam contribution 0 at machine precision at
all \(q\).
Lowest six eigenvalues of \(L_q\) (unit weights): at \(q = 211\),
\((0.9963,\, 2.9814,\, 4.9518,\, 6.9074,\, 8.8483,\, 10.7745) \to (1,3,5,7,9,11)\), the oscillator ladder,
with a uniform gap ≈ 2 visible at every \(q\) down to 29.
The prototype therefore verifies Criteria 2, 3, 5 quantitatively in the unfiltered case \(\Pi_q = I\).

### 2.7 Criterion 7: exact comparison with route T

| | Route B (balanced, \(h=\sqrt{2\pi/q}\)) | Route T (torus, \(x = k/q\)) |
|---|---|---|
| Limit space | \(L^2(\mathbb R)\) | \(L^2(\mathbb T)\) |
| Modulation generator | \((\rho_{X_c}{-}I)/(ih) \to x\) | \(\rho_X \to\) mult. by \(e^{2\pi i x}\) (no rescaling) |
| Translation generator | \((\rho_Y{-}I)/(ih) \to -i\partial_x\) | \(q(\rho_Y{-}I)/(2\pi i) \to -(i/2\pi)\partial_x\) |
| Limit operator | \(-A\partial_x^2 + Bx^2\) (oscillator) | \(-A\partial_x^2\) on \(\mathbb T\) (+ optional mult. term) |
| Spectrum | discrete, \(\sqrt{AB}(2n{+}1)\), gap | discrete on \(\mathbb T\), gap \((2\pi)^2A\) |
| Uniform gap status | theorem (uncertainty ineq.) | theorem (torus Poincaré) |
| Tightness | lemma (both second moments) | lemma (Rellich on \(\mathbb T\)) |
| Metaplectic content | yes (Hermite/oscillator limit) | no (NC-torus \(\theta\to0\); Rieffel) |
| Cyclic seam | superpolynomially small | exact (periodicity is native) |
| Literature anchors | Hannay–Berry; Atakishiyev–Wolf; Harper | Rieffel continuous fields |
| Q5b compatibility | principal symbol \(A\xi^2\) preserved | operator changes domain to \(\mathbb T\) |

Route T remains fully coherent and strictly simpler; it is the correct fallback if the balanced weight
checkpoint fails.

## 3. Impact matrix

**Q5b (published 1.3).**
Q5b consumes \(L_\Pi = -A\partial_x^2\) on \(L^2(\mathbb R)\) and reads the co-metric from the operator.
Under route B the *principal* symbol remains \(A\xi^2\) (the potential \(Bx^2\) is of lower order in
\(\xi\)), so every Q5b step that uses only the principal symbol survives verbatim; the
Schrödinger-representation reading arguably becomes more canonical, since \(A P^2 + B Q^2\) is a
distinguished element of the Heisenberg enveloping algebra.
To audit at Q5b's next pass: any step using the *continuous* spectrum \([0,\infty)\) of the free line
operator, spectral measures, or heat-kernel normalisations of \(-A\partial_x^2\) — these would need the
oscillator replacements (discrete spectrum, Mehler kernel).

**Q11 / temporal papers (PTO, LC series).**
They consume the co-metric closure, not the operator's global spectrum; low direct exposure.
The oscillator's discrete spectrum and ground state may *refine* the temporal-ordering picture
(a canonical lowest admissible mode); to note at their next revision, no retraction implied.

**Foundation / program / site.**
Until Q5a 3.0 exists, every surface must present Q5 as *open, reduced to explicit hypotheses*, not
resolved: the Q5a row of the programme registry, the Foundation cross-reference, and the q5a web page must
avoid "resolution of Q5"; the relabelled Zenodo record 2.0 is unaffected (metadata only).

**Simulations.**
Invalid under the change of scale: the branch-2.1 conjecture-C tail test (independently invalidated by its
test-vector width bug), any tail-mass criterion at cutoffs proportional to \(q\), and `extract_A.py`
(weight extraction assumes the \(1/q\) normalisation — must be re-derived to measure [H-w′]).
Scale-free and reusable: mode-support counts (`admissible_fourier_profile.py`), fingerprint-energy profiles
per shell.
New required runs: (i) balanced re-measurement of \(a_q(s)\) ([H-w′]); (ii) [H-Π3] test
\(\|\Pi_q \iota_q^*\psi - \iota_q^*\psi\|\) on Hermite profiles; (iii) the prototype extended with the
pipeline's \(\Pi_q\).

## 4. Stop-criterion assessment and recommendation

**(a) Common coherent normalisation for \(A\) and \(B\): passes structurally.**
Both coefficients arise from the single prefactor \(h^{-2}\) applied to the single weight family
\(a_q(s)\); the numerics confirm the two energies converge simultaneously with the same normalisation
(\(\mathcal E_q(\psi_0) \to 1\), \(\mathcal E_q(\psi_2) \to 5\)).
The residual risk is empirical, isolated in [H-w′]: the balanced-scaled weights must stabilise at positive
values on the actual pipeline data.

**(b) Mosco without assuming the conclusion: passes.**
Tightness follows from the two uniform second-moment bounds of §2.5 (a consequence of the confining
modulation terms plus gradient terms), and the gap from the discrete uncertainty inequality; neither step
invokes the limit form.
The only hypotheses left with hypothesis status are [H-w′] (weights) and [H-Π3] (filter approximation) —
both numerically testable, neither circular.

**Recommendation.**
Route B passes the structural criteria and the prototype validates it quantitatively in the unfiltered
case; adopt it as the working hypothesis, with final adoption gated on the two pipeline checkpoints
([H-w′], [H-Π3]).
If the balanced weight measurement fails (vanishing or divergent \(a_q\)), fall back to route T without
attempting to force \(L^2(\mathbb R)\).
Upon adoption, the rewrite is Q5a 3.0: Kuwae–Shioya frame replacing the inductive limit (H1 machinery
retired from the critical path), Proposition 1 as T2 with exact constants, Proposition 2 as T3's limsup,
§2.5 as the tightness lemma and gap theorem, oscillator limit operator, and the impact-matrix corrections
cascaded (Q5b principal-symbol audit, programme/site wording, simulation reruns).
Branch 2.1 remains an unpublished corrective trace.

## 5. Pipeline checkpoints gating final adoption

1. **[H-w′]** — re-measure \(a_q(s)\) in the balanced normalisation from the O-series fingerprint data
   (re-derive `extract_A.py`); adoption requires stabilisation at positive finite values for both
   generator families.
2. **[H-Π3]** — measure \(\|\Pi_q \iota_q^*\psi - \iota_q^*\psi\|\) for Hermite profiles on the stored
   \(\Pi_q\) matrices; adoption requires decay in \(q\).
