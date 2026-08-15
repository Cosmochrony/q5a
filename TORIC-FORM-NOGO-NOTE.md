# No-go / possibilities note: the energy form on the canonical toric windows

Working note — not for deposit. 2026-07-19.
Scope: the six computations authorised after the canonical-sector test, for the form restricted
to \(H_q = \Omega_{n_1(q)}^{(1)} = \mathrm{span}\{e_b : |b| \le n_1(q)\}\),
\(e_b(k) = e^{2\pi i b k/q}/\sqrt q\). Everything below is exact on \(H_q\); no Q5a file is
modified.

**Acquired result (restated as agreed).** Under the published filtration and at the measured
primes, the admissible spaces are exactly toric Fourier windows and reject balanced profiles;
the compatibility of the energy form with a NON-TRIVIAL toric limit is what this note examines.

## 0. Exact structure on the window

On \(H_q\): \(\rho_Y\) is DIAGONAL, \(\rho_Y e_b = e^{2\pi i b/q} e_b\); \(\rho_X\) is the
frequency SHIFT, \(\rho_X e_b = e_{b+1}\).
Hence for \(f = \sum_{|b|\le n_1} \hat f_b\, e_b\):
\[
\|(\rho_Y - I)f\|^2 = \sum_b 4\sin^2(\pi b/q)\,|\hat f_b|^2, \qquad
\|(\rho_X - I)f\|^2 = \sum_{b=-n_1}^{\,n_1+1} |\hat f_{b-1} - \hat f_b|^2 ,
\]
the second including the exact EDGE (leak) terms \(|\hat f_{n_1}|^2 + |\hat f_{-n_1}|^2\)
(conventions \(\hat f_{\pm(n_1+1)} = 0\)).
In \(x\)-space these are, respectively, the discrete Laplacian symbol and multiplication by
\(|e^{2\pi i x} - 1|^2\) — the asymmetry identified in the instruction, now exact.

## 1. The form with Q5a's actual weights and prefactor

Q5a Definition 2.6: prefactor \(q^{-2}/2\), weights \(a_q(s) \to \approx 2\) ([H-w′], both
sectors O(1)). For a FIXED smooth toric profile (fixed \(\hat f_m\), finitely many \(m\)):
Y-part \(= O(q^{-2})\) before the prefactor, X-part \(= O(1)\); total
\(\mathcal E_q(f) = O(q^{-2}) \to 0\).
**Exact answer: the zero form, at rate \(q^{-2}\), X-dominated. Restriction to \(H_q\) changes
nothing here.**

## 2. The compression \(P_{H}\rho_X P_{H}\) and the edges

The compressed shift is the truncated shift on \([-n_1, n_1]\).
Ambient vs compressed quadratic forms differ EXACTLY by the leak terms
\(|\hat f_{n_1}|^2 + |\hat f_{-n_1}|^2\).
CORRECTED 2026-07-19 after component-by-component recomputation: the ambient-form
restriction gives edge terms |f_{+-n1}|^2 (Dirichlet under blow-up); the operator compression
P(2I - X - X*)P yields THE SAME quadratic form (diagonal stays 2 at the edges) — Dirichlet as
well, NOT Neumann; Neumann arises only from explicit deletion of the outgoing edges (the graph
Laplacian of the induced path, degree 1 at the endpoints), which modifies the operator rather
than the domain and is not canonical. Compression does NOT automatically give Neumann; the
earlier statement of this note to the contrary was wrong. The paper must adopt ONE definition
(the ambient restriction, matching its own conventions) and derive Dirichlet explicitly.

## 3. The three common-prefactor regimes (fixed toric profiles) — the no-go

With common prefactor \(\alpha_q\) and weights \(A_Y, A_X > 0\) (measured O(1)):
- \(\alpha_q = 1\): limit \(= A_X \cdot\) multiplication by \(2(1 - \cos 2\pi x)\); the
  derivative (Y) sector vanishes. A bounded multiplication operator: closable form, NO kinetic
  term, no diffusion, no second-order operator.
