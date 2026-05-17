# Deployment Rules

These rules protect the deployable webpage repo.

## Deployable Boundary

The webpage repo is the GitHub Pages presentation layer. It should contain only
deployment-safe files needed for the public portfolio.

Do not copy these into the webpage repo unless explicitly approved:

- raw videos
- databases
- save files
- score files
- `.git` folders
- full source repos
- private archive files
- large raw datasets
- assignment ZIP bundles
- source-only design files such as `.ai` unless intentionally exposed

Prefer presentation-safe derivatives:

- PNG/JPG screenshots
- PDF previews
- exported posters
- HTML exports
- concise summaries
- curated source snippets

## Path Rule

Use deploy-safe relative paths only.

Never add local absolute paths such as:

```text
/Users/...
```

Webpage-visible links must resolve from the deployed static site.

## Required Audit

Run before deployment:

```bash
python3 tools/deployment_safe_audit.py
```

The audit must report:

- missing references: 0
- ignored-file references: 0
- untracked references: 0

Passing this audit means the deployable references are safe. It does not prove
that thumbnails, heroes, crops, cards, or media are visually acceptable. For
visual patches, also follow `VISUAL_QA_RULES.md` and inspect every affected
rendering context.

## JSON Validation

When editing `thumbnail-map.json`, run:

```bash
python3 -m json.tool thumbnail-map.json > /dev/null
```

## Git Rule

Before edits, commits, or pushes, verify:

```bash
pwd
git remote -v
git status --short --branch
```

Do not create empty commits.

Do not push unless explicitly requested.

Before commit or push, summarize:

- changed files
- staged files
- validation results
- unrelated local changes

Use targeted `git add` commands.
