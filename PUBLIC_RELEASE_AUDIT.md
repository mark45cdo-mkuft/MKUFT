# MKUFT Public Release Audit — Silver Update

Author: Mark Charles McLaughlin  
Status: completed public release audit  
Date: 12 July 2026

## Purpose

This record documents the public-readability, structural-coherence, statistical, and information-hygiene checks performed for the Silver Update.

It is not scientific validation of MKUFT. It records whether the public working copy states its claims honestly, routes its modules coherently, and contains only material cleared for publication.

## Scope reviewed

The review covered:

- public entry documents;
- the integrated master spine and canon map;
- the mathematical and formal spine;
- experimental, worked-example, and falsification documents;
- observer, threshold, procedural, Voynich, boundary, and explanatory modules;
- all four Silver Update modules;
- the complete pull-request diff against `main`;
- repository-wide checks for accidental non-public content and access secrets.

The file-by-file integration registry is in:

`docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md`

## Information-hygiene result

No access secret or uncleared non-public material was identified in the reviewed release.

Incorrect visibility and status labels in older public files were corrected.

The governing rule is:

> Only material deliberately cleared for public release belongs in the public canon.

This audit records categories of checks and corrections. It does not reproduce discarded wording or private source material.

## Correction summary

The audit corrected or tightened:

- inaccurate document status labels;
- notation collisions and unnormalised heuristic factors;
- one statistical comparison using the wrong uncertainty calculation;
- equations whose modelling status was not explicit enough;
- cross-layer expressions lacking clear units and operationalisation boundaries;
- applied claims stated more strongly than their evidence allowed;
- experimental proposals insufficiently separated from established findings;
- outdated public-entry and master-spine wording;
- incomplete routing between older modules and the Silver architecture.

No removed passage is quoted in this record.

## Architecture result

Every numbered document from `01` through `24` now has a recorded route to:

- its primary role;
- parent or required support;
- main outward application;
- principal limit or falsifier.

The public stack can be entered through:

- the README;
- the public overview;
- the integrated master spine;
- the reconstitution kernel;
- the mathematical appendix;
- the cross-support map;
- a domain application;
- the falsification summary.

Those routes are intended to reconstruct the same layer definitions, formulas, claim-status boundaries, and failure conditions.

## Statistical result

The RNG worked example now uses the uncertainty appropriate to a difference between two independent proportions.

Illustrative values are labelled as hypothetical rather than observed evidence or predicted effect size.

Environmental or observer terms must be specified before analysis and cannot be assigned afterwards to rescue a failed prediction.

## Public-readability result

The repository is not bare. The Silver Update contains:

- plain-English entry documents;
- a rebuilt integrated master spine;
- dedicated formal modules;
- a complete dependency registry;
- application modules;
- experimental requirements;
- branch-specific falsifiers;
- explicit claim-status boundaries.

The stack remains detailed, but the main entry points now provide a shorter route before technical depth.

## Important limitation — Git history

Editing or merging a file does not erase earlier public Git commits.

No history-rewrite requirement was identified during this audit.

If genuinely sensitive content is ever found in repository history, deleting it from the current version is not sufficient; history, caches, forks, releases, and any affected credentials would require separate remediation.

## Release gates

The Silver Update was cleared for merge after confirming that:

- the branch remained mergeable;
- the public entry route was coherent;
- formulas and status labels were consistent;
- no uncleared non-public material was present;
- speculative claims remained labelled;
- ordinary alternatives and falsifiers remained active;
- the update strengthened rather than obscured the original work.

## Audit conclusion

The Silver Update is materially more readable, statistically correct, structurally integrated, and publicly disciplined than the previous working copy.

No information-hygiene blocker was identified.
