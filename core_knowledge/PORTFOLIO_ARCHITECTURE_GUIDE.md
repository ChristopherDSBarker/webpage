# Portfolio Architecture Guide

This is the canonical architecture guide for AI work on the portfolio.

All execution workflows must obey this document before patching files.

## Core Architecture

```text
best_works / portfolio = canonical source, archive, and knowledge layer
webpage / portfolio-site = deployable recruiter-facing visualization layer
core_knowledge = governance and semantic system layer
```

These layers must not be confused.

The source/archive layer preserves original project packages, raw assets,
coursework, exploratory files, and evidence.

The webpage layer translates selected source evidence into a deployable,
recruiter-facing static portfolio.

The core knowledge layer defines the rules AI must follow so it does not invent
architecture, hallucinate representation, overbuild audits, or redesign the
site.

## Canonical Locations

Canonical source/archive repo:

```text
/Users/songsidiya/Documents/portfolio
```

Deployable webpage repo:

```text
/Users/songsidiya/Desktop/collaborative_experience_website/portfolio-site
```

Public webpage repo:

```text
https://github.com/ChristopherDSBarker/webpage
```

Do not modify the source/archive repo unless the user explicitly asks for that.

## Portfolio Product

The visible portfolio is the product.

Architecture docs, audits, workflow prompts, maps, CSVs, and scripts support the
portfolio. They are not the user-facing goal.

AI work should improve:

- recruiter readability
- project clarity
- truthful representation
- visual quality
- deployment stability
- source-to-webpage parity

AI work should avoid:

- redesigning stable UI without request
- treating audits as product work
- inventing missing project claims
- creating recursive governance layers
- mixing source/archive and webpage responsibilities

## Featured And Supporting Hierarchy

Featured projects are flagship work. They deserve stronger visual evidence,
clearer project pages, and higher recruiter visibility.

Supporting projects show breadth, coursework, design/media work, utilities,
experiments, and archive-worthy evidence without overwhelming the homepage.

Supporting work is not a failure state. It is a deliberate hierarchy.

Do not move work between featured and supporting unless the user asks or a parity
audit shows a clear source-of-truth mismatch that the user approves.

## Representation Standard

Do not infer representation.

A source project is represented only if it actually exists in the webpage
system through at least one explicit artifact:

- reel card
- dedicated project page
- project directory entry
- `thumbnail-map.json` entry
- resume link
- intentional archive/internal classification

Semantic mentions, similar themes, or related projects do not count as
representation.

## Source Evidence Standard

Project pages should be grounded in available source evidence:

- PDFs
- posters
- screenshots
- presentations
- logos
- demos
- notebooks or HTML exports
- code assets where appropriate
- verified GitHub repositories with contribution framing

Do not invent tools, client names, outcomes, responsibilities, or runtime claims
that the source package does not support.

When raw source artifacts are not deployment-safe, classify them as
source/archive/internal and expose safe derivatives such as screenshots, poster
exports, summaries, or presentation-safe files.

## Refinement Rule

Refine, do not reinvent.

Default to small, evidence-backed changes that preserve:

- site architecture
- featured/supporting structure
- recruiter-facing UI
- deployment-safe relative paths
- current visual identity
- existing project hierarchy

Large redesigns, new governance systems, and broad refactors require explicit
user approval.
