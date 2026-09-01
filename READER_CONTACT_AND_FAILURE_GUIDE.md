# Reader Contact, Translation, and Failure Guide

**Purpose:** give a new reader enough plain-English structure to decide whether MKUFT deserves deeper technical attention, without asking them to learn the repository's private development history first.

This guide exists because first-contact reading exposed a real weakness in the public interface: the technical structure can be careful while the explanation of *why the structure exists* arrives too late.

That is a communication failure, not a reason to lower the scientific standard.

## The translation rule

Do not translate hard science into long polite English. **Just explain the thing first.**

Simple words can still make a complicated paragraph. The test is not whether jargon has been removed. The test is how many new things the reader has to hold in their head at once.

Where one ordinary picture carries the relation, use it. Then return to the science.

> **Explain it normally → give the clean picture if it helps → name the technical object → give the exact scientific rule.**

A metaphor opens the door. It does not become evidence.

Do not change or dilute the mathematics to make it readable. Add a short translation around the mathematics so a non-specialist can tell what question the equation answers, what its pieces are doing, and what would make the move fail.

If an unfamiliar MKUFT term looks like a renamed standard concept, use the [MKUFT Translation and Prior-Art Key](MKUFT_TRANSLATION_AND_PRIOR_ART_KEY.md). The key does not assign one-to-one scientific equivalents. It asks what established science already owns, what exact residual operation MKUFT is claiming after that ownership is subtracted, and what result would make the separate handle unnecessary. It is an optional cross-check, not another reading stage.

## What a reader should be able to tell in five minutes

A reader should be able to answer five questions.

**What is the central proposal?**  
Before choosing a law, identify the object, scale, boundary, evidence position, admissible states, and lawful transitions. MKUFT calls this Layer Before Law.

**What is new enough to inspect?**  
Not a finished new law of nature. The present candidate contribution is a disciplined way to ask a sequence of harder questions: have we described the right object; is the higher-level description actually sufficient for the property we want to predict; do two apparently similar present states hide different futures; can the system still recover after perturbation; and does a proposed relation survive strong ordinary and prior-art controls? The technical names for those steps come later in this guide, after the questions they answer.

**What is ordinary or already known?**  
Many mathematical ingredients have strong prior art: coarse-graining, quotienting, lumpability, closure, reachability, dynamical systems, state sufficiency, Bell/CHSH mathematics, and control ideas. MKUFT does not claim those ingredients as inventions.

**What would make the work fail?**  
If the extra address structure adds no predictive, explanatory, interventional, or model-selection value; if cross-layer couplings have no carriers; if higher-level laws do not actually close at the claimed level; if ordinary models perform equally well; or if physics-facing burdens such as Bell compatibility, no-signalling, dimensional consistency, standard-limit recovery, and conservation fail.

**Where is the quickest technical attack?**  
Use [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md), [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md), and the [current v1.2 synthesis](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md). A good critique should identify one load-bearing proposition and try to kill it.

## Known reader-interface failure modes

### 1. Dependency-history asymmetry

The work was built recursively. A term often exists because a simpler version broke earlier.

The builder remembers that break.

The new reader does not.

So the builder sees a compressed handle while the reader sees a pile of nouns.

**Control:** public prose should give the ordinary-English question, then the failure that forced the distinction, then the technical name.

Example:

Bad:

> “Property-specific law descent requires readdressing under failed representative independence.”

Better:

> “A higher-level description can be useful and well-defined yet still fail to predict the property we care about. When that happens, lower-level information has to come back into the model. MKUFT calls the first issue failure of property-specific law descent and the correction readdressing.”

The second version is not less precise. It gives the precision a handle.

### 2. Link substitution

A repository can contain every correct document and still fail the reader by saying only “see Module 33S2, then 33S3, then 33S4.”

A link tells the reader where something is. It does not tell the reader why the next object follows from the previous one.

**Control:** every important transition should be carried by prose.

For example:

> “Once a higher-order object is identified, the next question is whether that object is actually sufficient to predict the target property. That is why the closure work leads directly into law descent.”

