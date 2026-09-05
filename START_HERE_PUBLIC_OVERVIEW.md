# Start Here — Public Overview of MKUFT

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Current principal publication:** [MKUFT — A Relational Architecture for Physical Law and Cross-Scale Dynamics](https://doi.org/10.5281/zenodo.21973064)  
**MKUFT concept DOI:** [10.5281/zenodo.17780565](https://doi.org/10.5281/zenodo.17780565)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](PROVENANCE_DOI_AND_ATTRIBUTION.md)

This page explains MKUFT in ordinary English first. The formal documents are linked after the idea they are meant to carry.

MKUFT is speculative research. It is not presented as an accepted completed theory of physics.

## Start with the problem, not the vocabulary

A large scientific model can go wrong before an equation is even chosen.

It can choose the wrong object.

It can mix a component with the whole system.

It can treat a useful description as though it were the mechanism itself.

It can borrow a rule from one scale and quietly apply it at another.

It can treat two states as equivalent because they look the same now even though they lead to different futures.

It can measure a local improvement while missing damage exported elsewhere.

A model can be mathematically respectable and still be aimed at the wrong thing. MKUFT is built around that class of failure.

Its central proposal is **Layer Before Law**:

> **Before asking which law governs something, establish what the thing is, where its boundary is, what role it has, what scale is active, what evidence is actually available, and which changes are possible from that state.**

Only after that should the law or effective rule be selected.

## The central object in plain English

A useful picture is a chessboard. Two visible arrangements can look identical while castling rights, repetition history, or en-passant availability make their legal futures different. The lesson is not that nature plays chess. It is that a present snapshot can be too coarse when omitted history or relation changes what may happen next.

MKUFT calls the smallest task-relative description that keeps those future-relevant differences from being falsely merged the effective **Address**. In the formal work it is a typed description: different kinds of state, history, relation, context and registration do not become interchangeable merely because one representation can write them down together.

A variable or distinction belongs in that Address when removing it would merge cases that later separate in a way the declared task cares about. If a realised transition changes which distinctions matter, the system must be addressed again from the state actually reached. The next lawful continuation is not inherited automatically from yesterday's description merely because that description was once sufficient.

The same criterion can recurse upward and downward across scale. A locally closed object can become a constituent in a wider system; if the wider use makes a previously omitted relation decision-bearing, the representation must already preserve it or reopen the smallest lower dependency that owns it. Where an observer or registration state is genuinely part of the declared operation, that state is subject to the same sufficiency burden.

Here is where the picture stops. Semantic, informational, physical, historical, relational, and observer-facing distinctions remain different typed objects. A distinction earns technical status only when preserving or removing it changes a declared prediction, admissible transition, recovery route, closure decision, measurement result, or other prospectively testable consequence. The architecture does not turn every semantic distinction into a physical variable, observation into a new force, or every domain into one universal coordinate set.

There is a semantic consequence worth making explicit. Two statements can both be true while answering different relational addresses. If substituting one for the other leaves the governing question unresolved and changes what the system is allowed to treat as closed or what operations may follow, the semantic distinction has operational load for that task. That is a testable addressing claim, not a claim that semantics is a new physical field.

## The four-layer shorthand

MKUFT often writes:

```math
S \rightarrow I \rightarrow P \rightarrow O
```

These letters are addresses, not four ordinary spatial dimensions.

**S — Substrate** is the proposed deeper possibility/source domain of the model.

**I — Information** is where relations, constraints, roles, addresses, rules, and routing are described.

**P — Physical** is where matter, energy, fields, bodies, instruments, timings, records, and measurable events live.

**O — Observer** is the observer or registration position: what is measured, available, attended to, or conditioned by the measurement context.

The important rule is not the letters. The important rule is: **do not move evidence, laws, or meaning from one address to another without showing the bridge.**

If a physical claim is made, it eventually has to become physical enough to measure.

## How to read equations outside your field

You are not expected to derive specialist equations outside your training in order to follow the architecture. You should still be able to tell what the variables stand for, what relation is being asserted, why that relation matters, and what result would make the claim fail.

The [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md) carries that handoff into the technical modules. It explains the purpose and broad meaning of the equations without replacing the specialist mathematics or pretending that a non-specialist has verified a derivation they have not checked.

## A simple example of why address matters

Imagine three descriptions of the same organised system:

- a list of its parts;
- a map of how the parts are connected;
- a description of the whole system's behaviour.

All three can be true and still answer different questions.

A heart is made of cells, but “list every cell” is not the most useful state description for predicting a heartbeat. At the same time, a high-level heartbeat variable is not automatically sufficient for every biochemical question about the heart.

A biological experiment can make the same point without accepting any MKUFT terminology. Take two systems whose measured present activity is matched as closely as the native field allows. Do not only address the systems: address the **challenge** and the **boundary conditions** too. A nominally identical cold shock, drug pulse, mechanical load or stimulus is not experimentally identical unless dose, timing, duration, environment, measurement burden and other load-bearing conditions are controlled tightly enough for the target question.

Now apply the same declared lawful challenge to states the current model calls equivalent. Before looking at the outcome, state what “equivalent” predicts, including the ordinary stochastic spread and uncertainty already allowed by the model.

If the futures split **systematically beyond that declared tolerance**, the experiment has exposed a failure of the current equivalence class. The model has merged states that are not equivalent for that future. The next job is not to announce a mysterious hidden variable: first ask whether the split came from an imperfectly matched state, a non-equivalent challenge, a boundary/environment difference, measurement error, or an already adequate stochastic model. Each successful control removes explanatory territory and is therefore useful negative-space information.

If a residual split survives those controls, add the **smallest physically or biologically defensible missing distinction**—for example a history, phase, metabolic, structural or relational variable—and test it prospectively on fresh cases. If that addition predicts the split and held-out closure improves, the old state description was incomplete for that target. If it does not, reopen the candidate or reject it.

The low state matters too. If the supposedly equivalent systems remain equivalent under a well-chosen separating challenge, within the declared uncertainty and tolerance, that is not “nothing happened.” It is evidence in favour of preserving the simpler state description for that target, regime and challenge family. MKUFT is therefore not a one-way machine for adding complexity: **controlled splitting pressures the model to reopen; controlled non-splitting can earn provisional preservation.**

There is one more part of the picture. The experiment only has access to a future through its **registration surface**: the measurements, records and readouts actually available. That is the conservative role of `O` in the SIPO shorthand. A split is meaningful only if the declared measurement family can resolve a target-relevant difference beyond its noise and tolerance. If the measurement itself physically disturbs the system, that disturbance belongs to the P-layer instrument and has to be controlled like any other part of the challenge. `O` does not supply a new force merely by being present.

This closes the example back into SIPO rather than leaving it as a downstream assay:

```text
addressed state + context/history
→ choose the active law and lawful challenge
→ propagate physically
→ register the result through a declared P→(P,O) measurement/readout
→ split or no split at the target-relevant resolution
→ use controls and negative space to localise what the result means
→ preserve the current state description or minimally readdress it
→ assemble the next law object from the updated address
```

So the test runs both ways. The current address determines which law and challenge are meaningful; the registered future then tests whether that address was sufficient. That is the recursive return, not an observer-caused-physics claim.

MKUFT separates two claims that are often fused:

> **This organised whole is a legitimate object for the question being asked.**

and

> **This organised whole has a sufficient closed law for the property we care about.**

The first does not guarantee the second.

That distinction is the centre of the law-descent work.

## From object to law

The current public architecture can be read as one continuing question.

### 1. What is the object?

[Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md) says the object, scale, boundary, and admissible state must be established before law ownership is assumed.

### 2. What information must the state contain?

The [SIPO Capstone](docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md) assembles the addressed state into a local law object. In plain English, it asks: what do we have to know before we are entitled to say which transitions are possible and how they should be weighted?

A useful shorthand is:

```text
D = what states are admissible here
T = what transitions are lawful here
W = how the lawful surviving routes are weighted or costed
```

The order matters. A route should not become “possible” merely because it is attractive or highly weighted.

SIPO then carries the result forward and back: the addressed state selects the admissible law object, physical propagation produces a continuation, the measurement/registration step creates a P-state plus O-record, and that realised path and record are folded into the next address. The conservative loop is therefore **address → law → physical future → registration → readdress**, with any stronger observer-dependent physical claim requiring separate evidence.

### 3. Does a higher-order whole actually own the law?

[Relational Closure, Law Descent, and Bidirectional Readdressing](docs/33S2_RELATIONAL_CLOSURE_LAW_DESCENT_AND_BIDIRECTIONAL_READDRESSING.md) separates four things:

```text
which historical object is this?
→ what relation makes it this kind of whole?
→ does that relation persist?
→ is the whole-level state sufficient for the property we want to predict?
```

If the higher level is sufficient, it can carry an effective law for that property and scope.

If not, the model has to reopen lower-level detail or stay multiscale.

### 4. Does good local performance mean the whole is healthy?

No.

[Cross-Scale Performance, Recoverability, and Hysteretic Readdressing](docs/33S3_CROSS_SCALE_PERFORMANCE_RECOVERABILITY_AND_HYSTERETIC_READDRESSING.md) separates local performance from whole-system closure, law sufficiency, and recoverability.

A part can improve its own score while the wider system becomes harder to restore.

That matters in biology, engineering, institutions, AI, and control systems.

### 5. Can two states look the same now but have different futures?

Yes. If so, the state description is missing something important.

[Address Sufficiency, Predictive Closure, and Reachable-Future Geometry](docs/33S4_ADDRESS_SUFFICIENCY_PREDICTIVE_CLOSURE_AND_REACHABLE_FUTURE_GEOMETRY.md) asks whether the present Address is rich enough to predict the future distinctions the task actually cares about.

[Rate-Conditioned Addressing](docs/33S5_RATE_CONDITIONED_ADDRESSING_TIME_PARAMETERISED_TRAVERSAL_AND_ADAPTIVE_REORGANISATION.md) then asks whether timing, rate, phase, dwell, schedule, or bounded history has to enter that Address.

Those variables are added only when they make a real predictive difference.

### 6. Is recovery really available?

[Addressed Admissible Futures](docs/33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md) treats recovery as a route through future state space, not a reassuring assumption.

A system may still function while its reserve of restorative futures is shrinking.

That gives a sharper question than “is it broken yet?”:

> **How much lawful room to recover is left?**

### 7. How do we detect a missing state variable before the usual marker appears?

[Future-Splitting State Recruitment](docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md) provides the direct assay.

Take states that the current model treats as equivalent. Make the state matching, challenge, boundary conditions and expected uncertainty explicit before testing. Then apply a controlled lawful challenge chosen to expose any hidden difference.

Two outcomes carry information:

```text
repeatable future split beyond declared tolerance
→ at least one equivalence claim is too coarse
→ first audit state matching, challenge equivalence, boundary/environment, measurement and ordinary stochastic explanations
→ use the controls and eliminated alternatives as negative-space data
→ recruit the smallest typed missing distinction that restores held-out prediction
→ test prospectively

no material split under a strong separating challenge
→ the current representation survives that attack
→ preserve the simpler state provisionally for that target, regime, challenge family and tolerance
```

The point is not to add complexity. The point is to make the model **earn either reopening or preservation**. A split does not automatically prove hidden internal state, because the challenge or boundary may have differed; a null does not prove metaphysical completeness, because it closes only the declared target and test family.

The first full prospective protocol that cashes this assay into a native physical/material experiment is [28C — Minimum Decisive FSAI/FSSR Flagship: History-Dependent HCP Magnesium Mechanics](docs/28C_FSAI_FSSR_MINIMUM_DECISIVE_FLAGSHIP_HCP_MAGNESIUM_PROTOCOL.md). It does **not** ask whether magnesium has loading-history effects; materials science already owns twinning, detwinning, hysteresis and constitutive internal variables. It asks a harder question: can the strongest practical predeclared reduced state be made to fail prospectively under a lawful separating reversal, can the smallest measurable physical repair restore held-out closure, does remove/restore behave as predicted, and does an FSSR state-splitting challenge add anything beyond a matched parameter-information design? The protocol is designed to return a clean preservation/null as readily as a positive recruitment result.

The registered result then returns to SIPO: it updates the evidence/history/context used to decide whether the next addressed state should remain compressed or recruit a new distinction before the next law object is assembled. That upstream return is part of the same architecture, not an optional afterthought.

### 8. What can the observer actually distinguish next?

A future split can be real without every useful next test being available from the current observer or registration state.

Imagine diagnosing a machine through a small inspection hatch. The first view may tell you that two apparently similar cases are heading toward different failures. One measurement lets you open a second panel; only from there does another test become possible. The later test was not secretly available at the start. **The state you reached changed what you could lawfully inspect next.**

That is the plain-English object behind [Observer-Bounded Traversal, Wake Screening, and Reachable Discriminator Frontiers](docs/33S7C_OBSERVER_BOUNDED_TRAVERSAL_WAKE_SCREENING_AND_REACHABLE_DISCRIMINATOR_FRONTIERS.md).

The metaphor stops at access and sequencing. Scientifically, the observer may simply be an instrument/readout arrangement. The available discriminator can be a measurement, comparison, perturbation, representation change, scale move, retrieval, controlled wait, or question. History is carried only while it still changes the declared future after the best present-state description is supplied; otherwise it remains provenance rather than active state burden.

So the recursive return becomes sharper:

```text
future-bearing distinction remains unresolved
→ use the smallest lawful discriminator currently reachable
→ register the realised result
→ readdress from the state actually reached
→ allow the next available test family to change
→ stop when no reachable lawful discriminator changes the declared target
```

This is not a claim that consciousness creates reality or that there is one uniquely correct question. It is a bounded statement about what a declared observer/experimental arrangement can legitimately resolve from the state it has actually reached.

## What the Bell/CHSH result teaches

The published [Bell Constraints as Typed Boundaries](papers/2026-08-25_BELL_CONSTRAINTS_TYPED_BOUNDARIES_v1.0.md) analysis keeps Bell-local factorisation, operational no-signalling, conditioned process closure, local admissibility ownership, completion, and scale/resource questions separate. Its tested independent Bell-local new-physics delta is **NULL**. The retained result is methodological: a typed correspondence and falsification architecture that prevents one Bell-related statement from silently substituting for another.

The [Cross-Domain Compositional Schema v0.4](papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md) was then pushed against Bell/CHSH geometry.

The first result is positive and exact. After the earlier dimensional objection, the facet-adapted construction represents the established four-correlator object as three independent affine coordinates on a native CHSH tetrahedral facet plus one transverse coordinate, with exact reconstruction. That is a hard known-answer calibration of the architecture's preservation/reopening and semantic-address discipline. It is not a new Bell theorem, new CHSH facet, or new quantum mechanism.

The stronger geometric candidate is then allowed to fail. The natural four-volume reduces exactly to known CHSH excess, so it supplies no independent Bell invariant or physical residual. That stronger new-physics branch is **NULL**.

The pair matters: **exact native reconstruction first; clean refusal of unsupported promotion second.** The later null does not erase the positive reconstruction, and the positive reconstruction does not license new physics.

The Bell results are therefore calibrations and correspondence work, not claims to have discovered a new Bell law or solved Bell's theorem.

## What ATLD is testing

The AI-facing branch asks whether a structured relational architecture actually improves long-horizon reasoning.

A good-looking conversation is not enough.

The architecture should beat fair alternatives when content, information access, time, compute, and revision opportunity are matched. Useful controls include flat structure, isolated components, one-way assistance, complete-history replay, and relation scrambling.

If replay or a simpler structure performs just as well, the stronger claim contracts.

[ATLD 2 v2.0](papers/2026-08-23_ATLD2_RESIDUAL_COORDINATE_IDENTIFICATION_v2.0.md) also reports a bounded 15-case exploratory execution pilot. The pilot shows that the scoring surface can be applied and return a shaped diagnostic profile; it does not establish confirmatory superiority of the structured condition or validate the five candidate residual coordinates.

## What physics still owes

A physicist is entitled to ask for the hard things.

MKUFT has not independently derived quantum mechanics, the Born rule, quantum field theory, general relativity, or a finished quantum theory of gravity.

If the architecture is promoted into a claimed fundamental physical theory, it must recover the established quantum and gravitational regimes, preserve Bell compatibility and operational no-signalling, define every claimed physical coupling, close dimensional and conservation bookkeeping, and produce a result that distinguishes it from the strongest adequate ordinary physical model.

The present Layer Before Law claim is prior to that promotion. It can be tested as an architecture without pretending the later burden has already been paid.

## What would make MKUFT less interesting or wrong?

The short version is straightforward.

If the added addresses do no work, remove them.

If a higher-level state does not predict the target property, do not grant it a closed higher-level law.

If a cross-layer bridge has no carrier, do not call it a physical mechanism.

If ordinary physics or a simpler model predicts the result equally well, prefer the simpler account.

If an observer-linked effect goes null under adequate controlled testing, contract or remove that branch.

If Bell compatibility, no-signalling, standard-physics recovery, dimensional consistency, or conservation bookkeeping fail where required, the physics-facing claim fails.

If a supposed novelty disappears under strong prior-art comparison, narrow the novelty claim.

If a result survives only because the failure criterion was changed after the result, the test failed.

The full technical statement is [MKUFT Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md).

## Known communication failure: a correct idea can still be unreadable

This repository has a reader-interface problem that is being actively corrected.

The work was developed recursively. Each new term usually exists because an earlier, simpler formulation failed under pressure. The people who built the chain remember those failures. A new reader sees only the final term.

That creates **dependency-history asymmetry**: the author sees compression; the reader sees jargon.

The repair is not to remove the technical language. The repair is to put the ordinary-English question immediately before it, explain why the distinction exists, show what failure it prevents, and then give the formal term.

There is a second, opposite failure. Once the reader has earned a relation, repeatedly restarting it or swapping its technical handle for a looser synonym makes the text harder rather than easier. The reader should be allowed to accumulate understanding. Public prose therefore carries the **minimum sufficient reader wake**: enough prior context for the next move to make sense, but no unnecessary replay and no semantic swapping of an already-earned object.

A clean metaphor is useful when it reduces a genuine conceptual crossing. It should preserve the relation, make its stopping point clear, and then hand the reader back to the native science. The aim is not to reduce the reader's intelligence requirement; it is to reduce avoidable reconstruction work.

A second repair is to stop using links as substitutes for explanation. A reader should know why the next document follows before clicking it.

The repository-level control is [Reader Contact, Translation, and Failure Guide](READER_CONTACT_AND_FAILURE_GUIDE.md). That guide is also recursive: when a repeatable reader-interface failure is discovered, the local passage is repaired and the transferable lesson is folded into the standing writing discipline so later prose does not recreate the same burden.

## Which route should you take?

If you are new to the work, read this page and then [Reader Contact, Translation, and Failure Guide](READER_CONTACT_AND_FAILURE_GUIDE.md).

If the public questions are clear but the technical chain is outside your field, use the [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md). It explains what each technical step is trying to establish, what the equations mean in broad terms, what can be left to domain specialists, and where each claim is easiest to kill.

If you are a physicist, continue to [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md), then [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md), then the [current v1.2 synthesis](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md).

If you work in complex systems, biology, control, or multiscale modelling, continue to [Recursive Constraint Closure](docs/32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md), [Relational Closure and Law Descent](docs/33S2_RELATIONAL_CLOSURE_LAW_DESCENT_AND_BIDIRECTIONAL_READDRESSING.md), and [Addressed Admissible Futures](docs/33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md).

If you work in AI, continue to [ATLD 2](papers/2026-08-23_ATLD2_RESIDUAL_COORDINATE_IDENTIFICATION_v2.0.md).

If you want frozen publications and DOI identities rather than the live module chain, use [Papers and Publications](papers/README.md).

If you want the complete technical dependency map, use the [Canon Map](CANON_MAP.md).

## Claim discipline

MKUFT keeps several claim levels separate:

1. conceptual proposal;
2. mathematical scaffold;
3. operational hypothesis;
4. discriminating prediction;
5. replicated empirical relation;
6. mechanism-level result;
7. foundational physical theory.

Different branches occupy different levels. A result in one branch does not promote the whole framework.

A structural relation can be important without being true. A mathematical mapping can be exact without being a new physical mechanism. A higher-order description can be a legitimate predictive object without owning a sufficient higher-order law. A null result can be scientifically useful.

Those distinctions are not protective wording. They are part of the test architecture.

## Publications and provenance

The principal DOI-bearing MKUFT publication is v2: [10.5281/zenodo.21973064](https://doi.org/10.5281/zenodo.21973064).

The current research-facing synthesis is v1.2, dated 30 August 2026, public in this repository, not yet DOI-bearing, and not peer reviewed: [MKUFT Layer Before Law submission synthesis v1.2](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md).

The complete publication index is [Papers and Publications](papers/README.md).

The exact DOI-bearing object controls the frozen publication version. Live GitHub work does not silently replace it.
