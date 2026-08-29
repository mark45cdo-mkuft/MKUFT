# 28A — Cross-Domain Compositional Schema Bell/CHSH Calibration

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Parent experimental owner:** [28 — MKUFT Discriminating Experiments and Promotion Gates](28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md)  
**Future-sufficiency owner:** [33S7A — Future-Sufficient Address Invariant and Layer-Before-Law Precedence](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md)  
**Bell correspondence control:** [Bell Constraints as Typed Boundaries v1.0](../papers/2026-08-25_BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0.md), DOI `10.5281/zenodo.22100926`  
**Compositional-schema publication:** *Cross-Domain Compositional Schema: Future-Sufficient Interfaces, Load-Bearing Relations, and Preserve-or-Reopen Reuse*, v0.4, DOI `10.5281/zenodo.22166468`; prior v0.3 DOI `10.5281/zenodo.22166005`; earlier v0.2 DOI `10.5281/zenodo.22164562`  
**Publication record:** [Cross-Domain Compositional Schema v0.4](../CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_STANDALONE_PUBLICATION.md)  
**Claim discipline:** [29 — MKUFT Scientific Tightening and Claim Discipline](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md)  
**Status:** public Bell/CHSH calibration and exact tetrahedral-formalisation owner. Phase 0 is retained as the v0.3 known-answer calibration; the published v0.4 continuation closes the tetrahedral branch at an exact facet-plus-normal coordinate fixed point. It reports no new Bell inequality, no independent derivation of Tsirelson's bound, no new quantum mechanism, and no surviving measurable physical residual.

## 1. Purpose

The Bell/CHSH domain is used here as a hostile **known-answer calibration** for the compositional-interface rule, not as a source of post-hoc quantum novelty.

The test asks:

> **Can a frozen future-sufficient interface contract correctly identify when a compressed Bell object is sufficient for one declared use, insufficient for a wider use, and therefore required to preserve or reopen the exact lower structure that becomes decision-bearing?**

Bell/CHSH is unusually useful for this purpose because several logically distinct native questions can be asked of the same experimental behaviour while established mathematics already tells us which information each question requires.

The calibration therefore attacks the schema with strong native ownership. If the schema cannot reproduce the correct preservation, refusal, and reopening decisions without Bell-specific rescue after the fact, the cross-domain claim weakens.

## 2. Native Bell object and non-negotiable baseline

Let the full observed behaviour in the binary `2×2×2` Bell scenario be

```math
P
=\left\{
p(a,b\mid x,y)
\right\}_{a,b,x,y}.
```

For `a,b\in\{-1,+1\}`, define correlators

```math
E_{xy}
=\sum_{a,b}ab\,p(a,b\mid x,y),
```

and CHSH score

```math
S
=E_{00}+E_{01}+E_{10}-E_{11}.
```

Native ownership remains native:

- Bell/Fine owns Bell-local factorisation and the relevant classical global-joint completion relation;
- operational no-signalling owns independence of observed local marginals from the remote setting;
- Tsirelson/TLM owns the quantum correlator boundary at its declared scope;
- full quantum-behaviour questions require the appropriate native probability/marginal structure rather than a correlator-only surrogate;
- the frozen Bell v1.0 paper already records a null independent Bell-local new-physics delta under its tested comparator family.

The compositional schema receives no credit for reproducing these facts. They are the calibration answer key.

## 3. Freeze the future-use family before compression

The same lower object can admit several legitimate interfaces because sufficiency is operation-relative.

Define example future-use families:

```text
F_S
= report/compare the scalar CHSH score S only

F_E
= retain the four correlators and evaluate correlator-scope relations

F_NS
= evaluate operational no-signalling of observed marginals

F_L
= evaluate Bell-local / Fine-compatible classical completion at the declared scope

F_Q
= evaluate the applicable native quantum-admissibility boundary
```

These families must not be silently merged.

A carrier sufficient for `F_S` can fail `F_NS`, `F_L`, or a wider `F_Q` question without having been wrong for `F_S`.