The link can come after that sentence.

### 3. Academic compression mistaken for rigour

Dense prose can hide the fact that a simple question is being asked.

Long nouns are useful once they carry stable meaning. They are harmful when the reader has to decode them before seeing the object.

**Control:** public-facing explanation uses teacher-level English first and formal terminology second. Technical modules may remain technical, but their entry surfaces should not require the reader to reverse-engineer the motivation.

### 4. Metaphor becoming machinery

A metaphor can make a relation obvious and then quietly start doing scientific work it cannot support.

**Control:** use the metaphor to open the door, then return immediately to the actual scientific object. Metaphor is translation, not evidence.

### 5. Scope bleed

One strong result in one branch can accidentally sound like support for the whole framework.

**Control:** claim levels remain local. A Bell calibration result does not prove MKUFT physics. An AI result does not prove the S-layer. A useful cross-domain relation does not become a new law of nature by association.

### 6. Mathematics mistaken for mechanism

An equation can be correct as mathematics and still fail to describe nature.

**Control:** every physics-facing claim must identify the physical variables, units, carrier, measurable consequence, ordinary baseline, and falsifier. Similarity to known mathematics validates the mapping where correct; it does not validate the ontology.

### 7. Cross-layer smuggling

A relation can be meaningful at the information layer without automatically becoming a physical cause.

**Control:** state the source address, target address, carrier, transformation, and expected target expression. If the bridge is not there, keep the claim descriptive or unresolved.

### 8. Null avoidance

A flexible framework can survive anything if every failure is renamed after the result.

**Control:** preserve predeclared failure states. The Bell/CHSH tetrahedral branch is a useful example: the exact construction survived, but the independent new-physics residual became NULL when the four-volume reduced to known CHSH excess. That null remains in the record.

### 9. AI confidence mistaken for evidence

AI systems can produce fluent technical text, including fluent mistakes.

**Control:** AI assistance is tooling, not validation. Claims must be traceable to mathematics, source material, reproducible calculation, experiment, or clearly labelled inference. Reader criticism is a discriminator, not something to be defeated rhetorically.

### 10. Version and provenance drift

A live repository, a frozen DOI paper, a module, a submission synthesis, and a PDF mirror can contain related material without being the same object.

**Control:** preserve exact version identity. Do not silently let a live edit rewrite a historical deposit.

## A worked example: MKUFT catches an addressing failure in itself

We found a hole in our own rules.

Say MKUFT makes a prediction and it is wrong. We inspect the failure, learn something useful, repair the model, and try again. That is normal scientific learning.

But zoom out one level.

If every time MKUFT is wrong it gets to learn why it was wrong and come back with a better answer, **when does MKUFT itself lose?**

We had been standing too close.

At branch level the object is one idea:

```text
idea → test → failure → learn
```

At the higher level the object is MKUFT as a generator of ideas. The question changes:

> **Is this architecture good at producing useful predictions before it knows the answers, or are we letting it keep trying until something survives?**

That is an MKUFT-style addressing error applied to MKUFT itself. The local branch and the parent generator are different objects and need different scoreboards.

The fix is simple:

> **A failure can teach MKUFT. It cannot simultaneously count as evidence that MKUFT succeeded.**

If the failure teaches a repair, good. That repair is a new hypothesis and needs fresh evidence.

A simple picture is an exam: you are allowed to study the answers you got wrong. You are not allowed to correct the old paper afterwards and call the corrected paper your original score.

The formal owner for this rule is [Branch Lineage, Generator Accountability, and Anti-Hydra Discipline](docs/29A_BRANCH_LINEAGE_GENERATOR_ACCOUNTABILITY_AND_ANTI_HYDRA_DISCIPLINE.md).

## Why the modules exist — the chain in ordinary English

### Layer Before Law

**Question:** are we applying a law before we have correctly identified the object and scale?

**Failure prevented:** using the right equation on the wrong object.

**Plain version:** the right equation can still give the wrong answer if you are asking it about the wrong thing.

[Read Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md).

### SIPO Capstone

**Question:** what must be in the addressed state before we can build the active law object?

