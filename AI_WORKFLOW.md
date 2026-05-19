# AI Workflow

This file is the execution protocol for AI work in this portfolio repo.

`AI_WORKFLOW.md` is not the portfolio source of truth.
The source of truth lives in `core_knowledge/`.

The purpose of this file is simple:

1. Read core knowledge first.
2. Protect the repo from AI drift.
3. Patch only the requested scope.
4. Add useful comments when editing code.
5. Run the required validation/audit tools before reporting success.

## Mandatory First Rule

Before doing any portfolio work, read the relevant files in:

```text
core_knowledge/
```

The primary canonical guide is:

```text
core_knowledge/PORTFOLIO_ARCHITECTURE_GUIDE.md
```

That guide is canonical for portfolio structure, deployable boundaries,
featured/supporting hierarchy, source-vs-webpage separation, representation
rules, and semantic parity expectations.

Do not duplicate the full architecture guide inside this workflow file.
Do not treat this workflow file as core knowledge.

## Repository Confirmation

Before changing anything, run:

```bash
pwd
git remote -v
git status --short --branch
```

Confirm the deployable webpage repo is:

```text
https://github.com/ChristopherDSBarker/webpage
```

If the repo is wrong, stop and report it.

If there are existing local changes, inspect them before editing.
Do not overwrite user work.
Do not mix unrelated changes into the same patch.

## Execution Order

Use this order for every task:

1. Read the relevant `core_knowledge/` files.
2. Confirm repository identity.
3. Inspect the current files before editing.
4. Classify the requested task.
5. Patch only the requested scope.
6. Add clear comments when editing code.
7. Run the required validation/audit tools.
8. Report changed files, tools run, and validation results.

## Scope Rules

- Refine, do not reinvent.
- Do not overbuild.
- Do not invent missing facts.
- Do not redesign unless explicitly asked.
- Do not infer representation.
- Do not modify source/archive files unless explicitly asked.
- Do not add new tools or audit scripts unless explicitly asked.
- Do not edit `AI_WORKFLOW.md` unless the user explicitly asks to change workflow rules.
- Do not create empty commits.
- Do not push unless explicitly requested.

## Code Comment Rule

Code comments are a standing requirement for AI-edited code.

When editing code, preserve existing useful comments and add clear comments
throughout the changed logic so future AI and human maintainers can understand
the intent.

Required comments should explain:

- why the change exists
- what behavior the logic protects
- how the code supports deployment safety, visual QA, semantic parity, or portfolio behavior
- any non-obvious condition, path, selector, mapping, validation rule, or fallback

Do not remove useful existing comments.
Do not add comments that only restate obvious syntax.
Do not use comments to justify unrelated changes.
Comments should make future edits safer, not noisier.

## Required Validation/Audit Tools

For deployable webpage changes, run:

```bash
python3 tools/deployment_safe_audit.py
```

This tool is required, but it only checks deploy/link safety.
It does not prove visual quality, semantic accuracy, crop quality, thumbnail
readability, or rendered portfolio correctness.

For JSON changes, also run:

```bash
python3 -m json.tool thumbnail-map.json > /dev/null
```

For thumbnail, hero, media, poster, image-reference, visual-card, or
representation changes, run every relevant available audit:

```bash
python3 tools/deployment_safe_audit.py
python3 tools/claimed_vs_exposed_audit.py
python3 tools/semantic_asset_audit.py
python3 tools/semantic_representation_audit.py
python3 tools/semantic_representation_report.py
```

Do not skip an available relevant audit just because
`deployment_safe_audit.py` passed.

If a tool is unavailable, blocked, missing, or fails, report that explicitly.
Do not claim full validation passed unless the relevant tools actually ran.

## Visual QA Rule

For visual changes, inspect rendered output when possible.

Check the affected context, such as:

- homepage/index preview
- projects reel preview
- project detail page hero/media section
- thumbnail-map/reference metadata

Do not report visual success from filenames, file paths, or markup alone.

## Reporting Rule

Before staging, committing, or pushing, report:

- changed files
- staged files
- tools run
- tools not run and why
- validation results
- whether unrelated local changes remain

Use targeted `git add` commands.
Do not stage unrelated files.

If there are no deployable changes, report:

```text
No deployable changes detected.
```

## Final Reminder

Core knowledge comes first.
Workflow comes second.
Execution comes third.

The visible portfolio is the product.
