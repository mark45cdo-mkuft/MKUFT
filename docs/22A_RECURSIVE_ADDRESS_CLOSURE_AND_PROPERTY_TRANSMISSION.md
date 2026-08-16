# 22A — Recursive Address Closure and Property Transmission

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**MKUFT DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](../PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Rights:** [Rights and Licence Notice](../RIGHTS_AND_LICENSE_NOTICE.md); [Module Rights Matrix](../MODULE_RIGHTS_MATRIX.md)

**Status:** public structural and methodological addendum to Module 22.

## 1. Purpose

An apparent object may conceal distinct objects, versions, boundaries, relations, roles, or governing rules. Naming those parts is not enough. Once decomposition exposes a load-bearing subobject or relation, that result must itself become a typed object of analysis.

> The output of object analysis becomes the input of the next analysis cycle when it still carries the conclusion.

This is a closure rule for the existing MKUFT addressing architecture. It does not add a new layer, ontology, force, or physical mechanism.

## 2. Core rule

> When analysis reveals distinct load-bearing subobjects, every such subobject and every relation between them must be typed in its own right. No property may pass from one object to another unless the connecting relation is shown to carry that property.

Compressed:

> **No untyped inheritance.**

Adjacency, ancestry, containment, similarity, shared naming, common provenance, and repository membership do not by themselves transmit every property.

## 3. Recursive object decomposition

Let the apparent object be $O^{(0)}$. A first decomposition may expose

```math
D(O^{(0)})
=
\{o_i,r_{ij},b_k,v_\ell,p_m\},
```

where $o_i$ are distinct subobjects or components, $r_{ij}$ relations between them, $b_k$ boundaries or scopes, $v_\ell$ versions or time-indexed states, and $p_m$ properties being asserted, measured, inherited, or transferred.

Every load-bearing element returned by $D$ receives a typed address such as

```math
T(x)
=
(\text{domain},\text{layer},\text{boundary},\text{version},\text{role},\text{evidence},\text{status}).
```

The tuple is an audit address rather than a claim that every domain shares one metric or mechanism.

If typing $x$ reveals further distinct load-bearing objects or relations, the process recurses:

```math
O^{(0)}
\rightarrow D(O^{(0)})
\rightarrow T(x)
\rightarrow D(x)
\rightarrow\cdots
```

The recursion stops when further decomposition no longer changes a load-bearing conclusion, route, boundary, falsifier, or outcome, or when the remaining unresolved branch is explicitly bounded.

## 4. Property-transmission rule

Let property $P$ belong to object $A$, and let relation $R$ connect $A$ to object $B$:

```math
A\xrightarrow{R}B.
```

The inference

```math
P(A)\Rightarrow P(B)
```

is permitted only where $R$ has been defined and supported as a valid carrier of property $P$.

Let $\mathcal C_P$ be the permitted carrier class for property $P$. Then

```math
P(A)\Rightarrow P(B)
\quad\text{only if}\quad
R\in\mathcal C_P.
```

The carrier class is property-specific. A relation that carries provenance may not carry licence, evidence, authority, ownership, causation, identity, responsibility, units, or moral status.

Relations requiring separate testing rather than automatic inheritance include **derived from**, **contained in**, **adjacent to**, **resembles**, **cites**, **belongs to the same framework**, **shares a repository**, **follows in time**, and **was produced by the same person or organisation**.

## 5. Recursive address closure

An analysis reaches **recursive address closure** only when:

1. every load-bearing object has an explicit address;
2. every load-bearing relation has a declared type;
3. every relevant boundary and version is distinguished;
4. every claimed property transfer names its carrier relation;
5. evidence is attached to the address where the claim is made;
6. unresolved ambiguity is recorded rather than silently inherited;
7. no conclusion depends on a hidden object, untyped relation, or borrowed property;
8. further decomposition no longer changes the load-bearing conclusion, or the remaining uncertainty is explicitly bounded.

Closure is not exhaustive knowledge. It is sufficient resolution of everything carrying the present conclusion.

## 6. Operational sequence

The method can be summarised as:

**apparent object → decomposition → load-bearing subobjects/versions/boundaries/relations → typed addresses → recursive re-entry → property-carrier test → ordinary alternatives and falsifiers → closure, bounded uncertainty, or failure.**

The practical questions are:

- What exact object is this?
- Which version or state is active?
- What boundary contains the claim?
- What load-bearing subobjects have been exposed?
- Which layer and domain does each inhabit?
- What relation joins them?
- Which property is being transferred?
- Does that relation actually carry that property?
- What evidence supports the transfer?
- What would break the inference?
- Has every load-bearing output re-entered the analysis?

## 7. Publication and version example

A research framework may contain a frozen deposited paper, a later live repository, separate source modules, a standalone publication, later companion modules, and implementation material.

Those objects may share authorship and provenance while retaining different version, licence, publication, and reuse states.

A DOI reference can carry citation and provenance. It does not automatically transmit the licence of the DOI-linked work into every later file.

Therefore:

- same framework does not imply same version;
- same repository does not imply same licence;
- source relationship does not imply licence inheritance;
- public visibility does not imply public-domain status.

This is an addressing example rather than jurisdiction-specific legal advice.

## 8. Cross-domain application

The rule is domain-general but remains domain-typed.

### Science

Evidence for one variable, scale, sample, or layer does not transfer automatically because the terms resemble one another.

### Organisations

Authority, responsibility, knowledge, permission, and ownership do not travel automatically through every reporting, contractual, or collaborative relation.

### Information systems

A dependency, import, shared identifier, or common repository does not automatically transmit security status, licence, trust, or semantic meaning.

### Observer and social analysis

Association, continuity, similarity, influence, and shared narrative do not automatically establish identity, intention, responsibility, agreement, or consciousness.

## 9. Failure modes

- **Object collapse:** distinct objects or versions are treated as one.
- **Premature closure:** decomposition stops after naming components without analysing the parts that still carry the conclusion.
- **Untyped inheritance:** a property moves across a relation not shown to carry it.
- **Provenance leakage:** origin or citation is mistaken for ownership, licence, evidence, or authority.
- **Containment leakage:** organisational, repository, or physical containment is treated as universal property inheritance.
- **Version leakage:** a rule attached to one release is assigned to another without support.
- **Layer leakage:** evidence or mechanism from one S–I–P–O address is borrowed by another.
- **Recursive explosion:** trivial details are decomposed even though they cannot change the conclusion.

Load-bearing relevance prevents recursive explosion: recurse only where the element can change the claim, route, boundary, falsifier, or outcome.

## 10. Falsifiers and reduction rule

The method is weakened if recursive typing adds no discrimination beyond ordinary careful analysis; carrier relations cannot be defined even approximately in practical cases; closure produces arbitrary stopping points; independent analysts cannot recover materially compatible load-bearing structure under declared rules; or the method repeatedly creates complexity without correcting conclusions or exposing hidden assumptions.

Reduction rule:

> If decomposition reveals no conclusion-changing subobject, relation, boundary, version, or property-transfer claim, retain the simpler object description.

## 11. Related public documents

- [Cross-Layer Invariants and Layer Addressing](22_CROSS_LAYER_INVARIANTS_AND_LAYER_ADDRESSING.md)
- [Cross-Support and Traversal Map](24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md)
- [Load-Bearing Invariants and Whole-System Deformation](25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)
- [Falsification Summary](05_FALSIFICATION_SUMMARY.md)

## 12. Compressed rule

> Decompose the apparent object. Re-address every load-bearing result. Transfer no property without a typed carrier relation. Stop only at recursive address closure or an explicitly bounded unresolved branch.
