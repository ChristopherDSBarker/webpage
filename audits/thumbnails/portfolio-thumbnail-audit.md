# Portfolio Thumbnail Audit + CMAPP Refinement Workflow

Goal: refine the portfolio thumbnail system without hallucinating visuals, breaking architecture boundaries, or generating semantically incorrect reel assets.

This document acts as the operational refinement layer between:

- `core_knowledge/`
- `thumbnail-map.json`
- `projects.html`
- homepage thumbnails
- reel presentation behavior
- deploy-safe portfolio visualization

The objective is not infinite thumbnail iteration.

The objective is:

- semantic clarity
- recruiter readability
- visual consistency
- deploy safety
- architecture alignment
- human-reviewable refinement

This audit supports the portfolio. It must never consume the portfolio.

---

# Core Operating Principle

The portfolio is a presentation system, not an AI image generation sandbox.

The AI must:

- represent existing work faithfully
- preserve semantic meaning
- preserve architecture boundaries
- avoid hallucinated visual identity
- avoid replacing strong source artifacts with generic “tech” graphics

If a stronger source-backed screenshot, chart, render, or crop exists:
USE THAT.

Do not generate abstraction over evidence.

---

# Canonical Architecture

## Source Layer (Ground Truth)

`best_works/`
`/Users/songsidiya/Documents/portfolio`

This is the canonical archive/source-of-truth layer.

AI must NEVER:

- overwrite source artifacts
- redesign source projects
- fabricate missing project media
- reinterpret project meaning
- invent screenshots

---

## Knowledge Layer

`core_knowledge/`

Defines:

- visual QA
- semantic representation rules
- architecture boundaries
- anti-hallucination constraints
- thumbnail governance
- deployment safety

AI must derive from this layer.

Never override it.

---

## Deployable Visualization Layer

`webpage/`
`portfolio-site/`

This is the frontend presentation layer.

Allowed AI operations:

- CSS refinement
- mapping refinement
- wire existing human-approved visual references
- document visual consistency issues
- report reel readability issues
- fallback routing
- deploy-safe presentation improvements

AI may audit references, report missing visuals, and wire existing
human-approved assets. AI may not generate, crop, resize, export, restore,
stage, commit, or push thumbnail image files.

---

# Thumbnail Philosophy

A reel thumbnail is:

- a hook
- a recognition cue
- a recruiter scanning aid

It is NOT:

- a compressed report
- a full PDF page
- a document archive
- a presentation slide dump
- a dense poster wall

Good thumbnails survive:

- horizontal scrolling
- rapid scanning
- neighboring visual competition
- reduced scale

---

# Thumbnail Selection Priority

Always use this order:

## Priority 1 — Real Project Evidence

Use:

- gameplay screenshots
- UI screenshots
- notebook charts
- workflow diagrams
- exported renders
- existing project-generated outputs
- design mockups
- posters
- owned still frames

Preferred because they are semantically grounded.

---

## Priority 2 — Human-Approved Derived Assets

AI may wire these only after explicit human visual approval. They are allowed
only if:

- readable at reel scale
- semantically accurate
- visually focused
- not dense document compression

Good examples:

- one chart cluster
- one system flow
- one composition moment
- one gameplay state

Bad examples:

- full PDF page
- entire slide deck
- unreadable scientific poster
- tiny dashboard

---

## Priority 3 — CSS / Generated Fallback

Use ONLY when no project-specific visual exists.

Fallbacks must remain:

- honest
- minimal
- category-specific
- semantically aligned

Fallbacks are temporary placeholders.

They are not final evidence.

---

# Anti-Hallucination Rules

AI must NEVER:

- generate thumbnails from filenames
- infer visuals from project titles alone
- fabricate UI states
- create fake charts
- create fake gameplay
- create fake workflows
- create fake screenshots
- replace evidence with generic AI graphics
- add decorative overlays unrelated to project meaning

If evidence does not exist:

MARK IT AS:

`HUMAN SCREENSHOT NEEDED`

Do not invent the missing artifact.

---

# Reel Visual QA Rules

A reel passes QA only if:

- focal point is readable
- composition survives scaling
- neighboring cards remain distinguishable
- contrast remains readable
- silhouette is recognizable
- category identity is preserved

Reject thumbnails that contain:

- dense unreadable text
- full reports
- tiny charts
- full posters
- weak hierarchy
- distant gameplay
- over-decorated overlays
- generic “dark tech” visual spam

---

# CMAPP Operational Integration

This workflow uses the CMAPP framework to prevent semantic drift.

---

# CONTEXT

Environment:

- recruiter-facing portfolio
- deploy-safe Git workflow
- human-reviewed architecture
- mixed media project categories
- real source-backed artifacts

Operational constraints:

- no hallucinated visuals
- no generated fake screenshots
- no restoring deleted reel assets
- no out-of-scope thumbnail cleanup
- no modifying source archives

