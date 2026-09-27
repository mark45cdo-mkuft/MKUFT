# MKUFT Repository Rendering Tooling

**Status:** non-canon repository operations note.  
**Scientific status:** not an MKUFT scientific module, theory claim, evidence owner, or architecture owner.  
**Operational ownership:** K4/C2 own reasoning, recruitment, receiver and recursive-learning discipline. MKUFT research/publication closure remains governed by [RESEARCH_DERIVATION_AND_CLOSURE_SOP.md](RESEARCH_DERIVATION_AND_CLOSURE_SOP.md) and release identity by [Module 34](docs/34_RESEARCH_OBJECT_IDENTITY_RELEASE_INTEGRITY_AND_REPRODUCIBILITY.md).

## House carrier

For technical GitHub Markdown in this repository:

- display mathematics uses fenced `math` blocks;
- inline mathematics uses `$...$`;
- use renderer-supported mathematical constructions;
- keep symbol definitions and scientific meaning explicit in nearby prose;
- preserve domain-native mathematical typography when mathematics is the object.

A receiver/client rendering defect does **not** authorise semantic or representational downgrade of the technical owner. Do not replace an exact equation with ASCII, prose, or Unicode shorthand merely because one client fails to render the normal mathematical carrier.

If a client cannot render the technical carrier:

1. preserve the exact scientific object;
2. diagnose the receiver/carrier boundary;
3. repair the renderer-compatible syntax if the syntax is actually wrong;
4. otherwise provide or point to an alternate reading carrier such as the verified publication PDF or a deliberately simplified explanatory route;
5. keep the technical Markdown owner mathematically exact;
6. verify the actual receiver before closure.

Plain-text or Unicode mathematical shorthand is allowed when it is intentionally the explanatory object. It must not silently replace the exact mathematical carrier that owns the formal relation.

## Mechanical gates

The repository-local checks are:

- [tools/check_markdown_rendering.py](tools/check_markdown_rendering.py)
- [tools/test_markdown_rendering_checker.py](tools/test_markdown_rendering_checker.py)
- [tools/check_publication_routes.py](tools/check_publication_routes.py)
- [tools/check_research_object_identity.py](tools/check_research_object_identity.py)
- [tools/test_research_object_identity_checker.py](tools/test_research_object_identity_checker.py)
- [.github/workflows/markdown-rendering-integrity.yml](.github/workflows/markdown-rendering-integrity.yml)

These are gates, not scientific owners. Automated integrity checks should report failure; they must not autonomously rewrite scientific modules on `main`.

## Visual closure

A green source checker is not visual proof. For publication-facing or equation-bearing changes, inspect representative rendered mathematics from the reader side, including an opening equation, a dense or unusual middle equation, a symbol-definition passage, and the compact/final relation where applicable.

If the exact intended receiver cannot be witnessed, leave receiver closure open rather than rewriting the scientific carrier to satisfy an imagined client.

## Standing invariant

> **Preserve the mathematics. Repair the failed layer. Verify the receiver. Keep formatting governance out of scientific canon.**
