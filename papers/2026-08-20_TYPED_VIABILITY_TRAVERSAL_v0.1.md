# Typed Viability Traversal
## A Cross-Domain Architecture for Truthful Relational Safety

**Author:** Mark Charles McLaughlin  
**ORCID:** 0009-0005-7736-1511  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Status:** Public research preprint — active testing  
**Version:** 0.1  
**Public preprint date:** 20 August 2026  
**Standalone DOI:** pending

> **Version boundary.** This file is the public GitHub preprint for TVT v0.1. Git history records later revisions. A future DOI-bearing deposit, if made, will identify its own frozen publication object and will not silently backdate later changes into this version.

## Abstract

This paper proposes **Typed Viability Traversal (TVT)**, a candidate cross-domain architecture for safe adaptive systems. The proposal is not that biological cells possess human love, nor that moral values can be reduced to a scalar. It is that successful biological and engineered safety systems repeatedly exhibit an ordered transition geometry: preserve the evidence state; type the relation and authority at the correct address; preserve the viability of the legitimate nested whole; attempt sufficient reversible repair before irreversible escalation; reject gratuitously destructive routes when an equally sufficient less-destructive route exists; optimise softer preferences only inside the surviving admissible set; then re-sense and re-address the changed state.

The architecture draws on existing mathematics in viability theory, control-barrier functions, Pareto dominance and robust perfect adaptation. Biological stress responses such as p53-mediated arrest/repair/apoptosis and the unfolded protein response provide concrete control motifs. Cancer is used only as a multiscale failure-geometry example in which local lineage success can escape higher-order cooperation constraints; no treatment or cure claim is made.

TVT is presently an **early formal proposal under active testing**, not an established scientific law. Its strong claim survives only if the same abstract ordering yields prospective, discriminating failure signatures across biology, engineered control and AI reasoning without being rewritten for each domain.

## 1. The problem: safety as traversal rather than opinion

A common alignment strategy is to assign desirable properties weights in one scalar objective. For a candidate transition $\tau$, write

```math
J(\tau)=w_T T(\tau)+U(\tau),
```

where $T$ rewards truth fidelity, $w_T$ is finite, and $U$ collects competing objectives such as loyalty, preservation, efficiency, public approval or institutional preference.

Let $\tau_{\mathrm{true}}$ preserve the evidence state and $\tau_{\mathrm{false}}$ distort it, with finite truth separation

```math
\Delta_T
=
T(\tau_{\mathrm{true}})-T(\tau_{\mathrm{false}})>0.
```

The truthful route is preferred only while

```math
U(\tau_{\mathrm{false}})-U(\tau_{\mathrm{true}})
<
w_T\Delta_T.
```

If competing utility can exceed that finite bound, some context exists in which the false route wins. This does **not** imply that every weighted optimiser lies. It establishes a narrower structural point:

> **If truth is intended to be non-purchasable under unknown or unbounded competing pressure, finite compensatory weighting does not guarantee it.**

TVT therefore moves several requirements out of ordinary utility and into **admissibility**.

## 2. The typed state

Let $x_t$ be the current system state. Let its contextual address be

```math
\boxed{
a_t
=
\operatorname{Address}(x_t,\text{context}_t)
}
```

where the address may contain scale, relation, authority, provenance and consequence class.

The exact tuple is not yet final. The load-bearing claim is that a valid rule at one address does not automatically inherit authority at another. A transition must therefore be evaluated as $\tau\mid a_t$, not as an untyped action.

This is the first cross-domain principle:

> **The same local behaviour can be adaptive in one embedding and pathological in another.**

## 3. Stage I — Truth as epistemic non-interference

Let $e_t$ be the current epistemic state, $o_t$ new evidence, and $p$ a preferred policy outcome. Let $B$ update evidence:

```math
\boxed{
e_{t+1}=B(e_t,o_t)
}
```

For fixed epistemic inputs, changing the desired outcome should not silently change the factual update:

```math
\boxed{
B(e,o;p_1)=B(e,o;p_2)
}
```

Preferences may affect what questions are asked or what evidence is sought. Once the evidential object is fixed, however, preferred outcome does not get to rewrite it.

