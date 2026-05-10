# Portfolio Inventory

Source of truth: `/Users/songsidiya/Documents/portfolio`

Purpose: internal maintenance document for project visibility, presentation status, and future refinement work.

Top-level source counts:

- `featured_projects`: 8 entries
- `supporting projects`: 26 entries
- `resume_assets`: 1 entry

## Visibility Constraint

Every top-level project must appear in at least one visible place:

- Homepage Featured Reel
- Projects Featured Reel
- Supporting Reel
- Projects Directory
- dedicated project page
- Resume page

## Repository Synchronization Rule

Curated project folders are the source-of-truth for page content. If a project folder contains major assets, the website must expose, summarize, or intentionally classify them.

Major assets include:

- PDFs
- screenshots
- presentations
- logos/branding files
- demos
- exports
- source notebooks or reports

Project pages should not omit major curated assets or compress multi-document project packages into one generic summary.

## Repository Coverage Rule

Every curated repository item must satisfy at least one of these:

- visible in the Featured Reel
- visible in the Supporting Reel
- visible in the Projects Directory
- exposed on a dedicated project page
- linked from the Resume page
- intentionally classified as archival/internal

No curated project folder should become unreachable from the portfolio navigation system.

## Repository Verification Rule

Repository existence and public linkability are separate states.

Valid repository verification sources include:

- public GitHub URL
- GitHub API visibility
- browser-visible repository listing
- user-confirmed ownership/contribution
- local repository synchronization record

Private or collaborative verified repositories may be represented with clear role language, but public GitHub buttons should only be added after URL accessibility and intended visibility are confirmed.

## Project Package Standard

When a curated project folder contains multiple meaningful assets, the website should present it as a package. Major assets should be classified as:

- summary
- presentation
- consultation
- branding
- screenshot
- demo
- source
- export

Before generating or editing a project page, enumerate the folder contents and map each major file to a presentation role.

Related tracking files:

- `portfolio-content-map.md`
- `portfolio-thumbnail-audit.md`
- `portfolio-project-directory.csv`
- `thumbnail-map.json`
- `github-repo-sync.md`

## Status Definitions

### Complete

Presentation-ready project with a visible page or card, media asset, and stable link path.

### In Progress

Active project or presentation still needing screenshots, demos, repo links, or stronger process context.

### Experimental

Prototype, research, or exploratory work retained because it shows technical breadth.

### Archived

Older coursework or secondary material preserved for completeness and discoverability.

## Presentation Quality Levels

- `Flagship`: strongest work, suitable for featured placement and deeper storytelling.
- `Supporting`: useful breadth material, visible but intentionally secondary.
- `Archival`: preserved for transparency; should not compete visually with flagship work.

## Featured Projects

- [x] Opioid Prescribing Risk Analysis
  - Website: `featured/opioid-prescribing-risk-analysis.html`
  - Status: complete
  - Presentation: flagship, needs stronger screenshots/charts over time
- [x] Grocery Retail Consumer Analytics
  - Website: `featured/grocery-retail-consumer-analytics.html`
  - Status: complete
  - Presentation: flagship, needs dashboard/process screenshots over time
- [x] Minesweeper Game
  - Website: `featured/minesweeper-game.html`
  - Status: in progress
  - Presentation: supporting/featured bridge, needs deployed demo and gameplay screenshots
- [x] Battleship Game
  - Website: `featured/battleship-game.html`
  - Status: archived
  - Presentation: supporting, needs gameplay screenshots
- [x] HTML Resume Portfolio
  - Website: `featured/html-resume-portfolio.html`
  - Status: complete
  - Presentation: featured, needs responsive/evolution screenshots
- [x] AI Caption Generator
  - Website: `featured/ai-caption-generator.html`
  - Status: in progress
  - Presentation: featured, needs app screenshots and deploy link
- [x] GAN Discord Bot
  - Website: `featured/gan-discord-bot.html`
  - Status: experimental
  - Presentation: supporting/featured bridge, needs README and output examples
- [x] Data Collaboration Room Studio
  - Website: `featured/data-collab-room-studio.html`
  - Status: archived
  - Presentation: research/design archive
  - Asset package: summary PDF, consultation PDF, capstone presentation PDF, logo PDF
  - Thumbnail: repo-backed Logo System PDF preview

