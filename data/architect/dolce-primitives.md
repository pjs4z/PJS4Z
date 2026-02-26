# DOLCE Primitives — Reference Library

**Descriptive Ontology for Linguistic and Cognitive Engineering**
*Foundational ontology developed by the Laboratory for Applied Ontology (LOA), ISTC-CNR, Trento*

DOLCE is a foundational (upper-level) ontology designed to capture the ontological categories underlying natural language and human commonsense. It is *descriptive* rather than prescriptive — it aims to model how people conceptualize reality, not reality "as it is." DOLCE is multiplicative (overlapping entities can co-exist in the same spatiotemporal location) and adopts a quality-based approach to properties.

Primary references: Masolo et al., *WonderWeb Deliverable D18* (2003); Gangemi et al., "Sweetening Ontologies with DOLCE" (2002).

---

## 1. Category Taxonomy

DOLCE's top-level category is **Particular** (PT) — every entity in the ontology is a particular. Universals are not first-class citizens; the ontology quantifies only over individuals.

### Hierarchy Diagram

```
Particular (PT)
├── Endurant (ED)
│   ├── Physical Endurant (PED)
│   │   ├── Amount of Matter (M)
│   │   ├── Feature (F)
│   │   └── Physical Object (POB)
│   └── Non-Physical Endurant (NPED)
│       ├── Mental Object (MOB)
│       └── Social Object (SOB)
│           ├── Agentive Social Object (ASO)
│           └── Non-Agentive Social Object (NASO)
│
├── Perdurant (PD)
│   ├── Event (EV)
│   │   ├── Achievement (ACH)
│   │   └── Accomplishment (ACC)
│   └── Stative (STV)
│       ├── State (ST)
│       └── Process (PRO)
│
├── Quality (Q)
│   ├── Temporal Quality (TQ)
│   │   └── Temporal Location (TL)
│   └── Physical Quality (PQ)
│       └── Spatial Location (SL)
│
└── Abstract (AB)
    ├── Region (R)
    │   ├── Temporal Region (TR)
    │   │   └── Time Interval (T)
    │   ├── Physical Region (PR)
    │   │   └── Space Region (S)
    │   └── Abstract Region (AR)
    └── Set
```

### Taxonomy Notes

- The four top branches — Endurant, Perdurant, Quality, Abstract — are **pairwise disjoint**.
- Leaf categories at the same level are also disjoint (e.g., Amount of Matter, Feature, and Physical Object share no instances).
- DOLCE-Lite and extensions (e.g., DnS, DOLCE+DnS Ultralite / DUL) may introduce additional categories such as Description, Situation, Role, and Collection.

---

## 2. Category Definitions

### 2.1 Endurant (ED)

Entities that are **wholly present** at every time at which they exist. An endurant has no temporal parts — it persists through time by being entirely present at each moment.

**Criterion:** If *x* is an endurant, then for any two times *t₁* and *t₂* at which *x* exists, *x* at *t₁* and *x* at *t₂* are the same whole entity (not temporal slices).

#### Physical Endurant (PED)

Endurants that possess a direct spatial quality — they have spatial location and physical extension.

| Subcategory | Definition | Examples |
|---|---|---|
| **Amount of Matter (M)** | A maximally self-connected physical endurant individuated by the stuff it is made of. Homeomerous: every part of an amount of matter is itself an amount of the same kind of matter. | A lump of gold, a volume of water, a portion of sand |
| **Feature (F)** | A physical endurant existentially dependent on another physical endurant whose spatial location is a proper part of its host's spatial location. Not independently identifiable. | A hole in a piece of cheese, a surface of a table, a boundary, a scratch on a door |
| **Physical Object (POB)** | A physical endurant with unity — it has a unifying principle that distinguishes it from arbitrary aggregates. Typically non-homeomerous. | A cat, a chair, a planet, a cell |

#### Non-Physical Endurant (NPED)

Endurants that lack direct spatial qualities. They exist in time but not in space (at least not intrinsically).

| Subcategory | Definition | Examples |
|---|---|---|
| **Mental Object (MOB)** | A non-physical endurant existentially dependent on a cognitive agent. Private to its bearer. | A belief, a desire, a percept, a mental image |
| **Social Object (SOB)** | A non-physical endurant dependent on a community of agents. Public / intersubjective. | — |
| — **Agentive Social Object (ASO)** | Social objects created by intentional collective acts. | A law, a corporation, a contract, a musical composition (qua work) |
| — **Non-Agentive Social Object (NASO)** | Social objects that emerge from social practice without deliberate creation. | A language, a custom, an economic recession |