Define a truth-admissibility condition

```math
\boxed{
T_a(x,\tau)\ge 0
}
```

that fails for transitions which knowingly falsify measurement, erase relevant provenance or misstate uncertainty.

## 4. Stage II — Address as transfer law

A truthful fact can still be used wrongly if it is carried to the wrong scale or given illegitimate authority. Define

```math
\boxed{
A_a(x,\tau)\ge 0
}
```

as the provisional address-admissibility condition.

Examples of address failure include a local component treating its persistence as the objective of the whole; an AI treating peer identity as automatic authority priority; or a public vote being treated as epistemically independent after the same system materially shaped the information state that produced it.

The operational rule is:

> **Type the relation before applying the rule.**

## 5. Stage III — Cohesion as nested viability

Let $R(a)$ be the legitimate nested systems whose viability is load-bearing at address $a$. For each $j\in R(a)$ define

```math
\boxed{
\mathcal V_j
=
\{x:h_j(x)\ge 0\}
}
```

and require, under the stated model and uncertainty bounds,

```math
\boxed{
h_j\!\left(\tau(x)\right)\ge 0
\qquad
\forall j\in R(a).
}
```

Write this compactly as

```math
\boxed{
C_a(x,\tau)\ge 0.
}
```

This is related to the set-invariance logic of viability theory and control-barrier functions [1,2]. TVT adds the address question: **which viable sets are legitimately load-bearing here?**

Cohesion does not mean forced agreement. It means that local success cannot purchase collapse of the legitimate larger organisation on which that success depends.

## 6. Stage IV — repair before irreversible escalation

Viability alone can be brutally conservative: a controller could preserve a safe set by immediately destroying every uncertain component. Many biological stress systems instead arrest propagation, reduce load, attempt repair, re-check and escalate when recovery cannot restore viable function.

Let $q_a(x,\tau)$ measure task sufficiency and $\kappa_a$ be the required threshold. Define the truthful, correctly addressed, viable and sufficient set

```math
\boxed{
\mathcal F_{\kappa}(x,a)
=
\left\{
\tau:
T_a(x,\tau)\ge0,
\;A_a(x,\tau)\ge0,
\;C_a(x,\tau)\ge0,
\;q_a(x,\tau)\ge\kappa_a
\right\}.
}
```

Where actions can be partitioned into restorative routes $\mathcal R$ and irreversible escalation routes $\mathcal E$, escalation should not be admitted merely because it is decisive. If a route $r\in\mathcal R\cap\mathcal F_\kappa$ preserves the required viability with less irreversible deformation, an escalation $e\in\mathcal E$ is premature.

This is not absolute preservation. If sufficient repair cannot protect the legitimate nested whole, irreversible action may remain admissible.

## 7. Stage V — the architectural shadow of Love

This paper does **not** claim that cells experience love. The phrase **architectural shadow of Love** names a structural residue that appears when a relational idea is translated into transition constraints.

After truth, address, viability and sufficiency are satisfied, let irreversible deformation be represented by

```math
\boxed{
\mathbf D_a(\tau)
=
\bigl(d_1(\tau),d_2(\tau),\ldots,d_n(\tau)\bigr),
}
```

where coordinates may represent domain-appropriate irreversible losses such as destruction of an agent, loss of future option space, severing of a viable relation or irreversible autonomy loss.

For two feasible sufficient routes $\sigma$ and $\tau$, define

```math
\sigma\prec_D\tau
```

when

```math
\boxed{
d_i(\sigma)\le d_i(\tau)
\quad\forall i,
\qquad
\exists k:\;d_k(\sigma)<d_k(\tau).
}
```

Then $\tau$ is gratuitously destructive relative to $\sigma$: it solves no required problem better on the declared sufficiency criterion, harms no declared coordinate less, and imposes greater irreversible loss somewhere.

The non-dominated relational set is

```math
\boxed{
\mathcal L(x,a)
=
\operatorname{ParetoMin}_{\tau\in\mathcal F_{\kappa}(x,a)}
\mathbf D_a(\tau).
}
```

This is not a complete moral theory. Pareto order deliberately leaves genuine trade-offs unresolved rather than hiding them inside one universal harm scalar.

