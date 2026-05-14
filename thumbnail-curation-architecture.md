# Thumbnail Curation Architecture

This is the canonical operating guide for homepage and projects-page thumbnails.
Keep it practical: thumbnail documentation should help future maintenance, not
preserve AI session history.

## Purpose

Thumbnails are curated proof-points, not scaled document previews. A good reel
visual should show the strongest implementation moment a recruiter can understand
quickly: gameplay, a working UI, a chart cluster, a pipeline diagram, or a
design-system artifact.

## Source Of Truth

- `thumbnail-map.json` records the current thumbnail source and status.
- `images/thumbnails/` contains deployment-safe derived thumbnail assets.
- `css/styles.css` owns shared reel sizing, crop behavior, and project focal
  classes.
- `index.html` and `projects.html` render the featured reel.

Do not update `thumbnail-map.json` before the referenced image exists locally and
has been verified in the browser.

## Current Featured Thumbnail State

| Project | Current Visual | Status | Maintenance Note |
|---|---|---|---|
| Protein AI Pipeline | `images/thumbnails/protein-ai-pipeline-hero.png` | derived | Keep as a tight research-poster crop until a stronger pipeline export exists. |
| Opioid Prescribing Risk Analysis | `images/thumbnails/opioid-prescribing-risk-hero.png` | derived | Keep focused on chart/key-finding density, not the full poster. |
| Grocery Retail Consumer Analytics | `images/thumbnails/grocery-retail-consumer-hero.png` | derived | Keep focused on methods/dashboard proof, not the full vertical poster. |
| Minesweeper Game | CSS gameplay-board cover | fallback | Replace only with a real mid-game screenshot. |
| Battleship Game | CSS board cover | fallback | Replace only with a real gameplay/title-state screenshot. |
| HTML Resume Portfolio | CSS browser cover | fallback | Acceptable fallback unless a clean live portfolio screenshot is available. |
| AI Caption Generator | CSS app cover | fallback | Highest remaining UI replacement target. Use a real upload/result state. |
| GAN Discord Bot | CSS Discord cover | fallback | Replace only with a real bot interaction/output screenshot. |
| Data Collaboration Room Studio | `images/thumbnails/data-collab-room-logo-system-hero.png` | derived | Acceptable logo-system crop; replace only with a stronger master board. |

## Replacement Priority

Prioritize a small number of high-signal replacements. The repo does not need a
large, perfectly governed hero-export program.

1. AI Caption Generator UI screenshot: upload panel plus generated caption output.
2. Branding master board: logo, type, and palette visible in one crop.
3. Gameplay screenshot for any featured game that has a real playable capture.
4. Improved Protein AI diagram crop only if a cleaner pipeline export exists.
5. Improved Grocery/Opioid chart crops only if the current derived crops fail at
   card scale.

Only add a new thumbnail if it is visibly stronger than the current one and is
backed by a real project artifact.

## Crop Rules

- Use a 3:2-ish landscape crop when possible.
- Prefer 1200-1600px width for source exports; avoid huge unoptimized files.
- Remove poster borders, title blocks, footnotes, and empty margins when they
  weaken the card.
- Preserve enough context that the project still reads truthfully.
- Do not fabricate visuals or use stock/generic images.
- Do not add extra frames or device chrome unless the source artifact already
  contains it; the site supplies the card frame.

## CSS Rules

Real image thumbnails use `.thumb`. CSS fallback visuals use `.visual-thumb`.
Project-specific classes should clarify focal intent without becoming a second
documentation system.

Current focal classes:

```css
.thumb.protein-ai-thumb { object-position: center; }
.thumb.opioid-thumb { object-position: center; }
.thumb.grocery-thumb { object-position: center; }
.thumb.ai-caption-thumb { object-position: center 55%; }
.thumb.discord-bot-thumb { object-position: center 60%; }
.thumb.branding-thumb { object-position: center center; }
```

If a derived crop already has the right composition, keep `object-position:
center`. Use vertical percentages only when the source image itself contains more
content than the card should show.

## Deployment Workflow

1. Export or crop the visual into `images/thumbnails/`.
2. Verify the image file opens and reads well at card scale.
3. Update the relevant `index.html` / `projects.html` path if the rendered source
   changes.
4. Update `thumbnail-map.json` to match the actual deployed file.
5. Commit image, HTML/CSS if needed, and JSON together.

Recommended checks:

```bash
python3 -m json.tool thumbnail-map.json > /dev/null
git diff --check
python3 -m http.server 8000
```

Then verify:

- `http://127.0.0.1:8000/index.html`
- `http://127.0.0.1:8000/projects.html`
- each new image path under `images/thumbnails/`

## When To Update This Document

Update this file only when the thumbnail system itself changes:

- featured project thumbnail source changes
- replacement priorities change
- crop rules or focal-positioning rules change
- deployment workflow changes

Do not add session summaries, audit recaps, or conversational reasoning here.
