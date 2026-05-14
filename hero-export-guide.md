# Hero Asset Export Guide: From Full Posters to Curated Crops

## Quick Reference: What Each Featured Project Needs

### The Format
Each hero export should be:
- **Dimensions**: 1600×1067 px (3:2 aspect ratio)
- **Format**: PNG, optimized to 8–15 KB
- **Location**: `images/thumbnails/{project}-hero.png`
- **Display Height**: 260px (will scale responsively)
- **Content**: Strongest implementation moment only (no full poster)

---

## Export Specifications by Project

### 1. Grocery Retail Consumer Analytics
```
Current File: images/grocery-retail-consumer-poster.png
Current Size: 3300×5100 px (EXTREMELY tall, nearly unreadable at thumbnail scale)
Problem: Dashboard invisible when scaled to card size

Export Name: images/thumbnails/grocery-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Consumer analytics dashboard visualizations
  - Key metric displays
  - Chart components
  - Retail insights synthesis
Content to Exclude:
  - Title block
  - Top margins/padding
  - Bottom margins/legend
  - Navigation UI
Crop Strategy:
  - Source: Middle 40% of poster (skip top title, skip bottom)
  - Focus: Dashboard grid and main visualizations
  - Aspect: Landscape (wider than tall)

Why This: At 260px display height, full poster becomes 170px wide (illegible).
Hero crop shows readable dashboard @ 260px.

Current CSS Focal Positioning Applied:
  .thumb.grocery-thumb { object-position: center 45%; }
```

---

### 2. AI Caption Generator
```
Current File: CSS fallback (abstract mockup)
Current Visual: abstract shapes (.ai-thumb fallback)
Problem: No actual UI visible; appears as abstract placeholder

Export Name: images/thumbnails/ai-caption-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Upload file input panel
  - Generated caption text result
  - Vibe/mood selector UI
  - App working state (not mockup)
Content to Exclude:
  - Empty states
  - Loading spinners (unless key feature)
  - Incomplete workflows
  - Error states
Crop Strategy:
  - Source: Screenshot of working app (full interface visible)
  - Focus: Both upload input AND caption result visible
  - Aspect: Landscape composition showing flow

Why This: Real app screenshot >> abstract CSS mockup. Transforms perception
from "placeholder" to "real working tool."

Current CSS Focal Positioning Applied:
  .thumb.ai-caption-thumb { object-position: center 55%; }

Source Location: 
  - Deployed app or local demo at `assets/ai-caption/`
  - Screenshot showing upload + results
```

---

### 3. Protein AI Pipeline
```
Current File: images/thumbnails/bridging-biology-and-ai-understanding.png
Current Size: Full research poster
Problem: Diagram unreadable when entire poster is shrunk to thumbnail

Export Name: images/thumbnails/protein-ai-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Central pipeline diagram
  - ESM-3 embeddings step
  - BLIP-2 caption generation step
  - GO similarity evaluation step
  - Flow connections and arrows
Content to Exclude:
  - Title block/header
  - References section
  - Bottom margins
  - Method legends (unless essential)
Crop Strategy:
  - Source: Crop poster to pipeline diagram only (roughly center 50%)
  - Focus: All three pipeline stages visible
  - Aspect: Landscape composition

Why This: Research proof-point. Pipeline diagram immediately communicates
AI methodology sophistication.

Current CSS Focal Positioning Applied:
  .thumb.protein-ai-thumb { object-position: center 35%; }

Source Location:
  - `assets/featured/ai-caption-generator/` or
  - `assets/supporting/design/bridging-biology-and-ai-understanding.pdf`
```

---

### 4. Opioid Prescribing Risk Analysis
```
Current File: images/opioid-prescribing-risk-poster.PNG
Current Size: 864×1296 px (narrow, tall poster)
Problem: Charts become invisible spec when scaled down

Export Name: images/thumbnails/opioid-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - ML model performance charts
  - Provider distribution maps
  - Risk score visualizations
  - Key analytics metrics
Content to Exclude:
  - Title/methodology sections
  - Bottom legend/references
  - Empty margins
  - Secondary analysis notes
Crop Strategy:
  - Source: Upper-to-middle poster region (0–60% vertical)
  - Focus: Chart cluster visible at readable size
  - Aspect: Landscape (wider than current narrow poster)

Why This: Data visualization proof. Charts become readable at 260px display
height, immediately communicating analytics capability.

Current CSS Focal Positioning Applied:
  .thumb.opioid-thumb { object-position: center 25%; }

Source Location:
  - `images/opioid-prescribing-risk-poster.PNG` (crop relevant section)
  - Or regenerate from `assets/opioid/Project2.ipynb`
```

---

