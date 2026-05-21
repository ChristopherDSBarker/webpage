# Portfolio Thumbnail Audit

Goal: every project card should have an original, portfolio-safe visual with consistent aspect ratio, clear visual weight, and no copyright-risk external thumbnail.

Operating principle: the audit should support the portfolio, not consume it. Prefer better warnings, clearer source-to-frontend mapping, and stronger visual evidence over new governance layers, recursive audits, or automation for its own sake.

Thumbnail existence rule: every reel card must use one of these: poster, screenshot, UI mockup, diagram, logo, gameplay image, generated cover, branded title card, or original CSS/SVG cover.

Reel readability rule: existence is not approval. A reel card passes visual QA
only when it works at small scale, next to neighboring cards, during fast
recruiter scanning.

Recommended base ratio: 16:10 in the current reel system. 16:9 is also acceptable for future exported image assets, but cards should crop or pad consistently.

## Thumbnail System Rules

- Use original work, project-owned screenshots, project-owned posters, or portfolio-native generated covers.
- Avoid external thumbnails, stock images, random screenshots, tiny icons, stretched images, and raw terminal screenshots.
- Keep one focal point per thumbnail.
- Keep title or concept readable at card size.
- Preserve the dark navy, blue, and yellow portfolio palette.
- Use category-specific fallback covers when real screenshots are not ready.

## Reel Composition Rules

A reel card is a hook and recognition cue. It is not a full project explanation,
compressed report, or document archive.

Good reel cards usually have:

- one focal idea
- one dominant visual shape
- low text density
- readable contrast
- a recognizable silhouette or project identity
- enough breathing room to survive next to neighboring cards

Bad reel cards usually show:

- full posters or full PDF pages
- raw document pages
- tiny unreadable charts
- overly dense scientific or presentation boards
- generic fallback covers next to evidence-heavy artifacts
- gameplay screens zoomed too far out
- title slides with weak focal hierarchy

If a reel thumbnail is semantically accurate but visually unreadable at reel
scale, prefer a simpler honest composition.

## Reel Categories

| Category | Good Reel Composition | Bad Reel Composition |
|---|---|---|
| Gameplay / UI | active interaction state, readable board, real app/output moment | entire screen, distant board, empty terminal, tiny interface |
| Diagram / System | one system flow, result cluster, model/output relationship | full report, compressed pipeline poster, dense slide |
| Artifact / Design | one composition moment, extracted crop, strong hierarchy | full poster, raw PDF page, full spread, text-heavy document |

## Thumbnail Selection Priority

When choosing reel thumbnails, use this order:

1. Real project artifacts already present in the curated repo: gameplay captures, UI captures, chart/result visuals, pipeline diagrams, exported design boards, logos, PDF previews, and notebook visualizations.
2. Derived project visuals: cropped PDF previews, extracted chart visuals, rendered outputs, or frames generated from owned project files, but only when the crop becomes a reel composition rather than a full document page.
3. Generated abstract thumbnails only when no project-specific media exists.

Generated covers should never replace strong original project visuals already present in the repo.

## Known Visual Risks

- Overusing node/circle compositions across unrelated categories.
- Adding decorative overlay structures that compete with the project concept.
- Making too many supporting thumbnails look like generic dashboard graphics.
- Repeating the same dark-tech visual grammar until different projects blur together.

## Thumbnail Stop Rule

Stop active thumbnail refinement once:

- every card has an original visual
- no card feels broken, empty, or placeholder-like
- categories are distinguishable at thumbnail scale
- the reel scans cleanly during horizontal scrolling

Further refinement beyond this point is optional polish and should be driven by real project screenshots, exported charts, or owned media stills.

## Warning Levels

- `Missing`: no concrete frontend representation or archive/internal classification exists. This blocks parity.
- `Weak`: the item is represented, but the card relies on fallback art, a generic cover, or a low-evidence crop.
- `Mismapped`: the frontend title/category/source path is not clearly tied to the canonical source name.
- `Visual Evidence Gap`: the source exists and is represented, but the thumbnail does not show the strongest available proof.

Tool warnings are leads. A warning should result in one of three outcomes: improve the page/media, clarify the mapping, or explicitly mark the source as archive/internal. Do not create another audit layer just to restate the same uncertainty.

## Thumbnail Map

