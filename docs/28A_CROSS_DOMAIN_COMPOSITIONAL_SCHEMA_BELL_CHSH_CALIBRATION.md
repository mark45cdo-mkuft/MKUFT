# 28A — Cross-Domain Compositional Schema Bell/CHSH Calibration

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Parent experimental owner:** [28 — MKUFT Discriminating Experiments and Promotion Gates](28_MKUFT_DISCRIMINATING_EXPERIMENTS_AND_PROMOTION_GATES.md)  
**Future-sufficiency owner:** [33S7A — Future-Sufficient Address Invariant and Layer-Before-Law Precedence](33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md)  
**Bell correspondence control:** [Bell Constraints as Typed Boundaries v1.0](../papers/2026-08-25_BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0.md), DOI `10.5281/zenodo.22100926`  
**Compositional-schema source:** *Cross-Domain Compositional Schema: Future-Sufficient Interfaces, Typed Partial Instantiation, and Minimal Restorative Descent*, v0.2, DOI `10.5281/zenodo.22164562`  
**Claim discipline:** [29 — MKUFT Scientific Tightening and Claim Discipline](29_MKUFT_SCIENTIFIC_TIGHTENING_AND_CLAIM_DISCIPLINE.md)  
**Status:** public methodological calibration protocol. It reports no new Bell result, no new Bell inequality, no new derivation of Tsirelson's bound, and no new physical mechanism.

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