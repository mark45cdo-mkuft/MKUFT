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

## What a reader should be able to tell in five minutes

A reader should be able to answer five questions.

**What is the central proposal?**  
Before choosing a law, identify the object, scale, boundary, evidence position, admissible states, and lawful transitions. MKUFT calls this Layer Before Law.

**What is new enough to inspect?**  
Not a finished new law of nature. The present candidate contribution is a disciplined way to ask a sequence of harder questions: have we described the right object; is the higher-level description actually sufficient for the property we want to predict; do two apparently similar present states hide different futures; can the system still recover after perturbation; and does a proposed relation survive strong ordinary and prior-art controls? The technical names come after the questions they answer.

**What is ordinary or already known?**  
Many mathematical ingredients have strong prior art: coarse-graining, quotienting, lumpability, closure, reachability, dynamical systems, state sufficiency, Bell/CHSH mathematics, and control ideas. MKUFT does not claim those ingredients as inventions.

**What would make the work fail?**  
If the extra address structure adds no predictive, explanatory, interventional, or model-selection value; if cross-layer couplings have no carriers; if higher-level laws do not actually close at the claimed level; if ordinary models perform equally well; or if physics-facing burdens such as Bell compatibility, no-signalling, dimensional consistency, standard-limit recovery, and conservation fail.

**Where is the quickest technical attack?**  
Use [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md), [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md), and the [current v1.2 synthesis](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md). A good critique should identify one load-bearing proposition and try to kill it.

## Known reader-interface failure modes

### 1. Dependency-history asymmetry

The work was built recursively. A term often exists because a simpler version broke earlier. The builder remembers that break. The new reader does not. So the builder sees a compressed handle while the reader sees a pile of nouns.

**Control:** give the ordinary question, then the failure that forced the distinction, then the technical name.

Bad:

> “Property-specific law descent requires readdressing under failed representative independence.”

Better:

> “A higher-level description can be useful and still fail to predict the thing we care about. When that happens, lower-level information has to come back into the model. The technical names for those two moves are law-descent failure and readdressing.”

### 2. Link substitution

A repository can contain every correct document and still fail the reader by saying only “see Module 33S2, then 33S3, then 33S4.”

A link tells the reader where something is. It does not tell the reader why the next object follows.

**Control:** carry the relation in one sentence before the link.

### 3. Academic compression mistaken for rigour

Dense prose can hide a simple question. Replacing technical nouns with long formal English does not fix that.

**Control:** explain one relation at a time. Use ordinary English first, a clean metaphor where it genuinely removes load, and formal terminology second.

### 4. Metaphor becoming machinery

A metaphor can make a relation obvious and then quietly start doing scientific work it cannot support.

**Control:** use the metaphor to open the door, then return immediately to the actual scientific object. Metaphor is translation, not evidence.

### 5. Scope bleed

One strong result in one branch can accidentally sound like support for the whole framework.

**Control:** claim levels remain local. A Bell calibration result does not prove MKUFT physics. An AI result does not prove the S-layer. A useful cross-domain relation does not become a new law of nature by association.

### 6. Mathematics mistaken for mechanism

An equation can be correct mathematics and still fail to describe nature.

**Control:** every physics-facing claim must identify physical variables, units, carrier, measurable consequence, ordinary baseline, and falsifier. Correct mathematical mapping does not validate ontology.

### 7. Cross-layer smuggling

A relation can be meaningful at the information layer without automatically becoming a physical cause.

**Control:** state source address, target address, carrier, transformation, and expected target expression. If the bridge is absent, keep the claim descriptive or unresolved.

### 8. Null avoidance

A flexible framework can survive anything if every failure is renamed after the result.

**Control:** preserve predeclared failure states. The Bell/CHSH tetrahedral branch is a useful example: the exact construction survived, but the independent new-physics residual became NULL when the four-volume reduced to known CHSH excess. That null remains in the record.

### 9. AI confidence mistaken for evidence

AI systems can produce fluent technical text, including fluent mistakes.

**Control:** AI assistance is tooling, not validation. Claims must trace to mathematics, source material, reproducible calculation, experiment, or clearly labelled inference.

### 10. Version and provenance drift

A live repository, frozen DOI paper, module, synthesis, and PDF mirror can contain related material without being the same object.

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

**Plain version:** the right equation can still give the wrong answer if you are asking it about the wrong thing.