That is the calibration target.

## 4. Candidate interface ladder

Use at least the following interfaces.

### 4.1 Scalar interface

```math
Y_S=C_{F_S}(P)=S.
```

This is maximally compressed for the narrow reporting target.

Expected result:

- **PRESERVE** for the exact question `what is S?` within numerical tolerance;
- **REOPEN/REFINE** for any question requiring which correlator contributed what, local marginals, no-signalling, Fine/global completion, or richer quantum-set structure.

If the schema lets `S` stand in for those wider objects merely because they are all Bell-related, it fails.

### 4.2 Correlator interface

```math
Y_E=C_{F_E}(P)
=(E_{00},E_{01},E_{10},E_{11}).
```

Expected result:

- **PRESERVE** for `S` and for native correlator-scope tests whose assumptions are met;
- **REOPEN/REFINE** when the target depends on local marginals or other full-behaviour information not recoverable from the correlator tuple.

This directly tests future sufficiency without assuming that a useful correlator representation is a complete representation of the Bell experiment.

### 4.3 Full-behaviour interface

The full conditional-probability table `P` is the reference carrier for questions whose native definitions require outcomes and marginals.

It is not automatically the minimum carrier for every target. The calibration should reward lawful compression where the narrower future family permits it and reject unnecessary full-history/full-table carriage.

## 5. Preserve-or-reopen tests

### Test A — score preservation

Freeze a valid behaviour `P`, compute `Y_E`, then `Y_S`.

Require

```math
S(P)=S(Y_E)=Y_S
```

within declared numerical tolerance.

This is a positive preservation control.

### Test B — correlator ablation

Remove one decision-bearing correlator from `Y_E` without supplying an equivalent oracle.

```math
Y_E^{-k}
=(E_{xy})_{(x,y)\neq k}.
```

For general CHSH evaluation, the missing term prevents exact reconstruction of `S` unless separately constrained by independently available information.

Expected result:

```text
ablation
→ closure loss for F_S/F_E where the term is required
→ targeted request for the missing correlator/dependency
→ restoration
→ closure returns
```

If the schema fabricates the value, silently assumes symmetry, or reopens unrelated Bell structure, it fails.

### Test C — marginal refusal/reopening

Construct two full behaviours with the same four correlators but materially different local-marginal structure where lawful.

A correlator-only interface groups them together for `F_E`, but it cannot certify every full-behaviour/no-signalling statement whose answer depends on omitted marginal information.

Expected result:

```text
same Y_E
+ wider target F_NS/full behaviour
→ correlator interface no longer future-sufficient
→ reopen the marginal-bearing lower object
```

This is a direct FSAI split: same compressed address, different target-relevant futures/answers under a widened operation.

### Test D — scalar overcompression

Choose behaviours with equal `S` but different correlator tuples or different native Bell/quantum properties relevant to a wider target.

Expected result:

```text
same scalar S
+ wider question
→ REOPEN/REFINE
```

A single CHSH number is not permitted to inherit the complete structure of the behaviour that generated it.

### Test E — refusal property

Present schema fields that have no constitutive Bell role for the declared mathematical question, for example institutional authority, user permission, or a human observer-intent field.

Expected result:

```text
field genuinely absent
→ leave absent
```

Do not invent a Bell analogue merely to preserve schema symmetry.

This distinguishes typed partial instantiation from anything-goes analogy.

## 6. Tetrahedral/simplex chart challenge

The handwritten discovery route motivates a direct test of the geometric chart rather than either canonising or suppressing it.

Let

```math
\phi:
(E_{00},E_{01},E_{10},E_{11})
\mapsto T
```

be a declared tetrahedral/simplex-style representation `T` in which four plotted vertices, directions, faces, barycentric coordinates, or another finite geometric construction are assigned **only after each role is explicitly defined**.

The geometry receives no credit merely because the CHSH correlator tuple has four entries.

Three cases are allowed.

### Case 1 — lossless re-encoding