- \(\alpha_q \sim q^2\): Y-sector \(\to A_Y (2\pi)^2\!\int_{\mathbb T}|f'|^2\)-type, but the
  X-sector diverges on every fixed profile with non-constant \(\hat f\): the Γ-limit is
  \(+\infty\) off the constants — a degenerate form.
- \(\alpha_q \sim q^{-2}\): the zero form (point 1).
**No common prefactor produces a toric limit containing both a finite kinetic term and the X
sector on fixed toric profiles. The no-go of the instruction is confirmed exactly.**

## 4. Is an anisotropic renormalisation \(q^2 a_q(Y)\) vs \(a_q(X)\) derived anywhere?

No. The corpus defines ONE weight family \(a_q(s)\) (Q5a Def. 2.5 from fingerprint responses —
measured O(1) for all four generators, [H-w′]) and ONE prefactor (Q5a Def. 2.6).
No paper derives per-generator prefactors; the O-series treats the generating set
symmetrically (BFS word metric); Foundation's Level 3 is scale-free.
**An anisotropic renormalisation would be a NEW INPUT, not a derived one.**
(For the record: it is also what the balanced route provided automatically, which was its
virtue — both sectors at the same scale \(h^{-2}\).)

## 5. The actual limit operator, regime by regime

| Regime | Limit on fixed toric profiles | Nature |
|---|---|---|
| \(\alpha_q = 1\) (derived: Q5a's own O(1) weights, no rescale) | \(2A_X(1-\cos 2\pi x)\) | bounded multiplication; no dynamics |
| \(\alpha_q = q^2\) | degenerate (\(+\infty\) off constants) | divergence |
| \(\alpha_q = q^{-2}\) (Q5a Def. 2.6) | 0 | zero form |

**Window-intrinsic regime (new, exact).** The filtration's own natural test profiles are
window-spread envelopes \(\hat f_b = n_1^{-1/2}\varphi(b/n_1)\), \(\varphi\) smooth on
\([-1,1]\). Then, exactly:
\[
\|(\rho_X - I)f\|^2 = n_1^{-2}\!\int_{-1}^{1}\!|\varphi'(u)|^2\,du\,(1+o(1)) + \text{edge terms},
\qquad
\|(\rho_Y - I)f\|^2 = \Bigl(\tfrac{2\pi n_1}{q}\Bigr)^{2}\!\int_{-1}^{1}\!u^2|\varphi(u)|^2\,du\,(1+o(1)),
\]
so with the (single, common) prefactor \(\alpha_q = n_1^2\):
\[
\mathcal E_q \;\longrightarrow\;
A_X\!\int_{-1}^{1}|\varphi'(u)|^2\,du \;+\; A_Y\,(2\pi)^2\,\frac{x_1(q)}{C_{\mathrm{Heis}}}\!\int_{-1}^{1} u^2|\varphi(u)|^2\,du ,
\]
using the exact identity \((n_1^2/q)^2 = x_1/C_{\mathrm{Heis}}\).
The limit lives on \(L^2([-1,1], du)\) — the RESCALED FREQUENCY WINDOW, not the torus:
- under the empirical coverage law (\(x_1 \to 0\)): a pure Laplacian \(-A_X\,\partial_u^2\) on
  \([-1,1]\), Dirichlet or Neumann per point 2;
- if \(x_1(q)\) were bounded away from zero: a SCHRÖDINGER (oscillator-type) operator
  \(-A_X\partial_u^2 + A_Y(2\pi)^2 (x_1/C_{\mathrm{Heis}})\,u^2\) — the balanced/oscillator
  picture resurfacing in the dual variable, under exactly the B-revival condition already
  identified (x₁ bounded below).
This regime uses one common prefactor and the derived weights — but its limit space is the
frequency window, not \(\mathbb T\): it is a possibility, not the toric limit Q5a announced.

## 6. Consequences for the co-metric consumed by Q5b

Q5b reads the co-metric from the principal symbol of \(L_\Pi = -A\partial_x^2\) on
\(L^2(\mathbb R)\). Under the results above:
- no derived common-prefactor regime produces ANY second-order operator in the spatial
  variable: the derived candidates are a multiplication operator (no symbol of order 2, no
  co-metric) or the zero form;
- the only non-trivial derived limit is second-order in the RESCALED FREQUENCY variable \(u\) on
  \([-1,1]\); a co-metric read from it lives on the frequency window, which would require a
  substantive reinterpretation of Q5b's spatial reading (not a verbatim survival);
- the oscillator variant (x₁ bounded below) would restore a principal symbol \(A_X\xi_u^2\), but
  again in the dual variable.
**As it stands, the object Q5b consumes is not produced by any derived toric regime.**

## Explicit calibrations (kept visible)

1. Permanent capture of every fixed mode requires \(n_1(q) \to \infty\): empirically monotone
   (4 → 19 over q = 29 → 601) but asymptotically HYPOTHETICAL — no proof.
2. \(x_1(q) \sim q^{-0.76}\) is a numerical fit on the available range, NOT a demonstrated law
   (CC-Note's open programme).

## Conclusion

The no-go is exact: no single derived prefactor yields a toric limit with both a finite kinetic
term and the X sector; the anisotropic fix is not corpus-derived.
The possibilities that remain, ranked by how much they preserve:
(i) the window-intrinsic limit \(-A_X\partial_u^2\;(+\,(2\pi)^2 A_Y x_1/C_{\mathrm{Heis}}\,u^2)\)
on \(L^2([-1,1])\) — derived weights, common prefactor \(n_1^2\), exact constants, boundary
condition fixed by the ambient/compressed choice; a genuine continuum limit, but on the
frequency window, with Q5b requiring reinterpretation;
(ii) the multiplication limit (\(\alpha_q = 1\)) — derived but dynamically trivial;
(iii) declaring the toric energy question open (Q5a 3.0 as a negative/structural result: windows
approximate toric functions, but the published form does not converge to a non-trivial toric
operator under any derived normalisation).
If none of (i)–(iii) is judged acceptable as Q5a 3.0's content, Q5 remains open at this
interface — per the instruction, that outcome is to be stated rather than repaired by a new
adjustable input.
