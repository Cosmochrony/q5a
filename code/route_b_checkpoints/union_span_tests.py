"""
Pre-registered tests B-v2 (PREREG-B2.md) and T (PREREG-T.md): union-span projector over ALL
central characters, canonical blocks (c1, 1, 1|2), depths up to the stored campaign maximum with
declared termination rules (full rank / 5e6-vector budget).

Deterministic. Reproduction:
    PYTHONPATH=<numpy+matplotlib> python3 union_span_tests.py
Outputs: results_B2.csv, results_T.csv, singular_spectra.csv, robustness_union_stored.csv,
fig_union_span.pdf, PROVENANCE-V2.md.
"""

import csv
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DATA_DIR = os.path.join(ROOT, "admissibility", "o14", "code", "o14_pipeline")
GEN_DIR = os.path.join(ROOT, "admissibility", "o25", "code")
sys.path.insert(0, GEN_DIR)

import spectral_O12 as o12  # noqa: E402

PRIMES = [29, 61, 101, 151, 211]
HERMITE_MAX = 6
FOURIER_MS = [0, 1, 2, 3, 4, 5, 6]
BUDGET = 5_000_000
EPS_MACH = 2.0 ** -52


def bfs_layers(q, gens_arr, depth):
    identity = (0, 0, 0)
    visited = {identity}
    current = [identity]
    shells = [current]
    for _ in range(depth):
        nxt = []
        for u in current:
            for g in gens_arr:
                v = o12.heisenberg_mul(u, tuple(g), q)
                if v not in visited:
                    visited.add(v)
                    nxt.append(v)
        if not nxt:
            break
        shells.append(nxt)
        current = nxt
    return shells


def canonical_blocks(q):
    out = []
    for c1 in range(1, q):
        c3 = 1 if (c1 + 2) % q != 0 else 2
        out.append((c1, 1, c3))
    return np.array(out, dtype=np.int64)


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


def union_gram(q, blocks, n_max, log):
    """Accumulate G = sum V^H V over all blocks x depths, with declared termination rules.
    Returns G, rank trajectory, vectors used, termination reason, depth reached."""
    gens_arr = np.array(o12.build_generators(q), dtype=np.int64)
    G = np.zeros((q, q), dtype=np.complex128)
    used = 0
    ranks = []
    shells = bfs_layers(q, gens_arr, 0)
    depth = 0
    reason = "n_max reached"
    while depth <= n_max:
        if depth >= len(shells):
            more = bfs_layers(q, gens_arr, depth)
            if depth >= len(more):
                reason = "BFS exhausted"
                break
            shells = more
        shell_arr = np.array(shells[depth], dtype=np.int64)
        for blk in blocks:
            V = o12.fingerprint_vectors_batch(shell_arr, blk, gens_arr, q)
            G += V.conj().T @ V
            used += V.shape[0]
        lam = np.linalg.eigvalsh(G)
        sig = np.sqrt(np.clip(lam, 0, None))
        tau = q * np.sqrt(EPS_MACH) * sig.max()
        rank = int((sig > tau).sum())
        ranks.append((depth, rank, used))
        log(f"  depth {depth}: rank {rank}/{q}, {used} vecs")
        if rank == q:
            reason = "full rank"
            break
        if used >= BUDGET:
            stable = len(ranks) >= 2 and ranks[-1][1] == ranks[-2][1]
            reason = "budget (rank stable)" if stable else "BUDGET-TRUNCATED"
            break
        depth += 1
    return G, ranks, used, reason, depth


def projector_from_gram(G, q):
    lam, U = np.linalg.eigh(G)
    sig = np.sqrt(np.clip(lam, 0, None))
    tau = q * np.sqrt(EPS_MACH) * sig.max()
    keep = sig > tau
    return U[:, keep], sig[::-1], int(keep.sum())


def eps_of(g, U):
    g = g.astype(np.complex128)
    proj = U @ (U.conj().T @ g)
    return float(np.linalg.norm(g - proj) / np.linalg.norm(g))