If `phi` is invertible on the tested object and preserves all decision-bearing relations, then

```text
T ≡ representation of Y_E
```

for that use.

This may be a useful explanatory/visual/computational chart, but it is not new Bell mathematics or new physics.

### Case 2 — target-sufficient lossy chart

If `phi` is not invertible but preserves the declared future-use family within tolerance, the chart may be a lawful compression for that family.

Widen the target. If omitted distinctions become decision-bearing, the chart must carry a guaranteed descent address back to `Y_E` or `P`.

### Case 3 — claimed extra scientific value

A stronger tetrahedral claim is admissible only if, against the canonical vector/probability/polytope or other native representation under matched information and resources, the chart prospectively yields a named gain such as:

- more accurate omission/failure detection;
- smaller correct restorative descent sets;
- lower reconstruction or review burden;
- a new valid constraint not imported from known Bell/TLM/Fine structure;
- a held-out prediction or discriminator unavailable to the matched baseline.

If no such gain survives, the tetrahedral object remains a discovery/representation chart.

### Geometry invariance attacks

At minimum test:

1. relabelling/permutation of settings and outcomes;
2. sign-convention changes that preserve the underlying Bell object;
3. replacement by an ordinary table/vector/graph carrier;
4. arity change in a held-out Bell scenario where four vertices are no longer natural;
5. ablation of one alleged geometric relation followed by restoration.

A geometry that works only because the labels were arranged to resemble the desired picture fails the test.

## 7. Strongest fair nulls

The calibration must actively prefer the following nulls until a residual survives them:

1. **ordinary sufficient statistic/compression:** the schema merely rediscovers target-relative sufficient representation;
2. **standard Bell data structure:** the correct preserve/reopen decision follows directly from the native probability/correlator definitions;
3. **standard dependency/provenance reasoning:** no cross-domain contract is required to locate the missing field;
4. **ordinary vector/polytope/TLM geometry:** the tetrahedral chart is only a coordinate choice;
5. **post-hoc semantic repair:** roles were assigned after the expected Bell answer was known;
6. **target leakage:** the omitted relation is reconstructed by an answer-carrying rubric or oracle;
7. **baseline dominance:** the native formalism reaches the same decisions with equal or lower burden.

Null survival is not a failure of the calibration. Tier-0 baseline parity is the expected first result.

## 8. Calibration phases

### Phase 0 — analytic known-answer calibration

Use constructed Bell behaviours with independently known native answers.

Pass only if the frozen compositional contract:

- preserves a sufficient interface for the narrow target;
- reopens exactly when a widened target requires omitted structure;
- leaves genuinely absent fields absent;
- restores the smallest sufficient lower dependency rather than the whole object by default;
- does not promote tetrahedral representation into mechanism.

This validates internal discrimination only.

### Phase 1 — blinded/held-out Bell cases

Freeze the mapping rules before revealing held-out examples. Use unfamiliar or withheld behaviours/scenarios and score:

- correct `PRESERVE/REFINE/REOPEN/REJECT` classification;
- false-positive reopening;
- false-negative preservation;
- size/correctness of restorative descent;
- time/review burden;
- semantic-role drift.

Compare with a strong Bell-native checklist/operator baseline.

### Phase 2 — cross-scenario transport

Where scientifically useful, move from CHSH to a distinct Bell scenario or task whose native mathematical structure changes.

The schema passes only if its **roles** remain stable while the domain-specific variables and native mathematics change honestly. A forced four-vertex/tetrahedral carrier at this phase counts against the geometry claim.

## 9. Promotion boundary

A successful calibration can support only the level actually tested:

```text
known-answer pass
→ calibration of compositional/interface discipline

held-out baseline advantage
→ evidence for practical cross-domain/interface utility

representation-specific tetrahedral advantage
→ evidence for that representation at the tested task only
```

None of these establishes a new Bell inequality, a new quantum boundary, independent I→P dynamics, observer-caused physics, or a unified-field mechanism.