---

### 2.2 Perdurant (PD)

Entities that **unfold in time** — they have temporal parts. A perdurant at any given moment is only partially present (one is experiencing a temporal slice of it).

**Criterion:** If *x* is a perdurant and *t* is a proper subinterval of *x*'s temporal span, then *x* restricted to *t* is a proper temporal part of *x*.

DOLCE classifies perdurants along an Aristotelian/Vendlerian aspect axis:

| | **+Cumulative** (homogeneous) | **−Cumulative** (non-homogeneous) |
|---|---|---|
| **+Atomic** (has a culmination) | — | **Achievement (ACH)**: instantaneous change of state |
| **−Atomic** (no natural culmination boundary) | **Process (PRO)**: homogeneous activity | **Accomplishment (ACC)**: directed change toward a result |
| **(neutral)** | **State (ST)**: static situation | — |

#### Event (EV)

Perdurants that are non-homogeneous — they involve change and are not cumulative (the sum of two events of the same type is not necessarily an event of that type).

| Subcategory | Definition | Examples |
|---|---|---|
| **Achievement (ACH)** | An atomic (instantaneous or point-like) event representing a change of state. Non-decomposable into subevents. | Reaching the summit, the light switching on, recognizing a face |
| **Accomplishment (ACC)** | A non-atomic event with an inherent culmination — it proceeds through phases toward a result. | Building a house, running a marathon, writing a thesis |

#### Stative (STV)

Perdurants that are **cumulative/homogeneous** — any temporal part of a stative of type *S* is also of type *S*.

| Subcategory | Definition | Examples |
|---|---|---|
| **State (ST)** | A homeomerous stative with no internal variation. | Being seated, being red, being alive |
| **Process (PRO)** | A homeomerous stative that involves activity but no directed change. | Running (as ongoing activity), raining, breathing |

---

### 2.3 Quality (Q)

Individual properties that **inhere** in entities. A quality is not a universal (like "redness") but a particular instance of a property (like *the specific color of this apple*). Qualities are the basic mechanism through which DOLCE handles attribution.

Qualities are existentially dependent on their bearer — they cannot exist independently.

| Subcategory | Definition | Examples |
|---|---|---|
| **Temporal Quality (TQ)** | Qualities relating to temporal aspects of an entity's existence. | The temporal duration of a concert |
| — **Temporal Location (TL)** | The specific temporal quality that locates an entity in time. | The time-position of a meeting |
| **Physical Quality (PQ)** | Qualities relating to physical/spatial aspects. | The color of this rose, the mass of this stone, the shape of this bottle |
| — **Spatial Location (SL)** | The specific physical quality that locates an entity in space. | The spatial position of a chair |

**Key mechanism:** Every quality has a **quale** (plural: *qualia*) — the value it takes at a given time, drawn from a quality space (region). For example, the color quality of a leaf may have a quale in the green region of color space in summer and in the yellow region in autumn.

---

### 2.4 Abstract (AB)

Entities that have **no spatial or temporal qualities** — they do not exist in space or time. Abstracts serve as the value spaces for qualities and as formal structures.

#### Region (R)

The structured spaces in which qualia live. Regions are the "positions" or "values" that qualities can take.

| Subcategory | Definition | Examples |
|---|---|---|
| **Temporal Region (TR)** | Regions of time. | — |
| — **Time Interval (T)** | A connected portion of the temporal axis. | The interval 9:00–10:00 on Jan 1, 2025 |
| **Physical Region (PR)** | Regions of physical quality spaces. | A color-space region, a mass-space value |
| — **Space Region (S)** | Regions of spatial quality space — geometric regions. | A spherical volume, a planar area |
| **Abstract Region (AR)** | Regions of non-physical quality spaces. | A price range, a utility interval |

#### Set

The category for mathematical/extensional collections, included for formal completeness.

---

## 3. Fundamental Relations

DOLCE's relational primitives connect entities across categories. Many relations are **time-indexed** to support change.

### 3.1 Parthood

Mereological relations form the backbone of DOLCE's structure. DOLCE distinguishes several parthood variants because different categories have different part–whole behavior.

#### Temporary Parthood — P(x, y, t)

> *x* is part of *y* at time *t*.

This is the most general parthood relation in DOLCE, allowing parts to change over time. It applies to endurants.