`thumbnail-map.json` is the operational source-of-truth for reel thumbnail selection. It records:

- current thumbnail source
- original repo asset when available
- `artifact`, `derived`, or `fallback` status
- next best replacement asset

Projects marked `fallback` should be upgraded only when a real repo-backed artifact becomes available.

## Priority Definitions

- `High`: flagship presentation weakness or card that directly affects first impression.
- `Medium`: worthwhile polish that improves project identity or evidence quality.
- `Low`: optional future enhancement after the reel already works.

## Category Styles

| Category | Best Thumbnail Type | Fallback Type |
|---|---|---|
| Research / Analytics | Poster, chart, dashboard, workflow diagram | Data cover |
| Interactive / Games | Gameplay screenshot, board mockup, title screen | Game board cover |
| AI Tools | UI screenshot, workflow, generated output preview | AI workflow cover |
| Design / Studio | Poster/spread preview, mockup, system diagram | Design grid cover |
| Media / Documentary | Original title card, still frame owned by project | Media title card |
| Creative Coding | GIF export, sketch screenshot | Creative cover |
| Code / Java | App screenshot, diagram, code visualization | Code cover |

## Featured Reel Audit

| Project | Current Thumbnail Status | Thumbnail Type | Visual Quality | Aspect Ratio | Missing Assets | Replacement Recommendation | Priority |
|---|---|---|---|---|---|---|---|
| Opioid Prescribing Risk Analysis | Present | Poster preview | Review | Consistent | More chart crops | Prefer one chart/result cluster if full poster compresses at reel scale | Medium |
| Grocery Retail Consumer Analytics | Present | Poster/chart crop | Weak crop | Consistent | Dashboard/process screenshots | Refine to a single insight graphic; current image is real evidence but visually dense | Medium |
| Minesweeper Game | Upgraded | Gameplay screenshot | Review | Consistent | Optional tighter crop | Keep real gameplay evidence; verify board is not too zoomed out at reel scale | Low |
| Battleship Game | Upgraded | Terminal gameplay screenshot | Review | Consistent | Optional tighter crop | Keep real gameplay evidence; reduce empty terminal space if it weakens scan clarity | Low |
| HTML Resume Portfolio | Present | Original web/resume cover | Good fallback | Consistent | Responsive screenshots | Replace with browser mockup screenshot | Medium |
| AI Caption Generator | Present | Original AI workflow cover | Intentional fallback | Consistent | App upload/output screenshots | Keep only as honest fallback; replace with real UI/output evidence when available | High |
| GAN Discord Bot | Present | Original AI workflow cover | Intentional fallback | Consistent | Bot output examples | Keep only as honest fallback; replace with Discord interaction/output screenshot | Medium |
| Data Collaboration Room Studio | Upgraded | Logo System PDF preview | Review | Consistent | Optional studio mockup crop | Avoid title-slide feel; prefer room/system identity if available | Medium |
| Protein AI Pipeline | Present | Research poster / derived crop | Adequate | Consistent | Pipeline or matrix visualization | Keep only if mapping stays explicit: external Cao Labs workstream plus Bridging Biology And AI poster | Medium |
| Mabi AI | Present | Rule/AI visual artifact | Good | Consistent | Optional in-game still | Keep unless a stronger in-game demo still is available | Low |
| Env Design | Present | Final environmental design board | Review | Consistent | None urgent | Prefer ecosystem/mountain focal composition over full educational poster | Medium |

## Supporting Reel Audit

