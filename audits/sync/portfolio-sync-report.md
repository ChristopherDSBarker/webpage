# Portfolio Synchronization Report

Date: 2026-05-10

Scope:

- Canonical source repo: `/Users/songsidiya/Documents/portfolio`
- Presentation repo: `/Users/songsidiya/Desktop/collaborative_experience_website/portfolio-site`
- GitHub source archive: `https://github.com/ChristopherDSBarker/best_works`
- GitHub webpage repo: `https://github.com/ChristopherDSBarker/webpage`

## Audit Rules

- Do not invent projects.
- Do not merge unrelated folders.
- Do not create inferred mappings.
- Treat `best_works` source folders as canonical.
- Treat `webpage` as the presentation layer.
- Every reel item must have a source mapping, visible route, and intentional thumbnail status.
- Raw datasets, ZIP bundles, and large videos should not be duplicated into the webpage repo.

## Summary

| Area | Status | Notes |
|---|---|---|
| Featured source folders | Synced | 8 canonical local folders remain represented. |
| GitHub-backed featured research project | Synced | Protein AI Pipeline maps to `Cao-Labs/lutesAI2025/ChrisB` with contribution framing. |
| Supporting source folders/files | Synced with partial media polish | All important supporting items appear in the supporting reel or directory. |
| Local/deploy links | Synced | Link audit found 0 missing local targets after patching ignored CSV/ZIP links. |
| Raw data/archive handling | Synced | CSV and ZIP targets are intentionally excluded from webpage deployment and referenced as source-archive material. |
| Deployment safety | Synced | HTML references were validated against tracked files and `.gitignore` exclusions. |
| Thumbnail governance | Partial | Artifact-backed thumbnails exist for posters, PDFs, GIF, sticker, identity emblem, CSCI logo, and room-studio logo; code/data studies still use CSS fallback thumbnails. |
| GitHub contribution framing | Partial | AI Caption Generator, Protein AI Pipeline, and CSCI 367 Game Systems are linked; remaining GitHub repos are classified in `../../docs/github/github-repo-sync.md` but not fully integrated into UI pages. |

## Deployment-Safe Synchronization

Deployment-safe synchronization validates more than local existence. A webpage-visible asset must:

- exist locally
- be tracked in the webpage repo
- avoid `.gitignore` exclusion
- resolve after GitHub Pages deployment
- be intentionally classified if it remains source-only in `best_works`

Audit command:

```bash
python3 tools/deployment_safe_audit.py
```

Current result:

- Missing references: 0
- Ignored-file references: 0
- Untracked references: 0

## Featured Reel Coverage

| Project ID | Source Folder | Reel | Project Page | Thumbnail Status | Sync Status |
|---|---|---:|---:|---|---|
| `opioid-prescribing-risk-analysis` | `featured_projects/opioid-prescribing-risk-analysis/` | Yes | Yes | Artifact poster | Synced |
| `grocery-retail-consumer-analytics` | `featured_projects/grocery-retail-consumer-analytics/` | Yes | Yes | Artifact poster | Synced |
| `minesweeper-game` | `featured_projects/minesweeper-game/` | Yes | Yes | CSS fallback; source tiles exist | Partial thumbnail |
| `battleship-game` | `featured_projects/battleship-game/` | Yes | Yes | CSS fallback; JAR/write-up exist | Partial thumbnail |
| `html-resume-portfolio` | `featured_projects/html-resume-portfolio/` | Yes | Yes | CSS fallback; original HTML/CSS exposed | Partial thumbnail |
| `ai-caption-generator` | `featured_projects/ai-caption-generator/` | Yes | Yes | CSS fallback; GitHub linked | Partial thumbnail |
| `gan-discord-bot` | `featured_projects/gan-discord-bot/` | Yes | Yes | CSS fallback; source code exposed | Partial thumbnail |
| `data-collab-room-studio` | `featured_projects/data_collab_room_studio/` | Yes | Yes | Derived logo-system PDF preview | Synced |

## Supporting Reel Coverage

