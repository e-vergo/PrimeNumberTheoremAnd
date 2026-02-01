> **Fork Notice**: This is a fork of [AlexKontorovich/PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) with [Side-by-Side Blueprint](https://github.com/e-vergo/Side-By-Side-Blueprint) integration for toolchain testing. The original project is maintained at [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd). All original proof code is preserved unchanged.

# Prime Number Theorem And...

![Lean](https://img.shields.io/badge/Lean-v4.27.0-blue)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-lightblue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Original Blueprint](https://img.shields.io/badge/Original_Blueprint-Website-blue.svg?logo=github&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/blueprint)
[![Original Docs](https://img.shields.io/badge/Original_Docs-Website-blue.svg?logo=readthedocs&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs)

---

## Project Overview

The objective of this project is to formalize in Lean the Prime Number Theorem (with classical error term), as well as related results such as the Prime Number Theorem in Arithmetic Progressions. A stretch goal would be to obtain the Chebotarev density theorem.

We are also hosting the [Integrated Explicit Analytic Number Theory network](https://www.ipam.ucla.edu/news-research/special-projects/integrated-explicit-analytic-number-theory-network/). A personal log describing the latter project may be [found here](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/wiki/Terence-Tao's-personal-log).

### Mathematical Content

The formalization pursues three parallel approaches to PNT:

1. **Wiener-Ikehara Tauberian theorem** - Following Michael Stoll's "Euler Products" project, which has a proof of PNT missing only the Wiener-Ikehara theorem.

2. **Complex analysis approach** - Develops residue calculus on rectangles, the argument principle, and Mellin transforms to derive PNT with an error term stronger than any power of log savings.

3. **Full treatment via Hadamard factorization** - The most general approach: residue calculus, Hadamard factorization theorem, zero-free region for zeta via Hoffstein-Lockhart+Goldfeld-Hoffstein-Liemann, leading to PNT with exp-root-log savings.

### Key Results

- **WeakPNT**: Prime Number Theorem via Wiener-Ikehara
- **MediumPNT**: PNT with improved error term via contour integration
- **WeakPNT_AP**: Prime Number Theorem in Arithmetic Progressions

---

## Side-by-Side Blueprint Integration

This fork serves as the largest integration test for the SBS toolchain and showcases its dependency graph validation capabilities.

### The Tao Incident (January 2026)

This project is where dependency graph validation proved its value. From the [Zulip discussion](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B/topic/Fixing.20a.20sign.20error.20in.20Erdos.20392):

> "When reviewing the blueprint graph I noticed an oddity in the Erdos 392 project: the final theorems (erdos-sol-1, erdos-sol-2) were mysteriously disconnected from the rest of the Erdos 392 lemmas; and the (AI-provided) proofs were suspiciously short. After some inspection I realized the problem: I had asked to prove the (trivial) statements that n! can be factored into **at least** n-n/log n + o(n/log n) factors of size <= n, when in fact the Erdos problem asks to factor into **at most** n-n/log n + o(n/log n) factors..."
>
> "Another cautionary tale not to blindly trust AI auto-formalization, even when it typechecks..."
>
> -- Terence Tao

The disconnected dependency graph made the logical error visible. This incident led directly to automated connectivity validation in the SBS toolchain.

### Scale

| Metric | Value |
|--------|-------|
| Blueprint annotations | 591 `@[blueprint]` attributes |
| Annotated files | 33 Lean source files |
| Total source files | 50 Lean files |

This scale exercises graph layout algorithms, performance optimizations, and validation checks that smaller test projects do not stress.

### Features Demonstrated

| Feature | Description |
|---------|-------------|
| Large-scale dependency graph | 591 nodes with Sugiyama hierarchical layout |
| Connectivity validation | Detects disconnected subgraphs (the Tao check) |
| Module reference support | `\inputleanmodule{PrimeNumberTheoremAnd.Wiener}` organizes chapters by mathematical topic |
| >100 node optimizations | Transitive reduction and visibility graph routing bypassed for performance |
| Multi-chapter organization | 10 chapters spanning three approaches to PNT |

### Integration Approach

All 591 annotations were added non-invasively. Zero changes to the original Lean proof code were required.

---

## Blueprint Organization

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

---

## Building

### Lean Project

```bash
lake exe cache get  # Fetch mathlib cache
lake build
```

### Blueprint Site

```bash
# Build with artifact generation
BLUEPRINT_DRESS=1 lake build

# Generate Lake facets
lake build :blueprint

# Generate dependency graph and manifest
lake exe extract_blueprint graph PrimeNumberTheoremAnd

# Generate site
lake exe runway build runway.json
```

Output is written to `.lake/build/runway/`.

### CI/CD

GitHub Actions workflow uses [dress-blueprint-action](https://github.com/e-vergo/dress-blueprint-action):

```yaml
- uses: e-vergo/dress-blueprint-action@main
```

---

## Toolchain Dependencies

This fork adds [Dress](https://github.com/e-vergo/Dress) as a dependency, which transitively provides:

| Repository | Purpose |
|------------|---------|
| [SubVerso](https://github.com/e-vergo/subverso) | Syntax highlighting with O(1) indexed lookups |
| [LeanArchitect](https://github.com/e-vergo/LeanArchitect) | `@[blueprint]` attribute with 8 metadata + 3 status options |
| [Dress](https://github.com/e-vergo/Dress) | Artifact generation, dependency graph layout, validation |
| [Runway](https://github.com/e-vergo/Runway) | Site generator, dashboard, paper/PDF |

---

## Zulip

The project is coordinated via a [Lean Zulip channel](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B).

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for instructions on how to claim issues, submit PRs, and participate in the project.

### Quick Contributions via Gitpod

To contribute to the original project without local installation, use Gitpod (links to upstream repository):

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/new/#https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/)

Dependencies load automatically, providing a web-based VS Code environment for editing and submitting PRs.

---

## Related Projects

### Original Project
- [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd) - Original PNT formalization
- [AlexKontorovich/PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) - Active development repository

### SBS Toolchain
- [SubVerso](https://github.com/e-vergo/subverso) - Syntax highlighting extraction with O(1) indexed lookups
- [LeanArchitect](https://github.com/e-vergo/LeanArchitect) - `@[blueprint]` attribute for annotations
- [Dress](https://github.com/e-vergo/Dress) - Artifact generation, dependency graph, validation
- [Runway](https://github.com/e-vergo/Runway) - Site generator, dashboard, paper/PDF
- [dress-blueprint-action](https://github.com/e-vergo/dress-blueprint-action) - GitHub Action for CI/CD

### Other SBS Projects
- [SBS-Test](https://github.com/e-vergo/SBS-Test) - Minimal test project (33 nodes, all 6 status colors)
- [General Crystallographic Restriction](https://github.com/e-vergo/General_Crystallographic_Restriction) - Production example with paper generation (57 nodes)

---

## Prior Art

The Prime Number Theorem has been formalized before:
- Avigad et al. in Isabelle via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/cs/0509025))
- Harrison in HOL Light via Newman's proof ([paper](https://www.cl.cam.ac.uk/~jrh13/papers/mikefest.html))
- Carneiro in Metamath via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/1608.02029))
- Eberl-Paulson in Isabelle via Newman's proof ([AFP](https://www.isa-afp.org/entries/Prime_Number_Theorem.html))

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