| Project | Current Thumbnail Status | Thumbnail Type | Visual Quality | Aspect Ratio | Missing Assets | Replacement Recommendation | Priority |
|---|---|---|---|---|---|---|---|
| Grid System Composition | Upgraded | Exported PDF preview | Review | Consistent | Stronger crop optional | Extract one hierarchy/composition moment instead of raw poster page | Medium |
| Package Series Design | Upgraded | Exported PDF preview | Good | Consistent | Package mockup optional | Keep exported preview; add product mockup later if available | Low |
| Typography Poster Design | Upgraded | Exported PDF preview | Good | Consistent | None urgent | Keep exported poster preview | Low |
| Favorite Things Magazine Spread | Upgraded | Exported PDF preview | Review | Consistent | Spread crop optional | Extract one typography/composition focal crop instead of raw page scan | Medium |
| Interactive Number Learning Publication | Upgraded | Exported PDF preview | Review | Consistent | Spread crop optional | Extract one learning interaction or publication detail instead of full document page | Medium |
| Wang Center Collab Sticker | Present | Project image | Good | Consistent | None urgent | Keep, crop if needed | Low |
| LLM Bias Detection Classifier | Present | Original data cover | Good fallback | Consistent | Chart/model screenshot | Add classifier report visual | Medium |
| Stock Market Visualization Analysis | Present | Original data cover | Good fallback | Consistent | Chart thumbnail | Export a strong plot from report | Medium |
| CORGIS Predictive Data Analysis | Present | Original data cover | Good fallback | Consistent | Notebook chart thumbnail | Export chart crop | Medium |
| Logistic Regression Analysis | Present | Original data cover | Good fallback | Consistent | Notebook chart thumbnail | Add model/ROC/confusion visual | Low |
| Decision Tree Analysis | Present | Original data cover | Good fallback | Consistent | Tree diagram | Add tree plot export | Low |
| Neural Network Analysis | Present | Original data cover | Good fallback | Consistent | Training curve/architecture | Add training curve or layer diagram | Low |
| Multiple Regression Analysis | Present | Original data cover | Good fallback | Consistent | Regression chart | Add coefficient/residual chart | Low |
| Spelling Bee Puzzle | Present | Original code cover | Good fallback | Consistent | UI or output screenshot | Add puzzle UI/text output screenshot | Low |
| Mountain Terrain Pathfinding | Present | Original code cover | Good fallback | Consistent | Terrain/path visual | Add terrain path screenshot | Medium |
| Image Tool | Present | Original code cover | Good fallback | Consistent | Before/after image | Add image transform comparison | Medium |
| Abstract Art | Present | Original creative cover | Good fallback | Consistent | Java canvas screenshot | Add generated art screenshot | Medium |
| Regex Pattern Analyzer | Present | Original code cover | Good fallback | Consistent | Pattern/output screenshot | Add analyzer output screenshot | Low |
| Processing Visual Experiment | Present | Original creative cover | Good fallback | Consistent | Sketch screenshot/GIF | Export sketch image | Medium |
| Array Visualization Study | Present | Original creative cover | Good fallback | Consistent | Sketch screenshot/GIF | Export sketch image | Medium |
| Animal Function Animation | Present | Original creative cover | Good fallback | Consistent | Animation GIF | Export GIF or still frame | Medium |
| Random Circles Generator | Present | Original creative cover | Good fallback | Consistent | Sketch screenshot | Export generated circles image | Medium |
| Bridging Biology And AI | Upgraded | Exported PDF preview | Good | Consistent | None urgent | Keep exported PDF preview | Low |
| Animated Short Scene | Present | Project GIF | Good | Consistent | None urgent | Keep GIF, verify file size later | Low |
| Community Documentary Media | Upgraded | Original media title card | Good, copyright-clean | Consistent | Owned still frames | Replace with owned still frame if available | Medium |
| BJUG Day Campaign | Upgraded | Original media title card | Good, copyright-clean | Consistent | Campaign stills/screenshots | Replace with owned campaign still if available | Medium |

## Current Gaps

- Previous audited state had no missing reel visuals; the 2026-05-21 patch removes live references to deleted reel crops instead of restoring them.
- Several cards still use original generated covers instead of true project screenshots.
- Some frontend titles intentionally differ from source names; keep mappings explicit for `Protein AI Pipeline` / `Bridging Biology And AI`, `SiDiYa Branding System` / `branding-with-name`, and `Short Film And Anti-Racist Art Exhibit` / `community-documentary-media`.
- Data Collaboration Room Studio now uses a repo-backed Logo System PDF preview instead of a generated studio cover.
- Media cards no longer depend on external YouTube thumbnails.
- Media cards now use graphic thumbnail scenes instead of text-only title cards.
- Reel cards now share a consistent fixed media height, border radius, hover behavior, and body rhythm.
- Game cards now have real visual evidence where available; remaining work is crop quality, not basic representation.
- Design PDFs now use exported PNG thumbnails.
- Validate paths before relying on older `Present` or `Upgraded` labels, because several file-backed thumbnail assets are currently deleted locally.

## 2026-05-21 Semantic Reference Audit