---

# MESSAGE

Core message:

The portfolio contains real work and must visually communicate authentic evidence without semantic distortion.

Secondary relational message:

The portfolio demonstrates:

- applied technical ability
- design literacy
- research credibility
- deployment discipline
- visual communication skill

The reel system must reinforce that credibility.

---

# AUDIENCE

## Primary Audience

- recruiters
- hiring managers
- internship reviewers
- frontend/UI evaluators
- technical reviewers

Needs:

- fast readability
- visual distinction
- evidence clarity
- recognizable project identity

---

## Secondary Audience

- professors
- collaborators
- technical peers
- future portfolio reviewers
- the user themself

Needs:

- architecture consistency
- semantic correctness
- audit traceability
- deployment safety

---

# PURPOSE

## Short-Term Purpose

- stabilize thumbnail system
- eliminate broken/missing reel references
- reduce hallucinated refinement passes
- improve recruiter scanning quality

## Long-Term Purpose

- preserve portfolio integrity
- maintain semantic trust
- create scalable presentation architecture
- prevent recursive AI refinement spirals

---

# PRODUCT

This file is:

- an operational refinement document
- an anti-hallucination governance layer
- a deploy-safe thumbnail workflow reference

It is NOT:

- an image-generation directive
- an automated asset replacement system
- a redesign mandate

---

# Current Approved Strategy

## Safe Reel Recovery Rule

If reel assets were deleted due to bad crops:

DO NOT RESTORE THEM.

Instead:

- reuse approved homepage thumbnails
- reuse canonical source assets
- use CSS fallback covers
- mark missing visuals explicitly

---

# Homepage vs Reel Separation

Homepage thumbnails:

- homepage identity
- larger presentation
- curated hook imagery

Reel thumbnails:

- rapid scanning
- compressed readability
- lightweight recognition cues

Do not mix these systems accidentally.

---

# Human Review Trigger Conditions

Require human review when:

- semantic meaning becomes ambiguous
- AI proposes generated imagery
- crop removes core project identity
- thumbnail becomes visually misleading
- multiple unrelated projects begin looking identical
- evidence quality is uncertain

Human review is mandatory before any thumbnail image file is generated, cropped,
resized, exported, restored, staged, committed, or pushed.

---

# NO_REAL_THUMBNAIL Rule

These projects are allowed to temporarily use fallback covers until real evidence exists:

- AI Caption Generator
- GAN Discord Bot
- LLM Bias Detection Classifier
- Stock Market Visualization Analysis
- CORGIS Predictive Data Analysis
- Logistic Regression Analysis
- Decision Tree Analysis
- Neural Network Analysis
- Multiple Regression Analysis
- Spelling Bee Puzzle
- Mountain Terrain Pathfinding
- Image Tool
- Abstract Art
- Regex Pattern Analyzer
- Processing Visual Experiment
- Array Visualization Study
- Animal Function Animation
- Random Circles Generator

These are NOT failures.

These are controlled placeholders.

---

# Refinement Stop Rule

STOP thumbnail refinement once:

- every card has a valid visual
- no card feels broken
- categories remain distinguishable
- reel scans cleanly
- mappings remain explicit
- architecture remains stable

Beyond this point:

additional refinement is optional polish only.

Do not enter infinite thumbnail iteration loops.

---

# Common AI Failure Modes

## Failure Mode 1 — Decorative Overload

Symptoms:

- circles
- nodes
- glowing overlays
- abstract “AI” graphics
- repeated dark-tech visuals

Result:

projects blur together semantically.

Fix:

return to source-backed evidence.

---

## Failure Mode 2 — Full Poster Compression

Symptoms:

- unreadable posters
- dense PDF previews
- tiny charts

Result:

visual collapse at reel scale.

Fix:

extract one focal composition moment.

---

## Failure Mode 3 — Semantic Drift

Symptoms:

- unrelated thumbnails
- fake screenshots
- misleading visuals
- wrong project identity

Fix:

re-anchor to:

- source archive
- core_knowledge
- canonical media

---

## Failure Mode 4 — Recursive Governance Explosion

Symptoms:

- audit of audits
- governance layers multiplying
- documentation consuming project work

Fix:

improve actual visuals instead.

---

# Deployment Safety Rules

NEVER:

- use `git add .`
- restore deleted reel crops automatically
- modify source archive folders
- change project meaning during thumbnail work
- mix homepage + reel + hero refinement together
- invent replacement media

ALWAYS:

- isolate presentation-layer changes
- validate paths
- preserve architecture boundaries
- prefer source-backed evidence
- keep changes human-reviewable

---

# Final Operational Rule

The portfolio already contains strong work.

The refinement layer exists to:

- clarify
- preserve
- organize
- present

NOT to reinvent the portfolio.

Stop optimizing once the reel communicates clearly.