def main():
    t0 = time.time()
    b2_rows, t_rows, spec_rows, rob_rows, prov = [], [], [], [], []
    prov.append("# Provenance v2 — union-span tests (B-v2 and T)")
    prov.append(f"- generator commit (o25): see PROVENANCE.md (identical); "
                f"data SHA256: identical to PROVENANCE.md")
    prov.append(f"- tolerance: sigma > q * sqrt(2^-52) * sigma_max (Gram method, frozen)")
    prov.append(f"- budget: {BUDGET} vectors/prime; canonical blocks (c1, 1, 1|2), all c1")
    for q in PRIMES:
        d = np.load(os.path.join(DATA_DIR, f"q{q}_o12.npz"), allow_pickle=True)
        n_max = len(d["ns"]) - 1
        blocks = canonical_blocks(q)
        print(f"[q={q}] union span: {len(blocks)} characters, depths<= {n_max}", flush=True)
        G, ranks, used, reason, depth = union_gram(
            q, blocks, n_max, lambda s: print(f"[q={q}]{s}", flush=True))
        U, spectrum, rank = projector_from_gram(G, q)
        prov.append(f"- q={q}: termination='{reason}' at depth {depth}, rank {rank}/{q}, "
                    f"{used} vectors; rank trajectory {ranks}")
        for i, s in enumerate(spectrum):
            spec_rows.append([q, i, s])
        # --- B-v2: balanced Hermite profiles
        h = np.sqrt(2 * np.pi / q)
        x_bal = h * (np.arange(q) - (q - 1) / 2.0)
        fine = np.arange(-25.0, 25.0, 1e-3)
        for n in range(HERMITE_MAX + 1):
            g = hermite_psi(n, x_bal)
            eps = eps_of(g, U)
            psi_f = hermite_psi(n, fine)
            tot = np.sum(psi_f ** 2) * 1e-3
            win = np.sqrt(np.sum(psi_f[np.abs(fine) > q * h / 2] ** 2) * 1e-3 / tot)
            synth = np.zeros_like(fine)
            for k in range(q):
                synth += hermite_psi(n, x_bal[k]) * np.sinc((fine - x_bal[k]) / h)
            disc = np.sqrt(np.sum((synth - psi_f) ** 2) * 1e-3 / tot)
            b2_rows.append([q, n, eps, win, disc, rank, rank / q])
        # --- T: toric vectors
        k = np.arange(q)
        for m in FOURIER_MS:
            g = np.exp(2j * np.pi * m * k / q)
            t_rows.append([q, f"m={m}", eps_of(g, U), rank, rank / q])
        t1 = 1 + np.cos(2 * np.pi * k / q)
        t_rows.append([q, "t1", eps_of(t1.astype(np.complex128), U), rank, rank / q])
        t2 = np.zeros(q, dtype=np.complex128)
        for m in range(-5, 6):
            t2 += 2.0 ** -abs(m) * np.exp(2j * np.pi * m * k / q)
        t_rows.append([q, "t2", eps_of(t2, U), rank, rank / q])
        # --- robustness: union over STORED blocks
        Gs, ranks_s, used_s, reason_s, depth_s = union_gram(
            q, d["blocks"].astype(np.int64), n_max, lambda s: None)
        Us, _, rank_s = projector_from_gram(Gs, q)
        eps0 = eps_of(hermite_psi(0, x_bal), Us)
        epsT = eps_of(np.exp(2j * np.pi * 1 * k / q), Us)
        rob_rows.append([q, rank_s, reason_s, eps0, epsT, used_s])
        print(f"[q={q}] done ({time.time() - t0:.0f}s): primary rank {rank}/{q} [{reason}], "
              f"stored-union rank {rank_s}/{q} [{reason_s}]", flush=True)

    for name, rows, hdr in [
        ("results_B2.csv", b2_rows, ["q", "hermite_n", "epsilon", "window_err", "disc_err",
                                     "rank", "rank_over_q"]),
        ("results_T.csv", t_rows, ["q", "vector", "epsilon", "rank", "rank_over_q"]),
        ("singular_spectra.csv", spec_rows, ["q", "index", "sigma"]),
        ("robustness_union_stored.csv", rob_rows, ["q", "rank", "termination",
                                                   "eps_hermite0", "eps_fourier1", "n_vecs"]),
    ]:
        with open(os.path.join(HERE, name), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(hdr)
            w.writerows(rows)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    qs = PRIMES
    for n in range(HERMITE_MAX + 1):
        ax[0].semilogy(qs, [max(r[2], 1e-17) for r in b2_rows if r[1] == n], "o-",
                       label=f"n={n}")
    ax[0].set_xlabel("q"); ax[0].set_ylabel("epsilon (B-v2, Hermite)")
    ax[0].legend(fontsize=7); ax[0].set_title("B-v2: union-span projector, balanced profiles")
    for lab in [f"m={m}" for m in FOURIER_MS] + ["t1", "t2"]:
        ax[1].semilogy(qs, [max(r[2], 1e-17) for r in t_rows if r[1] == lab], "o-", label=lab)
    ax[1].set_xlabel("q"); ax[1].set_ylabel("epsilon (T, toric)")
    ax[1].legend(fontsize=6); ax[1].set_title("T: union-span projector, toric profiles")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_union_span.pdf"))
    with open(os.path.join(HERE, "PROVENANCE-V2.md"), "w") as f:
        f.write("\n".join(prov) + "\n")
    print(f"all outputs written; total {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