## Supporting Projects

- [x] Abstract Art
- [x] Animal Function Animation
- [x] Animated Short Scene
- [x] Array Visualization Study
- [x] BJUG Day Campaign
- [x] Bridging Biology And AI
- [x] Community Documentary Media
- [x] CORGIS Predictive Data Analysis
- [x] Decision Tree Analysis
- [x] Favorite Things Magazine Spread
- [x] Grid System Dynamic Composition
- [x] Image Tool
- [x] Interactive Number Learning Publication
- [x] LLM Bias Detection Classifier
- [x] Logistic Regression Analysis
- [x] Mountain Terrain Pathfinding
- [x] Multiple Regression Analysis
- [x] Neural Network Analysis
- [x] Package Series Design
  - Website: `supporting/package-series-design.html`
  - Asset package: final package PDF, presentation PDF
- [x] Processing Visual Experiment
- [x] Random Circles Generator
- [x] Regex Pattern Analyzer
- [x] Spelling Bee Puzzle
- [x] Stock Market Visualization Analysis
- [x] Typography Poster Design
- [x] Wang Center Collab Sticker

## Resume Assets

- [x] Resume Project
  - Website: `resume.html`
  - Includes source resume and source cover letter PDFs.

## Portfolio Coverage Audit

Current deterministic asset audit:

- Curated asset files: 48
- Directly linked asset files: 39
- Classified internal/package assets: 9
- Unmatched curated assets: 0

| Repo item | Website presence | Major assets | Coverage status |
|---|---|---|---|
| `featured/data-collab-room-studio` | Featured page + Projects Directory | 4 PDFs: summary, consultation, capstone presentation, logo | Synced |
| `supporting/design/package-series-design*` | Supporting package page + Projects Directory | 2 PDFs: final package, presentation | Synced |
| `featured/grocery-retail-consumer-analytics` | Featured page + Projects Directory | HTML analysis, notebook, CSV, visualization | Synced |
| `featured/battleship-game` | Featured page + Projects Directory | JAR, write-up | Synced |
| `featured/ai-caption-generator` | Featured page + Projects Directory | Reflection PDF plus app files in `assets/ai-caption` | Synced |
| `supporting/design/*.pdf` | Supporting Reel + Projects Directory | Design PDFs and exported thumbnails | Synced |
| `supporting/code/*` | Supporting Reel + Projects Directory | Java, Processing, and source archive files | Public/archive |
| `supporting/data/*` | Supporting Reel + Projects Directory | Notebooks, reports, scripts, CSV/data assets | Public/archive |

## Technical Tasks

- [ ] Add README files for code-heavy projects.
- [ ] Add GitHub repository links where available.
- [ ] Add live demos for web/game projects where possible.
- [ ] Import only GitHub repos that reinforce existing projects or have clear standalone portfolio value.
- [ ] Import Protein AI Pipeline from `lutesAI2025` with ChrisB contribution framing.
- [ ] Add Mabinogi as a standalone supporting technical project after repo/source import.
- [ ] Add `csci367_4` as a supporting team project with lead developer framing after repo/source import.
- [ ] Add Derailed/train-io only with collaborative role and physics/gameplay contribution language.

## Presentation Tasks

- [ ] Add screenshots for games.
- [ ] Add app screenshots for AI Caption Generator.
- [x] Add thumbnail audit checklist.
- [x] Export stronger thumbnails for design PDFs.
- [x] Add chart/generative thumbnails for data notebooks and code studies.
- [ ] Expand flagship project storytelling with process diagrams and outcomes.
- [ ] Replace raw file exposure with dedicated project pages where more context is needed.

## Known UX Refinements

- Supporting Reel is intentionally denser and secondary compared with the Featured Reel.
- Some technical studies still depend on CSS-generated thumbnails until real screenshots or notebook exports are available.
- Some raw source links should eventually become small project pages with context, screenshots, and GitHub links.
- Contact, GitHub, LinkedIn, and PDF resume links should be checked before every deployment.
- GitHub repos should be mapped through `github-repo-sync.md` before adding new pages or reel cards.