| Project ID | Canonical Source | Reel/Directory | Presentation Route | Thumbnail Status | Sync Status |
|---|---|---:|---|---|---|
| `grid-system-dynamic-composition` | `supporting projects/grid-system-dynamic-composition.pdf` | Yes | Direct PDF | Derived PDF preview | Synced |
| `package-series-design` | `supporting projects/package-series-design/` | Yes | `supporting/package-series-design.html` | Derived PDF preview | Synced |
| `sidiya-branding-system` | `supporting projects/branding-with-name/` | Yes | `supporting/sidiya-branding-system.html` | Artifact emblem | Synced |
| `typography-poster-design` | `supporting projects/typography-poster-design.pdf` | Yes | Direct PDF | Derived PDF preview | Synced |
| `favorite-things-magazine-spread` | `supporting projects/favorite-things-magazine-spread.pdf` | Yes | Direct PDF | Derived PDF preview | Synced |
| `interactive-number-learning-publication` | `supporting projects/interactive-number-learning-publication.pdf` | Yes | Direct PDF | Derived PDF preview | Synced |
| `wang-center-collab-sticker` | `supporting projects/wang_center_collab.jpeg` | Yes | `supporting/wang-center-collab-sticker.html` | Artifact image | Synced |
| `llm-bias-detection-classifier` | `supporting projects/llm-bias-detection-classifier/` | Yes | Report/code assets | CSS fallback | Partial thumbnail |
| `corgis-predictive-data-analysis` | `supporting projects/corgis-predictive-data-analysis/` | Yes | HTML/notebook assets | CSS fallback | Partial thumbnail |
| `stock-market-visualization-analysis` | `supporting projects/stock-market-visualization-analysis/` | Yes | HTML/R assets | CSS fallback | Partial thumbnail |
| `logistic-regression-analysis` | `supporting projects/logistic_regression_analysis.ipynb` | Yes | Notebook asset | CSS fallback | Partial thumbnail |
| `decision-tree-analysis` | `supporting projects/decision_tree_analysis.ipynb` | Yes | Notebook asset | CSS fallback | Partial thumbnail |
| `neural-network-analysis` | `supporting projects/nueral_network_analysis.ipynb` | Yes | Notebook asset | CSS fallback | Partial thumbnail |
| `multiple-regression-analysis` | `supporting projects/multipleRegression_analysis.ipynb` | Yes | Notebook asset | CSS fallback | Partial thumbnail |
| `csci367-game-systems` | `distcrypto/csci367_4` | Yes | `supporting/csci367-game-systems.html` | Artifact concept logo | Synced |
| `spelling-bee-puzzle` | `supporting projects/spelling-bee-puzzle/` | Yes | Java source asset | CSS fallback | Partial thumbnail |
| `mountain-terrain-pathfinding` | `supporting projects/mountain-terrain-pathfinding/` | Yes | Java source asset | CSS fallback | Partial thumbnail |
| `image-tool` | `supporting projects/image-tool/` | Yes | Java source asset | CSS fallback | Partial thumbnail |
| `abstract-art` | `supporting projects/abstract-art/` | Yes | Java source asset | CSS fallback | Partial thumbnail |
| `regex-pattern-analyzer` | `supporting projects/regex-pattern-analyzer/` | Yes | `supporting/regex-pattern-analyzer.html` | CSS fallback | Partial source exposure |
| `processing-visual-experiment` | `supporting projects/processing-visual-experiment.pde` | Yes | PDE asset | CSS fallback | Partial thumbnail |
| `array-visualization-study` | `supporting projects/array-visualization-study.pde` | Yes | PDE asset | CSS fallback | Partial thumbnail |
| `animal-function-animation` | `supporting projects/animal-function-animation.pde` | Yes | PDE asset | CSS fallback | Partial thumbnail |
| `random-circles-generator` | `supporting projects/random-circles-generator.pde` | Yes | PDE asset | CSS fallback | Partial thumbnail |
| `bridging-biology-and-ai` | `supporting projects/bridging-biology-and-ai-understanding.pdf` | Yes | Direct PDF | Derived PDF preview | Synced |
| `animated-short-scene` | `supporting projects/animated-short-scene.gif` | Yes | Direct GIF | Artifact GIF | Synced |
| `community-documentary-media` | `supporting projects/community-documentary-media/` | Yes | `supporting/short-film-antiracist-exhibit.html` | CSS fallback; YouTube page | Partial thumbnail |
| `bjug-day-campaign` | `supporting projects/bjug-day-campaign.mp4` | Yes | `supporting/bjug-day-campaign.html` | CSS fallback; YouTube page | Partial thumbnail |

## Missing Asset Report

No canonical project folder/file is currently missing from the visible project system.

Known partials:

- Notebook/data studies need exported chart thumbnails if the goal is fully artifact-backed media.
- Java/Processing projects need rendered screenshots or exported sketch frames.
- CSCI 367 Game Systems is synchronized, but would benefit from an owned UI screenshot or auth/save/leaderboard systems diagram.
- Video/media projects need owned still frames if the goal is artifact-backed thumbnails.
- Regex Pattern Analyzer has a presentation page, but raw ZIP bundles are intentionally excluded from webpage deployment.

## Duplicate Thumbnail Report

No duplicate image-file thumbnail collisions were found in the major artifact-backed cards.

Remaining visual risk:

- CSS fallback thumbnails are intentionally distinct by class, but they are still fallback graphics rather than repo-derived artifacts.
- Long-term improvement should replace fallbacks with screenshots, exports, notebook charts, or owned stills.

## Unreachable Project Report

No unreachable canonical project group was found.

The following raw assets are intentionally not linked as deployable webpage files:

- Raw CSV datasets and summaries.
- Original assignment ZIP bundles.
- Large source videos.

Project pages now describe these as canonical source-archive materials instead of linking to ignored deployment files.

## Orphaned Repo Folder Report

No top-level featured/supporting source folder is orphaned from the website.

Top-level canonical coverage:

- Featured folders: 8/8 visible.
- Supporting folders: 10/10 visible.
- GitHub-backed supporting integrations: 1/1 visible for `distcrypto/csci367_4`.
- Supporting single-file works: 16/16 visible or intentionally represented.

## Next Surgical Sync Passes

1. Replace CSS fallback thumbnails with repo-derived artifacts where possible.
2. Add GitHub buttons and role labels one repo at a time from `../../docs/github/github-repo-sync.md`.
3. Create stronger artifact pages only where source folders contain enough material to justify them.
4. Keep raw datasets, ZIPs, and videos in `best_works`; do not duplicate them into `webpage`.
