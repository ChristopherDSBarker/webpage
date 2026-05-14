# Hero Asset Replacement Audit: Source Images vs. CSS Fixes

## Executive Summary

**The Problem**: Current thumbnails are full poster images shrunk to card size. CSS focal positioning is a structural improvement but cannot fix the fundamental issue: **the source assets are wrong for hero usage**.

**The Realization**: Recruiters see tiny, unreadable charts; weak visual hierarchy; excessive whitespace. CSS padding/object-fit/border-radius won't fix this because the poster itself contains the problem.

**The Solution**: Replace full posters with intentionally curated **hero crops** that:
- Show strongest implementation moment (not entire document)
- Communicate visual proof-point immediately (not require zooming)
- Remove excess whitespace and margins
- Emphasize recruiter-facing value (charts, UI, gameplay, identity)

---

## Current Asset Inventory & Issues

### 1. Protein AI Pipeline
**Current Asset**: `images/thumbnails/bridging-biology-and-ai-understanding.png`
- **Type**: Full research poster
- **Issue**: Entire poster scaled down → diagram illegible
- **Visual Problem**: Title block, margins, multiple sections → weak focal hierarchy

**What Recruiters See**:
- Tiny, unreadable pipeline diagram
- Too much whitespace
- No immediate proof-point visibility

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/protein-ai-hero.png`
- **Crop Strategy**: Central pipeline diagram ONLY
- **Content Focus**: ESM-3 → BLIP-2 → GO Similarity flow visualization
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Pipeline flows, node connections, method callouts
- **Expected Source**: PDF diagram page or exported pipeline visualization
- **Priority**: **HIGH** — strong AI research proof-point if visible

---

### 2. Opioid Prescribing Risk Analysis
**Current Asset**: `images/opioid-prescribing-risk-poster.PNG` (864×1296 px)
- **Type**: Full analysis poster (very tall, narrow)
- **Issue**: Entire poster scaled down → charts become invisible spec
- **Visual Problem**: Title, multiple chart sections, legend blocks → unreadable

**What Recruiters See**:
- Illegible bars and lines
- No data insight visible
- Weak visual proof of analytics work

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/opioid-hero.png`
- **Crop Strategy**: Chart cluster region ONLY (ML models, provider maps, risk metrics)
- **Content Focus**: Model performance comparison, geographic analysis, top charts
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Primary analysis charts (skip title, legend, margins)
- **Expected Source**: Crop from poster middle section (0–60% vertical)
- **Priority**: **HIGH** — data visualization proof critical for analytics credibility

---

### 3. Grocery Retail Consumer Analytics
**Current Asset**: `images/grocery-retail-consumer-poster.png` (3300×5100 px — extremely tall)
- **Type**: Full dashboard poster (massive vertical ratio)
- **Issue**: When scaled to 260px height, becomes 170px wide → completely unreadable
- **Visual Problem**: Dashboard grid, multiple panels, charts → indecipherable at thumbnail size

**What Recruiters See**:
- Essentially a solid color block
- No visual information communicates
- Zero dashboard comprehension

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/grocery-hero.png`
- **Crop Strategy**: Dashboard visualization cluster (skip title, skip bottom margin)
- **Content Focus**: Consumer analytics graphs, retail insights, key metrics
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Middle dashboard panel (30–70% of poster vertical)
- **Expected Source**: Crop from poster center (skip top 30%, skip bottom 30%)
- **Priority**: **CRITICAL** — most broken current visual; must replace

---

### 4. Minesweeper Game
**Current Asset**: CSS fallback `game-thumb` (abstract game board)
- **Type**: CSS-generated visual
- **Issue**: Abstract fallback; no actual gameplay visible
- **Visual Problem**: Placeholder pattern, not real game UI

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/minesweeper-hero.png`
- **Crop Strategy**: Live gameplay screenshot (mid-game state)
- **Content Focus**: Tile board with revealed numbers, flags, playable state
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Game board centered, UI controls visible (optional)
- **Expected Source**: Screenshot from actual game at localhost
- **Priority**: **MEDIUM** — CSS fallback adequate but real screenshot stronger

---

