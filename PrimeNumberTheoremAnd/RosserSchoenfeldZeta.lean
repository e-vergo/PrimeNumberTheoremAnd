import Dress
import PrimeNumberTheoremAnd.ZetaDefinitions


namespace RS

@[blueprint
  "RS_theorem_19"
  (title := "Rosser--Schoenfeld Theorem 19")
  (statement := /-- One has a Riemann von Mangoldt estimate with parameters 0.137, 0.443, and 1.588. -/)
  (above := /--
  \section{The zeta function bounds of Rosser and Schoenfeld}

  In this section we formalize the zeta function bounds of Rosser and Schoenfeld.
  -/)
]
theorem theorem_19 : riemannZeta.Riemann_vonMangoldt_bound 0.137 0.443 1.588 := by sorry

end RS
