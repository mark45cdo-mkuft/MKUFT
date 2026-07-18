# 22A — Recursive Address Closure and Property Transmission

<!-- MKUFT-PROVENANCE-HEADER:START -->
**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** `10.5281/zenodo.17780566`  
**Provenance:** This module is part of the public MKUFT canon. Exact revisions are timestamped by Git history.  
**Citation:** See [`PROVENANCE_DOI_AND_ATTRIBUTION.md`](../PROVENANCE_DOI_AND_ATTRIBUTION.md).  
<!-- MKUFT-PROVENANCE-HEADER:END -->

**Rights:** “Public” describes visibility, not a licence. See [`RIGHTS_AND_LICENSE_NOTICE.md`](../RIGHTS_AND_LICENSE_NOTICE.md) and [`MODULE_RIGHTS_MATRIX.md`](../MODULE_RIGHTS_MATRIX.md) for the exact current-version status.

**Status:** Public structural folding and companion addendum to module 22  
**Role:** require recursive re-analysis of newly exposed objects and prevent properties from travelling across relations that have not been shown to carry them.

---

## 1. Why this folding is needed

An apparent object may conceal several distinct objects, versions, boundaries, relations, roles, or governing rules.

Naming those parts is not yet a complete analysis. Once decomposition exposes a load-bearing subobject or relation, that result must re-enter the method as a new typed object of analysis.

> The output of object analysis becomes the input of the next analysis cycle.

This is a closure rule for the existing MKUFT addressing architecture. It does not add a new layer, ontology, force, or physical mechanism.

---

## 2. Core rule

> When analysis reveals distinct load-bearing subobjects, every such subobject and every relation between them must be typed in its own right. No property may pass from one object to another unless the connecting relation is explicitly shown to carry that property.

Compressed:

> **No untyped inheritance.**

Adjacency, ancestry, containment, similarity, shared naming, common provenance, and repository membership do not by themselves transmit every property.

---

## 3. Recursive object decomposition

Let an apparent object be `O^(0)`.

A first analysis may expose:

```text
D(O^(0)) = {o_i, r_ij, b_k, v_l, p_m}
```

where:

- `o_i` = distinct subobjects or components;
- `r_ij` = relations between objects;
- `b_k` = boundaries or scopes;
- `v_l` = versions, states, or time-indexed forms;
- `p_m` = properties being asserted, measured, inherited, or transferred.

Every load-bearing element returned by `D` must be assigned an address such as:

```text
T(x) = (domain, layer, boundary, version, role, evidence, status)
```

The tuple is an audit address, not a claim that every domain uses the same metric or mechanism.

If typing `x` reveals further distinct objects or relations, apply `D` again:

```text
O^(0) → D(O^(0)) → T(x) → D(x) → ...
```

The recursion stops only when the load-bearing structure is closed under the analysis conditions below.

---

## 4. Property-transmission rule

Let property `P` belong to object `A`, and let relation `R` connect `A` to object `B`:

```text
A --R--> B
```

The inference

```text
P(A) → P(B)
```

is permitted only when `R` has been defined and supported as a valid carrier of property `P`.

Write the permitted carrier class as `C_P`. Then:

```text
P(A) implies P(B) only if R ∈ C_P
```

The carrier class is property-specific. A relation that carries provenance may not carry licence, evidence, authority, ownership, causation, identity, responsibility, units, or moral status.

Examples of relations that require separate testing rather than automatic inheritance:

- derived from;
- contained in;
- adjacent to;
- resembles;
- cites;
- belongs to the same framework;
- shares a repository;
- follows in time;
- was produced by the same person or organisation.

---

## 5. Recursive address closure

An analysis reaches **recursive address closure** only when:

1. every load-bearing object has an explicit address;
2. every load-bearing relation has a declared type;
3. every relevant boundary and version is distinguished;
4. every claimed property transfer names its carrier relation;
5. evidence is attached to the address where the claim is made;
6. unresolved ambiguity is recorded rather than silently inherited;
7. no conclusion depends on a hidden object, untyped relation, or borrowed property;
8. further decomposition no longer changes the load-bearing conclusion, or any remaining unresolved branch is explicitly bounded.