Scope inspected:

- `core_knowledge/PORTFOLIO_ARCHITECTURE_GUIDE.md`
- `core_knowledge/PORTFOLIO_REPRESENTATION_RULES.md`
- `core_knowledge/VISUAL_QA_RULES.md`
- `projects.html`
- `thumbnail-map.json`
- `images/thumbnails/reels/`
- `audits/thumbnails/portfolio-thumbnail-audit.md`
- `/Users/songsidiya/Documents/portfolio` source archive, read-only

Architecture finding:

- `best_works` / `/Users/songsidiya/Documents/portfolio` remains the source/archive layer.
- `core_knowledge/` defines the rules for representation, no-hallucination, and visual QA.
- The webpage repo is only the deployable presentation layer.
- `thumbnail-map.json` records visual routing, but it should not claim deployable image assets that are absent from the repo.

Current worktree finding:

- `images/thumbnails/reels/` is empty in the current working tree because the bad reel crops were intentionally deleted.
- Do not restore deleted reel crops from git history unless a future human review explicitly approves one.
- The 2026-05-21 reel strategy patch removes live `projects.html` and `thumbnail-map.json` references to deleted reel files.
- Replacement choices use only existing approved homepage thumbnails, canonical source media, or CSS/text fallbacks.
- Missing-safe-image cases are marked as `HUMAN SCREENSHOT NEEDED` instead of inventing a visual.

### 2026-05-21 Reel Strategy Patch Decisions

| Project | Deleted reel asset removed | Current safe strategy | Expected meaning from source/core evidence | Mismatch status | Recommended action |
|---|---|---|---|---|---|
| Protein AI Pipeline | `images/thumbnails/reels/protein-ai-pipeline-reel.png` | `images/thumbnails/homepage/protein-ai-pipeline-home.png` | Cao Labs `ChrisB` research implementation plus Bridging Biology And AI supporting poster/pipeline evidence. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Mabi AI | `images/thumbnails/reels/mabi-ai-reel.png` | `images/thumbnails/homepage/mabi-ai-home.png` | Legacy Mabinogi pet AI behavior logic using XML/rule evidence. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Opioid Prescribing Risk Analysis | `images/thumbnails/reels/opioid-prescribing-risk-analysis-reel.png` | `images/thumbnails/homepage/opioid-prescribing-risk-analysis-home.png` | Healthcare data analysis, poster, charts, and model interpretation. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Pixel Progression | `images/thumbnails/reels/pixel-progression-reel.png` | `images/thumbnails/homepage/pixel-progression-home.png` | Collaborative PHP/JavaScript game systems with real gameplay, auth, saved state, and leaderboard context. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Grocery Retail Consumer Analytics | `images/thumbnails/reels/grocery-retail-consumer-analytics-reel.png` | `images/thumbnails/homepage/grocery-retail-consumer-analytics-home.png` | Consumer analytics poster/chart evidence from the grocery retail project. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Minesweeper Game | `images/thumbnails/reels/minesweeper-game-reel.png` | `images/thumbnails/homepage/minesweeper-game-home.png` | Real revealed Minesweeper board gameplay. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Battleship Game | `images/thumbnails/reels/battleship-game-reel.png` | `images/thumbnails/homepage/battleship-game-home.png` | Java Battleship terminal/gameplay board evidence. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| HTML Resume Portfolio | `images/thumbnails/reels/html-resume-portfolio-reel.png` | `images/thumbnails/homepage/html-resume-portfolio-home.png` | Rendered HTML/CSS resume or browser screenshot evidence. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Data Collaboration Room Studio | `images/thumbnails/reels/data-collaboration-room-studio-reel.png` | `images/thumbnails/homepage/data-collaboration-room-studio-home.png` | Four-PDF studio package: summary, consultation, capstone presentation, and logo system. | OK | Reuse approved homepage thumbnail; human can later decide whether reel should emphasize capstone or logo-system identity. |
| Env Design | `images/thumbnails/reels/env-design-reel.png` | `images/thumbnails/homepage/env-design-home.png` | Environmental design board for the Mount Rainier Paradise Area ecosystem. | OK | Reuse approved homepage thumbnail until a human-approved reel crop exists. |
| Grid System Composition | `images/thumbnails/reels/grid-system-dynamic-composition-reel.png` | CSS/text design fallback | Grid-system composition PDF/design artifact. | HUMAN SCREENSHOT NEEDED | Keep fallback until a safe PDF-derived crop is reviewed. |
| Package Series Design | `images/thumbnails/reels/package-series-design-reel.png` | CSS/text design fallback | Packaging design PDF package and presentation artifact. | HUMAN SCREENSHOT NEEDED | Keep fallback until a safe package or presentation crop is reviewed. |
| SiDiYa Branding System | `images/thumbnails/reels/sidiya-branding-system-reel.png` | `assets/brand/sidiya-emblem-final.png` | Personal identity system, emblem, typography, cultural symbolism, and website brand layer. | OK | Reuse canonical emblem source media. |
| Typography Poster Design | `images/thumbnails/reels/typography-poster-design-reel.png` | CSS/text design fallback | Typography/poster composition artifact. | HUMAN SCREENSHOT NEEDED | Keep fallback until a safe poster crop is reviewed. |
| Favorite Things Magazine Spread | `images/thumbnails/reels/favorite-things-magazine-spread-reel.png` | CSS/text design fallback | Editorial/magazine spread design artifact. | HUMAN SCREENSHOT NEEDED | Keep fallback until a safe spread crop is reviewed. |
| Interactive Number Learning Publication | `images/thumbnails/reels/interactive-number-learning-publication-reel.png` | CSS/text design fallback | Interactive visual-learning publication artifact. | HUMAN SCREENSHOT NEEDED | Keep fallback until a safe publication crop is reviewed. |
| Wang Center Collab Sticker | `images/thumbnails/reels/wang-center-collab-sticker-reel.jpeg` | `assets/supporting/media/wang-center-collab.jpeg` | Sticker / visual communication artifact from the supporting source file. | OK | Reuse canonical source media. |
| CSCI 367 Game Systems | `images/thumbnails/reels/csci367-game-systems-reel.png` | `assets/supporting/media/csci367-conceptlogo.png` | Collaborative PHP/JavaScript game systems with auth, save/load, leaderboard, and gameplay systems. | NEEDS HUMAN REVIEW | Use concept logo as a safe temporary visual; a gameplay/UI screenshot is still preferred. |
| Animated Short Scene | `images/thumbnails/reels/animated-short-scene-reel.gif` | `assets/supporting/animated-short-scene.gif` | Animation / motion study using the source GIF artifact. | OK | Reuse canonical source GIF. |

