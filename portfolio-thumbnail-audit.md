# Portfolio Thumbnail Audit

Goal: every project card should have an original, portfolio-safe visual with consistent aspect ratio, clear visual weight, and no copyright-risk external thumbnail.

Operating principle: the audit should support the portfolio, not consume it. Prefer better warnings, clearer source-to-frontend mapping, and stronger visual evidence over new governance layers, recursive audits, or automation for its own sake.

Thumbnail rule: every reel card must use one of these: poster, screenshot, UI mockup, diagram, logo, gameplay image, generated cover, branded title card, or original CSS/SVG cover.

Recommended base ratio: 16:10 in the current reel system. 16:9 is also acceptable for future exported image assets, but cards should crop or pad consistently.

## Thumbnail System Rules

- Use original work, project-owned screenshots, project-owned posters, or portfolio-native generated covers.
- Avoid external thumbnails, stock images, random screenshots, tiny icons, stretched images, and raw terminal screenshots.
- Keep one focal point per thumbnail.
- Keep title or concept readable at card size.
- Preserve the dark navy, blue, and yellow portfolio palette.
- Use category-specific fallback covers when real screenshots are not ready.

## Thumbnail Selection Priority

When choosing reel thumbnails, use this order:

1. Real project artifacts already present in the curated repo: screenshots, logos, posters, exported sketches, gameplay captures, PDF previews, notebook visualizations, and UI captures.
2. Derived project visuals: cropped PDF previews, extracted chart visuals, rendered outputs, or frames generated from owned project files.
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
| Opioid Prescribing Risk Analysis | Present | Poster preview | Good | Consistent | More chart crops | Keep poster; add chart-detail alt thumbnail later | Medium |
| Grocery Retail Consumer Analytics | Present | Poster/chart crop | Weak crop | Consistent | Dashboard/process screenshots | Refine to a stronger chart or poster crop; current image is real evidence but visually cramped | Medium |
| Minesweeper Game | Upgraded | Gameplay screenshot | Good | Consistent | Optional tighter crop | Keep real gameplay evidence; crop only if scan quality needs polish | Low |
| Battleship Game | Upgraded | Terminal gameplay screenshot | Good | Consistent | Optional tighter crop | Keep real gameplay evidence; avoid overstating runtime reliability | Low |
| HTML Resume Portfolio | Present | Original web/resume cover | Good fallback | Consistent | Responsive screenshots | Replace with browser mockup screenshot | Medium |
| AI Caption Generator | Present | Original AI workflow cover | Good fallback | Consistent | App upload/output screenshots | Replace with UI screenshot and example captions | High |
| GAN Discord Bot | Present | Original AI workflow cover | Good fallback | Consistent | Bot output examples | Replace with Discord interaction/output screenshot | Medium |
| Data Collaboration Room Studio | Upgraded | Logo System PDF preview | Good | Consistent | Optional studio mockup crop | Keep repo-backed logo artifact; add presentation crop later if stronger | Low |
| Protein AI Pipeline | Present | Research poster / derived crop | Adequate | Consistent | Pipeline or matrix visualization | Keep only if mapping stays explicit: external Cao Labs workstream plus Bridging Biology And AI poster | Medium |
| Mabi AI | Present | Rule/AI visual artifact | Good | Consistent | Optional in-game still | Keep unless a stronger in-game demo still is available | Low |
| Env Design | Present | Final environmental design board | Good | Consistent | None urgent | Keep final PNG; source-note PNG is supporting evidence, not the card visual | Low |

## Supporting Reel Audit

| Project | Current Thumbnail Status | Thumbnail Type | Visual Quality | Aspect Ratio | Missing Assets | Replacement Recommendation | Priority |
|---|---|---|---|---|---|---|---|
| Grid System Composition | Upgraded | Exported PDF preview | Good | Consistent | Stronger crop optional | Keep exported preview; refine crop later if needed | Low |
| Package Series Design | Upgraded | Exported PDF preview | Good | Consistent | Package mockup optional | Keep exported preview; add product mockup later if available | Low |
| Typography Poster Design | Upgraded | Exported PDF preview | Good | Consistent | None urgent | Keep exported poster preview | Low |
| Favorite Things Magazine Spread | Upgraded | Exported PDF preview | Good | Consistent | Spread crop optional | Keep exported preview; refine crop later if needed | Low |
| Interactive Number Learning Publication | Upgraded | Exported PDF preview | Good | Consistent | Spread crop optional | Keep exported preview; refine crop later if needed | Low |
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

- No reel card is missing a visual.
- Several cards still use original generated covers instead of true project screenshots.
- Some frontend titles intentionally differ from source names; keep mappings explicit for `Protein AI Pipeline` / `Bridging Biology And AI`, `SiDiYa Branding System` / `branding-with-name`, and `Short Film And Anti-Racist Art Exhibit` / `community-documentary-media`.
- Data Collaboration Room Studio now uses a repo-backed Logo System PDF preview instead of a generated studio cover.
- Media cards no longer depend on external YouTube thumbnails.
- Media cards now use graphic thumbnail scenes instead of text-only title cards.
- Reel cards now share a consistent fixed media height, border radius, hover behavior, and body rhythm.
- Game cards now have real visual evidence where available; remaining work is crop quality, not basic representation.
- Design PDFs now use exported PNG thumbnails.

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
