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

For JSON changes, also run:

```bash
python3 -m json.tool thumbnail-map.json > /dev/null
```

For visual QA, inspect the rendered pages or screenshots, not filenames alone.

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
