This repository contains the source of the **Q5a Cosmochrony paper**  
[*Continuum Limit of the Fibre:
Spectral Tightness, Dirichlet Forms, and the Discrete-to-Continuum Transition*](out/q5a.pdf).

This work addresses the **Q5 problem** posed in the Foundation paper:

> How does the discrete fibre structure
> \[
> F_n \simeq V_\rho \subset L^2(\mathbb{Z}/q\mathbb{Z})
> \]
> converge, in the large-$q$ limit, to a continuous structure
> compatible with $L^2(\mathbb{R})$ and effective spacetime geometry?

## Quick Summary

Q5a reduces the continuum limit problem to a **single spectral condition**.

More precisely:

- the discrete structure is recast as a sequence of Dirichlet forms $\mathcal{E}_q$
- the continuum limit is formulated as **Mosco convergence**
- the problem is reduced to a **tightness condition on admissible profiles**

The main result is:

> If admissible profiles satisfy uniform spectral tightness, then the fibre
> admits a well-defined continuum limit in $L^2(\mathbb{R})$.

This condition is not postulated.

It is:

- structurally motivated by the O-series
- strongly supported by numerical evidence

Thus Q5 is reduced from a geometric emergence problem to a **spectral compactness property**.

## Context

**O16–O27** established:

- admissibility constraints (Born–Infeld structure)
- canonical observable $\sigma_{\mathrm{pair}}$
- projection locking (**O22**)
- quaternionic structure (**O23**)
- observable rank stability (**O24**)
- numerical concentration and scaling (**O25**)
- quadratic interpretation (**O26**)
- representation-theoretic rigidity (**O27**)

However:

- all results remain at **finite prime $q$**
- the passage
  \[
  L^2(\mathbb{Z}/q\mathbb{Z}) \to L^2(\mathbb{R})
  \]
  is not yet justified
- the emergence of continuous geometry remains open

This defines Q5.

## Core Result

The paper establishes:

> The continuum limit of the fibre is equivalent to a spectral tightness condition
> on admissible profiles.

More precisely:

- admissible vectors define normalized profiles $f_q$
- the discrete energy $\mathcal{E}_q(f_q,f_q)$ controls oscillations
- tightness ensures precompactness in $L^2$

Under this condition:

- $\mathcal{E}_q$ converges (Mosco sense) to a continuous Dirichlet form
- $f_q$ converges strongly in $L^2(\mathbb{R})$
- the discrete structure admits a continuum limit

## Main Structural Results

### 1. Dirichlet reformulation

*Result.* The discrete fibre is encoded by a sequence of Dirichlet forms:

\[
\mathcal{E}_q(f,f) = \sum_{(x,y)} w_q(x,y)\,(f(x)-f(y))^2.
\]

Thus:

- geometry is replaced by energy
- convergence becomes an operator problem
- the continuum limit is recast analytically

### 2. Reduction to Mosco convergence

*Result.* The continuum limit holds if:

\[
\mathcal{E}_q \xrightarrow{\text{Mosco}} \mathcal{E}.
\]

Thus:

- the problem is reduced to functional analysis
- no geometric assumption is required a priori
- convergence is controlled via compactness

### 3. Spectral tightness condition

*Result.* The continuum limit reduces to:

\[
\forall \varepsilon > 0,\ \exists R:\quad
\sum_{|\xi| > R} |\hat f_q(\xi)|^2 < \varepsilon.
\]

Thus:

- admissible profiles must concentrate in low frequencies
- high-frequency leakage must vanish uniformly in $q$
- tightness becomes the central condition

### 4. Empirical validation

*Result.* Numerical experiments show:

- rapid decay of high-frequency energy
- uniform improvement as $q$ increases
- compatibility with the admissible scaling regime

Thus:

- tightness is strongly supported empirically
- the key hypothesis is not arbitrary

### 5. Tightness implies band-limitation

*Result.* Empirical tightness implies:

\[
R_q = O(1) = o(q),
\]

so admissible profiles are effectively band-limited.

Thus:

- aliasing effects vanish in the large-$q$ limit
- the discrete-to-continuum embedding is justified
- admissibility selects a low-frequency sector

### 6. Validity of the embedding

*Result.* In the band-limited regime:

