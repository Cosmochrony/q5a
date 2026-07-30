"""
Route B prototype: balanced-scaling limit of the finite Weil model (Q5a analysis note).

Scaling: h = sqrt(2*pi/q), centered grid x_k = h*(k - (q-1)/2), window ~ sqrt(2*pi*q).
Generators (centered Weil):
    (rho_X f)(k) = exp(i*h*x_k) f(k)      (modulation, centered character)
    (rho_Y f)(k) = f(k+1 mod q)           (cyclic shift = position step h)
Rescaled:
    Q_q = (rho_X - I)/(i*h)   -> x        P_q = (rho_Y - I)/(i*h) -> -i d/dx
Form (weights a=1, all four generators s in {X,X^-1,Y,Y^-1}):
    E_q(f) = (h^-2 / 2) * sum_s ||(rho_s - I) f||^2   (counting-norm ell^2)
Expected limit on Schwartz profiles: E_q(psi) -> int |psi'|^2 + int x^2 |psi|^2.
Operator: L_q = h^-2 [ (2I - rho_Y - rho_Y^-1) + diag(2 - 2 cos(h x_k)) ];
expected spectrum -> harmonic oscillator 2n+1 (Harper at flux 2*pi/q, band edge).

All quantities deterministic (no randomness). Reproducible with numpy only.
"""

import numpy as np

def grid(q):
    h = np.sqrt(2 * np.pi / q)
    k = np.arange(q)
    x = h * (k - (q - 1) / 2.0)
    return h, x

def herm0(x):
    return np.pi ** -0.25 * np.exp(-x ** 2 / 2)

def herm2(x):
    # normalized Hermite n=2 eigenfunction of -d^2/dx^2 + x^2 (eigenvalue 5)
    H2 = 4 * x ** 2 - 2
    return H2 * np.exp(-x ** 2 / 2) / np.sqrt(8) / np.pi ** 0.25

def dherm0(x):
    return -x * herm0(x)

def dherm2(x):
    return (8 * x * np.exp(-x ** 2 / 2) + (4 * x ** 2 - 2) * (-x) * np.exp(-x ** 2 / 2)) \
        / np.sqrt(8) / np.pi ** 0.25

def run(q, psi, dpsi, E_target):
    h, x = grid(q)
    f = psi(x)                      # sampled profile (width O(1) in x = O(sqrt q) in k)
    nrm2 = h * np.sum(np.abs(f) ** 2)
    # generators
    rhoX = np.exp(1j * h * x) * f
    rhoY = np.roll(f, -1)           # f(k+1)
    Q = (rhoX - f) / (1j * h)
    P = (rhoY - f) / (1j * h)
    errQ = np.sqrt(h * np.sum(np.abs(Q - x * f) ** 2) / nrm2)
    errP = np.sqrt(h * np.sum(np.abs(P - (-1j) * dpsi(x)) ** 2) / nrm2)
    # form with unit weights, four generators
    E = 0.0
    for g in (np.exp(1j * h * x), np.exp(-1j * h * x)):
        E += np.sum(np.abs((g - 1) * f) ** 2)
    for sh in (-1, 1):
        E += np.sum(np.abs(np.roll(f, sh) - f) ** 2)
    E *= (1.0 / h ** 2) * 0.5 * h   # (h^-2/2) * counting-sum, then *h = ell^2_h norm
    errE = abs(E / nrm2 * (nrm2 / (h * np.sum(np.abs(f) ** 2))) - E_target)
    E_over_norm = E / nrm2
    # wraparound magnitude (cyclic seam term)
    wrap = np.abs(f[0] - f[-1]) ** 2 / h ** 2 * h / nrm2
    return errQ, errP, E_over_norm, abs(E_over_norm - E_target), wrap

def spectrum(q, n_eigs=6):
    h, x = grid(q)
    # L_q = h^-2 [ (2I - S - S^T) + diag(2 - 2 cos(h x)) ]
    L = np.zeros((q, q))
    L += np.diag(2.0 + 2.0 - 2.0 * np.cos(h * x))
    for k in range(q):
        L[k, (k + 1) % q] -= 1.0
        L[k, (k - 1) % q] -= 1.0
    L /= h ** 2
    ev = np.linalg.eigvalsh(L)
    return ev[:n_eigs]

if __name__ == "__main__":
    print("q      errQ       errP       E(psi0)   |E-1|      wrap       E(psi2)   |E-5|")
    for q in (29, 61, 101, 151, 211, 401):
        eQ0, eP0, E0, dE0, w0 = run(q, herm0, dherm0, 1.0)
        eQ2, eP2, E2, dE2, w2 = run(q, herm2, dherm2, 5.0)
        print(f"{q:<6d} {eQ0:.3e}  {eP0:.3e}  {E0:.5f}  {dE0:.3e}  {w0:.1e}  {E2:.5f}  {dE2:.3e}")
    print("\nlowest eigenvalues of L_q (target: 1, 3, 5, 7, 9, 11):")
    for q in (29, 61, 101, 151, 211):
        ev = spectrum(q)
        print(f"q={q:<5d} " + "  ".join(f"{e:.4f}" for e in ev))
