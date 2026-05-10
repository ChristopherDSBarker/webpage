# Christopher Barker Portfolio Site

Applied technical portfolio focused on AI experimentation, data visualization, interactive systems, frontend/web development, and visual communication.

This repository contains the deployable GitHub Pages version of the portfolio. It is designed as one curated portfolio site, not a dump of every source file.

## Intended Audience

- internship recruiters
- frontend/UI hiring teams
- research reviewers
- collaborators
- academic portfolio review

## Technologies Represented

- HTML/CSS/JavaScript
- Python
- Java
- Processing
- R
- Streamlit
- GitHub Pages

## Deployment Target

This folder is ready to become the root content of the GitHub Pages repository:

```text
christopherbarker.github.io
```

When pushed to that repo, the site will be available at:

```text
https://christopherbarker.github.io
```

## Site Structure

```text
portfolio-site/
  index.html
  about.html
  projects.html
  resume.html
  contact.html
  css/
  js/
  images/
  assets/
  featured/
  supporting/
  resume/
```

## Content Layers

### Featured Projects

Flagship work prioritized for first impressions, recruiter scanning, and project-page storytelling.

### Supporting Work

Secondary technical, design, media, and archive material that shows breadth without cluttering the homepage.

### Project Directory

Complete discoverability layer that makes sure every important project has a visible path.

## Portfolio Architecture Principles

- Strongest work appears first.
- Homepage stays curated and limited.
- Every important project must be visible from at least one page.
- Project pages must reflect the curated source folder structure.
- Supporting work is secondary by design, not a second featured reel.
- Thumbnails should be original, media-driven, and copyright-safe.
- Project pages should prioritize screenshots, process, outcomes, and links over raw file exposure.

## Repository Synchronization Rule

Project pages must treat curated source folders as source-of-truth. If a folder contains PDFs, screenshots, presentations, logos, demos, or exports, the page should expose them, summarize them, or intentionally classify them. Avoid compressing multiple curated assets into a single generalized description.

## Repository Coverage Rule

Every curated repository item must satisfy at least one of these:

- visible in the Featured Reel
- visible in the Supporting Reel
- visible in the Project Directory
- exposed on a dedicated project page
- linked from the Resume page
- intentionally classified as archival/internal

No curated project folder should become unreachable from the portfolio navigation system. Omission must be intentional and documented, never accidental.

## GitHub Synchronization Rule

Public GitHub repositories should be mapped through `github-repo-sync.md` before they are added to reels or project pages. GitHub links should reinforce existing project identities when possible. Collaborative repositories require contribution clarification and should not imply sole ownership.

Contribution framing should be explicit. Use labels such as `Lead developer`, `Research implementation`, `Physics systems / gameplay mechanics`, `Solo / Full implementation`, or `Archive/reference` so collaborative work is neither hidden nor overstated.

Repository existence and public linkability are separate. A repo may be verified through public API visibility, browser-visible repository listings, user confirmation, or local sync records. Private/collaborative verified repos may be represented in the portfolio with role language, but public GitHub buttons should only be added after URL accessibility and intended visibility are confirmed.

## Project Package Standard

When a project folder contains multiple meaningful assets, present it as a package. Each major asset should be classified as one of:

- summary
- presentation
- consultation
- branding
- screenshot
- demo
- source
- export

## Thumbnail Selection Priority

Reel thumbnails should prefer actual project artifacts over generated representations:

1. Real repo-backed artifacts: screenshots, logos, posters, exported sketches, gameplay captures, PDF previews, notebook visualizations, and UI captures.
2. Derived project visuals: cropped PDF pages, extracted charts, rendered outputs, or owned media frames.
3. Generated abstract thumbnails only when no project-specific visual exists.

Generated covers should not replace strong original visuals already present in the curated repo.

`thumbnail-map.json` tracks the current thumbnail source for each reel item and marks it as `artifact`, `derived`, or `fallback`.

## Portfolio Philosophy

The portfolio prioritizes:

- applied technical creativity
- visual communication
- project discoverability
- original project artifacts
- scalable organization

## Source vs Presentation

Some raw coursework/source files are preserved for archival transparency. Presentation-facing pages should prioritize:

- screenshots and thumbnails
- concise project summaries
- process/context sections
- GitHub or demo links when available
- curated visual artifacts instead of raw folders

## Current Refinement Priorities

1. Confirm `contact.html` still uses the current email, GitHub, and LinkedIn links.
2. Add individual GitHub repository links to each featured project page when those repos are published.
3. Add stronger gameplay screenshots for Battleship and Minesweeper.
4. Deploy game projects separately if possible, then link the live demos.
5. Expand visual/process presentation for flagship AI and data projects.
6. Continue replacing raw file links with project pages where the work deserves more context.

## Publishing Checklist

1. Review `portfolio-inventory.md` for missing assets or hidden work.
2. Confirm all local links and PDFs resolve.
3. Check mobile layout for homepage, projects, resume, and contact pages.
4. Copy the contents of `portfolio-site/` into the root of `christopherbarker.github.io`.

## Curation rule

Keep the homepage limited to the strongest 4 to 6 visual projects plus resume and contact buttons. Put extra work in `projects.html` or `supporting/`.