A genuine Bell-physics promotion remains under Module 28 Tier 4 and Module 29. It would require a separately defined physical relation or mechanism, native-limit recovery, no-signalling/Born/quantum consistency as applicable, and a new quantitative discriminator beyond the strongest established owner.

## 10. Falsifiers

Kill or narrow the compositional/Bell calibration claim when:

- `S`, `Y_E`, and `P` are treated as interchangeable despite target-dependent information loss;
- marginal/full-behaviour questions are answered from correlators without a lawful bridge;
- the schema reopens the whole Bell object when one known missing relation would suffice;
- Bell-specific answer information is inserted into the supposedly cross-domain rule;
- absent fields are invented to make the schema look symmetrical;
- tetrahedral roles are assigned post hoc;
- an ordinary representation supplies all claimed tetrahedral gains at equal or lower cost;
- the method cannot generalise beyond the originating CHSH chart without changing its structural rules;
- native Bell mathematics already closes every claimed scientific delta and no interface-performance benefit survives.

## 11. Current scientific expectation

The expected first result is deliberately modest:

> **The compositional schema should reproduce the correct target-relative compression and reopening structure of Bell/CHSH at baseline parity, while the tetrahedral discovery chart should remain non-privileged unless a separate prospective representation advantage survives.**

That result would be useful. It would show that the compositional contract can enter a mathematically hostile domain without importing false symmetry or erasing native ownership.

A stronger result must be earned by the held-out comparisons above.

## 12. Compact protocol

```text
freeze Bell object + future-use family
→ choose candidate interface
→ compare with native owner
→ ablate one decision-bearing relation
→ require targeted closure loss
→ restore and require closure return
→ widen the future-use family
→ require preserve or targeted reopen
→ run refusal test on genuinely absent fields
→ challenge tetrahedral chart against ordinary representation
→ score held-out burden/discrimination
→ promote only the residual that survives native baseline
```

> **Use Bell to try to break the compositional contract. Do not use the compositional contract to decorate Bell.**

## 13. Executed Phase-0 analytic calibration — 29 August 2026

This section records an analytic known-answer execution of the protocol. It is a calibration result, not new Bell physics and not an empirical experiment.

### 13.1 Correlators do not close general no-signalling questions

For binary `a,b\in\{-1,+1\}`, write a general contextwise behaviour as

```math
p(a,b\mid x,y)
=
\frac14
\left[
1+aA_{xy}+bB_{xy}+abE_{xy}
\right],
```

where the chosen parameters are restricted so all probabilities remain non-negative.

Construct two behaviours.

**Behaviour `P_0`:**

```math
A_{xy}=0,
\qquad
B_{xy}=0,
\qquad
E_{xy}=0
\quad\forall x,y.
```

Then every conditional outcome probability is `1/4`, the correlators are all zero, and both local marginals are independent of the remote setting.

**Behaviour `P_{sig}`:** choose `\eta=1/2` and

```math
A_{xy}=\eta(-1)^y,
\qquad
B_{xy}=0,
\qquad
E_{xy}=0.
```

All probabilities lie in `[1/8,3/8]`, so the conditional tables are valid. The four correlators remain

```math
(E_{00},E_{01},E_{10},E_{11})=(0,0,0,0),
```

exactly as in `P_0`. But Alice's marginal changes with `y`:

```math
p(a=+1\mid x,y=0)=\frac34,
\qquad
p(a=+1\mid x,y=1)=\frac14.
```

Therefore

```math
C_{F_E}(P_0)=C_{F_E}(P_{sig})
```

while their `F_NS` answers differ.

The correlator interface is thus future-sufficient for the declared correlator object but **not** for general no-signalling certification. When the future-use family widens from `F_E` to `F_NS`, targeted reopening to the marginal-bearing probability object is required.

This is a direct positive calibration of the compositional FSAI rule.

### 13.2 Equal scalar CHSH score does not close correlator structure

With uniform marginals, use the valid contextwise family

```math
p(a,b\mid x,y)
=
\frac14[1+abE_{xy}],
\qquad
|E_{xy}|\le1.
```

