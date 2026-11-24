---
name: ME315 · Credenciamento docente
description: A typeset LaTeX article, in color, that solves the accreditation exercise in front of the reader.
colors:
  navy: "#132a4f"
  navy-raised: "#1d3a66"
  navy-ink: "#e9eef6"
  navy-mute: "#a9b8cf"
  theorem-blue: "#1f5bc4"
  theorem-blue-light: "#6f9be3"
  theorem-blue-deep: "#163f8a"
  blue-tint: "#e8f0fc"
  selected-row: "#edf3fc"
  verdict-green: "#17713a"
  verdict-green-bg: "#e9f6ee"
  verdict-red: "#b3261e"
  verdict-red-bg: "#fcecea"
  caution-amber-ink: "#7a4d00"
  caution-amber-bg: "#fff5dc"
  caution-amber-rule: "#d9a43a"
  desk: "#cdd5e0"
  sheet: "#ffffff"
  ink: "#111418"
  ink-secondary: "#2f3540"
  muted: "#535a66"
  hairline: "#c9d0da"
  hairline-faint: "#e6eaf0"
  row-stripe: "#f7f9fc"
typography:
  display:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "34px"
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "28px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.005em"
  title:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.5
  equation:
    fontFamily: "STIX Two Text, Cambria Math, serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.6
    fontFeature: "\"tnum\", \"lnum\""
  proposition:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "\"lnum\""
  table:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.4
  caption:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "15.5px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "STIX Two Text, Cambria, Times New Roman, serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.06em"
    fontFeature: "\"c2sc\", \"smcp\""
  mono:
    fontFamily: "Latin Modern Mono, Courier New, monospace"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  none: "0px"
spacing:
  xs: "8px"
  sm: "14px"
  md: "22px"
  lg: "28px"
  xl: "56px"
  sheet-x: "80px"
components:
  button-primary:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.sheet}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "3px 14px 5px"
    height: "34px"
  button-primary-hover:
    backgroundColor: "{colors.navy-raised}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.navy}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "3px 14px 5px"
    height: "34px"
  button-secondary-hover:
    backgroundColor: "{colors.blue-tint}"
  button-secondary-pressed:
    backgroundColor: "{colors.blue-tint}"
    textColor: "{colors.theorem-blue-deep}"
  field-input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: "2px 0 0"
    height: "34px"
  running-head:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.navy-ink}"
    height: "56px"
  tbox-header:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.sheet}"
    padding: "6px 16px 7px"
  tbox-header-ok:
    backgroundColor: "{colors.verdict-green}"
    textColor: "{colors.sheet}"
  tbox-header-no:
    backgroundColor: "{colors.verdict-red}"
    textColor: "{colors.sheet}"
  callout-attention:
    backgroundColor: "{colors.caution-amber-bg}"
    textColor: "{colors.caution-amber-ink}"
    padding: "7px 12px 8px"
  figure-segment:
    backgroundColor: "{colors.theorem-blue}"
    textColor: "{colors.sheet}"
    height: "26px"
  figure-segment-alt:
    backgroundColor: "{colors.navy-raised}"
    textColor: "{colors.sheet}"
---

# Design System: ME315 · Credenciamento docente

## Overview

**Creative North Star: "The Worked Solution, Printed in Color"**

The interface is a typeset paper, a LaTeX article that answers the exercise in front of the reader. It does not look like an admin dashboard. Inputs are stated as *Hipóteses*, the verdict is *Proposição 1* in a theorem box, the sum is a numbered equation centered with its number at the right margin, the evidence is a booktabs table with *Figura* and *Tabela* captions, and the per-row calculation is a *Demonstração* that ends in ∎. Sections are numbered (§1, §2, 1.1, 1.2), appendices hold the production list and the SQL, and cross-references read like `\ref` links.

