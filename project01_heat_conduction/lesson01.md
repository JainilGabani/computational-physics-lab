# Project 1 · Lesson 1 — Steady 1D conduction with heat generation

## 1. Objective
Derive the steady 1D heat equation from energy conservation, solve it analytically, discretize it with finite differences, and use the result to **generate a dimension from a requirement**.

## 2. Why it matters
This is the smallest complete instance of the loop:
requirement (max temperature rise) → physics (energy conservation + Fourier) → math (ODE) → algorithm (linear system) → **geometry (a thickness)** → verification.
Every later project — cold plates, nozzles, brackets — is this loop with more physics and more dimensions. If this loop is not airtight in 1D, it will be garbage in 3D.

Engineering context (illustrative): a battery cell or potted power-electronics block generates heat internally and is cooled on both faces. How thick may it be before the centre overheats?

## 3. Physics

### Conservation of energy (steady state, no flow)
Energy entering a volume + energy generated inside = energy leaving.

### Fourier's law
`q = −k dT/dx`

| Item | Content |
|---|---|
| Physical meaning | Heat flows from hot to cold, at a rate proportional to the temperature gradient. |
| Origin | Empirical (Fourier, 1822). Microscopically: phonon and electron transport averaged over many collisions. It is a *constitutive law*, not a conservation law. |
| Variables | `q` heat flux [W/m²]; `k` thermal conductivity [W/(m·K)]; `dT/dx` [K/m]; `T` [K or °C — differences are identical]. |
| Assumptions | Continuum; local thermodynamic equilibrium; isotropic material (else `k` is a tensor); linear response. |
| Limitations | Fails near the phonon mean free path (nanoscale) and in ultrafast transients. **Anisotropy matters in your future work**: battery cells (in-plane k ≈ 20–30× cross-plane), composites, and AM metal parts (build-direction dependence). `k` also varies with temperature. |
| Becomes an algorithm | Flux between two nodes ≈ `−k (T_{i+1} − T_i)/Δx`. |
| Becomes geometry | Combined with conservation, it fixes how thick a part may be for a given temperature limit. |
| Verification | Compare discrete solution with the exact analytical solution. |

## 4. Mathematics — derivation

Slab of thickness `L`, face area `A`, uniform volumetric generation `q'''` [W/m³], both faces held at `T_s`. Assume `L ≪` lateral dimensions so heat flows only in `x`.

Take a thin slice between `x` and `x + dx`:

```
in at x:        q(x)·A
generated:      q'''·A·dx
out at x+dx:    q(x+dx)·A
```

Steady state:  `q(x)A + q'''A dx = q(x+dx)A`

Taylor-expand `q(x+dx) ≈ q(x) + (dq/dx)dx`, cancel, divide by `A dx`:

```
dq/dx = q'''
```

Substitute Fourier's law with constant `k`:

```
d²T/dx² = −q'''/k            ← governing equation
T(0) = T_s,   T(L) = T_s       ← boundary conditions (Dirichlet)
```

Check units: left side K/m². Right side (W/m³)/(W/(m·K)) = K/m². ✔

Solving this analytically is **your exercise**. You need: integrating twice and applying two boundary conditions.

## 5. Computational thinking — finite differences

Replace the continuous `T(x)` with values at `N+1` equally spaced nodes:
`x_i = iΔx`, `Δx = L/N`, `i = 0 … N`.

Approximate the second derivative using Taylor series about `x_i`:

```
T(x+Δx) = T + ΔxT' + (Δx²/2)T'' + (Δx³/6)T''' + (Δx⁴/24)T'''' + …
T(x−Δx) = T − ΔxT' + (Δx²/2)T'' − (Δx³/6)T''' + (Δx⁴/24)T'''' − …
```

Add them; odd terms cancel:

```
T'' = (T_{i+1} − 2T_i + T_{i−1})/Δx²  −  (Δx²/12)·T''''  + …
```

The neglected term is the **truncation error**, proportional to `Δx²` → "second-order accurate". Note *what* it is proportional to besides `Δx²`. You will need that observation in the exercise.

Discrete equation at each interior node `i = 1 … N−1`:

```
T_{i−1} − 2T_i + T_{i+1} = −q'''_i Δx² / k
```

Boundary nodes: `T_0 = T_s`, `T_N = T_s`.

That is `N+1` linear equations in `N+1` unknowns: **A·T = b**, where `A` is tridiagonal. The physics problem has become a linear-algebra problem. That conversion — PDE → matrix — is what every FEA/CFD package does underneath.

## 6. Python — what you need for this lesson

```python
import numpy as np                 # NumPy: fast arrays + linear algebra

x = np.linspace(0.0, 0.03, 7)      # 7 evenly spaced points from 0 to 0.03 (inclusive)
A = np.zeros((7, 7))               # 7×7 matrix of zeros
b = np.zeros(7)                    # vector of 7 zeros
A[0, 0] = 1.0                      # row 0, column 0 (Python indexes from 0)
b[-1] = 25.0                       # -1 = last element
T = np.linalg.solve(A, b)          # solves A·T = b (LU factorisation underneath)
err = np.max(np.abs(T - T_exact))  # element-wise ops on whole arrays — no loop needed
```

A function can be passed as an argument:

```python
q_func = lambda x: 5e4 * np.ones_like(x)   # a tiny unnamed function: q(x) = 5e4 everywhere
q_values = q_func(x)                        # evaluate at every node at once
```

## 7. Verification (concept)
- **Verification**: did I solve the equations *right*? (code vs. mathematics)
- **Validation**: did I solve the *right* equations? (mathematics vs. reality)

This lesson only verifies. A perfectly verified model of a slab with the wrong `k` or wrong boundary condition is still wrong about the real part.

## 8. Geometry
In this lesson the "geometry" is one number: the thickness. That is deliberate. The principle — **a dimension exists because a physical limit forced it** — is the same whether the output is one number or a lattice of 10⁶ voxels. Lesson 3 turns a thermal field into a 2D profile.

## 9. Manufacturing
Covered as a question in the exercise: what happens when the physics-generated dimension conflicts with another requirement?

## 10–11. Challenge and failure test
See `exercise01.md`.

## 12. Engineering review
After you submit.

## 13. Next level
Lesson 2: convective boundary conditions (Robin), the fin equation, Biot number, and the first shape that *emerges* from physics: a fin whose profile is generated from a heat-flux requirement.
