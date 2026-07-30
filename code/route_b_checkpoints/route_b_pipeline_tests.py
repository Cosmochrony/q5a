"""
Pre-registered pipeline checkpoints [H-w'] and [H-Pi3] for Q5a route B.

See PREREGISTRATION.md (frozen before any measurement) for definitions and pass criteria.
Deterministic: uses only the STORED blocks from the O12/O25 npz stores; no new randomness.

Reproduction:
    PYTHONPATH=<numpy+matplotlib path> python3 route_b_pipeline_tests.py

Outputs (this directory): results_hw.csv, results_hpi3.csv, robustness_hw.csv,
fig_hw.pdf, fig_hpi3.pdf, PROVENANCE.md.
"""

import csv
import hashlib
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DATA_DIR = os.path.join(ROOT, "admissibility", "o14", "code", "o14_pipeline")
GEN_DIR = os.path.join(ROOT, "admissibility", "o25", "code")
sys.path.insert(0, GEN_DIR)

import spectral_O12 as o12  # noqa: E402  (build_generators, fingerprint_vectors_batch, ...)

PRIMES = [29, 61, 101, 151, 211]
N_CUT = {29: 5, 61: 7, 101: 10, 151: 12, 211: 13}  # stored fitting-window n1 (frozen)
HERMITE_MAX = 6
EPS_SKIP = 1e-12
CHUNK = 20000


def sha256(path):
    hh = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            hh.update(blk)
    return hh.hexdigest()