### 5. GAN Discord Bot
```
Current File: CSS fallback (abstract Discord frame)
Current Visual: abstract shapes (.discord-thumb fallback)
Problem: No actual bot interaction or generated image visible

Export Name: images/thumbnails/gan-discord-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Discord chat interface
  - Bot command invocation
  - Generated AI image output
  - Bot interaction in action
Content to Exclude:
  - Error messages
  - Loading states
  - Incomplete generations
  - Empty channel context
Crop Strategy:
  - Source: Discord screenshot showing bot + image
  - Focus: Generated image prominently visible
  - Aspect: Landscape showing full interaction flow

Why This: AI capability proof. Real Discord screenshot + generated image
immediately communicates bot functionality and AI integration.

Current CSS Focal Positioning Applied:
  .thumb.discord-bot-thumb { object-position: center 60%; }

Source Location:
  - Discord server screenshot (test bot interaction)
  - Or generate from deployment demo
```

---

### 6. Data Collaboration Room Studio (Branding)
```
Current File: images/thumbnails/data-collab-room-logo-system.png
Current Visual: abstract logo blocks
Problem: Weak branding communication; doesn't show design system strength

Export Name: images/thumbnails/branding-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Master logo design
  - Logo variations
  - Typography system samples
  - Color palette
  - Design system coherence
Content to Exclude:
  - Full PDF grid/guides
  - Hidden construction details
  - Empty space
  - Secondary applications
Crop Strategy:
  - Source: PDF design system page (or exported screenshot)
  - Focus: Logo + type + color visible together
  - Aspect: Landscape showing system wholeness

Why This: Design leadership proof. Shows not just logo but entire design
system thinking.

Current CSS Focal Positioning Applied:
  .thumb.branding-thumb { object-position: center center; }

Source Location:
  - `assets/featured/data-collab-room-studio/` design files
  - Or PDF design system page
```

---

### 7. Minesweeper Game
```
Current File: CSS fallback (abstract game board)
Current Visual: CSS-generated mine grid (.game-thumb fallback)
Problem: Abstract placeholder; no actual gameplay context

Export Name: images/thumbnails/minesweeper-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Live game board in mid-game state
  - Revealed tiles with numbers
  - Flag placements visible
  - Interaction state evident
Content to Exclude:
  - Game over states
  - New game (unrevealed board)
  - UI controls only (need board)
Crop Strategy:
  - Source: Gameplay screenshot at mid-game
  - Focus: Game board prominent, playable state clear
  - Aspect: Landscape with UI visible

Why This: Game dev portfolio proof. Real gameplay screenshot communicates
interaction capability and game logic.

Current CSS Focal Positioning Applied:
  .game-thumb { (already centered, adequate as fallback) }

Source Location:
  - Screenshot from `featured/minesweeper-game.html` (localhost)
  - Or deployed game instance
```

---

### 8. Battleship Game
```
Current File: CSS fallback (abstract game board)
Current Visual: CSS-generated battle grid (.game-thumb fallback)
Problem: Abstract placeholder; no actual game state visible

Export Name: images/thumbnails/battleship-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Game board with strategic state
  - Ships placed/visible
  - Hit markers visible
  - Miss markers visible
  - Player stats evident
Content to Exclude:
  - Game setup screens
  - Empty board (unrevealed)
  - Menu UI only
Crop Strategy:
  - Source: Gameplay screenshot mid-battle
  - Focus: Board grid + ship state + stats visible
  - Aspect: Landscape showing game state

Why This: OOP + game systems proof. Real game board shows Java
implementation and strategic game design.

Current CSS Focal Positioning Applied:
  .game-thumb { (already centered, adequate as fallback) }

Source Location:
  - Screenshot from `featured/battleship-game.html` (localhost)
  - Or deployed game instance
```

---

### 9. HTML Resume Portfolio
```
Current File: CSS fallback (abstract browser frame)
Current Visual: CSS-generated browser mockup (.web-thumb fallback)
Problem: Abstract placeholder; no actual website UI visible

Export Name: images/thumbnails/html-resume-hero.png
Dimensions: 1600×1067 px (3:2)
Content to Show:
  - Homepage hero section
  - Partial featured project reel
  - Navigation visible
  - Visual hierarchy evident
Content to Exclude:
  - Scroll position (show hero + reel start)
  - Empty states
  - Loading states
Crop Strategy:
  - Source: Website screenshot (hero + featured reel top)
  - Focus: Hero text + first few featured projects visible
  - Aspect: Landscape showing portfolio layout

Why This: Web dev portfolio proof. Real website screenshot
communicates design taste and development capability.

Current CSS Focal Positioning Applied:
  .web-thumb { (already centered, adequate as fallback) }

Source Location:
  - Screenshot from `index.html` (localhost:8003)
  - Or live deployed site at christopherdsbarker.github.io
```

---

## Practical Workflow: Export One Hero Crop

### Example: Grocery Analytics

**Step 1: Get the Source**
```bash
# Find current poster
ls -la images/grocery-retail-consumer-poster.png
# Output: 3300×5100 px
```

