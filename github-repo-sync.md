# GitHub Repository Synchronization

Source account: `https://github.com/ChristopherDSBarker`

Purpose: map public GitHub repositories into the existing portfolio architecture without turning the portfolio into a raw repo dump.

## Synchronization Rules

- Treat GitHub as technical evidence, not the portfolio itself.
- Prefer integrating repositories into existing project pages when the identity already exists.
- Create a new project page only when a repo has distinct standalone identity and enough presentation material.
- Collaborative repos require contribution language before they become public portfolio claims.
- Team projects should not be hidden when the contribution role is substantial; they should be shown with role scope.
- Repos with unclear contribution evidence stay archive/internal until clarified.
- Generated portfolio thumbnails should not replace real repo artifacts, screenshots, or diagrams.

## Repository Verification Rules

Repository existence may be verified through any of these:

- public GitHub URL
- GitHub API visibility
- browser-visible repository listing
- user-confirmed repository ownership/contribution
- local repository synchronization records

Private or collaborative repositories should not be excluded only because public API visibility is unavailable. Existence verification and public linkability are separate decisions.

## Visibility Status Taxonomy

| Status | Meaning |
|---|---|
| `Public verified` | Repo exists and can be linked publicly now |
| `Private verified` | Repo exists but should not receive a public button yet |
| `Collaborative verified` | Repo/project exists and contribution role is confirmed |
| `Pending visibility` | Existence/role known, but public link/source import decision is unresolved |
| `Internal` | Intentionally hidden or not portfolio-facing |

Public GitHub buttons should only be added after URL accessibility and intended visibility are confirmed.

## Contribution Role Labels

Use explicit role labels on project pages and directory entries:

- `Solo / Full implementation`
- `Lead developer`
- `Primary implementation`
- `Research implementation`
- `Physics systems / gameplay mechanics`
- `Collaborative contributor`
- `Archive/reference`

## Repo Classification

| Repo | Evidence Found | Verification | Classification | Portfolio Action | Status |
|---|---|---|---|---|---|
| `ChristopherDSBarker/pic_caption_app` | Public API repo with `app.py`; matches AI Caption Generator | Public verified | Existing featured integration | Added GitHub link to `featured/ai-caption-generator.html` | Synced |
| `Cao-Labs/lutesAI2025` | Public API repo; `ChrisB/` folder on `main`; README, protein image generation, BLIP-2 workflow, evaluation scripts, and similarity CSV exist | Collaborative verified | Featured research integration | Integrated as Protein AI Pipeline; state `Research implementation / ChrisB folder/workstream` | Synced |
| `matthew-jugovic/train-io` | Public API repo; design folder includes Derailed project files; contributor metadata shows `ChristopherDSBarker` with 9 contributions | Collaborative verified | Collaborative Derailed candidate | Add after curated source/assets are imported; state `Physics systems / gameplay mechanics` | Pending import |
| `ChristopherDSBarker/Mabinogi` | Browser-visible/user-confirmed solo project; not publicly discoverable by API/search in this session | Private verified | Standalone supporting technical project | Create supporting page after repo/source import; state `Solo / Full implementation`; add public button only if visibility is intended | Pending visibility |
| `distcrypto/csci367_4` | Public Git link resolves; temp clone verified README, `conceptlogo.png`, `game.js`, auth/register/login, leaderboard/save/score files, audio/game assets, and branch history including `chris_branch`; Christopher's lead/main implementation role is user-confirmed | Collaborative verified / public Git link verified | Supporting technical game project | Integrated as `supporting/csci367-game-systems.html`; uses repo-backed concept logo; public GitHub button added; role framed as user-confirmed lead/main implementation contributor | Synced |
| `ChristopherDSBarker/WoW-addons` | Public API repo with Lua addon utilities and `.toc` files | Public verified | Supporting/archive technical utility | Add as supporting/archive reference if screenshots/usage notes are added; state `Solo utility/addon development` | Archive/reference |
| `nsayre01/asset-manager` | Public API repo; contributor metadata did not show `ChristopherDSBarker` in public API result | Public repo / role unclear | Collaborative/external unclear | Do not surface until contribution evidence is provided | Hold |
| `arielbrice/ProgrammingPartyDiscordBot` | Public API repo; contributor metadata did not show `ChristopherDSBarker` in public API result | Public repo / role unclear | Collaborative/external unclear | Do not merge with GAN Discord Bot without contribution evidence | Hold |

## Recommended Next Integrations

1. **Protein AI Pipeline**
   - Source: `Cao-Labs/lutesAI2025`, especially `ChrisB/`.
   - Current status: integrated as a featured research page with GitHub workstream link and contribution statement.
   - Suggested next polish: add protein matrix visualizations, pipeline diagram crops, BLIP-2 output screenshots, or evaluation chart exports.
   - Required wording: "Research implementation and experimentation in the `ChrisB` folder/workstream." Do not imply ownership of the full Cao Labs repository.

2. **Derailed / train-io**
   - Candidate source: `matthew-jugovic/train-io`.
   - Needs: curated source/assets, gameplay screenshots, architecture notes, GitHub button, and decision on featured vs supporting.
   - Suggested wording: "Collaborative game project developed during 5S Summer Software. Contributed train physics systems and gameplay mechanics."

3. **Mabinogi**
   - Candidate source: user-confirmed solo repo/source.
   - Needs: repo URL or source import, screenshots/diagrams, and supporting technical page.
   - Suggested wording: "Solo technical project focused on AI systems, XML logic, deterministic rules, and behavior architecture."

4. **csci367_4**
   - Source: `distcrypto/csci367_4`.
   - Current status: integrated as a supporting technical game project with GitHub link, repo-backed concept logo, and contribution framing.
   - Suggested next polish: add an owned UI screenshot, systems diagram, or short architecture note for auth/save/leaderboard flow.
   - Required wording: "Collaborative project; lead/main implementation contributor role is user-confirmed." Do not imply sole ownership of the full repository.

5. **WoW Addons**
   - Candidate source: `ChristopherDSBarker/WoW-addons`.
   - Keep as supporting/archive reference unless it gets screenshots, usage notes, and a clearer portfolio story.
   - Suggested wording: "Solo Lua addon/utility scripting for game customization and real-use tooling."

## Do Not Auto-Expose

- Repos without clear contribution evidence.
- Forks/collaborative repos that could imply sole ownership.
- Utility repos with no screenshots, README depth, or portfolio narrative.
- Coursework or experiments that duplicate an existing project identity.

## Current Safe Change Made

`pic_caption_app` now reinforces the existing AI Caption Generator page instead of creating a duplicate project identity.