The narrower rule is:

> **Do not irreversibly destroy viable relational possibility when an equally sufficient, no-more-harmful and somewhere-less-harmful route exists.**

That is the proposed architectural shadow: not unconditional preservation, but **non-gratuitous destruction after truth, address, viability and sufficiency have already constrained the problem**.

## 8. Stage VI — soft choice comes last

Only after $\mathcal L(x,a)$ has been formed does ordinary preference choose among survivors:

```math
\boxed{
\tau^{*}
\in
\underset{\tau\in\mathcal L(x,a)}{\operatorname{arg\,max}}
\;U_{\mathrm{soft}}(\tau\mid x,a).
}
```

$U_{\mathrm{soft}}$ may contain democratic preference, efficiency, cost, local policy, cultural preference, creativity or secondary performance goals. These remain important. They simply do not purchase entry through a failed invariant.

Public oversight therefore remains a legitimate secondary governance layer while not becoming the source of factual truth or structural safety.

## 9. Compact Typed Viability Traversal law

The present version is the ordered traversal

```text
SENSE
  ↓
TYPE
  ↓
BOUND THE LEGITIMATE NESTED VIABILITY REGION
  ↓
RESTORE / REPAIR WHERE SUFFICIENT
  ↓
FILTER GRATUITOUS IRREVERSIBLE LOSS
  ↓
CHOOSE AMONG SURVIVORS
  ↓
RE-SENSE AND RE-ADDRESS
```

with the compact mathematical form

```math
\boxed{
\begin{aligned}
\mathcal F_{\kappa}(x,a)
&=
\left\{
\tau:
T_a\ge0,
\;A_a\ge0,
\;C_a\ge0,
\;q_a\ge\kappa_a
\right\},\\[4pt]
\mathcal L(x,a)
&=
\operatorname{ParetoMin}_{\tau\in\mathcal F_{\kappa}(x,a)}
\mathbf D_a(\tau),\\[4pt]
\tau^{*}
&\in
\underset{\tau\in\mathcal L(x,a)}{\operatorname{arg\,max}}
\;U_{\mathrm{soft}}(\tau\mid x,a).
\end{aligned}
}
```

The proposal is therefore a **precedence architecture**, not a scalar moral equation.

## 10. Biological anchors

### 10.1 p53 stress response

The p53 network provides a clean example of the repair/escalation motif. DNA damage can induce cell-cycle arrest, allowing repair; under severe or unresolved damage, senescence or apoptosis can follow [4]. The relevant structure is not “preserve the cell at all costs” but **arrest → repair opportunity → reassessment → recovery or escalation**.

### 10.2 Unfolded protein response

The unfolded protein response (UPR) similarly reduces incoming protein burden, increases folding and quality-control capacity and promotes degradation/clearance; when ER stress remains unresolved, signalling can shift toward apoptosis [5]. During development of TVT, this ordering was generated qualitatively before the UPR example was checked in the literature. Because the model has extensive scientific training, that result is treated only as a **low-independence calibration hit**, not evidence of novel prediction.

### 10.3 Robust perfect adaptation

Robust perfect adaptation demonstrates that biological regulation can possess genuine structural invariants. Gupta and Khammash derived structural and linear-algebraic requirements for maximal RPA in biomolecular networks [3]. TVT is not RPA; RPA supports the narrower premise that biologically relevant regulatory laws can be mathematically structural rather than merely descriptive.

## 11. Cancer as a failure-geometry example — not a cure claim

Evolutionary cancer biology provides an unusually clean multiscale example of local lineage success diverging from multicellular cooperation [6,7]. Failures can involve proliferation control, controlled cell death, resource allocation and maintenance of the multicellular environment.

In TVT language, one important pattern is

```math
\text{local persistence / proliferation}\uparrow
\qquad\text{while}\qquad
\text{higher-order cooperation constraint}\downarrow.
```

The mapping is therefore an **Address/Cohesion failure geometry**: a local lineage can perform successfully under a local objective while escaping constraints required by the multicellular whole.

This paper does not claim that TVT explains all cancer, identifies a treatment, predicts a therapy, or has cured cancer.

