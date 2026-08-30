# 34 — Research Object Identity, Release Integrity, and Reproducibility

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Canonical module date:** 27 August 2026  
**Publication-integrity parent:** [Rendering and Publication Integrity](../RENDERING_AND_PUBLICATION_INTEGRITY.md)  
**Research-process parent:** [Research Derivation and Closure SOP](../RESEARCH_DERIVATION_AND_CLOSURE_SOP.md)  
**Dependency/deformation parent:** [25 — Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)  
**Recursive-interface parent:** [33S7A — Future-Sufficient Address Invariant and Layer-Before-Law Precedence](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md)  
**Claim-discipline parent:** [29 — Scientific Tightening and Claim Discipline](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md)  
**Provenance control:** [Provenance, DOI, and Attribution](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Citation metadata:** [`CITATION.cff`](../CITATION.cff)  
**Machine-readable relationship metadata:** [`codemeta.json`](../codemeta.json)  
**Operational manifest route:** [`release-manifests/`](../release-manifests/)  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless an exact later publication states otherwise.  
**Status:** canonical research-object identity and reproducibility module. This module governs version identity, release boundaries, artifact verification, citation consistency, and external preservation; it does not change the scientific claims or evidential status of the objects it describes.

## 1. Purpose

A research programme can contain live source, rendered papers, frozen deposits, repository releases, machine-readable metadata, and external archives that share a title while differing in bytes, version, scope, or scientific state. Reproducibility therefore requires more than a readable filename or a remembered publication date.

The governing requirement is:

> **A declared research object must remain independently identifiable across source, release, archive, citation, and reader-facing carriers, so that a later reader can recover which exact object was evaluated, cited, reproduced, or compared.**

This module supplies that identity contract without collapsing distinct carriers into one object.

## 2. Typed research-object family

For a declared release version `v`, distinguish at least the following objects where they exist:

- **live source state** — the mutable repository state from which a release is prepared;
- **source commit** — the exact Git commit selected for the release boundary;
- **release tag** — the named immutable repository address associated with that source state;
- **release artifact set** — the files declared to constitute the released research object;
- **artifact manifest** — machine-readable file paths, byte counts, and cryptographic digests for that artifact set;
- **citation metadata** — author, title, version, date, identifiers, and recommended citation route;
- **reader-facing carrier** — the Markdown, PDF, data, code, or other object a reader actually receives;
- **external deposit or archive** — an independently hosted preservation or publication object, where applicable.

These objects may refer to one another, but they are not interchangeable.

A Git tag does not become a DOI. A DOI does not prove that two files have identical bytes. A checksum does not establish scientific validity. Citation metadata does not prove that the intended carrier was uploaded. Each object answers a different reproducibility question.

## 3. Release identity tuple

Define a release identity record

```math
\mathcal{R}_v = \left(C_v,T_v,A_v,H_v,M_v,D_v,P_v\right),
```

where:

- `C_v` is the exact source commit;
- `T_v` is the release tag;
- `A_v` is the declared artifact set;
- `H_v` is the artifact identity map, including SHA-256 and byte count;
- `M_v` is the release/citation metadata state;
- `D_v` is the external publication identifier set, such as a version DOI, where one exists;
- `P_v` is any additional independent preservation identifier, where one exists.

Not every release requires every optional external identifier. The minimum reproducible release boundary is the smallest tuple that lets another operator recover the exact source state and verify the declared artifacts without inference from filenames alone.

For an artifact `a \in A_v`, byte identity requires

```math
H_v(a)=\left(\mathrm{SHA256}(a),\mathrm{bytes}(a)\right).
```

If either component differs, the artifact is not the same frozen byte object even when its title and filename are unchanged.

## 4. Release classes

Not every repository edit is a publication event. Use three operational classes.

### 4.1 Working state

Ordinary development commits remain Git history. They do not require a release manifest merely because they exist.

### 4.2 Stable repository release

A named stable release should identify:

- exact commit;
- annotated release tag;
- declared artifact set;
- exact artifact hashes and byte counts;
- version/date metadata;
- relationship to prior and later releases where relevant.

### 4.3 Externally frozen research object

A release intended for DOI deposit, archival preservation, or another frozen external carrier additionally requires receiver-side verification of the deposited object and the external identifier relationship.

The frozen external object does not silently absorb later live-repository changes.

## 5. Signed release boundary

For a stable or externally frozen research release, use an annotated cryptographically signed Git tag where the repository platform and release procedure support it.

The signing credential remains outside the repository. No private credential, recovery material, or secret signing configuration belongs in source control.

The release close requires verification that:

1. the tag resolves to the intended source commit;
2. the platform reports the release signature state expected by the signing method;
3. the release manifest identifies the same commit and tag;
4. the declared artifact hashes were computed from the exact release candidates rather than reconstructed later from a changed working tree.

A verified signature establishes the cryptographic association between the signing identity and the tagged Git object. It does not by itself establish scientific correctness, novelty, or empirical confirmation.

## 6. Artifact manifest contract

A release manifest is a small machine-readable identity record stored under [`release-manifests/`](../release-manifests/).

Each concrete manifest must contain at minimum:

```json
{
  "schema_version": "1.0",
  "release_id": "<stable release identifier>",
  "tag": "<release tag>",
  "commit": "<40-character Git commit SHA>",
  "citation": {
    "version": "<declared version>",
    "date": "YYYY-MM-DD",
    "doi": "<optional version DOI>"
  },
  "artifacts": [
    {
      "path": "<repository-relative path>",
      "sha256": "<64 hexadecimal characters>",
      "bytes": 1
    }
  ]
}
```

Optional external identifiers may be added as typed key/value records. The manifest must not contain credentials, local absolute paths, transient download URLs, or mutable environment-specific state.

A manifest is not a scientific summary and should not duplicate the paper. Its job is exact object identity.

## 7. Metadata custody

The current metadata roles remain typed rather than duplicated.

- [`CITATION.cff`](../CITATION.cff) carries the principal repository citation surface and preferred citation.
- [`codemeta.json`](../codemeta.json) carries broader machine-readable research-object relationships and discovery metadata.
- standalone publication records carry version-specific DOI, rights, and live-versus-frozen relationships for their exact objects.
- release manifests carry byte-level artifact identity for declared release sets.

A new metadata file must not silently take over a role already carried by one of these files. If an external service requires a different authoritative metadata carrier, that transition must be explicit, documented, and checked in the same repository change that introduces it.

## 8. External preservation and publication

External identifiers must retain their own typed meaning.

```text
Git commit
→ signed release tag
→ declared release artifact set
→ release manifest
→ external deposit / archive where applicable
→ receiver-side object verification.
```

For a DOI-bearing publication, the DOI identifies the deposited publication object and its metadata record. The repository must still verify that the attached carrier is the intended object.

For an independent source archive, retain the archive's native persistent identifier where available rather than converting it into a local substitute.

The repository should prefer established archival and citation standards over locally invented identifier schemes when an adequate standard already exists.

### 8A. Dynamic retrieval and provenance independence

During the development of this research programme, the author repeatedly observed that publication of a new research object was followed by changes in the surrounding search and AI-retrieval surface. Material bearing unusually close conceptual or terminological relationships to the newly released object could become substantially more visible afterward, including older-dated material that had not appeared in earlier exploration of the same research neighbourhood. These observations are retained as a provenance and retrieval phenomenon rather than as evidence that any particular historical source was retrospectively created or altered.

The distinction matters because contemporary digital agreement is not automatically independent agreement. Search indexes, citation databases, institutional pages, AI-generated summaries, metadata services, and derivative research surfaces may share upstream dependencies. A large number of mutually consistent digital records can therefore provide less independent provenance than their raw count suggests. In the language of this architecture, provenance is **load-bearing** when a claim depends on historical priority, version identity, or causal order: local consistency between records does not establish that their ancestry is independent.

This problem becomes more important as tool-using generative systems gain the technical capacity to create documents, repositories, webpages, profiles, metadata, citations, and mutually referencing records across services. The existence of those capabilities does not establish that retrospective reconstruction of the scientific record has occurred in the cases observed here. It does mean, however, that a present-day web of mutually corroborating digital objects should not be treated as the strongest possible historical control when stronger independent anchors are available.

Accordingly, priority-sensitive work in this programme should preferentially preserve evidence that is difficult to reconstruct from a single later digital state: independently timestamped deposits, signed repository states, cryptographic hashes, archived captures, receiver-side verification, independent citations with demonstrable earlier custody, and, where relevant, non-derived institutional or physical records. Search-result surfaces may additionally be frozen before and after major releases so that changes in the semantic neighbourhood can themselves be measured rather than reconstructed from memory.

#### Epistemic compression and false closure

A second provenance hazard appears when a downstream representation is more epistemically closed than the source state from which it was produced. A partially grounded, dependency-rich, qualified, or unresolved object can be compressed into fluent prose that reads as settled even though no new evidence has entered the chain. The representation may be easier to consume while carrying less of the uncertainty, dependency, source, or reopening structure that made the original object scientifically interpretable.

For provenance-sensitive reuse, the relevant state transition is therefore not determined by fluency. A downstream representation may simplify expression, but it must not silently promote evidential state:

```text
UNRESOLVED / QUALIFIED / RESTORE-REQUIRED
+ no new evidence
→ fluent CLOSED representation
= invalid epistemic transition.
```

Where an omitted distinction can later become decision-bearing, lawful compression must either preserve the necessary ancestry and qualification state or preserve a reliable route back to the exact lower object before consequential reuse. If neither condition is met, the downstream state remains unresolved, incomplete, or restoration-required rather than being completed by narrative smoothness. This is the provenance-address form of the preserve-or-reopen rule owned by Module 33S7A.

If such a falsely closed representation is subsequently indexed, cited, summarised, or used as retrieval context, the local compression error can become a recursive provenance error. Later systems may inherit the confident surface while losing the source conditions that would have forced reopening. A system that repeatedly converts unresolved state into stronger closure without additional evidence should therefore be treated as exhibiting a state-transition and provenance failure, not merely a stylistic defect.

#### Recursive retrieval coupling

A further burden appears when the retrieval surface is itself allowed to become an input to later retrieval. A newly released object can alter which neighbouring objects are selected, summarised, cited, generated, or made salient; those derivative objects can then be indexed and returned in subsequent passes. The resulting topology is recursive:

```text
release
→ retrieval association
→ derivative representation / citation / summary
→ re-indexing
→ strengthened or altered retrieval association
→ later retrieval from the changed surface.
```

Under such a loop, the number of apparently corroborating records can increase without a corresponding increase in independent evidential ancestry. Later systems may encounter the accumulated derivative surface as prior context and reproduce it again. Local agreement can therefore become progressively stronger while the independence of the underlying support becomes progressively weaker.

This is an instance of the same load-bearing dependency problem formalised in Module 25 and the same preserve-or-reopen burden formalised for recursive reuse in Module 33S7A. When a provenance-bearing object is promoted into a later evidential interface, the later use must preserve enough ancestry to distinguish genuinely independent support from repeated descent through a common upstream state. A count of agreeing endpoints is not a substitute for a typed dependency route.

The recursive claim is testable at the retrieval address. For a priority-sensitive release, a fixed set of queries, result positions, dates, accounts or sessions, and retrieval systems can be frozen before publication and repeated afterward. Reproducible post-release appearance or strengthening of unusually close semantic neighbours across prospective replications supports a claim of **retrieval coupling** at the measured surface. Failure to reproduce the effect, instability under independent accounts or systems, or recovery of an ordinary ranking/indexing explanation contracts that claim. Retrieval coupling by itself does not assign authorship, intent, fabrication, or a unique mechanism.

The purpose of this requirement is not defensive priority assertion. It is a general consequence of the same dependency problem addressed elsewhere in MKUFT/ATLD: **if several apparently independent observations inherit from one hidden upstream state, treating them as independent evidence overcounts the support.** Research provenance therefore requires not only agreement between records but, where the burden warrants it, evidence about the independence and custody of the route by which those records came to agree.

> **A provenance system that recursively consumes its own outputs must preserve ancestry, qualification state, and lawful reopening routes, not merely consensus.**

## 9. Release procedure

For a stable or externally frozen research release:

```text
scientific object closed at its declared scope
→ publication/rendering gates green
→ exact source commit selected
→ release artifacts frozen locally
→ SHA-256/byte manifest generated
→ citation/version metadata checked
→ signed annotated tag created
→ tag/commit/signature state verified
→ repository release created
→ external deposit/archive created where applicable
→ receiver-side carrier verified
→ external identifier recorded
→ research-object identity gate rerun
→ release closed.
```

Do not create a release tag first and then continue editing the artifact intended to belong to that tag. If the artifact changes, select a new lawful source state and regenerate the manifest.

Where priority, discovery order, or retrieval coupling is itself part of the declared research burden, the release procedure may additionally freeze a small prospective retrieval-surface record before publication. That record should state the exact queries, date/time, retrieval system, account/session condition where relevant, and the captured result surface. It is an auxiliary measurement object, not a substitute for the release identity tuple or prior-art review.

## 10. Version succession

A later release does not rewrite an earlier one.

```math
\mathcal{R}_v \neq \mathcal{R}_{v+1}
```

whenever the declared source state, artifact bytes, release tag, version metadata, or external deposited object changes.

A later version may preserve the same concept DOI or publication family where the external repository supports that relationship, but each version retains its own exact identity.

Corrections to metadata that do not alter a frozen deposited object must be represented honestly as metadata corrections rather than as silent changes to the frozen bytes.

## 11. Machine gate

The standing checker is [`tools/check_research_object_identity.py`](../tools/check_research_object_identity.py), with fixture tests in [`tools/test_research_object_identity_checker.py`](../tools/test_research_object_identity_checker.py).

The gate verifies deterministic properties that can be established from the repository state, including:

- principal DOI/ORCID/repository consistency between the current citation carriers;
- presence of the Module 34 and release-manifest contract;
- valid concrete manifest structure;
- repository-relative artifact paths;
- exact SHA-256 and byte-count agreement for declared artifacts;
- absence of an undeclared competing metadata role;
- separation of the template manifest from concrete releases.

Signature verification and receiver-side external-deposit inspection remain explicit release-close observations. A repository checker must not claim to have observed an external platform state it did not actually inspect.

## 12. Failure and reduction conditions

The release-integrity claim fails or contracts when any applicable condition below is met:

- a declared artifact cannot be recovered from the recorded path and release state;
- a manifest digest or byte count does not match the declared artifact;
- a release tag resolves to a different source state than the release record declares;
- citation carriers disagree materially about the principal research object without an explicit version transition;
- an external identifier points to a different carrier than the repository record declares;
- a same-title object is treated as identical without byte-level or version-level evidence where exact identity matters;
- a signature state is asserted without observing the relevant verification result;
- a mutable live module is presented as though it were the exact frozen deposited object;
- a new metadata carrier silently replaces an existing metadata role without an explicit transition;
- records counted as independent support are shown to descend from a common upstream source that was not carried in the provenance model;
- a downstream representation silently converts an unresolved, qualified, or restoration-required source state into stronger closure without new evidence or a preserved lawful reopening route;
- a claimed retrieval-coupling pattern fails prospective replication under its declared query/session/system conditions or is adequately explained by an ordinary indexing, ranking, metadata, or shared-source mechanism.

Where ordinary Git history, a stable tag, and a single exact artifact are already sufficient for the declared reproducibility burden, no larger packaging system is required. Additional metadata anatomy is justified only when it resolves a real identity or reconstruction burden.

## 13. Scope boundary

This module governs research-object identity and reproducibility. It does not:

- upgrade a speculative claim into evidence;
- establish that a scientific result is correct;
- replace prior-art review;
- create a new scientific result merely by preserving one carefully;
- require every working commit to become a release;
- require an additional metadata standard when the current typed carriers already close the declared object;
- infer authorship, motive, fabrication, or retrospective alteration from a retrieval-surface change without independent route evidence.

The scientific object and the release object therefore remain distinct:

```text
scientific validity
≠ release identity
≠ byte identity
≠ citation identity
≠ archival identity.
```

A strong release chain makes the evaluated object recoverable. Scientific promotion still depends on the evidence, controls, nulls, falsifiers, and independent tests owned elsewhere in the canon.

## 14. Canonical compression

> **Freeze the smallest sufficient research object, identify its exact source state, bind its declared artifacts to reproducible byte identities, keep citation and archive roles typed, preserve ancestry, qualification state, and reopening routes where apparent consensus or closure may be recursively derived, verify the receiver-side object, and let later versions succeed rather than rewrite earlier ones.**