Version one was near-monochrome: ink on white, with blue only for links. The user found it hard to read ("falta uma cor pra contraste... tudo branco"), so the shipped world is the article with color. The colors come from a beamer/tcolorbox palette: a navy running head and navy title-page ground, a cool blue-gray desk under one white sheet, one strong theorem blue that carries numbering, data and references, a green or red title bar on the verdict box, and amber for cautions. Each color has a job. None of it is decoration.

The page is dense like a paper and calm like one. Everything sits on one centered sheet. There are no cards, tiles, sidebars or rounded widgets. Hierarchy comes from typography (numbered serif heads, italics for statements and variables, small caps for controls) and from booktabs rules, not from boxes.

**Key Characteristics:**
- One white sheet (max 1120px) on a cool blue-gray desk, under a sticky navy running head.
- STIX Two Text everywhere. Italic for math variables and statements, small caps for controls and field labels, Latin Modern Mono only for SQL and ISSN.
- Theorem blue marks structure and data: section numbers, figure segments, percentile bars, cross-references, selected-row labels.
- Verdict color appears only in the Proposição box, its sentence and the equation total.
- Square corners everywhere. Rules, not boxes.
- Text is left-aligned, never justified.

## Colors

A cool, ink-on-paper palette framed in navy, with one strong blue for structure and data and three semantic colors that each own one job.

### Primary
- **Running-Head Navy** (navy): the frame of the world. Sticky running head, title-page ground behind the login sheet, the filled primary button, section and subsection head text, the `\fbox` button outline and label, the heavy rule under each section title, the booktabs head rules and head text, the plain tbox frame and title bar, appendix summaries.
- **Raised Navy** (navy-raised): hover on the primary button, and the alternating (even) segment in Figura 1.
- **Navy Ink / Navy Mute** (navy-ink, navy-mute): text on navy. Navy-ink is for the running-head actions, navy-mute for inactive tabs and the small right-hand note in a tbox title bar.

### Secondary
- **Theorem Blue** (theorem-blue): structure and data. Section and subsection numbers, odd segments in Figura 1, the percentile bar fill in tables, cross-reference links ("(1)", "Figura 1", "Definição 1"), the bold pᵢ label on selected rows, the focus ring, the caret, the input focus underline.
- **Light Theorem Blue** (theorem-blue-light): only the 3px underline of the active running-head tab, where full theorem blue would disappear against navy.
- **Deep Theorem Blue** (theorem-blue-deep): label and text of a pressed toggle button.
- **Blue Tint / Selected Row** (blue-tint, selected-row): the button hover wash, the pressed-toggle ground and the equation-total flash use blue-tint. Rows that make up the sum S, and their demonstration rows, use selected-row.

### Tertiary
- **Verdict Green** (verdict-green): title bar and frame of the tbox when the docente meets Art. X, the word "atinge", the equation total when it passes.
- **Verdict Red** (verdict-red): title bar and frame when the docente does not meet it, the word "não atinge", a failing total, the 1,25 threshold line and its label in Figura 1, error text (login, "Fora do SJR" states).
- **Caution Amber** (caution-amber-ink, caution-amber-bg, caution-amber-rule): only the *Atenção.* callout (fictitious base, missing SJR years). Amber ink on a pale amber ground, framed by a 1px amber rule.

### Neutral
- **Reader Desk** (desk): the page background around the sheet.
- **Sheet White** (sheet): the paper. Also the gaps between segments in Figura 1.
- **Ink** (ink): body text, booktabs closing rule, SQL block rules.
- **Secondary Ink** (ink-secondary): notes, captions, field labels, journal names, demonstrations, the equation number.
- **Muted** (muted): file lists, scale ticks, unselected row labels, appendix sub-notes.
- **Hairline / Faint Hairline** (hairline, hairline-faint): appendix dividers, the rule between the proposition and its equation, the empty part of the Figura 1 track and of percentile bars.
- **Row Stripe** (row-stripe): background of even table rows.