def git_head(path):
    try:
        return subprocess.run(["git", "-C", path, "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        return "unknown"


def bfs_depth_capped(q, gens, depth):
    """BFS layers of the Cayley graph up to given depth.
    Identical layers to o12.bfs_shells (same heisenberg_mul, same generating set);
    only the stopping rule differs (depth cap instead of node-fraction cap)."""
    identity = (0, 0, 0)
    visited = {identity}
    current = [identity]
    shells = [current]
    for _ in range(depth):
        nxt = []
        for u in current:
            for g in gens:
                v = o12.heisenberg_mul(u, tuple(g), q)
                if v not in visited:
                    visited.add(v)
                    nxt.append(v)
        if not nxt:
            break
        shells.append(nxt)
        current = nxt
    return shells


def build_basis(q, shells, c_block, gens_arr, n_cut, eps_gs):
    """Gram-Schmidt basis of fingerprint vectors over shells 0..n_cut (rows orthonormal)."""
    basis = None
    for n in range(min(n_cut, len(shells) - 1) + 1):
        shell_arr = np.array(shells[n], dtype=np.int64)
        vecs = o12.fingerprint_vectors_batch(shell_arr, c_block, gens_arr, q)
        basis, _ = o12.gram_schmidt_batch(basis, vecs, eps=eps_gs)
    return basis


def gen_apply(name, M, q, x):
    """Apply generator to rows of M (N, q). x = centered balanced positions."""
    if name == "Y+":
        return np.roll(M, -1, axis=1)
    if name == "Y-":
        return np.roll(M, 1, axis=1)
    h = np.sqrt(2 * np.pi / q)
    phase = np.exp(1j * h * x)
    if name == "Xc+":
        return M * phase[None, :]
    if name == "Xc-":
        return M * np.conj(phase)[None, :]
    raise ValueError(name)


def weights_for(q, shells, c_block, gens_arr, n_cut, eps_gs, basis=None):
    """a_q(s) for the four generators: mean ||(rho_s - I)u||^2 over unit-normalised
    projected fingerprints of shells 0..n_cut."""
    if basis is None:
        basis = build_basis(q, shells, c_block, gens_arr, n_cut, eps_gs)
    h = np.sqrt(2 * np.pi / q)
    x = h * (np.arange(q) - (q - 1) / 2.0)
    sums = {s: 0.0 for s in ("Y+", "Y-", "Xc+", "Xc-")}
    count = 0
    skipped = 0
    for n in range(min(n_cut, len(shells) - 1) + 1):
        shell_arr = np.array(shells[n], dtype=np.int64)
        vecs = o12.fingerprint_vectors_batch(shell_arr, c_block, gens_arr, q)
        for lo in range(0, vecs.shape[0], CHUNK):
            V = vecs[lo:lo + CHUNK]
            P = (V @ basis.conj().T) @ basis        # Pi_q V
            nrm = np.linalg.norm(P, axis=1)
            keep = nrm > EPS_SKIP
            skipped += int((~keep).sum())
            U = P[keep] / nrm[keep][:, None]
            count += U.shape[0]
            for s in sums:
                D = gen_apply(s, U, q, x) - U
                sums[s] += float(np.sum(np.abs(D) ** 2))
    return {s: sums[s] / count for s in sums}, count, skipped, basis


def hermite_psi(n, x):
    """Normalised Hermite functions psi_n (physicists'), via stable recurrence."""
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


def hpi3_for(q, basis):
    """epsilon_{q,n}, window and discretisation errors for Hermite n = 0..HERMITE_MAX."""
    h = np.sqrt(2 * np.pi / q)
    x = h * (np.arange(q) - (q - 1) / 2.0)
    rows = []
    fine = np.arange(-25.0, 25.0, 1e-3)
    for n in range(HERMITE_MAX + 1):
        g = hermite_psi(n, x).astype(np.complex128)
        gn = np.linalg.norm(g)
        proj = (g @ basis.conj().T) @ basis
        eps = np.linalg.norm(g - proj) / gn
        psi_f = hermite_psi(n, fine)
        tot = np.sum(psi_f ** 2) * 1e-3
        win = np.sqrt(np.sum(psi_f[np.abs(fine) > q * h / 2] ** 2) * 1e-3 / tot)
        # discretisation: || iota iota* psi - psi || / ||psi|| via sinc synthesis on the fine grid
        synth = np.zeros_like(fine)
        for k in range(q):
            synth += hermite_psi(n, x[k]) * np.sinc((fine - x[k]) / h)
        disc = np.sqrt(np.sum((synth - psi_f) ** 2) * 1e-3 / tot)
        rows.append((q, n, eps, win, disc))
    return rows


def ols_loglog(qs, ys):
    lx, ly = np.log(np.array(qs, float)), np.log(np.array(ys, float))
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, res, _, _ = np.linalg.lstsq(A, ly, rcond=None)
    fit = A @ coef
    return coef[0], float(np.std(ly - fit))


def main():
    t0 = time.time()
    gens_list = o12.build_generators(29)
    gens_arr = np.array(gens_list, dtype=np.int64)

    prov = ["# Provenance — route B pipeline checkpoints", ""]
    prov.append(f"- generator code: admissibility/o25/code/spectral_O12.py @ commit "
                f"{git_head(os.path.join(ROOT, 'admissibility', 'o25'))} (o25 repo)")
    prov.append(f"- data repo commit: {git_head(os.path.join(ROOT, 'admissibility', 'o14'))} (o14 repo)")
    prov.append("- BFS: depth-capped variant of o12.bfs_shells (identical layers; stopping rule only)")
    prov.append(f"- frozen n_cut = stored n1: {N_CUT}")
    prov.append("- reproduction: PYTHONPATH=<numpy+matplotlib> python3 route_b_pipeline_tests.py")
    prov.append("")

    hw_rows, rob_rows, hpi_rows = [], [], []
    for q in PRIMES:
        path = os.path.join(DATA_DIR, f"q{q}_o12.npz")
        d = np.load(path, allow_pickle=True)
        prov.append(f"- q{q}_o12.npz sha256 = {sha256(path)}; seed={int(d['seed'])}; "
                    f"n1={int(d['n1'])}; blocks[0]={list(map(int, d['blocks'][0]))}")
        blocks = d["blocks"].astype(np.int64)
        n_cut = N_CUT[q]
        depth = min(n_cut + 3, 16)
        print(f"[q={q}] BFS to depth {depth} ...", flush=True)
        gens_q = o12.build_generators(q)
        gens_arr_q = np.array(gens_q, dtype=np.int64)
        shells = bfs_depth_capped(q, gens_arr_q, depth)
        print(f"[q={q}] shells: {[len(s) for s in shells[:n_cut + 1]]}", flush=True)

        # --- primary [H-w'] + basis reuse for [H-Pi3]
        w, cnt, skip, basis = weights_for(q, shells, blocks[0], gens_arr_q, n_cut,
                                          o12.EPS_GS)
        h2 = 2 * np.pi / q
        hw_rows.append([q, w["Y+"], w["Y-"], w["Xc+"], w["Xc-"], cnt, skip,
                        basis.shape[0], w["Y+"] / h2, w["Xc+"] / h2])
        print(f"[q={q}] primary a_q: Y+={w['Y+']:.4g} Y-={w['Y-']:.4g} "
              f"Xc+={w['Xc+']:.4g} Xc-={w['Xc-']:.4g} (rank {basis.shape[0]}, {cnt} vecs)",
              flush=True)

        # --- robustness grid
        variants = {"ncut+3": (min(n_cut + 3, len(shells) - 1), blocks[0], o12.EPS_GS),
                    "eps/10": (n_cut, blocks[0], o12.EPS_GS / 10)}
        for name, (nc, blk, eps) in variants.items():
            wv, cv, sv, _ = weights_for(q, shells, blk, gens_arr_q, nc, eps)
            rob_rows.append([q, name, wv["Y+"], wv["Y-"], wv["Xc+"], wv["Xc-"], cv])
        wm = {s: [] for s in ("Y+", "Y-", "Xc+", "Xc-")}
        for b in range(min(5, blocks.shape[0])):
            wv, cv, sv, _ = weights_for(q, shells, blocks[b], gens_arr_q, n_cut, o12.EPS_GS)
            for s in wm:
                wm[s].append(wv[s])
        rob_rows.append([q, "mean5blocks", np.mean(wm["Y+"]), np.mean(wm["Y-"]),
                        np.mean(wm["Xc+"]), np.mean(wm["Xc-"]), -1])
        conj = [b for b in blocks if int(b[0]) == (q - int(blocks[0][0])) % q]
        if len(conj):
            wv, cv, sv, _ = weights_for(q, shells, conj[0], gens_arr_q, n_cut, o12.EPS_GS)
            rob_rows.append([q, "conjblock",
                             (w["Y+"] + wv["Y+"]) / 2, (w["Y-"] + wv["Y-"]) / 2,
                             (w["Xc+"] + wv["Xc+"]) / 2, (w["Xc-"] + wv["Xc-"]) / 2, cv])
        else:
            rob_rows.append([q, "conjblock", "n/a", "n/a", "n/a", "n/a", 0])

        # --- [H-Pi3]
        hpi_rows.extend(hpi3_for(q, basis))
        print(f"[q={q}] done in {time.time() - t0:.0f}s", flush=True)

    with open(os.path.join(HERE, "results_hw.csv"), "w", newline="") as f:
        wcsv = csv.writer(f)
        wcsv.writerow(["q", "aY+", "aY-", "aXc+", "aXc-", "n_vecs", "n_skipped",
                       "rank", "aY+/h2", "aXc+/h2"])
        wcsv.writerows(hw_rows)
    with open(os.path.join(HERE, "robustness_hw.csv"), "w", newline="") as f:
        wcsv = csv.writer(f)
        wcsv.writerow(["q", "variant", "aY+", "aY-", "aXc+", "aXc-", "n_vecs"])
        wcsv.writerows(rob_rows)
    with open(os.path.join(HERE, "results_hpi3.csv"), "w", newline="") as f:
        wcsv = csv.writer(f)
        wcsv.writerow(["q", "hermite_n", "epsilon", "window_err", "disc_err"])
        wcsv.writerows(hpi_rows)

    # --- rates and figures
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    qs = [r[0] for r in hw_rows]
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    for i, s in enumerate(["aY+", "aY-", "aXc+", "aXc-"]):
        ax[0].loglog(qs, [r[1 + i] for r in hw_rows], "o-", label=s)
    ax[0].set_xlabel("q"); ax[0].set_ylabel("a_q(s)"); ax[0].legend()
    ax[0].set_title("[H-w'] weights, balanced convention")
    for n in range(HERMITE_MAX + 1):
        ys = [r[2] for r in hpi_rows if r[1] == n]
        ax[1].loglog(qs, ys, "o-", label=f"n={n}")
    ax[1].set_xlabel("q"); ax[1].set_ylabel("epsilon_{q,n}"); ax[1].legend(fontsize=7)
    ax[1].set_title("[H-Pi3] projection deficiency")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_hw_hpi3.pdf"))

    prov.append("")
    prov.append("## OLS log-log slopes (value, residual std)")
    for i, s in enumerate(["aY+", "aY-", "aXc+", "aXc-"]):
        ys = [r[1 + i] for r in hw_rows if r[0] >= 61]
        sl, rs = ols_loglog([r[0] for r in hw_rows if r[0] >= 61], ys)
        prov.append(f"- slope[{s}] (q>=61) = {sl:+.3f} (res std {rs:.3f})")
    for n in range(HERMITE_MAX + 1):
        ys = [r[2] for r in hpi_rows if r[1] == n]
        sl, rs = ols_loglog(qs, ys)
        prov.append(f"- slope[eps_n={n}] = {sl:+.3f} (res std {rs:.3f})")
    with open(os.path.join(HERE, "PROVENANCE.md"), "w") as f:
        f.write("\n".join(prov) + "\n")
    print("all outputs written; total %.0fs" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
