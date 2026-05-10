# Canonical Parity Audit

Date: 2026-05-10

Purpose: reconcile the three portfolio systems:

| System | Purpose |
|---|---|
| `best_works` | canonical source truth |
| `webpage` | deployable presentation layer |
| reels/pages | visible representation |

This audit checks coverage parity, not just file existence.

## Count Reconciliation

| Count Type | Count | Status | Notes |
|---|---:|---|---|
| Canonical featured folders | 8 | Verified | Local best_works folders remain represented. |
| GitHub-backed featured research integration | 1 | Verified | Protein AI Pipeline maps to `Cao-Labs/lutesAI2025/ChrisB`. |
| Canonical supporting folders | 10 | Verified | All represented in supporting reel or directory. |
| Canonical supporting single-file works | 16 | Verified | All represented in supporting reel or directory. |
| Visible project cards on `projects.html` | 35 | Verified | Matches thumbnail mappings exactly. |
| Thumbnail-map project entries | 35 | Verified | 8 featured + 27 supporting. |
| Project directory CSV rows | 36 | Verified with intentional extra | 35 project items + 1 Resume Project row. |
| Featured project pages | 9 | Verified | 8 local featured source folders plus 1 GitHub-backed research integration. |
| Supporting project pages | 7 | Intentional | Package/media/context-heavy supporting works and verified collaborative repo integrations have dedicated pages; smaller works route directly to assets. |
| Deployment-safe references | 0 issues | Verified | `tools/deployment_safe_audit.py` passes. |

## Thumbnail Parity

| Thumbnail Type | Count | Status |
|---|---:|---|
| Artifact-backed | 5 | Verified |
| Derived from repo artifacts | 7 | Verified |
| CSS fallback | 23 | Deployment-safe but semantically weak |

Interpretation:

- Every visible project card has a thumbnail-map entry.
- No thumbnail-map entry points to a missing file.
- Fallback thumbnails are intentional, but not the final artifact-backed ideal.

## Featured Project Parity

| Project ID | Canonical Folder | Visible Reel | Project Page | Thumbnail Map | GitHub Mapping | Status |
|---|---|---:|---:|---:|---|---|
| `opioid-prescribing-risk-analysis` | Yes | Yes | Yes | Yes | Generic profile only | Visible but GitHub unmapped |
| `grocery-retail-consumer-analytics` | Yes | Yes | Yes | Yes | Generic profile only | Visible but GitHub unmapped |
| `minesweeper-game` | Yes | Yes | Yes | Yes | Missing | Visible but semantically weak |
| `battleship-game` | Yes | Yes | Yes | Yes | Missing | Visible but semantically weak |
| `html-resume-portfolio` | Yes | Yes | Yes | Yes | Missing | Visible but semantically weak |
| `ai-caption-generator` | Yes | Yes | Yes | Yes | `pic_caption_app` verified | Parity verified |
| `gan-discord-bot` | Yes | Yes | Yes | Yes | Missing | Visible but semantically weak |
| `data-collab-room-studio` | Yes | Yes | Yes | Yes | Missing / not required | Parity verified |
| `protein-ai-pipeline` | GitHub source | Yes | Yes | Yes | `Cao-Labs/lutesAI2025/ChrisB` verified | Parity verified |

## Supporting Project Parity

| Group | Canonical Items | Visible Representation | Thumbnail Map | Status |
|---|---:|---:|---:|---|
| Design PDFs and package | 6 | 6 | 6 | Parity verified |
| Data and AI studies | 7 | 7 | 7 | Visible but semantically weak due to fallback thumbnails |
| Java / code utilities plus CSCI 367 game systems | 6 | 6 | 6 | CSCI 367 is artifact-backed; smaller code utilities remain semantically weak due to fallback thumbnails |
| Processing sketches | 4 | 4 | 4 | Visible but semantically weak due to fallback thumbnails |
| Media / documentary / campaign / animation / sticker | 5 | 5 | 5 | Parity verified with media-still improvement needed |

## GitHub Parity

| Repo | Portfolio Mapping | Visible UI Integration | Status |
|---|---|---:|---|
| `ChristopherDSBarker/pic_caption_app` | AI Caption Generator | Yes | Parity verified |
| `Cao-Labs/lutesAI2025` | Protein AI Pipeline | Yes | GitHub workstream integrated with contribution framing |
| `matthew-jugovic/train-io` | Derailed candidate | No | GitHub mapped, portfolio source not imported |
| `ChristopherDSBarker/Mabinogi` | Standalone supporting candidate | No | Private/user-confirmed, pending source import |
| `distcrypto/csci367_4` | Supporting technical game project | Yes | Public Git link verified; integrated with repo-backed concept logo and contribution framing |
| `ChristopherDSBarker/WoW-addons` | Supporting/archive candidate | No | Mapped, intentionally not surfaced yet |
| `nsayre01/asset-manager` | Hold | No | Contribution ambiguous |
| `arielbrice/ProgrammingPartyDiscordBot` | Hold | No | Contribution ambiguous |

Interpretation:

- GitHub mappings are intentionally broader than visible UI integrations.
- This is acceptable because the portfolio is curated first, GitHub second.
- New GitHub-backed pages should be added one at a time only after source import and contribution wording are confirmed.
- `Bridging Biology And AI` is now counted as a supporting artifact inside the Protein AI Pipeline page, not as a separate supporting reel identity.

## Detected Drift / Risks

### Metadata Drift

`portfolio-project-directory.csv` has been refreshed against `thumbnail-map.json`.

Current status:

- thumbnail/status drift count: 0
- artifact-backed thumbnails marked `Present`
- PDF-derived thumbnails marked `Present`
- CSS-generated thumbnails marked `Fallback`

`thumbnail-map.json` remains the visual source-of-truth. The CSV is now aligned as the reporting/overview table.

### Fallback Thumbnail Risk

23 thumbnail entries are still CSS fallback rather than repo-derived artifacts.

Status: acceptable for current deployment, but these remain the highest-value future polish targets.

### GitHub Integration Gap

AI Caption Generator, Protein AI Pipeline, and CSCI 367 Game Systems now have verified GitHub links in the UI.

Status: intentional. Additional GitHub integrations require one-at-a-time source import and contribution framing.

### Significance Gap

Count parity does not prove significance parity. A project can be structurally visible but still underrepresented if its implementation depth, repo evidence, resume importance, or recruiter value is stronger than its current visual/page treatment.

The Protein AI Pipeline integration is the example that defines this rule: the repo-backed research implementation had enough evidence to deserve a dedicated featured page rather than remaining implied by a supporting PDF.

## Parity Verdict

Parity is verified at the visibility and deployment level:

- no hidden top-level canonical featured folder
- no hidden top-level canonical supporting folder
- no visible reel item without a thumbnail mapping
- no thumbnail mapping without a visible project identity
- no deploy-broken local-only references

Remaining issues are not structural failures. They are controlled refinement items:

- replace fallback thumbnails with repo-derived screenshots/exports
- integrate GitHub repos surgically after source import
- add stronger project pages only where the source package justifies them
- periodically review whether representation level matches project significance