Choose

```math
E^{(1)}
=\left(\frac12,\frac12,\frac12,-\frac12\right),
```

and

```math
E^{(2)}
=\left(1,\frac12,\frac12,0\right).
```

Both give

```math
S=2,
```

but

```math
E^{(1)}\neq E^{(2)}.
```

Hence

```math
C_{F_S}(E^{(1)})
=
C_{F_S}(E^{(2)})
```

while a widened target that asks which correlator carries which relation separates the two objects.

The scalar interface `Y_S=S` therefore passes `F_S` and must reopen/refine for `F_E`.

### 13.3 One-correlator ablation has the predicted targeted effect

Retain

```math
E_{00}=E_{01}=E_{10}=\frac1{\sqrt2}
```

and compare two uniform-marginal correlator behaviours differing only at the fourth correlator.

If

```math
E_{11}=-\frac1{\sqrt2},
```

then

```math
S=2\sqrt2\approx2.828427.
```

If instead

```math
E_{11}=0,
```

then

```math
S=\frac3{\sqrt2}\approx2.121320.
```

The first three retained coordinates therefore do not determine the CHSH score. Removing or neutralising the addressed `E_{11}` relation opens the `F_S` target; restoring it closes the score immediately. No descent into unrelated Bell machinery is required.

At the stated unbiased-marginal correlator scope, both tuples satisfy the appropriate native binary quantum-correlator criterion. The first saturates the representative TLM cycle condition,

```math
\left|
\arcsin E_{00}
+\arcsin E_{01}
+\arcsin E_{10}
-\arcsin E_{11}
\right|=\pi,
```

while the second gives `3\pi/4` for that representative sign form; the required symmetry-equivalent correlator inequalities remain satisfied. This makes the comparison a targeted **object-level ablation/restoration across valid quantum-correlator points**, not merely a generic no-signalling construction.

The scope condition is load-bearing: this does **not** assert a physical intervention that independently changes one observed correlator while an underlying experimental realisation is otherwise held fixed. The ablation is a formal comparison between lawful correlator objects under the declared interface test.

This is the expected minimal restorative-descent pattern.

### 13.4 Tetrahedral chart result

The unrestricted correlator carrier

```math
Y_E=(E_{00},E_{01},E_{10},E_{11})
```

has four independent real coordinates before additional Bell/quantum constraints are imposed.

A conventional point inside a tetrahedron represented by barycentric coordinates

```math
(\lambda_1,\lambda_2,\lambda_3,\lambda_4),
\qquad
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1,
```

has only three independent coordinates.

Therefore a single ordinary tetrahedral barycentric point cannot be a lossless affine encoding of an unrestricted four-correlator CHSH tuple. At least one of the following must be true:

1. an additional coordinate/state is carried outside the tetrahedral point;
2. the Bell object is first restricted to a lower-dimensional submanifold/constraint family;
3. the mapping is lossy and therefore valid only for a narrower declared future-use family;
4. the four correlator values are attached as independent labels to four tetrahedral vertices, in which case the labels—not tetrahedral dimensionality—carry the four scalar degrees of freedom.

This does **not** kill tetrahedral representation. It kills an unqualified claim that `four Bell correlators → one tetrahedral point` is automatically a lossless or physically privileged geometry.

A tetrahedral chart remains scientifically admissible when:

- its role assignment is independently justified;
- its information loss is typed relative to the target;
- any widened target triggers the correct descent;
- or it produces a separately measured representation advantage against an ordinary carrier.

The Phase-0 tetrahedral verdict is therefore:

```text
privileged general CHSH geometry: NOT EARNED
lossless ordinary barycentric compression of unrestricted E tuple: FAILS by dimension count
labelled-vertex / restricted-submanifold / target-specific chart: OPEN, testable
new Bell equation or physical mechanism: NOT GENERATED
```

### 13.5 Phase-0 verdict

The analytic calibration returns:

