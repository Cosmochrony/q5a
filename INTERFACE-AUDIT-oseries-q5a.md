# Interface audit: Foundation / O-series → Q5a — the admissible-sector contract

Working note — not for deposit. 2026-07-19.
Scope: fix the six interface points authorised by the option-(c) decision, from the published
corpus only, WITHOUT modifying Q5a. Sources cited per point. The v1 / B-v2 / T diagnostics are
kept as three distinct results (route_b_checkpoints/); none is re-litigated here.

## 1. The canonical fibre object

**Answer: the single-character Weil representation \(V_{\rho,c}\) with the anti-linear pair
identification \(c \leftrightarrow q-c\) — effectively the pair sector
\(\{V_{\rho,c}, V_{\rho,q-c}\}\) modulo the parity involution. NOT \(\bigoplus_c V_{\rho,c}\).**

- Foundation Thm (A1–A3 + BI parity ⇒ Heisenberg): the fibre is \(F_n \simeq V_\rho\), ONE
  irreducible Weil representation at ONE non-trivial central character, unique by discrete
  Stone–von Neumann (Foundation, proof of thm:heisenberg; companion HeisenbergStructure).
- Foundation Level 2 explicitly constructs \(\rho_c\) on \(\mathbb{C}^q\) as "the natural carrier
  of the irreducible representation of \(G_q\) of central character \(c\)" — per character.
- O17: \(\rho_{q-c} = \overline{\rho_c}\); conjugate blocks carry the same dynamical information;
  the only structurally robust quantity is \(\delta_c = \delta_{q-c}\); the constant \(r(c,q)\) is
  a pipeline artefact.
- O18: the abstract fibre \(\{\chi, -\chi\}\) is realised as the involution
  \(c \leftrightarrow q-c\); conditional minimality: absent extra symmetries, the minimal fibre is
  exactly the parity orbit.

## 2. Superposable characters or distinct sectors?

**Answer: the corpus selects a FIXED central character with its anti-linear partner; it does
not license coherent superposition across sectors.** (Corrected formulation, 2026-07-19: a sum
of character sectors does carry a central action — but a reducible, non-scalar one; the point is
not that the action is undefined, but that the corpus's fibre is a single irreducible sector.)
Foundation's fibre is ONE \(V_\rho\) at one non-trivial central character (Stone–von Neumann);
O16–O18 define the physical observable on ONE conjugate pair \(\{c, q-c\}\), identified
anti-linearly (\(\rho_{q-c} = \overline{\rho_c}\)), never mixed linearly; different pairs are
parallel sectors carrying the same invariant (\(\delta\) universal in \(c\), O17).
**Consequence (explains B-v2/T):** taking the LINEAR span across sectors inside a single copy of
\(\mathbb{C}^q\) conflates inequivalent carriers and destroys the admissibility information — the
union frame is complete and well-conditioned at depth 0, as measured. The orthoprojector on a
cross-sector union is not the right object, exactly as suspected.

## 3. The canonical filtration

**Answer: Foundation Level 3 already defines it.** The orbit span at BFS depth \(n\):
\[
  F_{q,n}^{(c)} \;=\; \Omega_n^{(c)} \;=\; \mathrm{span}\{\rho_c(g)\,v_0 : g \in B_n\}
  \subseteq \mathbb{C}^q ,
\]
an increasing filtration per sector, whose per-shell rank increments are precisely the O12
capacity observable \(\sigma_c(n)\) (new Gram–Schmidt directions per shell).
**Distinction recorded:** the O12/O25 *fingerprint* vectors (triple products over blocks
\((c_1,c_2,c_3)\)) are the measurement pipeline's estimator, not the canonical fibre object; v1
projected onto fingerprint spans, not onto \(\Omega_n^{(c)}\). No test so far has measured the
canonical filtration itself.

## 4. A derived depth \(n(q)\)?

**Answer: yes as an object, with its asymptotic law still open — status to be stated exactly.**
The CC-Note defines the auto-calibrated saturation depth \(n_1(q)\) as a stop of *marginal
novelty* (the creation rate of new directions per explored vertex dropping below the fixed
threshold \(\varepsilon_{\mathrm{sat}}\)) — derived from the exploration itself, independent of
any continuum target. Its exact reduction:
\[
  n_1(q) = \bigl(x_1(q)/C_{\mathrm{Heis}}\bigr)^{1/4}\sqrt{q},
  \qquad x_1(q) = |B_{n_1}|/q^2 ,
\]
with \(|B_n| \sim C_{\mathrm{Heis}} n^4\) (D = 4) and the diffusive gap
\(\lambda_2 \approx 4\pi^2/q^2\); empirically \(x_1\) falls from 0.61 (q = 101) to 0.15
(q = 601), excluding constant coverage; model-free conclusion \(n_1/q \to 0\); the asymptotic law
of \(x_1(q)\) is the CC-Note's open analytical programme.
At \(n_1\) the cumulative rank is FAR FROM FULL (CC-Note, first point) — a fact AT THE MEASURED
PRIMES, not yet an asymptotic result; it is consistent with v1's measured ranks (77/151,
157/211) at those same primes.
**Observation (recorded, not a decision; corrected 2026-07-19):** the identity
\(n_1 = (x_1/C_{\mathrm{Heis}})^{1/4}\sqrt q\) exhibits a \(\sqrt q\) FACTORISATION, not yet a
\(\sqrt q\) LAW: \(n_1 \asymp \sqrt q\) would require \(x_1(q)\) bounded away from zero, whereas
the data show \(x_1\) falling (\(\sim q^{-0.76}\) on the available range, CC-Note), which if
sustained gives a sub-\(\sqrt q\) law (\(\approx q^{0.31}\)). The derived scale is established
only as sub-linear (\(n_1/q \to 0\), model-free).

