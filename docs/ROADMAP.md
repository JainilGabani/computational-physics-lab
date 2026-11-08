# Roadmap

Rule: a level is passed when you can **demonstrate** it (derivation, working verified code, defended review), not when you have read about it.

Time estimates assume ~10–15 focused hours/week. They are honest guesses, not promises. Most people take longer.

| Level | Capability you must demonstrate | Projects | Est. time |
|---|---|---|---|
| 0 | Python + NumPy fluency; calculus, linear algebra, ODEs at working level | Diagnostic, drills inside Project 1 | 1–3 months (parallel) |
| 1 | Derive governing equations from conservation laws; solve analytically; check units and limits | P1 Lessons 1–2 | weeks |
| 2 | Discretize ODE/PDE, solve, prove convergence order, verify against analytical solutions | P1 (1D → 2D, steady → transient) | 2–3 months |
| 3 | Geometry as an output of a physics model (thickness, profiles, fields → shapes) | P1 geometry stage, P2 start | 2–3 months |
| 4 | Automated component generator: requirements in, verified geometry + manufacturability check out | P2 heat exchanger, P3 pressure vessel | 4–6 months |
| 5 | Coupled physics (thermal–fluid, thermal–structural, compressible flow) | P4 nozzle, P5 cooling plate | 6–9 months |
| 6 | System models: components interacting, trade-offs, sensitivity, uncertainty | P5, P8 thermal management | 6–12 months |
| 7 | Automotive subsystems with load cases, fatigue, real manufacturing processes | P6 suspension, P7 chassis | 1–2 years |
| 8 | Vehicle-level architecture model (mass–energy–range–aero–structure–packaging) | P9 | 1–2 years |
| 9 | Manufacturing system modelling: process, cost, tooling, volume economics | — | parallel, years |
| 10 | Reusable computational platform with model updating from test data | Framework built across P1–P9 | continuous |
| 11 | Physical prototype vehicle | — | needs team + capital |
| 12 | Automotive company | — | needs team + capital + regulatory + supply chain |

Levels 0–6 are achievable by one disciplined person. Levels 7–12 are not solo activities.

## Project sequence

1. Computational heat conduction (1D → 2D → transient → geometry from thermal field)
2. Physics-driven heat exchanger / channel network
3. Pressure vessel / structural component
4. Computational nozzle (quasi-1D compressible flow → contour → CFD comparison)
5. Automotive cooling system (battery cold plate, motor cooling)
6. Suspension component
7. Chassis structure
8. Vehicle thermal management system
9. Computational vehicle architecture

## The software you will end up with

Built incrementally, never designed up front:

```
requirements → physics models → material models → constraints → manufacturing rules
→ geometry generators → numerical solvers → search/optimization → verification
→ CAD/mesh export → test data → model updating
```

Project 1 produces the first two bricks: a verified solver and a function that turns a requirement into a dimension.
