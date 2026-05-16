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