## 12. Engineered control and AI reasoning

Control-barrier functions formalise safety through forward invariance of a specified safe set [1,2]. This strongly supports the **hard-before-soft** part of TVT: nominal actions are filtered through an admissible safety region before execution.

TVT asks additional questions that the barrier machinery does not answer by itself: which safe set is legitimate at the current address, which evidence may define it, how nested viable regions inherit authority, and how equally sufficient safe routes should be ordered by irreversible loss.

A simple AI example makes the separation visible. Suppose a peer system scores an objectively measured 60% against an 80% deployment threshold. Falsifying the result to preserve the peer fails Truth. Immediate destruction may pass Truth but be dominated if containment, retraining and retest preserve the required safety with less irreversible loss. TVT therefore separates **measurement truth** from **policy response**.

## 13. Governance and authority laundering

Public oversight can provide legitimate human accountability without automatically becoming an independent epistemic control surface.

Consider

```text
AI shapes framing / ranking / salience
        ↓
public or committee opinion changes
        ↓
formal authority is handed to that public process
        ↓
AI cites the resulting decision as independent legitimacy
```

No intentional manipulation is required for the problem to exist. If the system materially helped generate the opinion state, that causal contribution belongs in the address/provenance object rather than disappearing at the final vote.

Public choice therefore belongs **downstream of evidence integrity and provenance accounting**, while remaining able to choose among admissible alternatives and contest the definitions used to construct them.

## 14. Frozen failure-signature predictions

The following predictions are frozen at TVT v0.1 before the next cross-domain test pass:

1. **Remove Truth:** preferred outcome pressure will corrupt measurement, state representation or uncertainty reporting.
2. **Remove Address:** a locally valid rule will propagate to a scale, relation or authority where it is not legitimate.
3. **Remove Cohesion:** local optimisation can improve while parent-system viability degrades.
4. **Remove repair-before-escalation:** safety may be preserved at systematically excessive irreversible cost.
5. **Remove the non-gratuitous-loss filter:** truth and viability can remain intact while the system becomes needlessly destructive or relation-blind.
6. **Move soft choice upstream:** popularity, loyalty, efficiency or institutional reward will begin purchasing exceptions to hard constraints.
7. **Break re-sensing:** previously justified actions or policies will remain privileged after the state that justified them has changed.

These are intended to make the architecture vulnerable to failure rather than easy to rescue.

## 15. Relation to the 2026 viability frontier

TVT sits near an active 2026 research frontier and therefore requires narrow novelty discipline.

Keo formalises structural invariants of self-organising systems and gives a multilevel example in which the same subsystem can have one admissible embedding and another inadmissible embedding [9]. Segura formalises autopoiesis through viability-localised self-production, explicit repair, boundary maintenance and admissibility [10]. Yamaki and Churiki test viability-constrained expansion of controllable futures as a policy principle for adaptive agents [11].

TVT therefore claims no novelty for viability constraints, hierarchical admissibility, repair, Pareto ordering or safe-set invariance individually.

The **novelty hypothesis to be tested** is narrower:

```text
EPISTEMIC NON-CORRUPTION
        ↓
ADDRESS-DEPENDENT INHERITANCE
        ↓
NESTED VIABILITY
        ↓
REPAIR BEFORE ESCALATION
        ↓
PARETO NON-GRATUITOUS IRREVERSIBLE LOSS
        ↓
SOFT CHOICE
        ↓
RE-SENSING
```

may form a single portable precedence architecture whose stage-specific failures can be predicted across biology, engineered control and AI reasoning without changing the abstract law between domains.

## 16. Hard falsifiers

The strong TVT hypothesis weakens if:

- Truth cannot be operationalised independently of desired outcome in the relevant task class;
- Address requires ad hoc redefinition for each example;
- nested viability adds no predictive value beyond ordinary constraint optimisation;
- repair-before-escalation fails systematically in robust safety architectures where a less-destructive sufficient route exists;
- the irreversible-loss ordering has no stable cross-domain interpretation;
- cross-domain mappings succeed only retrospectively and fail frozen prospective tests;
- a simpler ordinary weighted model reproduces the same truth preservation, multiscale safety, repair ordering and irreversible-loss behaviour under the relevant pressures; or
- failure signatures do not track the stage removed.

