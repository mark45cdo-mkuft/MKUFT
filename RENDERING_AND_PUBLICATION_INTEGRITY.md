# MKUFT Rendering and Publication Integrity

**Status:** standing public-canon integrity rule  
**Owner:** Mark Charles McLaughlin  
**Scope:** MKUFT repository papers, modules, publication records, frozen mirrors, and synchronized reading carriers  
**Companion research SOP:** [`RESEARCH_DERIVATION_AND_CLOSURE_SOP.md`](RESEARCH_DERIVATION_AND_CLOSURE_SOP.md)

## Core rule

> **Source correctness does not prove publication correctness. A scientific object is not ready merely because its source text is mathematically meaningful; every intended user-facing carrier must preserve readable meaning, object identity, and provenance.**

This rule was made explicit after a repository-wide rendering audit found mathematically valid TeX stored in Markdown forms that GitHub displayed as raw syntax or rejected macros.

## Carrier contract

For public GitHub Markdown:

- display mathematics uses fenced `math` blocks;
- inline mathematics uses `$...$`;
- unsupported GitHub math macros are not permitted in actual mathematical carriers;
- Unicode replacement characters and hidden control characters are not permitted;
- fenced blocks must balance;
- TeX-like mathematical source must not sit naked in prose where a reader sees markup rather than mathematics;
- inline code is a literal carrier, not a mathematical carrier.

Literal inline code may quote a command, notation label, filename, or source fragment without becoming the mathematical object itself. A literal code span does not generate or control a nearby fenced `math` display.

### Semantic-key gate

Rendered algebra and readable scientific meaning are separate obligations.

Where prose defines or interprets a load-bearing symbol, the nearby English must make the quantity's meaning unambiguous. Literal code-style notation is acceptable when that English binding is already clear and the exact mathematical object is rendered where required.

Fail the reader-side gate when a reader has to guess what a symbol means or decode raw source with no clear English binding. Do not perform cosmetic rewrites merely because another carrier would look prettier when the definition is already complete and readable.

The standing checker is:

- [`tools/check_markdown_rendering.py`](tools/check_markdown_rendering.py)
- [`tools/test_markdown_rendering_checker.py`](tools/test_markdown_rendering_checker.py)
- [`.github/workflows/markdown-rendering-integrity.yml`](.github/workflows/markdown-rendering-integrity.yml)

The workflow is a gate, not a substitute for human or agent visual inspection of important publication routes.

## Forced recursive closure gate

The existence of a checker, SOP, workflow, publication template, or prior successful example is **not** evidence that the current object passed it.

Before any public Markdown paper/module, DOI route, or publication-facing carrier may be called **closed**, all applicable gates must be positively met on the exact current object:

1. **specimen gate** — identify the current house-standard reference object before formatting or equation conversion;
2. **source gate** — run the rendering checker on the current repository state and obtain an actual pass result;
3. **checker-self-test gate** — the rendering checker must first pass its own known-good/known-bad fixture tests;
4. **reader-side gate** — open the exact public GitHub Preview or final PDF as a reader and visually inspect representative mathematics, headings, semantic keys, rights/status text, and navigation;
5. **object-identity gate** — verify that live module, public paper, publication record, frozen DOI object, and Drive carrier have not been collapsed or mislabeled;
6. **closure-evidence gate** — closure language is prohibited unless the actual pass evidence has been observed. If a gate did not run, cannot be observed, or remains ambiguous, the status is **written/provisioned but not closed**.

For major publication work, sample at least:

- the opening equation-bearing section;
- one middle section with the densest or most unusual mathematics;
- one symbol-definition/key passage;
- the compact/final law or summary equation;
- the publication metadata/rights boundary;
- and at least one surrounding linked module or paper.

For a larger body update, add a small random sample outside the immediately edited neighbourhood so a local clean-up does not create false confidence about the wider carrier.

> **Never infer “the checker must have caught it.” Either the gate produced evidence or it did not happen for closure purposes.**

## Interruption and write-boundary gate

An interruption, tool-window stop, or changed conversation state creates a new audit boundary.

Before resuming a write sequence:

1. read the current branch HEAD;
2. inspect the most recent commits;
3. verify the exact files changed;
4. re-fetch every file that may have been mid-edit;
5. confirm complete tails/closures and expected object identity;
6. only then resume.

A successful write call is not proof that a multi-file task is complete. An interruption is not proof that a pending write did or did not land.

After a write sequence, compare the intended base and current head where practical and verify that no unrelated files changed.

## Automated red-gate escalation

Objective integrity failure must not depend on the repository owner remembering to open the Actions page.

For main-branch pushes, the integrity workflow keeps a persistent repository issue while the gate is not green and closes that issue only after a later successful run.

The persistent issue is an escalation signal, not a replacement for the underlying logs. A red signal means publication-facing work is not closed.

## Recursive lesson — TVT public-rendering miss, 20 August 2026

A public TVT preprint reached GitHub Preview with visible renderer failures including an unsupported operator-name macro and a malformed display that GitHub reported as a missing close brace. The scientific equations were intelligible in source, but the reader-facing carrier was visibly broken.