### Named Rules
**The Every-Color-Has-a-Job Rule.** Navy frames, theorem blue numbers and measures, green and red judge, amber warns. A color that would be used outside its job is not used.

**The Verdict-Lives-in-the-Proposition Rule.** Green and red appear in the Proposição box, its sentence and the equation total. Red also marks the 1,25 threshold and error states. They are never used for decoration, section color or buttons.

**The Rescued-Contrast Rule.** Color is here because monochrome was hard to read. Do not drift back to all-ink-on-white chrome. The running head, section heads and table heads stay navy, and section numbers stay blue.

## Typography

**Display Font:** STIX Two Text (with Cambria, Times New Roman)
**Body Font:** STIX Two Text (with Cambria, Times New Roman), self-hosted subsets for Latin, Latin-ext, Greek and math operators
**Label/Mono Font:** Latin Modern Mono (with Courier New), the LaTeX `\texttt`

**Character:** One scientific serif does everything, the way a paper set in a single family does. Roles come from style rather than from a second family: italic for statements and variables, small caps for controls, bold run-in heads for Observação / Definição / Tabela / Figura.

### Hierarchy
- **Display** (600, 34px, 1.18, centered, balanced, max 28ch): only the title-page heading on the login sheet, in navy. 27px on mobile.
- **Headline** (600, 28px, 1.2): numbered section heads ("1 Apuração do docente"). Navy text, blue number, 2px navy rule below. 23px on mobile.
- **Title** (600, 20px): numbered subsection heads ("1.1 Hipóteses"). Navy text, blue number. 18.5px on mobile.
- **Equation** (400, 24px, 1.6, tabular lining numerals): display equations, centered, with the number (1)/(2) at the right margin in 18px secondary ink. Definition equations are 21px. 19px and left-aligned on mobile.
- **Proposition** (400, 19px, 1.5, italic): the theorem statement. The verdict word is bold italic in verdict color.
- **Body** (400, 17px, 1.5, lining numerals): running prose, max 72ch (notes max 80ch). 16.5px on mobile.
- **Table** (400, 16px, 1.4): booktabs cells. Head 600 navy. Numeric columns right-aligned with tabular numerals. The journal line is italic 15px.
- **Caption** (400, 15.5px, 1.45): notes, figcaptions, table captions, demonstrations, callouts. Bold run-in label ("Figura 1.", "Tabela 1.") in ink.
- **Label** (all-small-caps, 16-17px, +0.06em): field labels, buttons, running-head brand (18px, +0.07em) and actions.
- **Mono** (400, 15px in SQL blocks; .92em inline): SQL listings, ISSN codes. Nothing else.

### Named Rules
**The Math-Is-Italic Rule.** Every variable (p, S, N, j, c, Aⱼ) is set in italic serif with real subscripts, in prose, table heads and equations alike. Numbers are upright lining figures with a decimal comma (pt-BR).

**The Small-Caps-Means-Control Rule.** All-small-caps marks things you act on or fill in: buttons, field labels, the running-head brand and actions. Headings and prose never use it.

**The Ragged-Right Rule.** Text is left-aligned. Justification was tried and removed because Chrome has no pt-BR hyphenation and it opened rivers.

## Layout

A single centered sheet, max 1120px, with padding of 64px top, 80px sides and 72px bottom, and margins of 18-28px on the desk. On the app view the sheet starts 18px below a sticky 56px navy running head, whose inner row matches the sheet's 1120px width. The login is a narrower 820px title-page sheet (84px / 96px padding) centered on a full-height navy ground. Its content column is 56ch.

Inside the sheet, content follows a paper's order: data-source line with its action at the right, then numbered sections. Hypotheses use a two-column grid (1.15fr / 1fr, gaps 22px / 56px). §2's hypotheses are one three-column row (2.2fr / .8fr / 1.6fr). Tables and display equations span the full measure, and prose is capped at 72-80ch. The spacing rhythm is 8 / 14 / 22 / 28 / 56px: 14px cell and control gaps, 22px field gaps, 28-32px before a subsection, 56px before the appendix block.

