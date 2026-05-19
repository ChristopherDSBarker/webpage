# Visual QA Rules

These rules govern thumbnail, hero, card, and media presentation.

## Visual QA Goal

Visual QA should improve the portfolio as a recruiter-facing site.

It should catch:

- bad crops
- off-center images
- important content cut off
- unreadable card images
- dark backgrounds where light backgrounds are clearer
- inconsistent padding
- tiny images floating awkwardly
- thumbnails that do not match project identity
- hero images that are too dark or poorly framed
- reel cards that exist but fail at card scale
- full posters, PDFs, or document pages compressed into thumbnails
- thumbnails with no dominant focal idea
- neighboring cards whose visual weight collapses the reel rhythm

The core distinction:

- asset existence means the file resolves and is deployable
- reel readability means the card works during fast recruiter scanning

Do not treat one as proof of the other.

## Reel Composition Rules

A reel card is a hook, recognition cue, and recruiter scan target. It is not a
full project explanation, compressed report, or document archive preview.

Every reel thumbnail should have:

- one focal idea
- one dominant shape or visual cluster
- readable contrast at small scale
- low text density
- a recognizable project identity
- enough breathing room to survive next to neighboring cards

If a reel thumbnail is semantically accurate but visually unreadable at reel
scale, prefer a simpler honest composition.

## Reel Categories

Use these categories for review leads, not automatic redesign:

| Category | Good Reel Composition | Bad Reel Composition |
|---|---|---|
| Gameplay / UI | interaction state, active board, readable app/output moment | entire screen, distant board, empty terminal, tiny UI |
| Diagram / System | one flow, result cluster, model/output relationship | full report, scientific poster compression, unreadable pipeline |
| Artifact / Design | one composition moment, crop with clear hierarchy | full PDF page, full poster, raw publication spread, dense text block |

Intentional fallback cards are allowed when no real evidence exists, but they
should remain clearly marked as fallback review leads until a real screenshot,
output, chart, or artifact-derived crop exists.

## Inspection Rule

Inspect rendered pages or screenshots, not filenames alone.

For page-level visual QA, check:

- homepage
- projects page
- featured reel
- supporting reel
- archive page
- every relevant `featured/*.html` hero
- every relevant `supporting/*.html` hero

Do not stop after homepage/projects when the request includes independent
project pages.

## Mandatory Visual Patch Verification

Deployment-safe validation is required, but it is not visual QA. It only checks
whether references resolve to deployable files.

A visual patch is not complete when the file reference changes.
It is complete only when every affected rendering context has been inspected:
1. homepage/index preview
2. projects reel preview
3. project detail page hero/media section
4. thumbnail-map/reference metadata
5. deploy-safe audit

For thumbnail, hero, card, poster, or media changes, check these contexts
separately:

- homepage/index preview
- `projects.html` reel preview
- individual project detail page hero/media section
- `thumbnail-map.json` and changed references
- deploy/link safety

One asset may work in one context and fail in another. Do not call fixed until
all affected contexts pass.

Run all available relevant audit scripts before reporting success:

- `python3 tools/deployment_safe_audit.py`
- `python3 tools/claimed_vs_exposed_audit.py`
- `python3 tools/semantic_asset_audit.py`
- `python3 tools/semantic_representation_audit.py`
- `python3 tools/semantic_representation_report.py`

If a tool is unavailable, blocked, or fails, report that explicitly. Do not
pretend visual QA passed.

## Visual Patch Report

Every visual patch report must include:

- tools run
- tools not run and why
- pages visually checked
- screenshots or manual evidence used
- changed image assets
- changed references
- deployment audit result

## Thumbnail Selection

Prefer real project artifacts:

1. screenshots
2. gameplay captures
3. UI captures
4. charts/results
5. pipeline diagrams
6. exported design boards
7. logos
8. intentional fallback covers

Use generated or CSS fallback visuals only when no project-specific visual
exists.

## Crop And Background Rules

Use light or white padded backgrounds for logos, marks, and emblem thumbnails
when that improves readability.

Use padded full-context crops for posters, boards, design systems, pipeline
diagrams, and UI screenshots.

Use reel-specific composition crops when the full-context asset becomes dense,
document-like, or poster-like at card scale.

Do not make the crop so tight that the project evidence becomes misleading.

Do not replace strong original visuals with generic or decorative visuals.

## Patch Discipline

Visual QA patches should touch only visual presentation:

- thumbnail image files
- hero image files
- image references
- focal-position CSS
- light/dark presentation classes

Do not rewrite project descriptions, add/remove projects, or restructure the site
during a visual-only pass.
