# Thumbnail Mapping System Documentation

## Overview

The portfolio uses a **two-tier visual fallback system** to handle thumbnail exports and maintain visual consistency across the reel. This document explains the system, provides the complete asset export workflow, and ensures maintainability for future iterations.

### Key Principle

**Never update `thumbnail-map.json` before hero PNG files exist.** The JSON is the source-of-truth for asset routing; premature updates cause placeholder drift and broken links.

---

## System Architecture

### Tier 1: Hero PNG Exports (Primary)

Real images exported from source projects and placed in `images/thumbnails/` directory.

- **Location**: `images/thumbnails/*.png`
- **Dimensions**: landscape crop, usually 3:2-ish; large enough to stay sharp at card scale
- **Content**: Tight crops of strongest project moments
  - Gameplay screenshots (visual energy)
  - Dashboard/chart results (analytical proof)
  - UI screenshots (product polish)
  - Design system artifacts (process evidence)
- **Status in JSON**: `"status": "artifact"` (real export) or `"derived"` (composite/edited)

### Tier 2: CSS Fallback Visuals (Temporary)

Generated CSS gradients + patterns for design/data/code projects while awaiting PNG exports.

- **Implementation**: `.visual-thumb` divs with themed gradient + pattern
- **Types**:
  - `.ai-thumb`: Radial gradients + accent colors (suggests algorithm/ML)
  - `.design-thumb`: Grid pattern + accent borders (suggests layout/system)
  - `.data-thumb`: Horizontal bar chart visual (suggests analytics/results)
  - `.code-thumb`: Code lines pattern (suggests development)
  - `.creative-thumb`: Organic gradient + texture (suggests media/design)
- **Transition**: Replace with `.thumb` (real `<img>`) as PNG exports complete
- **Status in JSON**: `"status": "fallback"` (CSS-generated visual)

### Routing Logic

For each featured project:

```html
<!-- If PNG exists in images/thumbnails/: -->
<img class="thumb" src="images/thumbnails/protein-ai-pipeline-hero.png" alt="...">

<!-- If PNG not ready: fallback to CSS visual -->
<div class="visual-thumb ai-thumb"><!-- no content needed; styles handle visual --></div>
```

The `thumbnail-map.json` tracks this state per project, enabling atomic updates.

---

## File Structure

```
portfolio-site/
├── images/
│   └── thumbnails/
│       ├── protein-ai-pipeline-hero.png
│       ├── grocery-retail-consumer-hero.png
│       ├── opioid-prescribing-risk-hero.png
│       ├── data-collab-room-logo-system-hero.png
│       └── ...
├── thumbnail-map.json                             (source-of-truth)
├── thumbnail-map-doc.md                           (this file)
├── thumbnail-curation-architecture.md             (priority and crop rules)
├── index.html                                     (featured reel)
├── projects.html                                  (featured + supporting reels)
└── css/styles.css                                 (visual system)
```

---

## Export Workflow

Use this workflow only for replacements that are clearly stronger than the
current thumbnail. See `thumbnail-curation-architecture.md` for the current
priority queue.

1. Choose a repo-owned source artifact: screenshot, chart export, poster crop,
   gameplay capture, UI state, or design-system board.
2. Crop to the strongest landscape proof-point. Remove document borders, large
   empty margins, and title blocks unless they are essential context.
3. Save the image under `images/thumbnails/` using a stable kebab-case filename
   with a `-hero.png` suffix.
4. Verify the image at card scale on `index.html` and `projects.html`.
5. Update `thumbnail-map.json` only after the image exists and loads locally.

---

## Verification & Deployment

### Pre-Deployment Checklist

Before committing, verify:

```bash
# 1. All newly referenced PNG files exist in images/thumbnails/
ls -la images/thumbnails/*.png

# 2. Verify file sizes are reasonable for static deployment
du -sh images/thumbnails/*.png

# 3. Quick visual inspection: open a few in browser/preview
open images/thumbnails/grocery-retail-consumer-hero.png
open images/thumbnails/protein-ai-pipeline-hero.png

# 4. Validate thumbnail-map.json syntax
python3 -m json.tool thumbnail-map.json > /dev/null && echo "Valid JSON"

# 5. Test reel rendering locally
# Open index.html in browser; verify all featured project cards display correctly
# Check for broken images (red X) or CSS fallback visuals still appearing
```

### Atomic Deployment

Update `thumbnail-map.json` and deploy as single commit:

