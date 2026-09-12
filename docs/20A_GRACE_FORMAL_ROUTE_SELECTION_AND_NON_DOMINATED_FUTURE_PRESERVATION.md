# 20A — GRACE Formal Route Selection and Non-Dominated Future Preservation

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Current principal MKUFT publication:** [10.5281/zenodo.21973064](https://doi.org/10.5281/zenodo.21973064)  
**MKUFT concept DOI:** [10.5281/zenodo.17780565](https://doi.org/10.5281/zenodo.17780565)  
**Parent:** [20 — GRACE Traversal Rule](20_GRACE_TRAVERSAL_RULE.md)  
**Address/future parent:** [33S6 — Addressed Admissible Futures](33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md)  
**Equation discipline:** [27 — Typed Traversal and Equation Hygiene](27_TYPED_TRAVERSAL_AND_EQUATION_HYGIENE.md)  
**Agency/capture support:** [23 — Agency Accessibility and Capture Geometry](23_AGENCY_ACCESSIBILITY_AND_CAPTURE_GEOMETRY.md)  
**Public formalisation date:** 12 September 2026  
**Status:** public applied formalisation of the existing GRACE care-preserving route-selection kernel. It adds no new S–I–P–O layer, force, field, universal moral scalar, or independent physical law.

## 1. Purpose

GRACE already fixes the ordering:

```text
truth / evidence / law / safety / consent / permission / declared target
→ surviving lawful routes
→ care-preserving route comparison
→ realised transition
→ verification and readdressing
```

The missing mathematical bridge is narrow: make the route-comparison step explicit without reducing dignity, agency, repair, provenance, reversibility, restorative reachability, or target performance to one invented utility score.

The formal object here is therefore a **set-valued route selector under hard admissibility and typed, coordinate-wise comparison**.

It asks:

> **Among routes that are already admissible and capable of doing the declared job, which routes are needlessly destructive because another available route is no worse on every retained target and future-bearing coordinate and materially better on at least one?**

The result is deliberately weaker than a universal optimiser. It removes materially dominated routes. It does not manufacture a unique answer where the remaining values are genuinely incommensurable.

## 2. Declared system specification

Let `A_t` be the addressed state at time `t`. Let `\mathcal U_t` be the candidate action/intervention family available at that address.

Let `\Sigma` contain the declared decision specification, including as applicable:

- target variables and success conditions;
- prediction horizon;
- evidence state and measurement resolution;
- law, safety, consent, permission, authority, and boundary constraints;
- admissible intervention class;
- relevant affected-node addresses;
- target-performance readouts;
- future-bearing preservation readouts;
- uncertainty model and coordinate-specific materiality tolerances;
- stopping, verification, and readdressing conditions.

No field enters `\Sigma` merely because it sounds morally desirable or mathematically convenient. Every quantitative coordinate must terminate in a domain-native object, measurement, operational judgement, or falsifiable comparison at the scope claimed.

## 3. Hard admissibility comes first

Define a typed admissibility predicate

```math
\mathsf{Adm}_{\Sigma}(u\mid A_t)\in\{0,1\}.
```

Then

```math
\boxed{
\mathcal U_{\mathrm{adm}}(A_t;\Sigma)
=
\{u\in\mathcal U_t:\mathsf{Adm}_{\Sigma}(u\mid A_t)=1\}.
}
```

The predicate may itself be composed from several domain-native hard gates. The notation does **not** imply that truth, law, safety, consent, permission, or authority are naturally one numerical variable.

GRACE cannot restore an inadmissible route by assigning it a high care value. If a relation must lawfully end, if consent is absent, if a safety boundary dominates, or if an action is outside authority, that route remains outside `\mathcal U_{\mathrm{adm}}`.

This preserves the parent rule:

> **Care chooses among surviving lawful routes; it does not edit the truth surface.**

## 4. Target sufficiency without counterfeit scalarisation

Let the declared target-performance profile be

```math
T_{\Sigma}(u)
=
\bigl(T_1(u),\ldots,T_k(u)\bigr),
```

where each component has its own native meaning, direction, units or normalisation, uncertainty, and tolerance.

Where the task has a clear sufficiency gate, define

```math
\mathsf{Task}_{\Sigma}(u\mid A_t)\in\{0,1\}
```

and

```math
\mathcal U_Q
=
\{u\in\mathcal U_{\mathrm{adm}}:
\mathsf{Task}_{\Sigma}(u\mid A_t)=1\}.
```

A task may instead retain a typed vector of acceptable target outcomes rather than one threshold. Nothing in this module requires a single scalar objective.

## 5. Reciprocal affected-node address recruitment

For each materially affected receiving node `j`, let the candidate receiver-side address be schematically

```math
\Theta_j=(S_j,R_j,C_j),
```

where the components retain the meanings established in Module 20: relevant state, represented situation where operationally available, and relevant constraint/context state.

Reported, directly observed, and inferred components remain separately typed. An inferred private state does not become an observation because it appears inside a tuple.

Receiver-side coordinates are recruited through the future-sufficiency burden already owned by Module 33S6. Let `\Theta^{\mathrm{full}}` be the current evidence-supported candidate address and let

```math
\Theta^{-j}
=
\operatorname{Drop}
\left(
\Theta^{\mathrm{full}};\Theta_j
\right)
```

be the same candidate address with node `j`'s proposed receiver-side coordinate removed. `Drop` is a typed ablation operator, not subtraction in a homogeneous vector space.

Using the target-relative address residual `\mathcal R_q` from Module 33S6, retain the receiver-side coordinate only when its omission produces unresolved future aliasing beyond the declared tolerance under a challenge capable of exposing the distinction:

```math
\boxed{
j\in J^*
\quad\Longleftrightarrow\quad
\mathcal R_q\!\left(\Theta^{-j}\right)>\varepsilon_q.
}
```

Operationally, this means that erasing the receiver-side coordinate would merge states that require materially different target-relevant continuations. If the full candidate address itself still fails the sufficiency test, address closure remains provisional; the receiver coordinate is not allowed to hide an unresolved residual elsewhere.

The receiver-aware address is then written schematically as

```math
A_t^{\mathrm{rec}}
=
\operatorname{Aug}
\left(
A_t;
\{\Theta_j:j\in J^*\}
\right).
```

`Aug` is likewise a typed augmentation operator, not ordinary vector addition. A null receiver branch contributes nothing.

This keeps the operational boundary explicit:

```text
MODEL(j) ≠ ENDORSE(j) ≠ OBEY(j)
```

Receiver state can improve prediction or route choice without inheriting truth, permission, authority, objective custody, innocence, or veto power.

## 6. Future-bearing preservation profile

For every `u\in\mathcal U_Q`, let the projected or realised transition produce the next addressed state

```math
A_{t+1}^{(u)}.
```

Define a declared future-bearing preservation profile

```math
\Phi_{\Sigma}(u)
=
\bigl(
\phi_1(u),\ldots,\phi_m(u)
\bigr).
```

Each `\phi_r` must be domain-native and oriented so that a larger value means more of the declared desirable capacity is preserved, unless another sign convention is stated explicitly.

Possible coordinates, only where independently operationalised, include:

- restorative-future reserve `\rho_R(A_{t+1}^{(u)})` from Module 33S6;
- restorative-route existence `\chi_R` where existence is the relevant discriminator;
- practical agency/accessibility from Module 23;
- correction-channel integrity or truthful-feedback capacity;
- reversibility or bounded rollback capacity;
- provenance/record continuity;
- retained lawful capability;
- retained lawful relationship or interface where that relation is itself admissible and future-bearing;
- negative irreversible-loss coordinates derived from declared `D_{\mathrm{irr}}` components.

This list is **not** a mandatory universal vector. A coordinate that does no work in the receiving domain returns null.

In particular, `relationship preserved` is not automatically good. An unsafe, coercive, captured, deceptive, or otherwise inadmissible relation may need to terminate. GRACE preserves **lawful future-bearing structure**, not relation-for-relation's-sake.

## 7. Combined route profile

Define the typed combined route profile

```math
Z_{\Sigma}(u)
=
\bigl(
T_{\Sigma}(u),
\Phi_{\Sigma}(u)
\bigr).
```

This is a product of typed coordinates. It is **not** permission to sum metres, probabilities, legal permissions, dignity judgements, agency measures, task scores, and recovery reserves into one number.

For each retained coordinate `r`, let `\varepsilon_r\geq0` be a declared materiality threshold reflecting measurement resolution, uncertainty, decision relevance, or another domain-native reason. These thresholds must not be tuned after outcome inspection merely to produce a preferred route.

## 8. Material non-dominance

For two admissible task-sufficient routes `u,v\in\mathcal U_Q`, orient every retained coordinate so that larger is better and define ordinary coordinate-wise no-worse relation

```math
v\succeq_{\Sigma}u
\iff
Z_r(v)\ge Z_r(u)
\quad\forall r.
```

Define **material dominance** by

```math
\boxed{
v\succ_{\Sigma,\varepsilon}u
\iff
v\succeq_{\Sigma}u
\quad\land\quad
\exists r:
Z_r(v)>Z_r(u)+\varepsilon_r.
}
```

Thus tolerance is used to require at least one material improvement; it is not used to excuse a known worsening on another retained coordinate.

The GRACE surviving route set is the material non-dominated frontier

```math
\boxed{
\mathcal U_{\mathrm{GRACE}}
=
\left\{
 u\in\mathcal U_Q:
 \not\exists v\in\mathcal U_Q
 \text{ such that }
 v\succ_{\Sigma,\varepsilon}u
\right\}.
}
```

Interpretation:

> **A route is removed when another lawful, task-sufficient route is no worse on every retained target and future-bearing coordinate and materially better on at least one.**

This is the formal version of avoiding **unnecessary destruction**.

It is Pareto-like rather than scalar. If one route improves task performance while another preserves substantially more agency or restorative reserve, neither may dominate. GRACE does not invent an exchange rate between them.

## 9. Existence, multiplicity, and unresolved choice

The first emptiness test occurs **before** GRACE comparison:

```math
\mathcal U_Q=\varnothing
```

means that no candidate route currently survives both hard admissibility and the declared task-sufficiency burden. GRACE must not manufacture a restorative or gentle route merely because one would be preferred.

For a finite non-empty candidate set `\mathcal U_Q`, at least one materially non-dominated route exists under the relation above. The resulting `\mathcal U_{\mathrm{GRACE}}` may contain one route or several.

- **One route:** the declared profile leaves one material non-dominated survivor.
- **Several routes:** use a domain-native priority rule already justified by the task, retain the set for higher-authority choice, gather a discriminator, or acknowledge genuine underdetermination.

For infinite or continuous candidate families, existence of an attained non-dominated frontier may require domain-appropriate regularity, compactness, closure, or approximation assumptions. Failure to attain an optimum or frontier is a mathematical/engineering issue, not permission to smuggle in a preferred moral answer.

A lexicographic priority is allowed only when the ordering is part of `\Sigma` and has independent justification. A weighted sum is allowed only when the receiving domain genuinely supplies defensible commensuration. Neither is the default.

## 10. Uncertainty-aware dominance

Where route coordinates are estimated with uncertainty, material dominance should not be asserted from point estimates alone when the declared uncertainty can reverse the result.

A conservative certified relation may be written

```math
v\succ^{\mathrm{cert}}_{\Sigma,\varepsilon}u
```

only when the no-worse relation on every retained coordinate and at least one material improvement survive the declared uncertainty model.

If uncertainty leaves the routes incomparable, retain both or gather more information. This prevents false precision from turning GRACE into a rhetorical preference engine.

## 11. Recursive readdressing

GRACE route selection is not a one-shot plan frozen at `t`.

The complete recursion is

```math
\boxed{
A_t
\rightarrow
A_t^{\mathrm{rec}}
\rightarrow
\mathcal U_{\mathrm{adm}}
\rightarrow
\mathcal U_Q
\rightarrow
\mathcal U_{\mathrm{GRACE}}
\rightarrow
u_t
\rightarrow
A_{t+1}
\rightarrow
\text{readdress and repeat}.
}
```

Here `\nu_t\in\mathcal U_{\mathrm{GRACE}}` denotes the route actually selected for execution under the applicable authority and any justified tie-breaking rule.

After the realised transition, the unexecuted suffix of an earlier plan retains standing only if it remains admissible from `A_{t+1}`, as already required by Module 33S6.

This is the mathematical reason GRACE evaluates consequences at the state actually reached rather than treating an earlier humane intention as proof that later steps remain humane, lawful, effective, or recoverable.

## 12. Non-gratuitous-loss invariant

The public care/love/grace orientation can now be stated without inventing a `love score`:

> **Among routes that already satisfy the hard boundary and declared task, do not choose a route whose additional destruction is unnecessary because another available route is no worse on every retained target and future-bearing coordinate and materially better on at least one.**

This is a route-selection invariant, not a law of fundamental physics.

It does **not** mean:

- never terminate a relationship;
- never impose a cost;
- never use force or containment where lawfully required;
- every node is recoverable;
- every future should remain open;
- an adversary's preferred outcome deserves preservation;
- local comfort outranks truth, law, safety, consent, or the declared target.

It means only that **gratuitous loss does not become virtuous merely because the chosen route is effective**.

## 13. Twelve-axis validation matrix

A serious implementation should test the formal bridge across at least these twelve axes when they are relevant:

1. **Hard-boundary invariance** — an inadmissible route cannot re-enter because it scores well on preservation.
2. **Target sufficiency** — GRACE does not protect a route that fails the declared task merely because it is gentle.
3. **Dominated-route elimination** — a route with equal target performance and strictly worse future-bearing consequences should be removed.
4. **Non-scalar conflict** — when routes trade target gain against agency, recoverability, reversibility, or another typed value, the model should preserve incomparability unless a justified priority resolves it.
5. **Receiver-state ablation** — removing a genuinely load-bearing receiver coordinate should deform prediction or route choice in the preregistered direction; removing a null coordinate should not.
6. **Reported / observed / inferred separation** — receiver self-report, direct observation, and inferred private state must not silently collapse into one evidence class.
7. **Adversarial non-inheritance** — modelling a hostile or distorted node may change prediction without transferring its objective, interpretation, permission, or moral authority.
8. **Unsafe-relation termination** — the framework must permit a relation or interface to end where the hard boundary requires it; continuity itself is not a universal preservation target.
9. **Multi-node conflict** — several affected nodes remain separately addressed; no averaging into a single welfare scalar occurs unless the receiving domain justifies that aggregation.
10. **Uncertainty robustness** — apparent dominance that disappears under declared uncertainty must not be reported as settled.
11. **Recursive readdressing** — a route chosen at `t` must be reconsidered when its realised transition changes the Address, admissible set, or future-bearing geometry.
12. **Native termination / reduction** — every quantitative coordinate must terminate in a receiving-domain owner and ablation/failure condition; if GRACE adds no predictive, route-selection, repair, or future-bearing distinction beyond the native model, the stronger GRACE claim contracts for that regime.

These are validation axes, not twelve compulsory numerical dimensions. A null axis backgrounds when the object gives it no load-bearing role.

## 14. Minimal implementation sketch

```text
INPUT:
  current Address A_t
  candidate routes U_t
  declared specification Σ

1. Recruit only receiver-side coordinates that pass future-sufficiency / ablation.
2. Remove routes that fail truth/evidence/law/safety/consent/permission/authority boundaries.
3. Remove routes that fail the declared task.
4. Build only domain-native target and future-bearing readouts that can change the decision.
5. Compare surviving routes coordinate-wise under the declared uncertainty model.
6. Remove materially dominated routes.
7. If one route survives, execute if authority permits.
8. If several survive, apply a justified domain priority, gather a discriminator, escalate, or retain the unresolved set.
9. Verify realised downstream deformation.
10. Readdress from the state actually reached and repeat only where the object changed.
```

## 15. Ablation programme

The formal bridge earns standing only if removing it produces a predicted deformation.

Useful matched comparisons include:

### A. GRACE-on versus GRACE-off

Hold hard admissibility and task success constant. Remove the non-dominance comparison. Test whether the reduced system chooses routes with avoidable losses in restorative reserve, agency/access, correction capacity, provenance continuity, reversibility, or another preregistered future-bearing coordinate.

### B. Receiver-aware versus receiver-ablated

Hold the contemplated interaction fixed. Remove one candidate receiver-side coordinate. Test whether the predicted receiving-node response, safety result, route ranking, repair target, or future geometry changes as predicted.

### C. Full typed profile versus scalarised proxy

Compare the coordinate-wise route selector with a one-number proxy. Test whether scalarisation hides hard trade-offs, makes incommensurable routes appear ordered, or selects a route that is dominated in the original typed profile.

### D. Static plan versus recursive readdressing

Hold the starting plan fixed. Introduce a transition that changes one load-bearing Address coordinate. Test whether the static policy continues down an obsolete route while the readdressed policy lawfully changes continuation.

A null result is informative. If the formal bridge does not improve the declared outcome or expose a reproducible route distinction under an adequate test, its claimed load-bearing role contracts for that domain.

## 16. Relationship to the wider MKUFT body

This module does not duplicate the existing formal owners.

- **Module 20** owns the GRACE traversal and care-preserving route rule.
- **Module 23** owns agency accessibility, capture, lawful remainder, and restorative release.
- **Module 27** owns equation/type hygiene and blocks false commensuration.
- **Module 33S6** owns future-sufficient Address, restorative-future geometry, reserve, counterfactual load-bearing relation, and recursive readdressing.
- **Module 33S7C** owns observer-bounded recursive discrimination and future-sufficient stopping of additional viewpoint depth.

The present module supplies only the missing bridge:

```text
hard admissibility
→ target-sufficient survivors
→ typed target + future-bearing profile
→ material non-dominance
→ surviving route set
→ realised transition
→ readdressing
```

## 17. Failure and reduction conditions

The formalisation should be rejected, reduced, or rewritten where any of the following survives audit:

- a supposed hard constraint is actually a soft preference;
- target or preservation coordinates cannot be operationalised at the claimed scope;
- coordinate direction is chosen after seeing which route it favours;
- unrelated units are silently added or weighted without domain justification;
- receiver state is inferred without evidence and treated as known;
- relationship preservation is rewarded even when the relation itself is unsafe or inadmissible;
- a dominated route is retained only because it is narratively preferred;
- a genuine target/preservation trade-off is falsely presented as mathematical dominance;
- uncertainty can reverse the ranking but is omitted;
- local route success is promoted into whole-system restoration without checking downstream geometry;
- a native domain model already supplies the full demonstrated result and no independent GRACE residual remains;
- the formalism becomes too expensive or complex for the distinction it actually preserves.

## 18. Compact statement

> **Fix the truth and boundary first. Keep only routes that genuinely do the job. Represent future-bearing consequences in their own native coordinates. Remove routes that are needlessly worse without inventing a universal exchange rate between dignity, agency, safety, recovery, provenance, and performance. Then act from the state actually reached and test again.**
