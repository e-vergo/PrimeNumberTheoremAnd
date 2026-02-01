> **This is a fork of the original [PNT+](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) project with [Side-by-Side Blueprint](https://github.com/e-vergo/Side-By-Side-Blueprint) integration.** The original project is maintained by Alex Kontorovich and Terence Tao at [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd). All original Lean proof code is preserved unchanged; only `@[blueprint]` annotations were added.

# Prime Number Theorem And...

![Lean](https://img.shields.io/badge/Lean-v4.27.0-blue)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-lightblue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Original Blueprint](https://img.shields.io/badge/Original_Blueprint-Website-blue.svg?logo=github&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/blueprint)
[![Original Docs](https://img.shields.io/badge/Original_Docs-Website-blue.svg?logo=readthedocs&logoColor=white)](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs)

A collaborative formalization of the Prime Number Theorem and related results in Lean 4, organized by Alex Kontorovich and Terence Tao with contributions from the [Lean Zulip community](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B).

## Project Overview

The Prime Number Theorem (PNT) states that the number of primes up to x is asymptotically x/ln(x). This project formalizes PNT with classical error terms, along with related results in analytic number theory.

**Three parallel approaches:**

1. **Wiener-Ikehara Tauberian theorem** - Following Michael Stoll's "Euler Products" project
2. **Complex analysis approach** - Residue calculus, argument principle, and Mellin transforms
3. **Hadamard factorization** - The most general approach with exp-root-log savings

**Key results:**
- `WeakPNT`: Prime Number Theorem via Wiener-Ikehara
- `MediumPNT`: PNT with improved error term via contour integration
- `WeakPNT_AP`: Prime Number Theorem in Arithmetic Progressions

The project also hosts the [Integrated Explicit Analytic Number Theory network](https://www.ipam.ucla.edu/news-research/special-projects/integrated-explicit-analytic-number-theory-network/). A personal log describing the project may be [found here](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/wiki/Terence-Tao's-personal-log).

## Building

### Lean Project

```bash
lake exe cache get  # Fetch mathlib cache (~5GB)
lake build
```

### Blueprint Site (SBS Integration)

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

## Side-by-Side Blueprint Integration

This fork serves as the **large-scale integration example** for the [Side-by-Side Blueprint](https://github.com/e-vergo/Side-By-Side-Blueprint) toolchain, demonstrating capabilities at production scale.

### Scale

| Metric | Value |
|--------|-------|
| Blueprint annotations | 591 `@[blueprint]` attributes |
| Annotated files | 33 Lean source files |
| Total source files | 50 Lean files |
| Expected build time | ~20 minutes |
| Graph layout time | ~15 seconds |

### What This Fork Demonstrates

1. **Performance at scale**: Exercises graph layout algorithms and optimizations that smaller test projects cannot stress
2. **Connectivity validation**: Where the "Tao incident" proved the value of dependency graph analysis
3. **Module reference support**: Uses `\inputleanmodule{}` to organize 10 chapters by mathematical topic
4. **Non-invasive integration**: All 591 annotations added without modifying original proof code

### The Tao Incident (January 2026)

This project is where dependency graph validation proved its value. From the [Zulip discussion](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B/topic/Fixing.20a.20sign.20error.20in.20Erdos.20392):

> "When reviewing the blueprint graph I noticed an oddity in the Erdos 392 project: the final theorems (erdos-sol-1, erdos-sol-2) were mysteriously disconnected from the rest of the Erdos 392 lemmas; and the (AI-provided) proofs were suspiciously short. After some inspection I realized the problem: I had asked to prove the (trivial) statements that n! can be factored into **at least** n-n/log n + o(n/log n) factors of size <= n, when in fact the Erdos problem asks to factor into **at most** n-n/log n + o(n/log n) factors..."
>
> "Another cautionary tale not to blindly trust AI auto-formalization, even when it typechecks..."
>
> -- Terence Tao

The disconnected dependency graph made the logical error visible. This incident led directly to automated connectivity validation in the SBS toolchain.

### Large Graph Optimizations

At 591 nodes, this project triggers >100 node optimizations in the layout algorithm:

| Optimization | Normal | >100 nodes | Rationale |
|--------------|--------|------------|-----------|
| Barycenter iterations | Unlimited | Max 2 | O(n) per iteration |
| Transpose heuristic | Yes | Skipped | O(n^2) adjacent swaps |
| Visibility graph routing | Yes | Skipped | O(n^2) graph construction |
| Transitive reduction | O(n^3) | Skipped | Multi-hour build times |

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

## Attribution

### Original PNT+ Project

**Project leads:**
- **Alex Kontorovich** ([ORCID](https://orcid.org/0000-0001-7626-8319))
- **Terence Tao** ([ORCID](https://orcid.org/0000-0002-0140-7641))

With contributions from the [Lean Zulip community](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B).

**Original repositories:**
- [leanprover-community/PrimeNumberTheoremAnd](https://github.com/leanprover-community/PrimeNumberTheoremAnd) - Lean community home
- [AlexKontorovich/PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) - Active development

### Prior Art

The Prime Number Theorem has been formalized before:
- Avigad et al. in Isabelle via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/cs/0509025))
- Harrison in HOL Light via Newman's proof ([paper](https://www.cl.cam.ac.uk/~jrh13/papers/mikefest.html))
- Carneiro in Metamath via Selberg/Erdos method ([arXiv](https://arxiv.org/abs/1608.02029))
- Eberl-Paulson in Isabelle via Newman's proof ([AFP](https://www.isa-afp.org/entries/Prime_Number_Theorem.html))

### SBS Toolchain

The Side-by-Side Blueprint integration uses:
- [SubVerso](https://github.com/e-vergo/subverso) - Syntax highlighting with O(1) indexed lookups
- [LeanArchitect](https://github.com/e-vergo/LeanArchitect) - `@[blueprint]` attribute
- [Dress](https://github.com/e-vergo/Dress) - Artifact generation, dependency graph, validation
- [Runway](https://github.com/e-vergo/Runway) - Site generator, dashboard
- [dress-blueprint-action](https://github.com/e-vergo/dress-blueprint-action) - GitHub Action for CI/CD

## Contributing

Contributions to the original project are welcome. See the [Contributing Guide](CONTRIBUTING.md) for instructions on claiming issues, submitting PRs, and participating.

### Quick Contributions via Gitpod

To contribute without local installation, use Gitpod:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/new/#https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/)

## Related Projects

| Project | Scale | Purpose |
|---------|-------|---------|
| [SBS-Test](../SBS-Test/) | 33 nodes | Minimal test project (all 6 status colors) |
| [General Crystallographic Restriction](../General_Crystallographic_Restriction/) | 57 nodes | Production example with paper generation |

## License

Apache 2.0 - see [LICENSE](LICENSE).
