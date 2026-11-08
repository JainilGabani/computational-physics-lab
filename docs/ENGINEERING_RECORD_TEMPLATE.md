# Engineering Record — <project / lesson>

Copy this file into every project. An empty section is a finding, not a formatting issue.

1. **Requirements** — what must be achieved, with numbers and units.
2. **Assumptions** — each one stated, with the reason it is acceptable and what breaks if it is wrong.
3. **Governing equations** — derived, not quoted.
4. **Inputs** — every parameter, units, source (measured / datasheet / assumed).
5. **Outputs** — what the model produces.
6. **Constraints** — what cannot be violated (physics, manufacturing, cost, safety).
7. **Objectives** — what is being improved, and how it is measured.
8. **Numerical method** — discretization, solver, expected order of accuracy.
9. **Geometry generation** — how the solution becomes shape.
10. **Manufacturing** — process, limits, how they are encoded in the model.
11. **Verification** — evidence the math is implemented correctly (analytical comparison, convergence order).
12. **Validation** — evidence reality agrees (experiment, trusted data). "Not yet validated" is an acceptable answer; pretending is not.
13. **Uncertainty** — which inputs dominate the output uncertainty, and by how much.
14. **Failure modes** — of the product *and* of the model.
