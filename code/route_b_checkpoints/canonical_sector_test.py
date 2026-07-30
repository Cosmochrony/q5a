"""
Pre-registered CANONICAL sector test (PREREG-CANONICAL.md): filtration stage
H_q = Omega_{n1(q)}^{(1)} = span{rho_1(g) v0 : g in B_{n1(q)}}, v0 = uniform, c = 1,
published depths n1 = {29:4, 61:8, 101:11, 151:13, 211:14} (CC-Note/O28), no recalibration.

Deterministic. Reproduction:
    PYTHONPATH=<numpy+matplotlib> python3 canonical_sector_test.py
Outputs: results_canonical.csv, sensitivity_canonical.csv, conjugation_control.csv,
spectra_canonical.csv, fig_canonical.pdf.
"""

import csv
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
GEN_DIR = os.path.join(ROOT, "admissibility", "o25", "code")
sys.path.insert(0, GEN_DIR)

import spectral_O12 as o12  # noqa: E402  (heisenberg_mul, build_generators)

PRIMES = [29, 61, 101, 151, 211]
N1 = {29: 4, 61: 8, 101: 11, 151: 13, 211: 14}  # published (CC-Note Table / O28)
EPS_MACH = 2.0 ** -52


def bfs_ball(q, depth):
    gens = o12.build_generators(q)
    identity = (0, 0, 0)
    visited = {identity}
    current = [identity]
    balls = [list(visited)]
    for _ in range(depth):
        nxt = []
        for u in current:
            for g in gens:
                v = o12.heisenberg_mul(u, tuple(g), q)
                if v not in visited:
                    visited.add(v)
                    nxt.append(v)
        current = nxt
        balls.append(sorted(visited))
    return balls  # balls[d] = sorted list of elements of B_d


def orbit_basis(q, ball, c):
    """Orthonormal basis of span{rho_c(g) v0 : g in ball}, v0 uniform, via Gram method."""
    x = np.arange(q)
    G = np.zeros((q, q), dtype=np.complex128)
    V = []
    for (a, b, gam) in ball:
        vec = np.exp(2j * np.pi * c * (gam + b * x) / q) / np.sqrt(q)  # (rho_c(a,b,g)v0)(x)
        V.append(vec)
    V = np.array(V)
    G = V.conj().T @ V
    lam, U = np.linalg.eigh(G)
    sig = np.sqrt(np.clip(lam, 0, None))
    tau = q * np.sqrt(EPS_MACH) * sig.max()
    keep = sig > tau
    return U[:, keep], sig[::-1], int(keep.sum()), len(set(b for (_, b, _) in ball))


def eps_of(g, U):
    g = g.astype(np.complex128)
    return float(np.linalg.norm(g - U @ (U.conj().T @ g)) / np.linalg.norm(g))


def hermite_psi(n, x):
    p0 = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
    if n == 0:
        return p0
    p1 = np.sqrt(2.0) * x * p0
    if n == 1:
        return p1
    for m in range(2, n + 1):
        p2 = np.sqrt(2.0 / m) * x * p1 - np.sqrt((m - 1) / m) * p0
        p0, p1 = p1, p2
    return p1


def test_vectors(q):
    h = np.sqrt(2 * np.pi / q)
    xb = h * (np.arange(q) - (q - 1) / 2.0)
    k = np.arange(q)
    out = []
    for n in range(7):
        out.append((f"B:hermite{n}", hermite_psi(n, xb).astype(np.complex128)))
    for m in range(7):
        out.append((f"T:m={m}", np.exp(2j * np.pi * m * k / q)))
    out.append(("T:t1", (1 + np.cos(2 * np.pi * k / q)).astype(np.complex128)))
    t2 = np.zeros(q, dtype=np.complex128)
    for m in range(-5, 6):
        t2 += 2.0 ** -abs(m) * np.exp(2j * np.pi * m * k / q)
    out.append(("T:t2", t2))
    return out


def main():
    t0 = time.time()
    res_rows, sens_rows, conj_rows, spec_rows = [], [], [], []
    for q in PRIMES:
        n1 = N1[q]
        balls = bfs_ball(q, n1 + 1)
        print(f"[q={q}] |B_{n1}| = {len(balls[n1])}", flush=True)
        # main stage
        U, spectrum, rank, nb = orbit_basis(q, balls[n1], 1)
        pred = min(2 * n1 + 1, q)
        print(f"[q={q}] dim H_q = {rank} (predicted {pred}; distinct b: {nb})", flush=True)
        for i, s in enumerate(spectrum):
            spec_rows.append([q, i, s])
        vecs = test_vectors(q)
        for label, g in vecs:
            res_rows.append([q, label, eps_of(g, U), rank, rank / q, pred])
        # conjugation control
        Uc, _, rank_c, _ = orbit_basis(q, balls[n1], q - 1)
        for label, g in vecs:
            d1 = eps_of(g, U)
            d2 = eps_of(np.conj(g), Uc)
            conj_rows.append([q, label, d1, d2, abs(d1 - d2)])
        # depth sensitivity (fixed: n1-1, n1+1; sensitivity only)
        for d in (n1 - 1, n1 + 1):
            Ud, _, rank_d, _ = orbit_basis(q, balls[d], 1)
            for label, g in vecs:
                sens_rows.append([q, d, label, eps_of(g, Ud), rank_d])
        print(f"[q={q}] done ({time.time() - t0:.0f}s)", flush=True)

    for name, rows, hdr in [
        ("results_canonical.csv", res_rows,
         ["q", "vector", "epsilon", "dim", "dim_over_q", "predicted_dim"]),
        ("sensitivity_canonical.csv", sens_rows, ["q", "depth", "vector", "epsilon", "dim"]),
        ("conjugation_control.csv", conj_rows,
         ["q", "vector", "eps_c1", "eps_conj_qm1", "abs_diff"]),
        ("spectra_canonical.csv", spec_rows, ["q", "index", "sigma"]),
    ]:
        with open(os.path.join(HERE, name), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(hdr)
            w.writerows(rows)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    labels_B = [f"B:hermite{n}" for n in range(7)]
    labels_T = [f"T:m={m}" for m in range(7)] + ["T:t1", "T:t2"]
    for lab in labels_B:
        ax[0].semilogy(PRIMES, [max(r[2], 1e-17) for r in res_rows if r[1] == lab], "o-",
                       label=lab)
    ax[0].set_xlabel("q"); ax[0].set_ylabel("epsilon"); ax[0].legend(fontsize=6)
    ax[0].set_title("Canonical stage: balanced Hermite profiles")
    for lab in labels_T:
        ax[1].semilogy(PRIMES, [max(r[2], 1e-17) for r in res_rows if r[1] == lab], "o-",
                       label=lab)
    ax[1].set_xlabel("q"); ax[1].set_ylabel("epsilon"); ax[1].legend(fontsize=6)
    ax[1].set_title("Canonical stage: toric profiles")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_canonical.pdf"))
    print(f"all outputs written; total {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