## 5. Nature of the admissible limit

**Answer: a filtered system per pair sector — not a final subspace, not a projector, not a
quotient.** The admissibility content is the filtration \((\Omega_n^{(c)})_n\) together with its
increment law (capacity); linearising it into one final orthoprojector destroys it (point 2 and
the B-v2/T measurements). Per the frozen decision matrix, this lands in the branch: *"si elle
impose une filtration, reformuler Q5a comme convergence de systèmes filtrés ; ne pas fabriquer un
projecteur final"* — combined with branch 1, since the sector is also fixed (one conjugate pair).

## 6. Where would Mosco convergence actually make sense?

**Answer:** on the varying spaces \(H_q = \Omega_{n(q)}^{(c)}\) — the canonical filtration stage
of ONE conjugate pair sector at the derived depth — with isometries into the continuum target,
in the Kuwae–Shioya varying-spaces frame; the quadratic form is the weighted
\(\rho_c\)-difference form RESTRICTED to the stage (form domain = the stage, no interior
projector). The continuum target (torus vs line/oscillator) is exactly what the canonical-sector
tests must decide; the derived-depth observation of point 4 is the only scale input the corpus
itself supplies, and it is \(\Theta(\sqrt q\,x_1^{1/4})\).

## Decision mapping (per the authorised matrix)

The audit finds BOTH a fixed canonical sector (pair \(\{c, q-c\}\), points 1–2) AND a canonical
filtration with a derived depth object (points 3–4). Applicable branches:
- *"caractère fixe ou paire \(\{c,-c\}\)"* → any future B/T test must be run in the canonical
  pair sector, on the canonical object \(\Omega_n^{(c)}\) (not on fingerprint spans, not on
  cross-sector unions);
- *"filtration"* → Q5a must be reformulated as convergence of filtered systems; no final
  projector is to be fabricated.
The third branch (genuinely summable characters) is EXCLUDED by point 2; the fourth (no canonical
object) does not apply — the objects exist, with the single open item being the asymptotic law of
\(x_1(q)\), which has an established reduction and an explicit analytical programme (CC-Note).

## What this unblocks (subject to authorisation — nothing launched)

A canonical-sector test (new, separate pre-registration if authorised): project balanced and
toric profiles onto \(\Omega_{n}^{(c)}\) for the first conjugate pair, at the pipeline's own
depth trajectory (including \(n_1(q)\)), reporting ranks and rank fractions — the object v1
approximated with the wrong vectors (fingerprints) and B-v2/T destroyed with the wrong union.
Q5a 3.0 remains blocked until that evidence exists; route B vs T remains open, with the point-4
observation on record.