**Failure prevented:** treating candidate generation, admissibility, transition, and weighting as the same operation.

**Plain version:** before calculating what happens next, be clear about where the rule applies, what changes are allowed, and how alternatives are weighted.

[Read the SIPO Capstone](docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md).

### Relational Closure and Law Descent

**Question:** does the higher-order organisation merely give us a useful object, or is its state actually sufficient to predict the property we care about?

**Failure prevented:** confusing functional organisation with universal higher-level autonomy.

**Plain version:** a whole can be perfectly real and useful without knowing everything about itself. A heart is a useful object; that does not mean one heart-level description predicts every electrical failure.

[Read Relational Closure and Law Descent](docs/33S2_RELATIONAL_CLOSURE_LAW_DESCENT_AND_BIDIRECTIONAL_READDRESSING.md).

### Cross-Scale Performance and Recoverability

**Question:** can a part improve while the whole becomes less stable or harder to restore?

**Failure prevented:** mistaking local performance gain for whole-system health.

**Plain version:** being healthy now and being able to get home after damage are different properties.

[Read Cross-Scale Performance and Recoverability](docs/33S3_CROSS_SCALE_PERFORMANCE_RECOVERABILITY_AND_HYSTERETIC_READDRESSING.md).

### Address Sufficiency and Predictive Closure

**Question:** do two states that look equivalent now actually have the same relevant future?

**Failure prevented:** declaring the present state sufficient when hidden variables only become visible later.

**Plain version:** if two states look the same to your model but reliably go different ways, your model has forgotten something.

[Read Address Sufficiency and Predictive Closure](docs/33S4_ADDRESS_SUFFICIENCY_PREDICTIVE_CLOSURE_AND_REACHABLE_FUTURE_GEOMETRY.md).

### Rate-Conditioned Addressing

**Question:** does timing, rate, phase, dwell, schedule, or bounded history change what happens next?

**Failure prevented:** forcing time-dependent systems into a state description that has thrown away the time variable that carries the prediction.

**Plain version:** taking the same road does not mean making the same journey if one system races through it and another sits at a critical point for an hour.

[Read Rate-Conditioned Addressing](docs/33S5_RATE_CONDITIONED_ADDRESSING_TIME_PARAMETERISED_TRAVERSAL_AND_ADAPTIVE_REORGANISATION.md).

### Addressed Admissible Futures

**Question:** what futures are still reachable, and which of them restore the target function?

**Failure prevented:** assuming recoverability because the system is still functioning now.

**Plain version:** functioning now does not tell you whether there is still a road back after the next hit.

[Read Addressed Admissible Futures](docs/33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md).

### Future-Splitting State Recruitment

**Question:** when two apparently equivalent states later split, what missing state variable or relation predicts the split?

**Failure prevented:** adding variables by taste instead of because a controlled future difference proves they are needed.

**Plain version:** do not guess what the model forgot. Put two supposedly equivalent states under the same lawful pressure and try to make the missing difference show itself.

[Read Future-Splitting State Recruitment](docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md).

### Cross-Domain Compositional Schema

**Question:** can the preserve/reopen and future-sufficiency rules transfer into another domain without importing the answer?

**Failure prevented:** mistaking a useful analogy for a lawful cross-domain invariant.

**Plain version:** a pattern that looks good in two fields is not automatically the same law in both fields.

[Read Cross-Domain Compositional Schema v0.4](papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md).

### ATLD 2

**Question:** does typed relational architecture itself improve long-horizon AI performance under fair controls?

**Failure prevented:** mistaking a strong base model, more context, more compute, or complete-history replay for a gain caused by the architecture.

**Plain version:** if the AI got better, was it actually the architecture, or did we quietly give it more help?

[Read ATLD 2 v2.0](papers/2026-08-23_ATLD2_RESIDUAL_COORDINATE_IDENTIFICATION_v2.0.md).

## Immediate relevance by field

### If you are a physicist

