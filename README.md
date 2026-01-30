# Prime Number Theorem And...

![Lean](https://img.shields.io/badge/Lean-v4.27.0-blue)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-lightblue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Blueprint: Website](https://img.shields.io/badge/Blueprint-Website-blue.svg?logo=github&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/blueprint)
[![Docs: Website](https://img.shields.io/badge/Docs-Website-blue.svg?logo=readthedocs&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs)

> **Side-by-Side Blueprint Integration**: This fork demonstrates the SBS toolchain
> on a large-scale formalization (530 `@[blueprint]` annotations across 33 files).
> Zero changes to Lean proof code were required.
>
> Original project: [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd)

## Project Overview

The objective of this project is to formalize in Lean the Prime Number Theorem (with classical error term), as well as related results such as the Prime Number Theorem in Arithmetic Progressions. A stretch goal would be to obtain the Chebotarev density theorem.

We are also hosting the [Integrated Explicit Analytic Number Theory network](https://www.ipam.ucla.edu/news-research/special-projects/integrated-explicit-analytic-number-theory-network/). A personal log describing the latter project may be [found here](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/wiki/Terence-Tao's-personal-log).

### Mathematical Content

The formalization pursues three parallel approaches to PNT:

1. **Wiener-Ikehara Tauberian theorem** — Following Michael Stoll's "Euler Products" project, which has a proof of PNT missing only the Wiener-Ikehara theorem.

2. **Complex analysis approach** — Develops residue calculus on rectangles, the argument principle, and Mellin transforms to derive PNT with an error term stronger than any power of log savings.

3. **Full treatment via Hadamard factorization** — The most general approach: residue calculus, Hadamard factorization theorem, zero-free region for zeta via Hoffstein-Lockhart+Goldfeld-Hoffstein-Liemann, leading to PNT with exp-root-log savings.

### Key Results

- **WeakPNT**: Prime Number Theorem via Wiener-Ikehara
- **MediumPNT**: PNT with improved error term via contour integration
- **WeakPNT_AP**: Prime Number Theorem in Arithmetic Progressions

## Side-by-Side Blueprint Integration

This project is the **largest integration test** for the Side-by-Side Blueprint toolchain:

| Metric | Value |
|--------|-------|
| Blueprint annotations | 530+ |
| Lean source files | 33 |
| Graph nodes | 530+ |

### Toolchain Components

- [Dress](https://github.com/e-vergo/Dress) — Artifact generation, dependency graph construction, and validation
- [LeanArchitect](https://github.com/e-vergo/LeanArchitect) — `@[blueprint]` attribute for annotating declarations
- [Runway](https://github.com/e-vergo/Runway) — Site generator, dashboard, and paper/PDF generation
- [dress-blueprint-action](https://github.com/e-vergo/dress-blueprint-action) — GitHub Action for automated deployment

### Blueprint Organization

The blueprint uses `\inputleanmodule{}` commands to organize chapters by mathematical topic:

```latex
\chapter{First approach: Wiener-Ikehara Tauberian theorem}
\inputleanmodule{PrimeNumberTheoremAnd.Wiener}

\chapter{Second approach}
\inputleanmodule{PrimeNumberTheoremAnd.Rectangle}
\inputleanmodule{PrimeNumberTheoremAnd.ResidueCalcOnRectangles}
\inputleanmodule{PrimeNumberTheoremAnd.PerronFormula}
...
```

### Performance Notes

The 530+ node dependency graph required optimization in the toolchain:
- O(n^3) transitive reduction is skipped for graphs with >100 nodes
- Sugiyama layout algorithm handles the full graph
- Edge routing uses visibility graph + Dijkstra + Bezier curves

## Building Locally

```bash
./scripts/build_blueprint.sh
```

This script:
1. Builds the toolchain (SubVerso -> LeanArchitect -> Dress -> Runway)
2. Fetches mathlib cache
3. Builds the project with `BLUEPRINT_DRESS=1`
4. Generates the dependency graph
5. Generates the site with Runway
6. Starts a local server at `localhost:8000`

Output is written to `.lake/build/runway/`.

## Zulip

The project is coordinated via a [Lean Zulip channel](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B).

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for instructions on how to claim issues, submit PRs, and participate in the project.

### Quick contributions via Gitpod

If you want to quickly contribute to the project without installing your own copy of Lean, you can do so using Gitpod.
Simply visit: <https://gitpod.io/new/#https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/>, or click the button below:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/new/#https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/)

All the required dependencies will be loaded (this takes a few minutes), after which you will be brought to a web-based
VS Code window, where you can edit the code and submit PRs.

## Related Projects

### Original Project
- [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd) — Original PNT formalization

### SBS Toolchain
- [Dress](https://github.com/e-vergo/Dress) — Artifact generation, dependency graph, validation
- [LeanArchitect](https://github.com/e-vergo/LeanArchitect) — `@[blueprint]` attribute for annotations
- [Runway](https://github.com/e-vergo/Runway) — Site generator, dashboard, paper/PDF
- [dress-blueprint-action](https://github.com/e-vergo/dress-blueprint-action) — GitHub Action for CI/CD

### Other SBS Projects
- [SBS-Test](https://github.com/e-vergo/SBS-Test) — Minimal test project (16 nodes, all 6 status colors)
- [General Crystallographic Restriction](https://github.com/e-vergo/General_Crystallographic_Restriction) — Production example with paper generation

## Prior Art

The Prime Number Theorem has been formalized before:
- Avigad et al. in Isabelle via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/cs/0509025))
- Harrison in HOL Light via Newman's proof ([paper](https://www.cl.cam.ac.uk/~jrh13/papers/mikefest.html))
- Carneiro in Metamath via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/1608.02029))
- Eberl-Paulson in Isabelle via Newman's proof ([AFP](https://www.isa-afp.org/entries/Prime_Number_Theorem.html))

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