Responsive: at 980px and below, sheet padding drops to 48px / 40px. At 760px and below the sheet goes edge to edge with no shadow (32px / 18px padding). The running head becomes two rows (brand and actions, then full-width tabs that drop their long words). Every grid collapses to one column. Display equations wrap at term groups. The two wide tables keep a 760px minimum width inside a horizontal scroller, with demonstration text pinned sticky-left.

## Elevation & Depth

Flat paper on a desk. The only real lift is the sheet itself, with a soft, diffuse shadow. Inside the sheet nothing is elevated: depth inside the page is expressed with rules (booktabs, section rules, tbox frames) and pale tints (row stripes, selected rows). On mobile the sheet loses its shadow entirely.

### Shadow Vocabulary
- **Sheet on desk** (`box-shadow: 0 1px 2px rgba(20,22,26,.08), 0 10px 36px rgba(20,22,26,.07)`): the app sheet.
- **Sheet on navy** (`box-shadow: 0 2px 6px rgba(0,0,0,.25), 0 24px 60px rgba(0,0,0,.3)`): the login title-page sheet, deeper to read against the dark ground.
- **Running-head seam** (`box-shadow: 0 1px 0 rgba(0,0,0,.2)`): a one-pixel seam under the sticky head.
- **Toast** (`box-shadow: 0 10px 30px rgba(0,0,0,.2)`): the transient ink toast, the only floating element.

### Named Rules
**The One-Sheet Rule.** Only the sheet (and transient toast/dialog) casts a shadow. Nothing inside the sheet is lifted. Use a rule or a tint instead.

## Shapes

Square everywhere (0px radius): buttons, inputs, dialog, tbox, callouts, figure track. Forms are drawn with rules the way TeX draws them. There is a heavy 2px rule at the top and bottom of every table and a 1px rule under the head. A 2px navy rule sits under section heads and above the appendix block. Inputs are a single baseline. Buttons are a 1px `\fbox`. The Figura 1 track is a 26px navy-framed bar divided by 2px white seams. The one curve is the 7px chevron on appendix summaries, which rotates open.

## Components

### Buttons
Framed small caps, like `\fbox{\textsc{...}}`.
- **Shape:** square (0px), 1px border, min-height 34px, padding 3px 14px 5px, all-small-caps 17px weight 500, +0.06em.
- **Primary (Entrar):** filled navy with white label. Hover raises to navy-raised. Used once per view, for the one committing action.
- **Secondary:** transparent with navy frame and navy label ("Adicionar CSV do Scimago", "Carregar XML do Lattes", "Exportar CSV"). Hover washes blue-tint. File inputs are hidden behind a label styled as this button, with focus shown on the label.
- **Pressed toggle ("Mostrar / Ocultar demonstração"):** blue-tint ground, theorem-blue frame, deep-blue label.
- **Link action:** borderless small caps in theorem blue, underline on hover. In the running head ("Imprimir / PDF", "Sair") it is navy-ink.
- **Focus:** 2px theorem-blue outline, offset 2px (white outline on navy). Transitions take 150ms on background and color.

