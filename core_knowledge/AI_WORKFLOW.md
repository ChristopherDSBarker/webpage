# Core Knowledge AI Workflow

This file explains how AI should use `core_knowledge/`.

## First Read

Read `PORTFOLIO_ARCHITECTURE_GUIDE.md` first. It defines the system.

Then read only the rule files needed for the task:

- parity or missing project work: `PORTFOLIO_REPRESENTATION_RULES.md`
- deployment, path, asset, commit, or push work: `DEPLOYMENT_RULES.md`
- thumbnail, hero, crop, or media work: `VISUAL_QA_RULES.md`

## Execution Pattern

Use this sequence:

```text
core knowledge -> workflow -> execution
```

Do not use a giant prompt as a substitute for reading the architecture.

## Minimal Prompting Rule

Ask only high-value questions. If the user already provided enough context,
proceed.

For ambiguous work, clarify:

- the role to adopt
- the immediate goal
- constraints
- audience or deployment limits

## Patch Rule

Patch only the requested scope.

If a task reveals another category of work, report it separately instead of
mixing it into the current patch.

Examples:

- visual polish is separate from parity repair
- parity repair is separate from audit docs
- deployment synchronization is separate from governance docs
- source archive cleanup is separate from webpage presentation

## Final Reporting

Final reports should include only what matters:

- files changed
- validation run
- commit or push status if applicable
- remaining risks or optional polish

Do not bury the user in audit theory when the task was a concrete patch.