\[
L^2(\mathbb{Z}/q\mathbb{Z}) \to L^2(\mathbb{R})
\]

is valid after rescaling.

Thus:

- convergence is not assumed but derived
- the continuum limit is intrinsic
- no external regularisation is required

## Foundational Chain from the Substrate

The derivation is fully internal:

Born–Infeld admissibility  
$\to$ spectral profiles  
$\to$ uniform shell structure (O-series)  
$\to$ flat $\sigma_c(n)$ profile  
$\to$ spectral tightness  
$\to$ band-limited regime  
$\to$ Mosco convergence  
$\to$ continuum limit

No continuum assumption is introduced externally.

## Mathematical Role of Q5a

Q5a provides the analytical resolution framework for Q5:

- reformulates the problem in Dirichlet form language
- reduces continuum emergence to a compactness condition
- identifies spectral tightness as the key criterion
- links numerical O-series behaviour to analytical convergence
- justifies the discrete-to-continuum embedding
- provides a falsifiable condition for emergence

## Epistemic Structure of the Paper

### Established input

- admissibility structure (O16–O23)
- observable rank stability (O24)
- numerical scaling and concentration (O25)
- quadratic structure (O26)
- representation rigidity (O27)

### New results

- Dirichlet formulation of the fibre
- reduction to Mosco convergence
- identification of spectral tightness
- empirical validation of tightness
- derivation of band-limited regime
- justification of embedding
- reduction of Q5 to a single condition

### Remaining open problems

- analytical proof of uniform tightness
- identification of the limiting Dirichlet form
- extraction of effective geometry (dimension, metric)
- connection to spacetime structure

## Interpretation of the Result

The conceptual shift is:

- previous view: continuum emerges from increasing resolution
- Q5a: continuum emerges from **spectral compactness**

Thus:

- the limit is not driven by point density
- but by admissibility-induced low-frequency structure
- geometry arises from energy, not coordinates

## Structural Role of Q5a

Q5a initiates the continuum programme:

- **O-series**: finite-$q$ structure
- **Q5a**: analytical reduction of continuum limit
- **Q5b (future)**: extraction of geometry

Thus:

- the existence of the limit is addressed
- its geometric content remains to be derived

## What Q5a Adds

- Dirichlet formulation of fibre structure
- Mosco convergence framework
- spectral tightness criterion
- empirical validation of tightness
- band-limitation from admissibility
- intrinsic justification of embedding
- reduction of Q5 to a single spectral condition

## Outcome

The continuum problem is now:

- analytically well-posed
- reduced to a testable condition
- strongly supported numerically
- structurally connected to admissibility

The remaining task is no longer existence.

It is **analytical proof and geometric extraction**.

## Residual Open Problems

### Analytical tightness proof

Prove uniform spectral tightness from admissibility alone.

### Limiting operator

Identify the limiting Dirichlet form $\mathcal{E}$ explicitly.

### Effective geometry

Derive:

- metric structure
- dimensionality
- possible Lorentzian signature

### Large-$q$ regime

Extend numerical validation to larger primes.

## Status

The programme is now:

- structurally grounded (**O24**)
- numerically validated (**O25**)
- quadratically completed (**O26**)
- representation-theoretically rigid (**O27**)
- analytically reduced (**Q5a**)

The continuum limit is no longer a conjectural emergence.

It is a **well-defined spectral problem**.

## Repository Structure

```text
paper/
├── out/      # Compiled Q5a PDF
├── tex/      # LaTeX sources
└── README.md
```
# Citation

If you reference this work, please cite:

J. Beau: Continuum Limit of the Fibre:
Spectral Tightness, Dirichlet Forms, and the Discrete-to-Continuum Transition
Zenodo, 2026.

# Acknowledgements

Portions of the conceptual synthesis, structural organisation, and editorial refinement
benefited from iterative interactions with large language models used as analytical assistants.

All theoretical results, computations, and interpretations remain the sole responsibility
of the author.

# Contributions

This repository is intended as a research reference.

Critical feedback, independent verification, and further analysis of:

- spectral tightness
- Dirichlet convergence
- continuum limits
- admissibility constraints
- effective geometry

are welcome.

Please open an issue to discuss conceptual points, technical details, or possible
extensions.
