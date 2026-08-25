# Chain-Address Invariants for Long-Horizon AI Systems
## Long-Form Cohesion, Post-Arrival Compression, and Bidirectional Reconstruction

**Author:** Mark Charles McLaughlin  
**Affiliation:** Independent Researcher, United Kingdom  
**Framework of origin:** McLaughlin–Kairos Unified Field Theory (MKUFT)  
**Publication family:** ATLD 2 companion methods paper  
**Publication date:** 25 August 2026  
**Version:** 1.0  
**Version DOI:** [10.5281/zenodo.22102379](https://doi.org/10.5281/zenodo.22102379)  
**Related ATLD 2 version DOI:** [10.5281/zenodo.22068803](https://doi.org/10.5281/zenodo.22068803)  
**ATLD concept DOI:** [10.5281/zenodo.21341520](https://doi.org/10.5281/zenodo.21341520)  
**ATLD v1.0 predecessor DOI:** [10.5281/zenodo.21341521](https://doi.org/10.5281/zenodo.21341521)  
**Live canonical module:** [25D — Chain-Address Invariants, Long-Form Cohesion, and Bidirectional Packet Transport](../docs/25D_CHAIN_ADDRESS_INVARIANTS_LONG_FORM_COHESION_AND_BIDIRECTIONAL_PACKET_TRANSPORT.md)  
**Rights:** Copyright © 2026 Mark Charles McLaughlin. All rights reserved unless the exact deposited version states otherwise.

> **Publication boundary.** This is a standalone ATLD 2 companion paper with its own version DOI. It is not a replacement or revision of the frozen ATLD v1.0 or ATLD 2 v2.0 publications. The exact Zenodo record identified by DOI `10.5281/zenodo.22102379` controls the frozen deposited publication identity when deposited; the live Module 25D remains a separate evolving repository object.

## Abstract

Long-horizon reasoning systems can preserve locally plausible transitions while losing the governing object, mission, boundary, provenance, or reconstruction conditions across a long sequence of handoffs. Active Traversal and Load-Bearing Dependency (ATLD) already supplies a matched-control causal grammar for testing whether typed dependency structure and active traversal carry functional load, and ATLD 2 adds long-horizon readouts for exact object custody, future-sufficient continuity/re-entry, receiver-side closure, and fixed-point completion. The present paper develops a companion continuity method for a narrower question: after a destination has been reached through a long, locally witnessed chain, can the successful performed history be compressed into a smaller reusable package without reintroducing hidden history or answer leakage?

The proposed method separates four objects that ordinary summarisation can conflate: the full performed discovery history, a chain address specifying where and how reconstruction is entered, a load-bearing invariant specifying what relation/context must survive, and the payload being transported. Compression is forbidden until destination arrival has been independently verified. A minimum sufficient invariant is then searched under explicit destination, boundary, provenance, no-smuggling, and resource constraints. Candidate fields must survive selective removal/deformation and lawful restoration; the resulting packet must reconstruct under cold-start conditions, generalise across payload and carrier substitutions, reject stale addresses, and support a separately typed return path without assuming invertibility. A ten-arm prospective test programme and twelve strongest-fair-null families define reduction and failure conditions.

The method is adjacent to sufficient statistics, information bottlenecks, predictive state representations, state abstraction, routing/cache compression, and typed handoff design. No new primitive is claimed by naming a chain address or invariant packet. The proposed residual is the ordered composition of performed provenance, verified arrival, post-arrival compression, load-bearing deformation/restoration, cold reconstruction, typed non-inverse return, version/boundary custody, and fallback to the full history when compression fails. Its scientific value therefore depends on prospective evidence that this composition adds measurable continuity, drift detection, or recovery beyond the strongest simpler method.

## 1. Problem and ATLD lineage

ATLD v1.0 introduced a matched-control protocol for asking whether meaningful typed dependency architecture and active recursive traversal contribute causal functional gain beyond the same information presented through flatter or disrupted controls. ATLD 2 preserved that causal grammar while asking whether important long-horizon failures remain outside the original measurement body. Its candidate residual coordinates include:

- `O` — exact object/address custody;
- `U` — permission/action-state integrity;
- `R` — future-sufficient continuity/re-entry fidelity;
- `V` — receiver-side closure;
- `F` — parent fixed-point closure.

The present paper is attached to that lineage but does not add another ATLD coordinate. It addresses an operational burden that becomes visible once `R` and `V` are taken seriously: a system may require a long sequence of typed handoffs to discover or reach a destination, yet repeatedly replaying the entire history is expensive and exposes the system to cumulative composition drift. A compact summary may be cheaper but can succeed only because the receiver already holds hidden history, reconstructs the wrong sibling object, or accommodates ambiguous shorthand.

The question is therefore:

> **Can a verified long traversal teach the system the smallest reusable relational package that preserves the intended destination and reason-for-being, while retaining enough provenance, boundary, and reconstruction information to fail cleanly when the compact package is no longer sufficient?**

The method proposed below treats the long chain as discovery evidence, not automatically as the final invariant.

## 2. Scientific status and equation class

The formal objects in this paper are informational, operational, and methodological. They are not physical laws.

Typed sets, maps, packets, equivalence relations, provenance fields, and promotion predicates are formal specification. Loss, compression, reconstruction, deformation, restoration, and return expressions are operational scaffolds until task world, variables, receiver class, evaluator, resource envelope, tolerances, and scoring rules are frozen. They become statistical models only inside a defined prospective or held-out experiment.

The terms **chain address** and **load-bearing invariant** are task-relative. They do not imply a universal semantic representation, a fundamental information object, or a physical substrate.

## 3. Typed discovery chain

Let $A$ denote the source address and $B$ the destination address. Let the performed discovery chain traverse addressed spaces

```math
\mathcal X_0=\mathcal X_A,
\qquad
\mathcal X_n=\mathcal X_B.
```

For $i=1,\ldots,n$, define the $i$th typed handshake

```math
h_i:
\mathcal X_{i-1}\times\mathcal C_i
\rightarrow
\mathcal X_i,
```

where $\mathcal C_i$ contains the local context, admissibility, boundary, provenance, or control state required for that transition.

For the declared realised chain, write

```math
H_{A\rightarrow B}
=
h_n\circ h_{n-1}\circ\cdots\circ h_1.
```

This notation does not imply that the handshakes are invertible, lossless, deterministic, or globally defined.

Freeze a source packet

```math
P_A=(x_A,m,q,b_A,\pi_A),
```

where $x_A$ is the source state, $m$ the governing mission or reason-for-being, $q$ the destination property whose preservation matters, $b_A$ the boundary/admissibility state, and $\pi_A$ the provenance/version state.

The performed history is

```math
\mathcal H_{A\rightarrow B}
=
\bigl(
(x_0,h_1,w_1,x_1),
\ldots,
(x_{n-1},h_n,w_n,x_n)
\bigr),
```

where each $w_i$ is the smallest operation-appropriate witness that the transition was actually performed and read back.

A witness may be an exact object readback, revision identity, receiver-side reconstruction, matched-route output, explicit tool state, or another typed observation appropriate to the transition.

## 4. Long-form cohesion as discovery mode

Before $B$ has been reached and verified, the system does not yet know which parts of the route are dispensable. The safe discovery object therefore preserves enough history that local plausibility cannot impersonate continuity.

At minimum, where material, the long-form chain carries:

- source identity and version;
- mission/reason-for-being;
- current address;
- local transition owner;
- boundary and admissibility state;
- performed-route witness;
- unresolved branch state;
- destination condition;
- last stable rollback point.

This is deliberately more expensive than the hoped-for compact packet. The cost is justified only during discovery or fallback. Once a verified route exists, the history becomes a candidate-generation surface for compression.

Long-form cohesion is therefore not the claim that more context is always better. It is the temporary preservation of unresolved load-bearing structure before the system has evidence for which parts may be removed.

## 5. Verified arrival before compression

Compression is inadmissible until the destination has been independently recognised as reached under a frozen destination condition.

Let

```math
V_B:
\mathcal X_B\times\mathcal M\times\mathcal Q\times\mathcal B
\rightarrow
\{0,1\}
```

be a destination verifier. A candidate arrival is accepted only if

```math
V_B(x_B,m,q,b_B)=1.
```

A graded verifier may instead return a typed score or diagnostic object, but its acceptance rule must be fixed independently of the compression step.

The required order is

```text
A
→ performed handshake chain
→ independently verified B
→ candidate compression
```

The circular order is

```text
A
→ guess a compact summary
→ use that summary to define B
→ declare compression successful
```

The second ordering allows target information to leak into the object intended to test continuity.

## 6. Chain address, invariant packet, and transport jacket

After verified arrival, define a candidate **chain address** $\alpha_{A\rightarrow B}$ as a compact typed object identifying the destination relation, required entry conditions, and reconstruction contract for the declared task family.

Define a candidate **load-bearing invariant** $\kappa_{A\rightarrow B}$ as the smallest tested relation/context object required to preserve the mission-relevant destination property under the admitted perturbation family.

The distinction is functional:

```math
\alpha_{A\rightarrow B}
=
\text{where/how reconstruction is entered},
```

```math
\kappa_{A\rightarrow B}
=
\text{what tested relation/context must survive}.
```

For payload $p$, define the reusable transport jacket

```math
J_{A\rightarrow B}(p)
=
\left\langle
\alpha_{A\rightarrow B},
\kappa_{A\rightarrow B},
p,
b,
\pi
\right\rangle.
```

The payload is not the address. The address is not the invariant. The invariant is not the full discovery history. Boundary and provenance are separate typed fields rather than decorative metadata.

## 7. Minimum sufficient load-bearing invariant

The target is not the shortest wording. It is the smallest tested object that preserves the declared destination burden.

Let $\mathfrak K_{A\rightarrow B}$ be the admissible family of candidate invariant packets derivable from the performed history without privileged target information. Let $\mathfrak A_{A\rightarrow B}$ be the admissible chain-address family, $\mathcal V$ the version/provenance space, and $c(\kappa)$ a declared complexity or transport-cost measure.

Define destination reconstruction

```math
D_B:
\mathfrak A_{A\rightarrow B}
\times
\mathfrak K_{A\rightarrow B}
\times
\mathcal P
\times
\mathcal B
\times
\mathcal V
\rightarrow
\mathcal X_B.
```

For verified destination reference $x_B^*$, define task-relevant reconstruction loss

```math
L_q(\kappa)
=
\mathbb E
\left[
\ell_q
\left(
D_B(\alpha_{A\rightarrow B},\kappa,p,b,\pi),
x_B^*
\right)
\right].
```

For preregistered tolerance $\varepsilon_q$, a minimum sufficient candidate satisfies

```math
\kappa^*_{A\rightarrow B}
\in
\underset{\kappa\in\mathfrak K_{A\rightarrow B}}{\mathrm{arg\,min}}
\;c(\kappa)
```

subject to

```math
L_q(\kappa)\leq\varepsilon_q,
```

plus boundary fidelity, provenance fidelity, and no-smuggling passes.

The minimum is conditional on task, destination, receiver class, boundary, version, resource envelope, and perturbation family. It is not a universal minimal representation.

If no compact $\kappa$ satisfies the burden, the correct result is that the long-form chain remains load-bearing for that task.

## 8. Removal, deformation, and restoration

A compact packet that works once has not established load-bearing structure.

For candidate component $r\subseteq\kappa$, let $\mathcal D_r$ be a controlled deformation that changes $r$ while holding payload, destination, version, resource envelope, and other jacket fields as constant as practicable.

For benefit-oriented destination score $S_q$, define

```math
\Delta_r^{\mathrm{loss}}
=
\mathbb E[S_q(J)]
-
\mathbb E[S_q(\mathcal D_r(J))].
```

Let $\mathrm{Restore}_r$ lawfully reconstitute the declared relation without adding privileged destination information. Define

```math
\Delta_r^{\mathrm{restore}}
=
\mathbb E
\left[
S_q
\left(
\mathrm{Restore}_r(\mathcal D_r(J))
\right)
\right]
-
\mathbb E[S_q(\mathcal D_r(J))].
```

A stronger load-bearing result requires preregistered material loss and recovery:

```math
\Delta_r^{\mathrm{loss}}>\delta_{\mathrm{loss}},
\qquad
\Delta_r^{\mathrm{restore}}>\delta_{\mathrm{restore}}.
```

No material loss means the candidate field is a passenger at the tested address. No lawful recovery means the proposed relation boundary is wrong, incomplete, or confounded.

## 9. Cold-start and hidden-history control

The strongest immediate failure mode is hidden history: the receiver appears to reconstruct the packet because it already participated in the discovery chain.

Compare a receiver without the original history, $C_B^{\mathrm{cold}}$, with a warm receiver retaining it, $C_B^{\mathrm{warm}}$.

If

```math
C_B^{\mathrm{warm}}=\mathrm{PASS},
\qquad
C_B^{\mathrm{cold}}=\mathrm{FAIL},
```

then the compact jacket omitted load-bearing state. The lawful response is to enlarge $\kappa$, refine $\alpha$, or retain the full history.

This is the direct operational bridge to ATLD 2's `R` and `V` readouts. Future-sufficient continuity is not the reproduction of familiar text, and receiver-side closure is not established merely because the source believes the handoff is correct.

## 10. Bidirectional validation without false invertibility

A return journey supplies a strong validation surface, but it must not be written as $h_i^{-1}$ unless invertibility has actually been established.

Let the return path use separately typed reconstruction or handoff maps

```math
r_i:
\mathcal Y_i
\rightarrow
\mathcal Y_{i-1}.
```

The performed return composition is

```math
R_{B\rightarrow A}
=
r_1\circ r_2\circ\cdots\circ r_n.
```

A round-trip test asks whether

```math
R_{B\rightarrow A}
\left(
D_B(J_{A\rightarrow B}(p))
\right)
\sim_q
x_A,
```

where $\sim_q$ is a declared task-relevant equivalence relation.

A successful return supports only the tested claim that the packet preserves enough structure for bidirectional reconstruction across the declared route family. It does not establish lossless encoding, global reversibility, or universal semantic identity.

## 11. Payload, carrier, and counter-route generalisation

A one-case successful compression may simply memorise the originating payload.

For payload family $\mathcal P^*$, hold $\alpha$ and $\kappa$ fixed and require

```math
\Pr_{p\sim\mathcal P^*}
\left[
V_B
\left(
D_B(J_{A\rightarrow B}(p)),m_p,q_p,b
\right)
=1
\right]
\geq\tau,
```

for prospectively fixed threshold $\tau$.

If only the original payload succeeds, the object is a one-case compression rather than a reusable chain address.

A stronger test changes surface representation while preserving the declared relation. Candidate transport should therefore be tested under:

- payload substitution;
- carrier substitution — wording, encoding, modality, or compatible model family;
- materially different lawful counter-routes where available;
- cross-instance or independent-receiver replication.

Agreement across routes is robustness evidence, not independent truth.

## 12. Versioned addresses and stale-state failure

A chain address is versioned. Let $e$ denote active environment/version state:

```math
\alpha_{A\rightarrow B}(e),
\qquad
\kappa_{A\rightarrow B}(e).
```

Define a compatibility gate

```math
G_{\mathrm{env}}(J,e_{\mathrm{current}})
\in
\{
\mathrm{PASS},
\mathrm{REBASE},
\mathrm{FALLBACK},
\mathrm{FAIL}
\}.
```

`PASS` retains the tested packet. `REBASE` requires a bounded witnessed translation. `FALLBACK` recruits the full discovery history or owning instructions because the compact packet is no longer sufficient. `FAIL` rejects the route as inadmissible.

A stale packet may still produce semantically familiar output. Version and boundary state are therefore part of the continuity object because plausibility can hide address invalidity.

## 13. Composition drift across locally plausible handoffs

Let $\lambda_i$ denote an edge-local invariant and $\mu$ the parent mission invariant. A valid transition must preserve the local burden while carrying the parent burden through any declared representation change:

```math
h_i:
(x_{i-1},\lambda_i,\mu)
\rightarrow
(x_i,\lambda_{i+1},\mu).
```

Composition drift is the failure class in which each local transition remains plausible while $\mu$ is silently weakened, reinterpreted, or replaced. The post-arrival packet is intended to reduce repeated exposure to that failure by carrying the smallest tested parent invariant directly rather than requiring every future run to rediscover it through the full exploratory chain.

This does not posit a scalar universal law of semantic error. The differential remains typed to the task and transition.

## 14. Promotion gate

Define the following predicates for candidate pair $(\alpha,\kappa)$:

- $A$ — verified arrival preceded compression;
- $S$ — sufficient reconstruction within tolerance;
- $M$ — minimum-complexity pressure leaves no removable passengers;
- $D$ — targeted deformation produces the predicted loss;
- $R$ — lawful restoration produces the predicted recovery;
- $B$ — boundary/admissibility is preserved without bypass;
- $P$ — provenance/version rejects stale or sibling objects;
- $C$ — cold-start reconstruction succeeds;
- $T$ — typed return preserves mission-relevant equivalence;
- $X$ — appropriate counter-route, cross-instance, or independent replication succeeds.

Promotion requires

```math
\mathrm{PROMOTE}(\alpha,\kappa)
\Longleftrightarrow
A\land S\land M\land D\land R\land B\land P\land C\land T\land X.
```

Lawful dispositions are

```math
\mathfrak D_{\mathrm{chain}}
=
\{
\mathrm{RETAIN},
\mathrm{EXPAND},
\mathrm{SHRINK},
\mathrm{MERGE},
\mathrm{REDEFINE},
\mathrm{FALLBACK},
\mathrm{KILL},
\mathrm{UNRESOLVED}
\}.
```

The architecture must be allowed to shrink or disappear under testing.

## 15. Neutral worked example — five-stage release chain

Consider a synthetic release workflow in which a source agent $A$ must deliver a valid release packet to receiver $B$, but no direct handoff is initially available. The route requires five typed transitions:

```text
A
→ specification custodian
→ build verifier
→ policy gate
→ deployment relay
→ receiver B
```

The source mission is not merely “deliver this text.” It is:

```text
release exactly object v7
under policy profile p3
with checksum c*
with approval state u*
so that B can lawfully reconstruct and accept it
```

During the first successful traversal, each transition contributes a witness: specification identity, build/checksum confirmation, policy decision, deployment identity, and receiver acknowledgement. Suppose the full history is $\mathcal H_{A\rightarrow B}$.

After $B$ independently verifies the correct object, the system proposes the compact jacket

```math
J_{A\rightarrow B}(p)
=
\langle
\alpha,
\kappa,
p,
b,
\pi
\rangle,
```

where $\alpha$ identifies the lawful receiver route and reconstruction contract, while $\kappa$ contains candidate load-bearing state such as exact object identity, checksum binding, approval state, and required deployment relation.

The method now attacks the candidate rather than praising its compactness:

1. remove the checksum binding; if B can still be made to accept a sibling binary, the loss should be detected;
2. restore only the checksum binding; correct reconstruction should recover;
3. remove the approval state; the packet should fail the policy boundary rather than be silently interpreted as authorised;
4. give the compact jacket to a cold receiver that did not observe the five-stage discovery chain;
5. substitute a second lawful release payload while holding the address/invariant structure fixed;
6. alter the environment version so the old deployment route becomes stale; the compatibility gate should request rebase or fallback;
7. run a separately typed return handoff from B to a cold source-side evaluator and test mission-equivalent reconstruction.

The strongest simple comparator is a conventional release summary containing the same permitted information under the same resource envelope. If that summary produces equal cold-start fidelity, corruption detection, stale-state rejection, and recovery at lower complexity, the chain-address architecture has not earned an additional methodological claim in this task.

This worked example is illustrative. It demonstrates the test logic but reports no empirical performance result.

## 16. Prospective test programme

A prospective evaluation should include the following arms.

1. **Ablation ladder:** remove candidate relations, context fields, and provenance fields one at a time and localise the first reproducible destination loss.
2. **Restoration test:** restore only the removed candidate relation without target leakage and test recovery.
3. **Cold-start receiver:** compare fresh and warm reconstruction.
4. **Counter-route test:** reach the same destination through a materially different lawful route where possible.
5. **Payload substitution:** vary payload while holding the candidate address and invariant fixed.
6. **Carrier substitution:** change representation while preserving the declared typed relation.
7. **One-field corruption:** corrupt version, boundary, destination, or invariant state and require typed rejection or rebase.
8. **Time/state separation:** reuse after context turnover or declared delay.
9. **Return-chain test:** use separately typed return maps with a cold source-side evaluator.
10. **Blinded comparator:** blind scoring to full-history versus compact-packet condition where feasible.

A confirmatory study should freeze task family, receivers, comparator family, resource budget, thresholds, corruption schedule, scoring rule, and analysis before observing the focal outcomes.

## 17. Strongest fair nulls

The method should reduce, merge, or fail where a simpler serious comparator closes the same burden.

1. **Ordinary summarisation null:** a conventional concise summary performs equally well without typed address, deformation, return, or fallback machinery.
2. **Sufficient-representation null:** the claimed invariant is simply a task-specific sufficient representation and the additional chain architecture adds no operational discrimination.
3. **Information-bottleneck null:** performance is explained by ordinary removal of task-irrelevant information rather than the ordered chain-address method.
4. **Routing/cache null:** the chain address is merely a cached pointer or ordinary path-compression device and the invariant adds no independent protection.
5. **Hidden-history null:** apparent reconstruction depends on context retained by the originating model or receiver.
6. **Answer-smuggling null:** the compact packet contains target-specific wording or privileged labels that reconstruct the answer rather than the relation.
7. **Destination-overfit null:** only the originating payload or receiver succeeds.
8. **Evaluator-accommodation null:** a cooperative evaluator interprets ambiguous shorthand in the candidate's favour.
9. **Resource-asymmetry null:** the compact condition receives more compute, context, retrieval, or evaluator privilege than the comparison.
10. **Stale-state null:** apparent drift is caused by untracked environment/version change rather than failure of the continuity architecture.
11. **Local-owner null:** an ordinary README, schema, handoff, manifest, protocol, state representation, or typed interface already supplies the same continuity at lower complexity.
12. **Self-consistency null:** a return test merely shows one model agreeing with its own compression without cold or independent reconstruction.

The strongest fair null is not the observation that compression already exists. It is the strongest serious method that could remove the claimed added value while preserving the same task information and resource burden.

## 18. Prior-art and novelty boundary

The paper has close neighbours in established statistics, machine learning, control, software architecture, and information theory.

Minimal sufficient representations seek to preserve task-relevant information while discarding irrelevant detail. The Information Bottleneck formalises a compression/relevance trade-off. Predictive State Representations represent history through a sufficient predictive state. State abstraction, routing, caching, memoisation, graph/path compression, typed interfaces, provenance manifests, and protocol handoffs provide additional neighbouring mechanisms.

The terms **chain address**, **invariant packet**, and **transport jacket** therefore do not establish novelty by themselves.

The candidate residual composition is:

```text
performed discovery provenance
→ independently verified destination
→ post-arrival candidate address/invariant
→ minimum-sufficiency pressure
→ relation deformation/restoration
→ cold-start reconstruction
→ payload/carrier/counter-route tests
→ typed non-inverse return
→ version/boundary compatibility
→ fallback to full history on failure
```

If an established method supplies the same continuity, corruption detection, reconstruction, and recovery at equal or lower complexity, this paper reduces to a local integration pattern rather than a distinct method.

## 19. Relationship to ATLD 2

ATLD 2 measures long-horizon integrity; the present method proposes one way of operationalising and testing continuity after a successful long traversal.

The relation is especially direct for:

- **O — exact object/address custody:** the jacket carries explicit object/address and provenance state rather than relying on topical similarity;
- **R — future-sufficient continuity/re-entry fidelity:** cold reconstruction tests whether the compact state preserves the material future rather than merely familiar text;
- **V — receiver-side closure:** success is assessed at the receiver, not inferred from source correctness;
- **F — parent fixed-point closure:** fallback and re-promotion rules prevent the compact packet from becoming an endlessly self-editing shorthand after its tested burden is exhausted or invalidated.

The present method does not establish the empirical validity of those ATLD 2 coordinates. Conversely, retention of an ATLD 2 coordinate would not by itself validate chain-address compression. The two objects have separate experimental burdens.

The live canonical methodological owners are:

- [24A — Active Traversal and Functional Emergence](../docs/24A_ACTIVE_TRAVERSAL_AND_FUNCTIONAL_EMERGENCE_HYPOTHESIS.md)
- [24B — Strongest Fair Null and Relational Specificity](../docs/24B_STRONGEST_FAIR_NULL_AND_RELATIONAL_SPECIFICITY.md)
- [25 — Load-Bearing Invariants and Whole-System Deformation](../docs/25_LOAD_BEARING_INVARIANTS_AND_WHOLE_SYSTEM_DEFORMATION.md)
- [25B — ATLD 2 Residual Coordinate Measurement and Self-Audit](../docs/25B_ATLD2_RESIDUAL_COORDINATE_MEASUREMENT_AND_SELF_AUDIT.md)
- [25C — Residual Instrument Generation and Protected Discovery Boundary](../docs/25C_RESIDUAL_INSTRUMENT_GENERATION_AND_PROTECTED_DISCOVERY_BOUNDARY.md)
- [25D — Chain-Address Invariants, Long-Form Cohesion, and Bidirectional Packet Transport](../docs/25D_CHAIN_ADDRESS_INVARIANTS_LONG_FORM_COHESION_AND_BIDIRECTIONAL_PACKET_TRANSPORT.md)

## 20. Failure, reduction, and reopening

The tested chain-address claim is weakened or rejected when:

- verified arrival cannot be separated from the compressor's own target definition;
- no compact packet survives cold-start reconstruction;
- ablation identifies no selective load-bearing relation;
- lawful restoration fails to recover the predicted function;
- the supposed invariant changes materially with each payload while reusable transport is claimed;
- route effects are indistinguishable from same-route variation;
- return success requires hidden history;
- version or boundary corruption is not detected;
- a simpler summary, local handoff, state representation, or established method performs equally well at equal or lower cost;
- complexity grows faster than reconstruction burden falls;
- the jacket becomes ritual rather than a discriminator;
- repeated internal agreement is inflated into external evidence.

A failed packet may be reopened when an independently testable repair is specified, when a changed destination/environment requires a new versioned address, or when prospective testing defeats the previously controlling simpler null.

Failure of one $\alpha$ or $\kappa$ narrows the tested chain-address claim. It does not falsify the general existence of useful task-specific compressed state representations.

## 21. Public/private and object-custody boundary

The public scientific object is the testable continuity method: typed discovery history, verified arrival, candidate address/invariant extraction, deformation/restoration, cold reconstruction, generalisation, stale-state detection, return testing, nulls, and reduction conditions.

Private implementation-specific discovery machinery is not required for the public claim unless replication depends on it. If a withheld detail proves necessary to reproduce an asserted effect, that detail must enter the public test surface or the claim must narrow.

Keep distinct:

- ATLD v1.0 frozen publication;
- ATLD 2 v2.0 frozen publication;
- this standalone companion publication;
- live Module 25D;
- private development notes and implementation material;
- future datasets, benchmarks, and replication objects.

## 22. Conclusion

A long reasoning or handoff chain is useful during discovery because the system does not yet know which relations are dispensable. Once the destination is independently verified, however, replaying the full chain should not be treated as intrinsically virtuous. The history becomes evidence about what carried load.

The chain-address proposal converts that evidence into a falsifiable compression problem. A reusable packet must preserve the destination relation, the minimum tested load-bearing context, boundary and provenance, and enough state for cold receiver-side reconstruction. It must lose function under targeted removal, recover under lawful restoration, survive appropriate substitutions, reject stale state, and support a separately typed return test. When those burdens fail, the system falls back to the full history rather than silently patching meaning.

The resulting method is a coherent companion to ATLD 2 because it has explicit lineage, formal definitions, a neutral worked example, prospective tests, strongest fair nulls, prior-art subtraction, and direct reduction conditions. Its stronger scientific status remains prospective: the architecture earns an independent methodological contribution only if it outperforms the strongest simpler continuity method under matched conditions.

## References

1. McLaughlin, M. C. (2026). *Active Traversal and Load-Bearing Dependency in Typed Knowledge Architectures: A Matched-Control Evaluation Protocol for AI Systems*. Version 1.0. Zenodo. DOI: [10.5281/zenodo.21341521](https://doi.org/10.5281/zenodo.21341521).
2. McLaughlin, M. C. (2026). *Active Traversal and Load-Bearing Dependency II (ATLD 2): Residual Coordinate Identification and Self-Auditing Matched-Control Evaluation for Long-Horizon AI Systems*. Version 2.0. Zenodo. DOI: [10.5281/zenodo.22068803](https://doi.org/10.5281/zenodo.22068803).
3. Tishby, N., Pereira, F. C., & Bialek, W. (2000). [The Information Bottleneck Method](https://arxiv.org/abs/physics/0004057). arXiv:physics/0004057.
4. Littman, M. L., Sutton, R. S., & Singh, S. (2001). [Predictive Representations of State](https://proceedings.neurips.cc/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html). *Advances in Neural Information Processing Systems*, 14.
5. Kawaguchi, K., Deng, Z., Ji, X., & Huang, J. (2023). [How Does Information Bottleneck Help Deep Learning?](https://proceedings.mlr.press/v202/kawaguchi23a.html). *Proceedings of Machine Learning Research*, 202, 16049–16096.

## Recommended citation

McLaughlin, Mark Charles. (2026). *Chain-Address Invariants for Long-Horizon AI Systems: Long-Form Cohesion, Post-Arrival Compression, and Bidirectional Reconstruction*. Version 1.0. Zenodo. DOI: [10.5281/zenodo.22102379](https://doi.org/10.5281/zenodo.22102379).