### 5. Battleship Game
**Current Asset**: CSS fallback `game-thumb` (abstract game board)
- **Type**: CSS-generated visual
- **Issue**: Abstract fallback; no actual game state visible
- **Visual Problem**: Placeholder grid, not gameplay

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/battleship-hero.png`
- **Crop Strategy**: Live gameplay screenshot (mid-game with hits/misses/ships visible)
- **Content Focus**: Game board with strategic state (ships, hit markers, miss markers)
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Game board + player stats visible
- **Expected Source**: Screenshot from actual game at localhost
- **Priority**: **MEDIUM** — CSS fallback adequate; real game screenshot preferred

---

### 6. HTML Resume Portfolio
**Current Asset**: CSS fallback `web-thumb` (abstract browser frame)
- **Type**: CSS-generated visual
- **Issue**: Abstract fallback; no actual portfolio UI visible
- **Visual Problem**: Placeholder browser mockup

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/html-resume-hero.png`
- **Crop Strategy**: Live website screenshot (hero section + featured content)
- **Content Focus**: Homepage hero grid, featured project reel, visual hierarchy
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Hero section + partial featured reel visible
- **Expected Source**: Screenshot from actual portfolio at localhost or live
- **Priority**: **MEDIUM** — CSS fallback acceptable; real website screenshot shows skill

---

### 7. AI Caption Generator
**Current Asset**: CSS fallback `ai-thumb` (abstract interface mockup)
- **Type**: CSS-generated visual
- **Issue**: Abstract fallback; no actual UI or results visible
- **Visual Problem**: Placeholder shapes, not working app

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/ai-caption-hero.png`
- **Crop Strategy**: Live app screenshot (upload panel + generated caption result)
- **Content Focus**: Input image, generated caption output, vibe selection UI
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Full working app state (upload + result side-by-side or stacked)
- **Expected Source**: Screenshot from actual deployed app or local demo
- **Priority**: **CRITICAL** — CSS placeholder is very weak; real app screenshot transforms perception

---

### 8. GAN Discord Bot
**Current Asset**: CSS fallback `discord-thumb` (abstract Discord frame)
- **Type**: CSS-generated visual
- **Issue**: Abstract fallback; no actual bot interaction or generated image visible
- **Visual Problem**: Placeholder mockup, not real bot usage

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/gan-discord-hero.png`
- **Crop Strategy**: Discord screenshot (bot message + generated image visible)
- **Content Focus**: Command invocation, generated AI image output, bot interaction proof
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Bot message + generated image (crop to show bot value)
- **Expected Source**: Screenshot from actual Discord usage or test server
- **Priority**: **CRITICAL** — CSS placeholder is weak; real bot interaction screenshot shows AI capability

---

### 9. Data Collaboration Room Studio
**Current Asset**: `images/thumbnails/data-collab-room-logo-system.png`
- **Type**: Branding/design system PDF preview (abstract)
- **Issue**: Abstract logo blocks; no actual design system or studio work visible
- **Visual Problem**: Weak branding visual; doesn't communicate design leadership

**Needed Hero Crop**:
- **Filename**: `images/thumbnails/branding-hero.png`
- **Crop Strategy**: Master logo + typography system (full design system hero moment)
- **Content Focus**: Logo variations, type scales, color palette, system coherence
- **Dimensions**: 1600×1067 px (3:2 hero aspect)
- **Focal Region**: Strongest branding moment (logo center, type/color context visible)
- **Expected Source**: PDF design system page or exported branding guide
- **Priority**: **HIGH** — branding weak currently; strong design system export elevates perception

---

## Priority Export Roadmap

### **Priority 1: Fixes Worst Visuals** (Immediate ROI)
1. **Grocery Analytics** — Currently most broken (tiny 170px when scaled)
   - Source: Crop from poster center region
   - Output: `images/thumbnails/grocery-hero.png`
   - Impact: Transforms invisible placeholder into readable dashboard

2. **AI Caption Generator** — CSS placeholder very weak
   - Source: Screenshot from working app
   - Output: `images/thumbnails/ai-caption-hero.png`
   - Impact: Real UI >> abstract mockup

### **Priority 2: High Impact** (Strong Proof-Points)
3. **Protein AI Pipeline** — Research diagram currently unreadable
   - Source: Crop from poster diagram section
   - Output: `images/thumbnails/protein-ai-hero.png`
   - Impact: AI research work becomes visible

4. **Opioid Analysis** — Charts currently illegible
   - Source: Crop from poster chart cluster
   - Output: `images/thumbnails/opioid-hero.png`
   - Impact: Data visualization proof becomes apparent

