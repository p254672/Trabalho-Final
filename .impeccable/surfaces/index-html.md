---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Surface brief: index.html (portal inteiro)

Scope: login + two working sections (Apuração do docente; Revistas por categoria) + appendices. Mode: Operate. Audience: ME315 professor testing alone, loading files and checking numbers. Must not hide the calculation. Delivery via Shiny wrapper and GitHub Pages.

## Direction contract

THESIS: The portal is a typeset paper that solves the exercise in front of the reader. Hypotheses, a stated proposition, the sum written as a numbered equation, a booktabs table, a proof on demand. It refuses the admin dashboard: no cards, no KPI tiles, no sidebar of widgets.

OWN-WORLD: White sheet on a cool reader-gray desk. Ink #141414, hyperref blue #1f4e8c for every interactive reference, verdict green #1d6b35 and red #a3261d only inside the proposition. STIX Two Text everywhere (self-hosted), italic for math variables, small caps for controls, typewriter mono only for SQL and ISSN. Booktabs rules (heavy top and bottom, light middle). Inputs are fill-in blanks on a baseline. Buttons are framed small caps (\fbox).

STORY: The professor loads data as hypotheses, reads Proposição 1 (verdict), sees equation (1) add each pᵢ to the total against 1,25, checks Tabela 1, opens the demonstration per row, then switches to §2 to rank journals in a category by mean percentile over 4 SJR years.

FIRST VIEWPORT: Running head (title left, §1 / §2 tabs, Imprimir, Sair). Sheet: section title, Hypotheses form in two columns, then Proposição 1 in italic with the verdict, equation (1) centered full width with its number at right margin, Figura 1 bar below.

FORM: Resolução comentada (LaTeX article with worked solution), pick card, my rank 1; seed key 4fd84494. Signature interaction: "Mostrar demonstração" reveals per-row p = 1 − (posição − 1)/N with real numbers, ending in ∎; equation (1) terms re-typeset on every input change.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
