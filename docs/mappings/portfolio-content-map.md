# Portfolio Content Map

This document treats the portfolio like a content database: projects are entities, categories are relationships, and every meaningful item must have a visible path.

## Sitemap

| Page | Purpose | Primary Paths |
|---|---|---|
| `index.html` | First impression, intro, resume/contact CTAs, featured preview, all-work CTA | Nav, footer |
| `projects.html` | Primary work hub with Featured Reel, Supporting Reel, jump links, and complete directory | Nav, homepage, footer |
| `archive.html` | Backup complete categorized project directory | Projects directory reference |
| `resume.html` | Resume PDF, web resume, application assets, experience highlights | Nav, homepage CTA, footer |
| `contact.html` | Contact CTA and external profile links | Nav, homepage CTA, footer |
| `about.html` | Short identity/context page | Footer |
| `featured/*.html` | Dedicated featured project pages | Homepage reel, Projects reel, Projects directory |
| `supporting/*.html` | Dedicated supporting project pages for media/sticker work | Supporting reel, Projects directory |
| `docs/inventory/portfolio-inventory.md` | Maintenance checklist and presentation roadmap | Projects directory |
| `audits/thumbnails/portfolio-thumbnail-audit.md` | Visual QA checklist for reel thumbnails and replacement priorities | Projects directory |
| `thumbnail-map.json` | Operational thumbnail source map with artifact/derived/fallback status | Maintenance docs |
| `docs/github/github-repo-sync.md` | GitHub-to-portfolio placement audit and repo classification | Maintenance docs |

## Source Inventory Counts

| Source Folder | Top-Level Count | Website Surface |
|---|---:|---|
| `featured_projects` | 8 | Homepage Featured Reel, Projects Featured Reel, and Projects Directory |
| `supporting projects` | 26 | Projects Supporting Reel and Projects Directory |
| `resume_assets` | 1 | Resume page and Projects Directory |

## Current Architecture

| Layer | Purpose | Notes |
|---|---|---|
| Home | Recruiter-friendly first screen | Surfaces all featured projects in one horizontal reel |
| Featured Reel | Primary project browsing | Matches 8 top-level featured folders |
| Supporting Reel | Breadth and archive browsing | Matches 26 top-level supporting entries |
| Projects Directory | Complete directory | Embedded on Projects so full discovery does not require another page |
| Archive | Backup complete directory | Kept as a direct fallback, not a required navigation step |
| Resume | Credentials and supporting application materials | Includes source resume assets |

## Repository Synchronization Rule

Project pages must be generated from the curated repo inventory, not from memory or partial summaries. Before editing a project page:

1. Enumerate the source folder assets.
2. Classify each major asset by role: summary, presentation, consultation, branding, screenshot, demo, source, or export.
3. Expose, summarize, or intentionally classify each major asset on the page.
4. Keep the inventory and project page in sync when files are added, renamed, or removed.

If multiple PDFs exist in a curated project folder, present them as a structured project package instead of a single-file resource.

## Repository Coverage Rule

Every curated repository item must be visible, classified, indexed, or intentionally excluded. Acceptable coverage paths:

- Featured Reel
- Supporting Reel
- Projects Directory
- dedicated project page
- Resume page
- documented archival/internal classification

The Projects Directory is the main enforcement layer: it should mirror all meaningful top-level curated work even when the homepage stays selective.

## Repository Verification Rule

Repository existence can be verified independently from public linkability. Verification may come from public GitHub URLs, GitHub API visibility, browser-visible repository listings, user confirmation, or local sync records.

Use these states when mapping repos:

- `Public verified`
- `Private verified`
- `Collaborative verified`
- `Pending visibility`
- `Internal`

Do not add public GitHub buttons until the repo is linkable and intended to be public.

## Project Package Standard

Project pages with multiple curated assets should include an asset package section. Asset roles should be explicit:

- summary
- presentation
- consultation
- branding
- screenshot
- demo
- source
- export

## Navigation Hierarchy

Recommended top navigation:

`Projects | Resume | Contact`

Footer navigation:

`About | Projects | Resume | Contact`

This keeps the top nav action-focused. Projects is the single work hub, which reduces the decision point between Projects and Archive.

## Audit Results

| Check | Result |
|---|---|
| Featured projects surfaced | Pass: 8 of 8 |
| Supporting projects surfaced | Pass: 26 of 26 |
| Resume source project surfaced | Pass: 1 of 1 |
| Orphan HTML pages | Pass: none found after audit |
| Broken internal links | Pass |
| Project pages have route back | Pass: nav/footer plus project CTAs |
| Complete directory visible without extra page click | Pass: embedded on `projects.html` |

## Known Presentation Gaps

| Gap | Impact | Priority |
|---|---|---|
| Several projects use generated visual placeholders instead of true screenshots | Reduces credibility | High |
| GitHub links are not final on many project pages | Weakens review path | High |
| Live demos missing for games/apps | Reduces interaction proof | High |
| Design PDFs need stronger thumbnails/mockups | Makes design work less scannable | Medium |
| Data notebooks need chart thumbnails | Makes analytics work less visual | Medium |
| Several cards use original fallback covers instead of true screenshots | Acceptable temporarily, but screenshots will be stronger | Medium |
| Some project pages are thinner than others | Inconsistent depth | Medium |

## Featured vs Supporting Rules

Featured projects should meet most of these:

- Clear problem and outcome
- Strong visual or technical artifact
- Strong relevance to internships/research
- Dedicated page or high-quality external artifact
- Enough evidence to discuss in an interview

Supporting projects can be:

- Smaller but still meaningful
- Coursework that shows skill
- Design/media/code artifacts that show range
- Experimental work that supports the interdisciplinary narrative

Archive entries:

- Everything meaningful, including single-file works
- Utility pages and source assets that need discoverability
- Projects that are less visual but still part of the body of work

## Naming Convention

Use:

- Page slugs: `kebab-case.html`
- Asset folders: `kebab-case`
- Human titles: Title Case
- Source notes: keep original filenames in project pages or inventory when needed

Avoid:

- Multiple public names for the same project
- Unlinked source files
- Raw project assets with no card, archive entry, or explanation
