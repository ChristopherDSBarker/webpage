# Adversarial No-Hallucination Audit

Date: 2026-05-10

Purpose: verify semantic correctness after deployment-safe synchronization. This audit separates deployable correctness from content truth. A page can pass deployment checks and still be semantically weak, under-evidenced, visually mismatched, or contribution-ambiguous.

## Machine Checks

Command:

```bash
python3 tools/deployment_safe_audit.py
```

Result:

- Missing references: 0
- Ignored-file references: 0
- Untracked references: 0

Additional checks:

- `thumbnail-map.json` non-fallback image paths resolve.
- Public project GitHub links currently used by AI Caption Generator, Protein AI Pipeline, and CSCI 367 Game Systems resolve.

## Featured Reel Semantic Audit

| Project | Status | Notes |
|---|---|---|
| Opioid Prescribing Risk Analysis | Verified | Thumbnail and page use repo-backed poster/charts. Raw CSVs are source-archive only and no longer linked as deployable assets. |
| Grocery Retail Consumer Analytics | Verified | Thumbnail and page use repo-backed poster/visualization. Raw dataset CSV is source-archive only and no longer linked as deployable asset. |
| Data Collaboration Room Studio | Verified | Uses real logo-system PDF preview and exposes the 4-PDF project package. |
| AI Caption Generator | Deployment-safe but semantically weak | GitHub repo link resolves and source files are exposed. Thumbnail is still CSS fallback; needs app screenshot/output capture for artifact-backed identity. |
| Minesweeper Game | Deployment-safe but semantically weak | Source files and tile assets exist. Thumbnail is CSS fallback based on gameplay concept; needs real gameplay screenshot or deployed demo capture. |
| Battleship Game | Deployment-safe but semantically weak | JAR/write-up are exposed. Thumbnail is CSS fallback; needs gameplay screenshot or title screen. |
| HTML Resume Portfolio | Deployment-safe but semantically weak | Original HTML/CSS are exposed. Thumbnail is CSS fallback; needs browser/responsive screenshot. |
| GAN Discord Bot | Deployment-safe but semantically weak | Source code is exposed. Thumbnail is CSS fallback; needs output screenshot, README, or bot interaction capture. |

## Supporting Reel Semantic Audit

| Group | Status | Notes |
|---|---|---|
| Design PDFs | Verified | PDF-derived thumbnails and direct/project-page routes match canonical artifacts. |
| Package Series Design | Verified | Project page exposes both canonical PDFs; source-folder wording corrected to `supporting projects/package-series-design`. |
| SiDiYa Branding System | Verified | Dedicated page exposes the identity system as portfolio-relevant branding work and uses the authentic emblem artifact powering the website brand layer. |
| Wang Center Collab Sticker | Verified | Uses actual image artifact and dedicated page. |
| Animated Short Scene | Verified | Uses actual GIF artifact. |
| Protein AI Pipeline | Verified integration | Featured page links the Cao Labs `lutesAI2025` `ChrisB` folder/workstream and uses the Bridging Biology And AI PDF as a supporting research communication artifact. |
| Data notebook studies | Deployment-safe but semantically weak | Notebook routes are valid, but thumbnails are CSS fallbacks rather than actual chart exports. |
| Java/code projects | Deployment-safe but semantically weak | Source routes are valid, but thumbnails are CSS fallbacks rather than rendered outputs/screenshots. |
| Processing sketches | Deployment-safe but semantically weak | PDE routes are valid, but thumbnails are CSS fallbacks rather than exported sketch frames. |
| Regex Pattern Analyzer | Partial source exposure | Dedicated presentation page exists. ZIP bundles are intentionally source-archive only; page summarizes the package rather than deploying raw archive bundles. |
| CSCI 367 Game Systems | Verified integration | Supporting page uses repo-backed `conceptlogo.png`, links the verified public Git repo, and frames the lead/main implementation role as user-confirmed on a collaborative project. No gameplay screenshot or copyrighted art is fabricated. |
| BJUG Day Campaign | User-confirmed / source-archive video | Canonical folder contains MP4; webpage uses YouTube-hosted media to avoid large deployable video. Needs owned still frame if artifact-backed thumbnail is required. |
| Community Documentary Media | User-confirmed / source-archive video | Canonical folder contains MP4; webpage uses YouTube-hosted media and user-provided context. Award/exhibit/deputy-mayor details should remain user-verified unless source evidence is added. |

## Contribution Framing Audit

| Repo / Project | Status | Notes |
|---|---|---|
| `ChristopherDSBarker/pic_caption_app` | Verified public link | Integrated into AI Caption Generator. |
| `Cao-Labs/lutesAI2025` | UI-integrated | Protein AI Pipeline page links the public `ChrisB` folder/workstream. Contribution is framed as research implementation, not ownership of the whole lab repo. |
| `matthew-jugovic/train-io` | Classified, not UI-integrated | Keep pending until Derailed page/source import exists. Contribution should be framed as physics/gameplay systems. |
| `ChristopherDSBarker/Mabinogi` | User-confirmed private/solo | Do not add public button until linkability/visibility is confirmed. |
| `distcrypto/csci367_4` | UI-integrated | Public Git link resolves. Supporting page uses verified repo structure and repo-backed concept logo; lead/main implementation role remains user-confirmed and collaborative. |
| `WoW-addons` | Public/archive candidate | Keep as supporting/archive unless screenshots or usage notes are added. |
| `asset-manager` / `ProgrammingPartyDiscordBot` | Hold | Do not surface without contribution evidence. |

## Explicit Integration Boundary

`Bridging Biology And AI` is now intentionally merged into `Protein AI Pipeline` as a supporting research communication artifact.

The integration is allowed because the webpage now explicitly maps:

- project page: `featured/protein-ai-pipeline.html`
- GitHub workstream: `https://github.com/Cao-Labs/lutesAI2025/tree/main/ChrisB`
- supporting artifact: `assets/supporting/design/bridging-biology-and-ai-understanding.pdf`
- contribution framing: research implementation and experimentation in the `ChrisB` folder/workstream

Do not describe this as ownership of the whole Cao Labs repository.

## Orphan / Hidden Work Check

- Featured source folders: 8/8 represented.
- Supporting source folders: 10/10 represented.
- GitHub-backed supporting integrations: 1 represented (`distcrypto/csci367_4`).
- Supporting single-file works: represented in reel, directory, or source-archive classification.
- No top-level canonical project group is currently orphaned.

## Semantic Risks To Watch

- CSS fallback thumbnails are deployment-safe but not fully repo-derived artifacts.
- Media/video pages include user-confirmed context; add source evidence if public claims need stronger support.
- GitHub pages should not add public repo buttons for private/collaborative repos until linkability and contribution wording are confirmed.
- Project pages should continue using source-archive notes instead of linking ignored raw CSV/ZIP/MP4 files.

## Verdict

The site is deployment-safe and no major canonical project group is hidden. Remaining issues are semantic polish, not broken synchronization:

- artifact-backed thumbnails needed for fallback cards
- stronger evidence for media-page public claims
- careful one-at-a-time GitHub integration with contribution labels
