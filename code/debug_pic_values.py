"""
Minimal diagnostic: for q=61 pair 1 (c=2, first delocalized case),
print the 10 largest |pi_c[i,0]|^2 and their computed frequencies.
If phi_0 is a pure mode at xi_0: only ONE frequency should dominate.
If K=22 is real: 22 distinct frequencies should each have max ~1/q^2.
"""
import sys, os, importlib.util, numpy as np

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

npz_dir      = sys.argv[1]
pipeline_dir = sys.argv[2]

o12 = load_module(os.path.join(pipeline_dir, "spectral_O12.py"),        "o12")
o25 = load_module(os.path.join(pipeline_dir, "o25_paired_pipeline.py"), "o25")

data = np.load(os.path.join(npz_dir, "q61_o25.npz"), allow_pickle=True)
q    = int(data['q'])
n0   = int(data['n0'])
n1   = int(data['n1'])
seed = int(data['seed'])
pi_c    = data['pi_c']
basis_c = data['basis_c']

# ---- pair 1 (c=2) : the first K>>1 case ----
p = 1
c = int(data['pairs'][p, 0])
print(f"q={q}, pair={p}, c={c}, n0={n0}, n1={n1}")

rng  = np.random.default_rng(seed + p*997 + c*7)
cb_c = o25.sample_block_with_c1(c, q, rng)
print(f"cb_c = {cb_c}   (c1={cb_c[0]}, c2={cb_c[1]}, c3={cb_c[2]})")

# basis_heff = stored basis_c[p][:3,:]
B = np.asarray(basis_c[p]).astype(complex)
print(f"basis_c[p] shape = {B.shape}")
B3 = B[:3, :]
G  = B3 @ B3.conj().T
print(f"Gram matrix of basis_c[p][:3,:] (should be I):\n{np.round(G,4)}")
for j in range(3):
    fv = np.abs(np.fft.fft(B3[j]))**2
    xi = int(np.argmax(fv))
    if xi > q//2: xi = q-xi
    print(f"  row {j}: ||phi_j||={np.linalg.norm(B3[j]):.4f}, "
          f"peak_xi={xi}, peak_mass={fv[int(np.argmax(fv))]:.4e}, "
          f"second_mass={sorted(fv)[-2]:.4e}")

# pi_c for shell 0
arr0 = np.asarray(pi_c[p, 0])   # (N_s, 3)
print(f"\npi_c[{p},0] shape = {arr0.shape}")
col0 = np.abs(arr0[:,0])**2
print(f"  col 0:  max={col0.max():.4e}  1/q^2={1/q**2:.4e}  "
      f"n_above_threshold={( col0 > 0.5/q**2 ).sum()}")

# BFS + frequency computation
gens     = o12.build_generators(q)
gens_arr = np.array(gens, dtype=np.int64)
shells   = o12.bfs_shells(None, None, gens, q, float(data['bfs_frac']))
shell    = np.array(shells[n0], dtype=np.int64)
print(f"\nShell n0={n0}: {len(shell)} BFS elements  -> {len(shell)*64} fingerprints")

hmb = o12.heisenberg_mul_batch
c1,c2,c3 = int(cb_c[0]), int(cb_c[1]), int(cb_c[2])
freqs_all = []
for s1 in gens_arr:
    ep1 = hmb(shell, s1, q)
    for s2 in gens_arr:
        ep2 = hmb(ep1, s2, q)
        for s3 in gens_arr:
            ep3 = hmb(ep2, s3, q)
            xi  = (c1*ep1[:,1].astype(int) +
                   c2*ep2[:,1].astype(int) +
                   c3*ep3[:,1].astype(int)) % q
            freqs_all.append(xi)
freqs = np.concatenate(freqs_all)
print(f"Frequency range: [{freqs.min()}, {freqs.max()}]  "
      f"unique freqs = {len(np.unique(freqs))}")

# Top-10 |pi_c[i,0]|^2 values and their frequencies
top10 = np.argsort(col0)[-10:][::-1]
print(f"\nTop-10 |pi_c[i,0]|^2 values  (1/q^2 = {1/q**2:.4e}):")
print(f"  {'i':>6}  {'xi_computed':>12}  {'xi_folded':>10}  "
      f"{'|pi_c|^2':>12}  {'|pi_c|^2 * q^2':>14}")
for i in top10:
    xi   = int(freqs[i])
    xif  = min(xi, q-xi)
    print(f"  {i:>6d}  {xi:>12d}  {xif:>10d}  {col0[i]:>12.4e}  {col0[i]*q**2:>14.6f}")

# DIRECT CHECK: recompute pi_c[top10[0], 0] directly from basis_c and fingerprint
i0 = top10[0]
print(f"\nDirect recomputation of pi_c[{i0}, 0]:")
print(f"  From stored pi_c: {arr0[i0, 0]:.6e}")
# Recompute fingerprint for index i0
total_per_gen_combo = len(shell)
s1_idx = i0 // (total_per_gen_combo * 16)
rem    = i0 % (total_per_gen_combo * 16)
s2_idx = rem // (total_per_gen_combo * 4)
rem2   = rem % (total_per_gen_combo * 4)
s3_idx = rem2 // total_per_gen_combo
elem_idx = rem2 % total_per_gen_combo
s1 = gens_arr[s1_idx]; s2 = gens_arr[s2_idx]; s3 = gens_arr[s3_idx]
g  = shell[elem_idx]
ep1 = hmb(np.array([g]), s1, q)[0]
ep2 = hmb(np.array([ep1]), s2, q)[0]
ep3 = hmb(np.array([ep2]), s3, q)[0]
vfp = o12.fingerprint_vectors_batch(
    np.array([g]), np.array([c1,c2,c3]), gens_arr, q
)
i_in_batch = s1_idx*16 + s2_idx*4 + s3_idx
v_i = vfp[i_in_batch]
phi0 = B3[0]
pi_recomputed = np.dot(phi0.conj(), v_i)
print(f"  Recomputed directly: {pi_recomputed:.6e}")
print(f"  Match: {abs(arr0[i0,0] - pi_recomputed) < 1e-10}")
xi_freq = (c1*int(ep1[1]) + c2*int(ep2[1]) + c3*int(ep3[1])) % q
print(f"  Frequency: {xi_freq}  (folded: {min(xi_freq,q-xi_freq)})")
print(f"  |<phi0, v_i>|^2 = {abs(pi_recomputed)**2:.4e}  vs 1/q^2 = {1/q**2:.4e}")