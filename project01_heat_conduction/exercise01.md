# Exercise 1

Rules: Part A without looking anything up. Show all working for Parts B–C (paper photo or Markdown). Write predictions **before** running code. Do not use an AI or a solver to do Parts B–D for you — that defeats the only purpose of this exercise.

Submit: `answers01.md` + your completed `exercise01_starter.py` + plots.

---

## Part A — Diagnostic (honest answers only; "I don't know" is useful data)

1. Units of thermal conductivity, and what a value of 400 vs 0.2 physically means (name a material for each).
2. Write the Taylor series of `f(x + h)` to third order.
3. Solve by hand: `2a + b = 5`, `a − b = 1`. Then: when does a linear system `A·x = b` have no unique solution?
4. What is the difference between an ODE and a PDE? Give one engineering example of each.
5. In your own words: what does the divergence theorem say physically?
6. What does `x[1:-1]` return for `x = np.array([10, 20, 30, 40, 50])`?
7. Write a Python function that takes a list of numbers and returns their mean, without using any library.
8. In your own words: verification vs. validation. Give an example where a model is verified but not valid.
9. What have you actually built before (code, CAD, simulation, hardware)? One line each. No inflating.

## Part B — Derivation

1. Integrate `d²T/dx² = −q'''/k` with `T(0) = T(L) = T_s`. Find `T(x)`.
2. Find the location and value of the maximum temperature rise `ΔT_max = T_max − T_s`.
3. Invert the result: given an allowed rise `ΔT_allow`, derive the maximum allowed thickness `L_max(k, q''', ΔT_allow)`.
4. Check units of every result.
5. Limiting cases — answer *physically*, then confirm with your formula:
   - `q''' → 0`
   - `k → ∞`
   - `L` doubles: what happens to `ΔT_max`? Why is it not doubling?
6. One face is now perfectly insulated (`dT/dx = 0` at `x = 0`), the other at `T_s`. Without re-deriving everything: how does `L_max` change? (Hint: symmetry.)

## Part C — Prediction (before coding)

Illustrative numbers (order-of-magnitude, **not** datasheet values):
`k = 1.0 W/(m·K)`, `q''' = 5.0×10⁴ W/m³`, `T_s = 25 °C`, `ΔT_allow = 5 K`.

1. Compute `L_max` by hand.
2. If the cell chemistry generates twice the heat (fast charging), what is the new `L_max`? By what factor did it change?
3. Which input do you trust least, and how much would a ±50 % error in it change `L_max`?

## Part D — Implementation (`exercise01_starter.py`)

1. Implement `analytical_temperature`, `solve_fd`, `max_thickness`.
2. On paper first: write out the full matrix `A` and vector `b` for `N = 4`.
3. Run the comparison at `L = L_max`. Check that the numerical `ΔT_max` equals `ΔT_allow`.
4. Run the convergence study for **Case 1 (uniform q''')**. Before running, predict the slope on the log–log plot. Run it. **Explain what you see** using the truncation-error term from the lesson.
5. **Case 2**: `q'''(x) = q₀ sin(πx/L)`. Derive its analytical solution, implement it, rerun the convergence study. Report the observed order of accuracy (fit the slope).

## Part E — Failure test

1. Run Case 2 with `N = 2`. Compare the predicted `T_max` with the exact value. Express the error as a percentage of the temperature **rise**, not of the absolute temperature — and explain why that is the honest way to report it. Why is the coarse grid wrong in that direction?
2. In Case 1, look closely at the errors for the finest grids. They are not monotonic. What is causing that?
3. Change the boundary condition to `dT/dx = 0` on **both** faces with `q''' > 0`. Try to solve. What happens to the matrix, and what is the *physical* reason no steady solution exists?

## Part F — Engineering judgement

The packaging team says the cell must be **35 mm** thick for energy-content reasons. Your physics says otherwise.
List every lever you have (physical, design, manufacturing, operational), quantify the change each needs, and say which you would pull first and why. "Run a simulation" is not a lever.