The useful first question is whether Layer Before Law exposes a real modelling distinction that survives native physics. Attack the Bell/no-signalling boundary, standard-limit recovery, the physical carrier of any cross-layer claim, and the requirement to beat an adequate P-only model.

If those do not close, do not promote the framework to fundamental physics.

### If you are a mathematician

Ignore the branding for a moment and inspect the maps. Ask whether the definitions are coherent, whether the claimed descent condition is stronger than ordinary quotient/coarse-grain machinery, whether the equivalence classes are well formed, whether the future-sufficiency test adds a nontrivial condition, and whether any alleged novelty survives prior-art subtraction.

A clean result may be “this is known mathematics assembled into a useful operational synthesis.” That is an acceptable scientific outcome.

### If you work in biology or complex systems

Here is a concrete way to attack the idea rather than reading the whole framework first.

Take two systems whose measured present state looks the same under the model you normally use, but whose recent histories differ in a controlled way. Ask whether those two histories lead to different future behaviour. If they do, fit the strongest ordinary model using the present variables alone, then add the smallest physically defensible history or state variable that distinguishes the futures. If the extra variable removes an apparent interaction, false edge, or unexplained divergence and then predicts held-out cases, the original state description was incomplete. If it adds nothing, the MKUFT-style readdressing claim has earned nothing in that system.

In a neural or cellular setting, that can be made concrete with matched present activity and deliberately different prior state histories: test whether a causal or connectivity model infers a relation that disappears once the missing history/state coordinate is restored. The exact biological variable must come from the biology, not from MKUFT vocabulary.

That is the practical content behind the separation between functional identity, closure, property-specific law sufficiency, recoverability, and future-state adequacy.

### If you work in AI

Attack ATLD with matched controls.

Can a flat or replayed system recover the same result? Does relation scrambling matter? Does removing the claimed load-bearing structure produce the predicted failure? Are time, tokens, compute, information access, revision opportunity, and task distribution matched?

If not, apparent “emergence” may just be ordinary tooling advantage.

### If you work in control or engineering

Inspect reachable futures and restorative reserve.

The practical question is whether the architecture can detect that a system is losing its ability to recover before a conventional failure marker becomes obvious.

That is useful only if it predicts something earlier or better than standard viability, reachability, state-estimation, or control methods.

## How to criticise MKUFT efficiently

The best critique is not “this sounds like AI jargon” and it is not “this feels profound.”

Pick one proposition.

State the native field baseline.

State what MKUFT adds.

Ask what observation, proof, calculation, or controlled comparison would distinguish the added structure from the baseline.

Then try to remove it.

Useful attacks include:

- show that the “new” distinction is already standard under another name;
- show that the higher-level law fails representative independence for the claimed property;
- show that a simpler multiscale model performs equally well;
- show that a claimed cross-layer bridge has no lawful carrier;
- show that a Bell or no-signalling requirement is violated;
- show that a result depends on post-hoc threshold choice;
- show that a null is being reclassified after the fact;
- show that matched replay or scrambled controls recover the same gain;
- show that the state variable being recruited adds no prospective information.

A good kill is useful. It removes dead weight.

## Reading routes

**Fastest conceptual route:** [Public Overview](START_HERE_PUBLIC_OVERVIEW.md) → [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md) → [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md).

**Scientific traversal route:** [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md) → the linked technical owners. Use this when the public questions are clear but the hard chain would otherwise require you to reconstruct the missing intermediate relations yourself.

**Current research synthesis:** [MKUFT Layer Before Law v1.2](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md).

**Full technical dependency route:** [Canon Map](CANON_MAP.md).

**Frozen publications and DOI identities:** [Papers and Publications](papers/README.md).

## Final reader contract

The public-facing standard is simple:

> **Explain the object before naming the machinery. Explain why the distinction exists before asking the reader to remember it. Explain why the next document follows before giving the link. State how the claim can fail before asking the reader to trust it.**

The translation rule sharpens that contract rather than replacing it: explain normally first, use a clean picture where it reduces load, then return to the technical object and exact science. Metaphor remains translation, never evidence.

Technical language is useful compression after the meaning is secured.

Without that handoff, compression becomes noise.