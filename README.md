> **Fork Notice**: This is a fork of the original [PNT+ project](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) with [Side-by-Side Blueprint](https://github.com/e-vergo/Side-By-Side-Blueprint) integration. The original project is maintained at [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd). All original proof code is preserved unchanged.

# Prime Number Theorem And...

![Lean](https://img.shields.io/badge/Lean-v4.27.0-blue)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-lightblue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Original Blueprint](https://img.shields.io/badge/Original_Blueprint-Website-blue.svg?logo=github&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/blueprint)
[![Original Docs](https://img.shields.io/badge/Original_Docs-Website-blue.svg?logo=readthedocs&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs)

A formalization of the Prime Number Theorem and related results in Lean 4. This fork serves as the largest integration of the [Side-by-Side Blueprint](https://github.com/e-vergo/Side-By-Side-Blueprint) toolchain, demonstrating capabilities at scale with 591 `@[blueprint]` annotations across 33 Lean source files.

---

## Project Overview

The objective of this formalization is to prove the Prime Number Theorem with classical error term, along with related results such as the Prime Number Theorem in Arithmetic Progressions. A stretch goal is the Chebotarev density theorem.

The project pursues three parallel approaches to PNT:

1. **Wiener-Ikehara Tauberian theorem** - Following Michael Stoll's "Euler Products" project
2. **Complex analysis approach** - Residue calculus, argument principle, and Mellin transforms
3. **Hadamard factorization** - The most general approach with exp-root-log savings

---

## Side-by-Side Blueprint Integration

This fork demonstrates SBS toolchain capabilities at scale:

1. **Large-scale integration test**: Exercises graph layout algorithms, performance optimizations, and validation checks that smaller test projects cannot stress
2. **Connectivity validation showcase**: Where the "Tao incident" proved the value of dependency graph analysis
3. **Module reference demonstration**: Uses `\inputleanmodule{}` to organize 10 chapters by mathematical topic

**All 591 annotations were added non-invasively. Zero changes to the original Lean proof code were required.**

---

## The Tao Incident (January 2026)

This project is where dependency graph validation proved its value. From the [Zulip discussion](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B/topic/Fixing.20a.20sign.20error.20in.20Erdos.20392):

> "When reviewing the blueprint graph I noticed an oddity in the Erdos 392 project: the final theorems (erdos-sol-1, erdos-sol-2) were mysteriously disconnected from the rest of the Erdos 392 lemmas; and the (AI-provided) proofs were suspiciously short. After some inspection I realized the problem: I had asked to prove the (trivial) statements that n! can be factored into **at least** n-n/log n + o(n/log n) factors of size <= n, when in fact the Erdos problem asks to factor into **at most** n-n/log n + o(n/log n) factors..."
>
> "Another cautionary tale not to blindly trust AI auto-formalization, even when it typechecks..."
>
> -- Terence Tao

The disconnected dependency graph made the logical error visible. This incident led directly to automated connectivity validation in the SBS toolchain.

---

## Scale

| Metric | Value |
|--------|-------|
| Blueprint annotations | 591 `@[blueprint]` attributes |
| Annotated files | 33 Lean source files |
| Total source files | 50 Lean files |
| Expected build time | ~20 minutes |
| Graph layout time | ~15 seconds |

This scale triggers >100 node optimizations in the graph layout algorithm:
- Max 2 barycenter iterations (vs. unlimited)
- Transpose heuristic skipped
- Visibility graph routing bypassed (simple beziers used)
- O(n^3) transitive reduction skipped

---

## Key Results

- **WeakPNT**: Prime Number Theorem via Wiener-Ikehara
- **MediumPNT**: PNT with improved error term via contour integration
- **WeakPNT_AP**: Prime Number Theorem in Arithmetic Progressions

The project also hosts the [Integrated Explicit Analytic Number Theory network](https://www.ipam.ucla.edu/news-research/special-projects/integrated-explicit-analytic-number-theory-network/). A personal log describing the latter project may be [found here](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/wiki/Terence-Tao's-personal-log).

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

## Attribution

### Original PNT+ Project

This formalization was created and is maintained by:
- **Alex Kontorovich** (Project lead)
- **Terence Tao** and many contributors from the [Lean Zulip community](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B)

Original repositories:
- [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd) - Lean community home
- [AlexKontorovich/PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) - Active development

### Side-by-Side Blueprint Toolchain

The SBS integration uses:
- [SubVerso](https://github.com/e-vergo/subverso) - Syntax highlighting with O(1) indexed lookups (fork of leanprover/subverso by David Thrane Christiansen)
- [LeanArchitect](https://github.com/e-vergo/LeanArchitect) - `@[blueprint]` attribute (fork of hanwenzhu/LeanArchitect)
- [Dress](https://github.com/e-vergo/Dress) - Artifact generation, dependency graph, validation
- [Runway](https://github.com/e-vergo/Runway) - Site generator, dashboard
- [dress-blueprint-action](https://github.com/e-vergo/dress-blueprint-action) - GitHub Action for CI/CD

### Prior Art

The Prime Number Theorem has been formalized before:
- Avigad et al. in Isabelle via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/cs/0509025))
- Harrison in HOL Light via Newman's proof ([paper](https://www.cl.cam.ac.uk/~jrh13/papers/mikefest.html))
- Carneiro in Metamath via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/1608.02029))
- Eberl-Paulson in Isabelle via Newman's proof ([AFP](https://www.isa-afp.org/entries/Prime_Number_Theorem.html))

---

## Contributing

Contributions to the original project are welcome. See the [Contributing Guide](CONTRIBUTING.md) for instructions on how to claim issues, submit PRs, and participate in the project.

### Quick Contributions via Gitpod

To contribute to the original project without local installation, use Gitpod:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/new/#https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/)

---

## Tooling

For build commands, screenshot capture, compliance validation, archive management, and custom rubrics, see the [Archive & Tooling Hub](../archive/README.md).

## Related Projects

### Other SBS Examples

| Project | Scale | Purpose |
|---------|-------|---------|
| [SBS-Test](https://github.com/e-vergo/SBS-Test) | 33 nodes | Minimal test project (all 6 status colors) |
| [General Crystallographic Restriction](https://github.com/e-vergo/General_Crystallographic_Restriction) | 57 nodes | Production example with paper generation |

---

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
