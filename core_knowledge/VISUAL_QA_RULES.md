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
2. logos
3. posters
4. exported sketches
5. gameplay captures
6. PDF previews
7. notebook visualizations
8. UI captures

Use generated or CSS fallback visuals only when no project-specific visual
exists.

## Crop And Background Rules

Use light or white padded backgrounds for logos, marks, and emblem thumbnails
when that improves readability.

Use padded full-context crops for posters, boards, design systems, pipeline
diagrams, and UI screenshots.

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
