# MKUFT — Standalone Formal Addendum

Author: Mark McLaughlin

Status: official cleaned working copy for the private MKUFT GitHub repository.

## Relationship to Core

This addendum extends and sharpens the original MKUFT core paper. It does not replace the core and introduces no new ontology, entities, or metaphysical assumptions.

Its purpose is to formalise concepts already present in MKUFT using a node/trajectory/coherence-cost model.

## 1. Architectural Premise

MKUFT treats geometry as architecture, not decoration.

Geometric relations determine:

- which states of reality are stable,
- which transitions between states are permissible,
- the relative coherence cost of such transitions.

Physical laws are treated as emergent behaviours constrained by this architecture.

## 2. Mathematical State Space

Define the permissible state space as a constrained graph:

```text
G = (N, E)
```

Where:

- N = set of stable attractor states or nodes.
- E = set of admissible transitions or edges.

Nodes correspond to symmetry-locked, coherence-stable solutions permitted by geometric constraint.

The grammar of N is finite, while traversal through the graph can be unbounded.

## 3. Trajectories

A trajectory γ is an ordered path through G:

```text
γ = (n_0 → n_1 → n_2 → ... → n_k)
```

Traversal is governed by adjacency constraints. Not all node pairs are directly connected.

Agency, interaction, evolution, learning, and observation occur as constrained traversal, not arbitrary state creation.

## 4. Coherence Cost Functional

Each trajectory carries a traversal cost:

```text
C[γ] = ∫_γ λ(x) ds
```

Where:

- λ(x) = local coherence friction / gradient tension.
- ds = differential path element along γ.

Interpretation:

- Low λ(x): smooth, stable traversal.
- High λ(x): resistance, instability, or distortion.

Traversal cost is structural, not merely subjective.

## 5. Probability as Path Density

Transition likelihood between node A and node B is defined as:

```text
P(B | A) ∝ Σ_{γ ∈ Γ(A→B)} exp(-C[γ])
```

Where:

- Γ(A→B) = set of admissible trajectories between A and B.

Probability is an emergent property of path availability and cost, not intrinsic randomness alone.

## 6. Learning and Adaptation

Learning is defined as local reduction of coherence friction λ(x) along frequently traversed paths.

- No new nodes are required.
- Structural grammar remains unchanged.
- Skill acquisition corresponds to reduced traversal cost.

Learning is therefore path reinforcement, not state expansion.

## 7. Time as Emergent Quantity

Experienced time correlates with accumulated traversal cost:

```text
T_experienced ≈ Σ C[γ_i]
```

Predictions:

- Time compression in low-cost traversal regimes.
- Time dilation under high-cost or constrained traversal.

Time is therefore treated as a derived measure, not as the deepest primitive.

## 8. Formal Mapping to Existing MKUFT Claims

### 8.1 Learning and Skill Acquisition

- Nodes: stable skill states.
- Trajectories: learning paths.
- λ(x): effort, error rate, energetic/cognitive cost.

Prediction: learning curves reflect decreasing traversal cost.

Falsification: learning introduces new stable states without cost reduction.

### 8.2 Boundary Effects and Anomalous Phenomena

- Nodes: stable regimes.
- Boundaries: near-forbidden adjacencies.
- λ(x): coherence stress.

Prediction: anomalies cluster near high-cost transitions.

Falsification: anomalies distribute randomly, independent of boundary or coherence conditions.

### 8.3 Time Compression and Dilation

- Trajectory complexity and accumulated coherence cost map to experienced duration.

Prediction: time perception correlates with traversal cost.

Falsification: time perception is independent of traversal complexity and coherence cost.

### 8.4 Measurement and Observation

- Nodes: pre-existing permissible outcomes.
- Measurement: routing constraint.

Prediction: measurement alters transition statistics, not state availability.

Falsification: observation demonstrably creates new permissible states.

### 8.5 Environmental and Geometric Correlations

- Geometry: adjacency grammar.
- Structures: stable subgraphs.
- Environment: modulation of λ(x).

Prediction: recurrent geometries correlate with reduced traversal cost.

Falsification: no correlation between structure and traversal efficiency.

## 9. Falsifiability Summary

MKUFT is constrained or falsified if:

- probability does not correlate with path density,
- learning does not correspond to cost reduction,
- anomalies do not cluster near high-cost or boundary conditions,
- observation creates new permissible states rather than routing among available states,
- time perception is independent of traversal cost,
- geometry shows no measurable relation to traversal stability or coherence.

## 10. Canon Status

This addendum supersedes earlier short or partial addenda while preserving the original MKUFT core as authoritative.
