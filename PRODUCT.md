# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Front stays static HTML/CSS/JS with SQLite in the browser (sql.js). Delivery for the course: an R Shiny wrapper (`app.R`) that serves the same front, runnable with `shiny::runApp()` and publishable to shinyapps.io. The static site must keep working on GitHub Pages too.

## Users

Primary audience for this delivery: the professor of the course ME315 (PPGE), who evaluates the "Case ME315" submission. The professor checks that the accreditation rules are implemented correctly, that the calculation is transparent and auditable, and how the result is presented.

The tool is framed as if used by someone reviewing a faculty member's accreditation request: load the SJR base, load the faculty member's Lattes XML, set the request date and exceptions, read the verdict.

## Product Purpose

Portal for faculty accreditation (credenciamento docente). It selects a faculty member's best articles in the evaluation window and scores each one by the journal's percentile in the Scimago Journal Rank (SJR), then says whether the faculty member meets the minimum.

Success: the evaluator reaches a clear, defensible verdict and can trace every number back to the rule and the data that produced it.

## Positioning

The whole calculation runs in the browser with SQLite (sql.js) over public SJR CSVs. The SQL that produces the result is visible in the page. Faculty data (Lattes XML) never leaves the browser.

## Operating Context

- Static site, published on GitHub Pages; run locally with `py -m http.server` (opening via `file://` blocks the CSV fetch).
- Inputs: Scimago CSVs per subject area and year (listed in `data/manifest.json`), Lattes XML, manual article entry.
- Outputs: on-screen verdict and ranking, CSV export, print / PDF.
- Client-side login gate (PBKDF2 hashes in `index.html`), meant only to block casual use.

## Capabilities and Constraints

- Two jobs: (1) evaluate a faculty member's accreditation (best articles, verdict); (2) rank the best journals to publish in, per SJR category, over the last 4 years.
- Journal ranking: "area" = SJR category (e.g. "Statistics and Probability"). Score = mean of the journal's percentile in that category across the SJR years in the last 4 years (same 0–1 scale as p_i). Show top 20 by default, adjustable, with search by name / ISSN. Years with no data for a journal are reported, not hidden.
- Art. X: p_i = highest journal percentile across all SJR categories (and loaded years in the window); only p_i ≥ 0.25 counts; sum of the up to 4 best must reach 1.25.
- Percentile per category and year: `1 - (rank - 1) / N`, rank by descending SJR.
- Art. Y: base window 48 months; parenthood 72; PcD / dependent 60; medical leave adds its duration.
- Open interpretations to validate with the professor: percentile formula and which SJR year to use; whether exceptions accumulate (currently parenthood and PcD do not, medical does); filter by calendar year (Lattes has no month).
- Single static `index.html`, plain HTML/CSS/JS, no build step. `vendor/` holds sql.js. Must keep working offline from the repo folder through a local server.
- Language: Portuguese (pt-BR).

## Brand Commitments

No institutional identity required. Only the names "PPGE" and "ME315" as already used.

## Evidence on Hand

- `data/sjr-2024-EXEMPLO-FICTICIO.csv`: fictitious SJR values for testing only. The UI must keep flagging it as fictitious.
- No real faculty data in the repository. Never commit Lattes XML.

## Product Principles

1. Every number is traceable to a rule and to data.
2. Open interpretations are stated, not hidden.
3. Faculty data stays in the browser.
4. The verdict is the first thing the evaluator reads; the evidence is one step below it.
