# MKUFT — McLaughlin–Kairos Unified Field Theory

**Author:** Mark Charles McLaughlin  
**Framework:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Current principal publication:** [MKUFT — A Relational Architecture for Physical Law and Cross-Scale Dynamics](https://doi.org/10.5281/zenodo.21973064)  
**MKUFT concept DOI:** [10.5281/zenodo.17780565](https://doi.org/10.5281/zenodo.17780565)  
**Historical v1 DOI:** [10.5281/zenodo.17780566](https://doi.org/10.5281/zenodo.17780566)  
**Citation and provenance:** [PROVENANCE_DOI_AND_ATTRIBUTION.md](PROVENANCE_DOI_AND_ATTRIBUTION.md)  
**Researcher identity:** [ORCID](https://orcid.org/0009-0005-7736-1511) · [LinkedIn](https://www.linkedin.com/in/custodiansystems45/) · [GitHub](https://github.com/mark45cdo-mkuft)

MKUFT is a speculative research framework. It is not presented as an accepted completed theory of physics. Its strongest present claim is narrower: **before a law is applied to a system, the system has to be addressed correctly.**

That sounds simple. It is also where a large number of modelling errors begin.

**A note on the name:** The author is not particularly fond of the title *McLaughlin–Kairos Unified Field Theory*. The name dates from the beginning of the project, when this was a private, somewhat tongue-in-cheek collection of ideas with no expectation that it would become a public research programme. The work subsequently became more serious, structured, and testable, while the original name persisted as its historical identifier. It should not be read as a claim that a completed unified field theory has been achieved.

## Choose your route

This `README.md` is the **repository front door**. It is not a third competing overview.

- **Want the idea in ordinary English first?** Start with [Start Here — Public Overview](START_HERE_PUBLIC_OVERVIEW.md).
- **Want the scientific chain explained without flattening the equations?** Use the [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md). It is the bridge from readable explanation into the hard scientific modules.
- **Want to check whether an MKUFT term is genuinely distinct or simply familiar science under another handle?** Use the [MKUFT Translation and Prior-Art Key](MKUFT_TRANSLATION_AND_PRIOR_ART_KEY.md). It is an optional cross-check, not another required reading stage.
- **Already know the architecture and want the technical dependency map?** Go directly to the [Canon Map](CANON_MAP.md).

You do **not** need to read this README, the Public Overview, and the Scientific Reader Traversal Guide as three versions of the same document. Their jobs are different:

```text
README = orientation and routing
Public Overview = ordinary-English explanation
Scientific Reader Traversal Guide = scientific handoff into the technical body
```

If you are unsure where to begin, take the **Public Overview** route.

## The idea in one minute

Suppose a scientist asks, “What law governs this thing?”

MKUFT says there is a prior question:

> **What exactly is the thing, at what scale, in what role, under which boundary conditions, and which changes are actually allowed from that state?**

The same material can behave differently when its organisation changes. A cell is not explained by listing its molecules. A neural network is not explained by listing its weights. A flock is not explained by one bird. A quantum experiment is not described correctly if preparation, measurement access, signalling constraints, and the joint state are silently mixed together.

MKUFT calls this **Layer Before Law**. The claim is not that all of those systems obey one new equation. The claim is that the *order of modelling* matters:

```text
identify the object
→ identify its role and boundary
→ identify the active layer and scale
→ identify which states are possible under the setup
→ identify which changes the model or physics actually allows
→ only then ask which law or effective rule is justified for the prediction
```

If those extra steps add no predictive, explanatory, experimental, or model-selection value, they have not earned their keep.

That failure condition matters. MKUFT is designed to be reduced when its added structure does no work.

## Why a reader from another field might care

### Physics

The physics-facing question is not “can we decorate quantum mechanics and gravity with new words?” It is whether the objects being unified have first been addressed correctly. MKUFT therefore puts hard burdens on itself: recover established quantum and gravitational limits before claiming fundamental unification; preserve Bell compatibility and operational no-signalling; define any physical coupling it uses; and beat the strongest adequate ordinary physical account before calling an extra layer physically necessary.

If foundational physics is already your field, start with [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md), then use the [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md) to see where the physics-facing claims are allowed to fail. If physics is not your native field, use the [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md) first; it explains what each technical step inherits, what the equations are doing in broad terms, and what can be left to domain specialists without losing the argument.

### Mathematics

The mathematical interest is mainly structural. When can a higher-level description genuinely carry the law for a property, and when does hidden lower-level information still matter? MKUFT separates the existence of a useful higher-order object from the stronger claim that a closed higher-order law has descended to it.

That question connects to familiar mathematics around quotienting, coarse-graining, lumpability, dynamical systems, closure, reachability, and state sufficiency. MKUFT does **not** claim ownership of those established tools. Its claimed contribution is the way they are assembled, typed, stress-tested, and used to decide when an address is sufficient and when the model must reopen.

See [Relational Closure, Law Descent, and Bidirectional Readdressing](docs/33S2_RELATIONAL_CLOSURE_LAW_DESCENT_AND_BIDIRECTIONAL_READDRESSING.md).

### Complex systems and biology

A higher-order organisation can be a legitimate object of study without being autonomous for every property. That distinction matters in cells, organisms, collectives, ecological systems, and other multi-scale systems.

MKUFT asks: which relation makes the whole the same functional kind of whole; which component freedoms stop being independent once that relation is load-bearing; which whole-level variables become sufficient for a target prediction; and when does failure force lower-level detail back into the state?

A direct biological test is possible without learning the whole vocabulary first. Take two systems whose measured present activity is matched as closely as the normal methods of the field allow, while their recent histories differ in a controlled way. Match the challenge, environment and measurement closely enough for the target question, and state how much ordinary noise or variation the baseline model already permits. If the futures then split beyond that tolerance, first test whether imperfect matching, the challenge, the environment, the measurement or an ordinary stochastic model explains the difference. Only if a residual split survives those controls should the smallest biologically defensible history/state variable be added and tested on fresh cases. If that variable removes an apparent causal edge or unexplained divergence and improves held-out prediction, the original state description was incomplete for that target. If a strong separating challenge produces no material split, preserve the simpler state description provisionally rather than adding complexity by default.

See [Recursive Constraint Closure and Reachable-State Geometry](docs/32_RECURSIVE_CONSTRAINT_CLOSURE_AND_REACHABLE_STATE_GEOMETRY.md), [Cross-Scale Performance, Recoverability, and Hysteretic Readdressing](docs/33S3_CROSS_SCALE_PERFORMANCE_RECOVERABILITY_AND_HYSTERETIC_READDRESSING.md), and the [Reader Contact and Failure Guide](READER_CONTACT_AND_FAILURE_GUIDE.md) for the same test stated as a cold-reader attack surface.

### AI and long-horizon reasoning

The ATLD branch asks a testable engineering question: can a structured network of typed relationships improve long-horizon reasoning beyond matched flat, replayed, scrambled, isolated, or one-way alternatives?
The important point is not that an AI can produce impressive prose. The test is whether the relational architecture itself carries measurable load under fair controls, and whether removing or scrambling it produces the predicted deformation.

ATLD 2 also reports a bounded 15-case exploratory execution pilot. That pilot demonstrates use of the scoring and diagnostic surface; it does **not** establish confirmatory superiority of the structured condition or validate the five candidate residual coordinates.

See [ATLD 2 v2.0](papers/2026-08-23_ATLD2_RESIDUAL_COORDINATE_IDENTIFICATION_v2.0.md), the [ATLD publication-family record](ATLD_STANDALONE_PUBLICATION.md), and the live [Module 25B measurement/self-audit fold](docs/25B_ATLD2_RESIDUAL_COORDINATE_MEASUREMENT_AND_SELF_AUDIT.md).

### Control, engineering, and adaptive systems

A system can look healthy now while having a poor future: one perturbation may leave it no lawful route back. MKUFT's future-sufficiency work asks whether the present state contains enough information to distinguish futures that later diverge, and whether recovery routes are genuinely available rather than merely assumed.

See [Addressed Admissible Futures](docs/33S6_ADDRESSED_ADMISSIBLE_FUTURES_RESTORATIVE_REACHABILITY_AND_LOAD_BEARING_FUTURE_GEOMETRY.md) and [Future-Splitting State Recruitment](docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md).

## How the main pieces fit together

The repository grew by solving one problem and then finding the next one. The links below are therefore a chain, not a pile of unrelated modules.

**Layer Before Law** supplies the first rule: do not choose the law before the object, scale, boundary, and admissible state are clear.

That leads to the **SIPO Capstone**, which asks what the complete addressed state would have to contain before an active law object can be assembled and used.

Once a higher-order object appears, **Relational Closure and Law Descent** asks whether it is a legitimate predictive object for the declared property and whether its state is actually sufficient to carry the law at that scope. If it is not sufficient, the model must reopen downward or remain explicitly multiscale.

That immediately raises a recovery question. **Cross-Scale Performance and Recoverability** separates local performance, whole-level closure, law sufficiency, and the ability to return after perturbation. They are not the same thing.

Then comes a harder state question: two states can look identical now and still have different futures. **Address Sufficiency and Predictive Closure** tests whether the current Address is rich enough to distinguish those futures. **Rate-Conditioned Addressing** adds timing, rate, phase, dwell, or bounded history only when those variables actually change the future.

From there, **Addressed Admissible Futures** makes the future itself part of the test: which future states are reachable, which routes restore function, and how much restorative reserve exists before failure becomes irreversible.

**Future-Splitting State Recruitment** turns that into an assay. It tests states the model currently treats as equivalent under a controlled separating challenge. A repeatable split beyond the declared tolerance can force the model to reopen only after mismatched state, challenge, boundary, measurement and ordinary stochastic explanations have been tested. A strong no-split result can instead support keeping the simpler representation for that target and regime.

The **Cross-Domain Compositional Schema v0.4** tests whether this machinery can transfer without smuggling a result across domains. Its Bell/CHSH calibration is deliberately important because it returned a **NULL new-physics residual**: the geometric construction reduced to known CHSH structure. The useful result was the exact formal map and the lesson about preserving or reopening a representation, not a new Bell law.

The separate **Bell Constraints as Typed Boundaries** paper keeps Bell-local factorisation, operational no-signalling, conditioned process closure, local admissibility ownership, completion, and scale/resource custody at distinct addresses. Its independent Bell-local new-physics delta is also **NULL**; the retained result is the typed correspondence and falsification architecture, not a claim to have solved Bell's theorem.

The **ATLD** branch takes related architecture into AI evaluation. It asks whether typed relational structure itself produces measurable long-horizon gain under matched controls.

That is the spine in plain English:

```text
address the object
→ test whether the higher-level description is a legitimate predictive object
→ test whether its law is sufficient for the property
→ test whether it can recover
→ test whether its present state is sufficient for its future
→ use a controlled future split to test whether missing state is needed
→ preserve the simpler state when a strong no-split result survives the declared test
→ test the architecture against strong ordinary baselines
→ publish nulls as well as wins
```

For the detailed dependency map, use the [Canon Map](CANON_MAP.md) and [Cross-Support and Traversal Map](docs/24_MKUFT_CROSS_SUPPORT_AND_TRAVERSAL_MAP.md).

## Known failure modes — including our own

A framework can be technically careful and still fail at the reader interface. We treat that as a real failure mode rather than blaming the reader.

The most obvious risk in this repository is **dependency-history asymmetry**. The work was built step by step, so the authoring process remembers why each term exists. A new reader meets the final vocabulary without living through the failures that forced those distinctions. Perfectly legitimate compression can therefore look like unexplained jargon.

A second risk is **link substitution**: pointing to ten correct files instead of explaining the relation between them. A link is an address, not an explanation.

A third risk is **academic compression**: technically accurate prose can become so dense that it hides the simple question being asked. Public-facing text should therefore give the ordinary-English object first and the formal object second.

There are scientific failure modes too. MKUFT fails or contracts where:

- an added layer or address distinction makes no useful difference;
- a higher-level variable cannot predict the declared property better than the lower or multiscale account;
- a claimed cross-layer coupling has no physical carrier or measurable consequence;
- an observer-linked claim converges to null under adequate blinded testing;
- a proposed geometry adds no value beyond ordinary models;
- a physics-facing branch fails Bell compatibility, no-signalling, dimensional consistency, or standard-physics recovery;
- a claimed novelty disappears when compared with the strongest fair prior art or ordinary baseline;
- a result can be reproduced by a flat, replayed, scrambled, or otherwise simpler control;
- a failed branch is rescued by changing its meaning after the result;
- failed or null branches are pruned from the live theory and then omitted when the parent framework is credited as a successful scientific generator;
- a post-failure repair is treated as confirmed by the same evidence that generated the repair rather than tested prospectively.

Locality controls what a branch result proves; it does not erase the branch from the parent generator's performance history. A framework may learn from a failure, but a replacement branch requires fresh evidence and the original miss remains on the record. The full rule is in [Branch Lineage, Generator Accountability, and Anti-Hydra Discipline](docs/29A_BRANCH_LINEAGE_GENERATOR_ACCOUNTABILITY_AND_ANTI_HYDRA_DISCIPLINE.md).

The full technical list is in the [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md).

For the reader-interface problem itself, see [Reader Contact, Translation, and Failure Guide](READER_CONTACT_AND_FAILURE_GUIDE.md).

## What is established, what is proposed

The mathematics used by MKUFT includes established tools and familiar neighbouring ideas. Similarity to established mathematics validates the *mathematical grammar* where the mapping is correct. It does not validate MKUFT's physical ontology.

The framework presently contains several different claim levels:

1. conceptual proposals;
2. mathematical scaffolds;
3. operational hypotheses;
4. discriminating predictions;
5. empirical relations, where independently established;
6. mechanism-level claims, where earned;
7. foundational physical theory.

MKUFT as a whole has **not** reached level 7.

The current strongest novelty language is deliberately bounded: parts of the work are presented as candidate original formal syntheses or operational meta-principles after subtraction of known neighbouring work. Stronger physical claims require prospective quantitative success and independent testing.

## Current public research objects

The current principal DOI-bearing MKUFT publication is **MKUFT — A Relational Architecture for Physical Law and Cross-Scale Dynamics**, v2, published 17 August 2026: [DOI 10.5281/zenodo.21973064](https://doi.org/10.5281/zenodo.21973064).

The current research-facing synthesis is **MKUFT — Layer Before Law: A Typed Relational Architecture for Physical-Law Selection, Future-Sufficient Interfaces, and Cross-Scale Dynamics**, v1.2, dated 30 August 2026. It is public in this repository, not yet DOI-bearing, and not peer reviewed: [human-reader route](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md).

The published **Cross-Domain Compositional Schema v0.4** has version DOI `10.5281/zenodo.22166468` and concept DOI `10.5281/zenodo.22164561`. Its Bell/tetrahedral calibration retains a NULL independent physical residual. Live calibration/future-sufficiency folds are [Module 28A](docs/28A_CROSS_DOMAIN_COMPOSITIONAL_SCHEMA_BELL_CHSH_CALIBRATION.md) and [Module 33S7A](docs/33S7A_FUTURE_SUFFICIENT_ADDRESS_INVARIANT_AND_LAYER_BEFORE_LAW_PRECEDENCE.md); exact relation removal is treated as **protocol-relative exact-relation deformation**, not an automatic causal intervention.

The published **Bell Constraints as Typed Boundaries v1.0** has version DOI `10.5281/zenodo.22100926`. Its tested independent Bell-local new-physics delta is NULL; the retained result is the typed relation/access/completion/scale and falsification architecture.

The published **Future-Splitting State Recruitment v1.0** has version DOI `10.5281/zenodo.22058303`: [paper route](papers/2026-08-22_FUTURE_SPLITTING_STATE_RECRUITMENT_v1.0.md) and [canonical module fold](docs/33S7_FUTURE_SPLITTING_STATE_RECRUITMENT_STATE_ADEQUACY_AND_PROSPECTIVE_MECHANISM_LOCALISATION.md).

The published **ATLD 2 v2.0** has version DOI `10.5281/zenodo.22068803`. It is a methods/evaluation paper with an exploratory 15-case execution pilot; no confirmatory system superiority or completed validation of the candidate residual coordinates is claimed.

Historical publication-family identity routes retained for provenance include Voynich predecessor DOI `10.5281/zenodo.18178638` and ATLD v1.0 DOI `10.5281/zenodo.21341521`.

For the complete publication list, version identities, frozen carriers, and DOI routes, use [Papers and Publications](papers/README.md).

## Where to start

If you want the shortest human route, read:

1. [Start Here — Public Overview](START_HERE_PUBLIC_OVERVIEW.md)
2. [Reader Contact, Translation, and Failure Guide](READER_CONTACT_AND_FAILURE_GUIDE.md)
3. [Scientific Reader Traversal Guide](SCIENTIFIC_READER_TRAVERSAL_GUIDE.md)
4. [Layer Before Law](docs/26_LAYER_BEFORE_LAW_MKUFT_QUANTUM_GRAVITY_REFRAMING.md)
5. [Falsification Summary](docs/05_FALSIFICATION_SUMMARY.md)

The scientific traversal guide is the handoff between plain-language understanding and the hard modules. It explains what the equations are trying to establish and what a non-specialist can leave to domain experts without losing the scientific chain.

If you already know the field and want the technical chain, use the [Canon Map](CANON_MAP.md).

If you want papers rather than live modules, use [Papers and Publications](papers/README.md).

If you want the current submission synthesis, use [MKUFT Layer Before Law v1.2](papers/2026-08-30_MKUFT_LAYER_BEFORE_LAW_SUBMISSION_SYNTHESIS_v1.2.md).

## Development and provenance

This repository is live and continues to develop. DOI-bearing publications remain frozen publication objects; later GitHub work does not silently rewrite them.

Presentation defects, stale links, rendering problems, or confusing explanations are treated as defects to repair, not as intended scientific notation. Changes to the live repository should preserve version identity, provenance, and the difference between a live module, a repository paper route, and a frozen publication.

The project uses AI-assisted research tooling for drafting, checking, traversal, and consistency work. AI output is not treated as scientific evidence merely because an AI produced it.

## Human use

Some MKUFT material also carries practical ideas about boundaries, recovery, relation, responsibility, uncertainty, cohesion, and preserving a route forward after failure. Readers may explore those ideas separately from the physics.

If an AI is used for that purpose, a useful constraint is to ask it to interpret from the supplied MKUFT material without importing outside theories or invented additions. The result remains an interpretation of the framework, not an additional scientific finding.

Some of this work came from equations. Some came from life. They are not the same thing, but they can sometimes illuminate one another.
