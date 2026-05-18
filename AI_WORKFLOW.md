# AI Workflow

This file is the execution protocol for AI work in this portfolio repo.

Mandatory first rule:

Before execution, read and obey:

```text
core_knowledge/PORTFOLIO_ARCHITECTURE_GUIDE.md
```

That guide is canonical for portfolio structure, representation rules,
deployable boundaries, featured/supporting hierarchy, source-vs-webpage
separation, and semantic parity expectations.

## Execution Order

Use this order for every portfolio task:

1. Read the relevant `core_knowledge/` files.
2. Confirm repository identity.
3. Classify the task.
4. Inspect current files before editing.
5. Patch only the requested scope.
6. Run the right validation.
7. Summarize changed files before commit or push.

Do not treat audits, markdown files, or workflow rules as the product. The
visible portfolio is the product.

## Documentation Architecture

- `core_knowledge/` is canonical. Use it for rules and source-of-truth guidance.
- `audits/` is temporary reporting. Do not treat old audit conclusions as truth without rechecking current files/rendered pages.
- `docs/` is reference/support material. Use it for mappings, inventory, GitHub sync notes, and thumbnail process docs.
- Keep the repo root minimal: `README.md`, `AI_WORKFLOW.md`, deployable pages/assets, and operational data such as `thumbnail-map.json`.

## Repository Confirmation

Before changing anything, run:

```bash
pwd
git remote -v
git status --short --branch
```

The deployable webpage repo must be:

```text
https://github.com/ChristopherDSBarker/webpage
```

If the repo is wrong, stop and report it.

If the worktree has existing changes, inspect them before editing. Do not
overwrite user changes or mix unrelated work into the same commit.

## Task Classification

Classify work before patching:

- `frontend presentation`
- `assets`
- `resume`
- `documentation`
- `audit tooling`
- `deployment synchronization`
- `portfolio parity`
- `visual QA`

Keep separate categories in separate patches unless the user explicitly asks to
combine them.

## Core Rules

- Refine, do not reinvent.
- Do not overbuild.
- Do not invent missing facts.
- Do not redesign unless explicitly asked.
- Do not infer representation.
- Do not mix source/archive work with deployable webpage work.
- Do not add audit scripts when the task asks for content, parity, or visual QA.
- Do not create empty commits.
- Do not push unless explicitly requested.

## Source And Deploy Boundaries

Default source/archive location:

```text
/Users/songsidiya/Documents/portfolio
```

Default deployable webpage location:

```text
/Users/songsidiya/Desktop/collaborative_experience_website/portfolio-site
```

Do not modify the source/archive repo unless explicitly instructed.

Do not deploy raw videos, databases, saves, scores, `.git` folders, full repos,
or private/archive source files unless the user explicitly approves and the file
is deployment-safe.

## Validation

For deployable webpage changes, run:

```bash
python3 tools/deployment_safe_audit.py
```

This audit is required, but it only checks deploy/link safety. It does not
prove thumbnail quality, crop quality, context fit, semantic representation, or
whether a visual patch actually works in the rendered portfolio.

For JSON changes, also run:

```bash
python3 -m json.tool thumbnail-map.json > /dev/null
```

For visual QA, inspect the rendered pages or screenshots, not filenames alone.

## Visual Patch Verification

For thumbnail, hero, media, poster, image-reference, or visual-card changes,
run every available relevant check before reporting success:

```bash
python3 tools/deployment_safe_audit.py
python3 tools/claimed_vs_exposed_audit.py
python3 tools/semantic_asset_audit.py
python3 tools/semantic_representation_audit.py
python3 tools/semantic_representation_report.py
```

Use judgment for relevance, but do not skip an available audit just because
`deployment_safe_audit.py` passed. If a tool is unavailable, blocked, or fails,
report that explicitly and do not claim full visual QA passed.

A visual patch is not complete when the file reference changes.
It is complete only when every affected rendering context has been inspected:
1. homepage/index preview
2. projects reel preview
3. project detail page hero/media section
4. thumbnail-map/reference metadata
5. deploy-safe audit

This prevents a "1 of 3 fixed" patch where one image works in a project hero
but fails in the homepage or projects reel.

## Three-Context Thumbnail Rule

Check these contexts separately for any project thumbnail or hero change:

- `index.html` homepage preview
- `projects.html` reel card
- the individual `featured/*.html` or `supporting/*.html` project page hero
  and media section

One asset may work in one context and fail in another. Do not call a visual
patch fixed until every affected context passes.

## Visual Patch Report Template

For visual patches, report:

- tools run
- tools not run and why
- pages visually checked
- screenshots or manual evidence used
- changed image assets
- changed references
- deployment audit result

If rendered inspection was impossible, say so directly and describe what was
checked instead. Do not present markup-only or filename-only checks as visual
QA.

For parity work, compare source folders to actual webpage artifacts. A project is
represented only if it has a reel card, dedicated page, directory entry,
thumbnail-map entry, resume link, or intentional archive/internal
classification.

## Commit And Push Protocol

Before committing or pushing, report:

- changed files
- staged files
- validation result
- whether unrelated local changes remain

Use targeted `git add` commands. Do not stage unrelated files.

If there are no deployable changes, report:

```text
No deployable changes detected.
```

## Portfolio Work Reminder

The portfolio exists for recruiter readability, project clarity, truthful
representation, visual quality, and deployment stability.

Core knowledge comes first, workflow second, execution third.