[Read Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md).

### SIPO Capstone

**Question:** what must be in the addressed state before we can build the active law object?

**Plain version:** before calculating what happens next, be clear about where the rule applies, what changes are allowed, and how alternatives are weighted.

[Read the SIPO Capstone](docs/33_SIPO_CAPSTONE_CONSTRAINT_CONDITIONED_ADDRESSED_UPDATE_LAW.md).

### Relational Closure and Law Descent

**Question:** is the higher-order state sufficient to predict the property we care about?

**Plain version:** a whole can be perfectly real and useful without knowing everything about itself. A heart is a useful object; that does not mean one heart-level description predicts every electrical failure.

[Read Relational Closure and Law Descent](docs/33S2_RELATIONAL_CLOSURE_LAW_DESCENT_AND_BIDIRECTIONAL_READDRESSING.md).

### Cross-Scale Performance and Recoverability

**Question:** can a part improve while the whole becomes less stable or harder to restore?

**Plain version:** being healthy now and being able to get home after damage are different properties.

[Read Cross-Scale Performance and Recoverability](docs/33S3_CROSS_SCALE_PERFORMANCE_RECOVERABILITY_AND_HYSTERETIC_READDRESSING.md).

### Address Sufficiency and Predictive Closure

**Question:** do two states that look equivalent now actually have the same relevant future?

**Plain version:** if two states look the same to your model but reliably go different ways, your model has forgotten something.

[Read Address Sufficiency and Predictive Closure](docs/33S4_ADDRESS_SUFFICIENCY_PREDICTIVE_CLOSURE_AND_REACHABLE_FUTURE_GEOMETRY.md).

### Rate-Conditioned Addressing

**Question:** does timing, rate, phase, dwell, schedule, or bounded history change what happens next?

**Plain version:** taking the same road does not mean making the same journey if one system races through it and another sits at a critical point for an hour.

[Read Rate-Conditioned Addressing](docs/33S5_RATE_CONDITIONED_ADDRESSING_TIME_PARAMETERISED_TRAVERSAL_AND_ADAPTIVE_REORGANISATION.md).

### Addressed Admissible Futures

**Question:** what futures are still reachable, and which restore the target function?

**Plain version:** functioning now does not tell you whether there is still a road back after the next hit.

[Read Addressed Admissible Futures](docs/33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md).

### Future-Splitting State Recruitment

**Question:** when two apparently equivalent states later split, what missing variable predicts the split?

**Plain version:** do not guess what the model forgot. Put two supposedly equivalent states under the same lawful pressure and try to make the missing difference show itself.

[Read Future-Splitting State Recruitment](docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md).

### Cross-Domain Compositional Schema

**Question:** can the preserve/reopen and future-sufficiency rules transfer without importing the answer?

**Plain version:** a pattern that looks good in two fields is not automatically the same law in both fields.

[Read Cross-Domain Compositional Schema v0.4](papers/2026-08-29_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_v0.4.md).

### ATLD 2

**Question:** does typed relational architecture itself improve long-horizon AI performance under fair controls?

**Plain version:** if the AI got better, was it actually the architecture, or did we quietly give it more help?

[Read ATLD 2 v2.0](papers/2026-08-23_ATLD2_RESIDUAL_COORDINATE_IDENTIFICATION_v2.0.md).

## How to criticise MKUFT efficiently

Pick one proposition. State the native-field baseline. State what MKUFT adds. Ask what observation, proof, calculation, or controlled comparison distinguishes it. Then try to remove it.

A good kill is useful. It removes dead weight.

## Reading routes

**Fastest conceptual route:** [Public Overview](START_HERE_PUBLIC_OVERVIEW.md) → [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md) → [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md).

**Scientific traversal route:** [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md) → linked technical owners.

**Current research synthesis:** [MKUFT Layer Before Law v1.2](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md).

**Full technical dependency route:** [Canon Map](CANON_MAP.md).

**Frozen publications and DOI identities:** [Papers and Publications](papers/README.md).

## Final reader contract

> **Explain the thing normally first. Carry one relation at a time. Use a clean picture when it removes load. Then give the technical name and exact science. Never let the metaphor become evidence. Never change the mathematics merely to make the prose easier.**

Technical language is useful compression after the meaning is secured. Without that handoff, compression becomes noise.