```bash
# 1. Ensure all PNG files are placed in images/thumbnails/
ls -la images/thumbnails/

# 2. Update thumbnail-map.json with verified asset paths
# CRITICAL: only update after files are verified to exist above

# 3. Stage files + JSON atomically
git add images/thumbnails/*.png thumbnail-map.json

# 4. Single atomic commit
git commit -m "Add hero thumbnails for featured reel and update thumbnail-map"

# 5. Push to deployable repo
git push origin main

# 6. Verify deployment
# Open portfolio site live: https://christopherdsbarker.github.io/webpage/
# Test featured reel rendering with new images
```

### Rollback Strategy

If deployment breaks (images missing, JSON error, etc.):

```bash
# 1. Identify the bad commit
git log --oneline | head

# 2. Revert to previous good state
git revert <commit-hash>
git push origin main

# 3. Investigate: check images/thumbnails/ locally, validate JSON, retry
```

---

## Integration with HTML Pages

### Featured Reel (index.html)

Featured projects display hero PNGs via `.project-grid` reel:

```html
<div class="project-grid" data-reel="featured">
  <a href="featured/protein-ai-pipeline.html" class="project-card">
    <!-- Tier 1: Real image -->
    <img 
      class="thumb" 
      src="images/thumbnails/protein-ai-pipeline-hero.png" 
      alt="Protein AI pipeline diagram showing neural network architecture"
    >
  </a>
  
  <!-- Or: CSS fallback for projects awaiting PNG export -->
  <a href="featured/ai-caption-generator.html" class="project-card">
    <div class="visual-thumb ai-thumb" aria-label="AI caption generator interface preview"></div>
  </a>
</div>
```

### Featured Reel (projects.html)

Same system repeated for full `projects.html` featured reel section.

### Fallback Cascade

If a PNG does not exist, do not point an `<img>` at the missing file. Keep the
card on a `.visual-thumb` fallback until the real image is present:

1. Use `<div class="visual-thumb ...">` while the image is pending.
2. Add the PNG to `images/thumbnails/`.
3. Replace the fallback with `<img class="thumb" ...>`.
4. Update `thumbnail-map.json` in the same change.

---

## CSS Architecture

### Thumbnail System Styles (css/styles.css)

```css
/* Real image: PNG from images/thumbnails/ */
.thumb {
  width: 100%;
  height: 260px;
  object-fit: cover;
  object-position: center;
  background: var(--navy-2);
  transition: transform 180ms ease;
}

/* CSS fallback visual for design/data/code awaiting PNG export */
.visual-thumb {
  width: 100%;
  height: 260px;
  padding: 8px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, rgba(5, 7, 12, 0.98), rgba(16, 26, 47, 0.94)), var(--navy);
  transition: transform 180ms ease;
}

/* Type-specific fallback visuals */
.visual-thumb.ai-thumb { /* radial + algorithm suggestion */ }
.visual-thumb.design-thumb { /* grid + layout suggestion */ }
.visual-thumb.data-thumb { /* bars + analytics suggestion */ }
.visual-thumb.code-thumb { /* lines + development suggestion */ }
.visual-thumb.creative-thumb { /* organic + media suggestion */ }
```

### Featured Reel Context

Featured projects display with:
- **Height**: 260px (prominent, recruiter-facing)
- **Aspect**: landscape hero crop, usually close to 3:2
- **Gap**: 10px (tight spacing for visual density)
- **Reel animation**: Horizontal scroll snap (mobile-friendly)

Supporting projects display with:
- **Height**: 204px (secondary, less visual weight)
- **Aspect**: 3:2 (same ratio, smaller absolute size)
- **Gap**: 12px (slightly looser for secondary category)

---

## JSON Structure Reference

### Single Project Entry

```json
{
  "protein-ai-pipeline": {
    "title": "Protein AI Pipeline",
    "thumbnail": "images/thumbnails/protein-ai-pipeline-hero.png",
    "source_asset": "assets/supporting/design/bridging-biology-and-ai-understanding.pdf",
    "status": "derived",
    "next_best_asset": "cleaner pipeline diagram export"
  }
}
```

### Status Values

- `"artifact"`: Real PNG export from project source
- `"derived"`: Composite or edited PNG (e.g., cropped, color-adjusted)
- `"fallback"`: CSS-generated visual (temporary, pending PNG export)
- `"placeholder"`: Hardcoded color fill (minimal visual investment)