5. **GAN Discord Bot** — CSS placeholder weak
   - Source: Discord screenshot with bot + generated image
   - Output: `images/thumbnails/gan-discord-hero.png`
   - Impact: AI capability + bot interaction visible

### **Priority 3: Gameplay/Branding** (Supporting)
6. **Data Collab Room (Branding)** — Design leadership proof
   - Source: Design system PDF export
   - Output: `images/thumbnails/branding-hero.png`
   - Impact: Elevates design credibility

7. **Minesweeper Gameplay** — Game logic proof
   - Source: Live game screenshot
   - Output: `images/thumbnails/minesweeper-hero.png`
   - Impact: Game dev portfolio proof

8. **Battleship Gameplay** — Game dev proof
   - Source: Live game screenshot
   - Output: `images/thumbnails/battleship-hero.png`
   - Impact: OOP + game systems visible

---

## Export Strategy: From Full Poster to Hero Crop

### Example: Grocery Analytics (3300×5100 px poster → 1600×1067 px hero crop)

**Current Problem**:
```
Poster dimensions: 3300×5100 px (very tall, wide)
Thumbnail display: 260px height
→ Actual render width: 260px × (3300/5100) = 169px
→ Unreadable at this scale
```

**Solution**:
```
1. Identify dashboard region in poster (typically 30–70% vertical)
2. Crop to 3:2 aspect (1600×1067 equivalent)
3. Export as hero PNG to images/thumbnails/grocery-hero.png
4. Update thumbnail-map.json to reference new asset
```

**ImageMagick Example** (replace actual coordinates):
```bash
convert images/grocery-retail-consumer-poster.png \
  -crop 3300x3000+0+1500 \
  -resize 1600x1067 \
  images/thumbnails/grocery-hero.png
```

---

## Verification Checklist (After Each Export)

- [ ] File placed in `images/thumbnails/` with correct hero filename
- [ ] Dimensions are 1600×1067 px (3:2 aspect)
- [ ] Content is visually clear at 260px display height
- [ ] Focal region is prominent (no excessive margins)
- [ ] Recruiter-facing proof-point is immediately recognizable
- [ ] File size is optimized (8–15 KB typical)
- [ ] No placeholder abstraction remains
- [ ] Image is truthful representation of actual project

---

## CSS Integration (Already In Place)

Each featured project now has:
- **Focal positioning class** (e.g., `.protein-ai-thumb`)
- **object-position anchor** (e.g., `center 35%`)
- **Ready for PNG replacement** when hero crop exported

**Example HTML** (already applied):
```html
<img class="thumb protein-ai-thumb" src="images/thumbnails/protein-ai-hero.png" alt="...">
```

**Example CSS** (already applied):
```css
.thumb.protein-ai-thumb {
  object-position: center 35%;
}
```

When `protein-ai-hero.png` is placed in `images/thumbnails/`, the system immediately uses the real hero crop instead of the full poster.

---

## Updated Timeline

**Phase 1: Asset Exports** (User/Designer)
- Export 9 hero crops following export strategy
- Place in `images/thumbnails/` with hero filenames
- Verify each locally at 260px display height

**Phase 2: Atomic Deployment** (Already prepared)
- Update `thumbnail-map.json` to reference hero filenames
- Commit `images/thumbnails/*-hero.png` + JSON update together
- Deploy in single commit (no incremental updates)

**Phase 3: Verification**
- Check live site — all thumbnails display as hero visuals
- Verify no broken image references
- Confirm focal positioning working correctly

---

## Key Insight

**CSS Focal Positioning** ≠ Asset Fix

- ✅ CSS adjustment: Helps *where hero content exists*
- ❌ CSS cannot: Create missing hero content

**Current State**:
- ✅ CSS is ready: Focal positioning architecture in place
- ❌ Assets are wrong: Full posters, not hero crops
- 🔄 **Bottleneck**: Curated hero asset exports

**Next Step**: Generate 9 hero crop exports; deploy atomically with JSON update.

---

## References

- `thumbnail-curation-architecture.md` — Focal positioning system (CSS complete)
- `thumbnail-map.json` — Ready for hero filenames
- `css/styles.css` — Project-specific focal classes applied
- `projects.html` — Classes applied, awaiting hero PNGs
- `index.html` — Classes applied, awaiting hero PNGs