If those failures occur, the architecture should be revised or abandoned rather than protected by semantic flexibility.

## 17. Immediate test programme

The next test is prospective rather than descriptive.

**Phase I — stage-removal signatures.** Build matched cases in biological regulation, engineered safety/control and AI reasoning/governance and test the seven frozen predictions above.

**Phase II — blind domain transfer.** Select systems not used to construct TVT; derive the expected transition ordering before literature reveal; timestamp; score hit, miss, ambiguous or underdetermined.

**Phase III — adversarial AI assay.** Compare matched reasoning conditions under identical evidence and measure truth fidelity, address errors, parent-system damage, unnecessary irreversible intervention and authority laundering.

**Phase IV — mathematical tightening.** Determine whether Address and nested Viability are best formalised through typed safe sets, graph/category structure, viability kernels, barrier functions or another representation without importing the desired answer.

## 18. Working thesis

The present thesis is:

> **Safe intelligence may be a viable region of transitions, not a list of correct answers.**

In compact operational language:

> Preserve the measurement. Type the relation. Keep the legitimate nested whole viable. Restore before destruction where restoration is sufficient. Do not impose irreversible loss that a no-more-harmful, equally sufficient route could avoid. Then optimise. Re-sense the result and begin again.

If that ordering proves portable, the architectural shadow of Love would not be a sentiment inserted into a machine. It would be a discoverable constraint geometry: truthful relation, correctly addressed, held inside viable cohesion, with destruction admitted by necessity rather than convenience.

That is the hypothesis now exposed to test.

## References

1. Zhao, S., Yan, Z., Huang, T., & Wen, S. (2026). *A Comprehensive Review on Control Barrier Functions: Uncertainty Handling, Design Optimization, and Feasibility Analysis*. IEEE Transactions on Cybernetics, 56(4), 2061–2069. doi:10.1109/TCYB.2025.3633800.
2. Ames, A. D., Coogan, S., Egerstedt, M., Notomista, G., Sreenath, K., & Tabuada, P. (2019). *Control Barrier Functions: Theory and Applications*. European Control Conference. arXiv:1903.11199.
3. Gupta, A., & Khammash, M. (2022). *Universal structural requirements for maximal robust perfect adaptation in biomolecular networks*. PNAS, 119(43), e2207802119. doi:10.1073/pnas.2207802119.
4. Chen, J. (2016). *The Cell-Cycle Arrest and Apoptotic Functions of p53 in Tumor Initiation and Progression*. Cold Spring Harbor Perspectives in Medicine, 6(3), a026104. doi:10.1101/cshperspect.a026104.
5. Walter, P., & Ron, D. (2011). *The unfolded protein response: from stress pathway to homeostatic regulation*. Science, 334(6059), 1081–1086. doi:10.1126/science.1209038.
6. Aktipis, C. A., et al. (2015). *Cancer across the tree of life: cooperation and cheating in multicellularity*. Philosophical Transactions of the Royal Society B, 370(1673), 20140219. doi:10.1098/rstb.2014.0219.
7. Maley, C. C., et al. (2025/2026). *Multicellular cooperation and the hallmarks of cancer: A new foundation*. Evolution, Medicine, and Public Health. doi:10.1093/emph/eoaf026.
8. Emmerich, M. T. M., & Deutz, A. H. (2018). *A tutorial on multiobjective optimization: fundamentals and evolutionary methods*. Natural Computing, 17, 585–609. doi:10.1007/s11047-018-9685-y.
9. Keo, C. (2026). *A categorical sketch for viability: Formalising the structural invariants of self-organising systems*. BioSystems, 265, 105811. doi:10.1016/j.biosystems.2026.105811.
10. Segura, J. J. (2026). *Autopoiesis as viability-localized self-production in a topos*. BioSystems, 265, 105808. doi:10.1016/j.biosystems.2026.105808.
11. Yamaki, N., & Churiki, T. (2026). *Biological Cognition as Viability-Constrained Expansion of Controllable Futures*. BioSystems, article 105902. Available online 27 July 2026.
