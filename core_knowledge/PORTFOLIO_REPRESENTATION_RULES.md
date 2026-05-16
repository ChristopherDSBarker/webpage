# Portfolio Representation Rules

These rules define what counts as real portfolio representation.

## Strict Representation Rule

Do not infer representation.

A project from the canonical source/archive layer counts as represented only if
the webpage contains at least one explicit artifact:

- homepage featured reel card
- projects page featured reel card
- supporting reel card
- dedicated `featured/*.html` page
- dedicated `supporting/*.html` page
- `portfolio-project-directory.csv` row
- `thumbnail-map.json` entry
- resume page/link
- intentional archive/internal classification

Related language, nearby concepts, visual similarity, or another project with
overlapping themes do not count.

## Parity Workflow

For strict parity work:

1. Enumerate folders in `featured_projects`.
2. Enumerate folders and source items in `supporting_projects`.
3. Enumerate actual webpage artifacts.
4. Compare source IDs to webpage IDs directly.
5. Classify every item as present, missing, partial, stale, or intentionally
   archive/internal.

Do not use semantic representation as a substitute for actual representation.

## Page Evidence Rule

Each project page should expose or classify the meaningful source package
assets:

- PDFs
- posters
- screenshots
- presentations
- logos
- demos
- notebooks
- HTML exports
- code assets where appropriate

If an asset is not exposed, decide whether it is:

- not meaningful for presentation
- source/archive/internal
- too large or unsafe for deployment
- awaiting a safe derivative

## Directory And Thumbnail Rule

Every reel card should have a corresponding `thumbnail-map.json` entry.

Every important source project should have a `portfolio-project-directory.csv`
row unless it is intentionally archive/internal.

`thumbnail-map.json` records current visual routing. It should not claim an
asset exists before the deployable file is present.

## Claim Discipline

Use conservative wording.

Do not invent:

- clients
- tools
- technical stack
- runtime status
- solo ownership
- project purpose
- measurable outcomes
- deployment availability

Collaborative work needs explicit contribution framing.

Use labels such as:

- `Solo / Full implementation`
- `Lead developer`
- `Primary implementation`
- `Research implementation`
- `Collaborative contributor`
- `Archive/reference`