Closure is therefore not exhaustive knowledge of everything about the object. It is sufficient resolution of every element carrying the present conclusion.

---

## 6. Operational sequence

```text
apparent object
→ decompose
→ identify load-bearing subobjects, versions, boundaries, and relations
→ type each address
→ re-enter each newly exposed load-bearing element
→ test which relations carry which properties
→ run ordinary alternatives and falsifiers
→ declare closure, bounded uncertainty, or failure
```

A practical question set is:

```text
What exact object is this?
Which version or state is active?
What boundary contains the claim?
What subobjects have been exposed?
Which layer and domain does each inhabit?
What relation joins them?
Which property is being transferred?
Does that relation actually carry that property?
What evidence supports the transfer?
What would break the inference?
Has every load-bearing output re-entered the analysis?
```

---

## 7. Legal and publication example

A research framework may contain:

- a frozen deposited paper;
- a later live repository;
- separate source modules;
- a standalone publication;
- later companion modules;
- implementation materials.

These objects may share authorship and provenance while retaining different version, licence, publication, and reuse states.

A DOI reference can carry citation and provenance. It does not automatically carry the DOI-linked work's licence into every later file.

Likewise:

```text
same framework ≠ same version
same repository ≠ same licence
source relationship ≠ automatic licence inheritance
public visibility ≠ public-domain status
```

This is an addressing example, not a substitute for jurisdiction-specific legal advice.

---

## 8. Cross-domain application

The rule is domain-general but must remain domain-typed.

### Science

Evidence for one variable, scale, sample, or layer does not automatically transfer to another because the terms resemble one another.

### Organisations

Authority, responsibility, knowledge, permission, and ownership do not automatically travel through every reporting, contractual, or collaborative relation.

### Information systems

A dependency, import, shared identifier, or common repository does not automatically transfer security status, licence, trust, or semantic meaning.

### Observer and social analysis

Association, continuity, similarity, influence, and shared narrative do not automatically establish identity, intention, responsibility, agreement, or consciousness.

The same audit rule applies, but the carrier relations and evidence requirements must be defined separately in each domain.

---

## 9. Failure modes

- **Object collapse:** distinct objects or versions are treated as one.
- **Premature closure:** decomposition stops after naming components without analysing them.
- **Untyped inheritance:** a property moves across a relation that has not been shown to carry it.
- **Provenance leakage:** origin or citation is mistaken for ownership, licence, evidence, or authority.
- **Containment leakage:** repository, organisational, or physical containment is treated as universal property inheritance.
- **Version leakage:** a rule attached to one state or release is assigned to later or earlier versions without support.
- **Layer leakage:** evidence or mechanism from one S–I–P–O address is borrowed by another.
- **Recursive explosion:** every trivial detail is decomposed without testing whether it carries the conclusion.

The control against recursive explosion is load-bearing relevance: recurse only where the element can change the claim, route, boundary, falsifier, or outcome.

---

## 10. Falsifiers and reduction rule

This folding is weakened if:

- recursive typing adds no discrimination beyond ordinary careful analysis;
- carrier relations cannot be defined even approximately in practical cases;
- the closure test produces arbitrary stopping points;
- different analysts cannot recover the same load-bearing object structure under declared rules;
- the method repeatedly creates complexity without correcting conclusions or exposing hidden assumptions.

Reduction rule:

> If decomposition reveals no conclusion-changing subobject, relation, boundary, version, or property-transfer claim, retain the simpler object description and do not manufacture extra structure.

---

## 11. Architecture placement

```text
parent discipline: docs/22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md
repository traversal: docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md
load-bearing test: docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md
typed hygiene and closure: docs/27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md
falsification: docs/05_FALSIFICATION_SUMMARY.md
```

This module supplies a missing closure condition across those existing documents. It does not replace them.

---

## 12. Compressed canon rule

> Decompose the apparent object. Re-address every load-bearing result. Transfer no property without a typed carrier relation. Stop only at recursive address closure or an explicitly bounded unresolved branch.
