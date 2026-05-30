"""
Shell-by-shell diagnostic for q=61 pair 1 (c=2).
For each shell k in [n0,n1], shows:
  - n_fingerprints
  - max |pi_c[i,0]|^2 * q^2 (should be 1.0 only at xi=0)
  - freq of the fingerprint achieving this max
  - n_above_threshold
  - unique folded frequencies of above-threshold fingerprints

If K>1 appears: which shell introduces the first false detection.
"""
import sys, os, importlib.util, numpy as np

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

npz_dir      = sys.argv[1]
pipeline_dir = sys.argv[2]
q_target     = int(sys.argv[3]) if len(sys.argv) > 3 else 61
pair_target  = int(sys.argv[4]) if len(sys.argv) > 4 else 1

o12 = load_module(os.path.join(pipeline_dir, "spectral_O12.py"),        "o12")
o25 = load_module(os.path.join(pipeline_dir, "o25_paired_pipeline.py"), "o25")

fname = f"q{q_target}_o25.npz"
data  = np.load(os.path.join(npz_dir, fname), allow_pickle=True)
q    = int(data['q'])
n0   = int(data['n0'])
n1   = int(data['n1'])
seed = int(data['seed'])
pi_c    = data['pi_c']
basis_c = data['basis_c']

p = pair_target
c = int(data['pairs'][p, 0])
print(f"q={q}  pair={p}  c={c}  n0={n0}  n1={n1}")

rng  = np.random.default_rng(seed + p*997 + c*7)
cb_c = o25.sample_block_with_c1(c, q, rng)
print(f"cb_c = {cb_c}")

B3 = np.asarray(basis_c[p]).astype(complex)[:3,:]
# phi_0 frequency
fv0 = np.abs(np.fft.fft(B3[0]))**2
xi0 = int(np.argmax(fv0))
print(f"phi_0 peak frequency (unfolded): {xi0}  (folded: {min(xi0, q-xi0)})\n")

gens     = o12.build_generators(q)
gens_arr = np.array(gens, dtype=np.int64)
shells   = o12.bfs_shells(None, None, gens, q, float(data['bfs_frac']))
hmb      = o12.heisenberg_mul_batch
c1,c2,c3 = int(cb_c[0]), int(cb_c[1]), int(cb_c[2])
threshold = 0.5 / q**2

print(f"{'shell':>7}  {'n_elems':>8}  {'n_fp':>7}  {'n_above_thr':>12}  "
      f"{'max*q^2':>8}  {'max_freq':>9}  {'above_freqs'}")
print("-"*80)

for k in range(pi_c.shape[1]):
    s_abs = n0 + k
    if s_abs > n1:
        break
    arr = np.asarray(pi_c[p, k])
    if arr.ndim < 2 or arr.shape[0] == 0:
        print(f"{s_abs:>7d}  EMPTY")
        continue

    shell = np.array(shells[s_abs], dtype=np.int64)
    n_elems = len(shell)

    # Compute frequencies -- chunked to match fingerprint_vectors_batch ordering
    CHUNK_SIZE = 400
    freqs_all_chunks = []
    for cstart in range(0, len(shell), CHUNK_SIZE):
        chunk = shell[cstart:cstart + CHUNK_SIZE]
        freqs_list = []
        for s1 in gens_arr:
            ep1 = hmb(chunk, s1, q)
            for s2 in gens_arr:
                ep2 = hmb(ep1, s2, q)
                for s3 in gens_arr:
                    ep3 = hmb(ep2, s3, q)
                    xi  = (c1*ep1[:,1].astype(int) +
                           c2*ep2[:,1].astype(int) +
                           c3*ep3[:,1].astype(int)) % q
                    freqs_list.append(xi)
        freqs_all_chunks.append(np.concatenate(freqs_list))
    freqs = np.concatenate(freqs_all_chunks)

    n_fp = arr.shape[0]
    if len(freqs) != n_fp:
        print(f"{s_abs:>7d}  SIZE MISMATCH: freqs={len(freqs)} vs pi_c={n_fp}")
        continue

    col0 = np.abs(arr[:, 0])**2
    max_val = col0.max()
    max_i   = int(np.argmax(col0))
    max_xi  = int(freqs[max_i])
    max_xi_f= min(max_xi, q-max_xi)

    above_mask = col0 > threshold
    n_above    = above_mask.sum()
    above_xi_set = set()
    for i in np.where(above_mask)[0]:
        xi = int(freqs[i])
        above_xi_set.add(min(xi, q-xi))

    print(f"{s_abs:>7d}  {n_elems:>8d}  {n_fp:>7d}  {n_above:>12d}  "
          f"{max_val*q**2:>8.4f}  {max_xi_f:>9d}  {sorted(above_xi_set)}")