**Step 2: Identify Crop Region**
```
Full poster: 3300×5100 px (very tall)
Dashboard region: approximately 30–70% vertical
Calculation: 
  - Skip top 1530 px (30% of 5100)
  - Keep middle 2550 px (40% of 5100)
  - Skip bottom 1020 px (30% of 5100)
Result crop: 3300×2550 px starting at y=1530

Resize to hero:
  3300×2550 → 1600×1067 px (maintains aspect)
```

**Step 3: Use ImageMagick** (if available)
```bash
convert images/grocery-retail-consumer-poster.png \
  -crop 3300x2550+0+1530 \
  -resize 1600x1067 \
  -quality 85 \
  images/thumbnails/grocery-hero.png
```

**Step 4: Or Use Graphic Editor**
- Open grocery poster in Photoshop/GIMP
- Select region: 30–70% vertical (middle 40% of height)
- Crop to that region
- Resize to 1600×1067 px
- Export as PNG
- Save to `images/thumbnails/grocery-hero.png`

**Step 5: Optimize**
```bash
# Make sure file size is reasonable (8–15 KB typical)
ls -lh images/thumbnails/grocery-hero.png
# If too large: re-export with higher JPEG compression
```

**Step 6: Verify Locally**
```bash
# Open localhost:8003/projects.html in browser
# Find Grocery project card
# Verify: hero crop shows readable dashboard (not shrunk poster)
# Verify: focal positioning working (grocery-thumb class applied)
```

---

## Deployment: After All 9 Exports Are Ready

**Step 1: Verify All Files Present**
```bash
ls -lh images/thumbnails/*-hero.png
# Should show 9 files:
# grocery-hero.png
# ai-caption-hero.png
# protein-ai-hero.png
# opioid-hero.png
# gan-discord-hero.png
# branding-hero.png
# minesweeper-hero.png
# battleship-hero.png
# html-resume-hero.png
```

**Step 2: Update thumbnail-map.json**
```json
{
  "featured": {
    "grocery-retail-consumer-analytics": {
      "title": "Grocery Retail Consumer Analytics",
      "thumbnail": "images/thumbnails/grocery-hero.png",
      "source_asset": "curated hero crop",
      "status": "artifact"
    },
    "ai-caption-generator": {
      "title": "AI Caption Generator",
      "thumbnail": "images/thumbnails/ai-caption-hero.png",
      "source_asset": "app screenshot",
      "status": "artifact"
    },
    // ... etc for remaining 7
  }
}
```

**Step 3: Verify Locally @ 260px**
```bash
# Open localhost:8003
# Check projects.html featured reel
# Verify:
#   - All 9 cards display hero crops (not posters)
#   - Focal positioning working
#   - No broken image references
#   - Visual hierarchy clear
#   - Recruiter-facing proof-points visible
```

**Step 4: Atomic Deployment**
```bash
cd portfolio-site
git add images/thumbnails/*-hero.png
git add thumbnail-map.json
git commit -m "Add curated hero thumbnails and update thumbnail-map"
git push origin main
```

**Step 5: Verify Live**
```
Check: christopherdsbarker.github.io
Verify all thumbnails deployed correctly
Confirm no broken references
Success!
```

---

## Quality Checklist for Each Export

- [ ] File is 1600×1067 px (3:2 aspect ratio)
- [ ] Content is readable at 260px display height
- [ ] Hero moment is prominent (no wasted margins)
- [ ] Focal region makes sense (charts visible, title removed, etc.)
- [ ] File size is optimized (8–15 KB)
- [ ] File placed in `images/thumbnails/` with correct name
- [ ] PNG format, not JPEG
- [ ] No placeholder abstractions (real asset, not CSS fallback)
- [ ] Truthfully represents project (not fabricated)
- [ ] Matches project description and proof-point

---

## CSS Classes Now Active

Each featured project has these classes ready to receive hero PNG exports:

```css
.thumb.protein-ai-thumb { object-position: center 35%; }
.thumb.opioid-thumb { object-position: center 25%; }
.thumb.grocery-thumb { object-position: center 45%; }
.thumb.ai-caption-thumb { object-position: center 55%; }
.thumb.discord-bot-thumb { object-position: center 60%; }
.thumb.branding-thumb { object-position: center center; }
```

When `images/thumbnails/{project}-hero.png` is placed, the system
automatically uses the real hero crop instead of falling back to CSS.

---

## Reference Documentation

- `thumbnail-curation-architecture.md` — System design and philosophy
- `hero-asset-replacement-audit.md` — Detailed issues and priority roadmap
- `HERO-SYSTEM-SUMMARY.md` — Complete summary of what's ready and what's needed
- `thumbnail-map-doc.md` — Complete workflow documentation

All CSS is deployed. All HTML classes applied.

**Only missing**: 9 hero crop exports.