- Reflexive: P(x, x, t) for every t at which x is present
- Antisymmetric: if P(x, y, t) and P(y, x, t) then x = y
- Transitive: if P(x, y, t) and P(y, z, t) then P(x, z, t)

**Example:** The heart is part of the body at time *t*, but could be separated later during surgery.

#### Constant Parthood

A derived relation: *x* is a **constant part** of *y* iff *x* is part of *y* at every time at which *y* exists.

#### Temporal Parthood — P_t(x, y)

Temporal parthood applies to perdurants: *x* is a temporal part of perdurant *y* if *x* is a subinterval-restricted "slice" of *y*.

#### Overlap — O(x, y, t)

> *x* and *y* overlap at time *t* iff they share a common part at *t*.

O(x, y, t) ≡ ∃z [P(z, x, t) ∧ P(z, y, t)]

---

### 3.2 Constitution — K(x, y, t)

> *x* constitutes *y* at time *t*.

Constitution captures the relationship between a thing and the matter or stuff it is made of, without reducing one to the other (anti-reductionism).

**Properties:**
- Asymmetric: if K(x, y, t) then ¬K(y, x, t)
- Not transitive in general
- The constituted entity (*y*) and its constituent (*x*) share spatial location at *t* but may differ in modal properties, persistence conditions, and identity criteria

**Example:** A lump of bronze (Amount of Matter) constitutes a statue (Physical Object) at time *t*. The lump can survive melting and recasting; the statue cannot.

---

### 3.3 Participation — PC(x, y, t)

> Endurant *x* participates in perdurant *y* at time *t*.

Participation is the fundamental cross-category bridge connecting endurants and perdurants.

**Axiom:** Every perdurant must have at least one endurant participant at every time in its temporal span.

∀y [PD(y) → ∀t [being-present-at(y, t) → ∃x [ED(x) ∧ PC(x, y, t)]]]

**Axiom:** Every endurant must participate in at least one perdurant (the "life" of the endurant).

∀x [ED(x) → ∃y [PD(y) ∧ ∀t [being-present-at(x, t) → PC(x, y, t)]]]

**Example:** A potter (POB) participates in a sculpting event (ACC) at time *t*.

---

### 3.4 Dependence

Dependence relations formalize the idea that some entities cannot exist without others. DOLCE distinguishes two orthogonal axes: **specific vs. generic** and **constant vs. temporary**.

#### Specific Dependence — SD(x, y)

> *x* specifically depends on *y* iff *x* necessarily requires *that very individual y* to exist.

∀t [being-present-at(x, t) → being-present-at(y, t)]

**Example:** A particular smile specifically depends on the face it is a feature of.

#### Generic Dependence — GD(x, C)

> *x* generically depends on category *C* iff *x* necessarily requires *some* instance of *C* to exist, but not any particular one.

∀t [being-present-at(x, t) → ∃y [C(y) ∧ being-present-at(y, t)]]

**Example:** A person generically depends on the category Heart — a person needs *a* heart but not any specific heart (a transplant is possible).

#### Constant vs. Temporary Dependence

- **Constant dependence:** Holds at every time at which the dependent exists.
- **Temporary dependence:** Holds at some time(s) but not necessarily all.

#### Mutual Dependence

Two entities are **mutually dependent** iff each specifically depends on the other. Often found between qualities and their bearers in the same ontological "bundle."

---

### 3.5 Inherence — qt(x, y)

> Quality *x* inheres in entity *y*.

Inherence is a specific dependence that ties a quality to its bearer. Every quality has exactly one bearer, and every endurant and perdurant has at least one quality.

**Axiom:**
∀x [Q(x) → ∃!y [qt(x, y)]]

(Every quality inheres in exactly one entity.)

**Example:** The weight-quality of this book inheres in this book.

---

### 3.6 Quale — ql(x, y, t)

> *y* is the quale of quality *x* at time *t*.

The quale maps a quality to its current "value" in the appropriate region (quality space). This is how DOLCE represents change in properties: the quality persists, but its quale may shift across regions over time.

**Axiom:** At each time, a quality has exactly one quale.

∀x [Q(x) → ∀t [being-present-at(x, t) → ∃!y [R(y) ∧ ql(x, y, t)]]]

**Example:** The color-quality of a leaf has quale *green-region* in June and quale *yellow-region* in October.

---

### 3.7 Being-Present-At — PRE(x, t)

> Entity *x* is present at time *t*.

This is the basic temporal location relation. It does not imply that *x* is *wholly* present at *t* — for perdurants, only a temporal part may be present. For endurants, being-present means the whole entity is present.