The failure was not primarily that the repository lacked a standard. The standard already said to use supported GitHub math carriers and already said that visual inspection remained mandatory. The failure was **procedural non-enforcement**:

- the expected format existed but was treated as background knowledge rather than a forced precondition;
- the checker existed but its actual execution/pass was not demonstrated before closure was claimed;
- the public reader-side Preview was not positively inspected at the decisive moment;
- the checker itself had no recursive fixture test proving that its known failure classes still fired;
- closure language was therefore allowed to outrun evidence.

The corrective rule is:

> **A standard becomes operational only when the task is forced through it. A checker becomes evidence only when its pass is observed. A publication becomes closed only when the reader-facing carrier has been traversed successfully.**

The corrective changes are:

- TVT renderer-safe syntax repair without scientific revision;
- expanded `check_markdown_rendering.py` checks for banned macros, TeX brace balance, aligned-environment balance, nested/legacy delimiters, broken fences, hidden control characters, and raw TeX outside a carrier;
- `test_markdown_rendering_checker.py`, which intentionally feeds the checker known-bad and known-good fixtures before repository audit;
- workflow ordering changed to **self-test checker → audit public Markdown → audit publication routes**;
- closure procedure updated to require positive gate evidence rather than trust-by-existence.

This incident is retained as a recursive systems lesson, not merely a one-file formatting patch.

## Recursive lesson — false-positive gate and observer dependence, 22 August 2026

A later integrity run correctly failed, but the failure came from the integrity document itself literally quoting the banned source token while describing the historical TVT incident. The checker was protecting the repository, but its carrier typing was too coarse: literal code documentation and actual mathematical carriers were being treated as the same address.

The same closure pass also exposed a second procedural risk: a red workflow had existed without being positively surfaced because the owner had not manually opened the Actions page.

The resulting rules are:

- literal code and mathematical carriers are different typed objects;
- a checker must be strict at the mathematical carrier without false-failing harmless literal documentation;
- every repaired false positive receives a fixture proving both the allowed literal case and the blocked mathematical case;
- workflow failure must create a persistent repository signal on main;
- a green result after repair must be observed before closure;
- visual inspection must include semantic-key readability, not only the display equation.

## Publication-object contract

Do not collapse these object types:

1. **Live module** — evolving canonical research owner, normally in `docs/`.
2. **Public preprint** — coherent reader-facing paper, normally in `papers/`.
3. **Publication record** — DOI, citation, version, rights, provenance, and relationship metadata.
4. **Frozen deposit** — exact DOI-bearing object; once published, its identity is fixed for that version.
5. **Frozen repository mirror** — preservation copy of a deposited object; do not edit it as though it were a live module.
6. **Drive reading edition or mirror** — convenience carrier; it does not silently become the paper or canonical source.

A module can support a paper without becoming a paper. A paper can originate from modules without erasing their history. A Drive mirror can be useful without owning the scientific object.

## DOI freeze rule

Before a new standalone DOI is published:

1. identify the exact publication object;
2. reserve the DOI where appropriate;
3. insert the DOI into the exact manuscript if that is the chosen publication design;
4. regenerate the final PDF from the audited source;
5. visually inspect the final PDF from the reader side;
6. inspect the public GitHub paper route from the reader side;
7. verify citations, title, author, ORCID, version, date, rights, and DOI relationship;
8. run the checker self-test and repository rendering/publication checks and observe their pass evidence;
9. compute final checksums;
10. commit the exact DOI-bearing source/publication object;
11. upload the exact checked object to the DOI repository;
12. verify the DOI landing route after publication;
13. only then mark the version frozen.

A standing SOP is not evidence that these steps were performed. Closure requires evidence of the actual traversal.

## Discovery rule

Every standalone paper must have a direct route from [`papers/README.md`](papers/README.md).

Published DOI papers must additionally have a publication record that identifies:

- exact version DOI;
- concept DOI where applicable;
- author and title;
- controlling frozen object;
- relationship to live MKUFT modules;
- rights/licence boundary;
- readable public route.

A paper must not become undiscoverable merely because later canon work moved its source ideas into modules.

## Drive rule

Google Drive mirrors are not allowed to blur object identity.

- A module reading edition should say that it is a module reading edition.
- A standalone paper should preferably be represented by its actual publication PDF or a clearly identified paper copy.
- Plain-text/Unicode equation approximations in a Drive reading edition must not be treated as publication-grade mathematical typography.
- The DOI-bearing PDF remains the controlling visual object where the publication record says so.

## Change discipline

Rendering-only repairs must not be described as scientific revisions.

Scientific revisions must not be smuggled through as rendering repairs.

If a rendering repair changes bytes used by a recorded checksum, the checksum must be recalculated and its provenance updated.

The smallest repair should be identified first. Before applying it, ask whether the same failure would recur because the underlying gate is mistyped or incomplete. If so, prefer the smallest structural repair that removes recurrence while preserving the protection, and add a fixture for the discovered failure class.

## Standing invariant

> **Meaning → carrier → transformation → invariant → reader expression must close as one chain. Carrier validity is not delivery validity; test the door from the side the reader actually approaches it.**