### Generic or fallback reel references

These are not broken file references because they render through CSS/native markup, but they remain semantic review leads. Patch only when a real source-backed screenshot, chart, still, or output is available.

| Project | Current thumbnail/reel asset | Expected meaning from source/core evidence | Mismatch status | Recommended action |
|---|---|---|---|---|
| AI Caption Generator | CSS-generated AI app cover | Streamlit/upload-output caption app evidence. | NEEDS HUMAN REVIEW | Keep fallback until a real app screenshot or generated-caption output is captured. |
| GAN Discord Bot | CSS-generated Discord bot cover | Discord bot interaction and image-generation output. | NEEDS HUMAN REVIEW | Keep fallback until real bot output evidence exists. |
| LLM Bias Detection Classifier | CSS-generated data cover | Bias-classifier report, model output, or chart evidence. | SUSPECT | Replace only with a real report chart or classifier output screenshot. |
| Stock Market Visualization Analysis | CSS-generated data cover | R visualization/report chart evidence. | SUSPECT | Export a strong plot from the report before changing the reel. |
| CORGIS Predictive Data Analysis | CSS-generated data cover | Notebook/HTML analysis chart evidence. | SUSPECT | Use a notebook chart crop only after confirming the chart exists in source. |
| Logistic Regression Analysis | CSS-generated statistics cover | Statistical modeling output such as ROC, confusion matrix, or notebook result. | SUSPECT | Add a real model-output crop when available. |
| Decision Tree Analysis | CSS-generated tree cover | Decision-tree diagram or notebook result. | SUSPECT | Add a real tree plot export when available. |
| Neural Network Analysis | CSS-generated neural cover | Training curve, architecture diagram, or notebook result. | SUSPECT | Add a real training/architecture visual when available. |
| Multiple Regression Analysis | CSS-generated regression cover | Coefficient, residual, or regression chart evidence. | SUSPECT | Add a real chart crop when available. |
| Spelling Bee Puzzle | CSS-generated puzzle/code cover | Java puzzle output or UI/text evidence. | SUSPECT | Add an output screenshot only if it comes from the source package. |
| Mountain Terrain Pathfinding | CSS-generated terrain/code cover | Terrain/pathfinding visual or output evidence. | SUSPECT | Add a verified terrain/path screenshot when available. |
| Image Tool | CSS-generated image-tool cover | Before/after pixel/image modification evidence. | SUSPECT | Add a source-backed before/after comparison when available. |
| Abstract Art | CSS-generated creative cover | Rendered Java drawing/canvas output. | SUSPECT | Add a rendered output screenshot when available. |
| Regex Pattern Analyzer | CSS-generated regex/code cover | Pattern analyzer output or highlighted text evidence. | SUSPECT | Add a verified output screenshot when available. |
| Processing Visual Experiment | CSS-generated creative cover | Processing sketch frame or GIF evidence. | SUSPECT | Export a source-backed sketch frame before changing. |
| Array Visualization Study | CSS-generated creative cover | Processing array-visualization sketch evidence. | SUSPECT | Export a source-backed sketch frame before changing. |
| Animal Function Animation | CSS-generated motion cover | Processing animation frame or GIF evidence. | SUSPECT | Export a source-backed animation still/GIF before changing. |
| Random Circles Generator | CSS-generated circles cover | Processing generated-circle sketch evidence. | SUSPECT | Export a source-backed generated sketch frame before changing. |
| Community Documentary Media | CSS-generated media title card | Original short film / anti-racist exhibit media context. | NEEDS HUMAN REVIEW | Use only an owned, cleared still frame; keep CSS title card otherwise. |
| BJUG Day Campaign | CSS-generated campaign title card | Campaign video/project media context. | NEEDS HUMAN REVIEW | Use only an owned campaign still; keep CSS title card otherwise. |