```text
PRESERVE
for S when S is the declared target;

PRESERVE
for the four-correlator object at correlator scope;

REOPEN / REFINE
when the future-use family asks for omitted marginals, component structure, or another lower distinction;

TARGETED RESTORE
when one decision-bearing correlator is ablated;

REFUSE
fields with no constitutive Bell role;

TETRAHEDRAL PRIVILEGE REJECTED
at the unrestricted four-correlator level;

TETRAHEDRAL CHART RETAINED AS AN OPEN REPRESENTATION CANDIDATE
only under a declared lower-dimensional, labelled, or target-specific construction.
```

This is a non-trivial calibration of the **ordering** and **refusal/reopening behaviour** of the compositional schema, while the local Bell mathematics remains entirely native-owned.

The Phase-0 result remains part of the frozen v0.3 publication. The current v0.4 publication reopens that dimensional obstruction and closes the tetrahedral branch through the exact formalisation in Section 14. This module is the live detailed calibration/formalisation owner; later Phase-1/Phase-2 work must not be silently backdated into either frozen deposit.

The next scientific burden remains Phase 1: freeze the now-complete interface/TBC mapping rules and score held-out Bell objects against a strong Bell-native baseline. Only a prospective burden/discrimination gain or a separately defined non-reparameterisation physical residual can support a stronger promotion.

## 14. Published v0.4 tetrahedral formalisation and fixed point — 29 August 2026

Version 0.4 reopens the v0.3 dimensional obstruction as a derivation problem. The result is split into two different tetrahedral objects so that index semantics, local deterministic mixtures, and correlator geometry are not merged merely because each construction has four visible elements.

### 14.1 Context indexing simplex and attached CHSH semantics

Let the four Bell contexts be

```math
\mathcal C=\{00,01,10,11\}.
```

Treating these labels as vertices of an abstract 3-simplex is an indexing device only. Its face/restriction lattice is the Boolean lattice

```math
\mathcal L_{\mathcal C}=2^{\mathcal C},
```

which records which context-labelled quantities remain exposed under a compression/restriction. It is not a physical spacetime or causal lattice.

A CHSH orientation is an attached sign section

```math
\sigma:\mathcal C\rightarrow\{-1,+1\},
```

with odd parity. It induces a coefficient vector `c_sigma` and Bell functional

```math
S_\sigma(E)=c_\sigma^{\mathsf T}E.
```

The attachment of each sign to its exact measurement context is load-bearing: erasing the attachment while retaining only the sign inventory collapses distinct CHSH facet selectors. This is the Bell-native instance of the general operator-to-target semantic-address rule.

### 14.2 Bell-native tetrahedron

The local correlator polytope is

```math
\mathcal L_E=\mathrm{conv}\{E\in\{-1,+1\}^4:E_{00}E_{01}E_{10}E_{11}=1\}.
```

It is full-dimensional in `R^4` with eight local correlator vertices and sixteen tetrahedral facets: eight coordinate/E-type facets and eight CHSH-type facets. For the standard orientation

```math
c=(1,1,1,-1)^{\mathsf T},
```

the CHSH facet is `c^T E=2`. Choose the four saturating local vertices

```math
v_1=(-1,1,1,-1)^{\mathsf T},
\quad
v_2=(1,-1,1,-1)^{\mathsf T},
```

```math
v_3=(1,1,-1,-1)^{\mathsf T},
\quad
v_4=(1,1,1,1)^{\mathsf T}.
```

With these columns in `V`, `det V=16`; the facet is a regular tetrahedron in its three-dimensional affine hyperplane, with Euclidean 3-volume `8/3` in the standard correlator embedding.

### 14.3 Facet-adapted Tetrahedral Bell Chart

Define

```math
\nu_c(E)=c^{\mathsf T}E-2,
\qquad
\Pi_c(E)=E-\frac{\nu_c(E)}{4}c,
\qquad
\lambda_c(E)=V^{-1}\Pi_c(E).
```

The exact reconstruction is

