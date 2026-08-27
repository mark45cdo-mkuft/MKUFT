# Release Manifests

This directory stores machine-readable identity records for declared stable or externally frozen research releases.

The governing contract is [Module 34 — Research Object Identity, Release Integrity, and Reproducibility](../docs/34_RESEARCH_OBJECT_IDENTITY_RELEASE_INTEGRITY_AND_REPRODUCIBILITY.md).

A concrete manifest records only the information needed to recover and verify the declared release object: release identifier, tag, exact source commit, version/date identifiers, repository-relative artifact paths, SHA-256 digests, byte counts, and optional typed external identifiers.

## Rules

- `_template.json` is a template only and is ignored by the integrity checker.
- Concrete manifests use `.json` and must satisfy the Module 34 contract.
- Artifact paths are repository-relative, normalised paths.
- SHA-256 and byte counts are computed from the exact release candidates before the release is declared closed.
- Credentials, signing material, local absolute paths, transient access URLs, and environment-specific secrets do not belong in manifests.
- A manifest identifies an object; it does not establish scientific validity or replace the paper/publication record.
- If a declared artifact changes, create a new lawful release state and regenerate its manifest rather than editing the earlier release identity in place.

Run:

```text
python tools/test_research_object_identity_checker.py
python tools/check_research_object_identity.py
```

before closing a release-facing change.