Recommended patch plan:

1. Keep `projects.html` and `thumbnail-map.json` aligned so neither claims deleted `images/thumbnails/reels/*` files.
2. Do not restore deleted reel thumbnails unless a future human review explicitly approves the exact file.
3. For `Grid System Composition`, `Package Series Design`, `Typography Poster Design`, `Favorite Things Magazine Spread`, and `Interactive Number Learning Publication`, capture or export a human-approved source-backed crop before replacing the CSS fallback.
4. For `CSCI 367 Game Systems`, use a real gameplay/UI screenshot when available; until then the concept logo is only a safe temporary visual.
5. For existing CSS fallback projects, leave the fallback in place unless a real source-backed screenshot, chart, still, or output exists.

Common mistake warning:

- Do not ask AI to "make thumbnails better" from filenames.
- Do not use nearest matching image names as evidence.
- Do not generate random thumbnails to fill missing paths.
- Do not change project descriptions while fixing thumbnail references.
- Do not edit `core_knowledge/`, `ALL_SLIDES/`, or source/archive folders for this presentation-layer audit.

## NO_REAL_THUMBNAIL Tags

These projects have original, copyright-safe generated covers, but still need real exported screenshots, PDF previews, renders, or captured outputs for final polish.

- HTML Resume Portfolio
- AI Caption Generator
- GAN Discord Bot
- LLM Bias Detection Classifier
- Stock Market Visualization Analysis
- CORGIS Predictive Data Analysis
- Logistic Regression Analysis
- Decision Tree Analysis
- Neural Network Analysis
- Multiple Regression Analysis
- Spelling Bee Puzzle
- Mountain Terrain Pathfinding
- Image Tool
- Abstract Art
- Regex Pattern Analyzer
- Processing Visual Experiment
- Array Visualization Study
- Animal Function Animation
- Random Circles Generator
- Community Documentary Media
- BJUG Day Campaign

## Priority Queue

1. Add AI Caption Generator UI screenshot and generated-caption example.
2. Refine Grocery Retail Consumer Analytics to a stronger chart or poster crop.
3. Export chart thumbnails for data notebooks.
4. Add screenshots or renders for Java and Processing projects.
5. Replace media title cards with owned still frames only if the stills are original/cleared.
6. Tighten mapping labels for source-name aliases before adding more process documentation.