---

### 3.8 Spatial Relations

DOLCE inherits spatial relations through spatial qualities and their qualia. Key derived relations:

| Relation | Meaning |
|---|---|
| **Exact spatial location** | *x*'s spatial quale at *t* equals region *r* |
| **Spatial inclusion** | *x*'s spatial location is part of *y*'s spatial location at *t* |
| **Co-location** | *x* and *y* share the same spatial location at *t* (enabled by DOLCE's multiplicativity) |

Co-location is essential for constitution: the statue and the bronze are co-located but remain distinct individuals.

---

## 4. Cross-Cutting Constraints

Several global axioms govern how categories and relations interact:

| Constraint | Statement |
|---|---|
| **Quality exclusivity** | Qualities inhere in exactly one entity; they cannot "jump" bearers. |
| **Perdurant participation** | Every perdurant has at least one endurant participant at every moment of its existence. |
| **Endurant grounding** | Every endurant participates in some perdurant (its "life"). |
| **Region uniqueness** | At any time, a quality maps to exactly one quale (region value). |
| **Category disjointness** | Endurant, Perdurant, Quality, and Abstract are pairwise disjoint — no entity belongs to more than one top-level branch. |
| **Physical/Non-Physical disjointness** | PED and NPED are disjoint; an endurant is either physical or non-physical, not both. |
| **Constitution asymmetry** | If *x* constitutes *y*, then *y* does not constitute *x*. |

---

## 5. Quick Reference Table

### Categories at a Glance

| Code | Category | Branch | Key Trait |
|---|---|---|---|
| PT | Particular | — | Top-level; all entities |
| ED | Endurant | Endurant | Wholly present in time |
| PED | Physical Endurant | Endurant | Has spatial qualities |
| M | Amount of Matter | Endurant | Individuated by stuff |
| F | Feature | Endurant | Dependent on host PED |
| POB | Physical Object | Endurant | Has unity |
| NPED | Non-Physical Endurant | Endurant | No spatial qualities |
| MOB | Mental Object | Endurant | Private; agent-dependent |
| SOB | Social Object | Endurant | Intersubjective |
| ASO | Agentive Social Object | Endurant | Intentionally created |
| NASO | Non-Agentive Social Object | Endurant | Emergent from practice |
| PD | Perdurant | Perdurant | Has temporal parts |
| EV | Event | Perdurant | Non-cumulative |
| ACH | Achievement | Perdurant | Atomic change of state |
| ACC | Accomplishment | Perdurant | Directed process with culmination |
| STV | Stative | Perdurant | Cumulative / homogeneous |
| ST | State | Perdurant | No internal variation |
| PRO | Process | Perdurant | Ongoing activity |
| Q | Quality | Quality | Individual property instance |
| TQ | Temporal Quality | Quality | Temporal aspects |
| TL | Temporal Location | Quality | Position in time |
| PQ | Physical Quality | Quality | Physical aspects |
| SL | Spatial Location | Quality | Position in space |
| AB | Abstract | Abstract | Outside spacetime |
| R | Region | Abstract | Quality value space |
| TR | Temporal Region | Abstract | Time regions |
| T | Time Interval | Abstract | Connected time portion |
| PR | Physical Region | Abstract | Physical quality space |
| S | Space Region | Abstract | Geometric region |
| AR | Abstract Region | Abstract | Non-physical quality space |

### Relations at a Glance

| Symbol | Relation | Arity | Connects |
|---|---|---|---|
| P(x,y,t) | Temporary Parthood | 3 | ED × ED × T |
| P_t(x,y) | Temporal Parthood | 2 | PD × PD |
| O(x,y,t) | Overlap | 3 | ED × ED × T |
| K(x,y,t) | Constitution | 3 | ED × ED × T |
| PC(x,y,t) | Participation | 3 | ED × PD × T |
| SD(x,y) | Specific Dependence | 2 | PT × PT |
| GD(x,C) | Generic Dependence | 2 | PT × Category |
| qt(x,y) | Inherence | 2 | Q × (ED ∪ PD) |
| ql(x,y,t) | Quale | 3 | Q × R × T |
| PRE(x,t) | Being-Present-At | 2 | PT × T |

---

*Compiled from Masolo et al. (2003), Gangemi et al. (2002), and Borgo & Masolo (2009). For extensions (Descriptions & Situations, DUL, DOLCE+DnS Ultralite), see the respective publications from LOA/ISTC-CNR.*
