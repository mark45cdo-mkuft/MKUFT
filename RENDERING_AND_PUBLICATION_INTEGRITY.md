# MKUFT Rendering and Publication Integrity

**Status:** standing public-canon integrity rule  
**Owner:** Mark Charles McLaughlin  
**Scope:** MKUFT repository papers, modules, publication records, frozen mirrors, and synchronized reading carriers

## Core rule

> **Source correctness does not prove publication correctness. A scientific object is not ready merely because its source text is mathematically meaningful; every intended user-facing carrier must preserve readable meaning, object identity, and provenance.**

This rule was made explicit after a repository-wide rendering audit found mathematically valid TeX stored in Markdown forms that GitHub displayed as raw syntax or rejected macros.

## Carrier contract

For public GitHub Markdown:

- display mathematics uses fenced `math` blocks;
- inline mathematics uses `$...$`;
- unsupported GitHub math macros are not permitted;
- Unicode replacement characters and hidden control characters are not permitted;
- fenced blocks must balance;
- TeX-like mathematical source must not sit naked in prose where a reader sees markup rather than mathematics.

The standing checker is:

- [`tools/check_markdown_rendering.py`](tools/check_markdown_rendering.py)
- [`.github/workflows/markdown-rendering-integrity.yml`](.github/workflows/markdown-rendering-integrity.yml)

The workflow is a gate, not a substitute for human visual inspection of important publication routes.

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
8. compute final checksums;
9. commit the exact DOI-bearing source/publication object;
10. upload the exact checked object to the DOI repository;
11. verify the DOI landing route after publication;
12. only then mark the version frozen.

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

## Standing invariant

> **Meaning → carrier → transformation → invariant → reader expression must close as one chain. Carrier validity is not delivery validity; test the door from the side the reader actually approaches it.**
