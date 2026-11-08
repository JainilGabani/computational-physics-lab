"""
Project 1, Exercise 1 — steady 1D conduction with internal heat generation.

Governing equation:  d²T/dx² = -q'''(x) / k,   T(0) = T(L) = T_s

YOU write the three functions marked TODO. The plumbing below them
(convergence study, plotting) is given and commented so you can learn from it.
Run with:  python exercise01_starter.py
"""

import numpy as np                 # arrays and linear algebra
import matplotlib.pyplot as plt    # plotting

# ---------------------------------------------------------------------------
# Inputs (SI units). Illustrative values — NOT datasheet data.
# ---------------------------------------------------------------------------
K = 1.0          # thermal conductivity            [W/(m·K)]
Q0 = 5.0e4       # volumetric heat generation      [W/m³]
T_S = 25.0       # surface temperature             [°C]
DT_ALLOW = 5.0   # allowed centre-to-surface rise  [K]


# ---------------------------------------------------------------------------
# TODO 1: physics → geometry
# ---------------------------------------------------------------------------
def max_thickness(k, q0, dT_allow):
    """Return the largest slab thickness L [m] whose centre rise equals dT_allow.
    Derive the formula in Part B first. One line of code."""
    raise NotImplementedError("Derive L_max in Part B, then implement it here.")


# ---------------------------------------------------------------------------
# TODO 2: exact solution (Case 1: uniform q''')
# ---------------------------------------------------------------------------
def analytical_temperature(x, L, k, q0, T_s):
    """Exact T(x) for uniform generation q0. `x` is a NumPy array;
    return an array of the same shape (no loop needed)."""
    raise NotImplementedError("Derive T(x) in Part B, then implement it here.")


# ---------------------------------------------------------------------------
# TODO 3: the numerical solver
# ---------------------------------------------------------------------------
def solve_fd(L, k, q_func, T_s, N):
    """Finite-difference solution on N+1 nodes.

    q_func : a function q(x) returning q''' [W/m³] at an array of positions.
    Returns (x, T), both NumPy arrays of length N+1.

    Steps:
      1. build x with np.linspace, compute dx
      2. A = np.zeros((N+1, N+1)), b = np.zeros(N+1)
      3. boundary rows 0 and N: T = T_s
      4. interior rows i = 1..N-1: T[i-1] - 2T[i] + T[i+1] = -q_i dx² / k
      5. T = np.linalg.solve(A, b)
    """
    raise NotImplementedError("Write out A and b for N=4 on paper first.")


# ---------------------------------------------------------------------------
# Given plumbing — read every line and make sure you understand it.
# ---------------------------------------------------------------------------
def convergence_study(L, q_func, exact_func, N_list):
    """Max nodal error for each grid size in N_list."""
    errors = []                                   # empty list; we append to it
    for N in N_list:                              # loop over grid sizes
        x, T = solve_fd(L, K, q_func, T_S, N)     # numerical solution
        err = np.max(np.abs(T - exact_func(x)))   # worst nodal error
        errors.append(err)
    return np.array(errors)                       # list → array for maths


def main():
    L = max_thickness(K, Q0, DT_ALLOW)
    print(f"Generated thickness L_max = {L*1000:.2f} mm")   # f-string formatting

    uniform_q = lambda x: Q0 * np.ones_like(x)              # Case 1 source
    exact_1 = lambda x: analytical_temperature(x, L, K, Q0, T_S)

    # --- comparison plot ---------------------------------------------------
    x, T = solve_fd(L, K, uniform_q, T_S, N=10)
    x_fine = np.linspace(0.0, L, 200)
    print(f"Numerical centre rise = {T.max() - T_S:.4f} K (target {DT_ALLOW} K)")

    plt.figure()
    plt.plot(x_fine * 1000, exact_1(x_fine), label="analytical")
    plt.plot(x * 1000, T, "o", label="finite difference, N=10")
    plt.xlabel("x [mm]")
    plt.ylabel("T [°C]")
    plt.legend()
    plt.savefig("case1_profile.png", dpi=150)

    # --- convergence study --------------------------------------------------
    N_list = np.array([4, 8, 16, 32, 64, 128])
    err_1 = convergence_study(L, uniform_q, exact_1, N_list)
    print("Case 1 errors:", err_1)

    # TODO (Part D5): define Case 2 source and its exact solution, then
    # err_2 = convergence_study(L, sine_q, exact_2, N_list)
    # Fit observed order:  slope = np.polyfit(np.log(L / N_list), np.log(err_2), 1)[0]

    plt.figure()
    plt.loglog(L / N_list, err_1 + 1e-18, "o-", label="Case 1")  # +1e-18 avoids log(0)
    plt.xlabel("dx [m]")
    plt.ylabel("max |error| [K]")
    plt.legend()
    plt.savefig("convergence.png", dpi=150)
    print("Saved case1_profile.png and convergence.png")


if __name__ == "__main__":   # runs main() only when this file is executed directly
    main()