### Inputs / Fields
Fill-in blanks on a baseline.
- **Style:** no box. A 1px gray bottom rule (#8c8c8c), transparent ground, 34px tall, tabular numerals. The label sits above in small caps, secondary ink, 16px. Placeholders are italic gray.
- **Hover / Focus:** the rule darkens to ink on hover. On focus it turns theorem blue and doubles to 2px through an inset shadow, with no outline box.
- **Checkboxes:** 16px native, accent ink, label in body serif with a muted 14.5px aside ("+50%, até 6 anos").

### Navigation (running head)
- Sticky navy bar, 56px. Small-caps white brand at the left, then §-numbered tabs in body serif 17px: inactive navy-mute, hover and active white. The active tab carries a 3px light-theorem-blue underline inset 12px. Link actions sit at the right.
- On mobile it is two rows: brand and actions, then tabs at 44px min height with the long words dropped.
- Print hides the running head and shows a small-caps print header with a 1px rule instead.

### Theorem Box (tcolorbox)
The signature container, used for Proposição 1.
- 1px frame and a title bar in the same color: navy when neutral, verdict green when the docente meets Art. X, verdict red when not. The title bar has a 600-weight title at the left ("Proposição 1") and a 15px tinted note at the right. The body is white, padded 16px 20px 12px.
- The body holds the italic proposition, then the numbered equation (1) under a faint hairline.

### Display Equation
A centered math line with its number flush right in a separate grid column. Equation (1) is re-typeset on every input change. Its bold total flashes blue-tint, then fades over 1.4s (ease-out-expo). It is colored green or red against "≥ 1,250".

### Figura 1 (contribution bar)
A full-width 26px track framed in navy on a faint-hairline ground. Each pᵢ is a segment, alternating theorem blue and raised navy, with white 2px seams and an italic white pᵢ label. Segments animate width over 600ms. A 2px verdict-red vertical rule marks 1,25 with a red label. A muted 0-4 scale sits below, then a figcaption with a bold run-in.

### Booktabs Table
- Head: 600-weight navy text, 2px navy top rule, 1px navy mid rule. Body rows: alternating stripe. Closing rule: 2px. Cell padding 7px 14px 7px 0, first column indented 8px.
- Rows that make up S use the selected-row ground and a bold theorem-blue pᵢ label. Excluded rows drop to regular weight, secondary ink, and get a gray percentile bar.
- Percentile bar: a 4px faint-hairline track under the value, filled theorem blue in proportion to p.
- Demonstration row: indented italic "Demonstração." run-in with the full worked formula, ending in ∎. It shares its parent row's ground.

### Callout (Atenção)
Amber ink on a pale amber ground with a 1px amber rule, 7px 12px 8px padding, caption size, bold run-in "Atenção.". Used only for data warnings (fictitious base, missing years).

### Appendix (details)
A full-width summary row (18px, 600, navy) with a rotating 7px chevron, a muted 15.5px aside, and a hairline below. The block opens with a 2px navy rule. SQL inside is set in Latin Modern Mono between 2px ink rules, with comments in italic gray.

## Do's and Don'ts

### Do:
- **Do** build every new surface as part of the paper: numbered section or subsection, *Hipóteses* inputs, a stated result, a captioned table or figure, an appendix for raw material.
- **Do** keep the navy frame (running head, section heads, table heads) and theorem-blue section numbers. Contrast from color is a confirmed user requirement.
- **Do** set every variable in italic serif with subscripts, and every number with lining figures and a decimal comma. Use tabular numerals in tables and equations.
- **Do** use framed small-caps buttons (1px navy, 0px radius). Reserve the filled navy button for the single committing action of a view.
- **Do** draw inputs as baseline blanks that turn theorem blue on focus.
- **Do** separate with booktabs rules (2px top and bottom, 1px mid) and pale tints, never with nested boxes.
- **Do** put verdict green and red only on the Proposição box, its verdict word, the equation total, the threshold and error states.
- **Do** use the amber *Atenção.* callout for data caveats, so open interpretations and fictitious data are stated, not hidden.
- **Do** left-align all text.

### Don't:
- **Don't** introduce cards, KPI tiles, sidebars of widgets or rounded corners. The world is a paper, not an admin dashboard.
- **Don't** return to near-monochrome ink-on-white chrome. The user rejected it as hard to read.
- **Don't** use verdict green or red for buttons, headings, decoration or anything outside a judgment.
- **Don't** justify text. There is no pt-BR hyphenation in Chrome.
- **Don't** use Latin Modern Mono for anything but SQL and ISSN, and don't add a second display or sans family.
- **Don't** lift anything inside the sheet with a shadow.
