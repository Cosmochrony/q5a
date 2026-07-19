# Canonical Fourier Filtration and the Obstruction to a Spatial Continuum Limit (Q5a)

This repository contains the source of the **Q5a Cosmochrony paper**
*Canonical Fourier Filtration and the Obstruction to a Spatial Continuum Limit —
What the Admissible Fibre Does and Does Not Converge To*.

The paper addresses the **Q5 problem** posed in the Foundation paper — how the discrete
admissible fibre \(F_n \simeq V_\rho \subset L^2(\mathbb{Z}/q\mathbb{Z})\) relates to
continuous structure in the large-\(q\) limit — and answers a sharper preliminary question:
what does the canonical filtration actually converge to, under the published admissibility
form and normalisation?

## Results

- **Exact identification (proved).** With the pipeline's initial vector (the uniform state),
  the canonical filtration stage is exactly the toric Fourier window
  \(\Omega_n = \mathrm{span}\{e^{2\pi i b x/q} : |b| \le n\}\), of dimension
  \(\min(2n+1, q)\). Every fixed toric mode is captured once the published saturation depth
  \(n_1(q)\) exceeds its index; balanced (line-scale) profiles are rejected at all measured
  primes. The stage's physical bandwidth is exactly
  \(\sqrt{2\pi}\,(x_1(q)/C_{\mathrm{Heis}})^{1/4}\), governed by the critical coverage.
- **Zero-form theorem (proved).** With the published prefactor \(q^{-2}\) and bounded weights,
  the admissibility form tends to zero uniformly on norm-bounded sets; its Mosco limit is the
  zero form.
- **Normalisation no-go (proved under the measured weight behaviour).** If the modulation and
  translation weights both remain positive and of order one, no common scalar normalisation
  produces a non-trivial finite toric differential operator: preserving the derivative sector
  makes the modulation sector diverge; preserving the modulation sector eliminates the
  derivative. An anisotropic renormalisation is not derived anywhere in the corpus and would be
  a new input.
- **Dual window limit (conditional).** Under the frequency blow-up \(u = b/n_1(q)\), the
  rescaled form converges to a Dirichlet form on \(L^2([-1,1])\) in the rescaled *frequency*
  variable, with a potential term controlled by the critical coverage. A dual-space statement:
  it does not produce a spatial continuum.

**Q5 therefore remains open.** The downstream identification of a flat spatial co-metric from a
limit operator \(-A\partial_x^2\) on \(L^2(\mathbb{R})\) (companion paper Q5b) rests on an
input that is not established here. A balanced-scale route remains on record as a conditional
possibility, tied to a future non-vanishing asymptotic bound on the critical coverage
\(x_1(q)\) — never as a current result.

## Reproducibility

The numerical statements (balanced-profile rejection at the measured primes) are produced by
the deterministic script `code/canonical_sector_test.py` (published depths only, no
recalibration). Note: the script imports `spectral_O12.py` from the O25 repository
(`admissibility/o25/code/` in the Cosmochrony workspace); reproducing it requires that
repository alongside this one.

## Citation

> J. Beau, *Canonical Fourier Filtration and the Obstruction to a Spatial Continuum Limit*,
> Zenodo, 2026. DOI: [10.5281/zenodo.19642369](https://doi.org/10.5281/zenodo.19642369)

## Links

- 🌐 Programme website: https://cosmochrony.org
- 💻 GitHub organization: https://github.com/Cosmochrony

## Acknowledgements

Portions of the editorial refinement benefited from iterative interactions with large language
models, used as analytical assistants. All claims and final formulations remain the sole
responsibility of the author.