### Fallback Visual Types

- `"ai-thumb"`: Radial gradients + ML color palette
- `"design-thumb"`: Grid pattern + accent borders
- `"data-thumb"`: Horizontal bar chart visual
- `"code-thumb"`: Code line pattern
- `"creative-thumb"`: Organic gradient
- `"none"`: No CSS fallback (e.g., real images always available)

---

## Maintenance & Future Iterations

### Quarterly Review

Every 3–4 months, audit featured reel:

```bash
# 1. Check current fallback count
grep '"fallback"' thumbnail-map.json | wc -l

# 2. Spot-check PNG quality and relevance
ls -la images/thumbnails/ | sort -k5 -rn

# 3. Test reel rendering across devices
# Mobile: ensure snap alignment works
# Desktop: ensure scroll behavior is smooth
# Tablet: verify responsive breakpoints

# 4. Update supporting reel with new projects
# Add new design/data/code entries to supporting section
# Use CSS fallback visual until PNG export ready
```

### Asset Refresh Strategy

When project changes or visual updates needed:

```bash
# 1. Export new PNG from updated project
# Use a landscape crop that reads clearly at card scale

# 2. Place in images/thumbnails/ with existing naming convention
# Example: protein-ai-pipeline-hero.png (keep same filename)

# 3. Update thumbnail-map.json entry
# Bump version, update "sourceAsset", keep filename the same

# 4. Single atomic commit
git add images/thumbnails/protein-ai-pipeline-hero.png thumbnail-map.json
git commit -m "Update protein AI pipeline hero with new diagram export"
git push origin main
```

### Documentation Updates

When changing this workflow, update:

1. `thumbnail-curation-architecture.md` — If export priorities or crop rules change
2. `thumbnail-map-doc.md` — This file, if routing or deployment steps change
3. Architectural comments in `css/styles.css` — If visual system changes
4. `README.md` — If high-level governance changes

---

## Quick Reference

### "I just added a new PNG export. How do I deploy?"

1. Verify file exists: `ls images/thumbnails/new-project-hero.png`
2. Check that it is a landscape crop and not oversized for static deployment.
3. Update `thumbnail-map.json` with new entry or modify existing
4. Stage + commit + push:
   ```bash
   git add images/thumbnails/new-project-hero.png thumbnail-map.json
   git commit -m "Add hero thumbnail for new project"
   git push origin main
   ```

### "I want to replace the CSS fallback visual. What do I do?"

1. Export a landscape PNG from project source.
2. Place in `images/thumbnails/` with project-slug naming
3. Change HTML from `<div class="visual-thumb ai-thumb">` to `<img class="thumb" src="...png">`
4. Update `thumbnail-map.json` status to `"artifact"`
5. Deploy atomically

### "The featured reel looks wrong. What's the priority?"

1. Check `images/thumbnails/` — do all PNG files exist?
2. Open browser DevTools → Elements → inspect `.project-card` elements
3. If `.visual-thumb` showing (not `.thumb`), PNG path is wrong or file missing
4. If `.thumb` showing broken (red X), check filename against `thumbnail-map.json`
5. If all images present but styling looks off, review `css/styles.css` `.project-grid` and `.thumb` values

---

## Related Files

- **`thumbnail-map.json`** — Source-of-truth asset routing (ONLY update after PNG files verified)
- **`thumbnail-curation-architecture.md`** — Canonical thumbnail priorities, crop rules, and focal-positioning guidance
- **`css/styles.css`** — Visual system (`.project-grid`, `.thumb`, `.visual-thumb` implementation)
- **`index.html` & `projects.html`** — HTML reel rendering (featured + supporting)

---

## Archive & Historical Context

This system evolved from:
1. **Asset-driven reel** (display whatever files exist)
   → **Curator-driven reel** (display strongest visual moments, substitute fallbacks if needed)

2. **Full poster previews** (100% document coverage)
   → **Hero crop moments** (tight 3:2 highlights, gameplay/results/UI focus)

3. **Placeholder visuals** (solid colors, no design system)
   → **CSS fallback system** (themed gradients + patterns, suggests project type)

The shift from engineering-constrained to curation-constrained means visual selection now drives recruiter perception more than code architecture.

---

**Last Updated**: Current session  
**Maintainer**: Portfolio curation system  
**Questions?** See `thumbnail-curation-architecture.md` or architectural comments in `css/styles.css`