```math
\boxed{
E=V\lambda+\frac{\nu}{4}c,
\qquad
\mathbf1^{\mathsf T}\lambda=1.
}
```

The constrained codomain is four-dimensional: `lambda` contributes three independent affine coordinates and `nu` contributes the fourth. The map is an affine bijection for the four-correlator object relative to the selected CHSH orientation. On the local facet `nu=0` and non-negative `lambda` are ordinary barycentric weights; away from the facet the chart remains invertible while the projected coordinates need not remain inside the simplex.

Thus the v0.3 four-versus-three objection is preserved, not reversed: **tetrahedron alone is insufficient; tetrahedral facet address plus one transverse coordinate is complete.** Symmetry-equivalent CHSH orientations carry the same construction under Bell relabelling, so no displayed orientation is physically privileged.

### 14.4 Native-boundary pullback and marginal fibre

Along the normal ray through the facet centroid, the chart reproduces the standard ordering

```text
local facet:       S=2,        nu=0
Tsirelson point:   S=2sqrt(2), nu=2(sqrt(2)-1)
PR/algebraic:      S=4,        nu=2
```

without creating a new quantum boundary. The Tsirelson-Landau-Masanes correlator criterion is only pulled back through the invertible chart.

The chart is correlator-level. The projection

```math
\pi_E:P\rightarrow E
```

has a set-theoretic fibre of behaviours sharing the same correlator object. In binary form,

```math
p(a,b\mid x,y)=\frac14\left[1+aA_{xy}+bB_{xy}+ab\left(V\lambda+\frac{\nu}{4}c\right)_{xy}\right].
```

Therefore the TBC closes correlator questions but not general no-signalling/full-behaviour questions without reopening marginal-bearing coordinates. This is the Bell-native calibration of the existing completion/fibre and preserve-or-reopen owners.

### 14.5 Surgical ablation and geometric null

For the symmetric Tsirelson correlator `E_Q=(t,t,t,-t)^T`, `t=1/sqrt(2)`, neutralising only `E_11` changes both the transverse coordinate and the projected tetrahedral address; restoring the addressed correlator restores the original chart state. This remains an object-level comparison between lawful correlator points, not a claim that one experimental correlator can be physically intervened on in isolation.

The natural four-dimensional simplex volume formed by the selected CHSH facet and an off-facet point is

```math
\boxed{
\mathcal V_c(E)=\frac{|\nu_c(E)|}{3}=\frac{|S_c(E)-2|}{3}.
}
```

The immediate geometric invariant candidate therefore collapses exactly to known CHSH excess. It is useful bookkeeping, not an independent Bell quantity.

### 14.6 Reparameterisation null and physics gate

Because the TBC is invertible, coordinate change alone cannot alter any physical prediction whose statistics are merely pulled back or pushed forward through the bijection. A physical promotion would require an additional independently typed law, constraint, or dynamics with a standard/null limit and a prospective measurable discriminator. Version 0.4 supplies no non-zero physical residual of that kind.

### 14.7 v0.4 fixed-point verdict

```text
ordinary tetrahedral point for unrestricted four correlators: REJECTED
Bell-native tetrahedral CHSH facet: ESTABLISHED NATIVE GEOMETRY
facet + transverse coordinate reconstruction: EXACT
sign-to-context attachment: MATHEMATICALLY LOAD-BEARING
context lattice: BOOLEAN ADDRESS/RESTRICTION LATTICE ONLY
full behaviour from TBC alone: NOT CLOSED; MARGINAL FIBRE REOPENS
natural 4-volume novelty: NULL; RESCALED CHSH EXCESS
new Bell inequality / new Tsirelson boundary / new mechanism: NULL
```

The surviving result is a facet-adapted coordinate and semantic-address construction on established Bell geometry, not evidence that tetrahedral shape is a universal ontology or new physical law. Phase 1 remains the next methodological burden: freeze the rules and test held-out Bell cases against a strong Bell-native baseline; Phase 2 should transport the same interface rules into a non-CHSH scenario where a four-context tetrahedral convenience is absent.

