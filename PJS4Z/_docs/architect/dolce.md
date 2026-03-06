WonderWeb Deliverable D18

Ontology Library (ﬁnal)

Claudio Masolo, Stefano Borgo, Aldo Gangemi, Nicola Guarino, Alessandro Oltramari∗

∗Part of this work has been done in cooperation with partners inside and outside the WonderWeb project. In particular Sections 5, 6, and 10 has been done in collaboration with Luc Schneider of the Department of Philosophy of the University of Geneva; Sections 7 and 8 in collaboration with Pierre Grenon of the IFOMIS institute of Leipzig; and Section in collaboration with Peter Mika, Marta Sabou of the Vrije Universiteit of Amsterdam, and Daniel Oberle of the Institute AIFB of the University of Karlsruhe.

Laboratory For Applied Ontology - ISTC-CNR Via Solteri, 38 38100 Trento Italy email: borgo@loa-cnr.it

Identiﬁer Del 18

Class Deliverable

Version 1.0

Date 31-12-2003

Status Final

Distribution Public

Lead Partner ISTC-CNR

WonderWeb Project

This document forms part of a research project funded by the IST Programme of the Commission of the European Communities as project number IST-2001-33052.

For further information about WonderWeb, please contact the project co-ordinator:

Ian Horrocks The Victoria University of Manchester Department of Computer Science Kilburn Building Oxford Road Manchester M13 9PL Tel: +44 161 275 6154 Fax: +44 161 275 6236 Email: wonderweb-info@lists.man.ac.uk

ii

Contents

Administrative Details 1

1 Introduction 2 1.1 The Role of Foundational Ontologies . . . . . . . . . . . . . . . . . . . . 2 1.2 The WonderWeb Foundational Ontologies Library . . . . . . . . . . . . . 3 1.2.1 Philosophy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 1.2.2 Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 1.2.3 Development Approach . . . . . . . . . . . . . . . . . . . . . . 5

2 Design Options and Ontological Choices 7 2.1 Universals, Particulars and Individual Properties . . . . . . . . . . . . . . 9 2.2 Abstract and Concrete Entities . . . . . . . . . . . . . . . . . . . . . . . 10 2.3 3D vs. 4D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 2.4 Endurants and Perdurants . . . . . . . . . . . . . . . . . . . . . . . . . . 11 2.5 Co-localized entities . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

3 DOLCE: a Descriptive Ontology for Linguistic and Cognitive Engineering 13 3.1 Basic assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 3.2 Basic categories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 3.2.1 Endurants and Perdurants . . . . . . . . . . . . . . . . . . . . . 15 3.2.2 Qualities and quality regions . . . . . . . . . . . . . . . . . . . . 16 3.2.3 Abstract entities . . . . . . . . . . . . . . . . . . . . . . . . . . 19 3.3 Basic relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 3.3.1 Parthood and Temporary Parthood . . . . . . . . . . . . . . . . . 19 3.3.2 Dependence and Spatial Dependence . . . . . . . . . . . . . . . 20 3.3.3 Constitution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 3.3.4 Participation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 3.3.5 Quality inherence and quality value . . . . . . . . . . . . . . . . 22 3.4 Further distinctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 3.4.1 Physical and non-physical endurants . . . . . . . . . . . . . . . . 22 3.4.2 Non-physical endurants and the agentive/non-agentive distinction 23 3.4.3 Kinds of perdurants . . . . . . . . . . . . . . . . . . . . . . . . . 24 3.4.4 Kinds of quality . . . . . . . . . . . . . . . . . . . . . . . . . . 25

4 DOLCE’s Formal Characterization 26 4.1 Notation and introductory notes . . . . . . . . . . . . . . . . . . . . . . 26 4.2 Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 4.2.1 Mereological Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . 27 4.2.2 Quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 4.2.3 Temporal and Spatial Quale . . . . . . . . . . . . . . . . . . . . 28 4.2.4 Being present . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.2.5 Inclusion and Coincidence . . . . . . . . . . . . . . . . . . . . . 29 4.2.6 Perdurant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 4.2.7 Participation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

iii

4.2.8 Dependence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 4.2.9 Spatial Dependence . . . . . . . . . . . . . . . . . . . . . . . . . 31 4.2.10 Constitution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 4.3 Characterization of primitive relations . . . . . . . . . . . . . . . . . . . 33 4.3.1 Parthood . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 4.3.2 Temporary Parthood . . . . . . . . . . . . . . . . . . . . . . . . 33 4.3.3 Constitution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 4.3.4 Participation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 4.3.5 Quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 4.3.6 Quale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 4.3.7 Dependence and Spatial Dependence . . . . . . . . . . . . . . . 37 4.3.8 Being Present . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 4.4 Characterization of Categories . . . . . . . . . . . . . . . . . . . . . . . 38 4.4.1 Region . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 4.4.2 Quality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 4.4.3 Perdurant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 4.4.4 Endurant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39 4.5 Glossary of Basic Categories . . . . . . . . . . . . . . . . . . . . . . . . 41

5 OCHRE: the Object-Centered High-level Reference Ontology 42 5.1 Basic Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 5.2 Basic Categories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 5.2.1 Tropes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 5.2.2 Thin and Thick Objects . . . . . . . . . . . . . . . . . . . . . . . 44 5.2.3 Haecceities, Properties, Guises and Relations . . . . . . . . . . . 45 5.2.4 Eventualities . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 5.3 Basic Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 5.3.1 Parthood . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 5.3.2 Foundation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47 5.3.3 Similarity, Exact Similarity, Comparability . . . . . . . . . . . . 47 5.3.4 Connection and Anteriority . . . . . . . . . . . . . . . . . . . . . 47 5.3.5 Relational Precedence . . . . . . . . . . . . . . . . . . . . . . . 48 5.4 Derived Relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 5.4.1 Direct Parthood . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 5.4.2 Succession . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 5.4.3 Participation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

6 OCHRE’s Formal Characterization 51 6.1 Mereology - Theory of Parts and Wholes . . . . . . . . . . . . . . . . . . 51 6.1.1 Deﬁnitions of Mereology . . . . . . . . . . . . . . . . . . . . . . 51 6.1.2 Axioms of Mereology . . . . . . . . . . . . . . . . . . . . . . . 51 6.2 Theory of Foundations . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 6.2.1 Deﬁnitions of the Theory of Foundations . . . . . . . . . . . . . 51 6.2.2 Axioms of the Theory of Foundations . . . . . . . . . . . . . . . 52

iv

6.3 Theory of Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52 6.3.1 Deﬁnitions of the Theory of Similarity . . . . . . . . . . . . . . . 52 6.3.2 Axioms of the Theory of Similarity . . . . . . . . . . . . . . . . 52 6.4 Topology - Theory of Space and Time . . . . . . . . . . . . . . . . . . . 53 6.4.1 Deﬁnitions of Topology . . . . . . . . . . . . . . . . . . . . . . 53 6.4.2 Axioms of Topology . . . . . . . . . . . . . . . . . . . . . . . . 53 6.5 Theory of Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53 6.5.1 Deﬁnitions of the Theory of Properties . . . . . . . . . . . . . . 53 6.5.2 Axioms of the Theory of Properties . . . . . . . . . . . . . . . . 54 6.5.3 Theorems of the Theory of Properties . . . . . . . . . . . . . . . 54 6.6 Theory of Eventualities . . . . . . . . . . . . . . . . . . . . . . . . . . . 54 6.6.1 Deﬁnitions of the Theory of Eventualities . . . . . . . . . . . . . 54 6.6.2 Axioms of the Theory of Eventualities . . . . . . . . . . . . . . . 54 6.7 Theory of Relational Properties . . . . . . . . . . . . . . . . . . . . . . . 54 6.7.1 Deﬁnitions of the Theory of Relational Properties . . . . . . . . . 54 6.7.2 Axioms of the Theory of Relational Properties . . . . . . . . . . 55

7 BFO: Basic Formal Ontology 56 7.1 Introduction and preliminaries . . . . . . . . . . . . . . . . . . . . . . . 56 7.1.1 Universals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56 7.1.2 Temporality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56 7.1.3 Granularity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 7.2 BFO in a nutshell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 7.2.1 Snap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 7.2.2 Span . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 7.2.3 Snap–Span and Span–Snap . . . . . . . . . . . . . . . . . . . . 59

8 Formal Characterization of BFO 61 8.1 Span Entities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61 8.1.1 Parthood . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 8.1.2 Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 8.1.3 Dependence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64 8.1.4 Time and Space-time . . . . . . . . . . . . . . . . . . . . . . . . 65 8.1.5 Temporal Location . . . . . . . . . . . . . . . . . . . . . . . . . 65 8.1.6 Spatio-Temporal Location . . . . . . . . . . . . . . . . . . . . . 66 8.2 Snap Entities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 8.2.1 Instantaneous Existence . . . . . . . . . . . . . . . . . . . . . . 68 8.2.2 Instantaneous Parthood . . . . . . . . . . . . . . . . . . . . . . . 68 8.2.3 Instantaneous Topology . . . . . . . . . . . . . . . . . . . . . . 69 8.2.4 Instantaneous Dependence . . . . . . . . . . . . . . . . . . . . . 70 8.2.5 Instantaneous Inherence . . . . . . . . . . . . . . . . . . . . . . 71 8.2.6 Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71 8.2.7 Instantaneous Spatial Location . . . . . . . . . . . . . . . . . . . 72 8.3 Relations between Snap and Span entities . . . . . . . . . . . . . . . . . 72

v

9 Comparing the Basic Modules: A Case Study 74 9.1 The statue and the clay in DOLCE . . . . . . . . . . . . . . . . . . . . . . 74 9.2 The statue and the clay in OCHRE . . . . . . . . . . . . . . . . . . . . . 74 9.3 The statue and the clay in BFO . . . . . . . . . . . . . . . . . . . . . . . 77

10 Comparing the Basic Modules: Formal Links 79

11 The Link with Natural Language 87 11.1 Mapping WORDNET into DOLCE . . . . . . . . . . . . . . . . . . . . . 87 11.1.1 Endurants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 11.1.2 Perdurants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 11.1.3 Qualities and Abstracts . . . . . . . . . . . . . . . . . . . . . . . 88

12 A core Ontology of Services 92 12.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92 12.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93 12.3 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94 12.4 Descriptions as entities . . . . . . . . . . . . . . . . . . . . . . . . . . . 95 12.4.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95 12.4.2 An Ontology of Descriptions and Situations . . . . . . . . . . . . 96 12.4.3 Implementing the Ontology of Descriptions in DOLCE . . . . . . 97 12.5 The Core Ontology of Services . . . . . . . . . . . . . . . . . . . . . . . 99 12.5.1 The Service Offering Description . . . . . . . . . . . . . . . . . 100 12.5.2 Service Situations . . . . . . . . . . . . . . . . . . . . . . . . . 103 12.5.3 Axiomatization . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 12.6 Deﬁning web services: On the border of Infolandia . . . . . . . . . . . . 106 12.7 Alignment of the Web Services Architecture . . . . . . . . . . . . . . . . 109 12.8 Alignment of DAML-S . . . . . . . . . . . . . . . . . . . . . . . . . . . 111 12.8.1 Illustrated example . . . . . . . . . . . . . . . . . . . . . . . . . 112 12.9 Alignment of the Application Server’s ontology . . . . . . . . . . . . . . 115 12.9.1 Original Ontology . . . . . . . . . . . . . . . . . . . . . . . . . 115 12.9.2 Aligning the taxonomy . . . . . . . . . . . . . . . . . . . . . . . 116 12.9.3 API Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . 117 12.9.4 IDL Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . 119 12.9.5 Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

13 APPENDIX A: KIF version of DOLCE 129

14 APPENDIX B: KIF version of OCHRE 165

15 APPENDIX C: DOLCE-Lite-Plus 178

16 APPENDIX D: WORDNET-DOLCE alignment 247

vi

Administrative Details

Part of this work has been done in cooperation with partners inside and outside the WON-

DERWEB project. In particular Sections 5, 6, and 10 has been done in collaboration with Luc Schneider of the Department of Philosophy of the University of Geneva; Sections 7 and 8 in collaboration with Pierre Grenon of the IFOMIS institute of Leipzig; and Section in collaboration with Peter Mika, Marta Sabou of the Vrije Universiteit of Amsterdam, and Daniel Oberle of the Institute AIFB of the University of Karlsruhe.

1

1 Introduction

1.1 The Role of Foundational Ontologies

Ontologies are the basic infrastructure for the Semantic Web. Everybody agrees on this, as the very idea of the Semantic Web hinges on the possibility to use shared vocabular- ies for describing resource content and capabilities, whose semantics is described in a (reasonably) unambiguous and machine-processable form. Describing this semantics, i.e. what is sometimes called the intended meaning of vocabulary terms, is exactly the job ontologies do for the Semantic Web. But what kinds of ontologies do we need? This is still an open issue. In most practical applications, ontologies appear as simple taxonomic structures of primitive or composite terms together with associated deﬁnitions. These are the so-called lightweight ontologies, used to represent semantic relationships among terms in order to facilitate content-based access to the (Web) data produced by a given community. In this case, the intended meaning of primitive terms is more or less known in advance by the members of such community. Hence, in this case, the role of ontologies is more that of supporting termino- logical services (inferences based on relationships among terms – usually just taxonomic relationships) rather than explaining or deﬁning their intended meaning. On the other hand, however, the need to establishing precise agreements as to the meaning of terms becomes crucial as soon as a community of users evolves, or multi- cultural and multilingual communities need to exchange data and services. As recently reported by the Harvard Business Review1, this problem may have been “one of the main reasons that so many online market makers have foundered. The transactions they had viewed as simple and routine actually involved many subtle distinctions in terminology and meaning”. To capture (or at least approximate) such subtle distinctions we need an explicit repre- sentation of the so-called ontological commitments about the meaning of terms, in order to remove terminological and conceptual ambiguities. A rigorous logical axiomatisation seems to be unavoidable in this case, as it accounts not only for the relationships between terms, but – most importantly – for the formal structure of the domain to be represented. This allows one to use axiomatic ontologies not only to facilitate meaning negotiation among agents, but also to clarify and model the negotiation process itself, and in general the structure of interaction. We should immediately note that building axiomatic ontologies for these purposes may be extremely hard, both conceptually and computationally. However, this job only needs to be undertaken once, before the interaction process starts. The quality of meaning negotiation may drastically affect the trust in a service offered by the Semantic Web, but not the computational performance of the service itself. Thus, for example, a product procurement process involving multiple agents with distributed lightweight ontologies may be carried out in an efﬁcient way by using simple terminological services, but the risk of semantic mismatch can be minimized only if the agents rely on explicit, axiomatised ontologies, which serve to ensure mutual compatibility of the respective models in such a way as to check the extent of real agreement.

1October 2001.

2

Axiomatic ontologies come in different forms and can have different levels of gener- ality, but a special relevance is enjoyed by the so-called foundational ontologies, which address very general domains. One of the goals of the WONDERWEB project is the devel- opment of a library of such foundational ontologies, systematically related to each other in a way that makes the rationales and alternatives underlying different ontological choices as explicit as possible. Hopefully, this library will allow different Semantic Web applica- tions to commit to foundational ontologies according to their own needs and preferences, relying on the chosen modules (and their relationships with the rest of the library) for making explicit the underlying ontological assumptions and their formal consequences. Foundational ontologies are ultimately devoted to facilitate mutual understanding and inter-operability among people and machines. This includes understanding the reasons for non-interoperability, which may in some cases be much more important than imple- menting an integrated (but unpredictable and conceptually imperfect) system relying on a generic shared “semantics”. In conclusion, we see the role and nature of foundational ontologies (and axiomatic ontologies in general) as complementary to that of lightweight ontologies: the latter can be built semi-automatically, e.g. by exploiting machine learning techniques; the former require more painful human labour, which can gain immense ben- eﬁt from the results and methodologies of disciplines such as philosophy, linguistics, and cognitive science.

1.2 The WonderWeb Foundational Ontologies Library

Having motivated the role of foundational ontologies, let us describe the library we have developed within the WONDERWEB project: its philosophy, its structure, and its devel- opment approach.

1.2.1 Philosophy

We strongly believe it’s important to have a library of foundational ontologies, reﬂecting different commitments and purposes, rather than a single monolithic module. Indeed, we believe that the most important challenge for the Semantic Web is not so much the agree- ment on a monolithic set of ontological categories, but rather the careful isolation of the fundamental ontological options and their formal relationships. In our view, each mod- ule in this library should be described in terms of such fundamental options. Rationales and alternatives underlying the different ontological choices should be made as explicit as possible, in order to form a network of different but systematically related modules which the various Semantic Web applications can commit to, according to their ontological as- sumptions. In short, the main goals of the WONDERWEB Foundational Ontologies Library (WFOL, see Figure 1) are to serve as:

• a starting point for building new ontologies. One of the most important and critical questions when starting a new ontology is determining what things there are in the domain to be modeled. Adopting a high level view provides an enormous jump start in answering this question;

3

• a reference point for easy and rigorous comparisons among different ontological approaches;

• a common framework for analyzing, harmonizing and integrating existing ontolo- gies and metadata standards (by manually mapping existing categories into the cat- egories assumed by some module(s) in the library).

In addition, we intend the library to be:

• minimal – as opposed to other comprehensive ontology efforts, we intend the library to be as general as possible, including only the most reusable and widely applicable upper-level categories;

• rigorous – where possible, the ontologies in the libraries will be characterized by means of rich axiomatisations, and the formal consequences (theorems) of such characterizations will be explored in detail;

• extensively researched – each module in the library will be added only after careful evaluation by experts and consultation with canonical works. The basis for onto- logical choices will be documented and referenced.

1.2.2 Structure

The basic structure of our library is depicted in Figure 1. Modules are organized along two dimensions: vision, corresponding to the basic ontological choices made, and speciﬁcity, according to the level of generality. Note that the actual implementation of this library as a single software service is out of the scope of this project. However, this document can be seen as a high-level speciﬁcation for such implementation. In general, from the software engineering point of view, a foundational ontologies library can be seen as:

1. A collection of ontology modules, including:

• a collection of machine-readable ontologies (encoded e.g. as KIF ﬁles), cor- responding to the different ontology modules (see Appendix A, B for the KIF versions of DOLCE and OCHRE and Appendix C for an extended KIF version of DOLCE in order to introduce new concept indispensable for representing web services (see Section 12))2);

• an informal presentation of the basic ontological choices adopted for each module (Sections 3, 5, 7);

• a presentation of the logical axiomatisation adopted for each module, includ- ing a discussion on the motivations and consequences (i.e., theorems) of single axioms (Sections 4, 6, 8).

2. A speciﬁcation of differences and similarities existing among modules, including:

2The KIF version of the third module (BFO) is still not available.

4

Choose Vision

4D

3D

Top

Choose Subject

Bank

Formal Links Between Visions & Modules

Law

Single Vision Single Module

Figure 1: The WonderWeb Foundational Ontologies Library. The tree to the left describes a “roadmap” of ontological choices. Grey squares to the right correspond to ontologies (possibly) developed according to such choices. In turn, these are organized in modules according to domain speciﬁcity.

• an informal discussion on the differences between the ontological choices adopted;

• a logical speciﬁcation of the formal links (i.e., syntactic and semantic corre- spondences) existing between the various modules (in Section 10 the formal links between OCHRE and DOLCE are described in detail).

3. A mapping between ontology modules and natural language lexicons such as Word- Net (see Section 11 for the mapping between DOLCE and WORDNET and Appendix D for an implementation of these mappings in KIF).

1.2.3 Development Approach

Developing foundational ontologies is not simple at all. We decided to describe ﬁrst a core set of key ontological assumptions, focusing on the needs of other projects we were involved in, and reﬂecting our own choices and intuitions (see also the WONDERWEB Deliverable D15, that presents a ﬁrst “roadmap” of various ontological options and the general methodology adopted). This was the origin of DOLCE, whose acronym (Descrip- tive Ontology for Linguistic and Cognitive Engineering) reﬂects what we have called a cognitive bias. Since its ﬁrst development, DOLCE was not intended as a candidate for a “universal” standard ontology, but rather as a reference module, to be adopted as a start- ing point for comparing and elucidating the relationships with other future modules of the library. Indeed, the public availability of DOLCE - since its ﬁrst release - stimulated

5

other research groups working on formal ontology to make their own ontologies avail- able in the library as independent modules, although linked to DOLCE according to the WONDERWEB philosophy. It is important to remark that, to reach the objective of extending the library with exter- nal contributions, a substantial allocation of resources on both sides (the library developer and the interested contributors) was required, in order to understand the different choices, compare them, and harmonise the documentation. Given the available resources, we suc- ceeded in introducing two external modules besides DOLCE: OCHRE and BFO. The ﬁrst one is an ontology independently developed by Luc Schneider, currently at the Univer- sity of Geneve; the latter is being adopted by the IFOMIS research lab at the University of Leipzig for developing formal ontologies in the biomedical area. Further contacts for extending the library are in progress. A ﬁnal note concerns the logical language adopted for the various modules. The WONDERWEB project is committed to develop a layered language architecture for rep- resenting ontologies in the Semantic Web, based on existing standards such as RDF and

OWL. The latter is intended to be used as a language for representing and querying on- tologies on the Web, and has been carefully designed in order to offer the best possi- ble tradeoff between expressivity and computational efﬁciency, while guaranteeing at the same time important logical properties such as inferential completeness. The result is a layered logical language allowing for different degrees of expressivity, which is however much less expressive than ﬁrst-order logic. Using such a language for specifying foun- dational ontologies would be non-sensical: because of their very goals and nature, these ontologies need an expressive language, in order to suitably characterize their intended models. On the other hand, as we have noted above, their computational requirements are less stringent, since they only need to be accessed for meaning negotiation, not for terminological services where the intended meaning of terms is already agreed upon. The strategy we have devised to solve this expressivity problem is the following:

1. Describe a foundational ontology on paper, using a full ﬁrst-order logic with modal- ity;

2. Isolate the part of the axiomatization that can be expressed in OWL, and implement it;

3. Add the remaining part in the form of KIF3 comments attached to OWL concepts.

3Indeed, we are considering the new language CL (cl.tamu.edu), which is an extension of KIF.

6

2 Design Options and Ontological Choices

Before addressing speciﬁc issues about domain of discourse, basic categories, and their relations4, it may be important to clarify the general attitude towards ontological analysis, or – in other words – the motivations and the constraints that drive our conceptualization of reality. It comes to no surprise that the design options for building foundational ontolo- gies reﬂect the main categorical distinctions discussed in philosophy. However, among all the philosophical stands and distinctions, foundational ontologists seem particularly interested in two general attitudes: a) descriptive vs. revisionary, and b) multiplicative vs. reductionist.

(a) A descriptive ontology aims at capturing the ontological stands that shape natural lan- guage and human cognition. It is based on the assumption that the surface structure of natural language and the so-called commonsense have ontological relevance. As a conse- quence, the categories refer to cognitive artifacts more or less depending on human per- ception, cultural imprints and social conventions. Under this approach, there are no major restrictions on the postulation of ontological categories because overall philosophical or scientiﬁc paradigms are neglected. This attitude stands in contrast to the revisionary ap- proach. The revisionist considers linguistic and cognitive issues at the level of secondary sources (if considered at all), and does not hesitate to paraphrase linguistic expressions (or to re-interpret cognitive phenomena) when their ontological assumptions are not de- fensible on scientiﬁc grounds. The following example should make this contraposition clear. Commonsense distin- guishes between things (spatial objects like houses and computers) and events (temporal objects like bank transfers and computer repairs). In the wake of relativity theory, how- ever, time is viewed as another dimension of objects on a par with the traditional spatial dimensions. Considering the consequences of this scientiﬁc theory (or theories), some philosophers and computer scientists have come to believe that the commonsense dis- tinction between things that are and things that happen should be abandoned in favor of a uniﬁed viewpoint. According to these revisionist researchers, everything extends in space and time, and the distinction between things and events is an (ontologically irrel- evant) historical and cognitive accident. This example shows that a revisionary ontology is committed to capture the intrinsic nature of the world by providing structures that are independent from the conceptualizing agents. Classic examples of descriptive ontologies are [85] and [74].

(b) In designing ontologies, one has to model a considerable amount of concepts. These concepts form a wide taxonomy and are often intertwined in several ways. Since the complexity of the resulting system is quite high, there are considerable advantages in limiting the actual primitives to a small subset of the concepts. If this is possible, then many notions can be reconstructed in terms of the chosen primitives. A reductionist ontologist takes this view as a major guideline; he aims at describing a great number of ontological concepts with the smallest number of primitives. On the other hand, a multiplicative ontologist points at reaching a very expressive system without bothering

4See [34].

7

about the complexity of the ontology. Indeed, the aim is to provide a reliable account of reality despite of the large number of basic concepts needed. A clear example of this dichotomy is seen in the attitude towards co-localized enti- ties. A multiplicative ontology allows for different entities to be co-localized in the same space-time. These entities are assumed to be different because they have incompatible essential properties. This case is often presented through the problem of the vase and the clay it is made of. It seems natural to assume that the vase ceases to exist when a radi- cal change in shape occurs (for instance, when it breaks in peaces). Instead, the amount of clay is not altered by such events. According to the multiplicativist, these observa- tions show that there must be different (yet related) entities that are co-localized: the vase is constituted by an amount of clay, but it is not an amount of clay.5 Indeed, when a vase-master shapes a particular amount of clay, new properties are instantiated, and this justiﬁes the emergence of a new entity that we call a vase. This solution is opposed by the reductionists, which provide a different answer to this issue. They postulate that each space-time location contains at most one object. Incompatible essential properties (like those that distinguish the vase from the clay) are regarded as byproducts of the differ- ent viewpoints one can assume about spatio-temporal entities. The vase and the clay are surely different, reductionists claim, although not as entities but as views of the same spatio-temporal object.

Before concluding these general remarks on ontological analysis, we give the gist of another issue that highlights the (sometimes subtle) relationships between formalization and conceptualization. The problem of representing time and modality is an old and ever recurrent quandary in artiﬁcial intelligence. Basically, two approaches are possible: either one includes modal and temporal operators in the formal system from the very beginning, or reproduces modal reasoning into a ﬁrst-order language adding time and world (or situation) parameters to the predicates. In the ﬁrst case one can translate the expression “It is possible that John is ill” in a literal fashion. In the other approach, one has to rephrase the expression before translating it into the formalism. For instance, one can take the above expression to be equivalent to “There is a world in which John is ill”. This latter sentence can be translated literally. Although these options are generally well known to the practitioner, their conse- quences are sometimes not recognized. Bending for one or the other approach often deter- mines a preference in the dichotomies actualism/possibilism and presentism/eternalism. Actualism claims that only what is real exists, while possibilism admits possibilia (situ- ations or worlds) as well. Similarly, presentism assumes that only what is present exists, while for an eternalist the past, the present and the future are all existing. The decision to allow quantiﬁcation over instants or worlds is a decision faced by the possibilism and eternalism approaches. On the other side, actualism and presentism go hand in hand with the use of primitive modalities.

In the next paragraphs we present the most relevant options underlying the organiza- tion of an ontology. These are particularly important to clarify the commitments behind

5One of the purposes of the OntoClean methodology [47] is to help the user evaluating ontological choices of this type.

8

foundational ontologies and their basic categories. The following section outlines the ontological modules of the library. In this part, we resume the main theoretical choices discussed so far and show the ontological positions taken by the three ontologies DOLCE6,

BFO7, and OCHRE8.

2.1 Universals, Particulars and Individual Properties

The ontological distinction between universals and particulars can be characterized by means of the primitive relation of instantiation: particulars are entities that cannot have instances; universals are entities that can have instances9. In linguistic, ‘proper nouns’ are normally considered to refer to particulars, while ‘common nouns’ to universals. For example, ‘Varenne’, the Italian racehorse, is an instance of ‘horse’, but it cannot be in- stantiated itself. This characterization of the concept of universal is still vague since it does not clarify whether sets, predicates, and abstracts should be included among the universals. Let us consider why these entities are problematic. Sets are extensional entities, i.e. fully determined by their extension, and the mem- bership relation inherits this property: an element is a member of a set if it is in the extension of that set. The relation of instantiation is more generic and usually taken to be non-extensional. For example, the universals ‘three-angled polygon’ and ‘three-sided polygon’ are considered to be different although they have exactly the same instances, that is, they isolate the same sets. Predicates are sometimes closed with respect to the logical connectives, i.e. if P and Q are predicates, also ‘P and Q’, ‘P or Q’, and ‘not P’ are predicates. This seems awkward for universals. For example, one would probably include table and pumpkin among the universals, but not predicates like ‘table or pumpkin’ or ‘not table’. Finally, if abstracts are entities non extended in space-time (see also the next section), then they can differ from universals in many aspects. After all, not all abstracts seem to be universals (like numbers or sets). Furthermore, sometimes universals are taken to be localized in space-time since they are associated to the spatio-temporal locations of their instances10. More radically, universals can be rejected as in the trope theory [9]. Tropes do not have instances, they are properties/qualities of speciﬁc material entities and depend ontologically on them. In trope theory, it is possible to speak of the ‘whiteness’ of this speciﬁc piece of paper, while the universal ‘white’ does not exist. Note that tropes are often taken to be localized in the space-time of (the surface of) the material entities they depend on, that is, they cannot be considered as abstracts in the usual way. Related to this arguments, two further options have to be highlighted: objects can be seen as

6http://www.loa-cnr.it/DOLCE.html 7http://ontology.buffalo.edu/bfo/ 8http://www.ifomis.uni-leipzig.de/Research/pubs/forthcoming/ki2003epaper.pdf 9Properties and relations are usually considered as universals. 10In this case, the location of a universal is the sum of the locations of its instances and, according to this philosophical stand, every universal is ‘wholly present’ in each instance. This thesis is controversial. The difﬁculty of understanding how there can be a class of entities extended in space-time but not behaving like particulars, remains unsolved.

9

bearers (or substrates - using a well-known Aristotelian category) of their properties or as aggregations of their properties. In the ﬁrst case, objects are the result of a substratum (whatever this is claimed to be, i.e. rough matter) coming with peculiar qualities at a certain time; in the second, objects are individuated by different qualities considered in a certain spatial location at a certain time.

2.2 Abstract and Concrete Entities

We have mentioned that abstracts entities exist neither in space nor in time, i.e. they are not localized. On the other hand, concrete entities (or concretes) are deﬁned as entities that exist at least in time. Mathematical objects (like numbers and sets) are examples of abstracts, while ordinary objects (like cars, books, etc.) or events (like the 2000 Olympic Games) are examples of concrete entities. This characterization immediately raises a question: how is it possible that abstracts exist without existing at any time? Is it better to say that these are eternal and immutable, i.e., they exist at all times without chang- ing? From an ontological point of view the answer is not trivial, and perhaps a weaker characterization is preferable. An alternative deﬁnition is based on the ‘causal criterion’: abstracts possess no causal power while concretes do. This second deﬁnition, although similar to the ﬁrst, is quite different: if abstracts are ‘timeless’ entities, as in the ﬁrst deﬁnition, then they cannot be involved in causal relations; vice versa it is possible to in- dividuate entities localized in time and space (like ‘the centre of mass of the solar system’ see [60]) that lack any causal power. In what follows, we focus on the ﬁrst characteriza- tion of abstracts.11

2.3 3D vs. 4D

A fundamental ontological choice deals with the notion of change. What does it mean for an entity to change? This question raises the problem of variation in time and the related issue of the identity of the objects of experience. In general a 3D option claims that objects are: a) extended in a three-dimensional space; b) wholly present at each instant of their life; c) changing entities, in the sense that at different times they can instantiate different properties (indeed, one could say When I was out in the balcony my hands were colder than now). On the contrary a four- dimensional perspective states that objects are: a) space-time worms; b) only partially present at each instant; c) changing entities, in the sense that at different phases they can have different properties (My hands during the time spent out in the balcony, were colder than now). In the two following subsections we illustrate some speciﬁc arguments linked to this issue.

11The sense of abstractness introduced here is different from the one used in trope theory. Here concrete entities are ‘material’ (such as cars, tables, etc.), while tropes are properties or qualities of these entities (possibly with a spatio-temporal location).

10

2.4 Endurants and Perdurants

Classically, endurants (also called continuants) are characterized as entities that are ‘in time’, they are ‘wholly’ present (all their proper parts are present) at any time of their ex- istence. On the other hand, perdurants (also called occurrents) are entities that ‘happen in time’, they extend in time by accumulating different ‘temporal parts’, so that, at any time t at which they exist, only their temporal parts at t are present.12 For example, the book you are holding now can be considered an endurant because (now) it is wholly present, while “your reading of this book” is a perdurant because, your “reading” of the previous section is not present now. Note that it is possible to distinguish between ‘ordinary ob- jects’ (like the book) and ‘events or process’ (like ‘the reading of the book’) even when the domain contains perdurants only. In this latter case, one relies on properties that lie outside spatio-temporal aspects. Indeed, one can assume that four-dimensional entities do not need to have different spatio-temporal locations. A person and its life (both taken to be 4D entities) share the same space-time region but differ on other properties since, for instance, color, race, beliefs and the like make sense for person only. Endurants and perdurants can be characterized in a different way. Something is an endurant if (i) it exists at more than one moment and (ii) its parts can be determined only relatively to something else (for instance time)[49]. In other words, the distinction is based on the different nature of the parthood relation: endurants need a time-indexed parthood, while perdurants do not. Indeed, a statement like “this keyboard is part of my computer” is incomplete unless you specify a particular time, while “my youth is part of my life” does not require such a speciﬁcation.13

2.5 Co-localized entities

No matter what one decides about the ontological status of space and time, one has the option to include spatially and temporally co-located objects. It is quite natural to admit temporally co-localized objects (like you and the book you are reading) as well as spa- tially co-localized objects (somebody else can sit in the chair when I get up), while it is more problematic to justify the existence of spatio-temporally co-localized objects. Our natural language provides several compelling examples like a hole and the region of space it occupies, a statue and the clay it is made of, a person and its body. In other terms, in in- cluding (or excluding) spatio-temporally co-located objects, one answers major questions like: are there holes, or only holed objects? Are there statues or only statue-shaped stuff ? This subject is extremely complex and involves rather difﬁcult issues like identity through time, material constitution, essentiality, modality, etc. This is not the place for a detailed discussion of these issues. Nevertheless, we try to make explicit the positions of the ontologies in the library with respect to co-localization of entities. We distinguish be-

12Time-snapshots of perdurants (i.e., perdurants that are present only for an instant, and which lack proper temporal parts) are a limit case in this distinction. 13If the domain of quantiﬁcation contains both ‘objects’ and ‘events’, without reducing one kind of elements to the other, the participation relation, stating that objects participates in events, becomes funda- mental. For example, a person may participate in a discussion and a sword in a battle. This relation does not depend on the characterization of objects. It is crucial also in a four dimensionalist position where objects and events, although both 4D entities, are kept distinct.

11

tween entities that are spatially co-localized with ‘material entities’ –for example statues, persons, etc. – and entities that are dependent on ‘material entities’ although not spatially co-localized with them –for example holes, places, spots, shadows, etc. (see [13]) for a detailed treatment).

12

3 DOLCE: a Descriptive Ontology for Linguistic and Cog- nitive Engineering

3.1 Basic assumptions

The ﬁrst module of our foundational ontologies library is a Descriptive Ontology for Lin- guistic and Cognitive Engineering (DOLCE). According to the vision introduced above, we do not intend DOLCE as a candidate for a “universal” standard ontology. Rather, it is intended to act as starting point for comparing and elucidating the relationships with other future modules of the library, and also for clarifying the hidden assumptions underlying existing ontologies or linguistic resources such as WordNet. As reﬂected by its acronym, DOLCE has a clear cognitive bias, in the sense that it aims at capturing the ontological categories underlying natural language and human common- sense. We believe that such bias is very important for the Semantic Web (especially if we recognize its intrinsic social nature [15]). We do not commit to a strictly referentialist metaphysics related to the intrinsic nature of the world: rather, the categories we intro- duce here are thought of as cognitive artifacts ultimately depending on human perception, cultural imprints and social conventions (a sort of “cognitive” metaphysics). We draw in- spiration here from Searle’s notion of “deep background” [74], which represents the set of skills, tendencies and habits shared by humans because of their peculiar biological make up, and their evolved ability to interact with their ecological niches. The consequences of this approach are that our categories are at the so-called mesoscopic level [79], and they do not claim any special robustness against the state of the art in scientiﬁc knowledge: they are just descriptive notions that assist in making already formed conceptualizations explicit. They do not provide therefore a prescriptive (or “revisionary” [85]) framework to conceptualize entities. In other words, our categories describe entities in an ex post way, reﬂecting more or less the surface structures of language and cognition.

DOLCE is an ontology of particulars, in the sense that its domain of discourse is re- stricted to them. The fundamental ontological distinction between universals and partic- ulars can be informally understood by taking the relation of instantiation as a primitive: particulars are entities which have no instances14; universals are entities that can have instances. Properties and relations (corresponding to predicates in a logical language) are usually considered as universals. We take the ontology of universals as formally separated from that of particulars. Of course, universals do appear in an ontology of particulars, in- sofar they are used to organize and characterize them: simply, since they are not in the domain of discourse, they are not themselves subject to being organized and characterized (e.g., by means of metaproperties). An ontology of unary universals has been presented in [46]. In this paper, we shall occasionally use notions (e.g., rigidity) taken from such work in our meta-language. A basic choice we make in DOLCE is the so-called multiplicative approach: different entities can be co-located in the same space-time. The reason why we assume they are different is because we ascribe to them incompatible essential properties. The classical

14More exactly, we should say that they can’t have instances. This coincides with saying that they have no instances, since we include possibilia (possible instances) in our domain.

13

PT Particular

ED Endurant

PD Perdurant

Q Quality

AB Abstract

PED Physical Endurant

NPED Non-physical Endurant

R Region

AS Arbitrary Sum

EV Event STV Stative

TQ Temporal Quality

PQ Physical Quality

AQ Abstract Quality

Set Fact …

TL Temporal Location

SL Spatial Location

PR Physical Region

AR Abstract Region

TR Temporal Region

M Amount of Matter

ACH Achievement ACC Accomplishment ST State PRO Process

F Feature POB Physical Object

NPOB Non-physical Object

…

… … …

… … … …

T Time Interval

S Space Region

… … …

APO Agentive Physical Object

NAPO Non-agentive Physical Object

MOB Mental Object SOB Social Object

ASO Agentive Social Object

NASO Non-agentive Social Object

SAG Social Agent

SC Society

Figure 2: Taxonomy of DOLCE basic categories.

example is that of the vase and the amount of clay: necessarily, the vase does not survive a radical change in shape or topology, while, necessarily, the amount of clay does. There- fore the two things must be different, yet co-located: as we shall see, we say that the vase is constituted by an amount of clay, but it is not an amount of clay15. Certain properties a particular amount of clay happened to have when it was shaped by the vase-master are considered as essential for the emergence of a new entity. In language and cognition, we refer to this new entity as a genuine different thing: for instance, we say that a vase has a handle, but not that a piece of clay has a handle. A similar multiplicative attitude concerns the introduction of categories which in prin- ciple could be reduced to others. For instance, suppose we want to explore whether or not having points in addition to regions (or vice versa) in one’s ontology. It seems safe to assume the existence of both kind of entities, in order to study their formal relationships (and possibly their mutual reducibility), rather than committing on just one kind of entity in advance. Hence, when in doubt, we prefer to introduce new categories, since it is easy to explain their general behavior, while keeping at the same time the conceptual tools needed to account for their speciﬁc characteristics.

3.2 Basic categories

The taxonomy of the most basic categories of particulars assumed in DOLCE is depicted in Figure 2. They are considered as rigid properties, according to the OntoClean method- ology that stresses the importance of focusing on these properties ﬁrst. Some examples of “leaf” categories instances are illustrated in Table 1.

15One of the purposes of the OntoClean methodology [47, 48] is to help the user evaluating ontological choices like this one.

14

“Leaf” Basic Category Examples Abstract Quality the value of an asset Abstract Region the conventional value of 1 Euro Accomplishment a conference, an ascent, a performance Achievement reaching the summit of K2, a departure, a death Agentive Physical Object a human person (as opposed to legal person) Amount of Matter some air, some gold, some cement Arbitrary Sum my left foot and my car Feature a hole, a gulf, an opening, a boundary Mental Object a percept, a sense datum Non-agentive Physical Object a hammer, a house, a computer, a human body Non-agentive Social Object a law, an economic system, a currency, an asset Physical Quality the weight of a pen, the color of an apple Physical Region the physical space, an area in the color spectrum, 80Kg Process running, writing Social Agent a (legal) person, a contractant Society Fiat, Apple, the Bank of Italy State being sitting, being open, being happy, being red Temporal Quality the duration of World War I, the starting time of the 2000 Olympics Temporal Region the time axis, 22 june 2002, one second

Table 1: Examples of “leaf” basic categories.

3.2.1 Endurants and Perdurants

DOLCE is based on a fundamental distinction between enduring and perduring entities, i.e. between what philosophers usually call continuants and occurrents [76], a distinction still strongly debated both in the philosophical literature [89] and within ontology stan- dardization initiatives16. Again, we must emphasise that this distinction is motivated by our cognitive bias, and we do not commit to the fact that both these kinds of entity “do really exist”. Classically, the difference between enduring and perduring entities (which we shall also call endurants and perdurants) is related to their behavior in time. Endurants are wholly present (i.e., all their proper parts are present) at any time they are present. Perdu- rants, on the other hand, just extend in time by accumulating different temporal parts, so that, at any time they are present, they are only partially present, in the sense that some of their proper temporal parts (e.g., their previous or future phases) may be not present. E.g., the piece of paper you are reading now is wholly present, while some temporal parts of your reading are not present any more. Philosophers say that endurants are entities that are in time, while lacking however temporal parts (so to speak, all their parts ﬂow with them in time). Perdurants, on the other hand, are entities that happen in time, and can

16See for instance the extensive debate about the “3D” vs. the “4D” approach at suo.ieee.org, or the SNAP/SPAN opposition sketched in BFO

15

have temporal parts (all their parts are ﬁxed in time)17. Hence endurants and perdurants can be characterised by whether or not they can ex- hibit change in time. Endurants can “genuinely” change in time, in the sense that the very same endurant as a whole can have incompatible properties at different times; perdurants cannot change in this sense, since none of their parts keeps its identity in time. To see this, suppose that an endurant say “this paper” has a property at a time t “it’s white”, and a different, incompatible property at time t’ “it’s yellow”: in both cases we refer to the whole object, without picking up any particular part of it. On the other hand, when we say that a perdurant “running a race” has a property at t “running fast” (say during the ﬁrst ﬁve minutes) and an incompatible property at t’ “running slow” (say toward the end of the race) there are always two different parts exhibiting the two properties. Another way of characterizing endurants and perdurants – quite illuminating for our purposes – has been proposed recently by Katherine Hawley: something is an endurant iff (i) it exists at more than one moment and (ii) statements about what parts it has must be made relative to some time or other [49]. In other words, the distinction is based on the different nature of the parthood relation when applied to the two categories: endurants need a time-indexed parthood, while perdurants do not. Indeed, a statement like “this keyboard is part of my computer” is incomplete unless you specify a particular time, while “my youth is part of my life” does not require such speciﬁcation. In DOLCE, the main relation between endurants and perdurants is that of participation: an endurant “lives” in time by participating in some perdurant(s). For example, a person, which is an endurant, may participate in a discussion, which is a perdurant. A person’s life is also a perdurant, in which a person participates throughout its all duration. In the following, we shall take the term occurrence as synonym of perdurant. We prefer this choice to the more common occurrent, which we reserve for denoting a type (a universal), whose instances are occurrences (particulars).

3.2.2 Qualities and quality regions

Qualities can be seen as the basic entities we can perceive or measure: shapes, colors, sizes, sounds, smells, as well as weights, lengths, electrical charges. . . ‘Quality’ is of- ten used as a synonymous of ‘property’, but this is not the case in DOLCE: qualities are particulars, properties are universals. Qualities inhere to entities: every entity (includ- ing qualities themselves) comes with certain qualities, which exist as long as the entity exists.18 Within a certain ontology, we assume that these qualities belong to a ﬁnite set of quality types (like color, size, smell, etc., corresponding to the “leaves” of the quality taxonomy shown in Figure 2), and are characteristic for (inhere in) speciﬁc individuals: no two particulars can have the same quality, and each quality is speciﬁcally constantly dependent (see below) on the entity it inheres in: at any time, a quality can’t be present

17Time-snapshots of perdurants (i.e., in our time structure, perdurants whose temporal location is atomic, and which lack therefore proper temporal parts) are a limit case in this distinction. We consider them as perdurants since we assume that their temporal location is ﬁxed (a time-snapshot at a different time would be a different time-snapshot). 18We do not consider, for the time being, the possibility of a quality that intermittently inheres to some- thing (for instance, an object that ceases to have a color while becoming transparent).

16

1. This rose is red. 2. Red is a color. 3. This rose has a color. 4. The color of this rose turned to brown in one week. 5. The rose’s color is changing. 6. Red is opposite to green and close to brown.

Table 2: Some linguistic examples motivating the introduction of individual qualities.

unless the entity it inheres in is also present. So we distinguish between a quality (e.g., the color of a speciﬁc rose), and its “value” (e.g., a particular shade of red). The lat- ter is called quale, and describes the position of an individual quality within a certain conceptual space (called here quality space) [39]. So when we say that two roses have (exactly) the same color, we mean that their color qualities, which are distinct, have the same position in the color space, that is they have the same color quale. This distinction between qualities and qualia is inspired by [40] and the so-called trope theory [9] (with some differences that are not discussed here19). Its intuitive rationale is mainly due to the fact that natural language – in certain constructs – often seems to make a similar distinction (Table 2). For instance, in cases 4 and 5 of Table 2, we are not speaking of a certain shade of red, but of something else that keeps its identity while its ‘value’ changes. On the other hand, in case 6 we are not speaking of qualities, but rather of regions within quality spaces. The speciﬁc shade of red of our rose – its color quale – is therefore a point (or an atom, mereologically speaking) in the color space.20

Each quality type has an associated quality space with a speciﬁc structure. For exam- ple, lengths are usually associated to a metric linear space, and colors to a topological 2D space. The structure of these spaces reﬂects our perceptual and cognitive bias: this is an- other important reason for taking the notion of “quale”, as used in philosophy of mind, to designate quality regions, which roughly correspond to qualitative sensorial experiences of humans21. In this approach, we can explain the relation existing between ‘red’ intended as an adjective (as in “this rose is red”) and ‘red’ intended as a noun (as in “red is a color”): the rose is red because its color is located in the red region within the color space (more exactly, its color quale is a part of that region). Moreover, we can explain the difference between “this rose is red” and “the color of this rose is red” by interpreting “red” as synonymous of red-thing in the ﬁrst case, and of red-color in the latter case (Figure 3).

19An important difference is that standard trope theories explain a qualitative change in terms of a substi- tution of tropes (an old trope disappears and a new one is created). We assume instead that qualities persist in time during a qualitative change (note however that they are not endurants, since the parthood relation is not deﬁned for them). 20The possibility of talking of qualia as particulars rather than reiﬁed properties is another advantage of our approach. 21We also allow for non-sensorial “qualia” such as “a 1 Euro value” (ﬁxed by social conventions and independent from perception)

17

Quality

Physical Object

Region

Non-agentive Physical Object

Physical Quality

Physical Region

Color Region color space

Rose

P

Color

red color

P P P

qt

qt(c#1, rose#1) qlt

rose#1

color#1 color#2 color#3

c#1=the color of rose#1

ql(color#1, c#1, t) Red Object

Figure 3: Qualities and quality regions.

Space and time locations as special qualities. In our ontology, space and time loca- tions are considered as individual qualities like colors, weights, etc. Their corresponding qualia are called spatial (temporal) regions. For example, the spatial location of a phys- ical object belongs to the quality type space, and its quale is a region in the geometric space. Similarly for the temporal location of an occurrence, whose quale is a region in the temporal space. This allows an homogeneous approach that remains neutral about the properties of the geometric/temporal space adopted (for instance, one is free to adopt linear, branching, or even circular time).

Direct and indirect qualities. We distinguish in DOLCE two kinds of quality inherence: direct and indirect inherence. The main reason for this choice comes from the symmetric behavior of perdurants and endurants with respect to their temporal and spatial locations: perdurants have a well-deﬁned temporal location, while their spatial location seems to come indirectly from the spatial location of their participants; similarly, most endurants (what we call physical endurants, see below) have a clear spatial location, while their temporal location comes indirectly from the that of the perdurants they participate in. Another argument for this distinction concerns complex qualities like colors, which – according to Gardenfors – exhibit multiple dimensions (hue, luminosity, etc.). We model this case by assuming that such dimensions are qualities of qualities: the quality color of rose#1 has a speciﬁc hue that directly inheres to it, and indirectly inheres to rose#1.

Parts of qualities. As a ﬁnal comment, we must observe that no parthood relation (nei- ther temporal nor atemporal) is deﬁned for qualities in the DOLCE ontology. This seems to us a safe choice, since apparently we do not need to reason about parts of qualities (while we certainly do need to reason on parts of quality regions). So we do not have to commit on a single kind of parthood relationship for them (maybe some of them need a temporal parthood, while others do not). Since no parthood is deﬁned, qualities are neither endurants nor perdurants, although their persistence conditions may be similar, in certain cases, to those of endurants or perdurants.

18

3.2.3 Abstract entities

The main characteristic of abstract entities is that they do not have spatial nor temporal qualities, and they are not qualities themselves. The only class of abstract entities we consider in the present version of DOLCE is that of quality regions (or simply regions). Quality spaces are special kinds of quality regions, being mereological sums of all the regions related to a certain quality type. The other examples of abstract entities reported in Figure 2 (sets and facts) are only indicative.

3.3 Basic relations

According to the general methodology introduced in [34], before discussing the DOLCE backbone properties, we have ﬁrst to introduce a set of basic primitive relations, suitable to characterize our ontological commitments as neutrally as possible. We believe that these relations should be, as much as possible,

• general enough to be applied to multiple domains;

• such that they do not rest on questionable ontological assumptions about the onto- logical nature of their arguments;

• sufﬁciently intuitive and well studied in the philosophical literature;

• hold as soon as their relata are given, without mediating additional entities.

In the past, we adopted the term formal relation (as opposite to material relation) for a relation that can be applied to all possible domains. Recently, however, [25] proposed a different notion of formal relation: “A relation is formal if it holds as soon as its relata are given. Formal relations are called equivalently immediate relations, since they hold of their relata without mediating additional individuals”22. The notion of basic primitive relation proposed above combines together the two notions. Roughly, a basic primitive relation is an immediate relation that spans multiple application domains. The axioms constraining the arguments of primitive relations and functions are re- ported in Table 3, and summarized in Figure 4.

3.3.1 Parthood and Temporary Parthood

The endurants/perdurants distinction introduced in the previous section provides evidence for the general necessity of having two kinds of parthood relations: a-temporal and time- indexed parthood. The latter will hold for endurants, since for them it is necessary to know when a speciﬁc parthood relationship holds. Consider for instance the classical example of Tibbles the cat [76]: Tail is part of Tibbles before the cut but not after it. Formally, we can write P(Tail,Tibbles,before(cut)) and ¬P(Tail,Tibbles,after(cut)). Atemporal

22The notion of ‘immediate relation’ seems to be equivalent to what Johansson called ground relation [54]. According to Johansson, a ground relation “is derivable from its relata”. We understand that the very existence of the arguments is sufﬁcient to conclude whether the relation holds or not. This notion seems also equivalent to that of “internal relation”.

19

Parthood: “x is part of y” P(x,y) →(AB(x)∨PD(x))∧(AB(y)∨PD(y)) Temporary Parthood: “x is part of y during t” P(x,y,t) →(ED(x)∧ED(y)∧T(t))

Constitution: “x constitutes y during t” K(x,y,t) →((ED(x)∨PD(x))∧(ED(y)∨PD(y))∧T(t)) Participation: “x participates in y during t” PC(x,y,t) →(ED(x)∧PD(y)∧T(t)) Quality: “x is a quality of y” qt(x,y) →(Q(x)∧(Q(y)∨ED(y)∨PD(y))) Quale: “x is the quale of y (during t)” ql(x,y) →(TR(x)∧TQ(y)) ql(x,y,t) →((PR(x)∨AR(x))∧(PQ(y)∨AQ(y))∧T(t))

Table 3: Qualities and quality regions.

parthood, on the other hand, will be used for entities which do not properly change in time (occurrences and abstracts). In the present version, parthood will not be deﬁned for qualities. With respect to time-indexed parthood, two useful notions can be deﬁned. We shall say that an endurant is mereologically constant iff all its parts remains the same during its life, and mereologically invariant iff they remain the same across all possible worlds. For example, we usually take ordinary material objects as mereologically variable, because during their life they can lose or gain parts. On the other hand, amounts of matter are taken as mereologically invariant (all their parts are essential parts).

3.3.2 Dependence and Spatial Dependence

There are basically two approaches to characterizing the notion of ontological depen- dence:

• non-modal accounts (cf. [33] and [76], pp. 310-318);

• modal accounts (cf. [76]).

Non-modal approaches treat the dependence relation as a quasi-mereological prim- itive whose formal properties are characterized by axioms. However, as Simons has justly observed, such axiomatizations cannot rule out non-intended interpretations that are purely topological in nature. The only way to save them is actually to link them with modal accounts. In a modal approach, dependence of an entity x on an entity y might be deﬁned as fol- lows: x depends on y iff, necessarily, y is present whenever x is present. Such a deﬁnition seems to be in harmony both with commonsense intuition as well as philosophical tradi- tion (Aristotle, Husserl), despite the fact that there are some cases where, as Kit Fine has shown, this characterization is vacuous. Indeed, according to the deﬁnition, everything is

20

trivially dependent on necessarily existing or always present objects. However, Simons has shown that it is possible to exclude such vacuous examples and while this move might be philosophically dubious, it makes perfect sense in an engineering approach to ontolo- gies of everyday contingent objects. Our concept of dependence involves the notion of presence in time as well as modal- ity. We mainly use two variants of dependence, adapted from [86]: speciﬁc and generic constant dependence. The former is deﬁned both for particulars and properties, while the latter only for properties. A particular x is speciﬁcally constantly dependent on another particular y iff, at any time t, x can’t be present at t unless y is also present at t. For example, a person might be speciﬁcally constantly dependent on its brain. This notion is naturally extended to properties by deﬁning that a property φ is speciﬁcally constantly dependent on a property ψ iff every φer is speciﬁcally constantly dependent on a ψer. A property φ is generically constantly dependent on a property ψ iff, for any instance x of φ, at any time t, x can’t be present at t, unless a certain instance y of ψ is also present at t. For example, a person might be generically constantly dependent on having a heart. We deﬁne spatial dependence as a particular kind of dependence which is grounded not only in time (presence), but also in space. The deﬁnitions are as above with the further requirement that y has to be spatially co-localised with x in addition of being co-present. This notion is deﬁned both for endurants and perdurants.

3.3.3 Constitution

Constitution has been extensively discussed in the philosophical literature:

• Doepke (cit. in [76] p.238) “x constitutes y at time t iff x could be a substratum of y’s destruction”;

• Simons (cit. in [76] p.239) “When x constitutes y, there are certain properties of x which are accidental to x, but essential to y. (. . . ) Where the essential properties concern the type and disposition of parts, this is often a case of composition, but in other cases, such as that of body/person, it is not.”

Constitution is not Identity – Consider the following classical example. I buy a portion of clay (LUMPL) at 9am. At 2pm I made a statue (GOLIATH) out of LUMPL and I put GOLIATH on a table. At 3pm I replace the left hand of GOLIATH with a new one and I throw the old hand in the dustbin. There are three reasons to support the claim that LUMPL is not GOLIATH:

(i) Difference in histories. LUMPL is present a 9am, but GOLIATH is not [87].

(ii) Difference in persistence conditions. At 3pm GOLIATH is wholly present on the table, but LUMPL is not wholly present on the table (a statue can undergo replacements of certain parts, but not an amount (portion) of matter, i.e. all parts of LUMPL are essential but not all parts of GO-

LIATH are essential [87]. LUMPL can survive a change of shape, GOLIATH not.

21

(iii) Difference in essential relational properties It is metaphysically possible for LUMPL, but not for GOLIATH, to exist in the ab- sence of an artworld or an artist or anybody’s intentions [5].

3.3.4 Participation

The usual intuition about participation is that there are endurants “involved” in an occur- rence. Linguistics has extensively investigated the relation between occurrences and their participants in order to classify verbs and verbal expressions. Fillmore’s Case Grammar [29] and its developments (Construction Grammar, FrameNet) is one of the best attempts at building a systematic model of language-oriented participants. On the other hand, the ﬁrst systematic investigation goes back at least to Aristotle, that deﬁned four “causes” (aitiai), expressing the initiator, the destination, the instrument, and the substrate or host of an event. Sowa further speciﬁed subsets of aitiai on the basis of properties borrowed from linguistics (cfr. [84]). In an ontology based on a strict distinction between endurants and perdurants, par- ticipation cannot be simply parthood; the participating endurants are not parts of the occurrences: only occurrences can be parts of other occurrences. Moreover, the prim- itive participation we introduce is time-indexed, in order to account for the varieties of participation in time (temporary participation, constant participation).

3.3.5 Quality inherence and quality value

Finally, three primitive relations are introduced in order to account for qualities: a gen- eralized (direct or indirect) primitive relation23, holding between a quality and what it inheres to, and two kinds of “quale” relations (time-indexed and atemporal), holding be- tween a quality and its quale, according to whether the entity to which the quality inheres can change in time or not.

3.4 Further distinctions

Let us discuss in the following some further distinctions we make within our basic cate- gories, deﬁned with the help of the relations introduced in the previous section.

3.4.1 Physical and non-physical endurants

Within endurants, we distinguish between physical and non-physical endurants, accord- ing to whether they have direct spatial qualities. Within physical endurants, we distinguish between amounts of matter, objects, and features. This distinction is mainly based on the notion of unity we have discussed and formalized in [34]24. In principle, the general

23Direct inherence can be easily deﬁned in terms of indirect inherence. The viceversa seem to be more problematic, since it would involve a recursive deﬁnition. 24In this preliminary report, such formalization has not been included in the axiomatization presented below.

22

structure of such distinction is supposed to hold also for non-physical endurants: never- theless, we direct fully exploit it only for physical endurants, since the characteristics of non-physical features have not been considered yet.

Amounts of matter. The common trait of amounts of matter is that they are endurants with no unity (according to [34], none of them is an essential whole). Amounts of matter – “stuffs” referred to by mass nouns like “gold”, “iron”, “wood”, “sand”, “meat”, etc. – are mereologically invariant, in the sense that they change their identity when they change some parts.

Objects. The main characteristic of objects is that they are endurants with unity. How- ever, they have no common unity criterion, since different subtypes of objects may have different unity criteria. Differently from aggregates, (most) objects change some of their parts while keeping their identity, they can have therefore temporary parts. Often objects (indeed, all endurants) are ontologically independent from occurrences (discussed below). However, if we admit that every object has a life, it is hard to exclude a mutual speciﬁc constant dependence between the two. Nevertheless, we may still use the notion of de- pendence to (weakly) characterize objects as being not speciﬁcally constantly dependent on other objects.

Features. Typical examples of features are “parasitic entities” such as holes, bound- aries, surfaces, or stains, which are generically constantly dependent on physical objects25

(their hosts). All features are essential wholes, but, as in the case of objects, no common unity criterion may exist for all of them. However, typical features have a topological unity, as they are singular entities. Some features may be relevant parts of their host, like a bump or an edge, or places like a hole in a piece of cheese, the underneath of a table, the front of a house, which are not parts of their host. It may be interesting to note that we do not consider body parts like heads or hands as features: the reason is that we assume that a hand can be detached from its host (differently from a hole or a bump), and we assume that in this case it retains its identity. Should we reject this assumption, then body parts would be features.

3.4.2 Non-physical endurants and the agentive/non-agentive distinction

Within Physical Objects, a special place have those those to which we ascribe intentions, beliefs, and desires. These are called Agentive, as opposite to Non-agentive. Intention- ality is understood here as the capability of heading for/dealing with objects or states of the world26. This is an important area of ontological investigation we haven’t properly explored yet, so our suggestions are really very preliminary. In general, we assume that agentive objects are constituted by non-agentive objects: a person is constituted by an organism, a robot is constituted by some machinery, and so on.

25We may think that features are speciﬁcally constantly dependent on their host, but an example like “a whirlpool” is very critical in this sense. Notice that we are not considering as features entities that are dependent on mental-objects. 26See for example [74].

23

Among non-agentive physical objects we have for example houses, body organs, pieces of wood, etc. Non-physical Objects are divided into Social Objects and Mental Objects according to whether or not they are are generically dependent a community of agents. A private experience, for istance, is an example of a mental object. Social Objects are further divided into Agentive and Non-agentive. Examples of Agen- tive Social Objects are social agents like “the president of United States”: we may think that the latter, besides depending generically on a community of US citizens, depends also generically on “George Bush qua legal person” (since the president can be substi- tuted), which in turn depends speciﬁcally on “George Bush qua human being”. Social agents are not constituted by agentive physical objects (although they depend on them), while they can constitute societies, like the CNR, Mercedes-Benz, etc. Examples of Non- Agentive Social Objects are laws, norms, shares, peace treaties ecc., which are generically dependent on societies.

3.4.3 Kinds of perdurants

Perdurants (also called occurrences) comprise what are variously called events, processes, phenomena, activities and states. They can have temporal parts or spatial parts. For instance, the ﬁrst movement of (an execution of) a symphony is a temporal part of it. On the other side, the play performed by the left side of the orchestra is a spatial part. In both cases, these parts are occurrences themselves. We assume that objects cannot be parts of occurrences, but rather they participate in them. In DOLCE we distinguish among different kinds of occurrences mainly on the basis of two notions, both extensively discussed in the linguistic and philosophic literature: homeomericity and cumulativity. The former is discussed for instance in [11]; the latter has been introduced in [40], pp. 49-51, and reﬁned in [69]. Intuitively, we say that an occurrence is homeomeric if and only if all its temporal parts are described by the very expression used for the whole occurrence. Every temporal part of the occurrence “John sitting here” is still described by “John sitting here”. But if we consider “a walk from Ponte dei Sospiri in Venice to Piazza S. Marco”, there are no parts of such an event which constitute a walk from these two places. In linguistic as well as in philosophical terminology, the notion of the homeomericity of an occurrence is often introduced with respect to a property characteristic of (or exempliﬁed by) the occurrence itself. If such property holds for all the temporal parts of the occurrence, then the occurrence is homeomeric. In our axiomatization, this presupposes a ﬁnite list of occurrence-types (occurrents) which have to be declared in advance. An occurrence-type is stative or eventive according to whether it holds of the mere- ological sum of two of its instances, i.e. if it is cumulative or not. A sitting occurrence is stative since the sum of two sittings is still a sitting occurrence. Within stative occur- rences, we distinguish between states and processes according to homeomericity: sitting is classiﬁed as a state but running is classiﬁed as a process, since there are (very short) temporal parts of a running that are not themselves runnings. Finally, eventive occurrences (events) are called achievements if they are atomic, oth- erwise they are accomplishments.

24

Region

Temporal Region P P P

Abstract Region

Physical Region

qlt qlt ql

Quality

Abstract Quality

Physical Quality

Temporal Quality

qt qt qt

qt qt qt

Endurant

Perdurant

Non-physical Endurant

Physical Endurant

PCt

P,K Pt,K

Pt,K

Figure 4: Primitive relations between basic categories (the dotted lines to the left indicate that we are less conﬁdent with what concerns non-physical endurants.

3.4.4 Kinds of quality

We assume that qualities belong to disjoint quality types according to kinds of entity they directly inhere to. That is, temporal qualities are those that directly inhere to perdurants, physical qualities those that directly inhere to physical endurants, and abstract quali- ties those that directly inhere to non-physical perdurants (Figure 4). We are aware that, unfortunately, this terminology is very problematic: for instance, it should be clear that abstract qualities are not abstracts, since they have a temporal location. Better suggestions are welcome.

25

4 DOLCE’s Formal Characterization

4.1 Notation and introductory notes

Notation. In the following, we shall adopt the conventions below for variable and con- stant symbols:

• Constants denoting Particulars: a,b,c,...

• Variables ranging on Particulars: x,y,z,...

• Constants denoting Universals: T,R,Q...

• Variables ranging on Universals: φ,ψ,ρ,...

Modality and Time. In this module we shall adopt the simplest quantiﬁed modal logic, namely S5 plus the Barcan Formula [52]. This means that we assume a possibilist view including in the domain of quantiﬁcation all possibilia – all possible entities – indepen- dently of their actual existence [57] and that we quantify over a constant domain in every possible world (recall that all axioms and theorems are necessarily true even if the neces- sity box □is not present in front of the formulas). In addition we assume an eternalist view of time including in the domain of quantiﬁcation all past, present and future enti- ties/intervals.

Universals. In some cases we shall quantify over properties, and hence one might be- lieve we have to adopt a second-order logic. However, for our purpose, we need to quan- tify only over a ﬁnite list of predicates, those that are explicitly introduced in the present theory or in any theory that specializes (commits to) the present one. We follow therefore the strategy proposed by the Common Logic working group27, which is to view, under suitable conditions, a second-order axiom (or deﬁnition) as syntactic sugar for a ﬁnite list of ﬁrst-order axioms (deﬁnitions). Formally:

• all variables φ,ψ,ρ range on a ﬁnite set (Π) of explicitly introduced universals;

• the subclass of Π, that corresponds to the categories introduced in Figure 2, is called ΠX and it is identiﬁed by means of the (meta) predicate X : X(φ) iff φ ∈ΠX;

• existential quantiﬁers on universals, ∃φ(φ(x)), correspond to W ψ∈Π(ψ(x));

• universal quantiﬁers on universals, ∀φ(φ(x)), correspond to V ψ∈Π(ψ(x)).

More explicitly, in DOLCE we consider:

ΠX = {PT,AB,R,TR,T,PR,S,AR,Q,TQ,TL,PQ,SL,AQ,ED,PED,M,F,POB,APO, NAPO,NPED,NPOB,MOB,SOB,ASO,SAG,SC,NASO,AS,PD,EV,ACH,ACC, STV,ST,PRO}

27See cl.tamu.edu.

26

We can introduce some useful notions regarding universals:

(Dd1) RG(φ) ≜□∀x(φ(x) →□φ(x)) (φ is Rigid)

(Dd2) NEP(φ) ≜□∃x(φ(x)) (φ is Non-Empty)

(Dd3) DJ(φ,ψ) ≜□¬∃x(φ(x)∧ψ(x)) (φ and ψ are Disjoint)

(Dd4) SB(φ,ψ) ≜□∀x(ψ(x) →φ(x)) (φ Subsumes ψ)

(Dd5) EQ(φ,ψ) ≜SB(φ,ψ)∧SB(ψ,φ) (φ and ψ are Equal)

(Dd6) PSB(φ,ψ) ≜SB(φ,ψ)∧¬SB(φ,ψ) (φ Properly Subsumes ψ)

(Dd7) L(φ) ≜□∀ψ(SB(φ,ψ) →EQ(φ,ψ)) (φ is a Leaf )

(Dd8) SBL(φ,ψ) ≜SB(φ,ψ)∧L(ψ) (ψ is a Leaf Subsumed by φ)

(Dd9) PSBL(φ,ψ) ≜PSB(φ,ψ)∧L(ψ) (ψ is a Leaf Properly Subsumed by φ)

(Dd10) LX(φ) ≜X(φ)∧□∀ψ(SB(φ,ψ)∧X(ψ)) →EQ(φ,ψ)) (φ is a Leaf in ΠX)

(Dd11) SBLX(φ,ψ) ≜SB(φ,ψ)∧LX(ψ)

(Dd12) PSBLX(φ,ψ) ≜PSB(φ,ψ)∧LX(ψ)

(Dd13) PT(ψ,φi,...,φn) ≜ψ ̸= φ1 ∧DJ(φi,φj) for 1 ≤i ̸= j ≤n∧□∀x(ψ(x) ↔ (φ1(x)∨...∨φn(x))) (φ1,...,φn is a non-trivial Partition of ψ)

In Π we consider only non-empty universals, and all the predicates in ΠX are rigid, i.e.:

∀φ(NEP(φ))

∀φ((φ) →RG(φ))

and all the “taxonomic” constraints depicted in Figure 2 have to be considered as PT (ex- cept for the universals for which the categories they subsume are not completely speciﬁed in the Figure for which we have only a subsumption constraint), i.e. for example:

PT(PT,AB,Q,ED,PD),PT(R,TR,PR,AR),PT(ED,PED,NPED,AS),...

SB(AB,R),SB(TQ,TL),SB(PQ,SL),...

4.2 Deﬁnitions

4.2.1 Mereological Deﬁnitions

(Dd14) PP(x,y) ≜P(x,y)∧¬P(y,x) (Proper Part)

(Dd15) O(x,y) ≜∃z(P(z,x)∧P(z,y)) (Overlap)

(Dd16) At(x) ≜¬∃y(PP(y,x)) (Atom)

(Dd17) AtP(x,y) ≜P(x,y)∧At(x) (Atomic Part)

(Dd18) x+y ≜ιz∀w(O(w,z) ↔(O(w,x)∨O(w,y))) (Binary Sum)

27

(Dd19) σxφ(x) ≜ιz∀y(O(y,z) ↔∃w(φ(w)∧O(y,w)))28 (Sum of φ ’s)

(Dd20) PP(x,y,t) ≜P(x,y,t)∧¬P(y,x,t) (Temporary Proper Part)

(Dd21) O(x,y,t) ≜∃z(P(z,x,t)∧P(z,y,t)) (Temporary Overlap)

(Dd22) At(x,t) ≜¬∃y(PP(y,x,t)) (Temporary Atom)

(Dd23) AtP(x,y,t) ≜P(x,y,t)∧At(x,t) (Temporary Atomic Part)

(Dd24) x ≡t y ≜P(x,y,t)∧P(y,x,t) (Coincidence)

(Dd25) CP(x,y) ≜∃t(PRE(y,t))∧∀t(PRE(y,t) →P(x,y,t)) (Constant Part)

(Dd26) x+te y ≜ιz∀w,t(O(w,z,t) ↔(O(w,x,t)∨O(w,y,t)))

(Dd27) σtexφ(x) ≜ιz∀y,t(O(y,z,t) ↔∃w(φ(w)∧O(y,w,t)))29

4.2.2 Quality

(Dd28) dqt(x,y) ≜qt(x,y)∧¬∃z(qt(x,z)∧qt(z,y)) (Direct Quality)

(Dd29) qt(φ,x,y) ≜qt(x,y)∧φ(x)∧SBLX(Q,φ) (Quality of type φ)

4.2.3 Temporal and Spatial Quale

(Dd30) qlT,PD(t,x) ≜PD(x)∧∃z(qt(TL,z,x)∧ql(t,z))

(Dd31) qlT,ED(t,x) ≜ED(x)∧tσt′(∃y(PC(x,y,t′))

(Dd32) qlT,TQ(t,x) ≜TQ(x)∧∃z(qt(x,z)∧qlT,PD(t,z))

(Dd33) qlT,PQ∨AQ(t,x) ≜(PQ(x)∨AQ(x))∧∃z(qt(x,z)∧qlT,ED(t,z))

(Dd34) qlT,Q(t,x) ≜qlT,TQ(t,x)∨qlT,PQ∨AQ(t,x)

(Dd35) qlT(t,x) ≜qlT,ED(t,x)∨qlT,PD(t,x)∨qlT,Q(t,x) (Temporal Quale)

(Dd36) qlS,PED(s,x,t) ≜PED(x)∧∃z(qt(SL,z,x)∧ql(s,z,t))

(Dd37) qlS,PQ(s,x,t) ≜PQ(x)∧∃z(qt(x,z)∧qlS,PED(s,z,t))

(Dd38) qlS,PD(s,x,t) ≜PD(x)∧∃z(mppc(z,x)∧qlS,PED(s,z,t))

(Dd39) qlS(s,x,t) ≜qlS,PED(s,x,t)∨qlS,PQ(s,x,t)∨qlS,PD(s,x,t) (Spatial Quale)

Note – The temporal quale relation is not deﬁned on abstract entities. The spatial quale relation is not deﬁned on non-physical endurants, abstract qualities, non-physical perdu- rants (i.e. perdurants that have only non-physical participants))30, or abstract entities. Note – One can generalize the quale relations to include all temporal and physical quali- ties.

28In general, property φ might not belong to Π. However, it is assumed that φ is a property deﬁnable in the language of DOLCE. In addition, note that, in this formalism, the iota operator is interpreted as a relation. For instance, one can restate deﬁnition of fusion as follows: σ(x,φ) ≜∀y(O(y,x) ↔∃z(φ(z)∧O(y,z))). 29This deﬁnition may be problematic if φ depends on time. However, in the following, we apply it only to atemporal properties. 30In order to generalize the spatial quale relation in the case of non-physical entities we need a relation that specify (for each temporal interval) the physical endurant on which a non-physical endurant depends.

28

4.2.4 Being present

(Dd40) PRE(x,t) ≜∃t′(qlT(t′,x)∧P(t,t′)) (Being Present at t)

(Dd41) PRE(x,s,t) ≜PRE(x,t)∧∃s′(qlS(s′,x,t)∧P(s,s′)) (Being Present in s at t)

4.2.5 Inclusion and Coincidence

(Dd42) x ⊆T y ≜∃t,t′(qlT(t,x)∧qlT(t′,y)∧P(t,t′)) (Temporal Inclusion)

(Dd43) x ⊂T y ≜∃t,t′(qlT(t,x)∧qlT(t′,y)∧PP(t,t′)) (Proper Temporal Inclusion)

(Dd44) x ⊆S< y,t >≜∃s,s′(qlS(s,x,t)∧qlS(s′,y,t)∧P(s,s′)) (Temporary Spatial Inclusion)

(Dd45) x ⊂S< y,t >≜∃s,s′(qlS(s,x,t)∧qlS(s′,y,t)∧PP(s,s′)) (Temp. Proper Sp. Inclusion)

(Dd46) x ⊆ST y ≜∃t(PRE(x,t))∧∀t(PRE(x,t) →x ⊆S< y,t >) (Spatio-temporal Inclusion)

(Dd47) x ⊆ST< y,t >≜PRE(x,t)∧∀t′(AtP(t′,t) →x ⊆S< y,t′ >) (Spatio-temp. Incl. during t)

(Dd48) x ≈T y ≜(x ⊆T y∧y ⊆T x) (Temporal Coincidence)

(Dd49) x ≈S< y,t >≜(x ⊆S< y,t > ∧y ⊆S< x,t >) (Temporary Spatial Coincidence)

(Dd50) x ≈ST y ≜(x ⊆ST y∧y ⊆ST x) (Spatio-temporal Coincidence)

(Dd51) x ≈ST< y,t >≜PRE(x,t)∧∀t′(AtP(t′,t) →x ≈S< y,t′ > y) (Spatio-temp. Coincidence dur. t)

(Dd52) x⃝T y ≜∃t,t′(qlT(t,x)∧qlT(t′,y)∧O(t,t′)) (Temporal Overlap)

(Dd53) x⃝S < y,t >≜∃s,s′(qlS(s,x,t)∧qlS(s′,y,t)∧O(s,s′)) (Temporary Spatial Overlap)

4.2.6 Perdurant

(Dd54) PT(x,y) ≜PD(x)∧P(x,y)∧∀z((P(z,y)∧z ⊆T x) →P(z,x)) (Temporal Part)

(Dd55) PS(x,y) ≜PD(x)∧P(x,y)∧x ≈T y (Spatial Part)

(Dd56) NEPS(φ) ≜SB(PD,φ)∧□∃x,y(φ(x)∧φ(y)∧¬P(x,y)∧¬P(y,x)) (φ is Strongly Non-Empty)

(Dd57) CM(φ) ≜SB(PD,φ)∧□∀x,y((φ(x)∧φ(y)) →φ(xy)) (φ is Cumulative)

(Dd58) CM∼(φ) ≜SB(PD,φ)∧□∀x,y((φ(x)∧φ(y)∧¬P(x,y)∧¬P(y,x)) →¬φ(xy)) (φ is Anti-Cumulative)

(Dd59) HOM(φ) ≜SB(PD,φ)∧□∀x,y((φ(x)∧PT(y,x)) →φ(y)) (φ is Homeomerous)

(Dd60) HOM∼(φ) ≜SB(PD,φ)∧□∀x(φ(x) →∃y(PT(y,x)∧¬φ(y)) (φ is Anti-Homeom.)

29

Q: Quality

MSD

TQ Temporal Quality

PD Perdurance/ Occurrence AQ Abstract Quality

PQ Physical Quality

MSD

MSDS P-1GDS PGDS

OD

NPED: Non-physical Endurant

PED: Physical Endurant

NPOB: Non-physical Object

M Amount of Matter

OSD

MOB Mental Object

SOB: Social Object

GK

ASO: Agentive Social Object

POB: Physical Object

GK

SAG Social Agent

GK

APO Agentive Physical Obj

NAPO Non-agentive Physical Obj

SC Society

OGD

OGD

OGD

NASO Non-agentive Social Obj

F Feature

...

ED: Endurant

Figure 5: Constitution/(Spatial)Dependence relations between basic categories.

(Dd61) AT(φ) ≜SB(PD,φ)∧□∀x(φ(x) →At(x)) (φ is Atomic)

(Dd62) AT∼(φ) ≜SB(PD,φ)∧□∀x(φ(x) →¬At(x)) (φ is Anti-Atomic)

4.2.7 Participation

(Dd63) PCC(x,y) ≜∃t(PRE(y,t))∧∀t(PRE(y,t) →PC(x,y,t)) (Const. Participation)

(Dd64) PCT(x,y,t) ≜PD(y)∧∀z((P(z,y)∧PRE(z,t)) →PC(x,z,t)) (Temporary Total Participation)

(Dd65) PCT(x,y) ≜∃t(qlT(t,y)∧PCT(x,y,t)) (Total Participation)

(Dd66) mpc(x,y) ≜x = σtz(PCT(z,y)) (Maximal Participant)

(Dd67) mppc(x,y) ≜x = σtz(PCT(z,y)∧PED(z)) (Maximal Physical Participant)

(Dd68) lf(x,y) ≜x = σz(PCT(y,z)) (Life)

4.2.8 Dependence

(see Figure 5 for a summary of dependence relations between the basic categories)

30

(Dd69) SD(x,y) ≜□(∃t(PRE(x,t))∧∀t(PRE(x,t) →PRE(y,t))) (Speciﬁc Const. Dep.)

(Dd70) SD(φ,ψ) ≜DJ(φ,ψ)∧□∀x(φ(x) →∃y(ψ(y)∧SD(x,y))) (Speciﬁc Const. Dep.)

(Dd71) GD(φ,ψ) ≜DJ(φ,ψ)∧□(∀x(φ(x) →∃t(PRE(x,t)) (Generic Const. Dep.) ∧∀x,t((φ(x)∧At(t)∧PRE(x,t)) →∃y(ψ(y)∧PRE(y,t))))

(Dd72) D(φ,ψ) ≜SD(φ,ψ)∨GD(φ,ψ)) (Constant Dependence)

(Dd73) OD(φ,ψ) ≜D(φ,ψ)∧¬D(ψ,φ) (One-sided Constant Dependence)

(Dd74) OSD(φ,ψ) ≜SD(φ,ψ)∧¬D(ψ,φ) (One-sided Speciﬁc Constant Dependence)

(Dd75) OGD(φ,ψ) ≜GD(φ,ψ)∧¬D(ψ,φ) (One-sided Generic Constant Dependence)

(Dd76) MSD(φ,ψ) ≜SD(φ,ψ)∧SD(ψ,φ) (Mutual Speciﬁc Constant Dependence)

(Dd77) MGD(φ,ψ) ≜GD(φ,ψ)∧GD(ψ,φ) (Mutual Generic Constant Dependence)

Note – Regions are not present in time and then the deﬁnition of dependence does not make sense for these entities.

4.2.9 Spatial Dependence

(see Figure 5 for a summary of spatial dependence relations between the basic categories)

(Dd78) SDS(x,y) ≜□(∃t,s(PRE(x,s,t))∧∀s,t(PRE(x,s,t) →PRE(y,s,t))) (Speciﬁc Spatial Dependence)

(Dd79) PSDS(x,y) ≜□(∃t,s(PRE(x,s,t))∧∀s,t(PRE(x,s,t) → ∃s′(PP(s′,s)∧PRE(y,s′,t)))) (Partial Speciﬁc Spatial Dependence)

(Dd80) P−1SDS(x,y) ≜□(∃t,s(PRE(x,s,t))∧ ∀s,t(PRE(x,s,t) →∃s′(PP(s,s′)∧PRE(y,s′,t)))) (Inverse Partial Speciﬁc Spatial Dependence)

(Dd81) SDS(φ,ψ) ≜DJ(φ,ψ)∧□∀x(φ(x) →∃y(ψ(y)∧SDS(x,y)))

(Dd82) PSDS(φ,ψ) ≜DJ(φ,ψ)∧□∀x(φ(x) →∃y(ψ(y)∧PSDS(x,y)))

(Dd83) P−1SDS(φ,ψ) ≜DJ(φ,ψ)∧□∀x(φ(x) →∃y(ψ(y)∧P−1SDS(x,y)))

(Dd84) GDS(φ,ψ) ≜DJ(φ,ψ)∧□(∀x(φ(x) →∃t,s(PRE(x,s,t)) ∧∀x,s,t((φ(x)∧At(t)∧PRE(x,s,t)) →∃y(ψ(y)∧PRE(y,s,t)))) (Generic Spatial Dependence)

(Dd85) PGDS(φ,ψ) ≜DJ(φ,ψ)∧□(∀x(φ(x) →∃t,s(PRE(x,s,t)) ∧∀x,s,t((φ(x)∧At(t)∧PRE(x,s,t)) →∃y,s′(ψ(y)∧PP(s′,s)∧PRE(y,s′,t)))) (Partial Generic Spatial Dependence)

(Dd86) P−1GDS(φ,ψ) ≜DJ(φ,ψ)∧□(∀x(φ(x) →∃t,s(PRE(x,s,t)) ∧∀x,s,t((φ(x)∧At(t)∧PRE(x,s,t)) →∃y,s′(ψ(y)∧PP(s,s′)∧PRE(y,s′,t)))) (Inverse Partial Generic Spatial Dependence)

(Dd87) DGDS(φ,ψ) ≜GDS(φ,ψ)∧¬∃ρ(GDS(φ,ρ)∧GDS(ρ,ψ)) (Direct Generic Spatial Dependence)

(Dd88) SDtS(x,y,t) ≜SDS(x,y)∧PRE(x,t) (Temporary Speciﬁc Spatial Dependence)

31

(Dd89) GDtS(x,y,t) ≜∃φ,ψ(φ(x)∧ψ(y)∧GDS(φ,ψ)∧x ≈S< y,t >) (Temporary Generic Spatial Dependence)

(Dd90) DGDtS(x,y,t) ≜∃φ,ψ(φ(x)∧ψ(y)∧DGDS(φ,ψ)∧x ≈S< y,t >) (Temporary Direct Spatial Depencende)

(Dd91) OSDS(φ,ψ) ≜SDS(φ,ψ)∧¬D(ψ,φ) (One-sided Speciﬁc Spatial Dependence)

(Dd92) OGDS(φ,ψ) ≜GDS(φ,ψ)∧¬D(ψ,φ) (One-sided Generic Spatial Dependence)

(Dd93) MSDS(φ,ψ) ≜SDS(φ,ψ)∧SDS(ψ,φ) (Mutual Speciﬁc Spatial Dependence)

(Dd94) MGDS(φ,ψ) ≜GDS(φ,ψ)∧GDS(ψ,φ) (Mutual Generic Spatial Dependence)

Note – Supposing that DGDS(φ,ψ) does not mean that there could not be another ρ such that DGDS(ρ,ψ). That is we do not exclude at the moment the possibility that there are might be two different properties which are generically directly spatially dependent on a given property. If we allow this, we have no proper stratiﬁcation with respect to spatial dependence, in the sense that there is no total order between the strata. In order to guar- antee the latter, we would need axioms like the following (an analogue argument is valid for constitution):

(DGDS(φ,ψ)∧DGDS(ρ,ψ)) →ρ = φ (DGDS(φ,ψ)∧DGDS(φ,ρ)) →ρ = ψ

4.2.10 Constitution

(see Figure 5 for a summary of constitution relations between the basic categories))

(Dd95) DK(x,y,t) ≜K(x,y,t)∧¬∃z(K(x,z,t)∧K(z,y,t)) (Direct Constitution)

(Dd96) SK(x,y) ≜□(∃t(PRE(x,t))∧∀t(PRE(x,t) →K(y,x,t))) (x is Constantly Speciﬁcally Constituted by y)

(Dd97) SK(φ,ψ) ≜DJ(φ,ψ)∧□∀x(φ(x) →∃y(ψ(y)∧SK(x,y))) (φ is Constantly Speciﬁcally Constituted by ψ)

(Dd98) GK(φ,ψ) ≜DJ(φ,ψ)∧□(∀x(φ(x) →∃t(PRE(x,t))∧ ∀x,t((φ(x)∧At(t)∧PRE(x,t)) →∃y(ψ(y)∧K(y,x,t)))) (φ is Constantly Generically Constituted by ψ)

(Dd99) K(φ,ψ) ≜SK(φ,ψ)∨GK(φ,ψ)) (φ is Constituted by ψ)

(Dd100) OSK(φ,ψ) ≜SK(φ,ψ)∧¬K(ψ,φ) (φ is One-sided Cons. Specif. Const. by ψ)

(Dd101) OGK(φ,ψ) ≜GK(φ,ψ)∧¬K(ψ,φ) (φ is One-sided Cons. Gen. Const. by ψ)

(Dd102) MSK(φ,ψ) ≜SK(φ,ψ)∧SK(ψ,φ) (Mutual Speciﬁc Constitution)

(Dd103) MGK(φ,ψ) ≜GK(φ,ψ)∧GK(ψ,φ) (Mutual Generic Constitution)

32

4.3 Characterization of primitive relations

4.3.1 Parthood

We shall adopt for the atemporal parthood the axioms of atomic General Extensional Mereology (GEM), and the classical deﬁnitions of overlap, proper part, atom, etc.

Argument Restrictions

(Ad1) P(x,y) →(AB(x)∨PD(x))∧(AB(y)∨PD(y))

(Ad2) P(x,y) →(PD(x) ↔PD(y))

(Ad3) P(x,y) →(AB(x) ↔AB(y))

(Ad4) (P(x,y)∧SB(R,φ)∧X(φ)) →(φ(x) ↔φ(y))

Ground Axioms

(Ad5) (AB(x)∨PD(x)) →P(x,x)

(Ad6) (P(x,y)∧P(y,x)) →x = y

(Ad7) (P(x,y)∧P(y,z)) →P(x,z)

(Ad8) ((AB(x)∨PD(x))∧¬P(x,y)) →∃z(P(z,x)∧¬O(z,y))

(Ad9) (∃xφ(x)∧(∀x(φ(x) →AB(x))∨∀x(φ(x) →PD(x)))) →∃y(y = σxφ(x))

4.3.2 Temporary Parthood

We drop antisymmetry and we slightly modify the axioms for P by introducing the inﬁnite sum deﬁned in (D27).

Argument restrictions

(Ad10) P(x,y,t) →(ED(x)∧ED(y)∧T(t))

(Ad11) P(x,y,t) →(PED(x) ↔PED(y))

(Ad12) P(x,y,t) →(NPED(x) ↔NPED(y))

Ground Axioms

(Ad13) (P(x,y,t)∧P(y,z,t)) →P(x,z,t)

(Ad14) (ED(x)∧ED(y)∧PRE(x,t)∧PRE(y,t)∧¬P(x,y,t))→∃z(P(z,x,t)∧¬O(z,y,t))

(Ad15) (∃xφ(x)∧∀x(φ(x) →ED(x))) →∃y(y = σtexφ(x))

Links With Other Primitives

(Ad16) (ED(x)∧PRE(x,t)) →P(x,x,t)

(Ad17) P(x,y,t) →(PRE(x,t)∧PRE(y,t))

(Ad18) P(x,y,t) →∀t′(P(t′,t) →P(x,y,t′))

(Ad19) (PED(x)∧P(x,y,t)) →x ⊆S< y,t >

Debatable axiom

33

(AP=) (CP(x,y)∧CP(y,x)) →x = y

Note – With the introduction of (Ad15) we are accepting the existence of intermittent objects. Consider for example the sum of two objects that are temporally extended in disjoint intervals. In this case we have a theorem like PRE(c1 + c2,t) ↔(PRE(c1,t) ∨ PRE(c2,t)). Alternatively, we could deﬁne a different sum of temporally co-extensional endurants. (cf. [76] and [87]). Note – The unicity of the product is guaranteed only introducing (AP=). Note – We can alternatively consider P(x,y,t) deﬁned only on temporal atoms, by substi- tuting (Ad18) with P(x,y,t) →At(t). Note – It may be interesting to study the cases where the law of substitution restricted to coincident entities is valid. In other words, we may want to study the circumstances where taken a temporary n + 1-ary relation between particulars, Rel(x1,...,xn,t), then (Rel(x1,...,xn,t)∧x1 ≡t y1 ∧...∧xn ≡t yn) →Rel(y1,...,yn,t) holds. Note – Clearly, extensionality does not hold in this case. That is, having the same parts does not imply being the same. Nevertheless, we have still to decide whether or not having the same proper parts means being coincident: P(x,y,t) ↔∀z(PP(z,x,t) →P(z,y,t)).

4.3.3 Constitution

Argument restrictions

(Ad20) K(x,y,t) →((ED(x)∨PD(x))∧(ED(y)∨PD(y))∧T(t))

(Ad21) K(x,y,t) →(PED(x) ↔PED(y))

(Ad22) K(x,y,t) →(NPED(x) ↔NPED(y))

(Ad23) K(x,y,t) →(PD(x) ↔PD(y))

Ground Axioms

(Ad24) K(x,y,t) →¬K(y,x,t)

(Ad25) (K(x,y,t)∧K(y,z,t)) →K(x,z,t)

Links with other Primitives

(Ad26) K(x,y,t) →(PRE(x,t)∧PRE(y,t))

(Ad27) K(x,y,t) ↔∀t′(P(t′,t) →K(x,y,t′))

(Ad28) (K(x,y,t)∧PED(x)) →x ≈S< y,t >

(Ad29) (K(x,y,t)∧P(y′,y,t)) →∃x′(P(x′,x,t)∧K(x′,y′,t))

Links between Categories

(Ad30) GK(NAPO,M)

(Ad31) GK(APO,NAPO)

(Ad32) GK(SC,SAG)

General Properties

(Td1) ¬K(x,x,t)

34

(Td2) SK(φ,ψ) →SD(φ,ψ)

(Td3) GK(φ,ψ) →GD(φ,ψ)

(Td4) (SK(φ,ψ)∧SK(ψ,ρ)∧DJ(φ,ρ)) →SK(φ,ρ)

(Td5) (GK(φ,ψ)∧GK(ψ,ρ)∧DJ(φ,ρ)) →GK(φ,ρ)

Debatable Axioms

(??) SK(x,y) →¬D(y,x)

(??) SK(φ,ψ) →¬D(ψ,φ)

(??) GK(φ,ψ) →¬D(ψ,φ)

(??) K(x,y,t) →(AtP(z,x,t)) ↔AtP(z,y,t))

Note – This last axiom is strong but it is also very informative on the distinction between spatial dependence and constitution.

4.3.4 Participation

Argument restrictions

(Ad33) PC(x,y,t) →(ED(x)∧PD(y)∧T(t))

Existential Axioms

(Ad34) (PD(x)∧PRE(x,t)) →∃y(PC(y,x,t))

(Ad35) ED(x) →∃y,t(PC(x,y,t))

Links with other Primitives

(Ad36) PC(x,y,t) →(PRE(x,t)∧PRE(y,t))

(Ad37) PC(x,y,t) ↔∀t′(P(t′,t) →PC(x,y,t′))

Ground Properties

(Td6) ¬PC(x,x,t)

(Td7) PC(x,y,t) →¬PC(y,x,t)

Note - We consider also non-physical endurants as participants.

4.3.5 Quality

Argument restrictions

(Ad38) qt(x,y) →(Q(x)∧(Q(y)∨ED(y)∨PD(y)))

(Ad39) qt(x,y) →(TQ(x) ↔(TQ(y)∨PD(y)))

(Ad40) qt(x,y) →(PQ(x) ↔(PQ(y)∨PED(y)))

(Ad41) qt(x,y) →(AQ(x) ↔(AQ(y)∨NPED(y)))

Ground Axioms

(Ad42) (qt(x,y)∧qt(y,z)) →qt(x,z)

35

(Ad43) (dqt(x,y)∧dqt(x,y′)) →y = y′

(Ad44) (qt(φ,x,y)∧qt(φ,x′,y)) →x = x′

(Ad45) (qt(φ,x,y)∧qt(ψ,y,z)) →DJ(φ,ψ)

Existential Axioms

(Ad46) TQ(x) →∃!y(qt(x,y)∧PD(y))

(Ad47) PQ(x) →∃!y(qt(x,y)∧PED(y))

(Ad48) AQ(x) →∃!y(qt(x,y)∧NPED(y))

(Ad49) PD(x) →∃y(qt(TL,y,x))

(Ad50) PED(x) →∃y(qt(SL,y,x))

(Ad51) NPED(x) →∃φ,y(SBL(AQ,φ)∧qt(φ,y,x))

Ground Properties

(Td8) ¬qt(x,x)

Note – Maybe it is interesting to make explicit, for each kind of entities, which are the types of quality they necessarily possess.

4.3.6 Quale

Immediate Quale Argument restrictions

(Ad52) ql(x,y) →(TR(x)∧TQ(y))

(Ad53) (ql(x,y)∧TL(y)) →T(x)

Ground Axioms

(Ad54) (ql(x,y)∧ql(x′,y)) →x = x′

Existential Axioms

(Ad55) TQ(x) →∃y(ql(y,x))

(Ad56) (LX(φ)∧φ(x)∧φ(y)∧ql(r,x)∧ql(r′,y)) →∃ψ(LX(ψ)∧ψ(r)∧ψ(r′))

(Ad57) (LX(φ)∧φ(x)∧¬φ(y)∧ql(r,x)∧ql(r′,y)) →¬∃ψ(LX(ψ)∧ψ(r)∧ψ(r′))

Temporary Quale Argument restrictions

(Ad58) ql(x,y,t) →((PR(x)∨AR(x))∧(PQ(y)∨AQ(y))∧T(t))

(Ad59) ql(x,y,t) →(PR(x) ↔PQ(y))

(Ad60) ql(x,y,t) →(AR(x) ↔AQ(y))

(Ad61) (ql(x,y,t)∧SL(y)) →S(x)

Existential Axioms

(Ad62) ((PQ(x)∨AQ(x))∧PRE(x,t)) →∃y(ql(y,x,t))

36

(Ad63) (LX(φ)∧φ(x)∧φ(y)∧ql(r,x,t)∧ql(r′,y,t)) →∃ψ(LX(ψ)∧ψ(r)∧ψ(r′))

(Ad64) (LX(φ)∧φ(x)∧¬φ(y)∧ql(r,x,t)∧ql(r′,y,t)) →¬∃ψ(LX(ψ)∧ψ(r)∧ψ(r′))

Links with other Primitives

(Ad65) ql(x,y,t) →PRE(y,t)

(Ad66) ql(x,y,t) ↔∀t′(P(t′,t) →ql(x,y,t′))

4.3.7 Dependence and Spatial Dependence

Links between Categories

(Ad67) MSD(TQ,PD)

(Ad68) MSDS(PQ,PED)

(Ad69) MSD(AQ,NPED)

(Ad70) OGD(F,NAPO)

(Ad71) OSD(MOB,APO)

(Ad72) OGD(SAG,APO)

(Ad73) OGD(NASO,SC)

(Ad74) OD(NPED,PED)

General Properties

(Td9) (SD(φ,ψ)∧SD(ψ,ρ)∧DJ(φ,ρ)) →SD(φ,ρ)

(Td10) (GD(φ,ψ)∧GD(ψ,ρ)∧DJ(φ,ρ)) →GD(φ,ρ)

(Td11) (SD(φ,ψ)∧GD(ψ,ρ)∧DJ(φ,ρ)) →GD(φ,ρ)

(Td12) (GD(φ,ψ)∧SD(ψ,ρ)∧DJ(φ,ρ)) →GD(φ,ρ)

(Td13) SDS(φ,ψ) →SD(φ,ψ)

(Td14) GDS(φ,ψ) →GD(φ,ψ)

4.3.8 Being Present

Argument restrictions

(Td15) (ED(x)∨PD(x)∨Q(x)) →∃t(PRE(x,t))

(Td16) ((PED(x)∨PQ(x))∧PRE(x,t)) →∃s(PRE(s,x,t))

Ground Axioms

(Td17) (PRE(x,t)∧P(t′,t)) →PRE(x,t′)

(Td18) PRE(s,x,t) →PRE(x,t)

37

4.4 Characterization of Categories

In order to resume all the properties of categories, we shall report in this section also some axioms or theorems introduced in the previous sections. We shall mark these ax- ioms/theorems with an asterisk.

4.4.1 Region

(Ad4)∗(P(x,y)∧SB(R,φ)∧X(φ)) →(φ(x) ↔φ(y))

(Ad59)∗ql(x,y,t) →(PR(x) ↔PQ(y))

(Ad60)∗ql(x,y,t) →(AR(x) ↔AQ(y))

(Ad62)∗((PQ(x)∨AQ(x))∧PRE(x,t)) →∃y(ql(y,x,t))

Debatable Axioms

(??) ∃x(R(x) →¬∃y,t(ql(x,y,t)))

(??) □∀x,t(R(x) →∃y(ql(x,y,t))

4.4.2 Quality

(Ad38)∗qt(x,y) →(Q(x)∧(Q(y)∨ED(y)∨PD(y)))

(Ad39)∗qt(x,y) →(TQ(x) ↔(TQ(y)∨PD(y)))

(Ad40)∗qt(x,y) →(PQ(x) ↔(PQ(y)∨PED(y)))

(Ad41)∗qt(x,y) →(AQ(x) ↔(AQ(y)∨NPED(y)))

(Ad46)∗TQ(x) →∃!y(qt(x,y)∧PD(y))

(Ad47)∗PQ(x) →∃!y(qt(x,y)∧PED(y))

(Ad48)∗AQ(x) →∃!y(qt(x,y)∧NPED(y))

(Ad67)∗MSD(TQ,PD)

(Ad68)∗MSDS(PQ,PED)

(Ad69)∗MSD(AQ,NPED)

(Td15)∗(ED(x)∨PD(x)∨Q(x)) →∃t(PRE(x,t))

4.4.3 Perdurant

(Ad2)∗P(x,y) →(PD(x) ↔PD(y))

(Ad39)∗qt(x,y) →(TQ(x) ↔(TQ(y)∨PD(y)))

(Ad46)∗TQ(x) →∃!y(qt(x,y)∧PD(y))

(Ad49)∗PD(x) →∃y(qt(TL,y,x))

(Ad34)∗(PD(x)∧PRE(x,t)) →∃y(PC(y,x,t))

(Td15)∗(ED(x)∨PD(x)∨Q(x)) →∃t(PRE(x,t))

38

Conditions on Perdurant’s Leaves

(Ad75) PSBL(ACH,φ) →(NEPS(φ)∧CM∼(φ)∧AT(φ))

(Ad76) PSBL(ACC,φ) →(NEPS(φ)∧CM∼(φ)∧AT∼(φ))

(Ad77) PSBL(ST,φ) →(NEPS(φ)∧CM(φ)∧HOM(φ))

(Ad78) PSBL(PRO,φ) →(NEPS(φ)∧CM(φ)∧HOM∼(φ))

Existential Axioms

(Ad79) ∃φ(PSBL(ACH,φ))

(Ad80) ∃φ(PSBL(ACC,φ))

(Ad81) ∃φ(PSBL(ST,φ))

(Ad82) ∃φ(PSBL(PRO,φ))

Debatable Axioms

(??) (PD(x)∧PD(y)∧x ⊆T y) →∃z(z ≈T x∧z ⊆ST y)

4.4.4 Endurant

(Ad35)∗ED(x) →∃y,t(PC(x,y,t))

(Td15)∗(ED(x)∨PD(x)∨Q(x)) →∃t(PRE(x,t))

Physical endurant

(Ad11)∗P(x,y,t) →(PED(x) ↔PED(y))

(Ad21)∗K(x,y,t) →(PED(x) ↔PED(y))

(Ad40)∗qt(x,y) →(PQ(x) ↔(PQ(y)∨PED(y)))

(Ad47)∗PQ(x) →∃!y(qt(x,y)∧PED(y))

(Ad50)∗PED(x) →∃y(qt(SL,y,x))

(Ad68)∗MSDS(PQ,PED)

(Ad74)∗OD(NPED,PED)

Debatable Axioms

(??) (PED(x)∧PED(y)∧□(x ≈ST y)) →x = y

Amount of Matter

(Ad30)∗GK(NAPO,M)

39

Physical Object

(Ad32)∗GK(SC,SAG)

(Ad30)∗GK(NAPO,M)

(Ad70)∗OGD(F,NAPO)

(Ad71)∗OSD(MOB,APO)

(Ad72)∗OGD(SAG,APO)

Feature

(Ad70)∗OGD(F,NAPO)

Non-physical Endurant

(Ad12)∗P(x,y,t) →(NPED(x) ↔NPED(y))

(Ad22)∗K(x,y,t) →(NPED(x) ↔NPED(y))

(Ad41)∗qt(x,y) →(AQ(x) ↔(AQ(y)∨NPED(y)))

(Ad48)∗AQ(x) →∃!y(qt(x,y)∧NPED(y))

(Ad51)∗NPED(x) →∃φ,y(SBL(AQ,φ)∧qt(φ,y,x))

(Ad74)∗OD(NPED,PED)

Mental Object

(Ad71)∗OSD(MOB,APO)

Social Object

(Ad73)∗OGD(NASO,SC)

(Ad32)∗GK(SC,SAG)

(Ad71)∗OSD(MOB,APO)

(Ad72)∗OGD(SAG,APO)

40

4.5 Glossary of Basic Categories

AB Abstract ACC Accomplishment ACH Achievement APO Agentive Physical Object AQ Abstract Quality AR Abstract Region AS Arbitrary Sum ASO Agentive Social Object ED Endurant EV Event F Feature M Amount of Matter MOB Mental Object NAPO Non-agentive Physical Object NASO Non-agentive Social Object NPED Non-physical Endurant NPOB Non-physical Object PD Perdurant, Occurrence PED Physical Endurant POB Physical Object PQ Physical Quality PR Physical Region PRO Process PT Particular Q Quality R Region S Space Region SAG Social Agent SC Society SL Spatial Location SOB Social Object ST State STV Stative T Time Interval TL Temporal Location TQ Temporal Quality TR Temporal Region

Abstract AB Abstract Quality AQ Abstract Region AR Accomplishment ACC Achievement ACH Agentive Physical Object APO Agentive Social Object ASO Amount of Matter M Arbitrary Sum AS Endurant ED Event EV Feature F Mental Object MOB Non-agentive Physical Object NAPO Non-agentive Social Object NASO Non-physical Endurant NPED Non-physical Object NPOB Particular PT Perdurant, Occurrence PD Physical Endurant PED Physical Object POB Physical Quality PQ Physical Region PR Process PRO Quality Q Region R Social Agent SAG Social Object SOB Society SC Space Region S Spatial Location SL State ST Stative STV Temporal Location TL Temporal Quality TQ Temporal Region TR Time Interval T

41

5 OCHRE: the Object-Centered High-level Reference Ontology

OCHRE is the second module in the WonderWeb library. It has been developed by Luc Schneider at the Department of Philosophy of the University of Geneva. This ontology differs from the previous because it is based on different set of assumptions. In particular, it presents a revisionary view with respect to the standard notion of commonsense.

Revisionary Commonsensism. Any foundational ontology used in distributed AI ap- plicationsinvolving human-computer interaction has to take into account thenaive concep- tualisation shared by humans with regard to their every-day environment. Unfortunately, the problem with commonsense is that it is a moving target, and we share Casati’s [10] scepticism with respect to any attempt to read off an ontological commitment from the observable (linguistic or else) human behaviour. That is why we feel uneasy about the phrase “cognitive bias”, since it is not clear whether human cognition grants any kind of representational advantage to one ontological category over another (e.g. to “things” over “events”). On the other hand, however, theoretical studies of translation suggest that the interpretation of an alien speaker’s utterances only works on the assumption that the inter- preter and the interpretee share the greatest possible common background of beliefs about their common environment [20, 22, 21, 23, 24]. These shared assumptions are without doubt part of the conventional implicatures underlying human conversation [44]. Although Quine [72, pp. 29-45] has famously voiced some caution regarding a possi- ble indeterminacy of translation, a lack of empirical constraints for matching the vocab- ularies of different languages. In a critical appraisal of Quine’s behaviourist account of interpretation, Horwich [51, pp. 199-202] has shown that in practice such indeterminacies may actually be marginal. Thus, there is room for assuming the existence of a common human conceptual framework regarding the environment of every-day life. Of course, there is no guarantee that this “naive metaphysics” is true. But in the absence of any rea- son for a generalised doubt, there is some methodological legitimacy to adopt a “second naivet´e” (Putnam [71, pp. 488–489]), a “natural ontological attitude” (A. Fine [30]), with respect to human perception and conceptualisation of reality. Revisionism comes in at the stage of making “naive metaphysics” explicit. Indeed, while it should be rather unproblematic to gather a collection of distinctions between various material or concrete kinds of entities from colloquial usage, this is far from being so easy with respect to formal categories like “object”, “event”, “attribute”, “being part of”, “being connected to”, and so on. The latter are mere generalisations and belong already to a specialised discourse which is not part of every-day linguistic practice. To a large extent, “naive metaphysics” is a matter of extrapolation – and extrapolation can be guided by quite different criteria. In particular, revisionist metaphysics is characterised by a strict economy of basic formal categories. As such, revisionist metaphysics is not directed against commonsense or, at least, no more than against a certain traditional, if not “Aristotelian”, wording of the latter. So there is no contradiction in pursuing a descriptive approach while trying to keep the number of terms to a minimum.

42

5.1 Basic Assumptions

The Object-Centered High-level Reference ontology (OCHRE) has been developed within the above framework and aims at combining descriptive adequacy for commonsense with formal economy in the basic categories and their axiomatisation.

Particularism. OCHRE is an ontology of particulars, even more so than DOLCE, because it does not include universals, i.e. repeatable properties, in its domain. With “particulars”, we mean here the concrete individuals, whether physical, mental or social, which we regard to be composed out of simple (atomic) individual features, i.e. non-repeatable properties and relations. Nevertheless, the domain of OCHRE is left sufﬁciently unspeci- ﬁed to allow for user-speciﬁed extensions. Other theories can be plugged into OCHRE; a desirable addition could be elementary set theory as well as an apparatus for representing meta-knowledge.

Object-Centered Approach. OCHRE is an object-centered ontology in the sense that certain bundles of tropes, namely those exhibiting spatial and temporal features as well as their enduring cores, are granted a privileged ontological status over other particulars. Especially the “event” category is considered to be a derived from the concept of “object”, inasmuch occurrences as state-transitions are conceived of as successions of objects.

Extensionalism. OCHRE is decidedly extensionalist in two respects. On the one hand, we adopt extensionalism regarding parthood, which means that particulars with the same parts are considered to be the same. On the other hand, we adopt extensionalism with respect to spatial extent, insofar as no two spatial objects can be coincident. Thus, OCHRE rejects the multiplicative approach; instead of multiplying spatial objects having the same parts or the same spatial extension, we prefer to speak of spatial objects having various qualitative aspects or “guises”. A statue and the material it is made of are not two coinci- dent objects, but two facets of the same impenetrable object.

5.2 Basic Categories

The crucial ontological choice in foundational ontology pertains to the basic ontologi- cal categories. There is a widespread consensus amongst ontologists that the denizens of reality fall into three main categories: objects (like quarks, tables, stones, insurance companies and solar systems), attributes or particular properties and relations (like the various colour hues on a soap bubble, the mass and velocity of a bullet, your intelligence and your relatedness to your parents) as well as events and processes (like runnings, hugs, bank transfers, perceptions, and thinkings).

5.2.1 Tropes

Attributes can be regarded either as repeatables or as non-repeatables (Armstrong [3, p. 31]). Repeatables, also called universals, apply to more than one case; by contrast,

43

non-repeatables, commonly referred to as tropes (Williams [90]; Campbell [9]), are sin- gle characteristics of individuals. OCHRE endorses the view of Williams, Campbell, and Denkel that the building blocks of reality, the atoms of mereology, are non-repeatables. Note however, that not every non-repeatable has to be atomic: as we shall see, some non- repeatable properties (like colours) may be regarded as composite. In the context of this report, the term trope will denote atomic non-repeatables only.

5.2.2 Thin and Thick Objects

Considerations of formal economy have lead us to adopt the so-called qualitative account of objects, according to which the latter are regarded as bundles of properties and re- lations. The qualitative account enjoys a certain popularity among ontologists, as e.g. Williams ([90]), Campbell ([9]), Denkel ([26]), and Simons ([77]), because it avoids the problematic idea of objects as unscrutable blobs which attributes somehow adhere to. Nevertheless it is also true that objects are more than mere sums of their properties. A descriptively adequate ontology has to account for the completeness, independence, and spatio-temporal bulk that objects enjoy in contrast to arbitrary agglomerations of attributes (Denkel [26], pp. 16–17). Following Strawson [85, pp. 16–17, 39], the basic difference between objects and other entities is that the former can be singled out on their own, while the latter have to be individuated relatively to some object. Objects enjoy ontological priority over other particulars since they constitute a framework of reference that serves as a basis for identi- ﬁcation of all other entities. However, the thesis that objects form the basic framework of reference may seem to be undermined by the fact that objects change. Objects apparently lose and gain parts, move around, and exhibit incompatible properties and relations over time. A solution favoured by many ontologists, e.g. Quine ([72], p. 171), Heller ([50]), and Armstrong ([3], pp. 99–107), is to regard objects as space-time worms: incompatible facts just pertain to different phases of such four-dimensional entities. This approach is elegant, but rejects the intuitive distinction between objects and processes. Alternatively, one can stick to the intuition of objects as three-dimensional entities and temporalise the assertions about objects instead. Formal relations, like parthood, have to receive an additional temporal parameter. This approach has been defended, amongst many others, by Simons ([76], chap. 5), and has been adopted by Masolo et al. ([62]). However, temporalisation makes reasoning about formal relations like parthood more dif- ﬁcult. The problem of change emphasises an ambiguity of the naive concept of object. Vary- ing the terminology of Armstrong ([3], pp. 123–126) and developing intuitions from Si- mons ([77]) and Denkel ([26], p. 108), one has to distinguish between an evanescent whole, the thick object, and a core of enduring characteristics, the thin object. Thick ob- jects have spatio-temporal bulk and undergo change. More precisely: change consists in the succession of temporary aggregations of tropes shaped by relations of spatial connec- tion. Thin objects as the enduring cores of thick objects constitute the ultimate referential framework, the ontological backbone of reality. Successions of thick objects are held to- gether by thin objects common to all elements in these chains, such as for example by bundles of essential functions in the case of artifacts or organisms.

44

Our approach to the problem of change is akin to the stage theory proposed by Sider ([75], pp. 1-10, pp. 188-208), Hawley ([49], chap. 2), and Denkel ([26], pp. 101-109), with the main difference that thick objects are founded on thin objects. Successive incom- patible states of affairs bear on consecutive thick objects that share the same thin object as a common core. The exchange of colour-tropes in a ripening tomato just pertains to different evanescent wholes centered around the bundle of core characteristics, amongst them the tomato’s DNA. That one speaks of the same object through change is grounded in the existence of thin objects. Every temporal attribution of properties and relations to a thin object amounts to the atemporal attribution of these attributes to succeeding thick objects as its stages.

5.2.3 Haecceities, Properties, Guises and Relations

Since a thick object may contain other thick objects as parts, it is necessary to determine whether a trope or a thin object is associated with that thick object or one of its thick parts. For example, one would like to distinguish the weight of a body and the weight of its right arm. Such distinctions can be done through the relation of direct parthood, of which we will say more later. In the words of Williams ([90], p. 6), direct parts are ﬁne or abstract parts, as opposed to gross or concrete parts, of thick objects. A thin object that is a direct part of a thick object is called an haecceity of the latter. A direct part which does not overlap with an haecceity is called a property of the thick object. Every property of a thick object is supposed to be founded or dependent on exactly one haecceity of that thick object. We have said that a thick object has at least one haecceity. It seems counterintuitive that a thick object may have more than one haecceity, but this is the case for most every- day objects such as artifacts (or organisms) and the amount of material they are made of. Common-sense allows for numerically distinct objects to be spatially and temporally co-located, orcoincident, e.g., a terracotta statue and the clay it is made of, or a person and her body. Some ontologists, like Simons ([76], chap. 6), assume such entities to be distinct physical objects of which one (e.g. the clay) constitutes the other (e.g. the statue). In OCHRE, there is no need to allow for constitution as an additional non-extensional composition. Indeed, thick objects cannot be co-located, since they have spatial bulk and thus compete for space. Instead, we consider coincident entities to be direct parts of the same thick object. Thick objects may have more than one essence, each of which has its own periphery of dependent tropes. The mereological sum of a thin object and all the properties founded on it represents a qualitative aspect of the thick object, which we call a guise, after Casta˜neda ([14]). A particular thick object that we identify as a terracotta statue made of clay contains two sub-bundles of tropes, namely the statue and the amount of clay, each centered on a particular thin object: the functions of the artifact and the chemical characteristics of the material. These trope bundles are ﬁne or abstract parts of the same thick object and represent different aspects of the latter.

45

5.2.4 Eventualities

A descriptively adequate ontology has to acknowledge the intuitive distinction between objects and processes, or, as the philosophical jargon has it, between endurants and per- durants. Endurants have no phases and are present as a whole at each instant they are present at all. Perdurants, on the contrary, consist of different phases at different times (Lewis [59, p. 202]). However, taking this distinction for granted does not mean that its terms have both to be considered as primitive. According to the intuitive deﬁnition of endurants, tropes, as well as thin and thick objects, turn out to be endurants. Thin objects are wholly present in each of the thick objects they are part of, and the same trivially applies to tropes, i.e. to atoms. And since thick objects have no temporal parts, they too are endurants. In OCHRE, only a subclass of perdurants is envisaged, namely successions of thick objects and arbitrary sums of such successions, called eventualities. The basic eventualities are events as changes or state-transitions: for example, the change of a tomato’s colour from green to red amounts to the succession of a red tomato- stage to a green one. The change of a memory cell from 0 to 1 is the succession of a charged cell-stage to an uncharged one. The deﬁnition implies that there are no instan- taneous events, which is consistent with the doctrine that perdurants have at least two distinct temporal parts. The instantaneous left and right boundaries of eventualities are endurants, namely thick objects. Hence the events that represent the beginning and the ending of an eventuality cannot be instantaneous and always have to involve at least two object-stages. Eventualities are arbitrary mereological sums of events; they can be recursively char- acterised with single events as a base case. We call process any eventuality which is not a single event or state-transition.

5.3 Basic Relations

Obviously, OCHRE has also to acknowledge formal properties and formal relations that are the subject matter of any foundational ontology, such as object, trope, parthood, de- pendence, or similarity. References to formal properties and relations are made through the respective predicates. Formal relations apply to their relata directly, without any fur- ther mediating ties (Smith and Murray [82], pp. 50-51). This is just a consequence of their being the top-level categories of reality. In other words, the nexus between a formal property and its instances, in particular that between a formal relation and its relata, is ontologically unanalysable.

5.3.1 Parthood

Mereology, the formal theory of parthood, has grown out of early-20th-century mathe- matical research into a calculus of individuals capturing relations between set-theoretical urelemente (Leonard and Goodman [56]). There are several systems of mereology of dif- ferent strength. In OCHRE, we have adopted the so-called Closure Mereology (CM) that amounts to a Boolean algebra without a null element (Simons [76, chap. 1]; Casati and Varzi [12, chap. 3]). More precisely, OCHRE is based on the atomistic version of CM.

46

Parthood between particulars is supposed to be extensionally deﬁned over a domain of least elements, so-called atoms, and closed under the operations of binary sum and prod- uct. The atoms of mereology are all basic non-repeatables, i.e. tropes: the latter are the building blocks of reality. Sameness, i.e. identity between particulars, is conceived of simply as mutual parthood. In other words, parthood is partial identity (Armstrong [3, p. 17] ; Lewis [58, pp. 81–82]). Furthermore, there is a unique parthood relation between particulars, which does not exclude that additional subdomains of individuals (like sets) require the introduction of different concepts of parthood. All in all, this formal account of parthood has the advantage of a clear algebraic approach and a great conceptual unity.

5.3.2 Foundation

Intuitively, foundation can be understood in terms of identiﬁcation: a particular x is founded on an individual y if, and only if, in order to identify x, one has to single out y ﬁrst (Strawson ([85], pp. 16–17). In a certain sense, the entites on which something is founded are part of its very deﬁnition or identity (Fine [31], p. 275). Formally, foundation can be characterised as a reﬂexive and transitive relation which satisﬁes the following conditions (Fine [33, 32]; Simons [76, pp. 310-318]):

1. wholes are founded on their parts;

2. if something is founded on the atomic parts of something else, it is founded on the latter as a whole.

Thin objects, the haecceities of thick objects, are accounted for as bundles of atoms (or tropes) which are self-founded, i.e. founded only on their parts. Every thin object is an integral whole, i.e. a whole whose atomic parts held together by foundation relations. Using a term of Roman Ingarden [53, vol. 1], thin objects are autonomous in the sense that they contain all their determinations, all that is needed to explain them.

5.3.3 Similarity, Exact Similarity, Comparability

Similarity is a reﬂexive, symmetric and intransitive relation deﬁned over atoms (i.e. tropes); it can be conceived of as connection or immediate neighbourhood in a relational “qual- ity space”. Two atoms (tropes) are exactly similar if and only if they are similar to the same tropes. Thus, exact similarity is like qualitative identity, coincidence in a relational “quality space”. Comparability, ﬁnally, is the transitive closure of the similarity relation. These basic relations between tropes can be used to deﬁne resemblance relations between complex particulars. The most interesting case is exact resemblance, which holds be- tween two complex particulars if and only if their atomic parts can be matched together one-to-one in pairs of exactly similar tropes.

5.3.4 Connection and Anteriority

Thick objects are nodes in a comprehensive grid of spatial and temporal relations. The formal ontological theory of spatial and temporal relations is called topology; topology

47

constraints mereology and both together constitute the formal-ontological framework of mereotopology (Casati and Varzi [12, chap. 4]). The ﬁrst primitive of topology is spatial connection, a symmetric and intransitive relation that is reﬂexive in all cases it applies at all. Its underlying intuition is that of immediate neighborhood in space. E.g., France is connected to Germany and Germany to Poland, but France is not connected to Poland. A thick object is enclosed in another if, and only if, everything which is connected to the ﬁrst is also connected to the second. A heart is contained in a chest, a ﬁsh in a lake, and so on. The principle of monotonicity (Casati and Varzi [12, p. 54]) states that parthood between thick objects implies spatial enclosure, but not vice-versa. Since a heart is part of a chest, it is also enclosed in the latter. However, a ﬁsh is enclosed in, but is not part of a lake. Thick objects do not only exhibit spatial relations, but also temporal ones. The theory of temporal order used in OCHRE is the one proposed by Russell [73] and Chisholm [17]: accepting the relation of anteriority qua complete precedence as a primitive, one easily deﬁnes the relations of immediate anteriority and simultaneity. This theory is only weakly axiomatised on purpose: indeed, the question whether thick objects are instantaneous or temporally extended is left undecided. The important issue about thick objects is that they have no temporal parts. This is ensured by the principle of mereo-topological invariance, i.e. the stipulation that connection implies simultaneity. Capturing the intuition behind Chisholm’s account of entia successiva ([16, pp. 97–104]), a three-dimensionalist version of stage theory, this axiom states that thick objects are frozen in time: change consists in the succession of snap-shot like three-dimensional entities. A further important postulate is that coincidence, namely mutual spatial enclosure, implies sameness. In other words: distinct thick objects cannot be co-located, they com- pete for space. Thus there is no need to distinguish between a thick object and the region in which it is located. Indeed, a thick object can be seen as a qualitatively enriched spatio- temporal region. The principle of mereo-topological invariance together with the assumption that non- coincidence yields distinctness, may seem rather strong. In fact, any mereo-topological change implies a change of parts too, by the extensionality of parthood. Now, it is not that counterintuitive that any movement is accompanied by some qualitative change: kinetic energy is transformed into position energy with loss of some kinetic energy in form of heat through friction, the gravitational attraction between physical objects changes, and so on. Hence, the account of change in OCHRE may well be in harmony with a more or less scientiﬁc preconception of the world.

5.3.5 Relational Precedence

Non-repeatable relations (e.g. marriages, or kinships) have been often deﬁned as multiply dependent attributes (Simons [78], Mulligan and Smith [66]). Accordingly, a property of a thick object that is founded on haecceities of other thick objects is called a relational property in OCHRE. Relational properties are material properties in contrast to formal relations like parthood and foundation. (We remind the reader that formal relations are not represented by particulars; they correspond to sets of tuples.) But multiple foundedness is not sufﬁcient to account for relations; the relata stand

48

in a certain order of precedence, which is not simply part of the essence of a relational property, but is a formal relation sui generis. We assume that the relata of a relational prop- erty are strictly ordered by precedence. This means that there are no reﬂexive relational properties. Apparent reﬂexivity of material properties is just a linguistic phenomenon: a predicate may correspond to a disjunction between a material property and sameness. Symmetry occurs on the level of types or classes, in case the relata are always recombined by an exactly similar relational property with reverse order of precedence.

5.4 Derived Relations

5.4.1 Direct Parthood

Traditionally, the peculiar formal relation between objects and their characteristics has been called inherence and the authors of DOLCE follow this usage (Masolo et al. [62]). In

OCHRE, however, it is not necessary to provide for inherence as an additional primitive; in fact, the relation between (thin or thick) objects and their attributes can be accounted for in terms of foundation and parthood. A part of a thick object which is not itself a thick object is called a thin part. A thin part which does not overlap with any of the (proper) thick parts of a thick object is called a direct part. We have already mentioned how the concept of haecceity and that of property can be deﬁned using direct parthood. Every atom (trope) is a direct part of some thick object. In other words, there are no homeless tropes. Furthermore, no two comparable tropes may be both direct parts of the same thick object. Thus a physical object-stage cannot have more than one mass or kinetic energy. Also, every thick object has to contain at least one haecceity: as we have seen, many thick objects have more than one haecceity. Finally every property is founded on exactly one haecceity of the same thick object. Since haecceities qua thin objects are self-founded, properties are one-sidedly founded on haecceities.

5.4.2 Succession

Successive thick objects that are stages of the same thin object stand in a peculiar relation of loose identity: they are not identical, but everything that is true of them is also true, in a temporal sense, of the common thin object. This idea of stage-successions is directly related to Chisholm’s [16, pp. 97–104] account of change in terms of consecutive entities. We say that a thick object x is the successor of some thick object y with respect to a thin object z iff y is immediately anterior to x, and z is a common haecceity of x and y. In order to exclude that thin objects have instantaneous lives, we postulate that for each thin object x there are at least two thick objects that are in succession with respect to x. By extensionality of parthood, there must be at least one atomic part that is not shared between distinct stages of a thin object. Hence there cannot be successive stages with exactly the same proper parts: things change constantly.

49

5.4.3 Participation

In DOLCE, the relation between perdurants and the (thin) objects involved in them is called participation and considered to be a primitive. OCHRE’s particular account of perdurants in terms of endurants allows for participation to be deﬁned as a special case of parthood. Indeed, a thin object x participates in a eventuality y, if and only if there is an event which is part of y, such that x is the common haecceity of the succeeding thick objects that constitute this event.

50

6 OCHRE’s Formal Characterization

6.1 Mereology - Theory of Parts and Wholes

6.1.1 Deﬁnitions of Mereology

(Do1) SA(x,y) ≜P(x,y)∧P(y,x) (sameness)

(Do2) PP(x,y) ≜P(x,y)∧¬SA(x,y) (proper parthood)

(Do3) O(x,y) ≜∃z(P(z,x)∧P(z,y)) (overlap)

(Do4) U(x,y) ≜∃z(P(x,z)∧P(y,z)) (underlap)

(Do5) At(x) ≜PT(x)∧¬∃y(PP(y,x)) (atom)

(Do6) AtP(x,y) ≜P(x,y)∧At(x) (atomic parthood)

(Do7) Cx(x) ≜PT(x)∧¬At(x) (complex)

(Do8) SM(x,y,z) ≜∀w(P(w,x) ↔(P(w,y)∨P(w,z))) (sum)

(Do9) PR(x,y,z) ≜∀w(P(w,x) ↔(P(w,y)∧P(w,z))) (product)

(Do10) DF(x,y,z) ≜∀w(P(w,x) ↔(P(w,y)∧¬O(w,z))) (difference)

(Do11) UN(x) ≜∀y(P(y,x)) (universe)

6.1.2 Axioms of Mereology

(Ao1) P(x,y) →(PT(x)∧PT(y)) (parthood)

(Ao2) PT(x) →P(x,x) (reﬂexivity)

(Ao3) ((P(x,y)∧P(y,z)) →P(x,z) (transitivity)

(Ao4) SA(x,y) ↔(PT(x)∧PT(y)∧x = y) (sameness is particular-identity)

(Ao5) ∃y(AtP(y,x)) (atomicity)

(Ao6) (PT(x)∧PT(y)∧∀z(AtP(z,x) →AtP(z,y)) →P(x,y) (extensionality)

(Ao7) U(x,y) →∃z(SM(z,x,y)) (existence of sum)

(Ao8) (SM(x,z,w)∧SM(y,z,w)) →SA(x,y) (uniqueness of sum)

(Ao9) O(x,y) →∃z(PR(z,x,y)) (existence of product)

(Ao10) (PR(x,z,w)∧PR(y,z,w)) →SA(x,y) (uniqueness of product)

(Ao11) ∃x(UN(x)) (existence of universe)

(Ao12) (UN(x)∧UN(y)) →SA(x,y) (uniqueness of universe)

6.2 Theory of Foundations

6.2.1 Deﬁnitions of the Theory of Foundations

(Do12) SF(x,y) ≜F(x,y)∧¬P(y,x) (strong foundation)

(Do13) OF(x,y) ≜F(x,y)∧¬F(y,x) (one-sided foundation)

51

(Do14) MF(x,y) ≜F(x,y)∧F(y,x) (mutual foundation)

(Do15) TH(x) ≜Cx(x)∧∀y(F(x,y) →P(y,x)) (thin object)

(Do16) IW(x) ≜Cx(x)∧∀y,z((AtP(y,x)∧AtP(z,x)) →(F(y,z)∨F(z,y))) (integral whole)

6.2.2 Axioms of the Theory of Foundations

(Ao13) F(x,y) →(PT(x)∧PT(y)) (restriction)

(Ao14) PT(x) →F(x,x) (reﬂexivity)

(Ao15) (F(x,y)∧F(y,z)) →F(x,z) (transitivity)

(Ao16) P(y,x) →F(x,y) (wholes are founded on their parts)

(Ao17) (AtP(z,y) →F(x,z)) →F(x,y) (foundation on a whole)

(Ao18) ∃x(TH(x)) (existence of thin objects)

(Ao19) TH(x) →IW(x) (thin objects are integral wholes)

6.3 Theory of Similarity

6.3.1 Deﬁnitions of the Theory of Similarity

(Do17) ES(x,y) ≜∀z(SI(x,z) ↔SI(y,z)) (exact similarity)

(Do18) RS(x,y) ≜Cx(x)∧Cx(y)∧∃z,w(AtP(z,x)∧AtP(w,y)∧ES(z,w)) (resemblance)

(Do19) CR(x,y) ≜Cx(x)∧Cx(y)∧∀z(AtP(z,x) →∃w(AtP(w,y)∧ES(z,w))) (complete resemblance)

(Do20) ER(x,y) ≜CR(x,y)∧CR(y,x) (exact resemblance)

6.3.2 Axioms of the Theory of Similarity

(Ao20) SI(x,y) →(At(x)∧At(y)) (similarity)

(Ao21) At(x) →SI(x,x) (reﬂexivity)

(Ao22) SI(x,y) →SI(y,x) (symmetry)

(Ao23) CM(x,y) →(At(x)∧At(y)) (comparability)

(Ao24) CM(x,y) →CM(y,x) (symmetry)

(Ao25) (CM(x,y)∧CM(y,z)) →CM(x,z) (transitivity)

(Ao26) SI(x,y) →CM(y,x) (similarity implies comparability)

52

6.4 Topology - Theory of Space and Time

6.4.1 Deﬁnitions of Topology

(Do21) TK(x) ≜∃y(C(x,y)) (thick object)

(Do22) TKP(x,y) ≜TK(x)∧TK(y)∧P(x,y) (thick parthood)

(Do23) E(x,y) ≜∀z(C(z,x) →C(z,y)) (enclosure)

(Do24) CI(x,y) ≜E(x,y)∧E(y,x) (coincidence)

(Do25) IA(x,y) ≜A(x,y)∧¬∃z(A(x,z)∧A(z,y)) (immediate anteriority)

(Do26) TO(x,y) ≜¬A(x,z)∧¬A(y,x) (temporal overlap)

(Do27) SL(x,y) ≜∀z(TO(x,z) ↔TO(y,z)) (simultaneity)

6.4.2 Axioms of Topology

(Ao27) C(x,y) →(Cx(x)∧Cx(y)∧¬TH(x)∧¬TH(y))) (connection)

(Ao28) TK(x) →C(x,x) (reﬂexivity)

(Ao29) C(x,y) →C(y,x) (symmetry)

(Ao30) A(x,y) →(TK(x)∧TK(y)) (anteriority)

(Ao31) ¬A(x,x) (irreﬂexivity)

(Ao32) (A(x,y)∧A(y,z)) →A(x,z) (transitivity)

(Ao33) TK(x) →∃y(A(x,y)∨A(y,x)) (temporal order)

(Ao34) ∃x(TK(x)) (existence of thick objects)

(Ao35) C(x,y) →SL(x,y) (mereo-topological invariance)

(Ao36) TKP(x,y) →E(x,y) (monotonicity)

(Ao37) (TK(x)∧TK(y)∧CI(x,y)) →x = y (extensionality)

6.5 Theory of Properties

6.5.1 Deﬁnitions of the Theory of Properties

(Do28) THP(x,y) ≜P(x,y)∧TK(y)∧¬TK(x) (thin parthood)

(Do29) DP(x,y) ≜THP(x,y)∧¬∃z(THP(z,y)∧¬z = y∧O(z,x) (direct parthood)

(Do30) H(x,y) ≜TH(x)∧DP(x,y) (haecceity)

(Do31) Prop(x,y) ≜DP(x,y)∧∀z(H(z,y) →¬O(z,x)) (property)

(Do32) IProp(x,y) ≜Prop(x,y)∧IW(x) (integral property)

(Do33) G(x,y,z) ≜DP(x,y)∧H(z,y)∧∀w(P(w,x) ↔(w = z∨(Prop(w,y)∧F(w,z)))) (guise)

53

6.5.2 Axioms of the Theory of Properties

(Ao38) At(x) →∃y(DP(x,y)) (tropes are direct parts of thick objects)

(Ao39) (DP(y,x)∧DP(z,x)∧CM(y,z)) →SA(y,z) (comparable direct parts)

(Ao40) TK(x) →∃y(H(y,x)) (existence of haecceities)

(Ao41) (H(x,y)∧H(x,z)∧SL(y,z)) →SA(y,z) (unicity of simultaneous stages)

(Ao42) Prop(x,y) →∃z(H(z,y)∧F(x,z)) (property foundation: 1)

(Ao43) (Prop(x,y)∧H(z,y)∧H(w,y)∧F(x,z)∧F(x,w)) →SA(z,w) (prop. found.: 2)

6.5.3 Theorems of the Theory of Properties

(To1) (G(x,y,z)∧G(x′,y,z)) →SA(x,x′)

6.6 Theory of Eventualities

6.6.1 Deﬁnitions of the Theory of Eventualities

(Do34) SC(x,y,z) ≜IA(y,x)∧H(z,x)∧H(z,y) (succession)

(Do35) EV(x,y) ≜∃w,z(SM(x,w,z)∧SC(y,w,z)) (event in)

(Do36) E(x) ≜∃y(EV(x,y)) (event)

(Do37) PRO(x) ≜ETY(x)∧¬E(x) (process)

(Do38) lf(x,y) ≜ETY(x)∧TH(y)∧∀z(P(z,x) ↔EV(z,y)) (life)

(Do39) PC(x,y) ≜TH(x)∧ETY(y)∧∃z(EV(z,x)∧P(z,y)) (participation)

6.6.2 Axioms of the Theory of Eventualities

(Ao44) (SC(z,x,y)∧SC(w,x,y)) →z = w (unicity on the left)

(Ao45) (SC(x,y,z)∧SC(x,y,w)) →z = w (unicity on the right)

(Ao46) TH(x) →∃y,z(TK(y)∧TK(z)∧SC(y,z,x)) (thin objects as haecceities)

(Ao47) E(x) →ETY(x) (eventuality: 1)

(Ao48) (E(x)∧ETY(y)∧SM(z,x,y)) →ETY(z) (eventuality: 2)

6.7 Theory of Relational Properties

6.7.1 Deﬁnitions of the Theory of Relational Properties

(Do40) RPO(x,y) ≜Prop(x,y)∧∃z,w(H(z,w)∧¬H(z,y)∧¬w = y∧F(x,z))

(Do41) RL(x,y) ≜∃z(RPO(y,z)∧∃w(H(x,w)∧F(y,x))) (relatum)

54

6.7.2 Axioms of the Theory of Relational Properties

(Ao49) PC(x,y,z) →(RL(x,z)∧RL(y,z)) (precedence)

(Ao50) ¬PC(x,x,y) (irreﬂexivity)

(Ao51) (PC(x,y,w)∧PC(y,z,w)) →PC(x,z,w) (transitivity)

(Ao52) (RL(x,z)∧RL(y,z)) →(PC(x,y,z)∨PC(y,x,z)) (order of precedence)

55

7 BFO: Basic Formal Ontology

BFO is the third module of the WonderWeb Ontology. It has been developed at the IFOMIS institute in Leipzig.

7.1 Introduction and preliminaries

BFO is a foundational ontology that aims at reconciling the so-called three-dimensionalist and four-dimensionalist views (a bi-ontological theory, so to speak). Such a theory can however be stripped down of its meta-ontological ﬂavor. The result is the underling bi- categorial ontology, which is in essence a form of non-eliminativistic three dimension- alism. Generally speaking, continuants are here seen as persisting entities that are self- identical through time and that participate in occurrents of various sorts. The treatment of three dimensional entities ﬁnds its roots in a neo-Aristotelian metaphysics of substances [80]. Although the differences and similarities between BFO and DOLCE will be discussed in a later section, it is instructive to anticipate a few remarks on the baroque attitude of

BFO’s theory of universals and the modal realism of DOLCE. These remarks will drive the ﬁrst part of our presentation.

7.1.1 Universals

At the present stage, BFO adopts the structural vocabulary introduced for the characteri- zation of DOLCE as it concerns universals, without fussing about the modal interpretation. In particular, we present BFO as an ontology of particulars and add glosses on a num- ber of predicates that corresponds to formal universals recognized by BFO. The BFO’s native formal approach consists in introducing nominals for so-called gen- uine formal universals; using the instantiation relation for monadic universals (properties as they are called by most people) and some relational variant for the other universals.

7.1.2 Temporality

BFO has two components. A Snap ontology of endurants which is reproduced at each moment of time and is used to characterize static views of the world. This view is moti- vated by an underlying presentist metaphysics of time (if something exists, it exists at the present time). No temporal consideration is germane to the Snap ontology in this very elementary sense. Snap requires a temporal logic of a certain grade if we want to use it in temporal contexts. There are two devices in BFO in order to handle temporality. The ﬁrst one –probably not the most manageable one– consists in using diachronic relations, which hold between entities in temporally-different Snap views. This allows us to account for a large number of features, but it does not furnish an ontology of temporal entities in itself. Rather, and this is the second device of BFO, the theory contains a temporal component: the Span ontology. This is an ontology of happenings and occurrents and, more generally, of entities which persist in time by perduring (these are entities which have temporal

56

parts). Trans-ontological Snap considerations provide a useful device for characterizing Span entities. Indeed, an entity across different Snap instances corresponds to changes in a Snap entity. For example, a movement is a change in location, a discoloration is a change in the color trope of a material object, and so on. The interdependency and complementarity of the Snap and Span components is BFO’s message in a nutshell. In the bi-categorial context, we disregard meta-ontological devices (ontologies, the relation of being a constituent of an ontology, and the like), thus the predicates of BFO re- ceive an additional temporal parameter, namely, the moment or period of time at (during) which they obtain. This brings the formal characterization close to that of DOLCE since the latter introduces both non temporally qualiﬁed and temporally qualiﬁed predicates – although not quite for the same reasons. One drawback, as far as BFO is concerned, might be that certain categorial – or pseudo- categorial as argued in (Grenon, 2003b) –claims will be temporally qualiﬁed as well. This relates to DOLCE’s treatment of universals according to which a category includes all its possibilia as members. BFO differs on this aspect; categories have a number of instances at a time in the Snap case and they encompass all of their actual (past, present, future) instances in the Span case. In this regard, note that at the moment the list of rigid categories in BFO is not deﬁnite. Nonetheless, it is remarkable that the parameterization of certain statements of categorial membership is primarily related to granularity (and not to time).

7.1.3 Granularity

Snap ontologies are allegedly sensitive to the level of granularity at which their con- stituents are revealed. It is in this spirit that, taking account of the granularity paradigm, the categories of substance and aggregate of substances are relative to an ontology (we should better talk of pseudo-categories for this very reason). A number of reservations concerning this paradigm can be raised. Nevertheless, note that the actual characteriza- tion falls short of doing justice to the underling intuitions. A possible way out could be to introduce granularity parameters on a par with temporal parameters. However, this is inadequate from the realist standpoint of BFO (what are these parameters? in the temporal case the answer is simple: they are temporal regions). Perhaps, on this issue it is advisable to follow the formal treatment of granularity used in CYC. After this preliminary discussion, in the following pages we sketch the BFO theory. A more convoluted explication and justiﬁcation of the formalization can be found in [41]. Here, we draw attention to some salient similarities (with certain qualiﬁcations) and dis- similarities between BFO and DOLCE.

7.2 BFO in a nutshell

The entities considered here are all particulars. Particulars are either endurants (Snap) or perdurants (Span).

57

7.2.1 Snap

Snap entities are most importantly divided into substantial entities (which are the bearer of properties and change, e.g., material objects, organs, portions of the atmosphere, but also organisations and other agents), tropes (which are the latter’s qualities, functions, powers, dispositions, and other entities inhering in substantial entities, e.g., headaches, colour of a tomato, temperature of a body, tendency toward decomposition of the tomato, contracts –a document on which is written a contract is itself a substantial entity), and spatial regions (which are pure space regions). Here, we do not treat the so-called ‘quasi entities’, although the absence of a formal distinction does not prevent BFO to take these under its scope. The category of substantial entities is the most direct indicator of the neo-Aristotelian stand that BFO is committed to. In the world, these are entities that preserve their iden- tity through time, are subjected to (more or less continuous) change, and are the bearers of a number of qualities and assimilated entities. Among substantial entities, the salient category is that of maximally strongly connected substantial entities with bona ﬁde bound- aries, e.g., a body, a tomato, a ball and so on. Qualities and assimilated –Snap dependent entities or tropes– are particular entities (the instances of property universals) that depend for their existence on substantial enti- ties. The colour of this tomato depends on this tomato and it is no other entity’s colour. Another tomato may have a colour-trope of the exact same hue, etc. Colours of tomatoes may be qualitatively identical, they are as numerically distinct one from the other as their respective bearers are numerically distinct one from the other. Tropes are of various kinds which are best distinguished on modal basis although we do not introduce this aspect in the formalization. Among the relevant sub-kind of tropes we ﬁnd: states or conditions, functions, powers, dispositions, and liabilities.31 Tropes are divided in monadic (depen- dent upon a single entity, e.g., colours) and polyadic or relational (dependent upon more than one entity, e.g., contracts). The relation between a trope and its bearer is called inher- ence (this is a relation between particulars) which is also a form of speciﬁc dependence. The metaphysic of space is substantivalist in the sense that spatial regions are entities in their own right. These are distinct from substantial entities and may be the location of substantial entities as well as of tropes (in ﬁrst approximation, a trope of a substance is co-located with its bearer). We assume that spatial regions are (exactly) located at themselves. On the contrary, substantial entities – and their tropes – may be located at different regions at different times. However, at any time at which they exist they have a single spatial location. We leave open whether at each time a spatial region needs to be the location of a substantial entity (BFO supports both variants). Also, the present formalization remains agnostic as concerns cross-categorial sums of Snap entities. Rather, the existence of sums of two entities within each of the three mean species of Snap entities is explicitly introduced. Characteristically, sums remain in these species (cumulativity closure) and their parts as well (dissectivity closure). Snap entities are said to exist at a time. Indeed they may exist (and usually exist) at more than one time. Their existence needs to be continuous (a property left out in the present formalization). It is open, however, whether there are instantaneous Snap entities.

31At this level BFO does not draw a sharp distinction between the physical and the social.

58

As already mentioned, Snap is in itself not sensitive to time. Inherence, spatial loca- tion and other spatial relations are forms of co-existence. An interesting and genuinely diachronic relation that one could add to BFO is the genidentity relation (the such-as-to- have-come-forth-from relation). For example, this cake on the table is genidentical to the mereological sum of all pieces of cakes in the plates of the participants of the upcoming diner.

7.2.2 Span

Span entities are divided mainly into processual entities (which are happenings or occur- ring entities, changes of various kinds in substantial entities, e.g., raising of temperature, acquisition of a social status, movements, activities, etc.), temporal regions (the whole of time and all of its parts), and spatio-temporal regions (four dimensional regions of space- time, i.e., the whole locational substratum for occurrents its parts). These sub-kinds of Span entities are disjoint. Like spatial regions, temporal regions are not parts of space- time. It is remarkable that there is nothing analogous to tropes (Snap dependent entities) in Span, that is, there are no entities that are qualities of processes. Analogously to the case of substantial entities, processual entities are divided accord- ing to their topological properties. Processes are the self-connected processuals. For instance, baking a cake, falling down, scratching your nose are processes. More gen- erally, processuals have a temporal and a spatiotemporal extent and do not change their locations in time or space-time. Time is given entirely in a canonical Span ontology, BFO takes the whole of time to be an entity in its own right and any of its parts is a temporal region (these can be extended or instantaneous). Similarly, space-time is an entity in BFO and its parts are the spatio- temporal regions (these may be of various dimensions). Inforamlly, BFO regards time as a continuum, in the spirit of [8], and space-time as a four-dimensional manifold. Temporal and spatio-temporal regions are substrata of locations for every Span entity (and for Span entities only! Recall that Snap entities are considered to exist in time, not to be located in it). A regions is located in itself in the corresponding dimension and every Span entity has a unique location both in time and space-time (as already observed for processes). The existence of cross-categorial sums among Span entities is left open, while the existence of sums of two entities within the sub-kinds of Span entities is explicitly in- troduced. Sums remain in these species (cumulativity closure) and their parts as well (dissectivity closure). Span entities are perdurants, thus they have temporal parts. A temporal slice is a temporal part located at an instant of time. Temporal parts are more generally spatio- temporal parts, those which are carved up only in the temporal dimension. They are sometimes called phases. Processual entities are said to occur at a time when they have a temporal slice which is located at this time.

7.2.3 Snap–Span and Span–Snap

Although in the meta-ontological framework the relation between a snap entity and a moment of time at which it exists is deﬁnable, here it is taken as a primitive relation. From

59

this, we may deﬁne existence during a period of time (a quite weak notion). We can then proceed by adding a temporal argument to spatial location and inherence. For instance, Wojtyla exists now, it has been existing all throughout 2003, because at any instant of time during that year, Wojtyla was existing. During that year (at each and every instant), his papehood was inhering in him and he has been located at many spatial locations. Additional native primitive terms of BFO are non-temporalized predicates for the re- lation of participation and realization (they obtain at a given moment of time). In this context, we can introduce participation in relation to an extended processual which has to occur at the time at which its participants exist and during which the more basic syn- chronic relation obtains. Wojtyla realises his papehood when he acts according to his status. He participates in many other processual entities which have nothing to do with his papehood. Additional variants, such as the complete participation (when an entity participates to the whole of the processual in question) can be deﬁned. The life of a substantial is the sum of the processual entities it is a complete participant of. In many cases, the realization of a trope is just a part of its own life. Here we assume this is also part of the life of its bearer. Other forms of participation, beside realization, could be added but their conditions are not easily stated (think of intentional relations). On the other hand, it is difﬁcult to deﬁne the notion of life for tropes, since in many cases tropes exist without being realized, and it is unclear the relationship between the life of a trope and that of its bearer. It may be useful to introduce two categories of tropes: those who have realizations as proper parts of their life (e.g., functions) and those whose lives coincide with their realization (an example could be a condition or a state). Of course, one can go on deﬁning a number of sub-kinds of processuals, for instance functionings (the processes in which a function is realized – assuming that no single function is realized as a disconnected processual entity).

60

8 Formal Characterization of BFO

In keeping with the modular framework of BFO, following [41] I take Snap and Span entities as primitive notions. We can always introduce the term ‘Entity’ as applying to entities of any of the kinds used here. Since this is only a partial rendition of BFO (most importantly not including universals), I leave it open whether Snap and Span form parti- tions of this putative Entity, i.e., whether there are any other kinds of entities. Here, the instances of Snap and Span are all particulars.

(Ab1) DJ(Snap,Span)

(Ab2) PT(Span,PRS,TR,STR)

(Ab3) PT(Snap,SR,SBL,TRP)

8.1 Span Entities

Material in this section is based on or adapted from [41, 43].

Primitives relations and constants. On Span entities we assume the following primi- tives:

• Parthood: P(x,y) means that x is a part of y.

• Boundary For: B(x,y) means that x is a bona ﬁde boundary for y; x is not neces- sarily the whole boundary of y, but any part of it (contrast with Boundary Of to be deﬁned). A bona ﬁde boundary for an entity is to be understood as a partial external delineation of that entity. Boundaries are lower dimensional entities (e.g., a section of a sphere is a boundary for a ball; a section of a circle is one for a disk; a point for a line). Bona ﬁde boundaries are not all parts of the entities they bound, this is the case for closed entities (it is deﬁnitional for them)

• Fiat Boundary For: FB(x,y) means that x is a ﬁat boundary for y; FB is the ﬁat counterpart of B. Fiat boundaries are parts of the entities they are ﬁat boundaries for. A ﬁat boundary is for instance the delineation between two component parts of an entity (they are typically regarded as the products of convention).

• Speciﬁc Dependence: SD(x,y) means that x is speciﬁcally dependent on y. Speciﬁc dependence is deﬁned by (Smith, 1997) modally and SD(x,y) means that x and y do not overlap and x is such that it necessitates the existence of y in order to exist. Notice in particular that speciﬁc dependence is then not a form of parthood. Here, without a modal language, I am taking dependence as primitive.

• Time: the constant time designates an individual: the whole of time.

• Temporal Location: LT(x,t) means that t is the temporal region at which x is (uniquely) located. (It is exact temporal location.)

• Space-time: The term spacetime designates an individual: the whole of space-time.

• Spatio-temporal Location: LST(x,st) means that st is the spatio-temporal region at which x is (uniquely) located. (It is exact spatio-temporal location.)

61

8.1.1 Parthood

Material in this section is based on or adapted from [76, 80, 83].

Deﬁnitions. We introduce the classical mereological deﬁnitions.

(Db1) PP(x,y) ≜P(x,y)∧¬P(y,x)) (Proper Part)

(Db2) O(x,y) ≜∃z(P(z,x)∧P(z,y)) (Overlap)

(Db3) FUS(y,x[φ(x)]) ≜∀z(O(z,y) ↔∃w(φ(w)∧O(z,w))) (Fusion)

(Db4) SM(x,y,z) ≜FUS(x,w[P(w,y)∨P(w,z)]) (Sum)

(Db5) DF(x,y,z) ≜FUS(x,w[P(w,y)∧¬O(w,z)]) (Difference)

(Db6) CMP(x,y) ≜FUS(x,z[¬O(z,y)]) (Complement)

Axioms

(Ab4) P(x,y) →(Span(x)∧Span(x))

(Ab5) (P(x,y)∧TR(y)) →TR(x)

(Ab6) (P(x,y)∧STR(y)) →STR(x)

(Ab7) (P(x,y)∧PRS(y)) →PRS(y)

(Ab8) Span(x) →P(x,x)

(Ab9) (P(x,y)∧P(y,z)) →P(x,z)

(Ab10) (P(x,y)∧P(y,x)) →x = y

(Ab11) (FUS(y,x[φ(x)])∧FUS(y′,x[φ(x)])) →y = y′

(Ab12) (TR(x)∧TR(y)) →∃z(SM(z,x,y))

(Ab13) (STR(x)∧STR(y)) →∃z(SM(z,x,y))

(Ab14) (PRS(x)∧PRS(y)) →∃z(SM(z,x,y))

(Ab15) (TR(x)∧TR(y)∧SM(z,x,y)) →TR(z)

(Ab16) (STR(x)∧STR(y)∧SM(z,x,y)) →STR(z)

(Ab17) (PRS(x)∧PRS(y)∧SM(z,x,y)) →PRS(z)

8.1.2 Topology

Material in this section is based on or adapted from [81, 83]

Deﬁnitions

• Internal Part: IP(x,y) means that x is a part of y and no boundary for (B) x overlaps with y.

• Fiat Internal Part: FIP(x,y) means that x is a ﬁat part of y.

• Boundary: Bd(x) means that x is a boundary of an entity (at least one).

62

• Fiat Boundary: FBd(x) means that x is a ﬁat boundary of some entity.

• Boundary Of: BO(x,y) means that x is the complete (bona ﬁde) boundary of y. The boundary of an entity is the fusion of all entities which are (bona ﬁde) boundaries for this entity. The boundary of an entity is therefore a boundary for (B(x,y)) that entity.

• Fiat Boundary Of: FBO(x,y) as in the case of BO(x,y).

• Closure: CL(x,y) means that x is the closure of y. The closure of an entity is the sum of this entity with its boundary.

• Interior: INT(x,y) means that x is the interior of y. The interior of an entity is the difference between this entity and its closure.

• Weak Connected: WC(x) means that x is weakly connected, i.e., x is such that any two entities it is the sum of are such that their closures overlap. This is [83]’s Connected.

• Mildly Connected: MC(x) means that x is mildly connected, i.e., x is such that any two entities it is the sum of are such that one overlaps with the closure of the other or vice versa. This is [83]’s Connected*.

• Strongly Connected: SC(x) means that x is strongly connected, i.e., its interior is mildly connected.

• Connection: C(x,y) means that x is connected to y, i.e., x and y overlap or x overlaps with the closure of y or y overlaps with the closure of x.

• External Connection: EC(x,y) means that x is connected to y but they do not over- lap.

• Closed: CLS(x) means that x is closed, i.e., it is its own closure. A bona ﬁde boundary - in particular, the boundary of this entity - for closed entity is a part of this entity.

(Db7) IP(x,y) ≜P(x,y)∧∀z(B(z,y) →¬O(z,x)) (Internal Parthood)

(Db8) FIP(x,y) ≜P(x,y)∧∀z(FB(z,y) →¬O(x,y)) (Fiat Internal Parthood)

(Db9) Bd(x) ≜∃yB(x,y) (Boundary)

(Db10) FBd(x) ≜∃yFB(x,y) (Fiat Boundary)

(Db11) BO(x,y) ≜FUS(x,z[B(z,y)]) (Boundary Of)

(Db12) FBO(x,y) ≜FUS(x,z[FB(z,y)]) (Fiat Boundary Of)

(Db13) CL(x,y) ≜∀z(BO(z,x) →SM(x,y,z)) (Closure)

(Db14) INT(x,y) ≜∀z(CL(z,y) →DF(x,y,z)) (Interior)

(Db15) WC(x) ≜∀y,z,cy,cz((SM(x,y,z)∧CL(cy,y)∧CL(cz,z)) →O(cy,cz)) (Weak Connected)

(Db16) MC(x) ≜∀y,z,cy,cz((SM(x,y,z)∧CL(cy,y)∧CL(cz,z)) →(O(cy,z)∨O(cz,y)) (Mild Connected)

(Db17) SC(x) ≜∀y(INT(y,x) →MC(y)) (Strong Connected)

63

(Db18) C(x,y) ≜O(x,y)∨∀cx,cy((CL(cx,x)∧CL(cy,y)) →(O(cx,y)∨O(cy,x)) (Connection)

(Db19) EC(x,y) ≜C(x,y)∧¬O(x,y) (External Connection)

(Db20) CLS(x) ≜CL(x,x) (Closed)

Axioms

(Ab18) B(x,y) →(Span(x)∧Span(y))

(Ab19) (B(x,y)∧TR(y)) →TR(x)

(Ab20) (B(x,y)∧STR(y)) →STR(x)

(Ab21) (B(x,y)∧PRS(y)) →PRS(y)

(Ab22) (P(x,y)∧B(y,z)) →B(x,z)

(Ab23) FB(x,y) →P(x,y)

(Ab24) (P(x,y)∧FB(y,z)) →FB(x,z)

(Ab25) CL(x,y) →P(y,x)

(Ab26) (CL(x,y)∧CL(z,x)) →P(z,x)

(Ab27) (SM(x,y,z)∧CL(cx,x)∧CL(cy,y)∧CL(cz,z)∧SM(x′,cy,cz)) →cx = x′

(Ab28) (SM(x,y,z)∧SC(x)) →FC(y,z)

(Ab29) (Bd(x)∧FCn(x)) →∃y,z(FCn(y)∧B(x,y)∧IP(z,y))

Theorems

(Tb1) BO(x,y) →B(x,y)

(Tb2) (CLS(x)∧B(y,x)) →P(y,x)

The following are held to be theorem by [83]:

(Tb3) (B(x,y)∧B(y,z)) →B(x,z)

(Tb4) (B(x,y)∧CMP(z,y)) →B(x,z)

(Tb5) ¬(EC(x,y)∧CLS(x)∧CLS(y))

(Tb6) (FB(x,y)∧FB(y,z)) →FB(x,z)

8.1.3 Dependence

Material in this section is based on or adapted from [80, 81].

Deﬁnitions

(Db21) MSD(x,y) ≜SD(x,y)∧SD(y,x) (Mutual Speciﬁc Dependence)

(Db22) OSD(x,y) ≜SD(x,y)∧¬SD(y,x) (One-side Speciﬁc Dependence)

64

Axioms

(Ab30) SD(x,y) →(Span(x)∧Span(y))

(Ab31) SD(x,y) →¬O(x,y)

8.1.4 Time and Space-time

Deﬁnitions

• Temporal Region: TR(x) means that x is a region of time, i.e. a part of time which may be extended or instantaneous (a time instant), connected to various degrees or scattered.

• Temporal Instant: TI(x) means that x is an instant of time, i.e. a maximally strongly connected boundary of a temporal region.

• Spatio-temporal Region: STR(x) means that x is a region of space-time, i.e. a part of space-time.

(Db23) TR(x) ≜P(x,time) (Temporal Region)

(Db24) TI(x) ≜∃y(TR(y)∧B(x,y)∧SC(x)∧∀z((B(z,y)∧SC(z)) →x = z)) (Temporal Instant)

(Db25) STR(x) ≜P(x,spacetime) (Spatio-temporal Region)

Axioms

(Ab32) Span(time)

(Ab33) Span(spacetime)

(Ab34) SD(spacetime,time)

8.1.5 Temporal Location

Deﬁnitions

• Temporal Location at an Instant: ILT(x,t) means that x is temporally located at t and that t is an instant of time.

• Temporal Co-location: CoLT(x,y) means that x and y are located at the same tem- poral region.

• Temporal Subsumption: SbLT(x,y) means that x temporally subsumes y, i.e., the temporal location of y is a part of the temporal location of x.

• Temporal Part: TP(x,y) means that x is a temporal part of y, i.e., x is a part of y such that all parts of y temporally co-located with x are parts of x. (It is trivial to introduce a ternary relation indicating the time of location of x).

• Temporal Slice: TS(x,y) means that x is a temporal slice of y, i.e., x is an instanta- neous temporal part of y.

65

• Processual: PRS(x) means that x is a processual, i.e., an happening, an occurrent (not a temporal or spatiotemporal region).

• Process: PRO(x) means that x is a process, i.e., a maximally strongly connected occurrent (processual).

• Event: EV(x) means that x is an event, i.e., a temporal slice of a processual.

• Bona Fide Event: BFEV(x) means that x is a bona ﬁde event, i.e., a maximally strongly connected boundary of an occurrent.

(Db26) ILT(x,t) ≜(LT(x,t)∧TI(t)) (Temporal Location at a Instant)

(Db27) CoLT(x,y) ≜∃t(LT(x,t)∧LT(y,t)) (Temporal Co-localization)

(Db28) SbLT(x,y) ≜∀tx,ty((LT(x,tx)∧LT(y,ty)) →P(ty,tx)) (Temporal Subsumption)

(Db29) TP(x,y) ≜P(x,y)∧∀z((P(z,y)∧CoLT(z,x)) →P(z,x)) (Temporal Part)

(Db30) TS(x,y) ≜TP(x,y)∧∃t(ILT(x,t)) (Temporal Slice)

(Db31) OCC(x,t) ≜¬TR(x)∧¬STR(x)∧∃y(TS(y,x)∧ILT(y,t)) (Occurrence at an instant)

(Db32) PRS(x) ≜∃t(OCC(x,t)) (Processual)

(Db33) PRO(x) ≜PRS(x)∧SC(x)∧∀y((P(x,y)∧SC(y)) →x = y) (Process)

(Db34) EV(x) ≜∃y(PRS(y)∧TS(x,y)) (Event)

(Db35) BFEV(x) ≜∃y(PRS(y)∧TS(x,y)∧B(x,y)) (Bona-ﬁde Event)

Axioms

(Ab35) LT(x,t) →(Span(x)∧TR(t))

(Ab36) (LT(x,t)∧LT(x,t′)) →t = t′

(Ab37) Span(x) →∃t(LT(x,t))

(Ab38) Span(x) →∃y(TP(y,x))

(Ab39) TR(t) →LT(t,t)

(Ab40) LT(spacetime,time)

(Ab41) (PRO(x)∧PRO(y)∧P(x,y)) →x = y

Theorems

(Tb7) TP(x,y) →SbLT(y,x)

8.1.6 Spatio-Temporal Location

Deﬁnitions

• Spatio-temporal Part: STP(x,y) means that x is a spatio-temporal part of y, i.e., x is a part of y such that all parts of y spatiotemporally co-located with x are parts of x.

66

• Spatio-temporal Co-location: CoLST(x,y) means that x and y are located at the same spatio-temporal region.

(Db36) STP(x,y) ≜P(x,y)∧∀z((P(z,y)∧CoLST(z,x)) →P(z,x)) (Spatio-temp. Part)

(Db37) CoLST(x,y) ≜∃st(LST(x,st)∧LST(y,st)) (Spatio-temporal Co-location)

Axioms

(Ab42) LST(x,st) →(Span(x)∧STR(st))

(Ab43) (LST(x,st)∧LST(x,st′)) →st = st′

(Ab44) Span(x) →∃st(LST(x,st))

(Ab45) Span(x) →∃y(STP(y,x))

(Ab46) STR(x) →LST(x,x))

(Ab47) (TR(x)∧STP(y,x)) →x = y

(Ab48) (LST(x,st)∧LT(x,t)) →LT(st,t)

(Ab49) (LST(x,st)∧LT(st,t)) →LT(x,t)

8.2 Snap Entities

Primitives relations and constants. On Snap entities we assume the following primi- tives:

• Instantaneous Existence: EXt(x,t) means that x exists at the temporal instant t.

• Instantaneous Parthood: Pt(x,y,t) means that x is a part of y at the temporal instant t.

• Instantaneous Boundary For: Bt(x,y,t) means that x is a bona ﬁde boundary for y at the temporal instant t; x is not necessarily the whole boundary of yat t, but any part of it.

• Instantaneous Fiat Boundary For: FBt(x,y,t) means that x is a ﬁst boundary for y at the temporal instant t; FB is the ﬁat counterpart of B.

• Instantaneous Speciﬁc Dependence: SDt(x,y,t) means that x is speciﬁcally depen- dent on y at the temporal instant t.

• Instantaneous Inherence: IHt(x,y,t) means that at the instant of time t, x (directly) inheres in y. x is a trope of which y is a substantial. Inherence is a form of speciﬁc dependence.

• Space: the constant space designates an individual: the whole of space.

• Instantaneous Spatial Location: LS(x,s,t) means that s is the spatial region at which x is (uniquely) located at the temporal instant t. (It is exact spatial location.)

67

8.2.1 Instantaneous Existence

Axioms

(Ab50) EXt(x,t) →(Snap(x)∧TI(t))

(Ab51) Snap(x) →∃t(EXt(x,t))

8.2.2 Instantaneous Parthood

Deﬁnitions

(Db38) PPt(x,y,t) ≜Pt(x,y,t)∧¬Pt(y,x,t)) (Instantaneous Proper Part)

(Db39) Ot(x,y,t) ≜∃z(Pt(z,x,t)∧Pt(z,y,t)) (Instantaneous Overlap)

(Db40) FUSt(y,x[φ(x)],t) ≜∀z(Ot(z,y,t) ↔∃w(φ(w)∧Ot(z,w,t))) (Inst. Fusion)

(Db41) SMt(x,y,z,t) ≜FUSt(x,w[Pt(w,y,t)∨Pt(w,z,t)],t) (Instantaneous Sum)

(Db42) DFt(x,y,z,t) ≜FUSt(x,w[Pt(w,y,t)∧¬Ot(w,z,t)],t) (Instantaneous Difference)

(Db43) PDt(x,y,z,t) ≜FUSt(x,w[Pt(w,y,t)∧Pt(w,z,t)],t) (Instantaneous Product)

(Db44) CMPt(x,y,t) ≜FUSt(x,z[¬Ot(z,y,t)],t) (Instantaneous Complement)

Axioms

(Ab52) Pt(x,y,t) →(EXt(x,t)∧EXt(y,t))

(Ab53) (Pt(x,y,t)∧SR(y)) →SR(x)32

(Ab54) (Pt(x,y,t)∧SBL(y)) →SBL(x)

(Ab55) (Pt(x,y,t)∧TRP(y)) →TRP(x)

(Ab56) EXt(x,t) →Pt(x,x,t)

(Ab57) (Pt(x,y,t)∧Pt(y,z,t)) →Pt(x,z,t)

(Ab58) (Pt(x,y,t)∧Pt(y,x,t)) →x = y

(Ab59) (FUSt(y,x[φ(x)],t)∧FUSt(y′,x[φ(x)],t)) →y = y′

(Ab60) (EXt(x,t)∧EXt(y,t)∧SR(x)∧SR(y)) →∃z(SM(z,x,y,t))

(Ab61) (EXt(x,t)∧EXt(y,t)∧SBL(x)∧SBL(y)) →∃z(SM(z,x,y,t))

(Ab62) (EXt(x,t)∧EXt(y,t)∧TRP(x)∧TRP(y)) →∃z(SM(z,x,y,t))

(Ab63) (SR(x)∧SR(y)∧SM(z,x,y,t)) →SR(z)

(Ab64) (SBL(x)∧SBL(y)∧SM(z,x,y,t)) →SBL(z)

(Ab65) (TRP(x)∧TRP(y)∧SM(z,x,y,t)) →TRP(z)

Theorems

(Tb8) Pt(x,y,t) →(Snap(x)∧Snap(y)∧TI(t))

32Deﬁning spatial regions as in (Db66), from the transitivity of instantaneous parthood this “axiom” follows. We prefer to indicate this formula here as an axiom in order to be more explicit.

68

8.2.3 Instantaneous Topology

Deﬁnitions. The informal description of the notions introduced in this section is analo- gous to that in the section of (non-instantaneous) topology.

(Db45) IPt(x,y,t) ≜Pt(x,y,t)∧∀z(Bt(z,y,t) →¬Ot(z,x,t)) (Inst. Internal Parthood)

(Db46) FIPt(x,y,t) ≜Pt(x,y,t)∧∀z(FBt(z,y,t) →¬Ot(x,y,t)) (Inst. Fiat Internal Parthood)

(Db47) Bdt(x,t) ≜∃yBt(x,y,t) (Inst. Boundary)

(Db48) FBdt(x,t) ≜∃yFBt(x,y,t) (Inst. Fiat Boundary)

(Db49) BOt(x,y,t) ≜FUSt(x,z[B(z,y,t)],t) (Inst. Boundary Of)

(Db50) CLt(x,y,t) ≜∀z(BOt(z,x,t) →SMt(x,y,z,t)) (Inst. Closure)

(Db51) INTt(x,y,t) ≜∀z(CLt(z,y,t) →DFt(x,y,z,t)) (Inst. Interior)

(Db52) WCt(x,t) ≜∀y,z,cy,cz((SMt(x,y,z,t)∧CLt(cy,y,t)∧CLt(cz,z,t)) →Ot(cx,cy,t)) (Inst. Weak Connection)

(Db53) MCt(x,t) ≜∀y,z,cy,cz((SMt(x,y,z,t)∧CLt(cy,y,t)∧CLt(cz,z,t)) → (Ot(cy,z,t)∨Ot(cz,y,t)) (Inst. Mild Connection)

(Db54) SC(x,t) ≜∀y(INTt(y,x,t) →MCt(y,t)) (Inst. Strong Connection)

(Db55) Ct(x,y,t) ≜Ot(x,y,t)∨∀cx,cy((CLt(cx,x,t)∧CLt(cy,y,t)) → (Ot(cx,y,t)∨Ot(cy,x,t)) (Inst. Connection)

(Db56) ECt(x,y,t) ≜Ct(x,y,t)∧¬Ot(x,y,t) (Inst. External Connection)

(Db57) CLSt(x,t) ≜CLt(x,x,t) (Inst. Closed)

(Db58) SBCt(x,t) ≜SBL(x)∧SCt(x,t)∧∀y((Pt(x,y,t)∧SCt(y,t)) →x = y) (Inst. Substance)

(Db59) SBC(x) ≜∀t(EXt(x,t) →SBCt(x,t)) (Substance)

Axioms

(Ab66) Bt(x,y,t) →(EXt(x,t)∧EXt(y,t))

(Ab67) (Bt(x,y,t)∧SR(y)) →SR(x)

(Ab68) (Bt(x,y,t)∧SBL(y)) →SBL(x)

(Ab69) (Bt(x,y,t)∧TRP(y)) →TRP(x)

(Ab70) (Pt(x,y,t)∧Bt(y,z,t)) →Bt(x,z,t)

(Ab71) FBt(x,y,t) →Pt(x,y,t)

(Ab72) (Pt(x,y,t)∧FBt(y,z,t)) →FBt(x,z,t)

(Ab73) CLt(x,y,t) →Pt(y,x,t)

(Ab74) (CLt(x,y,t)∧CLt(z,x,t)) →P(z,x,t)

(Ab75) (SMt(x,y,z,t)∧SCt(x,t)) →FCt(y,z,t)

69

(Ab76) (SMt(x,y,z,t)∧CLt(cx,x,t)∧CLt(cy,y,t)∧CLt(cz,z,t)∧SMt(x′,cy,cz,t)) → cx = x′

(Ab77) BOt(x,y,t) →Bt(x,y,t)

(Ab78) (Bdt(x,t)∧FCnt(x,t)) →∃y,z(FCnt(y,t)∧Bt(x,y,t)∧IPt(z,y,t))

Theorems

(Tb9) Bt(x,y,t) →(Snap(x)∧Snap(y)∧TI(t))

(Tb10) BOt(x,y,t) →Bt(x,y,t)

(Tb11) (CLSt(x,t)∧Bt(x,y,t)) →Pt(x,y,t)

Possible theorems in view of adaptation from [83]:

(Tb12) (Bt(x,y,t)∧Bt(y,z,t)) →Bt(x,z,t)

(Tb13) (Bt(x,y,t)∧CMPt(z,y,t)) →Bt(x,z,t)

(Tb14) ¬(ECt(x,y,t)∧CLSt(x,t)∧CLSt(y,t))

(Tb15) (FBt(x,y,t)∧FBt(y,z,t)) →FBt(x,z,t)

8.2.4 Instantaneous Dependence

Temporalized variant for dependence relations.

Deﬁnitions

• Substance at an Instant: SBCt(x,t) means that, at t, x is a substance, i.e. it is a maximally strongly connected substantial entity. It has a bona ﬁde boundary.

• Substance: SBC(x) means that x is a substance at every time instant at which it exists.

(Db60) MSDt(x,y,t) ≜SDt(x,y,t)∧SDt(y,x,t) (Mutual Inst. Speciﬁc Dep.)

(Db61) OSDt(x,y,t) ≜SDt(x,y,t)∧¬SDt(y,x,t) (One-side Inst. Speciﬁc Dep.)

(Db62) SBCt(x,t) ≜SBL(x)∧SCt(x,t)∧∀y((Pt(x,y,t)∧SCt(y,t)) →x = y) (Substance at an Instant)

(Db63) SBC(x) ≜∀t(EXt(x,t) →SBCt(x,t)) (Substance)

Axioms

(Ab79) SDt(x,y,t) →(EXt(x,t)∧EXt(y,t))

(Ab80) SDt(x,y,t) →¬Ot(x,y,t)

(Ab81) SR(x) →¬∃y,t(SDt(x,y,t))

(Ab82) SBL(x) →¬∃y,t(SDt(x,y,t))

70

Theorems

(Tb16) (SBC(x)∧SBC(y)∧Pt(x,y,t)) →x = y

8.2.5 Instantaneous Inherence

Deﬁnitions

• Monadic Trope: MTRP(x) means that x is a monadic trope, i.e., it is speciﬁcally dependent on at most on one substantial entity.

• Relational Trope: RTRP(x) means that x is a relational trope, i.e., it is speciﬁcally dependent on at least two substantial entities.

(Db64) MTRP(x) ≜TRP(x)∧∀y,z,t((IHt(x,y,t)∧IHt(x,z,t)) →y = z) (Monadic Trope)

(Db65) RTRP(x) ≜TRP(x)∧∀t(EXt(x,t) →∃y,z(IHt(x,y,t)∧IHt(x,z,t)∧¬y = z)) (Relational Trope)

Axioms

(Ab83) IHt(x,y,t) →(TRP(x)∧SBL(y)∧TI(t))

(Ab84) IHt(x,y,t) →SDt(x,y,t)

(Ab85) (SBC(x)∧EXt(x,t)) →∃y(IHt(y,x,t))

(Ab86) (TRP(x)∧EXt(x,t)) →∃y(IHt(x,y,t))

(Ab87) (MTRP(x)∧IHt(x,y,t)∧IHt(x,y′,t′)) →y = y′

(Ab88) (RTRP(x)∧∀y1,y2,y3,t((IHt(x,y1,t)∧IHt(x,y2,t)∧IHt(x,y3,t)) → (y1 = y2 ∨y2 = y3 ∨y1 = y3))) →∀z1,z2,z3,z4,t,t′

((IHt(x,z1,t)∧IHt(x,z2,t)∧IHt(x,z3,t′)∧IHt(x,z4,t′)∧¬z1 = z2 ∧¬z3 = z4) →((z1 = z3 ∧z2 = z4)∨(z1 = z4 ∨z2 = z3)))

Theorems

(Tb17) IHt(x,y,t) →(EXt(x,t)∧EXt(y,t))

8.2.6 Space

Deﬁnitions

• SpatialRegion: SR(x) means that x is a spatial region, i.e., a part of space.

(Db66) SR(x) ≜Snap(x)∧∀t(EXt(x,t) →P(x,space,t)) (Spatial Region)

Axioms

(Ab89) TI(t) →EXt(space,t)

71

Theorems

(Tb18) Snap(space)

8.2.7 Instantaneous Spatial Location

Deﬁnitions

• Instantaneous Spatial Subsumtion: SbLS(x,y,t) means that x spatially subsumes y at t, i.e., at t, the spatial location of x is a part of the spatial location of y.

• Occupies: OCt(x,y,t) means that x occupies y at t, i.e., (i) x and y (which are both substantial entities) do not overlap at t and neither do their respective locations, but (ii) at t, the location of x is an internal part of the location of the sum of the x and y.

• Site: Sitet(x,t) means that x is a site at t, i.e., it is a substantial entity occupied at y by a substance.

(Db67) SbLS(x,y,t) ≜∀sx,sy((LS(x,sx,t)∧LS(y,sy,t)) →Pt(sx,sy,t)) (Spat. Subsumption)

(Db68) OCt(x,y,t) ≜∀s,sx,sy(SBL(x)∧SBL(y)∧EXt(x,t)∧EXt(y,t)∧¬O(x,y,t)∧ LS(x,sx,t)∧LS(y,sy,t)∧SMt(s,sx,sy)) →(¬Ot(sx,sy)∧IPt(sx,s)) (Occupies)

(Db69) Sitet(x,t) ≜∃y(SBC(y)∧OCt(y,x,t)) (Site)

Axioms

(Ab90) LS(x,s,t) →(Snap(x)∧SR(s)∧TI(t))

(Ab91) LS(x,s,t) →(EXt(x,t)∧EXt(s,t))

(Ab92) (LS(x,s,t)∧LS(x,s′,t)) →s = s′

(Ab93) (Snap(x)∧EXt(x,t)) →∃s(LS(x,s,t))

(Ab94) SR(x) →∃t(LS(x,x,t))

(Ab95) (TRP(x)∧FUSt(y,z[IHt(x,z,t)],t)∧LS(y,s,t)) →LS(x,s,t)

8.3 Relations between Snap and Span entities

Material in this section is partially based on or adapted from [42, 41, 43].

Primitives relations. The most fundamental form of participation is between a Snap entity and a temporal slice of a process (an event) - [42]:

• Participation: PCss(x,y,t) means that x is a substantial which participates in the event y at t.

• Realization: RZss(x,y,t) means that x is in a process of realization in the event y at t.

• Dependence: SDss(x,y,t) means that x is dependent on the event y at t.

72

Deﬁnitions

(Db70) TPCt(x,y,t) ≜∃z(TS(z,y)∧PCss(x,z,t)) (Temporal Participation)

(Db71) CPC(x,y) ≜∀t(OCC(y,t) →TPCt(x,y,t)) (Complete Participation)

(Db72) LF(x,y) ≜FUS(x,z[CPC(y,z)]) (Life)

(Db73) EvLS(x,sx,t) ≜FUS(sx,s[∃y(PCt(y,x,t)∧LS(y,s,t))],t) (Spat. Loc. of Events)

Axioms

(Ab96) SDss(x,y,t) →(Snap(x)∧EV(y)∧TI(t))

(Ab97) SDss(x,y,t) →(EXt(x,t)∧ILT(y,t))

(Ab98) PCss(x,y,t) →SDss(x,y,t)

(Ab99) PCss(x,y,t) →SBL(x)

(Ab100) RZss(x,y,t) →∃z(IHt(x,z,t)∧PCss(z,y,t))

(Ab101) (RZss(x,y,t)∧IHt(x,z,t)) →PCss(z,y,t))

73

9 Comparing the Basic Modules: A Case Study

In this section, we aim at comparing the ontologies in the library through an example. The example is stated as follows.

“A statute of clay exists for a period of time going from t1 to t2. Between t2 and t3, the statue is crashed and so ceases to exists although the clay is still there.”

9.1 The statue and the clay in DOLCE

This example is represented in DOLCE assuming that there is a perdurant, the crashing (crash), that lasts during all the period of time (from t1 to t3), and two endurants, the statue (statue) and the clay (clay), which are participants in the perdurant. More precisely, the crashing is an accomplishment (ACC), the statue is a non-agentive physical object (NAPO), and the clay is an amount of matter (M). Since in DOLCE one can represent temporal location explicitly using the category of time intervals (T), we have (Figure 6 illustrates the formal constraints between these entities):33

ACC(crash)∧NAPO(statue)∧M(clay)∧T(t1)∧T(t2)∧T(t3)

PRE(crash,t1 +t2 +t3)∧PC(statue,crash,t1+t2)∧PC(clay,crash,t1+t2 +t3)

From this, it follows that:

PRE(statue,t1+t2)∧PRE(clay,t1 +t2 +t3)

During its life, the statue is composed of the clay and so these are spatio-temporally co-localized:

DK(statue,clay,t1+t2)∧statue ⊆ST clay

All these constraints are based on the temporal (TL) and spatial (SL) locations of the perdurant and endurants. In DOLCE, endurants have only direct spatial qualities and perdurants only temporal qualities. The temporal regions of endurant and the spatial regions of perdurants are inherited by means of the participation relation (the ﬁrst conjunct below introduces these regions):

TL(tl)∧SL(slc)∧SL(sls)∧S(s1)∧S(s2)

qt(tl,crash)∧qt(slc,clay)∧qt(sls,statue)

ql(t1 +t2 +t3,tl)∧ql(s1,sls,t1 +t2)∧ql(s1,slc,t1 +t2)∧ql(s2,slc,t3)

9.2 The statue and the clay in OCHRE

Since OCHRE is an object-centered ontology, the main elements in the example, namely the statue and the clay, are both introduced as thin objects:

33For the sake of simplicity, here we use maximal temporal indices only, i.e., we write PC(x,y,t1 +t2) without PC(x,y,t1)∧PC(x,y,t2) although the latter is formally required by the axioms of DOLCE.

74

DKt1+t2

statue clay

ED

PCt1+t2 PCt1+t2+t3

crash

qt qt qt

PD

sls tl slc

ql

Q

qlt1+t2 qlt1+t2 qlt3

t1+t2+t3

P

P P

t3

t1 t2 s1 s2

R

Figure 6: The statue and the clay in DOLCE: formal constraints constraints between the entities in the domain. The temporal index indicates the time interval at which the relation is valid.

TH(statue)∧TH(clay)

Recall that in OCHRE the parthood relation is extensional and that thin objects are integral wholes, thus each of these two objects have atomic proper parts that we dub “essential tropes”. Let us assume that each object has two essential tropes (Figure 7 illustratates the mereo-topological and spatio-temporal constraints):34

• the mass and the volume are essential to the clay:

TR(mass)∧TR(vol)∧AtP(mass,clay)∧AtP(vol,clay)

• the form and the color are essential to the statue:

TR( form)∧TR(color)∧AtP( form,statue)∧AtP(color,statue)

In OCHRE, one has to model time through temporal relations over thick objects. These objects are stages of thin objects. The temporal relation we need in this example is the relation of immediate anteriority (IA). We need at least three thick objects, say s1,s2 and s3 (where si is related time ti):

TK(s1)∧TK(s2)∧TK(s3)

H(statue,s1)∧H(statue,s2)∧H(clay,s1)∧H(clay,s2)∧H(clay,s3)

IA(s1,s2)∧IA(s2,s3)

The fact that the statue is composed of the clay in the period from t1 to t2 can be represented as follows:

H(statue,s1)∧H(statue,s2)∧H(clay,s1)∧H(clay,s2)∧IA(s1,s2)

34For the sake of simplicity, we assume that all the tropes are simple (or atomic) although in general tropes like the color can be decomposed in different “dimensions”.

75

p

PP PP

EVY

e1 e2

PP PP PP PP

E

IA IA

s1 s2 s

3

TK

H H H H

H

statue clay

Prop Prop Prop

TH

PP PP PP PP

form color mass vol tr1 tr2 tr3

TR

Figure 7: The statue and the clay in OCHRE: constraints on Mereo-topology and Space- time.

That is, the relationship between the statue and the clay is not captured through the con- nection relation.35 Instead, they are considered haecceties of the same thick object. From the deﬁnition of H, all the essential tropes of the clay and of the statue are parts of s1 and s2. Therefore, to distinguish these two stages (and to distinguish s3 from the thin object clay), we need additional tropes here called tr1,tr2.tr3. These new tropes are direct parts of the thick objects (stages) and are not part of the thin objects themselves (tri is a property of si):

TR(tr1)∧TR(tr2)∧TR(tr3)

P(tr1,s1)∧P(tr2,s2)∧P(tr3,s3)

At this point, we look at the constraints for the foundation relation. For this, recall that:

• thin objects are founded on their parts only (see (Ao16));

• properties are founded on exactly one thin object (see (Ao42) and (Ao43));

• thick objects are founded on at least one thin object;

• thin objects are integral wholes, thus one of the two essential tropes we stated has to be founded on the other (see (Do16) and (Ao19)).

These constraints are captured by the following expressions (Figure 8 illustrates the con- straints on the foundation primitive):

F(statue, form)∧F(statue,color)∧F(clay,mass)∧F(clay,vol)

F(tr1,clay)∧F(tr2,clay)∧F(tr3,clay)

F(s1,statue)∧F(s2,statue,color)∧F(s1,clay)∧F(s2,clay)∧F(s3,clay)

35Remember that the connection relation is deﬁned only on thick objects.

76

p

EVY

e1 e2

E

s1 s2 s3

TK

statue clay

TH

form color mass vol tr1 tr2 tr3

TR

Figure 8: The statue and the clay in OCHRE: constraints on the foundation relation.

F(color, form)∧F(vol,mass)

Note that the tropes tr1, tr2 and tr3 are properties of the thick objects s1, s2 and s3, respectively. We have assumed that they are founded on the thin object clay. Thus, by (Do33), we have direct parts g1, g2 and g3 which are guises of the thick objects s1, s2 and s3, respectively. Since no trope is founded on the statue, the statue forms a guise on its own:

SM(g1,clay,tr1)∧SM(g2,clay,tr2)∧SM(g3,clay,tr3)

G(g1,clay,s1)∧G(g2,clay,s2)∧G(g3,clay,s3)

G(statue,statue,s1)∧G(statue,statue,s3)∧G(statue,statue,s3)

Thin objects are founded on their own parts. This explains why the thin object statue is not founded on the thin object clay. Finally, the example we are dealing with is formalized using two events e1,e2:

SM(e1,s1,s2)∧EV(e1,statue)∧EV(e1,clay)

SM(e2,s2,s3)∧EV(e2,clay)

and three eventualities (e1,e2 and p such that SM(p,e1,e2)). It follows that:

PC(statue,e1)∧PC(clay,e1)∧PC(clay,e2)∧PC(statue, p)∧PC(clay, p)

9.3 The statue and the clay in BFO

At this stage of the formalization of BFO, we cannot provide a detailed description of the statue/clay example since it involves the notion of quasi-entity (a notion not formalized yet) and the more general meta-ontological framework (which is left out in this presenta- tion). Nonetheless, we can give a few informal intuitions that drive BFO approach to this problem.

77

In BFO, a statue is simply a quasi-substance. In particular, it is an element of an ontology of art or social reality. It is consistent in BFO to think of a statue as capable of changing its parts (e.g., replacement of hands). On the other hand, the ontology in which the clay is to be found is one of physical reality. What can be said about the clay before and after the crashing is that the ﬁrst is genidentical to the aggregates of the detached parts. In a physical ontology, severing a piece of clay looks like a case of separation (creates two new substances). If you remove a part of the clay or replace it, the clay has changed (mereological change, maybe even morphological). The formalization of these intuitions in the framework of BFO can be done in different ways and the issue is under discussion.

78

10 Comparing the Basic Modules: Formal Links

In this section we provide an explicit example of the connections among modules in the library. Here we focalize to the link from OCHRE to DOLCE. This example intends (i) to clarify what we intend for semantic links and (ii) to show the level of formal complexity they may require. Note that our procedure uses standard set theory. We do not believe the use of set theory is an exception restricted to the particular modules we are dealing with in this section. Although one can consider problematic the application of set theory, since it is much stronger than the formalisms description logic can represent, it should be noticed that set theory is applied only to construct formal structures and it is not required in the actual formula translation. In our view, this kind of semantic links should form a special translation module in the library. This module should collect the formulas of a speciﬁc ontology and their translations into another ontology.

Our general task is the deﬁnition of a translation operator from OCHRE formulas into the DOLCE language. We indicate this operator with Φ. Note that the inverse operator is not consider here. Important differences between DOLCE and OCHRE make the translation particularly relevant. 1) As we know, DOLCE follows a multiplicativist approach, while OCHRE is a revisionist ontology. Indeed, OCHRE is based on a small number of basic categories and relations in comparison with DOLCE. This fact does not imply that OCHRE has a smaller number of entities in the domain of quantiﬁcation. Rather, the modest structure at the level of categories and relations forces OCHRE to state strong existential conditions. 2) On the other hand, DOLCE considers a wider domain of quantiﬁcation than OCHRE. For example,

OCHRE does not include abstract entities. 3) The distinctions DOLCE introduces are more speciﬁc than those in OCHRE. Ffor example, OCHRE does not distinguish agentive vs. non-agentive entities. In other words, the DOLCE taxonomy is more inclusive and deeper than the taxonomy of OCHRE. For this reason, only a fragment of DOLCE is “expressible” in terms of the

OCHRE language.

Technically speaking, we deﬁne:

(i) two kinds of structures indicated with O and D that are associated, respectively, with OCHRE and with a fragment of DOLCE;

(ii) the operator Φ : O →D mapping O-structures into D-structures.

Deﬁnition of OCHRE structures. An OCHRE structure O is an ordered tupla

⟨PT,P,F,C,A,SI,CM⟩

where:

• PT is a non-empty set of “particulars”;

• P is a binary relation on PT × PT satisfying the OCHRE axioms on the parthood relation;

79

• F is a binary relation on PT ×PT satisfying the OCHRE axioms on the foundation relation;

• SI is a binary relation on PT × PT satisfying the OCHRE axioms on the similarity relation;

• CM is a binary relation on PT ×PT satisfying the OCHRE axioms on the compara- bility relation;

• C is a binary relation on PT ×PT satisfying the OCHRE axioms on the connection relation;

• A is a binary relation on PT ×PT satisfying the OCHRE axioms on the anteriority relation.

In what follows we use all the deﬁnitions introduced in OCHRE. In particular, we often refer to the three subsets of PT corresponding to tropes, thin objects, and thick objects. These are:36

• TR = {x : x ∈PT ∧TR(x)};

• TH = {x : x ∈PT ∧TH(x)};

• TK = {x : x ∈PT ∧TK(x)}.

As we will see, an OCHRE structure can be translated into DOLCE using only a subset of the DOLCE categories. This fact allows us to simplify the axiomatization of DOLCE considered in this section by disregarding the irrelevant distinctions: the new axioms are indicated by Aod while others are ignored. The changes are indicated below.

Deﬁnition of DOLCE structures. A DOLCE structure D is an ordered tupla37

⟨ED,PD,Q,T,R,P(2),P(3),K,PC,qt,ql⟩

where:

• ED is a non-empty set of “endurants”;

• PD is a non-empty set of “perdurants”;

• Q is a non-empty set of “qualities”;

• T is a non-empty set of “time intervals”;

• R is a non-empty set of “space regions”;

• P(2) is a binary relation on (PD ∪T ∪R) × (PD ∪T ∪R) satisfying the following

DOLCE axioms on the parthood relation: (Ad1), (Ad2), (Ad5)–(Ad8)38. Instead of (Ad3) we consider the following two axioms:

36We use the same constant identiﬁer for a set and its corresponding predicate since there is no danger of confusion. 37In DOLCE, parthood and temporary parthood are indicated with the same symbol because they differ in the number of arguments. In the structure we differentiate this two relations indicating the number of arguments. When the number of arguments is clear from the context, we drop the arity index. 38We take AB = T ∪R. In addition, we do not consider the DOLCE axiom for fusion (Ad9) because

OCHRE does not include this operator.

80

(Aod1) P(x,y) →(T(x) ↔T(y)) (Aod2) P(x,y) →(R(x) ↔R(y))

• P(3) is a ternary relation on ED ×ED ×T satisfying the following DOLCE axioms on the temporary parthood relation: (Ad10), (Ad13), and (Ad16)–(Ad18);

• K is a binary relation on ED × ED39 satisfying the following DOLCE axioms on the composition relation: (Ad24)–(Ad27). In addition, instead of axiom (Ad20) we consider:

(Aod3) K(x,y,t) →(ED(x)∧ED(y)∧T(t))

• PC is a binary relation on ED×PD satisfying the following DOLCE axioms on the participation relation: (Ad33)–(Ad37);

• qt is a binary relation on Q ×ED40 satisfying the following DOLCE axioms on the quality relation: (Ad43)–(Ad44). In addition, instead of axioms (Ad38)–(Ad41) we consider:

(Aod4) qt(x,y) →(Q(x)∧ED(y));

and instead of axioms (Ad46)–(Ad48) we consider:

(Aod5) Q(x) →∃y(qt(x,y));

• ql is a ternary relation on R×Q×T satisfying the following DOLCE axioms on the temporary quale relation: (Ad65)–(Ad66). In addition, instead of (Ad58)–(Ad61) we consider:

(Aod6) ql(x,y,t) →(R(x)∧Q(y)∧T(t));

and instead of (Ad62) we consider:

(Aod7) (Q(x)∧PRE(x,t)) →∃r(ql(r,x,t));

As for OCHRE, in what follows, we use all the deﬁnitions introduced in DOLCE.

Deﬁnition of the operator Φ. Given an OCHRE structure O = ⟨PT,P,F,C,A,SI,CM⟩ we deﬁne the DOLCE structure associated with O

Φ(O) = ⟨ED,PD,Q,T,R,P(2),P(3),K,PC,qt,ql⟩

in the following way:

(Dod1) ED = TH

(Dod2) PD =℘(TK) where℘(TK) is the power set of TK

Let TAt be the set of atomic time intervals deﬁned as the maximal set of simulta- neously thick objects:

39We consider composition only between endurants. It is not clear to which extent it is possible to introduce composition between perdurants in OCHRE. 40We consider here qualities of endurants only.

81

(Dod3) TAt = {|tk|T : tk ∈TK}, where we put |tk|T = {tk′ : SL(tk′,tk)}

(Dod4) T =℘(TAt)

(Dod5) Q = {|tr,th|Q : tr ∈TR∧th ∈TH ∧IN(tr,th)}, where

IN(tr,th) ≜tr ∈TR∧th ∈TH ∧(P(tr,th)∨∃tk(Prop(tr,tk)∧H(th,tk)))

|tr,th|Q = {tr′ : IN(tr′,th)∧CM(tr′,tr)}

thus, a quality is the maximal set of comparable tropes that are in the relation IN with a thin object.

An atomic region is an element of RAt and it corresponds to a maximal set of similar tropes:

(Dod6) RAt = {|tr|R : tr ∈TR} and |tr|R = {tr′ ∈TR : SI(tr′,tr)}

Using RAt we deﬁne regions in our structure as the elements of the following set:

(Dod7) R = {||tr|R| : |tr|R ∈RAt}, where ||tr|R| ⊆{|tr′|R ∈RAt : CM(tr′,tr)}

i.e. regions are sets of comparable atomic regions.

(Dod8) P(2) = {(x,y) : (x,y ∈T ∨x,y ∈R∨x,y ∈PD)∧x ⊆y}

(Dod9) P(3) = {(x,y,t) : x,y ∈ED∧t ∈T ∧∀tat ∈t(PAt(x,y,tat))}

where PAt is deﬁned only on atomic time intervals by:

(Dod10) PAt = {(x,y,t) : x,y ∈ED∧t ∈TAt∧∃tkx,tky ∈t(H(x,tkx)∧H(y,tky)∧P(tkx,tky))}

(Dod11) K = {(x,y,t) : x,y ∈ED∧t ∈T ∧∀tat ∈t(KAt(x,y,tat))}

where KAt is deﬁned only on atomic time intervals by:

(Dod12) KAt = {(x,y,t) : x,y ∈ED∧t ∈TAt∧∃tk ∈t(H(x,tk)∧H(y,tk)∧∀gx,gy((G(gx,tk,x)∧ G(gy,tk,y)) →PP(gx,gy)))}

(Dod13) PC = {(x,y,t) : x ∈ED∧y ∈PD∧t ∈T ∧∀tat ∈t(PCAt(x,y,tat))}

where PCAt is deﬁned only on atomic time intervals by:

(Dod14) PCAt = {(x,y,t) : x ∈ED∧y ∈PD∧t ∈TAt ∧∃tk ∈(t ∩y)(H(x,tk))}

(Dod15) qt = {(|tr,th|Q,th) : |tr,th|Q ∈Q∧th ∈ED}

(Dod16) ql = {(r,q,t) : r ∈R∧q ∈Q∧t ∈T ∧r = {rat : tat ∈t ∧qlAt(rat,q,tat)}}

where qlAt is deﬁned only on atomic time intervals by:

(Dod17) qlAt = {(r,|tr,th|Q,t) : rat ∈RAt ∧|tr,th|Q ∈Q∧t ∈TAt ∧∃tr′,tk(tr′ ∈(|tr,th|Q∩ r)∧tk ∈t ∧P(tr′,tk)∧H(th,tk))}

(Dod1) states that endurants correspond to thin objects. For the sake of simplicity, here we take perdurants to be any set of thick objects (Dod2). This means that we admit instantaneous perdurants (corresponding to single- tons) and non-convex perdurants (corresponding to non-convex sets of elements in TK, where convexity is relative to the anteriority relation). Adding temporal or cardinal con- straints on the sets in ℘(TK), it is possible to limit PD. However, we do not consider this aspect. As in the case of perdurants, we admit non-convex and instantaneous time

82

intervals (Dod4); in particular, atomic time intervals are deﬁned as the the maximal set of simultaneous thick objects (Dod3). Quality are maximal sets of comparable tropes that are in the ralation IN with a thin object (Dod5). Note that we consider qualities of thin objects only. It is not clear whether one can deﬁne qualities of qualities (properties of properties) or temporal qualities (qual- ities of thick objects). Also, we will consider physical and abstract regions only. The regions are deﬁned as sets of comparable atomic regions (Dod7), where atomic regions are maximal sets of similar tropes of OCHRE (Dod6). The relation of being present is not considered in D, but it is very useful in the proofs. We introduce the PRE relation via the PREAt relation deﬁned only on atomic temporal intervals:

(Dod18) PREAt = {(x,t) : (x ∈ED ∧∃tk ∈t(H(x,tk)))∨(x ∈PD ∧∃tk ∈x ∩t) ∨(x = |tr,th|Q ∈Q∧∃tk ∈t,∃tr′ ∈|tr,th|Q(H(th,tk)∧P(tr′,tk)))}

(Dod19) PRE = {(x,t) : ∀tat ∈t(PREAt(x,tat))}

Main theorem. If O is an OCHRE structure, then Φ(O) is a DOLCE structure.

Proof. In the following we will consider only relations based on atomic temporal inter- vals (PAt,KAt,PCAt,qlAt); the general result follows directly from the deﬁnition of the correspondent non atomic version.

Parthood Argument restrictions

(Ad1), (Aod1), (Aod2) Directly from the deﬁnition (Dod8) and from the fact that AB = T ∪R.

Ground axioms

(Ad5)–(Ad8) Directly from the deﬁnitons (Dod8), (Dod4), (Dod7), and the properties of the ⊆relation.

Temporary Parthood Argument restrictions

(Ad10) Directly from the deﬁnition of temporary parthood (Dod9).

Ground axioms

(Ad13) From PAt(x,y,t), PAt(y,z,t), and (Dod10), we have ∃tkx,tky,tk′ y,tkz ∈t(H(x,tkx)∧H(y,tky)∧H(y,tk′ y)∧H(z,tkz)∧P(tkx,tky)∧P(tk′ y,tkz)). By (Ao3) and (Ao41), ∃tkx,tky,tkz ∈t(H(x,tkx)∧H(y,tky)∧H(z,tkz)∧P(tkx,tky)∧ P(tky,tkz)). By (Ao3) again, ∃tkx,tkz ∈t(H(x,tkx) ∧H(z,tkz) ∧P(tkx,tkz)), i.e., PAt(x,z,t).

Links with other primitives

83

(Ad16) From x ∈ED ∧PREAt(x,t), (Dod18), and (Ao1), we obtain ∃tk ∈t(H(x,tk) ∧ P(tk,tk)). By (Dod10), PAt(x,x,t).

(Ad17) From x,y ∈ED ∧PAt(x,y,t) and (Dod10), ∃tkx,tky ∈t(H(x,tkx) ∧H(y,tky) ∧ P(tkx,tky)). We get PREAt(x,t)∧PREAt(y,t) using (Dod18).

(Ad18) Directly from (Dod9), (Dod4), and (Dod8).

Constitution Argument restrictions

(Aod3) Directly from (Dod11).

Ground axioms

(Ad24) From KAt(x,y,t) and (Dod12) ∃tk ∈t(H(x,tk)∧H(y,tk)∧∀gx,gy((G(gx,tk,x)∧G(gy,tk,y)) →PP(gx,gy))). By the antisimmetry of PP, ∃tk ∈t(H(x,tk)∧H(y,tk)∧∀gx,gy((G(gx,tk,x)∧G(gy,tk,y)) →¬PP(gy,gx))). By (Dod12), we conclude that ¬KAt(y,x,t).

(Ad25) From KAt(x,y,t)∧KAt(y,z,t) and (Dod12), ∃tk ∈t(H(x,tk)∧H(y,tk)∧∀gx,gy((G(gx,tk,x)∧ G(gy,tk,y)) →PP(gx,gy)))∧ ∃tk′ ∈t(H(y,tk′)∧H(z,tk′)∧∀g′ y,gz((G(g′ y,tk′,y)∧G(gz,tk′,z)) →PP(g′ y,gz))) Now, we can use (Ao41) to get ∃tk ∈t(H(x,tk)∧H(y,tk)∧H(z,tk)∧ ∀gx,gy((G(gx,tk,x)∧G(gy,tk,y)) →PP(gx,gy))∧ ∀g′ y,gz((G(g′ y,tk,y)∧G(gz,tk,z)) →PP(g′ y,gz))) By (To1), ∃tk ∈t(H(x,tk)∧H(y,tk)∧H(z,tk)∧ ∀gx,gy,gz((G(gx,tk,x)∧G(gy,tk,y)∧G(gy,tk,z)) →(PP(gx,gy)∧PP(gy,gz)))) Since PPis transitive, we get ∃tk ∈t(H(x,tk)∧H(z,tk)∧∀gx,gz((G(gx,tk,x)∧G(gz,tk,z)) →PP(gx,gz))) thus, KAt(x,z,t) from (Dod12).

Links with other primitives

(Ad26) From KAt(x,y,t) and (Dod12), we get ∃tk ∈t(H(x,tk) ∧H(y,tk)). By (Dod18), we conclude that PREAt(x,t)∧PREAt(y,t).

(Ad27) Directly from (Dod11), (Dod8), and (Dod4).

Participation Argument restrictions

(Ad33) Directly from (Dod13).

Existential axioms

(Ad34) From x ∈PD ∧PREAt(x,t) and (Dod18), one gets ∃tk ∈t ∩x. By (Ao40) and (Dod2), this gives ∃y ∈ED,∃tk ∈t ∩x(H(y,tk)). Applying (Dod14), ∃y(PCAt(y,x,t)) holds.

84

(Ad35) From x ∈ED, (Ao46) and (Dod1), ∃tk(H(x,tk)). Taking t = |tk|T and y = {tk}, one obtains ∃tk,y,t(tk∈t ∩y∧H(x,tk)). From this and (Dod14), ∃y,t(PCAt(x,y,t)).

Links with other primitives

(Ad36) From PCAt(x,y,t) and (Dod14), x ∈ED∧y ∈PD∧∃tk(tk ∈y∩t ∧H(x,tk)). By (Dod18), PREAt(x,t)∧PREAt(y,t).

(Ad37) Directly from (Dod13), (Dod8), and (Dod4).

Quality Argument restrictions

(Aod4) Directly from (Dod15).

Ground axioms41

(Ad43) From qt(|tr,th|Q,y)∧qt(|tr,th|Q,y′) and (Dod15), th = y∧th = y′. Thus, y = y′.

(Ad44) We can rewrite the hypothesis as: qt(|tr,th|Q,y)∧qt(|tr′,th′|Q,y)∧CM(tr,tr′).By(Dod15), qt(|tr,th|Q,y)∧qt(|tr′,th|Q,y)∧CM(tr,tr′). From (Ao24), (Ao25) and (Dod5), we conclude that |tr,th|Q = |tr′,th|Q.

Existential axioms

(Aod5) Directly from (Dod5) and (Do15).

Temporary quale Argument restrictions

(Aod6) Directly from (Dod16)).

Existential axioms

(Ad62) From (Q(x)∧PREAt(x,t)) and (Dod18), (x = |tr,th|Q ∧∃tk ∈t,∃tr′ ∈|tr,th|Q(H(th,tk)∧P(tr′,tk))). Let r = |tr′|R, then ∃r ∈RAt(∃tk ∈t,∃tr′ ∈|tr,th|Q∩r(H(th,tk)∧P(tr′,tk))) and, by (Dod17), ∃r(qlAt(r,x,t)).

Links with other primitives

(Ad65) From qlAt(r,|tr,th|Q,t) and (Dod17), ∃tk ∈t,∃tr′ ∈|tr,th|Q ∩r(H(th,tk)∧P(tr′,tk)). That is, ∃tk ∈t,∃tr′ ∈|tr,th|Q(H(th,tk)∧P(tr′,tk)). Using (Dod18), one concludes that PREAt(|tr,th|Q,t).

(Ad66) Directly from (Dod16), (Dod8), and (Dod4).

□Main theorem

41Note that considering only qualities of endurants qt and dqt coincide.

85

Note that in the deﬁnition of DOLCE structures we do not have considered (Ad14), for the relation P(3). This because, OCHRE structures have to be strengthened in order to prove this axiom via Φ.

Deﬁnition of P(3)-extensional DOLCE structures. A P(3)-extensional DOLCE structure is a DOLCE structure with the additional axiom (Ad14).

Deﬁnition of TK-extensional OCHRE structures. A TK-extensional OCHRE structure is an OCHRE structure with the following additional axiom:

(Aod8) (TK(x)∧TK(y)∧¬P(x,y)) →∃z(TK(z)∧P(z,x)∧¬O(z,y))

Theorem. If O is a TK-extensional structure, then Φ(O) is a P(3)-extensional DOLCE structure.

Proof. We need to prove only (Ad14):

(Ad14) From x,y ∈ED∧PREAt(x,t)∧PREAt(y,t)∧¬PAt(x,y,t), (Dod10), and (Dod18), ∃tkx,tky ∈t(H(x,tkx)∧H(y,tky)∧¬P(tkx,tky)). By (Aod8), ∃tkx,tky ∈t,∃tkz(H(x,tkx)∧ H(y,tky)∧P(tkz,tkx)∧¬O(tkz,tky)) Thus, ∃tkx,tky,tkz ∈t(H(x,tkx)∧H(y,tky)∧P(tkz,tkx)∧¬O(tkz,tky)) and, by (Ao40), ∃tkx,tky,tkz ∈t,z ∈ED(H(x,tkx)∧H(y,tky)∧H(z,tkz)∧P(tkz,tkx)∧ ¬O(tky,tkz)) From this and (Dod10), ∃z ∈ED(PAt(z,x,t)∧¬OAt(z,y,t)) □Theorem

86

11 The Link with Natural Language

In the last years, lexicographers, lexical semanticists and ontologists have been joining forces to build innovative systems for integrating ontological knowledge with lexica and semantic resources in general. Although autonomously developed, lexica manifest a natural disposition to be in- formed by axiomatic ontologies: both kinds of resources are built with similar rela- tions (hyponymy/subsumption, meronymy/parthood, etc.), attempt to represent concepts (synsets/ontological categories), and capture relevant aspects of human semantic and world knowledge. In particular, from the viewpoint of applications, the “alliance” be- tween ontologies and lexica can improve the infrastructures of the emerging Semantic Web, supplying lexical coverage to formalized conceptual distinctions. Important exam- ples of this interaction are the recent works on the conceptual analysis of WORDNET (one of the ﬁrst lexical knowledge bases), and the wide use of upper ontologies in innovative international projects like EUROWORDNET42,SIMPLE, Balkanet43, DWDSnet44

The best-known and most frequently used lexicon in the NLP community is WORD- NET [27], as we said above, one of the ﬁrst resources available in the ﬁeld. WORDNETs’ building blocks are sets of cognitively synonymous English words from the four major syntactic classes. The synsets are interlinked by conceptual-semantic relations, forming a tight network. The conceptual-semantic relations differ somewhat according to the part of speech category of the synsets members. In the next paragraph we present an overview of the alignment we performed between

DOLCE foundational ontology and WORDNET 1.6, focused on the their top level structure (for the WORDNET top hierarchy see Table 4.

11.1 Mapping WORDNET into DOLCE

In the recent years, we developed a methodology for testing the ontological adequacy of taxonomic links called OntoClean [47, 48], which was used as a tool for a ﬁrst systematic analysis of WORDNET’s upper level taxonomy of nouns [35]. OntoClean was based on an ontology of properties (unary universals), characterized by means of meta-properties.

DOLCE, in this sense, has to be seen as a complement of OntoClean, being a reference ontology which exploit the distinctions identiﬁed by OntoClean. We adopt some preliminary assumptions in order to convert WORDNET’s databases into a workable knowledge base. In order to work with named concepts, we normalized the way synsets are referred to lexemes in WORDNET, thus obtaining one distinct name for each synset: if a synset had a unique noun phrase, this was used as concept name; if that noun phrase was polysemous, the concept name was numbered (e.g. window 1). If a synset had more than one synony- mous noun phrase, the concept name linked them together with a dummy character (e.g. Equine$Equid).

42http://www.illc.uva.nl/EuroWordNet/ 43http://www.ceid.upatras.gr/Balkanet/ 44http://www.dwdsnet.com/

87

Comparing WORDNET’s unique beginners with DOLCE’s ontological categories, it becomes evident that some notions are very heterogeneous: for example, Entity looks like a “catch-all” class containing concepts hardly classiﬁable elsewhere, like Anticipation, Imaginary Place, Inessential, etc. Such synsets have only a few children and these have been already excluded in our analysis. Some examples of our merging work are sketched in Table 5. Some problems encoun- tered for each category are discussed below.

11.1.1 Endurants

Entity is a very confused synset. A lot of its hyponyms have to be “rejected”: in fact there are roles (Causal Agent, Subject 4), unclear synsets (Location45.) and so on. This Unique Beginner maps partly to our Amount of Matter and partly to our Physical Object category. Some hyponyms of Physical Object are mapped to our top concept feature. By removing roles like Arrangement and Straggle, Group$grouping appears to in- clude Agentive Social Object (social group, ethnic group), Non-agentive Social Ob- ject (circuit), Agentive Physical Object (citizenry) and Non-agentive Physical Object (biological group, kingdom; collection). Possession 1 is a role, and it includes both roles and types. In our opinion, the synsets marked as types (Asset, Liability, etc.) should be moved towards lower levels of the ontology, since their meanings seem to deal more with a speciﬁc domain - the eco- nomic one - than with a set of general concepts. This means that the remainder branch has also to be eliminated from the top level, because of its overall anti-rigidity (the peculiarity of roles).

11.1.2 Perdurants

Event 1, Phenomenon 1, State 1 and Act 1 are the Unique Beginners (top nodes) of those branches of WORDNET denoting perdurants. In particular, the hyponyms of State 1 seem to ﬁt well with our state category, as the children of Process (a subordinate of Phenomenon). For the time being, we restrict the mapping of our accomplishment cat- egory to the homonymous synset of WORDNET. Event 1 is too heterogeneous to be clearly partitioned in terms of our approach: to a great extent, however, its hyponyms could be added to lower levels of the taxonomy of occurrences.

11.1.3 Qualities and Abstracts

ABSTRACTION 1 is the most heterogeneous Unique Beginner: it contains abstracts such as Set 5, quality regions such as Chromatic Color, qualities (mostly from the synset Attribute) and a hybrid concept (Relation 1) that contains social objects, concrete entities (as Substance 446), and even meta-level categories. Each child synset has been mapped appropriately.

45Referring to Location, we ﬁnd roles (There, Here, Home, Base, Whereabouts), instances (Earth), and geometric concepts like Line, Point, etc.) 46“The stuff of which an object consists”.

88

Psychological feature contains both mental objects (Cognition47) and events (Feeling 1). We consider Motivation as a material role, so to be added to lower levels of the taxonomy of mental objects. The classiﬁcation of qualities deals mainly with adjectives. This alignment focuses on the WORDNET database of nouns; nevertheless our treatment of qualities foreshadows a semantic organization of the database of adjectives too, which is a current desideratum in the WORDNET community. The ﬁnal results of our mapping are sketched in Table 5. As one can see, a substantial taxonomy rearrangement has been performed. The application of the explicit distinctions of DOLCE helped clarifying the meaning of WORDNET senses. We believe that strong (and explicit) ontological distinctions should also help reducing the risk of classiﬁcation mistakes in the ontology development process, and simplifying the update and mainte- nance process. This work, recently named ONTOWORDNET, is still ongoing: we are further reﬁning our methodology and extending the conceptual analysis of the hierarchic levels of WORDNET taxonomy.

47“The psychological result of perception, and learning and reasoning”.

89

Abstraction 1 Film Attribute Part$Portion Color Body Part Chromatic Color Substance$Matter Measure$Quantity$Amount$Quantum Body Substance Relation 1 Chemical Element Set 5 Food$Nutrient Space 1 Part$Piece Time 1 Subject$Content$Depicted Object Act$Human Action$Human Activity Event 1 Action 1 Fall 3 Activity 1 Happening$Occurrence$Natural Event Forfeit$Forfeiture$Sacriﬁce Case$Instance Entity$Something Time$Clip Anticipation Might-Have-Been Causal Agent$Cause$Causal Agency Group$Grouping Cell 1 Arrangement 2 Inessential$Nonessential Biological Group Life Form$Organism$Being$. . . Citizenry$People Object$Physical Object Phenomenon 1 Artifact$Artefact Consequence$Effect$Outcome. . . Edge 3 Levitation Skin 4 Luck$Fortune Opening 3 Possession 1 Excavation$. . . Asset Building Material Liability$Financial Obligation$. . . Mass 5 Own Right Cement 2 Territory$Dominion$. . . Bricks and Mortar Transferred Property$. . . Lath and Plaster Psychological Feature Body Of Water$Water Cognition$Knowledge Land$Dry Land$Earth$. . . Structure Location Feeling 1 Natural Object Motivation$Motive$Need Blackbody Full Radiator State 1 Body 5 Action$Activity$Activeness Universe$Existence$Nature$. . . Being$Beingness$Existence Paring$Paring Condition$status Damnation$Eternal Damnation

Table 4: WORDNET’s Top Level.

90

Endurant Perdurant Physical Endurant Eventive Amount of matter Accomplishment body substance accomplishment$achievement chemical element Stative mixture State compound$chemical compound condition$status mass 5 cognitive state ﬂuid 1 existence Physical Object death 4 Agentive Physical Object degree life form$organism$being$. . . medium 4 citizenry relationship 1 sainthood relationship 2 ethnic group conﬂict Non-agentive Physical Object Process body of water$water decrement 2 land$dry land$earth$. . . increment body$organic structure shaping artifact$artefact activity 1 biological group chelation kingdom execution collection activity 1 blackbody$full radiator Quality body 5 Physical Quality universe$existence$nature$creation position$place Feature chromatic color edge 3 Temporal Quality skin 4 time interval$interval paring$parings Abstract opening 3 Quality Region excavation$hole in the ground space 1 Non-physical Endurant time 1 Mental Object time interval$interval cognition chromatic color motivation Set Social Object set 5 Non-agentive Social Object Proposition rule$prescript statement 1 law symbol circuit 5 Agentive Social Object

social group

Table 5: Mapping WORDNET into DOLCE.

91

12 A core Ontology of Services

This section has been developed in cooperation with Peter Mika, Marta Sabou of the Vrije Universiteit of Amsterdam, and Daniel Oberle of the Institute AIFB of the University of Karlsruhe.

12.1 Introduction

This Technical Report covers original work by the authors on an Ontology of Services and Service Descriptions. This work has been initiated within the European WonderWeb project [1]. The WonderWeb architecture envisages a tight integration between web-based KR languages, ontology learning and manipulation tools, foundational ontologies and ontol- ogy building methodologies. WonderWeb also provides an infrastructure that facilitates plug’n’play engineering of ontology-based modules and, thus, the development and maintenance of comprehensive Semantic Web applications, an infrastructure which is called Application Server for the Semantic Web (ASSW) [68]. It facilitates re-use of existing modules, e.g. ontology stores, editors, and inference engines, combines means to coordinate the information ﬂow be- tween such modules, to deﬁne dependencies, to broadcast events between different mod- ules and to translate between ontology-based data formats. Since software modules come as black boxes of code, descriptions need to be attached to them in order to facilitate their discovery. As a result, the ASSW features a registry that stores descriptions of the module and its API. Such descriptions adhere to an ontology which is not only used for module and API discovery, but also for manual classiﬁcation, connectivity and implemen- tation tasks. An Application Server for the Semantic Web can therefore be considered as semantic middleware. Additionally, there exists the possibility to offer a module’s func- tionality by another paradigm. E.g., the module might not only be represented as one object revealing a particular API, but its functionality may also be accessible as separate web services. This is achieved by translating a module’s ontological API description into corresponding web service descriptions. Existing conceptualizations of web services, such as the Web Services Architecture (WSA) [6] are informal and thus cannot avoid ambiguities even in the very deﬁnition of web services (see Section 12.7). Ontologies for the descriptions of web services, in particular DAML-S [19] and its successor OWL-S, attempt to cater for both worlds, but make no distinction as to what are general aspects of services and what are the notions speciﬁc to software or web services in particular. As a result, confusion arises as to the nature of objects comprising and processed by web services (see Section 12.6). Therefore, the initiative was taken within the project to create an Ontology of Ser- vices using the DOLCE foundational ontology, which has been also developed within the project. The resulting “upper ontology” of services based on well-founded principles is expected to inﬂuence (support) the design of more speciﬁc ontologies, such as the one designed for the description of software modules in the ASSW use case. It was also con- ﬁrmed that the Ontology of Services would help in clearing up otherwise fuzzy deﬁnitions of concepts related to web services and in pointing out inconsistencies or ambiguities in

92

conceptualizations such as the WSA document. The Ontology of Services is thus part of a layered architecture of ontologies developed within WonderWeb (cf. Figure 9). On the one hand, it is an extension (module) to the DOLCE foundational ontology [63]. In particular, it makes extensive use of the Ontology of Descriptions (also called Descriptions & Situations or D&S) available in the extended version of DOLCE, called DOLCE+ [36] (see also Section 12.4). On the other hand, the Ontology of Services generalizes notions of existing conceptualizations of web services or web service descriptions such as the DAML-S [19], the Web Services Architecture [6] or the Ontology of Software Modules used within the ASSW [67]. More speciﬁcally, the Ontology of Services covers all kinds of services, with information services as a special case. At the bottom layer of the architecture we ﬁnd domain-level ontologies. An example of such an ontology is the ontology of Semantic Web tools, which provides descriptions directly processed by the ASSW.

DOLCE

Requirements

Descriptions & Situations

Design

WSA DAML-S ASSW Core Ontology of Services

Domain and application ontologies

Figure 9: Ontology stacking in WonderWeb.

Our method was a combination of a bottom-up and a top-down approach. On the one hand, ontologies in the lower layers provided representation requirements for the higher layers, which abstracted their concepts and relationships. On the other hand, the upper layers provided design guidelines to the lower layers. In the following, we will use the example of a typical (but hypothetical) web-based ﬂight booking service to illustrate some of the notions introduced.

12.2 Motivation

We share the motivation of the DAML coalition that descriptions of (web) services should be formulated according to an ontology in order to support the automation of service related task. While DAML-S deﬁnes service related concepts in relation to each other, it lacks the formal semantics to relate these concepts to the basic categories of philosophy, linguistics or human cognition. Typically for a domain ontology, there is no ﬁrm class or property hierarchy (most classes and properties are direct subclasses of the top level concept) and several relations take Thing as their domain or range. Part of the missing semantics is in the text of the document, while some are left to the reader or future work to decide. We believe that this situation is not satisfactory: the level of commitment in DAML-S will need to be raised if it is to support the complex tasks put forward by the coalition (for

93

a description of these tasks, see [19, 6]). Further axiomatization through alignment to a foundational ontology will help to exclude terminological and conceptual ambiguities due to unintended interpretations. This capacity will be critical if DAML-S is to be employed on a global scale, where the meaning of descriptions will need to be constantly negotiated. Axiomatization is not without dangers of its own: it may lead to the creation of an overly restrictive, rigid ontology which would require a commitment that is difﬁcult to achieve on a global scale (see [88] for an analysis of the contradiction between the for- mality, sharing scope and stability of knowledge). However, we believe that this dan- ger is mitigated by the design of DOLCE. While extensively researched and formalized, DOLCE is created with minimality in mind and includes only the most reusable and widely applicable upper-level categories [63]. DOLCE also calls for a careful isolation of the fundamental ontological options and their formal relationships and is built with mod- ularization in mind. This means that DOLCE can avoid to become a single, monolithic upper-ontology that would be rejected by its users. Note that DOLCE also allows us to observe minimality. In fact, our ontology is chieﬂy a combination of basic DOLCE and two extensions (an Ontology of Descriptions and an Ontology of Planning). To these existing ontologies less than 10 new concepts and 5 new properties were needed to be added to get to the core Ontology of Services.

12.3 Methodology

For the engineering of the Ontology of Services, we have chosen to follow a variation of ONIONS, the Ontologic Integration of Naive Sources methodology [38]. ONIONS has been successfully applied in the past for various developments (e.g. an ontology of ﬁshery services for the FAO of the UN). The methodology consists of the ﬁve steps shown below, which result in a new module (domain-speciﬁc extension) to a given foundational ontol- ogy (FO). Foundational ontologies such as DOLCE are explicitly designed as upper-level frameworks for analyzing, harmonizing and integrating existing ontologies and metadata standards [63].

1. Re-engineering. In the re-engineering phase, the sources are acquired and trans- formed in a uniform representation (data format).

2. Integration. In this step the sources are integrated in a logical sense. For example, distinctions between classes and instances are made, data types are harmonized etc.

3. Alignment. During alignment, concepts and relationships of the sources are char- acterized in terms of the concepts and relationships of a Foundational Ontology (FO). For example, at this stage classes described in the source ontologies are de- ﬁned as subclasses of the most speciﬁc superclass available in the FO.

4. Merging. In the last step, concepts described in various sources are merged when they carry the same meaning with respect to the application scenario.

The sources in our case were the WSA document, DAML-S, parts of the Common Information Model (CIM) and the Ontology of Software Modules used within the ASSW.

94

Instead of direct alignment to the DOLCE foundational ontology, we decided to de- velop a Core Ontology of Services based on D&S (which is an extension to DOLCE) and aligned the sources to this ontology. This two-stage alignment is a common technique when the conceptual gap between the source ontologies and the foundational ontology is large. Also, formulated at a more generic level, one may expect the core ontology to be reusable later in other scenarios (e.g. our Ontology of Services may be reused for descriptions of purely commercial services. However, our sources are geared speciﬁcally towards information services, which means that the resulting ontology may lack some of the notions necessary for the matching and retrieval of commercial service offerings). The remaining sections of this technical report is organized as follows. The Ontology of Descriptions (D&S) is introduced in Section 12.4. The Core Ontology of Services is presented in Section 12.5. Experiences with the alignment of the WSA document, DAML-S, and the Application Server’s ontology are discussed in Sections 12.7 to 12.9, respectively.

12.4 Descriptions as entities

12.4.1 Motivation

Foundational ontologies in WonderWeb are ontologies that contain a speciﬁcation of domain-independent concepts and relations based on formal principles derived from lin- guistics, philosophy, and mathematics. Formal principles are needed to allow an explicit comparison between alternative ontologies. Examples of formal principles are spatio- temporal localization, topological closure, heterogeneity of parts, dependency on the in- tention of agents, etc. We refer to [63] for a detailed explanation. While formalizing the principles governing physical objects or events is (quite) straight- forward, intuition comes to odds when an ontology needs to be extended with non- physical objects, such as social institutions, organizations, plans, regulations, narratives, mental contents, schedules, parameters, diagnoses, etc. In fact, important ﬁelds of inves- tigation have negated an ontological primitiveness to non-physical objects [65], because they are taken to have meaning only in combination with some other entity, i.e. their in- tended meaning results from a statement. For example, a norm, a plan, or a social role are to be represented as a (set of) statement(s), not as concepts. This position is documented by the almost exclusive attention dedicated by many important theoretical frameworks (BDI agent model, theory of trust, situation calculus, formal context analysis), to states of affairs, facts, beliefs, viewpoints, contexts, whose logical representation is set at the level of theories or models, not at the level of concepts or relations. On the other hand, recent work (e.g. [65]) addresses non-physical objects as ﬁrst- order entities that can change, or that can be manipulated similarly to physical entities. This means that many relations and axioms that are valid for physical entities can be used for non-physical ones as well. Here we support the position by which non-physical entities can be represented both as theories/models and as concepts with explicit reiﬁcation rules, and we share the following motivations:

1. Technology and society are full of reiﬁcations, for example when we divide human

95

experience into social, cultural, educational, political, religious, legal, economic, industrial, scientiﬁc or technological experiences

2. In realistic domains, specially in socially-intensive applications (e.g. law, ﬁnance, business, politics), a signiﬁcant amount of terms convey concepts related to non- physical entities, and such concepts seem to be tightly interrelated

3. Interrelations between theories are notoriously difﬁcult to be manipulated, then it would be an advantage to represent non-physical objects as instances of concepts instead of models satisfying some theory

4. For many domains of application, we are faced with partial theories and partial models that are explicated and/or used at various detail levels. Partiality and gran- ularity are two more reasons to have some theories and models manipulated as ﬁrst-order entities

5. Natural languages are able to reify whatever fragment of (usually informal) theo- ries and models by simply creating or reusing a noun. Once linguistically reiﬁed, a theory or a model (either formal or informal) enters a life-cycle that allows agents to communicate even in presence of partial (or even no) information about the rei- ﬁed theory or model. The Web contains plenty of examples of such creatures: catalog subjects or topics, references to distributed resources, unstructured or semi- structured (but explicitly referenced) contents, such as plans, methods, regulations, formats, proﬁles, etc., and even linguistic elements and texts (taken independently from a particular physical encoding) can be considered a further example

6. Recent (still) unpublished work by one of the authors reports that more 25% of WordNet (v1.6) noun synsets [28] can be formalised as non-physical object classes

In general, we feel entitled to say that representing ontological (reiﬁed) contexts is a difﬁcult alternative to avoid, when so much domain-oriented and linguistic categorisations involve reiﬁcation. However, we also want to provide an explicit account of the contextual nature of non-physical entities and thus aim for a reiﬁcation that accounts to some extent for the partial and hybrid structure of such entities. From the logical viewpoint, any reiﬁcation of theories and models provides a ﬁrst order representation. From the ontological engineering viewpoint, a straightforward reiﬁ- cation is not enough, since the elements resulting from reiﬁcation must be framed within an ontology, possibly built according to a foundational ontology.

12.4.2 An Ontology of Descriptions and Situations

The Descriptions and Situations ontology (D&S) [37] is an attempt to deﬁne a theory that supports a ﬁrst-order manipulation of theories and models, independently from the particular foundational ontology it is plugged in. In general, D&S commits only to a widespread and very ancient ontological distinc- tion between ﬂux, or an unstructured world or context, and logos, or an intentionality. D&S is neutral with respect to realism issues, such as whether we conceive a structure

96

because it is in the ﬂux, or because it is in our intentionality [64]. D&S as a representa- tion mechanism makes no pretense in either direction. Hence, a ﬂux can have as many inherent structure (parts, boundaries, qualities, etc.) as one might want to believe in or might claim to have discovered, but without a logos, a ﬂux would have no description of that structure. When logos is applied to the description of the ﬂux, some structure emerges (this reﬂects the cognitive structuring cognitive process [55]). The emerging structure is not necessarily equivalent to the actual structure. Due to its neutrality with respect to realism, D&S can generalize the ﬂux/logos dis- tinction, in order to obtain an epistemological layering. Epistemological layering consists of assuming that any logical structure Li (either formal or capable of being at least partly formalised) is built upon a ﬂux-like structure that it describes according to a more abstract, logos-like theory Ti (either formal or capable of being at least partly formalised). In other words, Ti describes what kind of ontological commitment Li is supposed to have within the epistemological layer that is shared by the encoder of an ontology. Epistemological layering reﬂects the so-called ﬁgure-ground shifting cognitive pro- cess [55]. Moreover, most assumption-makings in any domain of interest apply episte- mological layering (several names have been used to refer to ﬂux-like structures: tacit knowledge, context, substrate, etc.). D&S implements reiﬁcation rules for any Ti, called a description, and a basic frame- work for any Li, called a situation48, and for their elements. Flux-like structures are not reiﬁed in D&S, but they result to be the structures that include all the (ground) logical dependencies of the components of a situation S classiﬁed within an ontology O, plus any additional elements that could be part of the ground con- text of S according to some encoder of O, but that are not inside O. A ﬂux-like structure is called a state of affairs (SOA) in D&S.

12.4.3 Implementing the Ontology of Descriptions in DOLCE

DOLCE [63] has four top categories: endurant (including object- and substance-like enti- ties), perdurant (event- and state-like entities), quality (individual attributes), and abstracts (mainly conceptual “regions” for structuring attributes). Within DOLCE, D&S is plugged in as follows. A situation is a (new) top category, a description is a non-physical endurant. Description is disjoint from situation. A descrip- tion may be satisﬁed by a SOA. The satisfaction relation is reiﬁed in D&S as a ﬁrst-order referenced-by relation. A description satisﬁed by a SOA is an s-description. A SOA satisfying a description is a situation.49

Concerning the reiﬁcation of the elements of a theory, the descriptions that reify a selection rule on DOLCE regions (e.g. speed limit or visibility) are called parameters, the descriptions that reify a functional property of DOLCE endurants (e.g. citizen or

48We are keeping these names for the historical reasons. Other intuitive names have been proposed so far, e.g. representation, conceptualisation, or schema for description, and setting, Gestalt, or conﬁguration for situation. 49A situation can satisfy a (s-)description in many ways, so that we can build a taxonomy of satisfaction (referenced by) relations.

97

judge) are called functional roles, and the descriptions that reify sequences of DOLCE perdurants (e.g. schedule or pathway) are called courses. In D&S for DOLCE, descriptions have only other descriptions as parts. S-descriptions have courses, functional roles, and parameters as components. (See Fig. 10.) Between such components some relations hold: modality-target holding between functional roles and courses, and requisite-for holding between parameters and either functional roles or courses. Modality-target reiﬁes the modal dependence between a functional property, and a sequence, while requisite-for reiﬁes the logical dependence between a selection rule and either functional properties or sequences.

Figure 10: The DOLCE-Lite+ Library

Situations and s-descriptions are systematically related. The basic relation is selects, and it reiﬁes the instantiation relation between an individual in a model and a concept in a theory. Within DOLCE, selects relates components of an (s-) description to instances of DOLCE categories. Intuitively, selects(x,y) binds an individual y classiﬁed in a DOLCE category to a situation s that is referenced (satisﬁes) the s-description d that has x as a component. In particular: parameters are valued-by regions, f-roles play endurants, and courses sequence perdurants. Examples of descriptions and situations include:

• A clinical condition (situation) has an associated diagnosis (s-description) made by some agent.

• A case in point (situation) is constrained by a certain norm (s-description)

• A murder (situation) has been reported by a witness (functional role) in a testimony (s-description)

• Information science as a topic (s-description) references the manipulation of data structures (situation), both as a pure or applied science (parent s-descriptions)

98

• A person (endurant) plays the role of judge (functional role) in the context of a constitutive Law (s-description)

• 40kmph (region) is the value for a speed limit (parameter) in the context of an accident (state of affairs) described as a speed excess case (situation) in an area covered by trafﬁc Law (s-description)

D&S results to be a theory of ontological contexts because it is capable to describe various notions of context (physical and non-physical situations, topics, provisions, plans, assessments, beliefs, etc.) as ﬁrst-order entities.

12.5 The Core Ontology of Services

The core ontology of services consists of a repeated application of the Ontology of De- scriptions (D&S). D&S provides reiﬁcation rules for the properties by which varieties of the three basic categories of DOLCE (regions, endurants and perdurants) are deﬁned. Such reiﬁed rules are called parameters, roles and courses. Containers of such reiﬁed rules are called ”de- scriptions” D&S is a design pattern, for modelling non-physical contexts such as views, theories, beliefs, norms etc. An important distinction is made in D&S between (the com- ponents of) descriptions (the reiﬁed rules) and (components of) a particular model, also called state-of-affairs (SOA): elements of a SOA (regions, endurants and perdurants) may play the parameters, roles and courses of a description, in which case the SOA is under- stood as a situation (case) for a particular description. However, the same SOA may be interpreted according to other, alternative descriptions. This captures an important fea- ture of contexts, namely that multiple overlapping (or alternative) contexts may match the same world or model. For more information on D&S, we refer the reader to Section 12.4. Service descriptions as non-physical contexts are ideally suited as applications of D&S. Descriptions of services can be considered as views from various perspectives on a series of activities that constitute the service for the various parties involved. In other words, service descriptions exhibit the same distinction between what is offered, expected or planned (descriptions, theories) and the elements that consist a particular model of the world. Currently, we have considered ﬁve frequently occurring contexts regarding services, where each is a separate description of the same service in the D&S sense. More views may be added in the future when needs arise. Figure 11 shows their interrelationships.

1. Service Offering (Description). The Service Offering is the viewpoint of the legal entity providing the service. Much like commercial advertisements, the service offering may not describe entirely how the service will be carried out. This can also be considered as a proposal for a contract (agreement) for a service.

2. Service Requirements (Description). This is the counterpart of the offering in that it comprises the expectations of the requestor of the service. Requirements are often ﬂexible, concerning only a subset of the tasks, roles and parameters of service activities (but might also contain others).

99

3. Service Agreement (Description). Once an agreement is reached between the provider and the requestor of the service, their joint understanding regarding the service may be described in a Service Agreement. Agreement means an under- standing of the service as providing some value to the requestor, which may or may not be the same as the originally offered functionality of the service (in an extreme case, even doing nothing can be a service: consider the NOP command of machine language.) 50

4. Service Assessment (Description). Typically, when an agreement is reached mea- sures are taken to monitor, assess and control the execution of the service provided. Assessment concerns matching the service activities against the agreement.51 Ser- vice assessment may be executed by a third party and may also involve aspects not even mentioned in the above three descriptions, e.g. the cleanliness of a hotel room may be checked by looking for dust on the TV sets. In the web services area, assessment is of particular concern to those interested in the management of web services.52

5. Service Activities Description. This is a description of the social conventions regarding the execution of a service, whether a written code of practice (ISO) or unwritten norm. This view is the basis for legal action once a service deviates from the norms in ways not foreseen in the agreement.

12.5.1 The Service Offering Description

In the following, we detail the structure of a Service Offering Description (see Figure 12). All other views are similar in nature. The Service Offering Description is an S-Description, more precisely a Promise which has at least a single Service Task as temporary component.53 A Task in DOLCE+ is a Course, which has only other tasks as temporary components and sequences at least one activity. A Task can also have a Situation as its precondition or postcondition, which may or may not relate to (elements of) a situation for the description in which the Task is deﬁned.54

50Independently from the fact that it may described, similarly to WSA we believe that in general an agreement (written or unwritten) between provider and requestor is necessary to talk of a service. Spam, or a dolphin saving someone in the middle of the ocean is not considered a service, no matter how useful it proves afterwards. 51In an ideal world such a function would be meaningless. In reality, contracts are incomplete, since it is difﬁcult to imagine all possible outcomes ﬂowing from the agreement. Also, violations and the resulting penalties are often accepted rather than adhering to the contract (a kind of control strategy). 52The WSA document, for example, stresses the manageability of web services as this is a key feature to companies interested in providing management platforms for web services. The CIM standard was also developed for creating a common format for exchanging information between management systems (Software designed to manage the IT assets of companies, including both their software and hardware environment). 53In the following, all categories and relations not printed in Italics are deﬁned in DOLCE+, see Section 12.4. 54We decided not to give different names to elements of the offering such as Service Offering Task. Unity criteria is given by the structure, i.e. the entire description.

100

Figure 11: Relationships between the various views on a service.

We further deﬁne two disjoint subclasses of Task, Service Task and Computational Task. Service Tasks sequence only Service Activities and have only Service Tasks as temporary components. Similar statements hold for Computational Tasks. As we will see, the emergent distinction is that between tasks which require computational execution and work with information objects and tasks which involve physical objects. A number of concepts from the Ontology of Planning are likely to be useful con- junction with the Core Ontology of Services. These include the division of tasks into elementary and complex tasks, and the construction of complex tasks from elementary ones. This part of the ontology is not detailed here, but can be consulted at http: //www.isib.cnr.it/infor/ontology/DOLCE.html. The chief difference between tasks and activities is that of between a plan and a partic- ular execution of the plan: a plan represents possible sequences of execution. Examples of Computational Task are the reservation of a ﬂight and the collection of payment, both in the sense of a transaction in an information system, even if it may be implemented in a number of ways. A Service Task can be ﬂying the passenger (some passenger, not a particular one) to some destination. Again, this may be carried out in several ways. In our ontology we also deﬁne a number of roles that are most commonly found in service descriptions. Two common agentive roles are introduced, namely Requestor and Provider. These are described as subclasses of the legally-constructed-person notion imported from a legal extension of DOLCE (Legally constructed persons are agentive functional roles played by socially constructed persons). In agreement with WSA, we conceive them as legal entities so that they can enter into agreement regarding a service. Examples are a passenger role (requestor of the booking service) and the role of the travel agency (provider of the service). We also conceive a third kind of agent role, namely that of the Executor. This can be used for modelling delegation. Roles that are played by instruments of activities are called Instrumentality Roles in DOLCE-Lite+. Input and Output are examples of such roles. Computational Input and Computational Output are kinds of input and output that are played only by information objects and only have exploitation within Computational Tasks.

101

Figure 12: UML diagram of the Service Offering Description.

102

12.5.2 Service Situations

Our Service Offering Description introduced above stipulates the existence of a number entities in situations that satisfy the description. We also add some elements which may be useful in describing the settings of service executions. A Service Activity is kind of Activity (a perdurant in DOLCE). A Computational Ac- tivity is a special kind of Service Activity which has only information objects or binary software as participants (Computational activity is another name for software as a perdu- rant). An example of a Service Activity would be ﬂying Joe, a particular passenger, to his destination. An example of a Computational Activity would be the execution of the procedure that reserves a particular seat for a particular passenger. Information Object is a non-physical endurant in DOLCE, which may be expressed according to a Description System. Examples of Description Systems are RDF or WSDL. As described in 12.6, Software as Algorithm is an information object, while Software as Binary represents its physical counterpart (more speciﬁcally, Software as Binary is said to be the instrument of a Computational Activity, while information objects are data-for the Computational Activity). Assuming a procedural programming paradigm as common in the web services liter- ature, Software as Algorithm is modelled as set of Methods. Methods in turn may have a number of Parameters as parts. Methods and Parameters are necessarily identiﬁed by names. Parameters must also have exactly one type. We further introduce the minimal notions necessary for modelling information repre- sentation, partly based on earlier work on an ontology of communication and interpreta- tion [37]. See Fig. 13 for an illustration. In this example, Joe is a physical agent, but has a representation counterpart, namely the information object that is used to reference (identify) Joe in the software. The in- formation object represents a meaning, an S-Description which may involve the entity in question. A Literal may extrinsically represent that information object, in which case the literal is said to be the name of the entity.

12.5.3 Axiomatization

Service O f fering Description(x) →promise(x) ∀x.Service O f fering Description(x) → ∃y.temporary component(x,y)∧Service Task(y) Service Requestor(x) →Legally Constructed Person(x) Service Provider(x) →Legally Constructed Person(x) Service Executor(x) →agent role(x)

Service Input(x) →non agentive functional role(x) Computational Input(x) →Service Input(x) ∀x,y.Computational Input(x)∧played by(x,y) →In formation Ob ject(y) ∀x,y.Computational Input(x)∧has exploitation within(x,y) → Computational Task(y)

Service Output(x) →non agentive functional role(x)

103

Figure 13: Modelling information representation.

Computational Output(x) →Service Output(x) ∀x,y.Computational Output(x)∧played by(x,y) →In formation Ob ject(y) ∀x,y.Computational Output(x)∧has exploitation within(x,y) → Computational Task(y)

Conditional Output(x) →Service Output(x)

Computational Task(x) →Task(x)

∀x,y.Computational Task(x)∧sequences(x,y) →Computational Activity(y) ∀x,y.Computational Task(x)∧temporary component(x,y) →Computational Task(y) Service Task(x) →Task(x) ∀x,y.Service Task(x)∧sequences(x,y) →Service Activity(y) ∀x,y.Service Task(x)∧temporary component(x,y) →Service Task(y)

Service Activity(x) →Activity(x) Computational Activity(x) →Activity(x) ∀x,y.Computational Activity(x)∧participant(x,y) → In formation Ob ject(y)∨So ftware As Binary(y)

¬(Computational Activity(x)∧Service Activity(x)) ¬(Computational Task(x)∧Service Task(x))

So ftware as Algorithm(x) →In formation Ob ject(x) So ftware as Binary(x) →Physical Endurant(x)

104

Literal(x) →Concrete Datatype(x) Identi fier(x) →Literal(x)

Method(x) →In formation Ob ject(x) ∀x,y.Method(x)∧name(x,y) →Identi fier(y)∧̸ ∃zy ̸= z∧name(x,z)∧Identi fier(z)

Formal Parameter(x) →In formation Ob ject(x) ∀x,y.Formal Parameter(x)∧name(x,y) →Identi fier(y)∧¬∃zy ̸= z∧name(x,z)∧Identi fier(z) ∀x,y.Formal Parameter(x)∧name(x,y) →Concrete Datatype(y)∧¬∃zy ̸= z∧name(x,z)∧Concrete Datatype(z)

type(x,y) →Property(x,y) type(x,y) →Formal Parameter(x) type(x,y) →Concrete Datatype(y) type o f(x,y) →Property(x,y) type o f(x,y) →Concrete Datatype(x) type o f(x,y) →Formal Parameter(y) type(x,y) ↔type o f(y,x)

extrinsically represented by(x,y) →extrinsic relation(x,y) extrinsically represented by(x,y) →In formation Ob ject(x) extrinsically represented by(x,y) →Literal(y) extrinsically represents(x,y) →extrinsic relation(x,y) extrinsically represents(x,y) →Literal(x) extrinsically represents(x,y) →In formation Ob ject(y) extrinsically represents(x,y) ↔extrinsically represented by(y,x)

name o f(x,y) →extrinsic relation(x,y) name o f(x,y) →Literal(x) name o f(x,y) →Endurant(y) name(x,y) →extrinsic relation(x,y) name(x,y) →Endurant(x) name(x,y) →Literal(y) name(x,y) ↔name o f(y,x)

data for(x,y) →used in(x,y) data for(x,y) →In formation Ob ject(x) data for(x,y) →Computational Activity(y) data(x,y) →situation o f use o f(x,y) data(x,y) →Computational Activity(x) data(x,y) →In formation Ob ject(y) data(x,y) ↔data for(y,x)

task input(i,t) ↔Task(t)∧Input(i)∧modality target(i,t)

105

task output(o,t) ↔Task(t)∧Output(i)∧modality target(o,t)

NameO f(x,y) ↔Literal(x)∧Entity(y)∧∃z,w.In formation Ob ject(z)∧Meaning(w)∧ extrinsically represents(x,z)∧represents(z,w)∧involves(w,y)∧refers to(z,y)

input for(io,a) ↔In formation Ob ject(io)∧Activity(a)∧∃d,t,r.Serive O f fering- Description(d)∧Agentive Functional Role(r)∧Task(t)∧Input(r)∧task input(r,t)∧ sequences(t,a)

requestor in(e,a) ↔ Endurant(e)∧Service Requestor(a)∧plays(e,a)∧participant in(e,a)

provider in(e,a) ↔ Endurant(e)∧Service Provider(a)∧plays(e,a)∧participant in(e,a)

sequences(t,a)∧part(a,b) →sequences(t,b)

participant −in(e, p)∧setting(p,s) →setting(e,s)

12.6 Deﬁning web services: On the border of Infolandia

The greatest obstacle in conceptualizing web services seems to be the name itself, which is severely overloaded in meaning. Here are just some of the various deﬁnitions found in the literature:

1. A web service is a software system identiﬁed by a URI, whose public interfaces and bindings are deﬁned and described using XML. Its deﬁnition can be discovered by other software systems. These systems may then interact with the web service in a manner prescribed by its deﬁnition, using XML based messages conveyed by internet protocols [6].

2. A web service is viewed as an abstract notion that must be implemented by a con- crete agent. The agent is the physical entity (a piece of software) that sends and receives messages, while the service is the abstract set of functionality that is pro- vided. To illustrate this distinction, you might implement a particular web service using one agent one day (perhaps written in one programming language), and a different agent the next day (perhaps written in a different programming language). Although the agent may have changed, the web service remains the same (also from [6], although in clear contradiction to the previous def.)

3. A service is an active program or a software component in a given environment that provides and manages access to a resource that is essential for the function of other entities in the environment. A web service is a service that abides by a speciﬁc framework to offer its services. The framework provides the means to describe and discover the service, audit its service offering, and integrate the service with other

106

services to offer higher-level services.55

4. Loosely speaking, a web service is a piece of functionality (an object, a compo- nent, an application, a database call) that can be invoked over a network using a predeﬁned syntax.56

5. First of all, we start with an application that you want others to use. That is, you have a piece of software that initiates or accepts business transactions, provides or updates enterprise information, or perhaps manages the very systems and processes that make your business run. You may want to make this accessible to people in other parts of your organization, or a business partner, or a supplier, or a customer. We’re really thinking here about software-to-software communication rather than the person-sitting-at-a-browser-talking-to-server-software situation, though it turns out that web services can be used there as well.57

6. Among the most important Web resources are those that provide services. By “ser- vice” we mean Web sites that do not merely provide static information but allow one to effect some action or change in the world, such as the sale of a product or the control of a physical device. The Semantic Web should enable users to locate, se- lect, employ, compose, and monitor Web-based services automatically... Any Web- accessible program/sensor/device that is declared as a service will be regarded as a service. DAML-S does not preclude declaring simple, static Web pages to be ser- vices. But our primary motivation in deﬁning DAML-S has been to support more complex tasks like those described above. [19]

These deﬁnitions call one of the following (or both, as in the case of WSA) a web service:

1. An information system, invokeable using particular technologies such as XML, i.e. accessible through the Web. This is often confused with the functionality attributed to the service, even though functionality of a tool is contingent on usefulness in a particular situation.58

2. Some functionality (service) provided and a task to be fulﬁlled. This task is external to the software, e.g. a business transaction.

3. An interface to a software or heterogeneous system, which makes it web accessible. Having a publicly available description of a service is often considered a require- ment to call it a web service. As a consequence, this view often goes as far as equating the web service to (the description of) an interface.

55cf. http://www.informit.com under “Web Development”, “Web services”. 56cf. http://www.informit.com, Article “Web Services Part 3: What Are Web Services” by Alex Nghiem. 57cf. http://searchwebservices.techtarget.com, deﬁnition of web services 58Similar phenomena exist with real world objects: a hammer becomes a “tool” instead of an artifact when it is in the hands of someone who knows how to use it. Otherwise, it’s an amount of matter.

107

We have to separate these concepts in order to modularize our descriptions of ser- vices. It seems that at the heart of the entanglement between software, functionality and interfaces lies a disregard to the fact that web services exist on the boundary of the world inside an information system (Infolandia) and the outside world: The scope of “Web services” as that term is used by this working group is somewhat different. It encompasses not only the Web and REST Web services whose purpose is to create, retrieve, update, and delete information resources but extends the scope to consider services that perform an arbitrarily complex set of operations on resources that may not be “on the Web.” Although the distinctions here are murky and controversial, a “web service” invocation may lead to services being performed by people, physical objects being moved around (e.g. books delivered). [6] Thus web services carry out computational activities to support a service. But can we call the software a service? We believe that is not the case: usefulness, which is an essential property of a service, arises from the entire process involving real world as well as computational activities. In the case of a ﬂight booking service, the customer of the service values the fact that as a result of the service, he will be able to transport himself to one place or another. The fact that part of the execution involves an interaction between the travel agent and the customer through an information system (e.g. a WWW site) is a mere implementation aspect from the customer point of view. This is not to say that there cannot exist services which concern purely information objects, e.g. the transformation of some data from one from to another. Most services offered via the Web, however, will not be pure information services. The curious positioning of web services holds a particular challenge for ontological modelling. Descriptions of web services are, in fact, descriptions of two parallel worlds. In Infolandia, the world consist of software manipulating (representations of) information objects. Activities are sequenced by computational processes. Meantime in the real world passengers and airplanes are ﬂying to their destinations. The connection between these worlds is simply that some of the information objects in Infolandia are symbols of (or identiﬁers for) real world objects. Also, computational activities comprise part of the service execution in the real world. For example, a booking needs to be entered by the travel agent into an information system, so that the airline would know which passengers to allow on the plane. Since software stands in between the information and the real world, it stretches the categories of foundational ontologies.59 Upon close inspection, it seems that the term software is also heavily inﬂicted by polysemy and refers to at least four different concepts:

1. An algorithm. An algorithm is like a tune in music, distinct from its notations or executions. Algorithm is an endurant in DOLCE terms.

2. The encoding of an algorithm in some kind of representation, e.g. binary or Java code. Encoding can be either in mind, on paper or any other form. This is software as information object, which is also an endurant.

59The problem is similar to modelling communication, which occurs in three layers: 1) meaning 2) symbols, expressions 3) physical signals transmitted through a channel. The ﬁrst two aspects are logical, while the last one is physical, yet part of the same process.

108

3. Static implementation of software, which is a ﬁle on someone’s computer with the executable code. Different from the previous category in that it’s a directly exploitable form. This kind of software is a perdurant or 4D object60.

4. The running system, which is the result of an execution. This is the form of software which manifests itself in the form electrical signals rising and dropping, the screen ﬂickering and sound coming out the machine. This form of software is a physical perdurant or 4D object.

The ﬁrst two items represent software as a product, while the latter two refer to the process nature of software.61 The two seem just as inseparable as the wave and particle nature of light: without hardware in the physical world, no software would exist. In other words, perdurancy mutually depends on endurancy: for each state of a perdurant (soft- ware), there is a state of an endurant (hardware) reﬂecting that perdurant. Nevertheless, when we want to separate the two aspects of software in our descriptions, we will talk about Software-as-Perdurant and Software-as-Endurant.

12.7 Alignment of the Web Services Architecture

The Web Services Architecture (WSA) document is a work of the similarly named work- ing group of the W3C, whose membership is almost exclusively comprised by industry representatives. The document is an effort by the W3C to create a conceptual framework of web services based, which matches the requirements collected in [4]. The document is also input to other web services related activities at the W3C, namely the XML Proto- col Working Group (responsible, among others, for SOAP), the Web Services Description Working Group (working on WSDL) and the Web Services Choreography Working Group (working on service composition). The WSA is still a work in progress62, which means that our comments may be outdated. In general, the document shows a great deal of confusion over the deﬁnition of a web service (see also Section 12.6). The current deﬁnes the web service as a software system and requires that web services are identiﬁed by a URI and their public interfaces and bindings are deﬁned and described using XML. However, the authors themselves express doubts whether it’s truly required for a web service to have a public description. The notion of binding is left undeﬁned. Mentioning XML as base technology is also somewhat awkward, considering that it only concerns representation (ASCII or Unicode is then also a requirement).63

60Strictly speaking software is a 4D object: while someone can sit on a chair at a certain point in time, it is not possible to make sense of software at a given point in time. 4D objects are not yet covered by DOLCE. 61Similar bipolar effect characterizes the difference between service and product in the commercial world. Products can be viewed as a service: if someone buys a house for lifetime rental, what he actu- ally buys is the right to live there for the end of his life. 62W3C Working Draft of May 14, 2003 63The intention of the deﬁnition is to stress the interoperability requirements for web services . The document tries to be neutral with regard to more web-service-speciﬁc protocols.

109

Only one section later, in contradiction with the earlier deﬁnition, a web service is called an abstract notion that is implemented by an agent (a software). While it’s not ex- plained what this abstract notion is, the document notes that the purpose of a web service is to provide some functionality on behalf of its owner.64 Further, in Section 1.6.2, the document returns to the original deﬁnition, when doubts are expressed in the comments whether the web service is the external code or an interface to some external code. Besides notes on the architecture, the document also provides a collection of “Core Concepts and Relationships”. Unfortunately, this is only available in text and pictures. (For that reason, we did not perform the actual physical alignment.) Here we go through the major concepts, skipping features of the entire architecture, acts and concepts related to the management of web services. Skipped: authentication, choreography description language, correlation, discovery, discovery service, feature, identiﬁer, intermediary, life cycle, management capability, management conﬁguration, management event, manager, manageable element, manage- ability interface, management metric, message exchange pattern, message header, mes- sage description language, message identiﬁer, reliable messaging, representation, resource, SOAP, WSDL.

Agent A program, i.e. a software acting on behalf of a legal entity. A deployed element, i.e. physical. sameAs SoftwareAsEndurant and it plays computational agent role

Choreography A choreography is a set of possible interactions between a set of services. A choreography is thus another description, which operates on the union of the regions, endurants and perdurants referenced by the individual service descriptions. A choreography expresses only possible interactions, and therefore it is distinct from a composite service, i.e. a possible realization of interacting services.

Deployed element Deployed element is the collective name for physical objects. Agents, services and descriptions are mentioned as kinds of deployed elements. Deployed element is introduced also as a unit of manageability.

Legal entity Same as our deﬁnition.

Message A “unit of interaction between agents”. Message is a functional role in communication played exclusively by information objects. (Pigeons carrying letters seem to be excluded )

Message Sender, Message Receiver Conceived as kinds of agents. We model sender and receiver as functional roles in communication.

Service Again a new deﬁnition, emphasizing the process nature of a service and the agreement needed: “A service is a set of actions that form a coherent whole from

64“The provider entity is the legal entity that provides an appropriate agent to implement a particular service.” How does one determine whether an agent is appropriate before an agreement is reached over the service? General feeling is that the industry community thinks of a web service as an extra interface to an existing line-of-business system, i.e. functionality is engrained.

110

the point of view of service providers and service requesters.” If we disregard the universal, objectivist view of a service, this seems to be close to the set of tasks performed by a service or the entire description.

Service Description A “set of documents” that describe the interface to and semantics of a service.

If set of documents is meant in a representation-independent way, its akin to an information object representing the service (offering) description.

Service Provider, Service Requester Conceived as kinds of agents. We model providers and requesters as functional roles in some description of a service.

Service Semantics “The semantics of a service is the contract between the service provider and the service requester that expresses the effect of invoking the service.” Clearly, this is the Service Agreement Description.

Service Task “A service task is a unit of activity associated with a service. It is denoted by a pair: a goal and an action; the goal denotes the intended effect of the task and the action denotes the process by which the goal is achieved.” Matches the DOLCE notion of a task.

12.8 Alignment of DAML-S

DAML-S divides information about a web service into three kinds of descriptions: pro- ﬁles, processes and groundings. The reason behind this separation are the different func- tions these descriptions are designed to support. Proﬁles are primarily intended for dis- covery and matching of service offerings and requests, therefore proﬁles contain metadata about the service (classiﬁcation, ratings, source) as well as inputs, outputs, preconditions and effects of the entire service. Process descriptions, on the other hand, support the composition of web services by describing the IOPEs of individual atomic services that may be identiﬁed within the service and valid sequences of executions. Lastly, grounding concerns the information necessary to invoke a web service over the internet. (All three kinds of descriptions are meant for machine processing.) The goal of all modularizations is a separation of concerns. Given some division of concerns, a modularization is optimal if it reduces the need for links between modules in order to attend to those concerns (overlapping or cross-cutting concerns are problematic as there is a need to duplicate information, see the difﬁculty of maintaining consistency between IOPEs in the process and the proﬁle). This suggests that related information, which is expected to be used in conjunction with the same concern, should be allocated to the same module. Without a history of usage of web services, it is not known at this point how the information available in web service descriptions would be used and therefore it is difﬁcult to tell if the divisions in DAML-S are indeed the optimal ones. Our ontology suggests one important dimension for modularization: the distinction between elements of the description (a plan) and a situation (its execution). However, we

111

leave further modularization dependent on future use cases for our descriptions (on the technical side, we are also waiting for a more versatile modularization mechanism than namespaces). Although the deﬁnition of a service is ambiguous even in the natural text description of DAML-S, for the sake of argument we considered an daml-s:Service as a Service Of- fering Description, which has the ServiceProﬁle and ServiceModel (also Service Offering Descriptions) as parts. Actors in the ServiceProﬁle are aligned as Agentive Functional Roles . The ServiceModel concept was aligned to our Service Task concept, while the individual control constructs were mapped to task components provided by the Ontology of Plans. In the Core Ontology of Services, the notions of Inputs and Outputs were modelled as Non-Agentive Functional Roles and not as relations in DAML-S. Nevertheless, alignment was possible by means of a composed relationship. On the other hand, the notion of preconditions and effects are inherited from the Ontology of Plans (task-precondition and task-postcondition) where they are modelled as Situations. As it was not related to the focus of work, we omitted the alignment of the particular grounding ontology for WSDL [18]. Nevertheless, the notion of Software is present in the Core Ontology of Services as Information Object that can be expressed according to any number description systems.65 WSDL could be considered as such a description system and modelled to the extent required to express groundings. To the observer, our ontology might seem to be more verbose than DAML-S. In fact, we decompose many of the relationships in DAML-S, such as the link between endurants and their representation in information systems. We also decompose the grounding re- lation of DAML-S between processes and software implementations. Our goal in these decompositions is to ﬁnd semantically distinct building blocks of these relationships and thus reconstruct semantics. In effect, DAML-S relationships may be easily recomposed from these blocks. For example, we may introduce a composed relationship between in- formation objects and tasks, which says that if an information object plays input and that input has exploitation within a given task, we might say that such an information object is input-for that task, mimicking the similar relationship in DAML-S.

12.8.1 Illustrated example

In this Section we show how the semantics of the Congo example of DAML-S could be represented by our Core Ontology of Services. For the purposes of this demonstration, we shortened the example to the part described in [61]. We begin with the Service Offering Description proposed by Congo Inc., called Con- goBuyOffering. CongoBuyOffering has a number of functional roles and tasks as parts.

CongoBuyO f fering(x) →Service O f fering Description(x) CongoCustomer(x) →Service Requestor(x) ∀x,y.CongoCustomer(x)∧temporary component o f(x,y) →CongoBuyO f fering(y) CongoProvider(x) →Service Provider(x)

65An alternative, more reﬁned representation we considered was to model Software as an S-Description, in the sense of an abstract algorithm.

112

∀x,y.CongoProvider(x)∧temporary component o f(x,y) →CongoBuyO f fering(y)

In all situations, CongoInc necessarily plays the role of the provider (a role restriction).

agentive physical ob ject(CongoInc) ∀x,y.CongoProvider(x)∧played by(x,y) →y = CongoInc

LocateBook and BuyBook are elementary computational tasks.

LocateBook(x) →Computational Task(x) LocateBook(x) →elementary task(x) BuyBook(x) →Computational Task(x) BuyBook(x) →elementary task(x)

ExpandedCongoBuy is a complex service task, which has LocateBook and BuyBook as parts and is itself a temporary component of the offering. It is inferred that LocateBook and BuyBook are also temporary components.

ExpandedCongoBuy(x) →Service Task(x) ExpandedCongoBuy(x) →complex Task(x) ∀x,y.LocateBook(x)∧part o f(x,y) →ExpandedCongoBuy(y) ∀x,y.BuyBook(x)∧part o f(x,y) →ExpandedCongoBuy(y) ∀x,y.ExpandedCongoBuy(x)∧temporary component o f(x,y) → CongoBuyO f fering(y)

BookToLocate is a computational input to LocateBook. DescriptionOutput and Cata- logueBookOutput are conditional computational outputs of LocateBook.

BookToLocate(x) →Computational Input(x) ∀x,y.BookToLocate(x)∧modality target(x,y) →LocateBook(y) DescriptionOutput(x) →Conditional Output(x) DescriptionOutput(x) →Computational Output(x) CatalogueBookOutput(x) →Conditional Output(x) CatalogueBookOutput(x) →Computational Output(x) ∀x,y.DescriptionOutput(x)∧modality target(x,y) →LocateBook(y) ∀x,y.CatalogueBookOutput(x)∧modality target(x,y) →LocateBook(y)

BookToLocate is played by information objects in RDF that reference a book (Role playing can be similarly restricted for the outputs of BookToLocate).

BookDescription(x) →In formation Ob ject(x) language(RDF) ∀x,y.BookDescription(x)∧expressed according to(x,y) →y = RDF Book(x) →Physical Endurant(x) ∀x,y.BookDescription(x)∧refers to(x,y) →Book(y) ∀x,y.BookToLocate(x)∧played by(x,y) →BookDescription(y)

113

Next, we model an actual sale of a book. We show that this can be understood as a situation for the above description by mapping between elements of the setting and the service offering description. Note that this implies, for example, that CongoInc is necessarily participating in this sale as the provider.

Situation(CongoSale) CongoBuyO f fering(cbo) satis fies(CongoSale,cbo)

Joe is a CongoInc customer, who participates in the activity.

natural person(Joe) CongoCustomer(cc) plays(Joe,cc) participant in(Joe,BuyingWinnieThePooh)

BookObject is an information object (document), which refers to WinnieThePooh, a book that the customer would like to ﬁnd.

Book(WinnieThePooh) Literal(”WinnieThePooh”) name o f(WinnieThePooh,”WinnieThePooh”) part o f(WinnieThePooh,CongoSale) BookDescription(BookOb ject) refers to(BookOb ject,WinnieThePooh) BookToLocate(WinnieThePooh) plays(BookOb ject,WinnieThePooh) part(BookOb ject,CongoSale)

BuyingWinnieThePooh is the actual activity that is performed in this sale according to the task description. LocatingWinnieThePooh is a computational part of the activity that is carried out to locate the book. The BookObject is data for this activity.

Service Activity(BuyingWinnieThePooh) Computational Activity(LocatingWinnieThePooh) part o f(LocatingWinnieThePooh,BuyingWinnieThePooh) setting(BuyingWinnieThePooh,CongoSale) ExpandedCongoBuy(ecb) sequences(ecb,BuyingWinnieThePooh) data for(BookOb ject,LocatingWinnieThePooh)

We don’t capture that Joe provides the information object, i.e. the book to locate. We do capture that the information object references a book, and we could capture as a precondition that Joe wants book. We could also describe the effect: Joe has a book.

114

12.9 Alignment of the Application Server’s ontology

12.9.1 Original Ontology

The Application Server for the Semantic Web uses an ontology for software module and API discovery, manual classiﬁcation of software modules and for implementation tasks [68]. During its design we tried to stay as close as possible to DAML-S (cf. Section 12.8) for it is an accepted standard that has been investigated for a long time and has a sound basis [67]. Although DAML-S serves as a good starting point for our ontology, the main dif- ﬁculty was in the type of software entities to be described. While DAML-S describes web services, our goal is to describe software modules and their APIs. As a result some parts of DAML-S were not reusable. In the Appendix we present all the subontologies in DAML-S in comparison to ours before the alignment. What we will achieve in the next subsection is the alignment from the generic level, represented by DOLCE, D&S and the Core Ontology of Services, to the intermediate and domain level. The Implementation subontology is primarily used to facilitate component discovery for the client and of particular importance as it introduces several new concepts. Its ter- minology is shown below.

Software Module Speaking in terms of the object-oriented paradigm, a software module is an object revealing an Application Programming Interface (API). A software module fulﬁlls complex computational tasks. Examples: ontology store, inference engine.

Component Software module that is deployed to the Application Server for the Semantic Web 66.

System Component Component providing functionality for the Application Server for the Semantic Web itself, e.g. the registry.

Functional Component Component that is of interest to the client and can be discov- ered. Ontology-related software modules become functional components by mak- ing them deployable, e.g. RDF stores.

External Module An external module cannot be deployed directly as it may be pro- grammed in a different language, live on a different computing platform, etc. It equals a functional component from a client perspective. This is achieved by hav- ing a proxy component deployed that relays communication to the external module.

Proxy Component Special type of functional component that manages the communica- tion to an external module. Examples are proxy components for inference engines, like FaCT.

Interceptor Software that monitors requests and modiﬁes them. Examples: transaction or semantic interoperation interceptor.

66We use the word deployment as the process of registering, possibly initializing and starting a compo- nent to the Microkernel.

115

Surrogate Software embedded in the client application. It offers the same API as a particular component and relays communication to it. Meant for ease of use in the ASSW scenario, similar to stubs in CORBA.

12.9.2 Aligning the taxonomy

In a ﬁrst step, we strive to align the terminology in the subsection above. Figure 14 sketches an overview before we detail the concept’s axioms in the following paragraphs.

Endurant

COS

DOLCE

ASSW

D&S

Non-Physical Endurant

Physcal Endurant

Role

Information object Software as binary

Instrumentality Role

played_by

ASSW Component

Software Module

Interceptor Surrogate

deployed_ with

proxying_for

API

Functional Component System Component

offers

part_of

Method

Proxy Component Registry

. . .

relaying_communication_to

part_of

Formal Parameter

Figure 14: Alignment of the ASSW’s concepts

Software Module, Interceptor and Surrogate become subconcepts of Software-as- binary. A Software module offers an API which in turn is subconcept of Information Ob- ject. An API consists of Methods and a Method may have Formal Parameters. Software Modules are deployed with an Interceptor and Surrogates proxy for Software Modules on the client side.

So ftware Module(x) →So ftware as binary(x) Interceptor(x) →So ftware as binary(x) Surrogate(x) →So ftware as binary(x) API(x) →In formation ob ject(x) o f fers(x,y) →So ftware Module(x) o f fers(x,y) →API(y) deployed with(x,y) →So ftware Module(x) deployed with(x,y) →Interceptor(y)

116

proxying for(x,y) →Surrogate(x) proxying for(x,y) →So ftware Module(y)

While the conceptualization above is quite generic, Software Modules can become Components in the Application Server for the Semantic Web setting (formalizing the specializations of Component is straightforward). This behavior shows a clear contextual nature and, thus, we model an ASSW Component as a role played by a Software Module. The most prominent example for that is an Ontology Store Software Module which is a ﬁrst order entity but can be both the registry (i.e. a System Component) and a Functional Component within the Application Server.

ASSW Component(x) →Instrumentality Role(x) ∀x,y.ASSW Component(x)∧played by(x,y) →So ftware Module(y) Functional Component(x) →ASSW Component(x) Proxy Component(x) →Functional Component(x) System Component(x) →ASSW Component(x) Registry(x) →System Component(x) ...

Note that we do not list all specializations of System Component here (Registry, As- sociation Management, Component Loader, Cascading Component, etc.). Note also, that there is no need to model External Modules. It is enough to formalize Proxy Component as a role that relays communication to a Software Module.

relaying communication to(x,y) →Proxy Component(x) relaying communication to(x,y) →So ftware Module(y)

12.9.3 API Descriptions

After aligning the terminology we would like to capture the intuition that is common in both DAML-S and ASSW, namely that there are semantic descriptions of software (describing functionality or tasks) and syntactic descriptions of software (describing parts of software as an object). Hence we come up with a new kind of description in the D&S sense, called APIDescription (cf. Figure 15). In fact, we formalize a whole hierarchy of APIDescriptions as domain knowledge. E.g., in the Semantic Web domain, StoreAPIDescription along subconcepts like RDF- StoreAPIDescription or OntologyStoreAPIDescription. What is common to all API- Descriptions is that there has to be a role ASSW Component played by Software Module and the ASSW Component has exploitation within at least one Computational Task. The last relation is reﬁned for specializations of APIDescriptions, e.g. in an RDFStoreAPI- Description the role of a Functional Component has exploitation within a StoreTriple Computational Task etc.

StoreAPIDescription(x) →APIDescription(x) RDFStoreAPIDescription(x) →StoreAPIDescription(x) OntologyStoreAPIDescription(x) →StoreAPIDescription(x)

117

S-Description

DOLCE

D&S

Description System

Information Object

APIDescription

expressed- according- to

COS

Method ASSW

IDL

component_of

component_of component_of

component_of

played-by

Parameter Role

Course

Role

Task

Instrumentalitiy Role

APIDescriptionParameter

ASSW Component

Computational Task

Object

has exploitation within

ComponentID

queryLanguage

Operation

belongs_to

Query

Store

representationLanguage

belongs_to

...

Argument

StoreTriple StoreOntology

Figure 15: API Description

... ∀x.APIDescription(x) → ∃y,z,t.component o f(x,y)∧ASSW Component(y)∧played by(y,z)∧ So ftwareModule(z)∧has exploitation within(y,t)∧computational task(t) ... ∀x.RDFStoreAPIDescription(x) → ∃y,z,t.component o f(x,y)∧Functional Component(y)∧played by(y,z)∧ So ftwareModule(z)∧has exploitation within(y,t)∧StoreTriple(t) ...

Roles. The new roles introduced in the subsection above are relevant for the API De- scription. So-called ASSW Components and specializations are played by Software Mod- ules (cf. Figure 14). Every ASSW Component has exploitation within a Computational Task.

Courses. As depicted in Figure 15 we use Computational Task which is part of the Core Ontology of Services and subconcept of DOLCE’s Course. We deﬁne new, domain dependent, specializations thereof. In the example, we come up with Semantic Web re- lated Computational Task like StoreTriple or StoreOntology. They become components of the API Description and have exploitation within the ASSW Component role which are ultimately played by Software Modules.

Store(x) →computational task(x) StoreTriple(x) →Store(x)

118

StoreOntology(x) →Store(x) ... Query(x) →computational task(x)

The other way around, it is important to model which Method fulﬁlls the Compu- tational Tasks mentioned above. Therefore we have to deﬁne a new relation ’fulﬁlls’ between Information Object and Computational Task independent of the APIDescription.

ful fills(x,y) →In formation Ob ject(x) ful fills(x,y) →Computational Task(x)

Parameters. When a Software Module is deployed to the Application Server for the Se- mantic Web, it automatically gains several attributes, most prominently a ComponentID. Such properties do not belong to the software module but show a clear context depen- dency. Hence, we model them as new parameters that are component of the APIDescrip- tion (cf. Figure 15).

ComponentID(x) →APIDescriptionParameter(x) ∀x.ComponentID(x) →∃y.APIDescription(y)∧component o f(y,x) ...

In addition, specializations of the APIDescription may have several domain-dependent properties. E.g., an StoreAPIDescription may have a parameter representationLanguage or queryLanguage. [70] gives a nice overview of different Semantic Web software mod- ules and their characteristika. Such relations have to axiomatized accordingly, e.g.

queryLanguage(x) →APIDescriptionParameter(x) ∀x.queryLanguage(x) →∃y.StoreAPIDescription(y)∧component o f(y,x) ...

Figure 15 sketches the newly introduced parameter called APIDescriptionParameter which can be component of APIDescriptions only. Note that an APIDescription is not expected to have a certain number of parameters as component. They are optional alto- gether.

12.9.4 IDL Descriptions

For the syntactic descriptions of software we come up with a new kind of description called IDLDescription. For this purpose we formalized the terminology of IDL (Interface Description Language [45]), viz. Object, Operation, Argument etc., as instrumentality roles. The idea is that such roles are played by information objects, e.g. Object is played by Software Module and Operation is played by Method. The general idea is already featured in the Core Ontology of Services where Descrip- tion Systems are introduced as subconcept of D&S’s description. Information Objects, which are non physical Endurants, are expressed according to such a Description System. Examples would be RDF or the aforementioned IDL.

119

IDLDescription(x) →APIDescription(x) ∀x.IDLDescription(x) →∃y.component o f(x,y)∧Ob ject(y) ∀x.IDLDescription(x) →∃y.component o f(x,y)∧Operation(y) ∀x.IDLDescription(x) →∃y.component o f(x,y)∧Parameter(y) ... ∀x.Ob ject(x) →∃y.played by(x,y)∧So ftware Module(y) ∀x.Operation(x) →∃y.played by(x,y)∧Method(y) ∀x.Argument(x) →∃y.played by(x,y)∧Formal Parameter(y) ...

12.9.5 Example

Last but not least, the example in Figure 16 shows both an APIDescription and an IDLDe- scription of a KAON Ontology Store which is part of the KAON Tool suite [7]. For the sake of brevity, we limit ourselves to one Method ’AddStatement’ which is part of the KAONOntologyStore Software Module and fulﬁlls the task of storing a triple.

KAONOntologyStoreAPIDescription

Parameter Role Course (Task)

representationLanguage Functional Component Store Triple

fulfills

KAONOntologyStoreIDLDescription

Role Role Role

Object Operation Argument belongs_to

belongs_to

played-by valued-by

played-by

location-of Situation

AddStatement part_of

KAON KAONOntologyStore

Literal Software Module Method

Figure 16: KAON Ontology Store Example

In our context, the KAONOntologyStoreAPIDescription plays the role of a functional component deployed to the Application Server. The description features several parame- ters, such as representationLanguage and the ComponentID. Furthermore, the Functional Component has exploitation within the StoreTriple task. The KAONOntologyIDLDescription consists only of roles: Object is played by the KAONOntologyStore Software Module, Operation is played by the AddStatement Method, Argument played by a Formal Parameter and so on. Note that an APIDescription is expected to have several Tasks, like StoreTriple, Query, Retrieve and so on. The same holds for IDLDescription which should feature one Object

120

role related to a multitude of Operation roles.

121

Ontology Infrastructure for the Semantic Web

Appendix

Intermediate

Generic

Domain

DAML-S Profile´

. . .

Semantic Web Profiles

ServiceParameter

. . . StoreAndQuery APIDescription

... representationLanguage

name ...

Actor

queryLanguage

service- Parameter

Reification ... . . .

Datatypes

Profile hasAPIDescription APIDescription

contactInfo

OntologyStore Profile

QueryEngine Profile

Generic Ontology

Software Module

Input Output Precondition Effect

Query APIDescription

Store APIDescription

SoftwareModule- Profile

presents

Parameter

hasParameter

hasMethod

Method

mapsInput mapsOutput

API Description

presentedBy implementedBy

hasMethod StoreTriple StoreOntology

hasMethod

Thing hasType

supportedBy

SoftwareModule- Grounding

SoftwareModule

Retrieve . . . . . .

mapsMethod

...

mapsAPI

supports

Store

InputGrounding

SoftwareModule- Implementation

Semantic Web API Description

Software Module Implementation

mapsParameter hasInputGrounding

implements

hasInterfaceGrounding

InterfaceGrounding

hasMethodGrounding

MethodGrounding

IDLGrounding

hasOutputGrounding

OutputGrounding

IDL Grounding

mapsOperation

mapsInterface

mapsReturnType

Implementation

typeSpecification hasType

Type + void Type

hasOperation

Parameter

Operation

Interface

operationIdentifier

interfaceIdentifier

parameterIdentifier

returns

OperationType

String

hasInterface

IDL

requires

Functional- Component

. . .

Library

requiresLibrary

Component

System- Component

. . .

deployedWith

Code- Details

Interceptor

Proxy- Component

property

subconcept

concept

uses ontology

(sub)ontology

hasCodeDetails

. . .

[3] D. M. Armstrong. A World of States of Affairs. Cambridge University Press, Cam- bridge, 1997.

[4] Daniel Austin, Abbie Barbir, Christopher Ferris, and Sharad Garg. Web services architecture requirements. http://www.w3.org/TR/wsa-reqs, Nov 2002.

[5] L. R. Baker. Persons and Bodies: A Constitution view. Cambridge University Press, Cambridge, U.K., 2000. Belong to Guarino.

[6] David Booth, Michael Champion, Chris Ferris, Francis McCabe, Eric Newcomer, and David Orchard. Web Services Architecture, May 2003.

[7] E. Bozsak, M. Ehrig, S. Handschuh, A. Hotho, A. Maedche, B. Motik, D. Oberle, C. Schmitz, S. Staab, L. Stojanovic, N. Stojanovic, R. Studer, G. Stumme, Y. Sure, J. Tane, R. Volz, and V. Zacharias. KAON - towards a large scale Semantic Web. In Kurt Bauknecht, A. Min Tjoa, and Gerald Quirchmayr, editors, E-Commerce and Web Technologies, Third International Conference, EC-Web 2002, Aix-en-Provence, France, September 2-6, 2002, Proceedings, volume 2455 of Lecture Notes in Com- puter Science. Springer, 2002.

[8] F. Brentano. Philosophische Untersuchungen zu Raum, Zeit und Kontinuum, hrsg. von S. Krner und R. M. Chisholm. Meiner, Hamburg, 1976. (Eng. trans. by B. Smith, Philosophical Investigations on Space, Time and the Continuum, London, Croom Helm, 1988).

[9] K. Campbell. Abstract Particulars. Basil Blackwell, Oxford., 1990.

[10] R. Casati. Representational advantages. Proceedings of the Aristotelian Society, 2003:281–298, 2003.

[11] R. Casati and A. Varzi, editors. Events. Dartmouth, Aldershots, USA, 1996.

[12] R. Casati and A. Varzi. Parts and Places. The Structure of Spatial Representation. MIT Press, Cambridge, MA, 1999.

[13] R. Casati and A. C. Varzi. Holes and Other Superﬁcialities. MIT Press/Bradford Books, Cambridge (MA) and London (UK), 1994. Revised paperback edition, 1995.

[14] H. N. Castaneda. Objects, existence and reference. a prolegomenon to guise theory. Grazer Philosophische Studien, 25/26:31–66, 1985/1986.

[15] C. Castelfranchi. Information agents: The social nature of information and the role for trust. In Matthias Klusch and Franco Zambonelli, editors, Cooperative Informa- tion Agents V, 5th International Workshop, CIA 2001, volume 2182 of Lecture Notes in Computer Science, pages 208–210. Springer, Modena, Italy, 2001.

[16] R. M. Chisholm. Person and Object. A Metaphysical Study. La Salle, Open Court, 1976.

123

[17] R. M. Chisholm. A Realistic Theory of Categories: an Essay on Ontology. Cam- bridge University Press, Cambridge, 1996.

[18] Erik Christensen, Francisco Curbera, Greg Meredith, and Sanjiva Weerawarana. Web services description language (WSDL). http://www.w3.org/TR/wsdl, Mar 2003. W3C Note.

[19] The DAML Services Coalition. DAML Services, May 2003.

[20] D. Davidson. Inquiries into Truth and Interpretation. Oxford University Press, Oxford, 1984.

[21] D. Davidson. The method of truth in metaphysics. In Inquiries in Truth and Inter- pretation, pages 199–214. Oxford University Press, Oxford, 1984.

[22] D. Davidson. Radical interpretation. In Inquiries in Truth and Interpretation, pages 125–140. Oxford University Press, Oxford, 1984.

[23] D. Davidson. A coherence theory of truth and knowledge. In E. Lepore, editor, Truth and Interpretation. Oxford University Press, Oxford, 1986.

[24] D. Davidson. The structure and the content of thruth. The Journal of Philosophy, 87:279–328, 1990.

[25] W. Degen, B. Heller, H. Herrre, and B. Smith. GOL: A general ontological language. In C. Welty and B. Smith, editors, Second International Conference on Formal On- tology in Information systems (FOIS2001), Ogunquit, USA, 2001. ACM Press.

[26] A. Denkel. Object and property. Cambridge University Press, Cambridge., 1996.

[27] C. Fellbaum, editor. WordNet - An Electronic Lexical Database, volume Cambridge, Massachussetts. MIT Press, 1998.

[28] Christiane Fellbaum, editor. WordNet - An electronic lexical database. MIT Press, 1998.

[29] C. J. Fillmore. The case for case. In E. Bach and T. Harms, editors, Universals in Linguistic Theory. Rinehart and Wiston, New York, 1984.

[30] K. Fine. And not anti-realism either. Nous, 18:51–65, 1984.

[31] K. Fine. Ontological dependence. Proceedings of the Aristotelian Society, 95:269– 90, 1995.

[32] K. Fine. Part-whole. In B. Smith and D.W. Smith, editors, The Cambridge Com- panion to Husserl, pages 463–485. New York, Cambridge University Press, 1995.

[33] K. Fine and B. Smith. Husserl (Part One): The Pure Theory. Mimeograph, Manch- ester, 1983.

124

[34] A. Gangemi, N. Guarino, C. Masolo, and A. Oltramari. Understand- ing top-level ontological distinctions. In IJCAI-01 Workshop on Ontologies and Information Sharing, pages 26–33, Seattle, USA, 2001. AAAI Press. http://SunSITE.Informatik.RWTH-Aachen.DE/Publications/CEUR-WS/Vol-47/.

[35] A. Gangemi, N. Guarino, and A. Oltramari. Conceptual analysis of lexical tax- onomies: The case of WordNet top-level. In Christopher Welty and Smith Barry, editors, Formal Ontology in Information Systems. Proceedings of FOIS2001, pages 285–296. ACM Press, 2001.

[36] Aldo Gangemi and Peter Mika. Understanding the Semantic Web through Descrip- tions and Situations. Submitted to ODBASE 2003.

[37] Aldo Gangemi and Peter Mika. Understanding the semantic web through descrip- tions and situations. In DOA/CoopIS/ODBASE 2003 Confederated International Conferences DOA, CoopIS and ODBASE, Proceedings, LNCS. Springer, 2003.

[38] Aldo Gangemi, Domenico M. Pisanelli, and Geri Steve. An overview of the ONIONS project: Applying ontologies to the integration of medical terminologies. Data Knowledge Engineering, 31(2):183–220, 1999.

[39] P. G¨ardenfors. Conceptual Spaces: the Geometry of Thought. MIT Press, Cam- bridge, Massachussetts, 2000.

[40] N. Goodman. The Structure of Appearance. Harvard University Press, Cambridge MA., 1951.

[41] P. Grenon. Spatio-temporality in basic formal ontology: SNAP and SPAN, upper- level ontology, and framework of formalization (part I). Technical Report Series 05/2003, IFOMIS, 2003.

[42] P. Grenon. Spatio-temporality in BFO: Trans-ontology (part II). Technical report, IFOMIS, 2003.

[43] P. Grenon and B. Smith. Snap and span: Towards dynamic geospatial ontology. Spatial Cognition and Computation, 4(1), forthcoming.

[44] H. P. Grice. The logic of conversation. In P. Cole and J. L. Morgan, editors, Syntax and Semantics, volume 3, pages 41–58. Academic Press, New York, 1975.

[45] Object Modelling Group. Idl / language mapping speciﬁcation - java to idl, Aug 2002. 1.2.

[46] N. Guarino and C. Welty. A formal ontology of properties. In Rose Dieng and O. Corby, editors, Knowledge Engineering and Knowledge Management: Meth- ods, Models and Tools. 12th International Conference, EKAW2000, pages 97–112. Springer Verlag, France, 2000.

[47] N. Guarino and C. Welty. Evaluating ontological decisions with ontoclean. Com- munications of the ACM, 45(2):61–65, 2002.

125

[48] N. Guarino and C. Welty. Identity and subsumption. In Rebecca Green, Carol Bean, and Sung Myaeng, editors, The Semantics of Relationships: an Interdisciplinary Perspective. Kluwer (in press), 2002.

[49] K. Hawley. How Thing Persist. Clarendon Press, Oxford, UK, 2001.

[50] M. Heller. The Ontology of Physical Objects. Four Dimensional Hunks of Matter. Cambridge University Press, 1990.

[51] P. Horwich. Meaning. Oxford University Press, Oxford, 1998.

[52] G. E. Hughes and M. J. Cresswell. A New Introduction to Modal Logic. Routledge, London, 1996.

[53] R. Ingarden. Der Streit um die Existenz der Welt, volume 1-4. Max Niemeyer Verlag, Tubingen, 1964.

[54] I. Johansson. Ontological Investigations. An Inquiry into the Categories of Nature, Man and Society. Routledge, London, 1989.

[55] Wolfgang K¨ohler. Gestalt Psychology. Liveright, New York, 1947/1929.

[56] S. Leonard, H. and N. Goodman. The calculus of individuals and its uses. Journal of Symbolic Logic, 5:45–55, 1940.

[57] D. Lewis. New work for a theory of universals. Australasian Journal of Philosophy, 61(4), 1983. Reprinted in D.H. Mellor and A. Oliver (eds.), Properties, Oxford University Press 1997.

[58] D. Lewis. Parts of Classes. Basil Blackwell, Oxford, 1991.

[59] D.K. Lewis. On the Plurality of Worlds. Basil Blackwell, Oxford, 1986.

[60] E.J. Lowe. The possibility of metaphysics. Clarendon Press, Oxford, 1998.

[61] David Martin, Mark Burstein, Grit Denker, Jerry Hobbs, Lalana Kagal, Ora Las- sila, Drew McDermott, Sheila McIlraith, Massimo Paolucci, Bijan Parsia, Terry Payne, Marta Sabou, Evren Sirin, Monika Solanki, Naveen Srinivasan, and Ka- tia Sycara. DAML-S (and OWL-S) 0.9 draft release. http://www.daml.org/ services/daml-s/0.9/, Nov 2003.

[62] C. Masolo, A. Gangemi, N. Guarino, A. Oltramari, and L. Schneider. Wonderweb deliverable d17: The wonderweb library of foundational ontologies. Technical re- port, 2002.

[63] Claudio Masolo, Stefano Borgo, Aldo Gangemi, Nicola Guarino, Alessandro Oltra- mari, and Luc Schneider. The WonderWeb Library of Foundational Ontologies. WonderWeb Deliverable 17, 2002.

[64] Alexander Miller. The Stanford Encyclopedia of Philosophy, chapter Realism. Stan- ford University, winter edition edition, 2002.

126

[65] Michael S. Moore. Legal Reality: A Naturalist Approach to Legal Ontology. Law and Philosophy, 21(6):619–705, 2002.

[66] K. Mulligan and B. Smith. A relational theory of the act. Topoi, 5:115–130, 1986.

[67] D. Oberle, M. Sabou, D. Richards, and R. Volz. An ontology for semantic mid- dleware: extending DAML-S beyond web-services. In On the Move to Meaningful Internet Systems and Ubiquitous Computing, 2003 - DOA/CoopIS/ODBASE 2003 Confederated International Conferences DOA, CoopIS and ODBASE 2003 Catania, Sicily, Italy, November 3 - 7, 2003, Workshops, Lecture Notes in Computer Science. Springer, 2003. In press.

[68] D. Oberle, R. Volz, B. Motik, and S. Staab. An extensible open software environ- ment. International Handbooks on Information Systems, chapter III, pages 311–333. Springer, 2003.

[69] F. J. Pelletier. Non-singular references: Some preliminaries. In F. J. Pelletier, editor, Mass Terms: Some Philosophical Problems, pages 1–14. Reidel, Dordrecht, 1979.

[70] Asuncion Gomez Perez. A survey on ontology tools. OntoWeb Deliverable 1.3, May 2002. www.ontoweb.org.

[71] H. Putnam. Sense, nonsense, and the senses: An inquiry into the powers of the human mind. The Journal of Philosophy, 91:445–517, 1994.

[72] W. V. O. Quine. Word and Object. MIT Press, Cambridge-MA, 1960.

[73] B. Russell. On order in time. Proceedings of the Cambridge Philosophical Society, 32:216–228, 1936.

[74] J. Searle. Intentionality. Cambridge University Press, Cambridge, 1983.

[75] T. Sider. Four-Dimensionalism. An Ontology of Persistence and Time. Clarendon Press, Oxford, 2001.

[76] P. Simons. Parts: a Study in Ontology. Clarendon Press, Oxford, 1987.

[77] P. Simons. Particulars in particular clothing: Three trope theories of substance. Philosophy and Phenomenological Research, 54(3):553–575, 1994.

[78] P. Simons. Relational tropes. In G. Haeﬂinger and P. Simons, editors, Analytic Phenomenology: Essay in Honor of Guido Kung. Kluwer, Dordrecht, 1995.

[79] B. Smith. Formal ontology, commonsense and cognitive science. International Journal of Human Computer Studies, 43(5/6):626–640, 1995.

[80] B. Smith. On substances, accidents and universals: In defence of a constituent ontology. Philosophical Papers, 27:105–127, 1997.

[81] B. Smith. Basic concepts of formal ontology. In Nicola Guarino, editor, Formal Ontology in Information Systems, pages 19–28. IOS Press, Amsterdam, 1998.

127

[82] B. Smith and D. Murray. Logic, forma and matter. Proceedings of the Aristotelian Society, 81:47–63, 1981.

[83] B. Smith and A. Varzi. Fiat and bona ﬁde boundaries. Philosophy and Phenomeno- logical Research, 60(2):401–420, 2000.

[84] John F. Sowa. Knowledge Representation: Logical, Philosophical, and Computa- tional Foundations. PWS Publishing Co., Boston, 1999.

[85] P. F. Strawson. Individuals. An Essay in Descriptive Metaphysics. Routledge, Lon- don and New York, 1959.

[86] A. L. Thomasson. Fiction and Metaphysics. Cambridge University Press, Cam- bridge, 1999.

[87] J. J. Thomson. The statue and the clay. Nous, 32(2):149–173, 1998.

[88] Ludger van Elst and Andreas Abecker. Ontologies for information management: balancing formality, stability, and sharing scope. Expert Systems with Applications, 23(4):357–366, November 2002.

[89] A. Varzi. Foreword to the special issue on temporal parts. The Monist, 83(3), 2000.

[90] D. C. Williams. On the elements of being. Review of Metaphysics, 7:3–18/171–192, 1953.

128

13 APPENDIX A: KIF version of DOLCE

;;; DOLCE (V2.1) in KIF (text format) ;;; 31 December 03

;THIS IS A TRANSLATION IN KIF (ACCORDING TO THE KIF-DRAFT ;PROPOSED TO THE AMERICAN NATIONAL STANDARD NCITS.T2/98-004 ;http://logic.stanford.edu/kif/dpans.html) OF DOLCE V2.1

;For comments on this version, please contact: ;borgo@loa-cnr.it

;REVIEW INFO ;CHANGES - COMMENTS

;(D13) changed WORD into WORLD - Typo ;(NA3)-(NA9) have been dropped - These occur already ;somewhere else ;(NA10)-(NA12) are left as comments - These are guaranteed ;by def. (ND5) ;(NA13) has been dropped -It follows from (NA14) and (D2)

; Basic functions and relations ; new non-rigid universals introduced in specialized ; theories or in new versions of DOLCE need to be added in ; this definition as new disjunction clauses of ; form (= ?f ) ; (ND1): universals (defrelation UNIVERSAL (?f) := (or (X ?f)))

; new rigid universals introduced in new versions of DOLCE ; (or by the user) need to be added in this definition ; (ND2) rigid universals (defrelation X (?f) := (or (= ?f ALL) (= ?f AB) (= ?f R) (= ?f TR) (= ?f T) (= ?f PR) (= ?f S) (= ?f AR) (= ?f Q) (= ?f TQ) (= ?f TL) (= ?f PQ) (= ?f SL) (= ?f AQ) (= ?f ED) (= ?f M) (= ?f PED) (= ?f F) (= ?f POB) (= ?f APO) (= ?f NAPO) (= ?f NPED) (= ?f NPOB) (= ?f MOB) (= ?f SOB) (= ?f ASO) (= ?f SAG) (= ?f SC) (= ?f NASO) (= ?f AS) (= ?f PD) (= ?f EV) (= ?f ACH) (= ?f ACC) (= ?f STV) (= ?f ST) (= ?f PRO))))

; there are no particulars in this version of DOLCE, any ; particular has to be added in this definition, the def. ; will have form : (or (= ?x ) (= ?x )) ; (ND3) particulars (defrelation PARTICULAR(?x) := )

; there are no named worlds in this version of DOLCE, any ; world has to be added in this definition, the def. Will ; have form : (or (= ?w ) (= ?w )) ; (ND4) worlds (defrelation WORLD(?w) := )

; (ND5) accessibility relation on worlds (defrelation WLDR(?w ?v) := (and (WORLD ?w) (WORLD ?v)))

; (ND6) Parthood (defrelation P (?w ?x ?y) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y)))

129

; (ND7) Temporal Parthood (defrelation P (?w ?x ?y ?t) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)))

; (ND8) Constitution (defrelation K (?w ?x ?y ?t) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)))

; (ND9) Participation (defrelation PC (?w ?x ?y ?t) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)))

; (ND10) Quality (defrelation qt (?w ?x ?y) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y)))

; (ND11) Quale (defrelation ql (?w ?x ?y) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y)))

; (ND12) Quale (temporal) (defrelation ql (?w ?x ?y ?t) :=> (and (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)))

;*****************************************************

; (NA1) NEW AXIOM: total domain (forall (?x) (or (PARTICULAR ?x) (UNIVERSAL ?x) (WORLD ?x)))

; (NA2) partition of the domain (forall (?x) (and (<=> (PARTICULAR ?x) (and (not (UNIVERSAL ?x)) (not (WORLD ?x)))) (<=> (UNIVERSAL ?x) (and (not (PARTICULAR ?x)) (not (WORLD ?x)))) (<=> (WORLD ?x) (and (not (PARTICULAR ?x)) (not (UNIVERSAL ?x))))))

; Formal Characterization ;PRINCIPLES USED IN THE TRANSLATION IN KIF: ;Modal operators of possibility and necessity are translated in the standard ; way, see for instance p516 of Handbook of Logic in AI and Logic Prog. Vol.4; ;The indeces of relations are included prefixing a dot (we preserve the capital or ; lower case distinction) ;These are the only predicates (with their arity) that do not have possible worlds ; as arguments: ; X_1,PARTICULAR_1,UNIVERSAL_1, =_2

;No need for Barcan formulas, the domain of particulars turns out to be unique ; in the translation

;WLDR is an equivalence relation (from corrispondence theory, this implies ; that WLDR is a relation for S5). The axioms (NA10)-(NA12) are not necessary ; because of our definition of WLDR. ; (NA10) ;(forall (?w0) (=> (WORLD ?w0) (WLDR ?w0 ?w0))) ; (NA11) ;(forall (?w0 ?w1) ; (=> (and (WLDR ?w0 ?w1) (WORLD ?w0) (WORLD ?w1)) ; (WLDR ?w1 ?w0))) ; (NA12) ;(forall (?w0 ?w1 ?w2)

130

; (=> (and (WLDR ?w0 ?w1) ; (WLDR ?w1 ?w2) ; (WORLD ?w0) ; (WORLD ?w1) ; (WORLD ?w2)) ; (WLDR ?w0 ?w2)))

; ***THE UNIVERSALS ARE NECESSARILY NON-EMPY***-- axiom ; (NA14) -- axiom (forall (?w ?f) (=> (and (UNIVERSAL ?f) (WORLD ?w)) (NEP ?w ?f)))

; (NA15) -- axiom (forall (?w ?f) (=> (and (UNIVERSAL ?f) (WORLD ?w)) (or (not (X ?f)) (RG ?w ?f))))

; (NA16) Instances of PT -- axiom (forall (?w0) (=> (WORLD ?w0) (and (PT ?w0 ALL ED PD Q AB) (PT ?w0 ED PED NPED AS) (PT ?w0 PED M F POB) (PT ?w0 POB APO NAPO) (PT ?w0 NPOB MOB SOB) (PT ?w0 SOB ASO NASO) (PT ?w0 ASO SAG SC) (PT ?w0 PD EV STV) (PT ?w0 EV ACH ACC) (PT ?w0 STV ST PRO) (PT ?w0 Q TQ PQ AQ) (PT ?w0 R TR PR AR))))

; (NA17) Instances of SB -- axiom (forall (?w0) (=> (WORLD ?w0) (and (SB ?w0 ALL ED) (SB ?w0 ALL PD) (SB ?w0 ALL Q) (SB ?w0 ALL AB) (SB ?w0 ED PED) (SB ?w0 ED NPED) (SB ?w0 ED AS) (SB ?w0 PED M) (SB ?w0 PED F) (SB ?w0 PED POB) (SB ?w0 POB APO) (SB ?w0 POB NAPO) (SB ?w0 NPED NPOB) (SB ?w0 NPOB MOB) (SB ?w0 NPOB SOB) (SB ?w0 SOB ASO) (SB ?w0 SOB NASO) (SB ?w0 ASO SAG) (SB ?w0 ASO SC) (SB ?w0 PD EV) (SB ?w0 PD STV) (SB ?w0 EV ACH) (SB ?w0 EV ACC) (SB ?w0 STV ST) (SB ?w0 STV PRO) (SB ?w0 Q TQ) (SB ?w0 Q PQ) (SB ?w0 Q AQ) (SB ?w0 TQ TL) (SB ?w0 PQ SL) (SB ?w0 AB FACT) (SB ?w0 AB SET) (SB ?w0 AB R) (SB ?w0 R TR) (SB ?w0 R PR) (SB ?w0 R AR) (SB ?w0 TR T) (SB ?w0 PR S))))

; (NA18) Existence of sum (forall (?w0 ?x ?y) (=> (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0)) (exists (?z) (and (PARTICULAR ?z) (+ ?w0 ?x ?y ?z)))))

; (NA19) Existence of sigma (forall (?w0 ?f) (=> (and (UNIVERSAL ?f) (WORLD ?w0)) (exists (?z) (and (PARTICULAR ?z) (sigma ?w0 ?f ?z)))))

; (NA20) Existence of sum.t

131

(forall (?w0 ?x ?y) (=> (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0)) (exists (?z) (and (PARTICULAR ?z) (+.t ?w0 ?x ?y ?z)))))

; (NA21) Existence of sigma.t (forall (?w0 ?f) (=> (and (UNIVERSAL ?f) (WORLD ?w0)) (exists (?z) (and (PARTICULAR ?z) (sigma.t ?w0 ?f ?z)))))

; this could be added in the def. of UNIVERSAL ;(forall (@f) ; (<=> (UNIVERSAL @f) ; (exists (?g @h) (and (UNIVERSAL ?g) ; (or (UNIVERSAL @h) (= @h (listof))) ; (= @f (listof ?g @h))))))

; this could be added in the def. of PARTICULAR ;(forall (@x) ; (<=> (PARTICULAR @x) ; (exists (?y @z) (and (PARTICULAR ?y) ; (or (PARTICULAR @z) (= @z (listof))) ; (= @x (listof ?y @z))))))

;******************************************************** ;(D1) RG: Rigid Universal (defrelation RG (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x)) (=> (?f ?w ?x) (forall (?u) (=> (and (WLDR ?w ?u) (WORLD ?u)) (?f ?u ?x))))))))

;(D2) NEP: Non-Empty Universal (defrelation NEP (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (exists (?y) (and (PARTICULAR ?y) (?f ?w ?y)))))))

;(D3) DJ: Disjoint Universals (defrelation DJ (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x)) (not (and (?f ?w ?x) (?g ?w ?x)))))))

;(D4) SB: Subsumption (defrelation SB (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x)) (or (not (?g ?w ?x)) (?f ?w ?x))))))

132

;(D5) EQ: Equal Universals (defrelation EQ (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SB ?w0 ?f ?g) (SB ?w0 ?g ?f)))

;(D6) PSB: Properly Subsuming (defrelation PSB (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SB ?w0 ?f ?g) (not (SB ?w0 ?f ?g))))

;(D7) L: Leaf Universal (defrelation L (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (forall (?w ?g) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (UNIVERSAL ?g)) (or (not (?SB ?w0 ?f ?g)) (EQ ?w0 ?f ?g))))))

;(D8) SBL: Leaf Subsumed by (defrelation SBL (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SB ?w0 ?f ?g) (L ?w0 ?g)))

;(D9) PSBL: Leaf Properly Subsumed by (defrelation PSBL (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (PSB ?w0 ?f ?g) (L ?w0 ?g)))

;(D10) L__: Leaf in the set X (defrelation L.X (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (X ?f) (forall (?w ?g) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (UNIVERSAL ?g)) (=> (and (?SB ?w ?f ?g) (X ?g)) (EQ ?w ?f ?g))))))

;(D11) SBL__ (defrelation SBL.X (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SB ?w0 ?f ?g) (L.X ?w0 ?g)))

;(D12) PSBL__ (defrelation PSBL.X (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (PSB ?w0 ?f ?g) (L.X ?w0 ?g)))

; Definition (D13) is left for expressivity. In practice it becomes superfluous ; since the user needs to give a list of the n-tuple satisfying relation PT in ; axiom (NA17) ;(D13) PT: Partition (defrelation PT (?w0 ?f @g) := (and (UNIVERSAL ?f) (UNIVERSAL @g) (WORLD ?w0) (not (item ?f @g)) (forall (?h ?k) (and (=> (and (UNIVERSAL ?h) (UNIVERSAL ?k) (item ?h @g) (item ?k @g) (/= ?h ?k)) (DJ ?w0 ?h ?k)) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x)) (<=> (?f ?w ?x) (exists (?h)

133

(and (UNIVERSAL ?h) (item ?h @g) (?h ?w ?x))))))))))

; Mereological Definitions ;(D14) PP: Proper Part (defrelation PP (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (P ?w0 ?x ?y) (not (P ?w0 ?y ?x))))

;(D15) O: Overlap (defrelation O (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?z) (and (PARTICULAR ?z) (P ?w0 ?z ?x) (P ?w0 ?z ?y)))))

;(D16) At: Atom (defrelation At (?w0 ?x) := (and (PARTICULAR ?x) (WORLD ?w0) (not (exists (?y) (and (PARTICULAR ?y) (PP ?w0 ?y ?x))))))

;(D17) AtP: Atomic Part (defrelation AtP (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (P ?w0 ?x ?y) (At ?w0 ?x)))

;(D18) __ Binary Sum (defrelation + (?w0 ?x ?y ?z) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (WORLD ?w0) (forall (?u) (=> (PARTICULAR ?u) (<=> (O ?w0 ?u ?z) (or (O ?w0 ?u ?x) (O ?w0 ?u ?y))))) (forall (?z1) (=> (and (PARTICULAR ?z1) (forall (?u) (=> (PARTICULAR ?u) (<=> (O ?w0 ?u ?z1) (or (O ?w0 ?u ?x) (O ?w0 ?u ?y)))))) (= ?z1 ?z)))))

;(D19) (general) Sum ; Note: the rendition in KIF is weaker than the corresponding definition in ;modal FOL; here ?f has to be one of the universal introduced explicitly. ;[A possible way out: use string-variables (@f) to code Boolean ;combinations of universals.] (defrelation sigma (?w0 ?f ?z) := (and (PARTICULAR ?z) (UNIVERSAL ?f) (WORLD ?w0) (forall (?y) (=> (PARTICULAR ?y) (<=> (O ?w0 ?y ?z) (exists (?v)

134

(and (PARTICULAR ?v) (?f ?w0 ?v) (O ?w0 ?y ?v)))))) (forall (?z1) (=> (PARTICULAR ?z1) (exists (?y) (and (PARTICULAR ?y) (=> (<=> (O ?w0 ?y ?z1) (exists (?v) (and (PARTICULAR ?v) (?f ?w0 ?v) (O ?w0 ?y ?v))))) (= ?z1 ?z)))))))

;(D20) PP: Temporary Proper Part (defrelation PP (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (P ?w0 ?x ?y ?t) (not (P ?w0 ?y ?x ?t))))

;(D21) O: Temporary Overlap (defrelation O (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (exists (?z) (and (PARTICULAR ?z) (P ?w0 ?z ?x ?t) (P ?w0 ?z ?y ?t)))))

;(D22) At: Temporary Atom (defrelation At (?w0 ?x ?t) := (and (PARTICULAR ?x) (PARTICULAR ?t) (WORLD ?w0) (not (exists (?y) (and (PARTICULAR ?y) (PP ?w0 ?y ?x ?t))))))

;(D23) AtP: Temporary Atomic Part (defrelation AtP (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (P ?w0 ?x ?y ?t) (At ?w0 ?x ?t)))

;(D24) Coincidence (defrelation =.t (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (P ?w0 ?x ?y ?t) (P ?w0 ?y ?x ?t)))

;(D25) CP: Constant Part (defrelation CP (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t) (and (PARTICULAR ?t) (PRE ?w0 ?y ?t))) (forall (?t) (=> (and (PARTICULAR ?t) (PRE ?w0 ?y ?t))

135

(P ?w0 ?x ?y ?t)))))

;(D26) (defrelation +.t (?w0 ?x ?y ?z) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (WORLD ?w0) (forall (?u ?t) (=> (and (PARTICULAR ?u) (PARTICULAR ?t)) (<=> (O ?w0 ?u ?z ?t) (or (O ?w0 ?u ?x ?t) (O ?w0 ?u ?y ?t))))) (forall (?z1 ?t) (=> (and (PARTICULAR ?z1) (PARTICULAR ?t) (forall (?u) (=> (PARTICULAR ?u) (<=> (O ?w0 ?u ?z1 ?t) (or (O ?w0 ?u ?x ?t) (O ?w0 ?u ?y ?t)))))) (= ?z1 ?z)))))

;(D27) ; NOTE: this rendition includes only the listed universal, for instance, ; no Boolean combination of universals is included [see also comment on (D19)] (defrelation sigma.t (?w0 ?f ?z) := (and (PARTICULAR ?z) (UNIVERSAL ?f) (WORLD ?w0) (forall (?y ?t) (=> (and (PARTICULAR ?y) (PARTICULAR ?t)) (<=> (O ?w0 ?y ?z ?t) (exists (?v) (and (PARTICULAR ?v) (?f ?w0 ?v) (O ?w0 ?y ?v ?t)))))) (forall (?z1 ?t) (=> (and (PARTICULAR ?z1) (PARTICULAR ?t)) (exists (?y) (and (PARTICULAR ?y) (=> (<=> (O ?w0 ?y ?z1 ?t) (exists (?v) (and (PARTICULAR ?v) (?f ?w0 ?v) (O ?w0 ?y ?v ?t)))) (= ?z1 ?z))))))))

; Quality ;(D28) dqt: Direct Quality (defrelation dqt (?w0 ?x ?y) := (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (qt ?w0 ?x ?y) (not (exists (?z) (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (qt ?w0 ?z ?y))))))

;(D29) qt: Quality of type (defrelation qtf (?w0 ?f ?x ?y) := (and (UNIVERSAL ?f) (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (qt ?w0 ?x ?y) (?f ?w0 ?x) (SBL.X ?w0 Q ?f)))

136

; Temporal and Spatial Quale ;(D30) ql_T,PD (defrelation ql.T.PD (?w0 ?t ?x) := (and (PARTICULAR ?t) (PARTICULAR ?x) (WORLD ?w0) (PD ?w0 ?x) (exists (?z) (and (PARTICULAR ?z) (qtf ?w0 TL ?z ?x) (ql ?w0 ?t ?z)))))

;(D31) ql_T,ED (defrelation ql.T.ED (?w0 ?t ?x) := (and (PARTICULAR ?t) (PARTICULAR ?x) (WORLD ?w0) (ED ?w0 ?x) (forall (?u) (=> (PARTICULAR ?u) (<=> (O ?w0 ?u ?t) (exists (?v ?y) (and (PARTICULAR ?v) (PARTICULAR ?y) (PC ?w0 ?x ?y ?v) (O ?w0 ?u ?v)))))) (forall (?t1) (=> (PARTICULAR ?t1) (exists (?u) (and (PARTICULAR ?u) (=> (<=> (O ?w0 ?u ?t1) (exists (?v ?y) (and (PARTICULAR ?v) (PARTICULAR ?y) (PC ?w0 ?x ?y ?v) (O ?w0 ?u ?v)))) (= ?t1 ?t))))))))

;(D32) ql_T,TQ (defrelation ql.T.TQ (?w0 ?t ?x) := (and (PARTICULAR ?t) (PARTICULAR ?x) (WORLD ?w0) (TQ ?w0 ?x) (exists (?z) (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (ql.T.PD ?w0 ?t ?z)))))

;(D33) ql_T,PQ_or_AQ (defrelation ql.T.PQAQ (?w0 ?t ?x) := (and (PARTICULAR ?t) (PARTICULAR ?x) (WORLD ?w0) (or (PQ ?w0 ?x) (AQ ?w0 ?x)) (exists (?z) (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (ql.T.ED ?w0 ?t ?z)))))

;(D34) ql_T,Q (defrelation ql.T.Q (?w0 ?t ?x) := (and (PARTICULAR ?t) (PARTICULAR ?x) (WORLD ?w0) (or (ql.T.TQ ?w0 ?t ?x) (ql.T.PQAQ ?w0 ?t ?x))))

;(D35) ql_T: Temporal Quale (defrelation ql.T (?w0 ?t ?x) := (and (PARTICULAR ?t)

137

(PARTICULAR ?x) (WORLD ?w0) (or (ql.T.ED ?w0 ?t ?x) (ql.T.PD ?w0 ?t ?x) (ql.T.Q ?w0 ?t ?x))))

;(D36) ql_S,PED (defrelation ql.S.PED (?w0 ?s ?x ?t) := (and (PARTICULAR ?s) (PARTICULAR ?x) (PARTICULAR ?t) (WORLD ?w0) (PED ?w0 ?x) (exists (?z) (and (PARTICULAR ?z) (qtf ?w0 SL ?z ?x) (ql ?w0 ?s ?z ?t)))))

;(D37) ql_S,PQ (defrelation ql.S.PQ (?s ?x ?t) := (and (PARTICULAR ?s) (PARTICULAR ?x) (PARTICULAR ?t) (WORLD ?w0) (PQ ?w0 ?x) (exists (?z) (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (ql.S.PED ?w0 ?s ?z ?t)))))

;(D38) ql_S,PD (defrelation ql.S.PD (?w0 ?s ?x ?t) := (and (PARTICULAR ?s) (PARTICULAR ?x) (PARTICULAR ?t) (WORLD ?w0) (PD ?w0 ?x) (exists (?z) (and (PARTICULAR ?z) (mppc ?w0 ?z ?x) (ql.S.PED ?w0 ?s ?z ?t)))))

;(D39) ql_S: Spatial Quale (defrelation ql.S (?w0 ?s ?x ?t) := (and (PARTICULAR ?s) (PARTICULAR ?x) (PARTICULAR ?t) (WORLD ?w0) (or (ql.S.PED ?w0 ?s ?x ?t) (ql.S.PQ ?w0 ?s ?x ?t) (ql.S.PD ?w0 ?s ?x ?t))))

;Being present ;(D40) PRE: Being Present at (defrelation PRE (?w0 ?x ?t) := (and (PARTICULAR ?x) (PARTICULAR ?t) (WORLD ?w0) (exists (?u) (and (PARTICULAR ?u) (ql.T ?w0 ?u ?x) (P ?w0 ?t ?u)))))

;(D41) PRE: Being Present in at (defrelation PRE (?w0 ?x ?s ?t) := (and (PARTICULAR ?x) (PARTICULAR ?s) (PARTICULAR ?t) (WORLD ?w0) (PRE ?w0 ?x ?t) (exists (?u) (and (PARTICULAR ?u) (ql.S ?w0 ?u ?x ?t)

138

(P ?w0 ?s ?u)))))

; Inclusion and Coincidence ;(D42) Temporal Inclusion (defrelation incl.T (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t ?u) (and (PARTICULAR ?t) (PARTICULAR ?u) (ql.T ?w0 ?t ?x) (ql.T ?w0 ?u ?y) (P ?w0 ?t ?u)))))

;(D43) Proper Temporal Inclusion (defrelation sincl.T (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t ?u) (and (PARTICULAR ?t) (PARTICULAR ?u) (ql.T ?w0 ?t ?x) (ql.T ?w0 ?u ?y) (PP ?w0 ?t ?u)))))

;(D44) Temporary Spatial Inclusion (defrelation incl.S.t (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (exists (?s ?r) (and (PARTICULAR ?s) (PARTICULAR ?r) (ql.S ?w0 ?s ?x ?t) (ql.S ?w0 ?r ?y ?t) (P ?w0 ?s ?r)))))

;(D45) Temp. Proper Sp. Inclusion (defrelation sincl.S.t (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (exists (?s ?r) (and (PARTICULAR ?s) (PARTICULAR ?r) (ql.S ?w0 ?s ?x ?t) (ql.S ?w0 ?r ?y ?t) (PP ?w0 ?s ?r)))))

;(D46) Spatio-temporal Inclusion (defrelation incl.S.T (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t) (and (PARTICULAR ?t) (PRE ?w0 ?x ?t))) (forall (?t) (=> (and (PARTICULAR ?t) (PRE ?w0 ?x ?t)) (incl.S.t ?w0 ?x ?y ?t)))))

;(D47) Spatio-temp. Incl. during (defrelation incl.S.T.t (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (PRE ?w0 ?x ?t) (forall (?u) (=> (and (PARTICULAR ?u) (AtP ?w0 ?u ?t)) (incl.S.t ?w0 ?x ?y ?u)))))

139

;(D48) Temporal Coincidence (defrelation ˜.T (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (incl.T ?w0 ?x ?y) (incl.T ?w0 ?y ?x)))

;(D49) Temporary Spatial Coincidence (defrelation ˜.S.t (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (incl.S.t ?w0 ?x ?y ?t) (incl.S.t ?w0 ?y ?x ?t)))

;(D50) Spatio-temporal Coincidence (defrelation ˜.S.T (?w0 ?x ?y) := (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (incl.S.T ?w0 ?x ?y) (incl.S.T ?w0 ?y ?x)))

;(D51) Spatio-temp. Coincidence during (defrelation ˜.S.T.t (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (PRE ?w0 ?x ?t) (forall (?u) (=> (and (PARTICULAR ?u) (AtP ?w0 ?u ?t)) (˜.S.t ?w0 ?x ?y ?u)))))

;(D52) O_T: Temporal Overlap (defrelation O.T (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t ?u) (and (PARTICULAR ?t) (PARTICULAR ?u) (ql.T ?w0 ?t ?x) (ql.T ?w0 ?u ?y) (O ?w0 ?t ?u)))))

;(D53) O_S,t: Temporary Spatial Overlap (defrelation O.S.t (?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (exists (?s ?r) (and (PARTICULAR ?s) (PARTICULAR ?r) (ql.S ?w0 ?s ?x ?t) (ql.S ?w0 ?r ?y ?t) (O ?w0 ?s ?r)))))

; Perdurant ;(D54) P_T: Temporal Part (defrelation P.T (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (PD ?w0 ?x) (P ?w0 ?x ?y) (forall (?z) (=> (and (PARTICULAR ?z) (P ?w0 ?z ?y)

140

(incl.T ?w0 ?z ?x)) (P ?w0 ?z ?x)))))

;(D55) P_S: Spatial Part (defrelation P.S (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (PD ?w0 ?x) (P ?w0 ?x ?y) (˜.T ?w0 ?x ?y)))

;(D56) NEP_S: Strongly Non-Empty (defrelation NEP.S (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (exists (?x ?y) (and (PARTICULAR ?x) (PARTICULAR ?y) (?f ?w ?x) (?f ?w ?y) (not (P ?w ?x ?y)) (not (P ?w ?y ?x))))))))

;(D57) CM: Cumulative (defrelation CM (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w ?x ?y ?z) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (+ ?w ?x ?y ?z) (?f ?w ?x) (?f ?w ?y)) (?f ?w ?z)))))

;(D58) CM: Anti-Cumulative (defrelation CM˜ (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w ?x ?y ?z) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (+ ?w ?x ?y ?z) (?f ?w ?x) (?f ?w ?y) (not (P ?w ?x ?y)) (not (P ?w ?y ?x))) (not (?f ?w ?z))))))

;(D59) HOM: Homeomerous (defrelation HOM (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w ?x ?y) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x)

141

(PARTICULAR ?y) (?f ?w ?x) (P.T ?w ?y ?x)) (?f ?w ?y)))))

;(D60) HOM: Anti-Homeom. (defrelation HOM˜ (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (?f ?w ?x)) (exists (?y) (and (PARTICULAR ?y) (P.T ?w ?y ?x) (not (?f ?w ?y))))))))

;(D61) AT: Atomic (defrelation AT (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (?f ?w ?x)) (At ?w ?x)))))

;(D62) AT: Anti-Atomic (defrelation AT˜ (?w0 ?f) := (and (UNIVERSAL ?f) (WORLD ?w0) (SB ?w0 PD ?f) (forall (?w ?x) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (?f ?w ?x)) (not (At ?w ?x))))))

;Participation ;(D63) PC_C: Constant Participation (defrelation PC.C (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t) (and (PARTICULAR ?t) (PRE ?w0 ?y ?t))) (forall (?t) (=> (and (PARTICULAR ?t) (PRE ?w0 ?y ?t)) (PC ?w0 ?x ?y ?t)))))

;(D64) PC_T: Temporary Total Particip. (defrelation PC.T (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (PD ?w0 ?y) (forall (?z) (=> (and (PARTICULAR ?z) (P ?w0 ?z ?y) (PRE ?w0 ?z ?t)) (PC ?w0 ?x ?z ?t)))))

;(D65) PC_T: Total Participation (defrelation PC.T (?w0 ?x ?y) :=

142

(and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (exists (?t) (and (PARTICULAR ?t) (ql.T ?w0 ?t ?y) (PC.T ?w0 ?x ?y ?t)))))

;(D66) mpc: Maximal Participant (defrelation mpc (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (forall (?z ?t) (=> (and (PARTICULAR ?z) (PARTICULAR ?t)) (<=> (O ?w0 ?z ?x ?t) (exists (?v) (and (PARTICULAR ?v) (PC.T ?w0 ?v ?y ?t) (O ?w0 ?z ?v ?t)))))) (forall (?z ?x1 ?t) (=> (and (PARTICULAR ?z) (PARTICULAR ?x1) (PARTICULAR ?t) (<=> (O ?w0 ?z ?x1 ?t) (exists (?v) (and (PARTICULAR ?v) (PC.T ?w0 ?v ?y ?t) (O ?w0 ?z ?v ?t))))) (= ?x1 ?x)))))

;(D67) mppc: Maximal Physical Participant (defrelation mppc (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (forall (?z ?t) (=> (and (PARTICULAR ?z) (PARTICULAR ?t)) (<=> (O ?w0 ?z ?x ?t) (exists (?v) (and (PARTICULAR ?v) (PC.T ?w0 ?v ?y ?t) (PED ?w0 ?z) (O ?w0 ?z ?v ?t)))))) (forall (?z ?x1 ?t) (=> (and (PARTICULAR ?z) (PARTICULAR ?x1) (PARTICULAR ?t) (<=> (O ?w0 ?z ?x1 ?t) (exists (?v) (and (PARTICULAR ?v) (PC.T ?w0 ?v ?y ?t) (PED ?w0 ?z) (O ?w0 ?z ?v ?t))))) (= ?x1 ?x)))))

;(D68) lf: Life (defrelation lf (?w0 ?x ?y) := (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (forall (?z) (=> (PARTICULAR ?z) (<=> (O ?w0 ?z ?x) (exists (?v) (and (PARTICULAR ?v) (PC.T ?w0 ?y ?v) (O ?w0 ?z ?v)))))) (forall (?z ?u)

143

(=> (and (PARTICULAR ?z) (PARTICULAR ?u) (<=> (O ?w0 ?z ?u) (exists (?v) (and (PARTICULAR ?v) (PC.T ?w0 ?y ?v) (O ?w0 ?z ?v))))) (= ?u ?x)))))

; Dependence ;(D69) SD: Specific Constant Dep. (defrelation SD (?w0 ?x ?y) := (or (and (PARTICULAR ?x) (PARTICULAR ?y) (WORLD ?w0) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (and (exists (?t) (and (PARTICULAR ?t) (PRE ?w ?x ?t))) (forall (?t) (=> (and (PARTICULAR ?t) (PRE ?w ?x ?t)) (PRE ?w ?y ?t))))))) (and (UNIVERSAL ?x) (UNIVERSAL ?y) (WORLD ?w0) (DJ ?w0 ?x ?y) (forall (?w ?x1) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x1) (?x ?w ?x1)) (exists (?y1) (and (PARTICULAR ?y1) (?y ?w ?y1) (SD ?w ?x1 ?y1))))))))

;(D70) SD: Specific Const. Dep. ;included in def (D69)

;(D71) GD: Generic Const. Dep. (defrelation GD (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (DJ ?w0 ?f ?g) (forall (?w ?x ?t) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?t) (?f ?w ?x)) (and (exists (?t1) (and (PARTICULAR ?t1) (PRE ?w ?x ?t1))) (=> (and (At ?w ?t) (PRE ?w ?x ?t)) (exists (?y) (and (PARTICULAR ?y) (?g ?w ?y) (PRE ?w ?y ?t)))))))))

;(D72) D: Constant Dependence (defrelation D (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (or (SD ?w0 ?f ?g) (GD ?w0 ?f ?g))))

;(D73) OD: One-sided Constant Dependence (defrelation OD (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g)

144

(WORLD ?w0) (D ?w0 ?f ?g) (not (D ?w0 ?g ?f))))

;(D74) OSD: One-sided Specific Constant Dependence (defrelation OSD (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SD ?w0 ?f ?g) (not (D ?w0 ?g ?f))))

;(D75) OGD: One-sided Generic Constant Dependence (defrelation OGD (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (GD ?w0 ?f ?g) (not (D ?w0 ?g ?f))))

;(D76) MSD: Mutual Specific Constant Dependence (defrelation MSD (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SD ?w0 ?f ?g) (SD ?w0 ?g ?f)))

;(D77) MGD: Mutual Generic Constant Dependence (defrelation MGD (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (GD ?w0 ?f ?g) (GD ?w0 ?g ?f)))

; Spatial Dependence ;(D78) SD_S: Specific Spatial Dependence (defrelation SD.S (?w0 ?x ?y) := (or (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (and (exists (?t ?s) (and (PARTICULAR ?t) (PARTICULAR ?s) (PRE ?w ?x ?s ?t))) (forall (?t ?s) (=> (and (PARTICULAR ?t) (PARTICULAR ?s) (PRE ?w ?x ?s ?t)) (PRE ?w ?y ?s ?t))))))) (and (WORLD ?w0) (UNIVERSAL ?x) (UNIVERSAL ?y) (DJ ?w0 ?x ?y) (forall (?w ?x1) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x1) (?x ?w ?x)) (exists (?y1) (and (PARTICULAR ?y1) (?y ?w ?y1) (SD.S ?w ?x1 ?y1))))))))

;(D79) PSD_S: Partial Specific Spatial Dependence

145

(defrelation PSD.S (?w0 ?x ?y) := (or (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (and (exists (?t ?s) (and (PARTICULAR ?t) (PARTICULAR ?s) (PRE ?w ?x ?s ?t))) (forall (?t ?s) (=> (and (PARTICULAR ?t) (PARTICULAR ?s) (PRE ?w ?x ?s ?t)) (exists (?r) (and (PARTICULAR ?r) (PP ?w ?r ?s) (PRE ?w ?y ?r ?t))))))))) (and (WORLD ?w0) (UNIVERSAL ?x) (UNIVERSAL ?y) (DJ ?w0 ?x ?y) (forall (?w ?x1) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x1) (?x ?w ?x1)) (exists (?y1) (and (PARTICULAR ?y1) (?y ?w ?y1) (PSD.S ?w ?x1 ?y1))))))))

;(D80) P-1SD_S: Inverse Partial Specific Spatial Dependence (defrelation P1SD.S (?w0 ?x ?y) := (or (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (and (exists (?t ?s) (and (PARTICULAR ?t) (PARTICULAR ?s) (PRE ?w ?x ?s ?t))) (forall (?t ?s) (=> (and (PARTICULAR ?t) (PARTICULAR ?s) (PRE ?w ?x ?s ?t)) (exists (?r) (and (PARTICULAR ?r) (PP ?w ?s ?r) (PRE ?w ?y ?r ?t))))))))) (and (WORLD ?w0) (UNIVERSAL ?x) (UNIVERSAL ?y) (DJ ?w0 ?x ?y) (forall (?w ?x1) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x1) (?x ?w ?x1)) (exists (?y1) (and (PARTICULAR ?y1) (?y ?w ?y1) (P1SD.S ?w ?x1 ?y1))))))))

;(D81) SD_S ;included in def (D78)

146

;(D82) PSD_S ;included in def (D79)

;(D83) P-1SD_S ;included in def (D80)

;(D84) GD_S: Generic Spatial Dependence (defrelation GD.S (?w0 ?f ?g) := (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (DJ ?w0 ?f ?g) (forall (?w ?x ?s ?t) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?t) (PARTICULAR ?s) (?f ?w ?x)) (and (exists (?t1 ?s1) (and (PARTICULAR ?t1) (PARTICULAR ?s1) (PRE ?w ?x ?s1 ?t1))) (=> (and (At ?w ?t) (PRE ?w ?x ?s ?t)) (exists (?y) (and (PARTICULAR ?y) (?g ?w ?y) (PRE ?w ?y ?s ?t)))))))))

;(D85) PGD_S: Partial Generic Spatial Dependence (defrelation PGD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (DJ ?w0 ?f ?g) (forall (?w ?x ?s ?t) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (PARTICULAR ?x) (PARTICULAR ?s) (PARTICULAR ?t) (?f ?w ?x)) (and (exists (?s1 ?t1) (and (PRE ?w ?x ?s1 ?t1) (PARTICULAR ?s1) (PARTICULAR ?t1)) (=> (and (At ?w ?t) (PRE ?w ?x ?s ?t)) (exists (?y ?u) (and (PARTICULAR ?y) (PARTICULAR ?u) (?g ?w ?y) (PP ?w ?u ?s) (PRE ?w ?y ?u ?t)))))))))

;(D86) P-1GD_S: Inverse Partial Generic Spatial Dependence (defrelation P1GD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (DJ ?w0 ?f ?g) (forall (?w ?x ?s ?t) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (PARTICULAR ?x) (PARTICULAR ?s) (PARTICULAR ?t) (?f ?w ?x)) (and (exists (?t1 ?s1)

147

(and (PARTICULAR ?t1) (PARTICULAR ?s1) (PRE ?w ?x ?s1 ?t1)) (=> (and (At ?w ?t) (PRE ?w ?x ?t)) (exists (?y ?u) (and (PARTICULAR ?y) (PARTICULAR ?u) (?g ?w ?y) (PP ?w ?s ?u) (PRE ?w ?y ?u ?t)))))))))

;(D87) DGD_S: Direct Generic Spatial Dependence (defrelation DGD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (GD.S ?w0 ?f ?g) (not (exists (?h) (and (UNIVERSAL ?h) (GD.S ?w0 ?f ?h) (GD.S ?w0 ?h ?g))))))

;(D88) Sdt_S: Temporary Specific Spatial Dependence (defrelation SDt.S (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (SD.S ?w0 ?x ?y) (PRE ?w0 ?x ?t)))

;(D89) GDt_S: Temp. Gen. Sp. Dep. (defrelation GDt.S (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (exists (?f ?g) (and (UNIVERSAL ?f) (UNIVERSAL ?g) (?f ?w0 ?x) (?g ?w0 ?y) (GD.S ?w0 ?f ?g) (˜.S.t ?w0 ?x ?y ?t)))))

;(D90) DGDt_S: Temp. Direct Sp. Dep. (defrelation DGDt.S (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (exists (?f ?g) (and (UNIVERSAL ?f) (UNIVERSAL ?g) (?f ?w0 ?x) (?g ?w0 ?y) (DGD.S ?w0 ?f ?g) (˜.S.t ?w0 ?x ?y ?t)))))

;(D91) OSD_S: One-sided Specific Spatial Dependence (defrelation OSD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SD.S ?w0 ?f ?g) (not (D ?w0 ?g ?f))))

;(D92) OGD_S: One-sided Generic Spatial Dependence (defrelation OGD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g)

148

(WORLD ?w0) (GD.S ?w0 ?f ?g) (not (D ?w0 ?g ?f))))

;(D93) MSD_S: Mutual Specific Spatial Dependence (defrelation MSD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SD.S ?w0 ?f ?g) (SD.S ?w0 ?g ?f)))

;(D94) MGD_S: Mutual Generic Spatial Dependence (defrelation MGD.S (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (GD.S ?w0 ?f ?g) (GD.S ?w0 ?g ?f)))

; Constitution ;(D95) DK: Direct Constitution (defrelation DK (?w0 ?x ?y ?t) := (and (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (WORLD ?w0) (K ?w0 ?x ?y ?t) (not (exists (?z) (and (PARTICULAR ?z) (K ?w0 ?x ?z ?t) (K ?w0 ?z ?y ?t))))))

;(D96) SK: Constantly Specifically Constituted by (defrelation SK (?w0 ?x ?y) := (or (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (forall (?w) (=> (and (WLDR ?w0 ?w) (WORLD ?w)) (and (exists (?t) (and (PARTICULAR ?t) (PRE ?w ?x ?t)) (forall (?t) (=> (and (PARTICULAR ?t) (PRE ?w ?x ?t)) (K ?w ?y ?x ?t)))))))) (and (UNIVERSAL ?x) (UNIVERSAL ?y) (WORLD ?w0) (DJ ?w0 ?f ?g) (forall (?w ?x1) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x1) (?f ?w ?x1)) (exists (?y1) (and (PARTICULAR ?y1) (?y ?w ?y1) (SK ?w ?x1 ?y1))))))))

;(D97) SK: Constantly Specifically Constituted by ;included in def (D96)

;(D98) GK: Constantly Generically Constituted by (defrelation GK (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (DJ ?w0 ?f ?g)

149

(forall (?w ?x ?t) (=> (and (WLDR ?w0 ?w) (WORLD ?w) (PARTICULAR ?x) (PARTICULAR ?t) (?f ?w ?x)) (and (exists (?t1) (and (PARTICULAR ?t1) (PRE ?w ?x ?t1))) (=> (and (At ?w ?t) (PRE ?w ?x ?t)) (exists (?y) (and (PARTICULAR ?y) (?g ?w ?y) (K ?w ?y ?x ?t)))))))))

;(D99) K__Constituted by (defrelation K (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (or (SK ?w0 ?f ?g) (GK ?w0 ?f ?g))))

;(D100) OSK: One-sided Cons. Specif. Const. by (defrelation OSK (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SK ?w0 ?f ?g) (not (K ?w0 ?g ?f))))

;(D101) OGK: One-sided Cons. Generic. Const. by (defrelation OGK (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (GK ?w0 ?f ?g) (not (K ?w0 ?g ?f))))

;(D102) MSK: Mutual Specific Constitution (defrelation MSK (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (SK ?w0 ?f ?g) (SK ?w0 ?g ?f)))

;(D103) MGK: Mutual Generic Constitution (defrelation MSK (?w0 ?f ?g) := (and (UNIVERSAL ?f) (UNIVERSAL ?g) (WORLD ?w0) (GK ?w0 ?f ?g) (GK ?w0 ?g ?f)))

; Characterization of functions and relations ; Parthood ; Argument Restrictions ;(A1) (forall (?w0 ?x ?y) (=> (and (P ?w0 ?x ?y) (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y)) (and (or (AB ?w0 ?x) (PD ?w0 ?x)) (or (AB ?w0 ?y) (PD ?w0 ?y)))))

;(A2) (forall (?w0 ?x ?y) (=> (and (P ?w0 ?x ?y)

150

(WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y)) (<=> (PD ?w0 ?x) (PD ?w0 ?y))))

;(A3) (forall (?w0 ?x ?y) (=> (and (P ?w0 ?x ?y) (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y)) (<=> (AB ?w0 ?x) (AB ?w0 ?y))))

;(A4) (forall (?w0 ?x ?y ?f) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (UNIVERSAL ?f) (P ?w0 ?x ?y) (SB ?w0 R ?f) (X ?f)) (<=> (?f ?w0 ?x) (?f ?w0 ?y))))

; Ground Axioms ;(A5) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (or (AB ?w0 ?x) (PD ?w0 ?x))) (P ?w0 ?x ?x)))

;(A6) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (P ?w0 ?x ?y) (P ?w0 ?y ?x)) (= ?x ?y)))

;(A7) (forall (?w0 ?x ?y ?z) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (P ?w0 ?x ?y) (P ?w0 ?y ?z)) (P ?w0 ?x ?z)))

;(A8) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (or (AB ?w0 ?x) (PD ?w0 ?x)) (not (P ?w0 ?x ?y))) (exists (?z) (and (PARTICULAR ?x) (P ?w0 ?z ?x) (not (O ?w0 ?z ?y))))))

;(A9) ; Note: this version in KIF consider only the universal explicitly listed ;[see comment on (D19)] (forall (?w0 ?f)

151

(=> (and (WORLD ?w0) (UNIVERSAL ?f) (exists (?x) (and (PARTICULAR ?x) (?f ?w0 ?x))) (or (forall (?x) (=> (and (PARTICULAR ?x) (?f ?w0 ?x)) (AB ?w0 ?x))) (forall (?x) (=> (and (PARTICULAR ?x) (?f ?w0 ?x)) (PD ?w0 ?x))))) (exists (?y) (and (PARTICULAR ?y) (sigma ?w0 ?f ?y)))))

; Temporary Parthood ; Argument restrictions ;(A10) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (P ?w0 ?x ?y ?t)) (and (ED ?w0 ?x) (ED ?w0 ?y) (T ?w0 ?t))))

;(A11) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (P ?w0 ?x ?y ?t)) (<=> (PED ?w0 ?x) (PED ?w0 ?y))))

;(A12) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (P ?w0 ?x ?y ?t)) (<=> (NPED ?w0 ?x) (NPED ?w0 ?y))))

; Ground Axioms ;(A13) (forall (?w0 ?x ?y ?z ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (PARTICULAR ?t) (P ?w0 ?x ?y ?t) (P ?w0 ?y ?z ?t)) (P ?w0 ?x ?z ?t)))

;(A14) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (ED ?w0 ?x) (ED ?w0 ?y) (PRE ?w0 ?x ?t) (PRE ?w0 ?y ?t) (not (P ?w0 ?x ?y ?t))) (exists (?z) (and (PARTICULAR ?z) (P ?w0 ?z ?x ?t)

152

(not (O ?w0 ?z ?y ?t))))))

;(A15) ;[see comment on (D19)] (forall (?w0 ?f) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (exists (?x) (and (PARTICULAR ?x) (?f ?w0 ?x))) (forall (?x) (=> (and (PARTICULAR ?x) (?f ?w0 ?x)) (ED ?w0 ?x)))) (exists (?y) (and (PARTICULAR ?y) (sigma.t ?w0 ?f ?y)))))

; Links With Other Primitives ;(A16) (forall (?w0 ?x ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?t) (ED ?w0 ?x) (PRE ?w0 ?x ?t)) (P ?w0 ?x ?x ?t)))

;(A17) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (P ?w0 ?x ?y ?t)) (and (PRE ?w0 ?x ?t) (PRE ?w0 ?y ?t))))

;(A18) (forall (?w0 ?x ?y ?t ?u) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (PARTICULAR ?u) (P ?w0 ?x ?y ?t) (P ?w0 ?u ?t)) (P ?w0 ?x ?y ?u)))

;(A19) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (PED ?w0 ?x) (P ?w0 ?x ?y ?t)) (incl.S.t ?w0 ?x ?y ?t)))

; Constitution ; Argument restrictions ;(A20) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (K ?w0 ?x ?y ?t)) (and (or (ED ?w0 ?x) (PD ?w0 ?x)) (or (ED ?w0 ?y) (PD ?w0 ?y)) (T ?w0 ?t))))

153

;(A21) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (K ?w0 ?x ?y ?t)) (<=> (PED ?w0 ?x) (PED ?w0 ?y))))

;(A22) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (K ?w0 ?x ?y ?t)) (<=> (NPED ?w0 ?x) (NPED ?w0 ?y))))

;(A23) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (K ?w0 ?x ?y ?t)) (<=> (PD ?w0 ?x) (PD ?w0 ?y))))

; Ground Axioms ;(A24) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (K ?w0 ?x ?y ?t)) (not (K ?w0 ?y ?x ?t))))

;(A25) (forall (?w0 ?x ?y ?z ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (PARTICULAR ?t) (K ?w0 ?x ?y ?t) (K ?w0 ?y ?z ?t)) (K ?w0 ?x ?z ?t)))

; Links with other Primitives ;(A26) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (K ?w0 ?x ?y ?t)) (and (PRE ?w0 ?x ?t) (PRE ?w0 ?y ?t))))

;(A27) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)) (<=> (K ?w0 ?x ?y ?t) (forall (?u) (=> (and (PARTICULAR ?u) (P ?w0 ?u ?t)) (K ?w0 ?x ?y ?u))))))

154

;(A28) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (PED ?w0 ?x) (K ?w0 ?x ?y ?t)) (˜.S.t ?w0 ?x ?y ?t)))

;(A29) (forall (?w0 ?x ?y ?y1 ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?y1) (PARTICULAR ?t) (K ?w0 ?x ?y ?t) (P ?w0 ?y1 ?y ?t)) (exists (?x1) (and (PARTICULAR ?x1) (P ?w0 ?x1 ?x ?t) (K ?w0 ?x1 ?y1 ?t)))))

; Links between Categories ;(A30) (forall (?w0) (=> (WORLD ?w0) (GK ?w0 NAPO M)))

;(A31) (forall (?w0) (=> (WORLD ?w0) (GK ?w0 APO NAPO)))

;(A32) (forall (?w0) (=> (WORLD ?w0) (GK ?w0 SC SAG)))

; Participation ; Argument restrictions ;(A33) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (PC ?w0 ?x ?y ?t)) (and (ED ?w0 ?x) (PD ?w0 ?y) (T ?w0 ?t))))

; Existential Axioms ;(a34) (forall (?w0 ?x ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?t) (PD ?w0 ?x) (PRE ?w0 ?x ?t)) (exists (?y) (and (PARTICULAR ?y) (PC ?w0 ?y ?x ?t)))))

;(a35) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (ED ?w0 ?x)) (exists (?y ?t) (and (PARTICULAR ?y) (PARTICULAR ?t) (PC ?w0 ?x ?y ?t)))))

; Links with other Primitives ;(a36) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x)

155

(PARTICULAR ?y) (PARTICULAR ?t) (PC ?w0 ?x ?y ?t)) (and (PRE ?w0 ?x ?t) (PRE ?w0 ?y ?t))))

;(a37) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)) (<=> (PC ?w0 ?x ?y ?t) (forall (?u) (=> (and (PARTICULAR ?u) (P ?w0 ?u ?t)) (PC ?w0 ?x ?y ?u))))))

; Quality ; Argument restrictions: ;(a38) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (qt ?w0 ?x ?y)) (and (Q ?w0 ?x) (or (Q ?w0 ?y) (ED ?w0 ?y) (PD ?w0 ?y)))))

;(a39) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (qt ?w0 ?x ?y)) (<=> (TQ ?w0 ?x) (or (TQ ?w0 ?y) (PD ?w0 ?y)))))

;(a40) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (qt ?w0 ?x ?y)) (<=> (PQ ?w0 ?x) (or (PQ ?w0 ?y) (PED ?w0 ?y)))))

;(a41) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (qt ?w0 ?x ?y)) (<=> (AQ ?w0 ?x) (or (AQ ?w0 ?y) (NPED ?w0 ?y)))))

; Ground Axioms: ;(a42) (forall (?w0 ?x ?y ?z) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (qt ?w0 ?x ?y) (qt ?w0 ?y ?z)) (qt ?w0 ?x ?z)))

;(a43) (forall (?w0 ?x ?y ?z) (=> (and (WORLD ?w0)

156

(PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (qt ?w0 ?x ?y) (qt ?w0 ?x ?z)) (= ?y ?z)))

;(a44) (forall (?w0 ?f ?x ?y ?z) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (qtf ?w0 ?f ?x ?y) (qtf ?w0 ?f ?z ?y)) (= ?x ?z)))

;(a45) (forall (?w0 ?f ?g ?x ?y ?z) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?z) (qtf ?w0 ?f ?x ?y) (qtf ?w0 ?g ?y ?z)) (DJ ?w0 ?f ?g)))

; Existential Axioms: ;(a46) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (TQ ?w0 ?x)) (exists (?y) (and (PARTICULAR ?y) (qt ?w0 ?x ?y) (PD ?w0 ?y) (forall (?z) (=> (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (PD ?w0 ?z)) (= ?z ?y)))))))

;(a47) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PQ ?w0 ?x)) (exists (?y) (and (PARTICULAR ?y) (qt ?w0 ?x ?y) (PED ?w0 ?y) (forall (?z) (=> (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (PED ?w0 ?z)) (= ?z ?y)))))))

;(a48) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (AQ ?w0 ?x)) (exists (?y) (and (PARTICULAR ?y) (qt ?w0 ?x ?y) (NPED ?w0 ?y) (forall (?z) (=> (and (PARTICULAR ?z) (qt ?w0 ?x ?z) (NPED ?w0 ?z))

157

(= ?z ?y)))))))

;(a49) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PD ?w0 ?x)) (exists (?y) (and (PARTICULAR ?y) (qtf ?w0 TL ?y ?x)))))

;(a50) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PED ?w0 ?x)) (exists (?y) (and (PARTICULAR ?y) (qtf ?w0 SL ?y ?x)))))

;(a51) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (NPED ?w0 ?x)) (exists (?f ?y) (and (PARTICULAR ?y) (UNIVERSAL ?f) (SBL ?w0 AQ ?f) (qtf ?w0 ?f ?y ?x)))))

; Quale ; Immediate Quale ; Argument restrictions: ;(A52) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (ql ?w0 ?x ?y)) (and (TR ?w0 ?x) (TQ ?w0 ?y))))

;(A53) (forall (?w0 ?x ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (ql ?w0 ?x ?y) (TL ?w0 ?y)) (T ?w0 ?x)))

; Basic Axioms: ;(A54) (forall (?w0 ?x ?x1 ?y) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?x1) (PARTICULAR ?y) (ql ?w0 ?x ?y) (ql ?w0 ?x1 ?y)) (= ?x ?x1)))

; Existential Axioms: ;(A55) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (TQ ?w0 ?x)) (exists (?y) (and (PARTICULAR ?y) (ql ?w0 ?y ?x)))))

;(A56) (forall (?w0 ?f ?x ?y ?r ?r1) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PARTICULAR ?x)

158

(PARTICULAR ?y) (PARTICULAR ?r) (PARTICULAR ?r1) (L.X ?w0 ?f) (?f ?w0 ?x) (?f ?w0 ?y) (ql ?w0 ?r ?x) (ql ?w0 ?r1 ?y)) (exists (?g) (and (UNIVERSAL ?g) (L.X ?w0 ?g) (?g ?w0 ?r) (?g ?w0 ?r1)))))

;(A57) (forall (?w0 ?f ?x ?y ?r ?r1) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?r) (PARTICULAR ?r1) (L.X ?w0 ?f) (?f ?w0 ?x) (not (?f ?w0 ?y)) (ql ?w0 ?r ?x) (ql ?w0 ?r1 ?y)) (not (exists (?g) (and (UNIVERSAL ?g) (L.X ?w0 ?g) (?g ?w0 ?r) (?g ?w0 ?r1))))))

; Temporary Quale ; Argument restrictions: ;(A58) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (ql ?w0 ?x ?y ?t)) (and (or (PR ?w0 ?x) (AR ?w0 ?x)) (or (PQ ?w0 ?y) (AQ ?w0 ?y)) (T ?w0 ?t))))

;(A59) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (ql ?w0 ?x ?y ?t)) (<=> (PR ?w0 ?x) (PQ ?w0 ?y))))

;(A60) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (ql ?w0 ?x ?y ?t)) (<=> (AR ?w0 ?x) (AQ ?w0 ?y))))

;(A61) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x)

159

(PARTICULAR ?y) (PARTICULAR ?t) (ql ?w0 ?x ?y ?t) (SL ?w0 ?y)) (S ?w0 ?x)))

; Existential Axioms: ;(A62) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x) (or (PQ ?w0 ?x) (AQ ?w0 ?x)) (PRE ?w0 ?x ?t)) (exists (?y) (and (PARTICULAR ?y) (ql ?w0 ?y ?x ?t)))))

;(A63) (forall (?w0 ?f ?x ?y ?r ?r1 ?t) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?r) (PARTICULAR ?r1) (PARTICULAR ?t) (L.X ?w0 ?f) (?f ?w0 ?x) (?f ?w0 ?y) (ql ?w0 ?r ?x ?t) (ql ?w0 ?r1 ?y ?t)) (exists (?g) (and (UNIVERSAL ?g) (L.X ?w0 ?g) (?g ?w0 ?r) (?g ?w0 ?r1)))))

;(A64) (forall (?w0 ?f ?x ?y ?r ?r1 ?t) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?r) (PARTICULAR ?r1) (PARTICULAR ?t) (L.X ?w0 ?f) (?f ?w0 ?x) (not (?f ?w0 ?y)) (ql ?w0 ?r ?x ?t) (ql ?w0 ?r1 ?y ?t)) (not (exists (?g) (and (UNIVERSAL ?g) (L.X ?w0 ?g) (?g ?w0 ?r) (?g ?w0 ?r1))))))

; Link with Parthood and extension: ;(A65) (forall (?w0 ?x ?y ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t) (ql ?w0 ?x ?y ?t)) (PRE ?w0 ?y ?t)))

;(A66) (forall (?w0 ?x ?y ?t)

160

(=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?y) (PARTICULAR ?t)) (<=> (ql ?w0 ?x ?y ?t) (forall (?u) (=> (and (PARTICULAR ?u) (P ?w0 ?u ?t)) (ql ?w0 ?x ?y ?u))))))

; Dependence and Spatial Dependence ; Links between categories ;(A67) (forall (?w0) (=> (WORLD ?w0) (MSD ?w0 TQ PD)))

;(A68) (forall (?w0) (=> (WORLD ?w0) (MSD.S ?w0 PQ PED)))

;(A69) (forall (?w0) (=> (WORLD ?w0) (MSD ?w0 AQ NPED)))

;(A70) (forall (?w0) (=> (WORLD ?w0) (OGD ?w0 F NAPO)))

;(A71) (forall (?w0) (=> (WORLD ?w0) (OSD ?w0 MOB APO)))

;(A72) (forall (?w0) (=> (WORLD ?w0) (OGD ?w0 SAG APO)))

;(A73) (forall (?w0) (=> (WORLD ?w0) (OGD ?w0 NASO SC)))

;(A74) (forall (?w0) (=> (WORLD ?w0) (OD ?w0 NPED PED)))

; Characterization of Categories ; Perdurant ; Conditions on Perdurant’s Leaves ;(A75) (forall (?w0 ?f) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PSBL ?w0 ACH ?f)) (and (NEP.S ?w0 ?f) (CM˜ ?w0 ?f) (AT ?w0 ?f))))

;(A76) (forall (?w0 ?f) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PSBL ?w0 ACC ?f)) (and (NEP.S ?w0 ?f) (CM˜ ?w0 ?f) (AT˜ ?w0 ?f))))

;(A77) (forall (?w0 ?f) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PSBL ?w0 ST ?f)) (and (NEP.S ?w0 ?f) (CM ?w0 ?f) (HOM ?w0 ?f))))

;(A78) (forall (?w0 ?f) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (PSBL ?w0 PRO ?f)) (and (NEP.S ?w0 ?f) (CM ?w0 ?f) (HOM˜ ?w0 ?f))))

; Existential Axioms ;(A79)

161

(forall (?w0) (=> (WORLD ?w0) (exists (?f) (and (UNIVERSAL ?f) (PSBL ?w0 ACH ?f)))))

;(A80) (forall (?w0) (=> (WORLD ?w0) (exists (?f) (and (UNIVERSAL ?f) (PSBL ?w0 ACC ?f)))))

;(A81) (forall (?w0) (=> (WORLD ?w0) (exists (?f) (and (UNIVERSAL ?f) (PSBL ?w0 ST ?f)))))

;(A82) (forall (?w0) (=> (WORLD ?w0) (exists (?f) (and (UNIVERSAL ?f) (PSBL ?w0 PRO ?f))))) ; ========================================= ; THEOREMS ; General Properties ; (T1) (forall (?w0 ?x ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?t)) (not (K ?w0 ?x ?x ?t))))

; (T2) (forall (?w0 ?f ?g) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (SK ?w0 ?f ?g)) (SD ?w0 ?f ?g)))

; (T3) (forall (?w0 ?f ?g) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (GK ?w0 ?f ?g)) (GD ?w0 ?f ?g)))

; (T4) (forall (?w0 ?f ?g ?h) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (UNIVERSAL ?h) (SK ?w0 ?f ?g) (SK ?w0 ?g ?h) (DJ ?w0 ?f ?h)) (SK ?w0 ?f ?h)))

; (T5) (forall (?w0 ?f ?g ?h) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (UNIVERSAL ?h) (GK ?w0 ?f ?g) (GK ?w0 ?g ?h) (DJ ?w0 ?f ?h)) (GK ?w0 ?f ?h)))

; Ground Properties ; (T6) (forall (?w0 ?x ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?t)) (not (PC ?w0 ?x ?x ?t))))

; (T7) (forall (?w0 ?x ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x)

162

(PARTICULAR ?y) (PARTICULAR ?t) (PC ?w0 ?x ?y ?t)) (not (PC ?w0 ?y ?x ?t))))

; (T8) (forall (?w0 ?x) (=> (and (WORLD ?w0) (PARTICULAR ?x)) (not (qt ?w0 ?x ?x))))

; General properties ; (T9) (forall (?w0 ?f ?g ?h) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (UNIVERSAL ?h) (SD ?w0 ?f ?g) (SD ?w0 ?g ?h) (DJ ?w0 ?f ?h)) (SD ?w0 ?f ?h)))

; (T10) (forall (?w0 ?f ?g ?h) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (UNIVERSAL ?h) (GD ?w0 ?f ?g) (GD ?w0 ?g ?h) (DJ ?w0 ?f ?h)) (GD ?w0 ?f ?h)))

; (T11) (forall (?w0 ?f ?g ?h) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (UNIVERSAL ?h) (SD ?w0 ?f ?g) (GD ?w0 ?g ?h) (DJ ?w0 ?f ?h)) (GD ?w0 ?f ?h)))

; (T12) (forall (?w0 ?f ?g ?h) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (UNIVERSAL ?h) (GD ?w0 ?f ?g) (SD ?w0 ?g ?h) (DJ ?w0 ?f ?h)) (GD ?w0 ?f ?h)))

; (T13) (forall (?w0 ?f ?g) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (SD.S ?w0 ?f ?g)) (SD ?w0 ?f ?g)))

; (T14) (forall (?w0 ?f ?g) (=> (and (WORLD ?w0) (UNIVERSAL ?f) (UNIVERSAL ?g) (GD.S ?w0 ?f ?g)) (GD ?w0 ?f ?g)))

; Being Present ; (T15) (forall (?w0 ?x)

163

(=> (and (WORLD ?w0) (PARTICULAR ?x) (or (ED ?w0 ?x) (PD ?w0 ?x) (Q ?w0 ?x))) (exists (?t) (and (PARTICULAR ?t) (PRE ?w0 ?x ?t)))))

; (T16) (forall (?w0 ?x ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?t) (or (PED ?w0 ?x) (PQ ?w0 ?x)) (PRE ?w0 ?x ?t)) (exists (?s) (and (PARTICULAR ?s) (PRE ?w0 ?s ?x ?t)))))

; (T17) (forall (?w0 ?x ?t ?t1) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?t) (PARTICULAR ?t1) (PRE ?w0 ?x ?t) (P ?w0 ?t1 ?t)) (PRE ?w0 ?x ?t1)))

; (T18) (forall (?w0 ?x ?s ?t) (=> (and (WORLD ?w0) (PARTICULAR ?x) (PARTICULAR ?s) (PARTICULAR ?t) (PRE ?w0 ?s ?x ?t)) (PRE ?w0 ?x ?t)))

164

14 APPENDIX B: KIF version of OCHRE

;============================================================ ; THE OBJECT-CENTRED HIGH-LEVEL REFERENCE ONTOLOGY ; (OCHRE) ; ; Translation in the Knowledge Interchange Format (KIF) ; (American National Standard NCITS.T2/98-004) ; (http://logic.stanford.edu/kif/dpans.html) ; ; in the framework of ; EC IST Project 2001-33052 ; WONDERWEB: ONTOLOGY INFRASTRUCTURE FOR THE SEMANTIC WEB ; ; version: 2.1 ; date: December 13, 2003 ; author: Luc Schneider ; institute: Department of Philosophy, University of Geneva ; e-mail: schneil3@etu.unige.ch ;=============================================================

;============ ; THE DOMAIN ;============

; Existence of particulars (exists (?x) (particular ?x))

;======================================== ; MEREOLOGY - THEORY OF PARTS AND WHOLES ;========================================

; DEFINITIONS OF MEREOLOGY ;==============================

; ----Sameness---- (defrelation same (?x ?y) := (and (part_of ?x ?y) (part_of ?y ?x)))

; ----Proper parthood---- (defrelation proper_part_of (?x ?y) := (and (part_of ?x ?y) (not (same ?x ?y))))

; ----Overlap---- (defrelation overlap (?x ?y) := (exists (?z) (and (part_of ?z ?x) (part_of ?z ?y))))

; ----Underlap---- (defrelation underlap (?x ?y) := (exists (?z) (and (part_of ?x ?z) (part_of ?y ?z))))

; ----Atom---- (defrelation atom (?x) := (and (particular ?x) (not

165

(exists (?y) (proper_part_of ?y ?x)))))

; ----Atomic part---- (defrelation atomic_part_of (?x ?y) := (and (atom ?x) (part_of ?x ?y)))

; ----Complex---- (defrelation complex (?x) := (and (particular ?x) (not (atom ?x))))

; ----Sum---- (defrelation sum (?x ?y ?z) := (forall (?w) (<=> (part_of ?w ?x) (or (part_of ?w ?y) (part_of ?w ?z)))))

; ----Product---- (defrelation product (?x ?y ?z) := (forall (?w) (<=> (part_of ?w ?x) (and (part_of ?w ?y) (part_of ?w ?z)))))

; ----Difference---- (defrelation difference (?x ?y ?z) := (forall (?w) (<=> (part_of ?w ?x) (and (part_of ?w ?y) (not (overlap ?w ?z))))))

; ----Universe---- (defrelation universe (?x) := (forall (?y) (part_of ?y ?x)))

; AXIOMS OF MEREOLOGY ;========================

; ----Parthood---- (forall (?x ?y) (=> (part_of ?x ?y) (and (particular ?x) (particular ?y))))

; ----Reflexivity of parthood---- (forall (?x) (=> (particular ?x) (part_of ?x ?x)))

; ----Transitivity of parthood----

166

(forall (?x ?y ?z) (=> (and (part_of ?x ?y) (part_of ?y ?z)) (part_of ?x ?z)))

; ----Sameness implies identity of particulars---- (forall (?x ?y) (<=> (same ?x ?y) (and (particular ?x) (particular ?y) (= ?x ?y))))

; ----Atomicity---- (forall (?x) (=> (particular ?x) (exists (?y) (atomic_part_of ?y ?x))))

; ----Extensionality---- (forall (?x ?y) (=> (and (particular ?x) (particular ?y) (forall (?z) (=> (atomic_part_of ?z ?x) (atomic_part_of ?z ?y)))) (part_of ?x ?y)))

; ----Existence of sum---- (forall (?x ?y) (=> (underlap ?x ?y) (exists (?w) (sum ?w ?x ?y))))

; ----Uniqueness of sum---- (forall (?x ?y ?z ?w) (=> (and (sum ?x ?z ?w) (sum ?y ?z ?w)) (same ?x ?y)))

; ----Existence of product---- (forall (?x ?y) (=> (overlap ?x ?y) (exists (?w) (product ?w ?x ?y))))

; ----Uniqueness of product---- (forall (?x ?y ?z ?w) (=> (and (product ?x ?z ?w) (product ?y ?z ?w)) (same ?x ?y)))

; ----Existence of universe---- (exists (?x) (universe ?x))

167

; ----Uniqueness of universe---- (forall (?x ?y) (=> (and (universe ?x) (universe ?y)) (same ?x ?y)))

;=========================== ; THE THEORY OF FOUNDATIONS ;===========================

; DEFINITIONS OF THE THEORY OF FOUNDATIONS ;==========================================

; ----Strong foundation---- (defrelation strongly_founded_on (?x ?y) := (and (founded_on ?x ?y) (not (part_of ?y ?x))))

; ----One-sided foundation---- (defrelation one-sidedly_founded_on (?x ?y) := (and (founded_on ?x ?y) (not (founded_on ?y ?x))))

; ----Mutual foundation---- (defrelation mutually_founded_on (?x ?y) := (and (founded_on ?x ?y) (founded_on ?y ?x)))

; ----Thin object---- (defrelation thin_object (?x) := (and (complex ?x) (forall (?y) (=> (founded_on ?x ?y) (part_of ?y ?x)))))

; ----Integral whole---- (defrelation integral_wole (?x) := (and (complex ?x) (forall (?y ?z) (=> (and (atomic_part_of ?y ?x) (atomic_part_of ?z ?x)) (or (founded_on ?y ?z) (founded_on ?z ?y))))))

; AXIOMS OF THE THEORY OF FOUNDATIONS ;=====================================

; ----Foundation---- (forall (?x ?y) (=> (founded_on ?x ?y) (and (particular ?x)

168

(particular ?y))))

; ----Reflexivity of foundation---- (forall (?x) (=> (particular ?x) (founded_on ?x ?x)))

; ----Transitivity of foundation---- (forall (?x ?y ?z) (=> (and (founded_on ?x ?y) (founded_on ?y ?z)) (founded_on ?x ?z)))

; ----Wholes are founded on their parts---- (forall (?x ?y) (=> (part_of ?y ?x) (founded_on ?x ?y)))

; ----Something is founded on a whole, ; if it is founded on all its atomic parts.---- (forall (?x ?y) (=> (forall (?z) (=> (atomic_part_of ?z ?y) (founded_on ?x ?z))) (founded_on ?x ?y)))

; ----Existence of thin objects---- (exists (?x) (thin_object ?x))

; ----Thin objects are integral wholes.---- (forall (?x) (=> (thin_object ?x) (integral_whole ?x)))

;========================== ; THE THEORY OF SIMILARITY ;==========================

; DEFINITIONS OF THE THEORY OF SIMILARITY ;=========================================

; ----Exact similarity---- (defrelation exactly_similar (?x ?y) := (forall (?z) (<=> (similar ?x ?z) (similar ?y ?z))))

; ----Resemblance---- (defrelation resembles (?x ?y) := (and (complex ?x) (complex ?y) (exists (?z ?w) (and (atomic_part_of ?z ?x) (atomic_part_of ?w ?y) (exactly_similar ?z ?w)))))

; ----Complete resemblance----

169

(defrelation completely_resembles (?x ?y) := (and (complex ?x) (complex ?y) (forall (?z) (=> (atomic_part_of ?z ?x) (exists (?w) (and (atomic_part_of ?w ?y) (exactly_similar ?z ?w)))))))

; ----Exact resemblance---- (defrelation exactly_resembles (?x ?y) := (and (completely_resembles ?x ?y) (completely_resembles ?y ?x)))

; AXIOMS OF THE THEORY OF SIMILARITY ;====================================

; ----Similarity---- (forall (?x ?y) (=> (similar ?x ?y) (and (atom ?x) (atom ?y))))

; ----Reflexivity of similarity---- (forall (?x) (=> (atom ?x) (similar ?x ?x)))

; ----Symmetry of similarity---- (forall (?x ?y) (=> (similar ?x ?y) (similar ?y ?x)))

; ----Comparability---- (forall (?x ?y) (=> (comparable ?x ?y) (and (atom ?x) (atom ?y))))

; ----Symmetry of comparability---- (forall (?x ?y) (=> (comparable ?x ?y) (comparable ?y ?x)))

; ----Transitivity of comparability---- (forall (?x ?y ?z) (=> (and (comparable ?x ?y) (comparable ?y ?z)) (comparable ?x ?z)))

; ----Similarity implies comparability---- (forall (?x ?y) (=> (similar ?x ?y)

170

(comparable ?x ?y)))

;========================================= ; TOPOLOGY - THE THEORY OF SPACE AND TIME ;=========================================

; DEFINITIONS OF TOPOLOGY ;=========================

; ----Thick object---- (defrelation thick_object (?x) := (exists (?y) (connected ?x ?y)))

; ----Thick parthood---- (defrelation thick_part_of (?x ?y) := (and (thick_object ?x) (thick_object ?y) (part_of ?x ?y)))

; ----Enclosure---- (defrelation enclosed (?x ?y) := (forall (?z) (=> (connected ?x ?z) (connected ?y ?z))))

; ----Coincidence---- (defrelation coincident (?x ?y) := (and (enclosed ?x ?y) (enclosed ?y ?x)))

; ----Immediate anteriority---- (defrelation immediately_anterior (?x ?y) := (and (anterior ?x ?y) (not (exists (?z) (and (anterior ?x ?z) (anterior ?z ?y))))))

; ----Temporal overlap---- (defrelation temporally_overlaps (?x ?y) := (and (not (anterior ?x ?y)) (not (anterior ?y ?x))))

; ----Simultaneity---- (defrelation simultaneous (?x ?y) := (forall (?z) (<=> (temporally_overlaps ?x ?z) (temporally_overlaps ?y ?z))))

; B - AXIOMS OF TOPOLOGY ;========================

; ----Connection---- (forall (?x ?y) (=> (connected ?x ?y) (and (complex ?x)

171

(complex ?y) (not (thin_object ?x)) (not (thin_object ?y)))))

; ----Reflexivity of connection---- (forall (?x) (=> (thick_object ?x) (connected ?x ?x)))

; ----Symmetry of connection---- (forall (?x ?y) (=> (connected ?x ?y) (connected ?y ?x)))

; ----Anteriority---- (forall (?x ?y) (=> (anterior ?x ?y) (and (thick_object ?x) (thick_object ?y))))

; ----Irreflexivity of anteriority---- (forall (?x) (not (anterior ?x ?x)))

; ----Transitivity of anteriority---- (forall (?x ?y ?z) (=> (and (anterior ?x ?y) (anterior ?y ?z)) (anterior ?x ?z)))

; ----Temporal order---- (forall (?x) (=> (thick_object ?x) (exists (?y) (or (anterior ?x ?y) (anterior ?y ?x)))))

; ----Existence of thick objects---- (exists (?x) (thick_object ?x))

; ----Mereotopological invariance---- (forall (?x ?y) (=> (connected ?x ?y) (simultaneous ?x ?y)))

; ----Monotonicity---- (forall (?x ?y) (=> (thick_part_of ?x ?y) (enclosed ?x ?y)))

; ----Extensionality---- (forall (?x ?y) (=>

172

(coincident ?x ?y) (same ?x ?y)))

;========================== ; THE THEORY OF PROPERTIES ;==========================

;========================================= ; DEFINITIONS OF THE THEORY OF PROPERTIES ;=========================================

; ----Thin parthood---- ; A part of a thick object which is not itself ; a thick object is called a thin part. (defrelation thin_part_of (?x ?y) := (and (part_of ?x ?y) (thick_object ?y) (not (thick_object ?x))))

; ----Direct parthood---- ; A thin part which does not overlap with any ; of the (proper) thick parts of a thick object ; is called a direct part. (defrelation direct_part_of (?x ?y) := (and (thin_part_of ?x ?y) (not (exists (?z) (and (thick_part ?z ?y) (not (same ?z ?y)) (overlaps ?x ?z))))))

; ----Haecceity---- ; A thin object that is a direct part of a thick ; object is called an haecceity of that thick object. (defrelation haecceity (?x ?y) := (and (thin_object ?x) (direct_part_of ?x ?y)))

; ----Property---- ; A direct part of a thick object that does not ; overlap with an haecceity is called a property. (defrelation property (?x ?y) := (and (direct_part_of ?x ?y) (forall (?z) (=> (haecceity ?z ?y) (not (overlaps ?x ?z))))))

; ----Integral property---- ; Complex properties that form integral wholes, ; e.g., colours (composed of saturations, hues ; and brightnesses), are called integral properties. (defrelation integral_property (?x ?y) := (and (property ?x ?y) (integral_whole ?x)))

; ----Guise or facet---- ; A direct part containing an haecceity and all ; the properties founded on the latter is called

173

; a guise or facet. ; E.g. the statue and the clay are not distinct ; thick objects, but guises, hence thin parts, ; of the same thick object. (defrelation guise (?x ?y ?z) := (and (direct_part_of ?x ?y) (haecceity ?z ?y) (forall (?w) (<=> (part_of ?w ?x) (or (same ?w ?z) (and (property ?w ?y) (founded_on ?w ?z)))))))

;==================================== ; AXIOMS OF THE THEORY OF PROPERTIES ;====================================

; ----Tropes are direct parts of thick objects.---- (forall (?x) (=> (atom ?x) (exists (?y) (direct_part_of ?x ?y))))

; ----Comparable direct parts---- (forall (?x ?y ?z) (=> (and (comparable ?x ?y) (direct_part_of ?x ?z) (direct_part_of ?y ?z)) (same ?x ?y)))

; ----Existence of haecceities---- (forall (?x) (=> (thick_object ?x) (exists (?y) (haecceity ?y ?x))))

; ----Unicity of simultaneous stages---- (forall (?x ?y ?z) (=> (and (haecceity ?x ?y) (haecceity ?x ?z) (simultaneous ?y ?z)) (same ?y ?z)))

; ----Property foundation: 1---- (forall (?x ?y) (=> (property ?x ?y) (exists (?z) (and (haecceity ?z ?y) (founded_on ?x ?z)))))

; ----Property foundation: 2---- (forall (?x ?y ?z ?w) (=> (and (property ?x ?y)

174

(haecceity ?z ?y) (haecceity ?w ?y) (founded_on ?x ?z) (founded_on ?x ?w)) (same ?z ?w)))

;===================================== ; THE THEORY OF RELATIONAL PROPERTIES ;=====================================

;==================================================== ; DEFINITIONS OF THE THEORY OF RELATIONAL PROPERTIES ;====================================================

; ----Relational property---- (defrelation relational_property (?x ?y) := (and (property ?x ?y) (exists (?z ?w) (and (haecceity ?z ?w) (not (haecceity ?z ?y)) (not (same ?w ?y)) (founded_on ?x ?z)))))

; ----Relatum---- (defrelation relatum (?x ?y) := (and (exists (?z) (relational_property ?y ?z)) (exists (?w) (haecceity ?x ?w)) (founded_on ?y ?x)))

;=================================================== ; B - AXIOMS OF THE THEORY OF RELATIONAL PROPERTIES ;===================================================

; ----Precedence---- (defrelation precedes (?x ?y ?z) :=> (and (relatum ?x ?z) (relatum ?y ?z)))

; ----Irreflexivity of precedence---- (forall (?x ?y) (not (precedes ?x ?x ?y)))

; ---- Transitivity of precedence---- (forall (?x ?y ?z ?w) (=> (and (precedes ?x ?y ?w) (precedes ?y ?z ?w)) (precedes ?x ?z ?w)))

; ----Order of precedence---- (forall (?x ?y ?z) (=> (and (relatum ?x ?z) (relatum ?y ?z)) (or (precedes ?x ?y ?z)

175

(precedes ?y ?x ?z))))

;============================= ; THE THEORY OF EVENTUALITIES ;=============================

;============================================ ; DEFINITIONS OF THE THEORY OF EVENTUALITIES ;============================================

; ----Succession---- (defrelation succeeds (?x ?y ?z) := (and (immediately_anterior ?y ?x) (haeceeity ?z ?x) (haecceity ?z ?y)))

; ----Event in---- (defrelation event_in (?x ?y) := (exists (?z ?w) (and (succeeds ?z ?w ?y) (sum ?x ?z ?w))))

; ----Event---- (defrelation event (?x) := (exists (?y) (event_in ?x ?y)))

; ----Process---- (defrelation process (?x) := (and (eventuality ?x) (not (event ?x))))

; ----Life---- (defrelation life (?x ?y) := (and (eventuality ?x) (thin_object ?y) (forall (?z) (<=> (part_of ?z ?x) (event_in ?z ?y)))))

; ----Participation---- (defrelation participates (?x ?y) := (and (thin_object ?x) (eventuality ?y) (exists (?z) (and (event_in ?z ?x) (part_of ?z ?y)))))

;======================================= ; AXIOMS OF THE THEORY OF EVENTUALITIES ;=======================================

; ----Succession: unicity on the left---- (forall (?x ?y ?z ?w) (=> (and (succeeds ?z ?x ?y) (succeeds ?w ?x ?y)) (same ?z ?w)))

176

; ----Succession: unicity on the right---- (forall (?x ?y ?z ?w) (=> (and (succeeds ?x ?y ?z) (succeeds ?x ?y ?w)) (same ?z ?w)))

; ----Thin objects as haecceities---- (forall (?x) (=> (thin_object ?x) (exists (?y ?z) (and (thick_object ?y) (thick_object ?z) (succeeds ?y ?z ?x)))))

; ----Eventuality: 1---- (forall (?x) (=> (event ?x) (eventuality ?x)))

; ----Eventuality: 2---- (forall (?x ?y ?z) (=> (and (event ?x) (eventuality ?y) (sum ?z ?x ?y)) (eventuality ?z)))

177

15 APPENDIX C: DOLCE-Lite-Plus

Scope of DOLCE-Lite+

The“lite” versions of DOLCE are simpliﬁed translations of DOLCE2.0 into various logical languages. They are maintained for several reasons:

1. allowing the implementation of DOLCE-based ontologies in languages that are less expressive than FOL. In particular, DOLCE-Lite does not make use of S5 modalities and of some temporally-indexed relations. Modal operators are not heavily exploited in DOLCE, then the consequences are not very harmful for most uses. Temporal indexing is partly supported by ’composing’ originally indexed relations with temporal location relations. Even this support is not provided for description logic versions of DOLCE-Lite like DAML+OIL, OWL-DL, etc.

2. allowing a description-logic-like naming policy for DOLCE signature. In many cases, different names are adopted for relations that have the same name but different arities in the FOL version, or for relations that have polymorphic domains

3. allowing extensions of DOLCE that do not have a detailed axiomatization yet, and modularizing them

4. taking beneﬁt of the services of certain implemented languages -specially the classiﬁcation services provided by description logics- in order to support domain applications

In this report, we describe the current structure of the DOLCE-Lite+ ontology library, and we brieﬂy summarize the content of the extensions, their purpose and applications in realistic domains. As an appendix, we include the code for the library in two languages: a dialect of KIF3.0 (PL), and DAML+OIL. The ﬁrst one contains a complete code for the library, including the WordNet alignment modules. The second one contains the library (according to available costructs of DAML+OIL) without the WordNet code, since it is very simple and takes much space. DOLCE-Lite+KIF is currently used in some applications that need deep inferences, which can only be provided by expressive, logic-programming-like languages. DOLCE-Lite+DAML is currently used in Semantic Web applications, for example in the Core Ontology for Services (COS), extensively described in section xxx. The extensions to DOLCE presented in the library are work in progress, and although some of them have been tested in realistic applications, they should be taken cautiously from the viewpoint of rigorous formal ontology.

Structure of DOLCE-Lite+

Currently, DOLCE-Lite+ is designed as follows (ﬁg:library):

1. The ”Top” module contains only the topmost distinctions of the signature. Among unary relations, the topmost classes are ”entity” (aka ”particular”), ”formal-property”, and ”universal”. The instances of ”universal” are subclasses of ”entity” or ”formal-property”. ”Formal-property” is used to implement so-called ”meta-properties”, such as those deﬁned in the Onto- Clean methodology [48]. ”Entity” is the topmost class for individuals. Among binary relations, ”immediate-relation” and ”mediated-relation” are those holding between entities. An ”immediate-relation” is a relation that holds without additional mediating individuals. In logical terms, it is a non-composed relation. A ”mediated-relation” holds through other mediating individuals. Logically, it is a relation that composes other relations. For example, a ”temporary-participation” relation is a participation relation (holding between objects and events) composed with a mereological relation, because a ”part” relation allows to talk of the participation of an object to part of an event. Other relations are present for reasons related to the fea- tures of implemented logics, rather than for ontological completeness. For example, ”entity-to-constant-relation” allows to link so-called ”abstract data” i.e. entities, individuals of a domain that exist ’outside’ the information service that uses the ontology (e.g. dogs, walkings, thoughts, colors, etc.), with so-called ”concrete data” i.e. individuals of a domain existing ’inside’ the information service that uses the ontology (e.g. integers, strings, etc.).

2. The ”DOLCE” module contains the ’lite’ version of DOLCE2.0, with some customization due to the application experiences carried out so far. Among classes, the basic taxonomy is the same as DOLCE2.0. Among binary relations, the following branches are currently characterized:

• Identity. Total order, ontological identity.

• Part. Mereology is characterized in both atemporal (for any entity) and temporalized (only for endurants) ways. Proper-part and component (qualiﬁed proper part) relations are introduced.

• Constitution. Member relations are considered constituencies (see section on DOLCE).

• Connection. Both weak (no common boundary) and strong (common boundary) relations are characterized. Succes- sion relations are also introduced as primitives, and in both direct and indirect form.

• Attribution. Inherence of qualities in entities, and representation of qualities within abstract regions are both charac- terized.

• Participation. Participation of endurants in perdurants is characterized both as atemporal, and temporalized. Mereo- logical varieties of participation (complete, temporary, constant) are deﬁned. An attempts to characterize ”functional” participation is presented in a lower module.

178

• Localization. This is the branching that goes farthest from DOLCE2.0, since we have tried to capture some naive notions of location by means of mediated relations. ”Generic-location” has been introduced to catch both ”exact” and ”approximate” localizations. Exact ones hold between entities and regions. Approximate ones hold between entities (regions are mediating individuals related through mereological relations. Approximate localization relations are deﬁned in a lower module

• Dependency. Both speciﬁc and generic dependence are characterized. Some subrelations are deﬁned for different domains.

3. The ”Descriptions” module contains the larger and most peculiar extension to DOLCE. It is described in a dedicated section below. Unary and binary relations are highly interrelated, since the module implements the so-called theory of ”descriptions and situations” ([37]) in the form of a ”design pattern” that can be applied to many domains without important modiﬁcations. The basic classes are: ”description”, furtherly distinguished into ”c-description” (concept description) and ”s-description” (situation description), and ”situation”. S-descriptions have c-descriptions as components. C-descriptions have different functions and are distinguished into ”courses”, ”roles”, and ”parameters”. Each c-description ’describes’ the way an entity is found in a situation. The structure of c-descriptions that are components of an s-description constitutes a set of partial rules that can be employed to ’recognize’ a situation. This machinery allows to talk of the descriptions we use to perceive, to create, to regulate, etc. any kind of state of affairs. The basic binary relations are: ”satisﬁed-by”, holding between s-descriptions and situations; ”selects”, holding between c-descriptions and entities in a state of affairs; ”setting-for”, holding between situations and entities in a state of affairs. Other relations allow to add structure to the c-descriptions within a same s-description. Other classes and relations are deﬁned to (minimally) introduce important types of descriptions and roles, such as plans, norms, techniques, systems, social roles, organizations, agents vs. patients, etc. Another important distinction introduced here is that between physical and ”functional” endurants. Functionality (as represented through roles) creates a kind of ’layering’ in the ontology, since the same amount of matter can be seen as such (e.g. a piece of clay), or as a physical object (a statue), or as functionally-viewed matter (clay used for its therapeutical properties), or as a functional object (a memorial statue). These four views can be considered four different entities, although they are co-located and bear certain dependencies.

4. The ”Communication” module contains a simple sketch of a communication theory by using the theory of descriptions (indeed, the two theories are interrelated, since descriptions depend on some intentional agent and on her communication practices). The theory characterised here is composed of some basic semiotic notions (”expression”, ”meaning”, ”context”, ”represents”, ”interpretant”, etc.), and of Jakobson’s theory of communicative functions (”encoder”, ”decoder”, ”message”, ”channel”, ”context”, ”code”). The theory has been used to characterize P2P communication.

5. The ”Extrinsic” module contains some relations to link entities with concrete data like strings and numbers.

6. The ”Modalities” module contains the characterization of modal relations as they are treated by legal theorists such as Hohfeld and L. Allen. It is far than complete, but it shows how the theory of descriptions can be used to represent modal notions at ﬁrst order. Modalities is built around the four basic notions of ”right, ”power”, ”privilege”, and ”immunity”, with their converses.

7. The ”Time Topology” module contains an adaptation of J. Allen’s temporal relations to DOLCE-Lite+. Temporal relations hold here between perdurants, and are ”mediated” relations, since they need a mediating time interval (that is the universe of discourse in the original Allen’s theory). Mereotopological relations are used to deﬁne temporal relations.

8. The ”Places” module contains the deﬁnition of several ”approximate” localization relation (see above). It also contains some classes to distinguishes physical and non-physical (e.g. ”political”) geographical entities, geographical features, etc.

9. The ”Functional Participation” module contains functionally-viewed participation relations, such as ”performs”, ”used-in”, ”target-of”, ”consequence-of”, etc. Such relations constrain participation within the scope of an s-description: an event is participated by an object according to an s-description and its components. The module also contains the deﬁnition of some further classes of perdurants, such as ”activity” and ”phenomenon”, which stand on intentionality as a differential criterion.

10. The ”Plans” module contains an attempt to characterize planning concepts according to the theory of descriptions. Plans are taken to be a kind of ”method” (an s-description), whose peculiar components are ”tasks” that provide instructions to execute actions. Goals are considered both as s-descriptions (”goal-descriptions”) and expected goal-situations that satisfy goal- descriptions. Pre- and post-conditions are also characterized. A typical algebra of tasks (case, branching, synchronization, concurrency, cycling, etc.) is characterized with the help of succession relations. Tasks are distinguished from the executed actions; consequently, the status of a procedure (e.g. ”started”) belongs to a different class from the status of a task (e.g. ”accepted”). Moreover, some classes are deﬁned to talk of plan representation: ﬂow charts, join and fork nodes, etc.

11. The ”Systems” module contains very few classes to get some basic meanings of ”system” and ”artifact”.

12. The ”WNATOP” module contains some classes needed to make a preliminary alignment of the WordNet nouns taxonomy. It also shows some domain-oriented examples of application of DOLCE-Lite+ classes.

13. The ”WNAT” module contains the 809 classes corresponding to the so-called ”synsets” from WordNet 1.6 [28]that have been aligned to DOLCE-Lite+. This alignment has allowed the use of WordNet as a plugin to DOLCE. Some experiments seem very encouraging [2], but much reﬁnement is still needed to get a sound ontological organization of the entire WordNet.

179

14. The ”Services” module contains a preliminary alignment of the DAML-S ontology into DOLCE-Lite+. It is not only an alignment, since the scope of a core ontology of services is wider than the DAML-S one.

15. Various other modules are being built or maintained, notably for the legal domain, for the biomedical domain, for banking and ﬁnance, etc.

Figure 18: The DOLCE-Lite+ Library

180

KIF version of DOLCE-Lite+ (PL dialect)

(DEFMODULE "TOP" :INCLUDES ())

(IN-MODULE "TOP")

(DEFCONCEPT UNIVERSAL (?SELF) :=> (CONCEPT ?SELF))

(DEFCONCEPT ENTITY (?SELF) :AXIOMS (UNIVERSAL ENTITY))

(DEFRELATION FORMAL-PROPERTY (?SELF))

(DEFRELATION EXTRINSIC-RELATION (?A ?B) :AXIOMS (SYMMETRIC EXTRINSIC-RELATION))

(DEFRELATION IMMEDIATE-RELATION (?A ?B) :AXIOMS (AND (SYMMETRIC IMMEDIATE-RELATION) (DOCUMENTATION IMMEDIATE-RELATION "A relation that holds without additional mediating individuals. In logical terms, a non-composed relation.")))

(DEFRELATION META-RELATION (?A ?B) :AXIOMS (SYMMETRIC META-RELATION))

(DEFRELATION TERNARY-META-RELATION (?A ?B ?C))

(DEFRELATION ENTITY-TO-CONSTANT-RELATION (?A ?B))

(DEFRELATION CONSTANT-TO-ENTITY-RELATION (?A ?B) :AXIOMS (INVERSE CONSTANT-TO-ENTITY-RELATION ENTITY-TO-CONSTANT-RELATION))

(DEFRELATION TERNARY-CONCEPTUAL-RELATION (?A ?B ?C))

(DEFRELATION CONCEPT-TO-ENTITY-RELATION (?A ?B))

(DEFRELATION ENTITY-TO-CONCEPT-RELATION (?A ?B) :AXIOMS (INVERSE ENTITY-TO-CONCEPT-RELATION CONCEPT-TO-ENTITY-RELATION))

(DEFRELATION RELATION-TO-ENTITY-RELATION (?A ?B))

(DEFRELATION ENTITY-TO-RELATION-RELATION (?A ?B) :AXIOMS (INVERSE ENTITY-TO-RELATION-RELATION RELATION-TO-ENTITY-RELATION))

(DEFRELATION MEDIATED-RELATION (?A ?B) :<=> (EXISTS (?C) (AND (IMMEDIATE-RELATION ?A ?C) (IMMEDIATE-RELATION ?C ?B)))) :AXIOMS (AND (SYMMETRIC MEDIATED-RELATION) (DOCUMENTATION MEDIATED-RELATION "A relation that composes other relations. For example, a participation relation composed with a representation relation.")))

(DEFRELATION MEDIATED-EXTRINSIC-RELATION (?A ?B) :<=> (EXISTS (?C) (AND (EXTRINSIC-RELATION ?A ?C) (EXTRINSIC-RELATION ?C ?B)))) :AXIOMS (SYMMETRIC MEDIATED-RELATION))

(DEFRELATION HYBRID-RELATION (?A ?B) :<=> (EXISTS (?C) (AND (IMMEDIATE-RELATION ?A ?C) (ENTITY-TO-CONSTANT-RELATION ?C ?B)))))

(DEFRELATION INVERSE-HYBRID-RELATION (?A ?B) :AXIOMS (INVERSE INVERSE-HYBRID-RELATION HYBRID-RELATION))

(DEFRELATION HYBRID-MEDIATED-RELATION (?A ?B) :<=> (EXISTS (?C)

181

(AND (MEDIATED-RELATION ?A ?C) (ENTITY-TO-CONSTANT-RELATION ?C ?B)))))

(DEFRELATION INVERSE-HYBRID-MEDIATED-RELATION (?A ?B) :AXIOMS (INVERSE INVERSE-HYBRID-MEDIATED-RELATION HYBRID-MEDIATED-RELATION))

(ASSERT (= (INVERSE CONSTANT-TO-ENTITY-RELATION) ENTITY-TO-CONSTANT-RELATION))

(ASSERT (= (INVERSE ENTITY-TO-CONCEPT-RELATION) CONCEPT-TO-ENTITY-RELATION))

(ASSERT (= (INVERSE ENTITY-TO-RELATION-RELATION) RELATION-TO-ENTITY-RELATION))

(ASSERT (= (INVERSE INVERSE-HYBRID-RELATION) HYBRID-RELATION))

(ASSERT (= (INVERSE INVERSE-HYBRID-MEDIATED-RELATION) HYBRID-MEDIATED-RELATION))

(ASSERT (forall (?a ?b) (=>> (EXTRINSIC-RELATION ?a ?b) (LITERAL ?b))))

(ASSERT (forall (?a ?b) (=>> (EXTRINSIC-RELATION ?a ?b) (LITERAL ?a))))

(ASSERT (forall (?a ?b) (=>> (IMMEDIATE-RELATION ?a ?b) (ENTITY ?b))))

(ASSERT (forall (?a ?b) (=>> (IMMEDIATE-RELATION ?a ?b) (ENTITY ?a))))

(ASSERT (forall (?a ?b) (=>> (ENTITY-TO-CONSTANT-RELATION ?a ?b) (LITERAL ?b))))

(ASSERT (forall (?a ?b) (=>> (ENTITY-TO-CONSTANT-RELATION ?a ?b) (ENTITY ?a))))

(ASSERT (forall (?a ?b ?c) (=>> (and (TERNARY-CONCEPTUAL-RELATION ?a ?b ?c) (ENTITY ?a) (ENTITY ?b)) (ENTITY ?c))))

(ASSERT (forall (?a ?b) (=>> (META-RELATION ?a ?b) (RELATION ?b))))

(ASSERT (forall (?a ?b) (=>> (META-RELATION ?a ?b) (RELATION ?a))))

(ASSERT (forall (?a ?b) (=>> (CONCEPT-TO-ENTITY-RELATION ?a ?b) (ENTITY ?b))))

(ASSERT (forall (?a ?b) (=>> (RELATION-TO-ENTITY-RELATION ?a ?b) (ENTITY ?b))))

(ASSERT (forall (?a ?b) (=>> (RELATION-TO-ENTITY-RELATION ?a ?b) (RELATION ?a))))

(ASSERT (forall (?a ?b) (=>> (exists (?c) (and (MEDIATED-RELATION ?a ?c)

182

(IMMEDIATE-RELATION ?c ?b))) (MEDIATED-RELATION ?a ?b))))

(ASSERT (forall (?a ?b) (=>> (exists (?c) (and (IMMEDIATE-RELATION ?a ?c) (MEDIATED-RELATION ?c ?b))) (MEDIATED-RELATION ?a ?b))))

(ASSERT (BINARY-RELATION CONSTANT-TO-ENTITY-RELATION))

(ASSERT (BINARY-RELATION ENTITY-TO-CONCEPT-RELATION))

(ASSERT (BINARY-RELATION ENTITY-TO-RELATION-RELATION))

(ASSERT (BINARY-RELATION INVERSE-HYBRID-RELATION))

(ASSERT (BINARY-RELATION INVERSE-HYBRID-MEDIATED-RELATION))

(DEFMODULE "TOP/DOLCE" :INCLUDES ("TOP") :SHADOW (FEATURE MEMBER-OF ABSTRACT SET))

(IN-MODULE "TOP/DOLCE")

(DEFCONCEPT FEATURE (?SELF) :=> (PHYSICAL-ENDURANT ?SELF) :AXIOMS (DOCUMENTATION FEATURE "Features are ’parasitic entities’, that exist insofar their host exists. Typical examples of features are holes, bumps, boundaries, or spots of color. Features may be relevant parts of their host, like a bump or an edge, or dependent regions like a hole in a piece of cheese, the underneath of a table, the front of a house, or the shadow of a tree, which are not parts of their host. All features are essential wholes, but no common unity criterion may exist for all of them. However, typical features have a topological unity, as they are singular entities."))

(DEFCONCEPT ABSTRACT (?SELF) :=> (ENTITY ?SELF) :AXIOMS (DOCUMENTATION ABSTRACT "The main characteristic of abstract entities is that they do not have spatial nor temporal qualities, and they are not qualities themselves. The only class of abstract entities we consider in the present version of the upper ontology is that of quality regions (or simply regions). Quality spaces are special kinds of quality regions, being mereological sums of all the regions related to a certain quality type. The other examples of abstract entities (sets and facts) are only indicative."))

(DEFCONCEPT SET (?SELF) :=> (ABSTRACT ?SELF))

(DEFRELATION IDENTITY-C (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (AND (REFLEXIVE IDENTITY-C) (SYMMETRIC IDENTITY-C) (TRANSITIVE IDENTITY-C) (DOCUMENTATION IDENTITY-C "Any pair of individuals are ontologically identical if they are identical to themselves. This is the non-extrinsic TBox version

183

of the ’identity’ relation. A total order: reflexive, symmetric, and transitive. Being ontologically identical does not imply being notionally identical.")))

(DEFRELATION DIFFERENT-P (?A ?B) :<=> (AND (IMMEDIATE-RELATION ?A ?B) (NOT (IDENTITY-C ?A ?B))) :AXIOMS (AND (IRREFLEXIVE DIFFERENT-P) (SYMMETRIC DIFFERENT-P)))

(DEFRELATION PART (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (AND (REFLEXIVE PART) (TRANSITIVE PART) (DOCUMENTATION PART "The most generic part relation. A partial order (reflexive, asymmetric, and transitive).")))

(DEFRELATION PART-OF (?A ?B) :<=> (PART ?B ?A))

(DEFRELATION ATOM ((?A ENTITY)) :<=> (NOT (EXISTS ?X (AND (ENTITY ?X) (PROPER-PART ?A ?X)))))

(DEFRELATION TEMPORARY-PART (?A ?B) :<=> (AND (PART ?A ?B) (ENDURANT ?A) (ENDURANT ?B) (PARTLY-COMPRESENT-WITH ?A ?B)) :AXIOMS (DOCUMENTATION TEMPORARY-PART "Being part at time t. It holds for endurants only. This is important to model parts that can change or be lost over time without affecting the identity of the whole. In FOL, this is expressed as a ternary relation, but in DLs we only can reason with binary relations, then only the necessary axiom of compresence is represented here."))

(DEFRELATION TEMPORARY-PART-OF (?A ?B) :<=> (TEMPORARY-PART ?B ?A))

(DEFRELATION PROPER-PART (?A ?B) :<=> (AND (PART ?A ?B) (NOT (IDENTITY-C ?A ?B))) :AXIOMS (AND (IRREFLEXIVE PROPER-PART) (ANTISYMMETRIC PROPER-PART) (TRANSITIVE PROPER-PART) (DOCUMENTATION PROPER-PART "The proper part relation: irreflexive, antisymmetric, and transitive.")))

(DEFRELATION PROPER-PART-OF (?A ?B) :<=> (PROPER-PART ?B ?A))

(DEFRELATION OVERLAPS (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PART ?A ?C) (PART-OF ?C ?B)))) :AXIOMS (AND (SYMMETRIC OVERLAPS) (DOCUMENTATION OVERLAPS "Mereological overlap: having a common part.")))

(DEFRELATION SIBLING-PART (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PART-OF ?A ?C) (PART ?C ?B)))) :AXIOMS (AND (SYMMETRIC SIBLING-PART) (DOCUMENTATION SIBLING-PART "Mereological sibling: having a common whole")))

(DEFRELATION TEMPORARY-PROPER-PART (?A ?B) :<=> (AND (PROPER-PART ?A ?B) (ENDURANT ?A) (ENDURANT ?B) (PARTLY-COMPRESENT-WITH ?A ?B)) :AXIOMS (DOCUMENTATION TEMPORARY-PROPER-PART "Being proper part at time t. It holds for endurants only. This is important to model proper parts that can change or be lost over time without affecting the identity of the whole."))

184

(DEFRELATION TEMPORARY-PROPER-PART-OF (?A ?B) :<=> (TEMPORARY-PROPER-PART ?B ?A))

(DEFRELATION COMPONENT (?A ?B) :=> (PROPER-PART ?A ?B) :AXIOMS (AND (IRREFLEXIVE COMPONENT) (ANTISYMMETRIC COMPONENT)))

(DEFRELATION COMPONENT-OF (?A ?B) :<=> (COMPONENT ?B ?A))

(DEFRELATION TEMPORARY-COMPONENT (?A ?B) :<=> (AND (COMPONENT ?A ?B) (ENDURANT ?A) (ENDURANT ?B) (PARTLY-COMPRESENT-WITH ?A ?B)) :AXIOMS (DOCUMENTATION TEMPORARY-COMPONENT "Being component at time t. It holds for endurants only. This is important to model components that can change or be lost over time without affecting the identity of the whole."))

(DEFRELATION TEMPORARY-COMPONENT-OF (?A ?B) :<=> (TEMPORARY-COMPONENT ?B ?A))

(DEFRELATION CONSTITUENT (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION CONSTITUENT "’Constituent’ should depend on some layering of the ontology. For example, scientific granularities or ontological ’strata’ are typical layerings. A constituent is a part belonging to a lower layer. Since layering is actually a partition of the ontology, constituents are not properly classified as parts, although this kinship can be intuitive for common sense. Example of constituents are the entities constituting a setting (a situation), the entities constituting a collection, etc."))

(DEFRELATION CONSTITUENT-OF (?A ?B) :<=> (CONSTITUENT ?B ?A))

(DEFRELATION HAS-MEMBER (?A ?B) :=> (CONSTITUENT ?A ?B) :AXIOMS (DOCUMENTATION HAS-MEMBER "Being a constituent in a countable collection, for example: member of a society, bacterium in a colony, etc."))

(DEFRELATION MEMBER-OF (?A ?B) :<=> (HAS-MEMBER ?B ?A))

(DEFRELATION WEAK-CONNECTION (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (AND (SYMMETRIC WEAK-CONNECTION) (DOCUMENTATION WEAK-CONNECTION "The basic connection, not requiring a common boundary.")))

(DEFRELATION BOUNDARY-OF (?A ?B) :=> (PROPER-PART-OF ?A ?B) :AXIOMS (DOCUMENTATION BOUNDARY-OF "A boundary here is taken to be a part (mereological treatment). Consequently, in the case of endurants, (reified) boundaries are features."))

(DEFRELATION BOUNDARY (?A ?B) :<=> (BOUNDARY-OF ?B ?A) :AXIOMS (SINGLE-VALUED BOUNDARY))

(DEFRELATION STRONG-CONNECTION (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C ?D) (AND (BOUNDARY ?A ?C) (OVERLAPS ?C ?D) (BOUNDARY-OF ?D ?B)))) :AXIOMS (AND (SYMMETRIC STRONG-CONNECTION) (DOCUMENTATION STRONG-CONNECTION "By strong connection here we mean a connection between

185

two entities that share a boundary.")))

(DEFRELATION T-SUCCESSOR (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION T-SUCCESSOR "To be understood as ’entity x has successor y’. Succession does not exclude connection, but it excludes overlapping (see rules files). It can be direct or indirect, and assumes a choice (temporal, spatial, abstract, etc. Cf. the cognitive ’path’ schema."))

(DEFRELATION T-PREDECESSOR (?A ?B) :<=> (T-SUCCESSOR ?B ?A) :AXIOMS (DOCUMENTATION T-PREDECESSOR "To be understood as ’entity x has predecessor y’."))

(DEFRELATION DIRECT-SUCCESSOR (?A ?B) :=> (T-SUCCESSOR ?A ?B) :AXIOMS (DOCUMENTATION DIRECT-SUCCESSOR "Anti-transitive succession."))

(DEFRELATION DIRECT-PREDECESSOR (?A ?B) :<=> (DIRECT-SUCCESSOR ?B ?A) :AXIOMS (DOCUMENTATION DIRECT-PREDECESSOR "To be understood as ’entity x has predecessor y’."))

(DEFRELATION INDIRECT-SUCCESSOR (?A ?B) :<=> (AND (T-SUCCESSOR ?A ?B) (EXISTS (?C) (AND (DIRECT-SUCCESSOR ?A ?C) (DIRECT-SUCCESSOR ?C ?B)))) :AXIOMS (DOCUMENTATION INDIRECT-SUCCESSOR "Transitive succession."))

(DEFRELATION INDIRECT-PREDECESSOR (?A ?B) :<=> (INDIRECT-SUCCESSOR ?B ?A))

(DEFRELATION INHERENT-IN (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION INHERENT-IN "The immediate relation holding for qualities and entities."))

(DEFRELATION HAS-QUALITY (?A ?B) :<=> (INHERENT-IN ?B ?A))

(DEFRELATION T-INHERENT-IN (?A ?B) :<=> (AND (INHERENT-IN ?A ?B) (EXISTS (?C) (AND (Q-LOCATION ?A ?C) (TEMPORAL-REGION ?C) (EXACT-LOCATION-OF ?C ?B) (TEMPORAL-REGION ?C)))) :AXIOMS (DOCUMENTATION T-INHERENT-IN "The immediate relation holding for qualities and entities at time t."))

(DEFRELATION HAS-T-QUALITY (?A ?B) :<=> (T-INHERENT-IN ?B ?A))

(DEFRELATION Q-LOCATION (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION Q-LOCATION "The immediate relation holding for qualities and regions. See ’generic location’ branching for the various mediated relations that embed q-location."))

(DEFRELATION Q-LOCATION-OF (?A ?B) :<=> (Q-LOCATION ?B ?A))

(DEFRELATION HAS-QUALE (?A ?B) :=> (Q-LOCATION ?A ?B))

(DEFRELATION QUALE-OF (?A ?B) :<=> (HAS-QUALE ?B ?A))

186

(DEFRELATION HOST (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION HOST "The immediate relation holding for features and entities."))

(DEFRELATION HOST-OF (?A ?B) :<=> (HOST ?B ?A))

(DEFRELATION PARTICIPANT (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION PARTICIPANT "The immediate relation holding between endurants and perdurants."))

(DEFRELATION PARTICIPANT-IN (?A ?B) :<=> (PARTICIPANT ?B ?A))

(DEFRELATION COMPLETE-PARTICIPANT (?A ?B) :<=> (AND (PARTICIPANT ?A ?B) (FORALL (?C) (=> (PART ?B ?C) (PARTICIPANT ?A ?C)))) :AXIOMS (DOCUMENTATION COMPLETE-PARTICIPANT "x participates in y with all its parts."))

(DEFRELATION COMPLETE-PARTICIPANT-IN (?A ?B) :<=> (COMPLETE-PARTICIPANT ?B ?A))

(DEFRELATION TEMPORARY-PARTICIPANT (?A ?B) :<=> (AND (PARTICIPANT ?A ?B) (EXISTS (?C) (AND (PART ?A ?C) (PARTICIPANT ?C ?B)))) :AXIOMS (DOCUMENTATION TEMPORARY-PARTICIPANT "x participates in some of y’s parts."))

(DEFRELATION TEMPORARY-PARTICIPANT-IN (?A ?B) :<=> (TEMPORARY-PARTICIPANT ?B ?A))

(DEFRELATION TOTAL-PARTICIPANT (?A ?B) :<=> (AND (PARTICIPANT ?A ?B) (FORALL (?C) (=> (PART ?A ?C) (PARTICIPANT ?C ?B)))) :AXIOMS (DOCUMENTATION TOTAL-PARTICIPANT "x participates in all y’s parts."))

(DEFRELATION TOTAL-PARTICIPANT-IN (?A ?B) :<=> (TOTAL-PARTICIPANT ?B ?A))

(DEFRELATION GENERIC-LOCATION (?A ?B) :=> (MEDIATED-RELATION ?A ?B) :AXIOMS (DOCUMENTATION GENERIC-LOCATION "The most generic mediated (indirect) location relation. This is meant to support naive localization, between any kinds of entities. Generic location is primarily branched into ’exact’ location, ranging on regions, and ’approximate’ location, ranging on non-regions."))

(DEFRELATION GENERIC-LOCATION-OF (?A ?B) :<=> (GENERIC-LOCATION ?B ?A))

(DEFRELATION EXACT-LOCATION (?A ?B) :<=> (AND (GENERIC-LOCATION ?A ?B) (REGION ?B) (EXISTS (?C) (AND (HAS-QUALITY ?A ?C) (Q-LOCATION ?C ?B)))) :AXIOMS (DOCUMENTATION EXACT-LOCATION "Location relation bounded to regions and defined analytically through the composition of inherence and q-location."))

(DEFRELATION EXACT-LOCATION-OF (?A ?B) :<=> (EXACT-LOCATION ?B ?A))

(DEFRELATION PHYSICAL-LOCATION (?A ?B) :<=> (AND (EXACT-LOCATION ?A ?B) (PHYSICAL-ENDURANT ?A) (PHYSICAL-REGION ?B)) :AXIOMS (DOCUMENTATION PHYSICAL-LOCATION "Analytical location holding between physical endurants and physical

187

regions."))

(DEFRELATION PHYSICAL-LOCATION-OF (?A ?B) :<=> (PHYSICAL-LOCATION ?B ?A))

(DEFRELATION SPATIAL-LOCATION (?A ?B) :<=> (AND (PHYSICAL-LOCATION ?A ?B) (PHYSICAL-ENDURANT ?A) (SPACE-REGION ?B)) :AXIOMS (DOCUMENTATION SPATIAL-LOCATION "Analytical location holding between physical endurants and spatial regions."))

(DEFRELATION SPATIAL-LOCATION-OF (?A ?B) :<=> (SPATIAL-LOCATION ?B ?A))

(DEFRELATION P-SPATIAL-LOCATION (?A ?B) :<=> (AND (EXACT-LOCATION ?A ?B) (PERDURANT ?A) (SPACE-REGION ?B) (EXISTS (?C) (AND (PARTICIPANT ?A ?C) (PHYSICAL-ENDURANT ?C) (SPATIAL-LOCATION ?C ?B)))) :AXIOMS (DOCUMENTATION P-SPATIAL-LOCATION "Analytical indirect location holding between perdurants and space regions."))

(DEFRELATION P-SPATIAL-LOCATION-OF (?A ?B) :<=> (P-SPATIAL-LOCATION ?B ?A))

(DEFRELATION TEMPORAL-LOCATION (?A ?B) :<=> (AND (EXACT-LOCATION ?A ?B) (PERDURANT ?A) (TEMPORAL-REGION ?B)) :AXIOMS (DOCUMENTATION TEMPORAL-LOCATION "Analytical location holding between physical perdurants and temporal regions."))

(DEFRELATION TEMPORAL-LOCATION-OF (?A ?B) :<=> (TEMPORAL-LOCATION ?B ?A))

(DEFRELATION DURATION (?A ?B) :=> (TEMPORAL-LOCATION ?A ?B))

(DEFRELATION DURATION-OF (?A ?B) :<=> (DURATION ?B ?A))

(DEFRELATION E-TEMPORAL-LOCATION (?A ?B) :<=> (AND (EXACT-LOCATION ?A ?B) (ENDURANT ?A) (TEMPORAL-REGION ?B) (EXISTS (?C) (AND (PARTICIPANT-IN ?A ?C) (PERDURANT ?C) (TEMPORAL-LOCATION ?C ?B)))) :AXIOMS (DOCUMENTATION E-TEMPORAL-LOCATION "Analytical indirect location holding between endurants and temporal regions."))

(DEFRELATION E-TEMPORAL-LOCATION-OF (?A ?B) :<=> (E-TEMPORAL-LOCATION ?B ?A))

(DEFRELATION ABSTRACT-LOCATION (?A ?B) :<=> (AND (EXACT-LOCATION ?A ?B) (NON-PHYSICAL-ENDURANT ?A) (ABSTRACT-REGION ?B)) :AXIOMS (DOCUMENTATION ABSTRACT-LOCATION "Analytical location holding between non-physical endurants and abstract regions."))

(DEFRELATION ABSTRACT-LOCATION-OF (?A ?B) :<=> (ABSTRACT-LOCATION ?B ?A))

(DEFRELATION DEPEND-ON-SPATIAL-LOCATION (?A ?B) :<=> (AND (EXACT-LOCATION ?A ?B) (NON-PHYSICAL-ENDURANT ?A) (SPACE-REGION ?B) (EXISTS (?C) (AND (PHYSICALLY-DEPENDS-ON ?A ?C) (NON-PHYSICAL-ENDURANT ?A) (PHYSICAL-ENDURANT ?C) (SPATIAL-LOCATION ?C ?B) (SPACE-REGION ?B)))) :AXIOMS (DOCUMENTATION DEPEND-ON-SPATIAL-LOCATION "Analytical indirect location holding between non-physical endurants

188

and space regions."))

(DEFRELATION DEPEND-ON-SPATIAL-LOCATION-OF (?A ?B) :<=> (DEPEND-ON-SPATIAL-LOCATION ?B ?A))

(DEFRELATION PRESENT-AT (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (E-TEMPORAL-LOCATION ?A ?C) (ENDURANT ?A) (TIME-INTERVAL ?C) (PART ?C ?B) (TIME-INTERVAL ?B)))) :AXIOMS (DOCUMENTATION PRESENT-AT "Presence is axiomatized as being temporally located in a part of one’s life."))

(DEFRELATION TIME-OF-PRESENCE-OF (?A ?B) :<=> (PRESENT-AT ?B ?A))

(DEFRELATION PARTLY-COMPRESENT-WITH (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PRESENT-AT ?A ?C) (PRESENT-AT ?B ?C)))) :AXIOMS (SYMMETRIC PARTLY-COMPRESENT-WITH))

(DEFRELATION Q-PRESENT-AT (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C ?D) (AND (INHERENT-IN ?A ?C) (PHYSICAL-QUALITY ?A) (PHYSICAL-ENDURANT ?C) (E-TEMPORAL-LOCATION ?C ?D) (TIME-INTERVAL ?D) (PART ?D ?B) (TIME-INTERVAL ?B)))) :AXIOMS (DOCUMENTATION Q-PRESENT-AT "Presence of a physical quality when inheres in an endurant."))

(DEFRELATION TIME-OF-Q-PRESENCE-OF (?A ?B) :<=> (Q-PRESENT-AT ?B ?A))

(DEFRELATION HAPPENS-AT (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (TEMPORAL-LOCATION ?A ?C) (PERDURANT ?A) (TIME-INTERVAL ?C) (PART ?C ?B) (TIME-INTERVAL ?B)))) :AXIOMS (DOCUMENTATION HAPPENS-AT "Perdurant presence (happening) is axiomatized as being temporally located at a point in one’s life."))

(DEFRELATION TIME-OF-HAPPENING-OF (?A ?B) :<=> (HAPPENS-AT ?B ?A))

(DEFRELATION SPECIFICALLY-CONSTANTLY-DEPENDENT-ON (?A ?B) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION SPECIFICALLY-CONSTANTLY-DEPENDENT-ON "The constant dependence between two individuals. Taken here as primitive."))

(DEFRELATION SPECIFIC-CONSTANT-DEPEND-ON-OF (?A ?B) :<=> (SPECIFICALLY-CONSTANTLY-DEPENDENT-ON ?B ?A))

(DEFRELATION GENERICALLY-DEPENDS-ON (?A ?B) :<=> (AND (IMMEDIATE-RELATION ?A ?B) (EXISTS (?P) (AND (SUPERRELATION ?P ENTITY) (INSTANCE-OF ?B ?P)))) :AXIOMS (DOCUMENTATION GENERICALLY-DEPENDS-ON "The dependence on an individual of a given type."))

(DEFRELATION GENERIC-DEPEND-ON-OF (?A ?B) :<=> (GENERICALLY-DEPENDS-ON ?B ?A))

(DEFRELATION E-DEPENDS-ON (?A ?B) :<=> (AND (SPECIFICALLY-CONSTANTLY-DEPENDENT-ON ?A ?B) (ENDURANT ?A) (ENDURANT ?B)) :AXIOMS (DOCUMENTATION E-DEPENDS-ON "Specific dependence between endurants.

189

The only constraint given here is temporal co-occurrence (correlation), but an interesting form of dependence should include some causality context."))

(DEFRELATION E-DEPEND-ON-OF (?A ?B) :<=> (E-DEPENDS-ON ?B ?A))

(DEFRELATION PHYSICALLY-DEPENDS-ON (?A ?B) :<=> (AND (E-DEPENDS-ON ?A ?B) (NON-PHYSICAL-ENDURANT ?A) (PHYSICAL-ENDURANT ?B)) :AXIOMS (DOCUMENTATION PHYSICALLY-DEPENDS-ON "Specific dependence of non-physical on physical endurants."))

(DEFRELATION PHYSICAL-DEPEND-ON-OF (?A ?B) :<=> (PHYSICALLY-DEPENDS-ON ?B ?A))

(DEFRELATION DESCRIPTIVELY-DEPENDS-ON (?A ?B) :<=> (AND (E-DEPENDS-ON ?A ?B) (ENDURANT ?A) (NON-PHYSICAL-ENDURANT ?B)) :AXIOMS (DOCUMENTATION DESCRIPTIVELY-DEPENDS-ON "Specific dependence of endurants on non-physical endurants."))

(DEFRELATION DESCRIPTIVE-DEPEND-ON-OF (?A ?B) :<=> (DESCRIPTIVELY-DEPENDS-ON ?B ?A))

(DEFRELATION TEMPORARILY-DEPENDS-ON (?A ?B) :=> (AND (E-DEPENDS-ON ?A ?B) (PARTLY-COMPRESENT-WITH ?A ?B)) :AXIOMS (DOCUMENTATION TEMPORARILY-DEPENDS-ON "Specific, but temporary dependence between endurants."))

(DEFRELATION TEMPORARY-DEPEND-ON-OF (?A ?B) :<=> (TEMPORARILY-DEPENDS-ON ?B ?A))

(DEFRELATION P-DEPENDS-ON (?A ?B) :<=> (AND (IMMEDIATE-RELATION ?A ?B) (PERDURANT ?A) (PERDURANT ?B) (FORALL ?Z (=> (AND (TIME-INTERVAL ?Z) (HAPPENS-AT ?A ?Z) (NOT (PART ?A ?B))) (HAPPENS-AT ?B ?Z)))) :AXIOMS (DOCUMENTATION P-DEPENDS-ON "Primitive dependence between perdurants. The only constraint given here is temporal co-occurrence (correlation), but an interesting form of dependence should include some causality context."))

(DEFRELATION P-DEPEND-ON-OF (?A ?B) :<=> (P-DEPENDS-ON ?B ?A))

(DEFCONCEPT ENDURANT (?SELF) :=> (ENTITY ?SELF) :AXIOMS (DOCUMENTATION ENDURANT "The main characteristic of endurants is that all of them are independent essential wholes. This does not mean that the corresponding property (being an endurant) carries proper unity, since there is no common unity criterion for endurants. Endurants can ’genuinely’ change in time, in the sense that the very same endurant as a whole can have incompatible properties at different times. To see this, suppose that an endurant say ’this paper’ has a property at a time t ’it’s white’, and a different, incompatible property at time t’ ’it’s yellow’: in both cases we refer to the whole object, without picking up any particular part of it. Within endurants, we distinguish between physical and non-physical endurants, according to whether they have direct spatial qualities. Within physical endurants, we distinguish between amounts of matter, objects, and features. "))

(DEFCONCEPT ARBITRARY-SUM (?SELF) :=> (ENDURANT ?SELF))

190

(DEFCONCEPT PHYSICAL-ENDURANT (?SELF) :=> (ENDURANT ?SELF))

(DEFCONCEPT AMOUNT-OF-MATTER (?SELF) :=> (PHYSICAL-ENDURANT ?SELF) :AXIOMS (DOCUMENTATION AMOUNT-OF-MATTER "The common trait of amounts of matter is that they are endurants with no unity (according to Gangemi et a. 2001 none of them is an essential whole). Amounts of matter - ’stuffs’ referred to by mass nouns like ’gold’, ’iron’, ’wood’, ’sand’, ’meat’, etc. - are mereologically invariant, in the sense that they change their identity when they change some parts."))

(DEFCONCEPT RELEVANT-PART (?SELF) :=> (FEATURE ?SELF))

(DEFCONCEPT DEPENDENT-PLACE (?SELF) :=> (FEATURE ?SELF))

(DEFCONCEPT PHYSICAL-OBJECT (?SELF) :=> (PHYSICAL-ENDURANT ?SELF) :AXIOMS (DOCUMENTATION PHYSICAL-OBJECT " The main characteristic of physical objects is that they are endurants with unity. However, they have no common unity criterion, since different subtypes of objects may have different unity criteria. Differently from aggregates, (most) physical objects change some of their parts while keeping their identity, they can have therefore temporary parts. Often physical objects (indeed, all endurants) are ontologically independent from occurrences (discussed below). However, if we admit that every object has a life, it is hard to exclude a mutual specific constant dependence between the two. Nevertheless, we may still use the notion of dependence to (weakly) characterize objects as being not specifically constantly dependent on other objects."))

(DEFCONCEPT AGENTIVE-PHYSICAL-OBJECT (?SELF) :=> (PHYSICAL-OBJECT ?SELF) :AXIOMS (DOCUMENTATION AGENTIVE-PHYSICAL-OBJECT " Within Physical objects, a special place have those to which we ascribe intentions, beliefs, and desires. These are called Agentive, as opposite to Non-agentive. Intentionality is understood here as the capability of heading for/dealing with objects or states of the world. This is an important area of ontological investigation we haven’t properly explored yet, so our suggestions are really very preliminary. In general, we assume that agentive objects are constituted by non-agentive objects: a person is constituted by an organism, a robot is constituted by some machinery, and so on. Among non-agentive physical objects we have for example houses, body organs, pieces of wood, etc. "))

(DEFCONCEPT NATURAL-PERSON (?SELF) :=> (AGENTIVE-PHYSICAL-OBJECT ?SELF) :AXIOMS (DOCUMENTATION NATURAL-PERSON "A person ontologically dependent on an organism"))

(DEFCONCEPT NON-AGENTIVE-PHYSICAL-OBJECT (?SELF)

191

:=> (PHYSICAL-OBJECT ?SELF) :AXIOMS (DOCUMENTATION NON-AGENTIVE-PHYSICAL-OBJECT " Within Physical objects, a special place have those those to which we ascribe intentions, beliefs, and desires. These are called Agentive, as opposite to Non-agentive. Intentionality is understood here as the capability of heading for/dealing with objects or states of the world. This is an important area of ontological investigation we haven’t properly explored yet, so our suggestions are really very preliminary. A possible modelling of case roles has been started within the descriptions plugin (see file: descriptions.lisp) that could be embedded within basic DOLCE. In general, we assume that agentive objects are constituted by non-agentive objects: a person is constituted by an organism, a robot is constituted by some machinery, and so on. Among non-agentive physical objects we have for example houses, body organs, pieces of wood, etc. "))

(DEFCONCEPT UNITARY-COLLECTION (?SELF) :=> (NON-AGENTIVE-PHYSICAL-OBJECT ?SELF) :AXIOMS (DOCUMENTATION UNITARY-COLLECTION "A non-agentive physical object constituted by members of definite kinds."))

(DEFCONCEPT NON-PHYSICAL-ENDURANT (?SELF) :=> (ENDURANT ?SELF) :AXIOMS (DOCUMENTATION NON-PHYSICAL-ENDURANT "An endurant having only abstract qualities. Its temporal or spatial qualities are inherited by the physical endurants it depends on."))

(DEFCONCEPT QUALITY (?SELF) :=> (ENTITY ?SELF) :AXIOMS (DOCUMENTATION QUALITY " Qualities can be seen as the basic entities we can perceive or measure: shapes, colors, sizes, sounds, smells, as well as weights, lengths, electrical charges... ’Quality’ is often used as a synonymous of ’property’, but this is not the case in this upper ontology: qualities are particulars, properties are universals. Qualities inhere to entities: every entity (including qualities themselves) comes with certain qualities, which exist as long as the entity exists."))

(DEFCONCEPT TEMPORAL-QUALITY (?SELF) :=> (QUALITY ?SELF) :AXIOMS (DOCUMENTATION TEMPORAL-QUALITY "A quality inherent only in perdurants."))

(DEFCONCEPT PHYSICAL-QUALITY (?SELF) :=> (QUALITY ?SELF) :AXIOMS (DOCUMENTATION PHYSICAL-QUALITY "A quality inherent only in physical endurants."))

(DEFCONCEPT ABSTRACT-QUALITY (?SELF) :=> (QUALITY ?SELF) :AXIOMS (DOCUMENTATION ABSTRACT-QUALITY "A quality inherent only in non-physical endurants."))

(DEFCONCEPT TEMPORAL-LOCATION-Q (?SELF) :=> (TEMPORAL-QUALITY ?SELF))

192

(DEFCONCEPT SPATIAL-LOCATION-Q (?SELF) :=> (PHYSICAL-QUALITY ?SELF))

(DEFCONCEPT REGION (?SELF) :=> (ABSTRACT ?SELF) :AXIOMS (DOCUMENTATION REGION "We distinguish between a quality (e.g., the color of a specific rose), and its value (e.g., a particular shade of red). The latter is called quale, and describes the position of an individual quality within a certain conceptual space (called here quality space) Gardenfors (2000). So when we say that two roses have (exactly) the same color, we mean that their color qualities, which are distinct, have the same position in the color space, that is they have the same color quale."))

(DEFCONCEPT TEMPORAL-REGION (?SELF) :=> (REGION ?SELF) :AXIOMS (DOCUMENTATION TEMPORAL-REGION "A region at which only temporal qualities can be directly located. It assumes a metrics for time."))

(DEFCONCEPT PHYSICAL-REGION (?SELF) :=> (REGION ?SELF) :AXIOMS (DOCUMENTATION PHYSICAL-REGION "A region at which only physical qualities can be directly located. It assumes some metrics for physical properties."))

(DEFCONCEPT ABSTRACT-REGION (?SELF) :=> (REGION ?SELF) :AXIOMS (DOCUMENTATION ABSTRACT-REGION "A region at which only abstract qualities can be directly located. It assumes some metrics for abstract (neither physical nor temporal) properties."))

(DEFCONCEPT TIME-INTERVAL (?SELF) :=> (TEMPORAL-REGION ?SELF))

(DEFCONCEPT SPACE-REGION (?SELF) :=> (PHYSICAL-REGION ?SELF))

(DEFCONCEPT SPATIO-TEMPORAL-REGION (?SELF) :=> (SPACE-REGION ?SELF))

(DEFCONCEPT QUALE (?SELF) :<=> (AND (REGION ?SELF) (NOT (EXISTS (?A) (PROPER-PART ?SELF ?A)))))

(DEFCONCEPT PERDURANT (?SELF) :=> (ENTITY ?SELF) :AXIOMS (DOCUMENTATION PERDURANT "Perdurants (also called occurrences) comprise what are variously called events, processes, phenomena, activities and states. They can have temporal parts or spatial parts. For instance, the first movement of (an execution of) a symphony is a temporal part of it. On the other side, the play performed by the left side of the orchestra is a spatial part. In both cases, these parts are occurrences themselves. We assume that objects cannot be parts of occurrences, but rather they participate in them. Perdurants extend in time by accumulating different temporal parts, so that, at any time they are present, they are only partially present, in the sense that some of their proper temporal parts (e.g., their previous or future phases) may

193

be not present. E.g., the piece of paper you are reading now is wholly present, while some temporal parts of your reading are not present any more. Philosophers say that endurants are entities that are in time, while lacking however temporal parts (so to speak, all their parts flow with them in time). Perdurants, on the other hand, are entities that happen in time, and can have temporal parts (all their parts are fixed in time)."))

(DEFCONCEPT EVENT (?SELF) :=> (PERDURANT ?SELF) :AXIOMS (DOCUMENTATION EVENT "An occurrence-type is stative or eventive according to whether it holds of the mereological sum of two of its instances, i.e. if it is cumulative or not. A sitting occurrence is stative since the sum of two sittings is still a sitting occurrence."))

(DEFCONCEPT STATIVE (?SELF) :=> (PERDURANT ?SELF) :AXIOMS (DOCUMENTATION STATIVE "An occurrence-type is stative or eventive according to whether it holds of the mereological sum of two of its instances, i.e. if it is cumulative or not. A sitting occurrence is stative since the sum of two sittings is still a sitting occurrence."))

(DEFCONCEPT STATE (?SELF) :=> (STATIVE ?SELF) :AXIOMS (DOCUMENTATION STATE "Within stative occurrences, we distinguish between states and processes according to homeomericity: sitting is classified as a state but running is classified as a process, since there are (very short) temporal parts of a running that are not themselves runnings."))

(DEFCONCEPT PROCESS (?SELF) :=> (STATIVE ?SELF) :AXIOMS (DOCUMENTATION PROCESS "Within stative occurrences, we distinguish between states and processes according to homeomericity: sitting is classified as a state but running is classified as a process, since there are (very short) temporal parts of a running that are not themselves runnings."))

(DEFCONCEPT ACHIEVEMENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (DOCUMENTATION ACHIEVEMENT "Eventive occurrences (events) are called achievements if they are atomic, otherwise they are accomplishments."))

(DEFCONCEPT ACCOMPLISHMENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (DOCUMENTATION ACCOMPLISHMENT "An Occurrence that contains its result as a boundary. It does include aborted, suspended, misperformed accomplishments, and does NOT include processes that have a result that wasn’t intended as their achievement. This disclaimer leads to the conclusion that the accomplishment/process distinction is dependent on intentionality. (Cf. The F-Perdurant plugin to DOLCE). Eventive occurrences (events) are called achievements if they are atomic, otherwise they are accomplishments."))

194

(DEFCONCEPT FACT (?SELF) :=> (ABSTRACT ?SELF))

(DEFCONCEPT SITUATION (?SELF) :=> (ENTITY ?SELF) :AXIOMS (DOCUMENTATION SITUATION "Support for settings (situations, episodes, states of affairs). This results to be a new category in DOLCE, but it could be equivalently modelled as a special complex perdurant defined through its relations to qualities, regions, and endurants. In fact, a perdurant should be the only mandatory component of a setting. See also documentation for ’S-Description’. As a disjoint category, a situation is generically dependent on a description made by some agent. Two descriptions of a same situation are possible, otherwise we would result in a solipsistic ontology. A situation has a unity criterion -the intentionality of the describing agent- and is (pseudo-) extensional, since its constituents are invariant to a description. The difference with physical endurants is extensionality; in fact, the unity criterion for situations creates a view on the constituents of a situation, but if a situation looses a constituent, it is no more the same situation. This double dependence (on constituents and on descriptions) is characteristic of an ’interactionist’ assumption: (pseudo-) extensionally speaking, the reality is always the same, but a particular cut is given on it by an observer -but not necessarily a ’unique’ cut. Consequently, situation is a *generically constantly dependent* property, but a *specifically constantly constituted* property. Notice that these metaproperties are compatible with a special kind of perdurant as well as of endurant, but not with a special kind of region."))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF ENDURANT PERDURANT QUALITY REGION SITUATION)))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF NON-PHYSICAL-ENDURANT PHYSICAL-ENDURANT ARBITRARY-SUM)))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF PHYSICAL-OBJECT FEATURE AMOUNT-OF-MATTER)))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF AGENTIVE-PHYSICAL-OBJECT NON-AGENTIVE-PHYSICAL-OBJECT)))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF ABSTRACT-QUALITY TEMPORAL-QUALITY PHYSICAL-QUALITY)))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF ABSTRACT-REGION TEMPORAL-REGION PHYSICAL-REGION)))

(ASSERT (forall (?a ?b) (=>> (TEMPORARY-PART ?a ?b) (ENDURANT ?b))))

(ASSERT (forall (?a ?b) (=>> (TEMPORARY-PART ?a ?b) (ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (TEMPORARY-PROPER-PART ?a ?b) (ENDURANT ?b))))

195

(ASSERT (forall (?a ?b) (=>> (TEMPORARY-PROPER-PART ?a ?b) (ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (TEMPORARY-COMPONENT ?a ?b) (ENDURANT ?b))))

(ASSERT (forall (?a ?b) (=>> (TEMPORARY-COMPONENT ?a ?b) (ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (INHERENT-IN ?a ?b) (ENTITY ?b))))

(ASSERT (forall (?a ?b) (=>> (INHERENT-IN ?a ?b) (QUALITY ?a))))

(ASSERT (forall (?a ?b) (=>> (T-INHERENT-IN ?a ?b) (ENTITY ?b))))

(ASSERT (forall (?a ?b) (=>> (T-INHERENT-IN ?a ?b) (QUALITY ?a))))

(ASSERT (forall (?a ?b) (=>> (Q-LOCATION ?a ?b) (REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (Q-LOCATION ?a ?b) (QUALITY ?a))))

(ASSERT (forall (?a ?b) (=>> (HAS-QUALE ?a ?b) (QUALE ?b))))

(ASSERT (forall (?a ?b) (=>> (HAS-QUALE ?a ?b) (QUALITY ?a))))

(ASSERT (forall (?a ?b) (=>> (HOST ?a ?b) (ENTITY ?b))))

(ASSERT (forall (?a ?b) (=>> (HOST ?a ?b) (FEATURE ?a))))

(ASSERT (forall (?a ?b) (=>> (PARTICIPANT ?a ?b) (ENDURANT ?b))))

(ASSERT (forall (?a ?b) (=>> (PARTICIPANT ?a ?b) (PERDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (EXACT-LOCATION ?a ?b) (REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (EXACT-LOCATION ?a ?b) (ENTITY ?a))))

196

(ASSERT (forall (?a ?b) (=>> (PHYSICAL-LOCATION ?a ?b) (PHYSICAL-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (PHYSICAL-LOCATION ?a ?b) (PHYSICAL-ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (SPATIAL-LOCATION ?a ?b) (SPACE-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (SPATIAL-LOCATION ?a ?b) (PHYSICAL-ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (P-SPATIAL-LOCATION ?a ?b) (SPACE-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (P-SPATIAL-LOCATION ?a ?b) (PERDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (TEMPORAL-LOCATION ?a ?b) (TEMPORAL-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (TEMPORAL-LOCATION ?a ?b) (PERDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (DURATION ?a ?b) (PERDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (E-TEMPORAL-LOCATION ?a ?b) (TEMPORAL-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (E-TEMPORAL-LOCATION ?a ?b) (ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (ABSTRACT-LOCATION ?a ?b) (ABSTRACT-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (ABSTRACT-LOCATION ?a ?b) (NON-PHYSICAL-ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (DEPEND-ON-SPATIAL-LOCATION ?a ?b) (SPACE-REGION ?b))))

(ASSERT (forall (?a ?b) (=>> (DEPEND-ON-SPATIAL-LOCATION ?a ?b) (NON-PHYSICAL-ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (PRESENT-AT ?a ?b) (TIME-INTERVAL ?b))))

(ASSERT (forall (?a ?b) (=>> (PRESENT-AT ?a ?b) (ENDURANT ?a))))

197

(ASSERT (forall (?a ?b) (=>> (PARTLY-COMPRESENT-WITH ?a ?b) (ENDURANT ?b))))

(ASSERT (forall (?a ?b) (=>> (PARTLY-COMPRESENT-WITH ?a ?b) (ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (Q-PRESENT-AT ?a ?b) (TIME-INTERVAL ?b))))

(ASSERT (forall (?a ?b) (=>> (Q-PRESENT-AT ?a ?b) (PHYSICAL-QUALITY ?a))))

(ASSERT (forall (?a ?b) (=>> (HAPPENS-AT ?a ?b) (TIME-INTERVAL ?b))))

(ASSERT (forall (?a ?b) (=>> (HAPPENS-AT ?a ?b) (PERDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (E-DEPENDS-ON ?a ?b) (ENDURANT ?b))))

(ASSERT (forall (?a ?b) (=>> (E-DEPENDS-ON ?a ?b) (ENDURANT ?a))))

(ASSERT (forall (?a ?b) (=>> (P-DEPENDS-ON ?a ?b) (PERDURANT ?b))))

(ASSERT (forall (?a ?b) (=>> (P-DEPENDS-ON ?a ?b) (PERDURANT ?a))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (PERDURANT ?a) (PARTICIPANT-IN ?self ?a))) (ENDURANT ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (PARTICIPANT-IN ?self ?b)) (ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (ENDURANT ?c) (PART ?self ?c))) (ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (ENDURANT ?d) (PART-OF ?self ?d))) (ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (ENDURANT ?e) (CONSTITUENT ?self ?e))) (ENDURANT ?self))))

198

(ASSERT (forall (?self) (<= (forall (?a) (<= (PHYSICAL-ENDURANT ?a) (PART ?self ?a))) (PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (PHYSICAL-ENDURANT ?b) (PART-OF ?self ?b))) (PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (PHYSICAL-ENDURANT ?c) (CONSTITUENT ?self ?c))) (PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (PHYSICAL-QUALITY ?d) (HAS-QUALITY ?self ?d))) (PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (exists (?e) (and (HAS-QUALITY ?self ?e) (PHYSICAL-QUALITY ?e))) (PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (NON-PHYSICAL-ENDURANT ?a) (PART ?self ?a))) (NON-PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (NON-PHYSICAL-ENDURANT ?b) (CONSTITUENT ?self ?b))) (NON-PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (ABSTRACT-QUALITY ?c) (HAS-QUALITY ?self ?c))) (NON-PHYSICAL-ENDURANT ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (INHERENT-IN ?self ?a) (ENTITY ?a))) (QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (REGION ?b) (Q-LOCATION ?self ?b))) (QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (QUALITY ?c) (HAS-QUALITY ?self ?c))) (QUALITY ?self))))

(ASSERT (forall (?self)

199

(<= (forall (?a) (<= (TEMPORAL-REGION ?a) (Q-LOCATION ?self ?a))) (TEMPORAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (TEMPORAL-QUALITY ?b) (HAS-QUALITY ?self ?b))) (TEMPORAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (PERDURANT ?c) (INHERENT-IN ?self ?c))) (TEMPORAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (exists (?d) (and (INHERENT-IN ?self ?d) (PERDURANT ?d))) (TEMPORAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (PHYSICAL-REGION ?a) (Q-LOCATION ?self ?a))) (PHYSICAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (PHYSICAL-QUALITY ?b) (HAS-QUALITY ?self ?b))) (PHYSICAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (PHYSICAL-ENDURANT ?c) (INHERENT-IN ?self ?c))) (PHYSICAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (exists (?d) (and (INHERENT-IN ?self ?d) (PHYSICAL-ENDURANT ?d))) (PHYSICAL-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (ABSTRACT-REGION ?a) (Q-LOCATION ?self ?a))) (ABSTRACT-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (ABSTRACT-QUALITY ?b) (HAS-QUALITY ?self ?b))) (ABSTRACT-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (NON-PHYSICAL-ENDURANT ?c) (INHERENT-IN ?self ?c))) (ABSTRACT-QUALITY ?self))))

(ASSERT (forall (?self) (<= (exists (?d) (and (INHERENT-IN ?self ?d)

200

(NON-PHYSICAL-ENDURANT ?d))) (ABSTRACT-QUALITY ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (REGION ?a) (PART ?self ?a))) (REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (REGION ?b) (PART-OF ?self ?b))) (REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (QUALITY ?c) (Q-LOCATION-OF ?self ?c))) (REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (TEMPORAL-REGION ?a) (PART ?self ?a))) (TEMPORAL-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (TEMPORAL-QUALITY ?b) (Q-LOCATION-OF ?self ?b))) (TEMPORAL-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (PHYSICAL-REGION ?a) (PART ?self ?a))) (PHYSICAL-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (PHYSICAL-QUALITY ?b) (Q-LOCATION-OF ?self ?b))) (PHYSICAL-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (ABSTRACT-REGION ?a) (PART ?self ?a))) (ABSTRACT-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (ABSTRACT-QUALITY ?b) (Q-LOCATION-OF ?self ?b))) (ABSTRACT-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (SPACE-REGION ?a) (PART ?self ?a))) (SPACE-REGION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (SPATIAL-LOCATION-Q ?b) (Q-LOCATION-OF ?self ?b))) (SPACE-REGION ?self))))

201

(ASSERT (forall (?self) (<= (exists (?a) (and (PARTICIPANT ?self ?a) (ENDURANT ?a))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (and (HAS-QUALITY ?self ?b) (TEMPORAL-LOCATION-Q ?b))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (ENDURANT ?c) (PARTICIPANT ?self ?c))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (TEMPORAL-QUALITY ?d) (HAS-QUALITY ?self ?d))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (PERDURANT ?e) (PART ?self ?e))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?f) (<= (PERDURANT ?f) (PART-OF ?self ?f))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?g) (<= (PERDURANT ?g) (CONSTITUENT ?self ?g))) (PERDURANT ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (not (HAS-QUALITY ?self ?a)) TRUE)) (ABSTRACT ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (HOST ?self ?a)) (FEATURE ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS" :INCLUDES ("DOLCE") :SHADOW (DESCRIPTION METHOD))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS")

(DEFCONCEPT DESCRIPTION (?SELF) :=> (NON-PHYSICAL-ENDURANT ?SELF) :AXIOMS (AND (DOCUMENTATION DESCRIPTION

202

"A non-physical endurant, generically dependent on some communication act (and indirectly on some agentive physical object participating in that act).")))

(DEFCONCEPT METHOD (?SELF) :=> (S-DESCRIPTION ?SELF))

(DEFCONCEPT S-DESCRIPTION (?SELF) :=> (DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION S-DESCRIPTION "A situation can be modelled as: - a [complex] perdurant - a perdurant token - a description (proposition) - a new compound category (?fact). As a perdurant, it seems quite natural, but, is ’Brutus stabbed Caesar’ an instance of a perdurant? In a sense yes, but if we want to talk of the veridicity of it? Truth values are attached to propositions, not to instances of concepts ... But if we classify a proposition or fact as a description concerning a perdurant ... Then we could have situation-descriptions (propositions), and situation-perdurants (facts), and propositions can be true (adequate, used, accepted, adopted, executed) of corresponding facts. Do we need a new category that contains facts, or the existence of descriptions referencing interrelated perdurants, endurants, qualities and regions is sufficient to account for facts? In a minimal solution, a concept named ’s-description’ is created, with the intended meaning of a description that encompasses (kind of ’references’) at least one perdurant with at least one endurant with at least one quality and region. This also entails that *all* contexts depend on descriptions, since the entities in a a situation are modelled only because a description encompasses them (see documentation about situations). It is still possible to incorporate a new hybrid category called Situation (or State-of-Affairs or Episode), automatically generated by constructing the dependency graph that focuses on an S-Description and may even result from the transitive closure of the encompasses, participant, and inherence relationships. BTW, this hybrid category, although easily constructable as a Universal, has a still unclear ontological status as a particular. Is it a 4D or 3.5D entity? A tentative preliminary such category is introduced in the file: Situations.lisp."))

(DEFCONCEPT C-DESCRIPTION (?SELF) :=> (DESCRIPTION ?SELF))

(DEFCONCEPT FUNCTIONAL-ROLE (?SELF) :=> (C-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION FUNCTIONAL-ROLE "A description that refers to (in particular, it is ’played by’) endurants, as a component of some s-description. Functional roles are the descriptive counterpart of endurants, and, as endurants participate in perdurants, they usually have attitudes towards descriptions of perdurants. This relation is named ’modality target’, because it actually reifies at first order a typology of modal relations."))

(DEFCONCEPT COURSE (?SELF) :=> (C-DESCRIPTION ?SELF))

(DEFCONCEPT PARAMETER (?SELF)

203

:=> (C-DESCRIPTION ?SELF))

(DEFRELATION REFERENCES ((?A DESCRIPTION) (?B ENTITY)) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION REFERENCES "A relation holding between descriptions and entities whatsoever (thus including descriptions themselves). An intuition for the references relation could be that a description adds information to an entity. In fact, descriptions depend on a communication setting. In most cases, this is the characteristic relation that provides a (functional) unity criterion to objects, events, etc. For example, cars are objects and not mere aggregates because there is a project, a design, a social value, a functional structure, a personal emotional structure, etc. attached to them. This attachment can be represented by means of ’descriptions’ that ’reference’ cars. The most obvious application is for situations, which do not exist without a description, although they still are extensional entities: a situation without a part is no more the same situation, but a situation is not a mere aggregate, since it has references to a description as its unity criterion. Adding information to an entity can also be thought as an intentional solution to a holistic stance. Defenders of this view -within different frameworks- are Kant, Brentano, Husserl, Gestalt psychologists, Merleau-Ponty ... References is distinguished according to the kinds of descriptions and referenced ground entities: referencing between s-descriptions and situations is called ’SATISFIED-BY’, while referencing between s-description components and situation constituents is called ’SELECTS’. Other kinds of referencing relations can be defined, e.g. ’MODALITY-TARGET’ is bound to functional roles and courses, ’REQUISITE-FOR’ is bound to parameters and either functional roles or courses, ’REPRESENTS’ is bound to information objects and the meaning in which they are involved, ’REALIZED-BY’ is bound to information objects and physical representations that are involved in them, etc."))

(DEFRELATION REFERENCED-BY (?A ?B) :<=> (REFERENCES ?B ?A))

(DEFRELATION SATISFIED-BY (?A ?B) :<=> (AND (REFERENCES ?A ?B) (S-DESCRIPTION ?A) (SITUATION ?B)) :AXIOMS (DOCUMENTATION SATISFIED-BY "The referencing relation between s-descriptions and situations. It can be understood as a reification of the ’satisfiability’ relation of formal semantics that holds between theories and models. A theory is reified as a description, thus acquiring a life-cycle: a theory can be changed, versioned, discussed, issued, etc. ’Theory’ can be a ’potential’ theory in the sense that most conceptualizations that could be formalized, could also be reified, e.g. plans, norms, stories, projects, diagnoses, methods, etc. No position is taken on the extensionality of s-descriptions. For example, if a theory is required to be reified in fine detail, if it changes an axiom, it could be considered no more the same theory. On the other hand, if theories are reified without such a strong assumption, axioms can be changed just like non-essential parts of physical objects, with the theory preserving its identity. In case a theory is considered extensional, it might be considered a member of a class of ’theory changing history’. A model is reified as situation, thus the class of models that can satisfy a theory are reified as a situation type (class). Situations depend on s-descriptions, but not vice-versa (constructivist stance). Components of s-descriptions ’select’ constituents of situations."))

(DEFRELATION SATISFIES (?A ?B)

204

:<=> (SATISFIED-BY ?B ?A))

(DEFRELATION SELECTS (?A ?B) :<=> (AND (REFERENCES ?A ?B) (C-DESCRIPTION ?A) (OR (ENDURANT ?B) (PERDURANT ?B) (REGION ?B))) :AXIOMS (DOCUMENTATION SELECTS "The referencing relation between components of s-descriptions and constituents of situations. It can be understood as a reification of the ’satisfiability’ relation of formal semantics that holds between elements of theories and elements of models."))

(DEFRELATION SELECTED-BY (?A ?B) :<=> (SELECTS ?B ?A))

(DEFRELATION PLAYS (?A ?B) :<=> (AND (SELECTED-BY ?A ?B) (ENDURANT ?A) (FUNCTIONAL-ROLE ?B)))

(DEFRELATION PLAYED-BY (?A ?B) :<=> (PLAYS ?B ?A))

(DEFRELATION SEQUENCES (?A ?B) :<=> (AND (SELECTED-BY ?A ?B) (PERDURANT ?B) (COURSE ?A)))

(DEFRELATION SEQUENCED-BY (?A ?B) :<=> (SEQUENCES ?B ?A))

(DEFRELATION VALUE-FOR (?A ?B) :<=> (AND (SELECTED-BY ?A ?B) (REGION ?A) (PARAMETER ?B)))

(DEFRELATION VALUED-BY (?A ?B) :<=> (VALUE-FOR ?B ?A))

(DEFRELATION MODALITY-TARGET (?A ?B) :<=> (AND (REFERENCES ?A ?B) (COURSE ?A) (FUNCTIONAL-ROLE ?B)))

(DEFRELATION MODALITY-TARGET-OF (?A ?B) :<=> (MODALITY-TARGET ?B ?A))

(DEFRELATION REQUISITE-FOR (?A ?B) :<=> (AND (REFERENCES ?A ?B) (PARAMETER ?A) (OR (COURSE ?B) (FUNCTIONAL-ROLE ?B))))

(DEFRELATION HAS-REQUISITE (?A ?B) :<=> (REQUISITE-FOR ?B ?A))

(DEFRELATION FUNCTIONALLY-DEPENDS-ON (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (FUNCTIONAL-ROLE ?A) (FUNCTIONAL-ROLE ?B) (E-DEPENDS-ON ?A ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT-OF ?A ?C) (S-DESCRIPTION ?C) (TEMPORARY-COMPONENT ?C ?B)))) :AXIOMS (DOCUMENTATION FUNCTIONALLY-DEPENDS-ON "The dependence between two functional roles within the same s-description. This provides an ordering of functional roles (a ’functional structure’), whose intuition is ’superordination’."))

(DEFRELATION FUNCTIONAL-DEPEND-ON-OF (?A ?B) :<=> (FUNCTIONALLY-DEPENDS-ON ?B ?A))

(DEFRELATION PARAMETRICALLY-DEPENDS-ON (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (PARAMETER ?A) (PARAMETER ?B) (E-DEPENDS-ON ?A ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT-OF ?A ?C) (S-DESCRIPTION ?C) (TEMPORARY-COMPONENT ?C ?B)))) :AXIOMS (DOCUMENTATION PARAMETRICALLY-DEPENDS-ON "The dependence between two parameters

205

within the same s-description. This provides an ordering of parameters that helps combining regions according to a certain view."))

(DEFRELATION PARAMETRICAL-DEPEND-ON-OF (?A ?B) :<=> (PARAMETRICALLY-DEPENDS-ON ?B ?A))

(DEFRELATION ENCOMPASSES (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (S-DESCRIPTION ?A) (ENTITY ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT ?A ?C) (C-DESCRIPTION ?C) (SELECTS ?C ?B)))) :AXIOMS (DOCUMENTATION ENCOMPASSES "A double composition may be needed here for linking s-descriptions and situation components, since many possible components could be available in the setting. The first one constrains encompasses through setting components, the second one constrains encompasses through description components. On the other hand, here we only implement the second composition, since we suggest that situations emerge out of states of affairs because an s-description references it, then encompassed entities only require a relation to s-description components."))

(DEFRELATION ENCOMPASSED-BY (?A ?B) :<=> (ENCOMPASSES ?B ?A))

(DEFRELATION EXPECTS (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (S-DESCRIPTION ?A) (PERDURANT ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT ?A ?C) (COURSE ?C) (SEQUENCES ?C ?B)))))

(DEFRELATION EXPECTED-BY (?A ?B) :<=> (EXPECTS ?B ?A))

(DEFRELATION INVOLVES (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (S-DESCRIPTION ?A) (ENDURANT ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT ?A ?C) (FUNCTIONAL-ROLE ?C) (PLAYED-BY ?C ?B)))))

(DEFRELATION INVOLVED-IN (?A ?B) :<=> (INVOLVES ?B ?A))

(DEFRELATION ADMITS (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (S-DESCRIPTION ?A) (REGION ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT ?A ?C) (PARAMETER ?C) (VALUED-BY ?C ?B)))))

(DEFRELATION ADMITTED-BY (?A ?B) :<=> (ADMITS ?B ?A))

(DEFRELATION PARAMETRIZED-BY (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (PARAMETER ?B) (EXISTS (?C) (AND (EXACT-LOCATION ?A ?C) (VALUE-FOR ?C ?B)))))

(DEFRELATION PARAMETRIZES (?A ?B) :<=> (PARAMETRIZED-BY ?B ?A))

(DEFRELATION INDIRECTLY-PLAYS ((?A ENDURANT) (?B ENDURANT)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (PLAYS ?C ?D) (FUNCTIONAL-ROLE ?C) (FUNCTIONAL-ROLE ?D) (PLAYED-BY ?D ?B)))) :AXIOMS (DOCUMENTATION INDIRECTLY-PLAYS "A relation for endurants associated by means of two interplaying functional roles. For example, a device like a watch can play a non-agentive role like ’instrumentality’, but an instrumentality role could play an agentive role like ’machine’ (in a wide sense of agentivity), that is played by some agentive device."))

206

(DEFRELATION INDIRECTLY-PLAYED-BY (?A ?B) :<=> (INDIRECTLY-PLAYS ?B ?A))

(DEFRELATION REFINES ((?A S-DESCRIPTION) (?B S-DESCRIPTION)) :=> (REFERENCES ?A ?B) :AXIOMS (DOCUMENTATION REFINES "A relation between s-descriptions, representing a granularity refinement. The refined one has at least one component that is expanded in the refining one."))

(DEFRELATION REFINED-BY (?A ?B) :<=> (REFINES ?B ?A))

(DEFRELATION EXPANDS ((?A C-DESCRIPTION) (?B C-DESCRIPTION)) :=> (REFERENCES ?A ?B) :AXIOMS (DOCUMENTATION EXPANDS "A relation between c-descriptions, representing a granularity refinement. An expanded c-description does *not* imply that its s-description refines another s-description of the simple description."))

(DEFRELATION EXPANDED-BY (?A ?B) :<=> (EXPANDS ?B ?A))

(DEFRELATION SPECIALIZES ((?A DESCRIPTION) (?B DESCRIPTION)) :=> (IMMEDIATE-RELATION ?A ?B) :AXIOMS (DOCUMENTATION SPECIALIZES "A partial order relation that holds between descriptions. It supports the association between a description and another description featuring the same properties of the former, with possible additional ones."))

(DEFRELATION SPECIALIZED-BY (?A ?B) :<=> (SPECIALIZES ?B ?A))

(DEFCONCEPT INTERNAL-DESCRIPTION (?SELF) :<=> (AND (S-DESCRIPTION ?SELF) (= (CARDINALITY (SETOFALL ?A (PHYSICALLY-DEPENDS-ON ?SELF ?A))) 1)) :AXIOMS (AND (DOCUMENTATION INTERNAL-DESCRIPTION "Internal descriptions are dependent on an intentional agent.")))

(DEFCONCEPT SOCIAL-DESCRIPTION (?SELF) :<=> (AND (S-DESCRIPTION ?SELF) (>= (CARDINALITY (SETOFALL ?A (PHYSICALLY-DEPENDS-ON ?SELF ?A))) 2)) :AXIOMS (AND (DOCUMENTATION SOCIAL-DESCRIPTION "Examples of Social Descriptions are laws, norms, shares, peace treaties ecc., which are generically dependent on societies. Social descriptions are dependent on a community of agents.")))

(DEFRELATION SOCIAL-OBJECT (?SELF) :<=> (OR (SOCIAL-DESCRIPTION ?SELF) (SOCIAL-ROLE ?SELF) (SOCIAL-AGENT ?SELF)) :AXIOMS (DOCUMENTATION SOCIAL-OBJECT "A catch-all class for entities from the social world. It includes agentive and non-agentive social roles, and social descriptions."))

(DEFCONCEPT FUNCTIONALLY-VIEWED-MATTER (?SELF) :<=> (AND (AMOUNT-OF-MATTER ?SELF) (EXISTS (?A) (AND (PLAYS ?SELF ?A) (FUNCTIONAL-ROLE ?A)))))

(DEFCONCEPT AGENTIVE-FUNCTIONAL-OBJECT (?SELF) :<=> (AND (AGENTIVE-PHYSICAL-OBJECT ?SELF) (EXISTS (?A) (AND (PLAYS ?SELF ?A) (FUNCTIONAL-ROLE ?A)))))

(DEFCONCEPT NON-AGENTIVE-FUNCTIONAL-OBJECT (?SELF)

207

:<=> (AND (NON-AGENTIVE-PHYSICAL-OBJECT ?SELF) (EXISTS (?A) (AND (PLAYS ?SELF ?A) (FUNCTIONAL-ROLE ?A)))))

(DEFRELATION SETTING-FOR (?A ?B) :<=> (AND (CONSTITUENT ?A ?B) (SITUATION ?A) (OR (ENDURANT ?B) (PERDURANT ?B) (REGION ?B))))

(DEFRELATION SETTING (?A ?B) :<=> (SETTING-FOR ?B ?A))

(DEFRELATION EXPECTED-SETTING-FOR ((?A SITUATION) (?B C-DESCRIPTION)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (SATISFIES ?A ?C) (S-DESCRIPTION ?C) (TEMPORARY-COMPONENT ?C ?B)))) :AXIOMS (DOCUMENTATION EXPECTED-SETTING-FOR "A double composition is needed here for linking situations and s-descriptions components, since many possible constituents could be available in the situation."))

(DEFRELATION EXPECTED-SETTING (?A ?B) :<=> (EXPECTED-SETTING-FOR ?B ?A))

(DEFCONCEPT AGENTIVE-FUNCTIONAL-ROLE (?SELF) :=> (FUNCTIONAL-ROLE ?SELF) :AXIOMS (DOCUMENTATION AGENTIVE-FUNCTIONAL-ROLE "Agent is a role played by some object that intentionally carries out a process or event, or bears a state. By intentional agent we mean here any object oriented to achieve a given state of the world. Intentionality can be either external or internal. A cognitive agent has an explicit representation for goals, intentions, and beliefs. Intentionality and representation-explicitness are addressed by the theory of ’Modalities’ in D\&S, which is still under development and will be enhanced by ontologies of agents currently being examined. The perdurant carried out can be partly present even in absence of it or of its whole (other agents can realize it). Examples of Agentive Functional Roles are social agents like ’the president of United States’: we may think that the latter, besides depending generically on a community of US citizens, depends also generically on ’George Bush qua legal person’ (since the president can be substituted), which in turn depends specifically on ’George Bush qua human being’. Social agents are not constituted by agentive physical objects (although they depend on them), while they can constitute societies or organizations, like the Italian Government, Mercedes-Benz, etc. Agentive-functional-role is a low-level role for agentivity, meaning that it is played by physical agents or by other agentive functional roles. In this theory there is a related functional role called ’Agent-Role’ that is a generalized ’case’ role for attributing intentionality."))

(DEFCONCEPT SOCIAL-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (DOCUMENTATION SOCIAL-ROLE "A role created and maintained by a society.")))

(DEFCONCEPT SOCIAL-AGENT (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (DOCUMENTATION SOCIAL-AGENT "An agentive role created and maintained by a society.")))

(DEFCONCEPT SOCIALLY-CONSTRUCTED-PERSON (?SELF)

208

:=> (SOCIAL-AGENT ?SELF) :AXIOMS (DOCUMENTATION SOCIALLY-CONSTRUCTED-PERSON "A person which is constructed by other previously existing persons (socially constructed or born)."))

(DEFCONCEPT SOCIAL-UNIT (?SELF) :=> (SOCIAL-AGENT ?SELF))

(DEFCONCEPT NON-AGENTIVE-FUNCTIONAL-ROLE (?SELF) :=> (FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (DOCUMENTATION NON-AGENTIVE-FUNCTIONAL-ROLE " A non-agentive functional role is the specification of a function without an (internal or external) intention (e.g. ’container’, ’burnt area’, etc).")))

(DEFCONCEPT REGULATION (?SELF) :=> (S-DESCRIPTION ?SELF))

(DEFCONCEPT OBLIGATION (?SELF) :=> (S-DESCRIPTION ?SELF))

(DEFCONCEPT COMMITMENT (?SELF) :=> (OBLIGATION ?SELF))

(DEFCONCEPT SCRIPT (?SELF) :=> (S-DESCRIPTION ?SELF))

(DEFCONCEPT TECHNIQUE (?SELF) :=> (METHOD ?SELF))

(DEFCONCEPT PROJECT (?SELF) :=> (METHOD ?SELF))

(DEFCONCEPT CONTRACT (?SELF) :=> (REGULATION ?SELF))

(DEFCONCEPT NORM (?SELF) :=> (REGULATION ?SELF))

(DEFCONCEPT PROMISE (?SELF) :=> (COMMITMENT ?SELF))

(DEFCONCEPT LIFE-CYCLE (?SELF) :=> (COURSE ?SELF))

(DEFCONCEPT INDICATOR (?SELF) :=> (PARAMETER ?SELF))

(DEFRELATION REPRESENTS ((?A DESCRIPTION) (?B INFORMATION-OBJECT)) :=> (REFERENCES ?A ?B) :AXIOMS (DOCUMENTATION REPRESENTS "A relation between information objects that are used as representations (signs) and the content they represent. Information objects are ’systemic’ objects created by the system of rules of the semiotic code. For the representation between the physical implementation of information objects (physical representations) and information objects, the ’realized-by’ relation is used."))

(DEFCONCEPT INFORMATION-OBJECT (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFRELATION REPRESENTED-BY (?A ?B) :<=> (REPRESENTS ?B ?A))

(DEFRELATION REALIZED-BY ((?A INFORMATION-OBJECT) (?B PHYSICAL-ENDURANT)) :=> (AND (MEDIATED-RELATION ?A ?B)

209

(EXISTS (?C ?D) (AND (EXPRESSED-ACCORDING-TO ?A ?C) (SATISFIED-BY ?C ?D) (DESCRIPTION-SYSTEM ?C) (SETTING-FOR ?D ?B)))) :AXIOMS (DOCUMENTATION REALIZED-BY "A physical representation (p. endurant, p. perdurant, or p. quality) realizes a description according to a system of rules. This is a subrelation of ’references’ because it does not only means that a description may add information to an entity (the intended meaning of ’references’), but (differential condition) when that entity is a ’realization’ of a description, this entity is supposed to conventionally represent a position in a system of rules, allowing interpreters to perceive an expression. On the other hand, this is a subclass of references, and not a new immediate relation, because (similarity condition) a physical representation is an entity that contains additional information provided by its communication value according to a system of rules."))

(DEFRELATION REALIZES (?A ?B) :<=> (REALIZED-BY ?B ?A))

(DEFRELATION PHYSICALLY-REPRESENTS ((?A PHYSICAL-ENDURANT) (?B DESCRIPTION)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (REALIZES ?A ?C) (REPRESENTS ?C ?B)))))

(DEFRELATION PHYSICALLY-REPRESENTED-BY (?A ?B) :<=> (PHYSICALLY-REPRESENTS ?B ?A))

(DEFRELATION EXPRESSED-ACCORDING-TO ((?A INFORMATION-OBJECT) (?B DESCRIPTION-SYSTEM)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PLAYS ?A ?C) (FUNCTIONAL-ROLE ?C) (TEMPORARY-COMPONENT-OF ?C ?B)))))

(DEFCONCEPT DESCRIPTION-SYSTEM (?SELF) :=> (INFORMATION-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION DESCRIPTION-SYSTEM "These provide roles and operations to create valid information objects (e.g. grammars, codes, templates)."))

(DEFRELATION EXPRESSION-MEANS-FOR (?A ?B) :<=> (EXPRESSED-ACCORDING-TO ?B ?A))

(DEFRELATION LEXICALIZES (?A ?B) :<=> (AND (REPRESENTS ?A ?B) (TERM ?A)))

(DEFRELATION LEXICALIZED-BY (?A ?B) :<=> (LEXICALIZES ?B ?A))

(DEFRELATION Q-REPRESENTS ((?A REGION) (?B INFORMATION-OBJECT)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C ?D) (AND (EXPRESSED-ACCORDING-TO ?A ?C) (TEMPORARY-COMPONENT ?C ?D) (DESCRIPTION-SYSTEM ?C) (PARAMETER ?D) (VALUED-BY ?D ?B)))) :AXIOMS (DOCUMENTATION Q-REPRESENTS "This relation supports the representation of conceptual regions by information objects. It is defined as a composed relation: an information object is expressed according to a description system that maps a quality space. In other words, this means that a representation of conceptual regions within quality spaces requires an explicit conceptualization of the dimensions operating in the quality space. In still other words, a quality space can be mapped to a theory, which can be reified as a special

210

kind of ’Description-System’."))

(DEFRELATION Q-REPRESENTED-BY (?A ?B) :<=> (Q-REPRESENTS ?B ?A))

(DEFRELATION Q-REALIZED-BY ((?A REGION) (?B PHYSICAL-ENDURANT)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (Q-REPRESENTED-BY ?A ?C) (REALIZED-BY ?C ?B)))))

(DEFRELATION Q-REALIZES (?A ?B) :<=> (Q-REALIZED-BY ?B ?A))

(DEFRELATION METAPHORICALLY-PLAYS (?A ?B) :=> (PLAYS ?A ?B))

(DEFRELATION METAPHORICALLY-PLAYED-BY (?A ?B) :<=> (METAPHORICALLY-PLAYS ?B ?A))

(DEFCONCEPT LINGUISTIC-OBJECT (?SELF) :=> (INFORMATION-OBJECT ?SELF))

(DEFCONCEPT DIAGRAMMATIC-OBJECT (?SELF) :=> (INFORMATION-OBJECT ?SELF))

(DEFCONCEPT ICONIC-OBJECT (?SELF) :=> (INFORMATION-OBJECT ?SELF))

(DEFCONCEPT TEXT (?SELF) :=> (LINGUISTIC-OBJECT ?SELF) :AXIOMS (DOCUMENTATION TEXT "A complex linguistic object, expressed according to a language and still independent from a particular physical support."))

(DEFCONCEPT FORMAL-EXPRESSION (?SELF) :=> (LINGUISTIC-OBJECT ?SELF))

(DEFCONCEPT AXIOM (?SELF) :=> (FORMAL-EXPRESSION ?SELF))

(DEFCONCEPT PREDICATE-NAME (?SELF) :=> (FORMAL-EXPRESSION ?SELF))

(DEFCONCEPT LOGICAL-OPERATOR (?SELF) :=> (FORMAL-EXPRESSION ?SELF))

(DEFCONCEPT FORMAL-SYSTEM (?SELF) :=> (FORMAL-EXPRESSION ?SELF))

(DEFCONCEPT AXIOMATIZATION (?SELF) :=> (FORMAL-SYSTEM ?SELF))

(DEFCONCEPT DOCUMENT (?SELF) :=> (TEXT ?SELF) :AXIOMS (DOCUMENTATION DOCUMENT "A formatted text, still independent from a *physical* document."))

(DEFCONCEPT STYLESHEET (?SELF) :=> (DESCRIPTION-SYSTEM ?SELF))

(DEFCONCEPT STATEMENT (?SELF) :=> (LINGUISTIC-OBJECT ?SELF))

(DEFCONCEPT TERM (?SELF) :=> (LINGUISTIC-OBJECT ?SELF))

(DEFCONCEPT PROPER-NOUN (?SELF) :=> (LINGUISTIC-OBJECT ?SELF))

211

(DEFCONCEPT MEASUREMENT-UNIT (?SELF) :=> (INFORMATION-OBJECT ?SELF))

(DEFCONCEPT INFORMATION-COLLECTION (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (DOCUMENTATION INFORMATION-COLLECTION "An information object constituted by members of definite, complex kinds of information objects.")))

(DEFCONCEPT LITERATURE (?SELF) :=> (INFORMATION-COLLECTION ?SELF))

(DEFCONCEPT INFORMATION-DESCRIPTION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION INFORMATION-DESCRIPTION "An information description is an s-description that involves information objects. They can be divided into 1) formal descriptions, which provide roles and operations to define formal descriptions (e.g. theories), 2) description systems, which provide roles and operations to create valid information objects (e.g. grammars), and 3) classes of descriptions, which are contexts of (ev. ordered) lists of information objects, and 4) informal descriptions, which provide roles and operations to define informal descriptions (e.g. narratives)."))

(DEFCONCEPT FORMAL-DESCRIPTION (?SELF) :=> (INFORMATION-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION FORMAL-DESCRIPTION "These provide roles and operations to define formal descriptions (e.g. theories)."))

(DEFCONCEPT CLASS-OF-DESCRIPTIONS (?SELF) :=> (INFORMATION-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION CLASS-OF-DESCRIPTIONS "These provide contexts of (ev. ordered) lists of information objects, e.g terminologies, subjects, knowledge domains."))

(DEFCONCEPT INFORMAL-DESCRIPTION (?SELF) :=> (INFORMATION-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION INFORMAL-DESCRIPTION "These provide roles and operations to define informal descriptions (e.g. narratives)."))

(DEFCONCEPT THEORY (?SELF) :=> (FORMAL-DESCRIPTION ?SELF))

(DEFCONCEPT TERMINOLOGY (?SELF) :=> (CLASS-OF-DESCRIPTIONS ?SELF))

(DEFCONCEPT CLASSIFICATION (?SELF) :=> (CLASS-OF-DESCRIPTIONS ?SELF))

(DEFCONCEPT TOPIC (?SELF) :=> (CLASS-OF-DESCRIPTIONS ?SELF) :AXIOMS (DOCUMENTATION TOPIC "Any reified knowledge domain, informally referred. Intuitively, a formal description is the formal counterpart of a topic, while an informal description is its informal counterpart. Subjects or topics are often ’opaque’, meaning that no related list of information objects is provided (e.g. in flat catalogues). On the other hand, any subject, together with the contents derivable from a referred information collection, constitutes such a list."))

(DEFCONCEPT SEMIOTIC-CODE (?SELF)

212

:=> (DESCRIPTION-SYSTEM ?SELF))

(DEFCONCEPT LANGUAGE (?SELF) :=> (SEMIOTIC-CODE ?SELF))

(DEFCONCEPT GRAMMAR (?SELF) :=> (DESCRIPTION-SYSTEM ?SELF))

(DEFCONCEPT DOCUMENT-TEMPLATE (?SELF) :=> (DESCRIPTION-SYSTEM ?SELF))

(DEFCONCEPT NARRATIVE (?SELF) :=> (INFORMAL-DESCRIPTION ?SELF))

(DEFRELATION D-CONSTITUENT (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (ENDURANT ?A) (FUNCTIONAL-ROLE ?B) (EXISTS (?C) (AND (CONSTITUENT ?A ?C) (ENDURANT ?C) (PLAYS ?C ?B)))) :AXIOMS (DOCUMENTATION D-CONSTITUENT "Relation for dealing with constitution when functional roles are considered instead of physical endurants."))

(DEFRELATION D-CONSTITUENT-OF (?A ?B) :<=> (D-CONSTITUENT ?B ?A))

(DEFRELATION REGULATES (?A ?B) :<=> (AND (SATISFIED-BY ?A ?B) (REGULATION ?A)))

(DEFRELATION REGULATED-BY (?A ?B) :<=> (REGULATES ?B ?A))

(DEFRELATION CONSTRAINS (?A ?B) :<=> (AND (EXPECTS ?A ?B) (REGULATION ?A) (PERDURANT ?B)))

(DEFRELATION CONSTRAINED-BY (?A ?B) :<=> (CONSTRAINS ?B ?A))

(DEFCONCEPT CASE-SYSTEM (?SELF) :<=> (AND (S-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (CASE-ROLE ?A)))))

(DEFCONCEPT CASE-ROLE (?SELF) :=> (FUNCTIONAL-ROLE ?SELF) :AXIOMS (DOCUMENTATION CASE-ROLE "Case roles are functional roles that are constitutent of the case system of descriptions. The case system goes back at least to Aristotle’s ’aitiai’, and has been proposed in various forms by Port Royal’s grammarians and recently by Charles Fillmore, Roger Shank, Ray Jackendoff, John Sowa, etc. The case system can be used on top of functional descriptions to distinguish forms of behaviour. They can also be used to specialize the ’participation’ relation. Case roles constitute a partition. This is untenable without the notion of description, since participants can change through time: for example, an object can be an agent for part of an activity, and then become a patient. By using descriptions, we can simply state that for one part of an activity, the object *plays* the role of agent, and for another part, it plays the role of patient. The case system will be connected to rest of D\&S as soon as possible. The main issue is that the agentive/non-agentive distinction, which is ’attached’ to roles, can be overruled by a role in the case system. In other words, an ’agentive-functional-role’ can play roles other than ’agent-role’ in the case system."))

(DEFCONCEPT SUBSTRATE-ROLE (?SELF) :=> (CASE-ROLE ?SELF) :AXIOMS (DOCUMENTATION SUBSTRATE-ROLE "Substrate is a role played by some endurant that carries out a process or event, or bears a state, without doing it intentionally. Another condition is that no part of the perdurant can exist if the endurant (or its whole) playing the substrate-role does not exist. On the contrary, an agent-role provides intentionality, and the perdurant

213

carried out can be partly present even in absence of it or of its whole (other agent-roles can realize it."))

(DEFCONCEPT AGENT-ROLE (?SELF) :=> (CASE-ROLE ?SELF) :AXIOMS (DOCUMENTATION AGENT-ROLE "Agent-role is here a placeholder within the case system (cf. Fillmore, Minsky). It is used to define so-called ’functional’ participant relations, but in DAML+OIL version there is no trace of that use (due to lack of expressivity). We expect to build a linkage between the case system and the agentive/non-agentive functional roles currently defined in the theory. This is currently under investigation. The main issue is that the agentive/non-agentive distinction, which is ’attached’ to roles, can be overruled by a role in the case system. In other words, an ’agentive-functional-role’ can play roles other than ’agent-role’ in the case system."))

(DEFCONCEPT PATIENT-ROLE (?SELF) :=> (CASE-ROLE ?SELF) :AXIOMS (DOCUMENTATION PATIENT-ROLE "Patient is a role played by some endurant that participates in a perdurant without carrying it out, either without doing it intentionally but being affected by it, or by having a ’passive’ intentionality."))

(DEFCONCEPT INSTRUMENTALITY-ROLE (?SELF) :=> (CASE-ROLE ?SELF) :AXIOMS (DOCUMENTATION INSTRUMENTALITY-ROLE "Instrumentality is a role played by some endurant that participates in a perdurant. It can carry out parts of or even the whole perdurant, but only if there is something playing agent- or substrate-role that bootstraps the perdurant. It can bear only external intentionality, although there can be a compresent internal intentionality. This deals with the complexity of ’delegation’."))

(DEFCONCEPT TARGET-ROLE (?SELF) :=> (PATIENT-ROLE ?SELF) :AXIOMS (DOCUMENTATION TARGET-ROLE ""))

(DEFCONCEPT CONSEQUENCE-ROLE (?SELF) :=> (CASE-ROLE ?SELF) :AXIOMS (DOCUMENTATION CONSEQUENCE-ROLE "Consequence is a role played by some endurant that participates in a perdurant. The role-player does not carry out the perdurant, and comes into being only when the perdurant or a functional part of it (its ’prerequisite’) has been completed."))

(DEFCONCEPT DEVICE-ROLE (?SELF) :=> (AND (INSTRUMENTALITY-ROLE ?SELF) (FORALL (?A) (=> (PLAYED-BY ?SELF ?A) (PHYSICAL-OBJECT ?A)))) :AXIOMS (DOCUMENTATION DEVICE-ROLE ""))

(DEFCONCEPT RESOURCE-ROLE (?SELF) :=> (AND (INSTRUMENTALITY-ROLE ?SELF) (FORALL (?A) (=> (PLAYED-BY ?SELF ?A) (AMOUNT-OF-MATTER ?A)))) :AXIOMS (DOCUMENTATION RESOURCE-ROLE ""))

(DEFCONCEPT ARTIFACT-ROLE (?SELF) :=> (CONSEQUENCE-ROLE ?SELF) :AXIOMS (DOCUMENTATION ARTIFACT-ROLE "An artifact role is a kind of consequence role motivated by an intentional activity."))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF C-DESCRIPTION S-DESCRIPTION)))

214

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF PARAMETER FUNCTIONAL-ROLE COURSE)))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF AGENTIVE-FUNCTIONAL-ROLE NON-AGENTIVE-FUNCTIONAL-ROLE)))

(ASSERT (forall (?self) (<= (forall (?a) (<= (DESCRIPTION ?a) (TEMPORARY-PART ?self ?a))) (DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (DESCRIPTION ?b) (COMPONENT ?self ?b))) (DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (DESCRIPTION ?c) (REFERENCED-BY ?self ?c))) (DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (DESCRIPTION ?d) (SPECIALIZED-BY ?self ?d))) (DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (SITUATION ?a) (SATISFIED-BY ?self ?a))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (ENTITY ?b) (ENCOMPASSES ?self ?b))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (REGION ?c) (ADMITS ?self ?c))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (PERDURANT ?d) (EXPECTS ?self ?d))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (ENDURANT ?e) (INVOLVES ?self ?e))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?f) (<= (or (FUNCTIONAL-ROLE ?f) (COURSE ?f) (PARAMETER ?f)) (TEMPORARY-COMPONENT ?self ?f))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self)

215

(<= (exists (?g) (and (TEMPORARY-COMPONENT ?self ?g) (or (FUNCTIONAL-ROLE ?g) (COURSE ?g) (PARAMETER ?g)))) (S-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (S-DESCRIPTION ?a))) (C-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (or (ENDURANT ?b) (PERDURANT ?b) (REGION ?b)) (SELECTS ?self ?b))) (C-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (C-DESCRIPTION ?c) (EXPANDS ?self ?c))) (C-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (S-DESCRIPTION ?a))) (FUNCTIONAL-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (ENDURANT ?b) (PLAYED-BY ?self ?b))) (FUNCTIONAL-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (COURSE ?c) (MODALITY-TARGET ?self ?c))) (FUNCTIONAL-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (PARAMETER ?d) (HAS-REQUISITE ?self ?d))) (FUNCTIONAL-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (FUNCTIONAL-ROLE ?e) (EXPANDS ?self ?e))) (FUNCTIONAL-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?f) (and (GENERICALLY-DEPENDS-ON ?self ?f) (ENDURANT ?f))) (FUNCTIONAL-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (S-DESCRIPTION ?a))) (COURSE ?self))))

216

(ASSERT (forall (?self) (<= (forall (?b) (<= (PERDURANT ?b) (SEQUENCES ?self ?b))) (COURSE ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (FUNCTIONAL-ROLE ?c) (MODALITY-TARGET-OF ?self ?c))) (COURSE ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (PARAMETER ?d) (HAS-REQUISITE ?self ?d))) (COURSE ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (COURSE ?e) (EXPANDS ?self ?e))) (COURSE ?self))))

(ASSERT (forall (?self) (<= (forall (?f) (<= (COURSE ?f) (PART ?self ?f))) (COURSE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (S-DESCRIPTION ?a))) (PARAMETER ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (REGION ?b) (VALUED-BY ?self ?b))) (PARAMETER ?self))))

(ASSERT (forall (?self) (<= (exists (?c) (and (VALUED-BY ?self ?c) (REGION ?c))) (PARAMETER ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (or (FUNCTIONAL-ROLE ?d) (COURSE ?d)) (REQUISITE-FOR ?self ?d))) (PARAMETER ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (PART ?self ?a) (PROMISE ?a))) (CONTRACT ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (PLAYS ?self ?a) (SEMIOTIC-CODE ?a))) (CODE ?self))))

217

(ASSERT (forall (?self) (<= (exists (?b) (EXPRESSED-ACCORDING-TO ?self ?b)) (INFORMATION-OBJECT ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (EXPRESSED-ACCORDING-TO ?self ?a) (LANGUAGE ?a))) (TEXT ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (PART ?self ?a) (AXIOM ?a))) (AXIOMATIZATION ?self))))

(ASSERT (forall (?self) (<= (exists (?v06) (and (= (CARDINALITY (kappa (?a) (HAS-MEMBER ?self ?a))) ?v06) (>= ?v06 2))) (INFORMATION-COLLECTION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (INVOLVES ?self ?a) (INFORMATION-OBJECT ?a))) (INFORMATION-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT ?self ?a) (FORMAL-EXPRESSION ?a))) (THEORY ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (DOCUMENT ?b) (EXPRESSION-MEANS-FOR ?self ?b))) (DOCUMENT-TEMPLATE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (REPRESENTED-BY ?self ?a) (TEXT ?a))) (NARRATIVE ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (S-DESCRIPTION ?a) (SATISFIES ?self ?a))) (SITUATION ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (and (SATISFIES ?self ?b) (S-DESCRIPTION ?b))) (SITUATION ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (and (SETTING-FOR ?self ?b) (or (ENDURANT ?b) (PERDURANT ?b) (REGION ?b)))) (SITUATION ?self))))

(ASSERT (forall (?self)

218

(<= (exists (?d) (and (GENERICALLY-DEPENDS-ON ?self ?d) (S-DESCRIPTION ?d))) (SITUATION ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (SITUATION ?e) (PART ?self ?e))) (SITUATION ?self))))

(ASSERT (forall (?self) (<= (and (not (SUBSTRATE-ROLE ?self)) (not (PATIENT-ROLE ?self)) (not (INSTRUMENTALITY-ROLE ?self)) (not (CONSEQUENCE-ROLE ?self))) (AGENT-ROLE ?self))))

(ASSERT (forall (?self) (<= (and (not (SUBSTRATE-ROLE ?self)) (not (PATIENT-ROLE ?self)) (not (INSTRUMENTALITY-ROLE ?self)) (not (AGENT-ROLE ?self))) (CONSEQUENCE-ROLE ?self))))

(ASSERT (forall (?self) (<= (and (not (SUBSTRATE-ROLE ?self)) (not (PATIENT-ROLE ?self)) (not (CONSEQUENCE-ROLE ?self)) (not (AGENT-ROLE ?self))) (INSTRUMENTALITY-ROLE ?self))))

(ASSERT (forall (?self) (<= (and (not (SUBSTRATE-ROLE ?self)) (not (INSTRUMENTALITY-ROLE ?self)) (not (CONSEQUENCE-ROLE ?self)) (not (AGENT-ROLE ?self))) (PATIENT-ROLE ?self))))

(ASSERT (forall (?self) (<= (and (not (PATIENT-ROLE ?self)) (not (INSTRUMENTALITY-ROLE ?self)) (not (CONSEQUENCE-ROLE ?self)) (not (AGENT-ROLE ?self))) (SUBSTRATE-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (CASE-SYSTEM ?a))) (CASE-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (FUNCTIONALLY-DEPENDS-ON ?self ?a) (or (AGENT-ROLE ?a) (SUBSTRATE-ROLE ?a)))) (PATIENT-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (FUNCTIONALLY-DEPENDS-ON ?self ?a) (or (AGENT-ROLE ?a) (SUBSTRATE-ROLE ?a)))) (INSTRUMENTALITY-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a)

219

(and (FUNCTIONALLY-DEPENDS-ON ?self ?a) (or (AGENT-ROLE ?a) (SUBSTRATE-ROLE ?a)))) (CONSEQUENCE-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (FUNCTIONALLY-DEPENDS-ON ?self ?a) (AGENT-ROLE ?a))) (TARGET-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (FUNCTIONALLY-DEPENDS-ON ?self ?a) (AGENT-ROLE ?a))) (ARTIFACT-ROLE ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION" :INCLUDES ("DESCRIPTIONS") :SHADOW (COMMUNICATION CODE))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION")

(DEFCONCEPT COMMUNICATION (?SELF) :=> (ACCOMPLISHMENT ?SELF) :AXIOMS (DOCUMENTATION COMMUNICATION "Here communication is taken in a rather wide sense, being possible as an (intentional) activity as well as a phenomenon."))

(DEFCONCEPT SEMIOTIC-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (DOCUMENTATION SEMIOTIC-ROLE "A semiotic role is played within a communication setting by a description that participates in a communication (act). They are used to fill the universe of the so-called ’interpretation function’. Two of them are equivalent to two communication functions (message and context)."))

(DEFCONCEPT EXPRESSION (?SELF) :=> (SEMIOTIC-ROLE ?SELF) :AXIOMS (DOCUMENTATION EXPRESSION "Expressions are played by information objects and are semiotic roles. They are used to fill the first domain of the so-called ’interpretation function’. It may be equivalent to the ’message’ communication role, but since communication theory and semiotic theories are different, it is more correct to say that a message plays an expression role."))

(DEFCONCEPT S-CONTEXT (?SELF) :=> (SEMIOTIC-ROLE ?SELF) :AXIOMS (DOCUMENTATION S-CONTEXT "S-Contexts are played by S-Descriptions and are semiotic roles. They are used to fill the second domain of the so-called ’interpretation function’. It may be equivalent to the ’context’ communication role,, but since communication theory and semiotic theories are different, it is more correct to say that a c-context plays an s-context."))

(DEFCONCEPT MEANING (?SELF) :=> (SEMIOTIC-ROLE ?SELF) :AXIOMS (DOCUMENTATION MEANING "Meanings are played by descriptions whatsoever and are semiotic roles. They are used to fill the range of the so-called ’interpretation function’. It is not equivalent to any communication function.

220

Descriptions playing meaning have different natures according to the situation referenced by S-Contexts. In other words, meanings are just what ontology is supposed to explicit, thus they cannot be thematized within the same ontology that describes them (both used and mentioned)."))

(DEFRELATION INTERPRETATION (?A ?B ?C) :<=> (AND (TERNARY-CONCEPTUAL-RELATION ?A ?B ?C) (EXPRESSION ?A) (S-CONTEXT ?B) (MEANING ?C)) :AXIOMS (AND (SINGLE-VALUED INTERPRETATION) (DOCUMENTATION INTERPRETATION "The basic interpretation function of semiotics states that, given an information object and a context (either descriptive or physical - a situation), a description results. There is some inherent recursivity here, since information objects and descriptive contexts are descriptions as well. The recursion is weakened by the fact that: 1) information objects are a partition within descriptions, and are dependent on some physical entity; 2) descriptive contexts are a superclass of semiotic contexts.")))

(DEFRELATION INTERPRETANT (?A ?B) :<=> (AND (FUNCTIONAL-DEPEND-ON-OF ?A ?B) (EXISTS ?Y (AND (S-CONTEXT ?Y) (INTERPRETATION ?A ?Y ?B)))) :AXIOMS (DOCUMENTATION INTERPRETANT "A meaning is the interpretant of an expression when there is an s-context for the interpretation function of that expression. A same s-description (semiotic interpretation) is required."))

(DEFRELATION INTERPRETANT-OF (?A ?B) :<=> (INTERPRETANT ?B ?A))

(DEFCONCEPT COMMUNICATION-METHOD (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION COMMUNICATION-METHOD "Jakobson defined six functions of communication that are compatible with Shannon’s theory of information. They are the ’message’, here covered by ’Message-Role’, the context, covered here by ’C-Context’, the code, covered by ’Code’, plus ’Channel’, ’Encoder’, and ’Decoder’, which are introduced below. Message-Role, C-Context, and Code can also be viewed as playing a semiotic role (Expression, S-Context, Semiotic-Code). For a communication method, we also need other components that are not specified in Jakobson’s theory: ’Communication-Turns’ governing the sequence of a communication process, and ’Communication-Parameters’, governing the values that participants and events of a communication should have in order for the communication to be successful (i.e. for the communication method to be satisfied)."))

(DEFCONCEPT COMMUNICATION-SITUATION (?SELF) :<=> (AND (SITUATION ?SELF) (EXISTS (?A) (AND (SATISFIES ?SELF ?A) (COMMUNICATION-METHOD ?A))) (EXISTS (?B) (AND (SETTING-FOR ?SELF ?B) (INFORMATION-OBJECT ?B))) (EXISTS (?C) (AND (SETTING-FOR ?SELF ?C) (COMMUNICATION ?C))) (EXISTS (?D) (AND (SETTING-FOR ?SELF ?D) (SOCIAL-AGENT ?D)))))

(DEFCONCEPT COMMUNICATION-TURNS (?SELF) :=> (COURSE ?SELF))

(DEFCONCEPT COMMUNICATION-PARAMETER (?SELF) :=> (PARAMETER ?SELF))

(DEFCONCEPT AGENTIVE-COMMUNICATION-ROLE (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (DOCUMENTATION AGENTIVE-COMMUNICATION-ROLE "The set of agentive roles in Jakobson’s theory of communication."))

221

(DEFCONCEPT NON-AGENTIVE-COMMUNICATION-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (DOCUMENTATION NON-AGENTIVE-COMMUNICATION-ROLE "The set of non-agentive roles in Jakobson’s theory of communication."))

(DEFCONCEPT ENCODER (?SELF) :=> (AGENTIVE-COMMUNICATION-ROLE ?SELF))

(DEFCONCEPT DECODER (?SELF) :=> (AGENTIVE-COMMUNICATION-ROLE ?SELF))

(DEFCONCEPT CHANNEL-ROLE (?SELF) :=> (NON-AGENTIVE-COMMUNICATION-ROLE ?SELF))

(DEFCONCEPT MESSAGE-ROLE (?SELF) :=> (NON-AGENTIVE-COMMUNICATION-ROLE ?SELF))

(DEFCONCEPT CODE-ROLE (?SELF) :=> (NON-AGENTIVE-COMMUNICATION-ROLE ?SELF))

(DEFCONCEPT C-CONTEXT (?SELF) :=> (NON-AGENTIVE-COMMUNICATION-ROLE ?SELF))

(ASSERT (forall (?self) (<= (forall (?a) (<= (DESCRIPTION ?a) (PLAYED-BY ?self ?a))) (MEANING ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (S-DESCRIPTION ?a) (PLAYED-BY ?self ?a))) (S-CONTEXT ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (INFORMATION-OBJECT ?a) (PLAYED-BY ?self ?a))) (EXPRESSION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (PLAYS ?self ?a) (S-CONTEXT ?a))) (TOPIC ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (SEQUENCED-BY ?self ?a) (COMMUNICATION-TURNS ?a))) (COMMUNICATION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (COMMUNICATION-METHOD ?a))) (COMMUNICATION-TURNS ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT ?self ?a) (MESSAGE-ROLE ?a))) (COMMUNICATION-METHOD ?self))))

(ASSERT (forall (?self) (<= (exists (?b)

222

(and (TEMPORARY-COMPONENT ?self ?b) (CHANNEL-ROLE ?b))) (COMMUNICATION-METHOD ?self))))

(ASSERT (forall (?self) (<= (exists (?c) (and (TEMPORARY-COMPONENT ?self ?c) (CODE-ROLE ?c))) (COMMUNICATION-METHOD ?self))))

(ASSERT (forall (?self) (<= (exists (?d) (and (TEMPORARY-COMPONENT ?self ?d) (AGENTIVE-COMMUNICATION-ROLE ?d))) (COMMUNICATION-METHOD ?self))))

(ASSERT (forall (?self) (<= (exists (?e) (and (GENERICALLY-DEPENDS-ON ?self ?e) (COMMUNICATION ?e))) (DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (SOCIAL-AGENT ?a) (PLAYED-BY ?self ?a))) (AGENTIVE-COMMUNICATION-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (COMMUNICATION-METHOD ?a))) (AGENTIVE-COMMUNICATION-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT-OF ?self ?a) (COMMUNICATION-METHOD ?a))) (NON-AGENTIVE-COMMUNICATION-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (PHYSICAL-ENDURANT ?a) (PLAYED-BY ?self ?a))) (CHANNEL-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (INFORMATION-OBJECT ?a) (PLAYED-BY ?self ?a))) (MESSAGE-ROLE ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (and (PLAYS ?self ?b) (EXPRESSION ?b))) (MESSAGE-ROLE ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (S-DESCRIPTION ?a) (PLAYED-BY ?self ?a))) (C-CONTEXT ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (and (PLAYS ?self ?b) (S-CONTEXT ?b)))

223

(C-CONTEXT ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (DESCRIPTION-SYSTEM ?a) (PLAYED-BY ?self ?a))) (CODE-ROLE ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/EXTRINSIC" :INCLUDES ("DESCRIPTIONS"))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/EXTRINSIC")

(DEFRELATION NUMEROSITY (?A ?B) :=> (ENTITY-TO-CONSTANT-RELATION ?A ?B) :AXIOMS (SINGLE-VALUED NUMEROSITY))

(DEFRELATION NUMEROSITY-OF (?A ?B) :<=> (NUMEROSITY ?B ?A))

(DEFRELATION COUNTED-BY ((?A REGION) (?B NUMBER)) :=> (ENTITY-TO-CONSTANT-RELATION ?A ?B) :AXIOMS (SINGLE-VALUED COUNTED-BY))

(DEFRELATION COUNTS (?A ?B) :<=> (COUNTED-BY ?B ?A))

(DEFRELATION HAS-INFORMAL-DESCRIPTION ((?A ENTITY) (?B STRING)) :=> (ENTITY-TO-CONSTANT-RELATION ?A ?B))

(DEFRELATION INFORMAL-DESCRIPTION-OF (?A ?B) :<=> (HAS-INFORMAL-DESCRIPTION ?B ?A))

(DEFRELATION TITLE ((?A INFORMATION-OBJECT) (?B STRING)) :=> (ENTITY-TO-CONSTANT-RELATION ?A ?B))

(DEFRELATION TITLE-OF (?A ?B) :<=> (TITLE ?B ?A))

(DEFRELATION UNIT (?A ?B))

(DEFRELATION UNIT-OF (?A ?B) :<=> (UNIT ?B ?A))

(DEFRELATION UNIVERSAL-TIME ((?A TEMPORAL-REGION) (?B NUMBER)) :=> (ENTITY-TO-CONSTANT-RELATION ?A ?B))

(DEFRELATION UNIVERSAL-TIME-OF (?A ?B) :<=> (UNIVERSAL-TIME ?B ?A))

(DEFRELATION TIME-VALUE ((?A PERDURANT) (?B NUMBER)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (TEMPORAL-LOCATION ?A ?C) (UNIVERSAL-TIME ?C ?B)))))

(DEFRELATION TIME-VALUE-OF (?A ?B) :<=> (TIME-VALUE ?B ?A))

(ASSERT (forall (?a ?b) (=>> (NUMEROSITY ?a ?b) (NUMBER ?b))))

(ASSERT (forall (?a ?b) (=>> (UNIT ?a ?b) (MEASUREMENT-UNIT ?b))))

224

(ASSERT TRUE)

(DEFMODULE "TOP/DOLCE/T-TOPOLOGY" :INCLUDES ("DOLCE"))

(IN-MODULE "TOP/DOLCE/T-TOPOLOGY")

(DEFRELATION MEREOTOPOLOGICAL-ASSOCIATION (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (ENTITY ?A) (ENTITY ?B) (OR (PART ?A ?B) (PROPER-PART ?A ?B) (PART ?B ?A) (PROPER-PART ?B ?A) (OVERLAPS ?A ?B) (STRONG-CONNECTION ?A ?B) (WEAK-CONNECTION ?A ?B) (DIRECT-SUCCESSOR ?A ?B) (DIRECT-SUCCESSOR ?B ?A))) :AXIOMS (SYMMETRIC MEREOTOPOLOGICAL-ASSOCIATION))

(DEFRELATION TEMPORAL-RELATION ((?A PERDURANT) (?B PERDURANT)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C ?D) (AND (TEMPORAL-LOCATION ?A ?C) (MEREOTOPOLOGICAL-ASSOCIATION ?C ?D) (TEMPORAL-REGION ?C) (TEMPORAL-REGION ?D) (TEMPORAL-LOCATION-OF ?D ?B)))) :AXIOMS (SYMMETRIC TEMPORAL-RELATION))

(DEFRELATION TEMPORAL-CONNECTION (?A ?B) :<=> (AND (TEMPORAL-RELATION ?A ?B) (EXISTS (?C ?D) (AND (TEMPORAL-LOCATION ?A ?C) (WEAK-CONNECTION ?C ?D) (TEMPORAL-REGION ?C) (TEMPORAL-REGION ?D) (TEMPORAL-LOCATION-OF ?D ?B)))) :AXIOMS (SYMMETRIC TEMPORAL-CONNECTION))

(DEFRELATION TEMPORALLY-CONTAINS (?A ?B) :<=> (AND (TEMPORAL-RELATION ?A ?B) (EXISTS (?C ?D) (AND (TEMPORAL-LOCATION ?A ?C) (PROPER-PART ?C ?D) (TEMPORAL-REGION ?C) (TEMPORAL-REGION ?D) (TEMPORAL-LOCATION-OF ?D ?B)))))

(DEFRELATION TEMPORALLY-CONTAINED-IN (?A ?B) :<=> (TEMPORALLY-CONTAINS ?B ?A))

(DEFRELATION PRECEDES (?A ?B) :<=> (AND (TEMPORAL-RELATION ?A ?B) (EXISTS (?C ?D) (AND (TEMPORAL-LOCATION ?A ?C) (DIRECT-SUCCESSOR ?C ?D) (TEMPORAL-REGION ?C) (TEMPORAL-REGION ?D) (TEMPORAL-LOCATION-OF ?D ?B)))))

(DEFRELATION FOLLOWS (?A ?B) :<=> (PRECEDES ?B ?A))

(DEFRELATION CO-OCCURS (?A ?B) :<=> (AND (TEMPORAL-RELATION ?A ?B) (EXISTS (?C ?D) (AND (TEMPORAL-LOCATION ?A ?C) (IDENTITY-C ?C ?D) (TEMPORAL-REGION ?C) (TEMPORAL-REGION ?D) (TEMPORAL-LOCATION-OF ?D ?B)))) :AXIOMS (SYMMETRIC CO-OCCURS))

(DEFRELATION MEETS (?A ?B) :<=> (AND (TEMPORAL-CONNECTION ?A ?B) (PRECEDES ?A ?B)))

(DEFRELATION MET-BY (?A ?B) :<=> (MEETS ?B ?A))

225

(DEFRELATION STARTS (?A ?B) :=> (AND (TEMPORALLY-CONTAINED-IN ?A ?B) (EXISTS (?C) (AND (PRECEDES ?A ?C) (PART-OF ?C ?B)))))

(DEFRELATION STARTED-BY (?A ?B) :<=> (STARTS ?B ?A))

(DEFRELATION CONCLUDES (?A ?B) :=> (AND (TEMPORALLY-CONTAINED-IN ?A ?B) (EXISTS (?C) (AND (FOLLOWS ?A ?C) (PART-OF ?C ?B)))))

(DEFRELATION CONCLUDED-BY (?A ?B) :<=> (CONCLUDES ?B ?A))

(DEFRELATION TEMPORAL-INTERSECTION (?A ?B) :<=> (AND (TEMPORAL-RELATION ?A ?B) (EXISTS (?C ?D ?E) (AND (TEMPORAL-LOCATION ?A ?C) (OVERLAPS ?C ?D) (TEMPORAL-REGION ?C) (TEMPORAL-REGION ?D) (DIRECT-SUCCESSOR ?D ?E) (TEMPORAL-REGION ?E) (TEMPORAL-LOCATION-OF ?E ?B)))) :AXIOMS (SYMMETRIC TEMPORAL-INTERSECTION))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/MODALITIES" :INCLUDES ("DESCRIPTIONS"))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/MODALITIES")

(DEFCONCEPT MODAL-DESCRIPTION (?SELF) :<=> (AND (S-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (MODALITY-TARGET ?A ?B) (COURSE ?B))))))) :AXIOMS (AND (DOCUMENTATION MODAL-DESCRIPTION "A modal description is any part of a description that has a unity criterion consisting in the specification of a right, power, duty, etc. Notice that modal descriptions can appear in conventionalized s-descriptions as well as in idiosyncratic assessements, narratives, promises, etc.")))

(DEFCONCEPT RIGHT (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-RIGHT-ON ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT NON-RIGHT (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-NOT-RIGHT-ON ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT POWER (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-POWER-ON ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT DISABILITY (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF)

226

(EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-DISABILITY-TO ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT PRIVILEGE (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-PRIVILEGE-OF ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT DUTY (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-DUTY-OF ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT IMMUNITY (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-IMMUNITY-OF ?A ?B) (COURSE ?B))))))))

(DEFCONCEPT LIABILITY (?SELF) :<=> (AND (MODAL-DESCRIPTION ?SELF) (EXISTS (?A) (AND (TEMPORARY-COMPONENT ?SELF ?A) (AND (FUNCTIONAL-ROLE ?A) (EXISTS (?B) (AND (HAS-LIABILITY-TO ?A ?B) (COURSE ?B))))))))

(DEFRELATION LEGAL-MODALITY-TARGET (?A ?B) :=> (MODALITY-TARGET ?A ?B))

(DEFRELATION LEGAL-MODALITY-TARGET-OF (?A ?B) :<=> (LEGAL-MODALITY-TARGET ?B ?A))

(DEFRELATION HAS-POWER-ON (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION POWER-TARGET-OF (?A ?B) :<=> (HAS-POWER-ON ?B ?A))

(DEFRELATION HAS-DISABILITY-TO (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION DISABILITY-TARGET-OF (?A ?B) :<=> (HAS-DISABILITY-TO ?B ?A))

(DEFRELATION HAS-PRIVILEGE-OF (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION PRIVILEGE-TARGET-OF (?A ?B) :<=> (HAS-PRIVILEGE-OF ?B ?A))

(DEFRELATION HAS-DUTY-OF (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION DUTY-TARGET-OF (?A ?B) :<=> (HAS-DUTY-OF ?B ?A))

(DEFRELATION HAS-RIGHT-ON (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION RIGHT-TARGET-OF (?A ?B) :<=> (HAS-RIGHT-ON ?B ?A))

227

(DEFRELATION HAS-NOT-RIGHT-ON (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION NOT-RIGHT-TARGET-OF (?A ?B) :<=> (HAS-NOT-RIGHT-ON ?B ?A))

(DEFRELATION HAS-IMMUNITY-OF (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION IMMUNITY-TARGET-OF (?A ?B) :<=> (HAS-IMMUNITY-OF ?B ?A))

(DEFRELATION HAS-LIABILITY-TO (?A ?B) :=> (LEGAL-MODALITY-TARGET ?A ?B))

(DEFRELATION LIABILITY-TARGET-OF (?A ?B) :<=> (HAS-LIABILITY-TO ?B ?A))

(DEFRELATION HAS-BDI-ON (?A ?B) :=> (MODALITY-TARGET ?A ?B))

(DEFRELATION BDI-TARGET-OF (?A ?B) :<=> (HAS-BDI-ON ?B ?A))

(DEFRELATION SUBJECTED-TO (?A ?B) :=> (MODALITY-TARGET ?A ?B))

(DEFRELATION SUBJECT-TARGET-OF (?A ?B) :<=> (SUBJECTED-TO ?B ?A))

(DEFRELATION HAS-EXPLOITATION-WITHIN (?A ?B) :=> (MODALITY-TARGET ?A ?B))

(DEFRELATION USE-TARGET-OF (?A ?B) :<=> (HAS-EXPLOITATION-WITHIN ?B ?A))

(DEFRELATION CONSEQUENT-WITHIN (?A ?B) :=> (MODALITY-TARGET ?A ?B))

(DEFRELATION CONSEQUENCE-TARGET-OF (?A ?B) :<=> (CONSEQUENT-WITHIN ?B ?A))

(ASSERT (forall (?self) (<= (exists (?c ?d ?e) (and (TEMPORARY-PART-OF ?self ?c) (S-DESCRIPTION ?c) (TEMPORARY-COMPONENT ?self ?d) (TEMPORARY-COMPONENT ?self ?e) (FUNCTIONAL-ROLE ?d) (COURSE ?e) (MODALITY-TARGET ?d ?e))) (MODAL-DESCRIPTION ?self))))

(ASSERT (forall (?a ?b) (<= (COURSE ?b) (HAS-BDI-ON ?a ?b))))

(ASSERT (forall (?a ?b) (<= (AGENT-ROLE ?a) (HAS-BDI-ON ?a ?b))))

(ASSERT (forall (?a ?b) (<= (COURSE ?b) (SUBJECTED-TO ?a ?b))))

(ASSERT (forall (?a ?b) (<= (PATIENT-ROLE ?a)

228

(SUBJECTED-TO ?a ?b))))

(ASSERT (forall (?a ?b) (<= (COURSE ?b) (HAS-EXPLOITATION-WITHIN ?a ?b))))

(ASSERT (forall (?a ?b) (<= (INSTRUMENTALITY-ROLE ?a) (HAS-EXPLOITATION-WITHIN ?a ?b))))

(ASSERT (forall (?a ?b) (<= (COURSE ?b) (CONSEQUENT-WITHIN ?a ?b))))

(ASSERT (forall (?a ?b) (<= (CONSEQUENCE-ROLE ?a) (CONSEQUENT-WITHIN ?a ?b))))

(ASSERT (forall (?x ?y) (<= (not (HAS-DUTY-OF ?x ?y)) (HAS-PRIVILEGE-OF ?x ?y))))

(ASSERT (forall (?x ?y) (<= (not (HAS-PRIVILEGE-OF ?x ?y)) (HAS-DUTY-OF ?x ?y))))

(ASSERT (forall (?x ?y) (<= (not (HAS-LIABILITY-TO ?x ?y)) (HAS-IMMUNITY-OF ?x ?y))))

(ASSERT (forall (?x ?y) (<= (not (HAS-IMMUNITY-OF ?x ?y)) (HAS-LIABILITY-TO ?x ?y))))

(ASSERT (forall (?x ?y) (<= (not (HAS-DISABILITY-TO ?x ?y)) (HAS-POWER-ON ?x ?y))))

(ASSERT (forall (?x ?y) (<= (forall (?z) (<= (HAS-LIABILITY-TO ?z ?y) (and (MODALITY-TARGET ?z ?y) (AGENT-ROLE ?z)))) (HAS-POWER-ON ?x ?y))))

(ASSERT (forall (?x ?y) (<= (not (HAS-POWER-ON ?x ?y)) (HAS-DISABILITY-TO ?x ?y))))

(ASSERT (forall (?x ?y) (<= (forall (?z) (<= (HAS-IMMUNITY-OF ?z ?y) (and (MODALITY-TARGET ?z ?y) (AGENT-ROLE ?z)))) (HAS-DISABILITY-TO ?x ?y))))

(ASSERT (forall (?x ?y) (<= (not (HAS-NOT-RIGHT-ON ?x ?y)) (HAS-RIGHT-ON ?x ?y))))

(ASSERT (forall (?x ?y) (<= (forall (?z) (<= (HAS-DUTY-OF ?z ?y) (and (MODALITY-TARGET ?z ?y) (AGENT-ROLE ?z)))) (HAS-RIGHT-ON ?x ?y))))

(ASSERT (forall (?x ?y)

229

(<= (not (HAS-RIGHT-ON ?x ?y)) (HAS-NOT-RIGHT-ON ?x ?y))))

(ASSERT (forall (?x ?y) (<= (forall (?z ?a) (<= (HAS-PRIVILEGE-OF ?z ?y) (and (MODALITY-TARGET ?z ?y) (AGENT-ROLE ?z)))) (HAS-NOT-RIGHT-ON ?x ?y))))

(DEFMODULE "TOP/DOLCE/T-TOPOLOGY/PLACES" :INCLUDES ("T-TOPOLOGY" "DESCRIPTIONS"))

(IN-MODULE "TOP/DOLCE/T-TOPOLOGY/PLACES")

(DEFRELATION APPROXIMATE-LOCATION (?A ?B) :=> (GENERIC-LOCATION ?A ?B))

(DEFRELATION APPROXIMATE-LOCATION-OF (?A ?B) :<=> (APPROXIMATE-LOCATION ?B ?A))

(DEFRELATION PLACE (?A ?B) :<=> (AND (APPROXIMATE-LOCATION ?A ?B) (PHYSICAL-ENDURANT ?A) (PHYSICAL-ENDURANT ?B) (EXISTS (?C ?D) (AND (SPATIAL-LOCATION ?A ?C) (SPACE-REGION ?C) (MEREOTOPOLOGICAL-ASSOCIATION ?C ?D) (SPACE-REGION ?D) (SPATIAL-LOCATION-OF ?D ?B)))))

(DEFRELATION PLACE-OF (?A ?B) :<=> (PLACE ?B ?A))

(DEFRELATION SITUATION-PLACE (?A ?B) :<=> (AND (APPROXIMATE-LOCATION ?A ?B) (SETTING-FOR ?A ?B) (SITUATION ?A) (ENDURANT ?B)))

(DEFRELATION SITUATION-PLACE-OF (?A ?B) :<=> (SITUATION-PLACE ?B ?A))

(DEFRELATION MATERIAL-PLACE (?A ?B) :<=> (AND (APPROXIMATE-LOCATION ?A ?B) (ENDURANT ?A) (PHYSICAL-ENDURANT ?B) (EXISTS (?C ?D) (AND (EXACT-LOCATION ?A ?C) (SPACE-REGION ?C) (MEREOTOPOLOGICAL-ASSOCIATION ?C ?D) (SPACE-REGION ?D) (SPATIAL-LOCATION-OF ?D ?B)))))

(DEFRELATION MATERIAL-PLACE-OF (?A ?B) :<=> (MATERIAL-PLACE ?B ?A))

(DEFRELATION FIAT-PLACE (?A ?B) :<=> (AND (APPROXIMATE-LOCATION ?A ?B) (ENDURANT ?A) (NON-PHYSICAL-ENDURANT ?B) (EXISTS (?C ?D) (AND (EXACT-LOCATION ?A ?C) (SPACE-REGION ?C) (MEREOTOPOLOGICAL-ASSOCIATION ?C ?D) (SPACE-REGION ?D) (DEPEND-ON-SPATIAL-LOCATION-OF ?D ?B)))))

(DEFRELATION FIAT-PLACE-OF (?A ?B) :<=> (FIAT-PLACE ?B ?A))

(DEFRELATION GEOGRAPHIC-PART-OF (?A ?B) :<=> (AND (FIAT-PLACE ?A ?B) (POLITICAL-GEOGRAPHIC-OBJECT ?A) (POLITICAL-GEOGRAPHIC-OBJECT ?B)))

230

(DEFRELATION GEOGRAPHIC-PART (?A ?B) :<=> (GEOGRAPHIC-PART-OF ?B ?A))

(DEFRELATION PARTICIPANT-PLACE (?A ?B) :<=> (AND (GENERIC-LOCATION ?A ?B) (PERDURANT ?A) (ENDURANT ?B) (EXISTS (?C) (AND (PARTICIPANT ?A ?C) (APPROXIMATE-LOCATION ?C ?B) (ENDURANT ?C)))))

(DEFRELATION PARTICIPANT-PLACE-OF (?A ?B) :<=> (PARTICIPANT-PLACE ?B ?A))

(DEFRELATION ORIGIN (?A ?B) :=> (PLACE ?A ?B))

(DEFRELATION ORIGIN-OF (?A ?B) :<=> (ORIGIN ?B ?A))

(DEFRELATION DESCRIPTIVE-ORIGIN (?A ?B) :=> (FIAT-PLACE ?A ?B))

(DEFRELATION DESCRIPTIVE-ORIGIN-OF (?A ?B) :<=> (DESCRIPTIVE-ORIGIN ?B ?A))

(DEFCONCEPT PHYSICAL-PLACE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF))

(DEFCONCEPT GEOGRAPHICAL-OBJECT (?SELF) :=> (PHYSICAL-PLACE ?SELF))

(DEFCONCEPT NON-PHYSICAL-PLACE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT GEOGRAPHICAL-ROLE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF))

(DEFCONCEPT POLITICAL-GEOGRAPHIC-OBJECT (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF))

(DEFCONCEPT COUNTRY (?SELF) :=> (POLITICAL-GEOGRAPHIC-OBJECT ?SELF))

(ASSERT (forall (?self) (<= (exists (?a) (and (PHYSICALLY-DEPENDS-ON ?self ?a) (PHYSICAL-OBJECT ?a))) (NON-PHYSICAL-PLACE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (PHYSICALLY-DEPENDS-ON ?self ?a) (GEOGRAPHICAL-OBJECT ?a))) (POLITICAL-GEOGRAPHIC-OBJECT ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/MODALITIES/F-PARTICIPATION" :INCLUDES ("MODALITIES" "T-TOPOLOGY") :SHADOW (ACTION))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/MODALITIES/F-PARTICIPATION")

(DEFCONCEPT ACTION (?SELF) :=> (ACCOMPLISHMENT ?SELF) :AXIOMS (AND (DOCUMENTATION ACTION "A Perdurant that exemplifies the intentionality of an agent.

231

Could it be aborted, incomplete, mislead, while remaining a (potential) accomplishment? The point here is that having a result depends on a method, then an action remains an action under incomplete results. As a matter of fact, if we neutralize intentionality, a purely topological, post-hoc view is at odds with the notion of incomplete accomplishments.")))

(DEFRELATION FUNCTIONAL-PARTICIPANT (?A ?B) :<=> (AND (PARTICIPANT ?A ?B) (EXISTS (?C ?D) (AND (SEQUENCED-BY ?A ?C) (MODALITY-TARGET-OF ?C ?D) (PLAYED-BY ?D ?B)))) :AXIOMS (DOCUMENTATION FUNCTIONAL-PARTICIPANT "This relation constrains participation within the scope of an s-description: an event is participated by an object according to an s-description and its components."))

(DEFRELATION FUNCTIONAL-PARTICIPANT-IN (?A ?B) :<=> (FUNCTIONAL-PARTICIPANT ?B ?A))

(DEFRELATION PERFORMS (?A ?B) :<=> (AND (FUNCTIONAL-PARTICIPANT-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (AGENTIVE-FUNCTIONAL-ROLE ?C) (HAS-BDI-ON ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION PERFORMED-BY (?A ?B) :<=> (PERFORMS ?B ?A))

(DEFRELATION AGENT-IN (?A ?B) :<=> (PERFORMS ?A ?B))

(DEFRELATION HAS-AGENT (?A ?B) :<=> (PERFORMED-BY ?A ?B))

(DEFRELATION PRESCRIBES (?A ?B) :=> (PERFORMS ?A ?B))

(DEFRELATION PRESCRIBED-BY (?A ?B) :<=> (PRESCRIBES ?B ?A))

(DEFRELATION PATIENT-OF (?A ?B) :<=> (AND (FUNCTIONAL-PARTICIPANT-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (PATIENT-ROLE ?C) (SUBJECTED-TO ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION PATIENT (?A ?B) :<=> (PATIENT-OF ?B ?A))

(DEFRELATION TARGET-OF (?A ?B) :<=> (AND (PATIENT-OF ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (TARGET-ROLE ?C) (SUBJECTED-TO ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION HAS-TARGET (?A ?B) :<=> (TARGET-OF ?B ?A))

(DEFRELATION GENERIC-TARGET-OF (?A ?B) :<=> (AND (FUNCTIONAL-PARTICIPANT-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (TARGET-ROLE ?C) (TEMPORARY-COMPONENT-OF ?C ?D) (S-DESCRIPTION ?D) (EXPECTS ?D ?B) (ACTIVITY ?B)))))

(DEFRELATION GENERIC-TARGET (?A ?B)

232

:<=> (GENERIC-TARGET-OF ?B ?A))

(DEFRELATION THEME (?A ?B) :=> (PATIENT ?A ?B))

(DEFRELATION THEME-OF (?A ?B) :<=> (THEME ?B ?A))

(DEFRELATION USED-IN (?A ?B) :<=> (AND (FUNCTIONAL-PARTICIPANT-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (INSTRUMENTALITY-ROLE ?C) (HAS-EXPLOITATION-WITHIN ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION SITUATION-OF-USE-OF (?A ?B) :<=> (USED-IN ?B ?A))

(DEFRELATION INSTRUMENT-OF (?A ?B) :<=> (AND (USED-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (DEVICE-ROLE ?C) (HAS-EXPLOITATION-WITHIN ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION INSTRUMENT (?A ?B) :<=> (INSTRUMENT-OF ?B ?A))

(DEFRELATION RESOURCE-FOR (?A ?B) :<=> (AND (USED-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (RESOURCE-ROLE ?C) (HAS-EXPLOITATION-WITHIN ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION RESOURCE (?A ?B) :<=> (RESOURCE-FOR ?B ?A))

(DEFRELATION CONSEQUENCE-OF (?A ?B) :<=> (AND (FUNCTIONAL-PARTICIPANT-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (CONSEQUENCE-ROLE ?C) (CONSEQUENT-WITHIN ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION CONSEQUENCE (?A ?B) :<=> (CONSEQUENCE-OF ?B ?A))

(DEFRELATION PRODUCT-OF (?A ?B) :<=> (AND (FUNCTIONAL-PARTICIPANT-IN ?A ?B) (EXISTS (?C ?D) (AND (PLAYS ?A ?C) (ARTIFACT-ROLE ?C) (CONSEQUENT-WITHIN ?C ?D) (SEQUENCES ?D ?B)))))

(DEFRELATION PRODUCT (?A ?B) :<=> (CONSEQUENCE-OF ?B ?A))

(DEFRELATION SUBSTRATE-OF (?A ?B) :<=> (AND (TOTAL-PARTICIPANT-IN ?A ?B) (FUNCTIONAL-PARTICIPANT-IN ?A ?B)))

(DEFRELATION SUBSTRATE (?A ?B) :<=> (SUBSTRATE-OF ?B ?A))

(DEFRELATION HAS-STATE (?A ?B) :<=> (AND (SUBSTRATE-OF ?A ?B) (STATE ?B)))

(DEFRELATION STATE-OF (?A ?B) :<=> (HAS-STATE ?B ?A))

(DEFRELATION CO-PARTICIPATES-WITH (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PARTICIPANT-IN ?A ?C) (PARTICIPANT ?C ?B)))))

233

(DEFRELATION REFERENCE-THEME (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PERFORMS ?A ?C) (THEME ?C ?B)))))

(DEFRELATION REFERENCE-THEME-OF (?A ?B) :<=> (REFERENCE-THEME ?B ?A))

(DEFRELATION MAKES (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PERFORMS ?A ?C) (ACTIVITY ?C) (CONSEQUENCE ?C ?B)))))

(DEFRELATION MADE-BY (?A ?B) :<=> (MAKES ?B ?A))

(DEFRELATION RULES ((?A SOCIALLY-CONSTRUCTED-PERSON) (?B FUNCTIONAL-ROLE)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C ?D) (AND (PERFORMS ?A ?C) (ACTIVITY ?C) (EXPECTED-BY ?C ?D) (ACTIVITY ?C) (REGULATION ?D) (INVOLVES ?D ?B) (REGULATION ?D)))))

(DEFRELATION RULED-BY (?A ?B) :<=> (RULES ?B ?A))

(DEFRELATION RESULT-OF (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (ACTIVITY ?B) (EXISTS (?C ?D) (AND (SEQUENCED-BY ?A ?C) (T-PREDECESSOR ?C ?D) (SEQUENCES ?D ?B))) (EXISTS (?E) (AND (PARTICIPANT ?A ?E) (PARTICIPANT-IN ?E ?B) (ACTIVITY ?B))) (FOLLOWS ?A ?B)) :AXIOMS (DOCUMENTATION RESULT-OF "A perdurant p1 results from another one p2 if they are sequenced within a same course, if a same endurant participates in both perdurants, and if p1 follows p2."))

(DEFRELATION RESULT (?A ?B) :<=> (RESULT-OF ?B ?A))

(DEFRELATION USES (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (PERFORMS ?A ?C) (SITUATION-OF-USE-OF ?C ?B)))))

(DEFRELATION USED-BY (?A ?B) :<=> (USES ?B ?A))

(DEFCONCEPT ACTIVITY (?SELF) :=> (ACTION ?SELF) :AXIOMS (AND (DOCUMENTATION ACTIVITY "In dependency terms, an activity is an action that is generically constantly dependent on a conventional, shared description (course) adopted by participants. Intuitively, activities are complex actions that are at least partly conventionally planned.")))

(DEFCONCEPT PHENOMENON (?SELF) :=> (ACCOMPLISHMENT ?SELF) :AXIOMS (AND (DOCUMENTATION PHENOMENON "A phenomenon seems an accomplishment when some intentionality puts boundaries on it (although it is not claimed to be inherently intentional). On the other hand, a purely physical phenomenon does not seem to have inherent boundaries either ... and also for biological processes as well as economic processes this seems to be disputable. If the boundary hypothesis is discarded, phenomenon should migrate under process.")))

234

(DEFCONCEPT PHYSICAL-PHENOMENON (?SELF) :=> (PHENOMENON ?SELF))

(DEFCONCEPT FLUX (?SELF) :=> (PROCESS ?SELF) :AXIOMS (AND (DOCUMENTATION FLUX "Fluxes are processes that (also) contain accomplishments as constituents. In other words, fluxes emerge out of accomplishments.")))

(DEFCONCEPT RECONSTRUCTED-FLUX (?SELF) :<=> (AND (FLUX ?SELF) (FORALL (?A) (=> (HAS-MEMBER ?SELF ?A) (ACCOMPLISHMENT ?A)))) :AXIOMS (AND (DOCUMENTATION RECONSTRUCTED-FLUX "Reconstructed fluxes are fluxes that only contain accomplishments as members.")))

(DEFCONCEPT COGNITIVE-STATE (?SELF) :=> (STATE ?SELF))

(DEFCONCEPT COGNITIVE-EVENT (?SELF) :=> (EVENT ?SELF))

(ASSERT (forall (?a ?b) (=>> (THEME ?a ?b) (INFORMATION-OBJECT ?b))))

(ASSERT (forall (?self) (<= (exists (?a ?b) (and (PARTICIPANT ?self ?a) (SOCIAL-AGENT ?a) (GENERICALLY-DEPENDS-ON ?self ?b) (COGNITIVE-STATE ?b))) (ACTION ?self))))

(ASSERT (forall (?self) (<= (exists (?a ?b) (and (SEQUENCED-BY ?self ?a) (COURSE ?a) (GENERICALLY-DEPENDS-ON ?self ?b) (COURSE ?b))) (ACTIVITY ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (SUBSTRATE ?self ?a) (NATURAL-PERSON ?a))) (COGNITIVE-STATE ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (SUBSTRATE ?self ?a) (NATURAL-PERSON ?a))) (COGNITIVE-EVENT ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (CONSTITUENT ?self ?a) (ACCOMPLISHMENT ?a))) (FLUX ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS" :INCLUDES ("DOCUMENTS" "PLACES") :SHADOW (GOAL PLAN))

235

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS")

(DEFCONCEPT GOAL (?SELF) :<=> (AND (S-DESCRIPTION ?SELF) (EXISTS (?D ?A ?B) (AND (S-DESCRIPTION ?D) (PART ?D ?SELF) (TEMPORARY-COMPONENT ?SELF ?A) (TEMPORARY-COMPONENT ?SELF ?B) (AGENT-ROLE ?A) (TASK ?B) (HAS-BDI-ON ?A ?B)))) :AXIOMS (DOCUMENTATION GOAL "A goal is constructed here as a situation description that references a certain setting (a goal state). A goal has at least one agent (role) as component, and agents have a BDI on a goal task when a goal is instantiated."))

(DEFCONCEPT PLAN (?SELF) :=> (METHOD ?SELF) :AXIOMS (DOCUMENTATION PLAN "A generic plan is a method for executing or performing a procedure or a stage of a procedure. If the postcondition is a desired one, this is a goal-state and is referenced by a goal."))

(DEFCONCEPT PATH (?SELF) :=> (COURSE ?SELF))

(DEFCONCEPT TASK (?SELF) :=> (COURSE ?SELF))

(DEFCONCEPT SCHEDULE (?SELF) :<=> (AND (TASK ?SELF) (EXISTS (?A ?B) (AND (HAS-REQUISITE ?SELF ?A) (PARAMETER ?A) (VALUED-BY ?A ?B) (TIME-INTERVAL ?B)))))

(DEFCONCEPT PLAN-INFORMATION (?SELF) :<=> (AND (INFORMATION-OBJECT ?SELF) (EXISTS (?A) (AND (REPRESENTS ?SELF ?A) (PLAN ?A)))) :AXIOMS (DOCUMENTATION PLAN-INFORMATION "Documents, models, or diagrams that present the information about a plan."))

(DEFCONCEPT GOAL-STATE (?SELF) :<=> (AND (SITUATION ?SELF) (EXISTS (?A ?E ?F) (AND (SATISFIES ?SELF ?G) (GOAL ?G) (SETTING-FOR ?SELF ?E) (AGENT ?E) (SETTING-FOR ?SELF ?A) (OR (AND (PERDURANT ?A) (EXISTS (?B) (AND (RESULT-OF ?A ?B) (ACTIVITY ?B) (EXPECTED-BY ?B ?G)))) (AND (ENDURANT ?A) (EXISTS (?C) (AND (CONSEQUENCE-OF ?A ?C) (ACTIVITY ?C) (EXPECTED-BY ?C ?G)))) (AND (REGION ?A) (ADMITTED-BY ?A ?G)))))) :AXIOMS (DOCUMENTATION GOAL-STATE "A goal state is instantiated when it is referenced by a goal (description) that is adopted by some endurant playing an agent role, and executing a task from the goal description, on which it has a BDI."))

(DEFRELATION AGENT (?SELF) :<=> (AND (OR (AGENTIVE-PHYSICAL-OBJECT ?SELF) (AGENTIVE-FUNCTIONAL-ROLE ?SELF)) (EXISTS (?A ?B) (AND (PARTICIPANT-IN ?SELF ?A) (ACTIVITY ?A) (SEQUENCED-BY ?A ?B) (TASK ?B)))))

236

(DEFRELATION METHOD-OF (?A ?B) :<=> (AND (EXPECTS ?A ?B) (METHOD ?A) (ACTIVITY ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT ?A ?C) (TASK ?C) (SEQUENCES ?C ?B)))))

(DEFRELATION HAS-METHOD (?A ?B) :<=> (METHOD-OF ?B ?A))

(DEFRELATION QUANTITATIVELY-ADMITS (?A ?B) :<=> (AND (HYBRID-MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (ADMITS ?A ?C) (COUNTED-BY ?C ?B)))))

(DEFRELATION QUANTITATIVELY-ADMITTED-BY (?A ?B) :<=> (QUANTITATIVELY-ADMITS ?B ?A))

(DEFRELATION ENVISAGES (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (S-DESCRIPTION ?A) (PERDURANT ?B) (EXISTS (?C) (AND (WEAK-CONNECTION ?A ?C) (S-DESCRIPTION ?C) (EXPECTS ?C ?B)))))

(DEFRELATION ENVISAGED-BY (?A ?B) :<=> (ENVISAGES ?B ?A))

(DEFRELATION EXPLOITS (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (METHOD ?A) (ENDURANT ?B) (EXISTS (?C) (AND (METHOD-OF ?A ?C) (ACTIVITY ?C) (SITUATION-OF-USE-OF ?C ?B)))))

(DEFRELATION EXPLOITED-BY (?A ?B) :<=> (EXPLOITS ?B ?A))

(DEFRELATION SIBLING-TASK ((?A TASK) (?B TASK)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT-OF ?A ?C) (PLAN ?C) (TEMPORARY-COMPONENT ?C ?B)))) :AXIOMS (AND (SYMMETRIC SIBLING-TASK) (DOCUMENTATION SIBLING-TASK "Two tasks contained in the same plan.")))

(DEFRELATION PRECONDITION ((?A S-DESCRIPTION) (?B SITUATION)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (SATISFIED-BY ?A ?C) (SITUATION ?C) (DIRECT-PREDECESSOR ?C ?B)))) :AXIOMS (DOCUMENTATION PRECONDITION "A situation is a pre-condition of the execution of a method (and of its tasks) when it is a predecessor (however succession is interpreted, although temporal interpretation is the usual one) of that execution, and is constituted by a subset of the individuals that constitute the execution situation. For example, a surgical guideline describes how to carry out a heart transplant: its (expected) execution situation is constituted by the perdurants, endurants, and regions described by the guideline, while its pre-condition situation might be only constituted by the heart to be removed, the one to be transplanted, their anatomical and morphological environment, the physiological functions in which they participates, and some physiological values. But the devices used during the transplantation and the surgeon might (or might not) be external to the pre-condition situation. This definition does not cover the possibility of a pre-condition having constituents that are not involved in the description. This is a difficult issue. A possible solution is that such pre-conditions are actually referenced by other s-descriptions that -for instance- ’control’ the feasibility of a procedure, or

237

’analyze’ a set of events under an independent unity criterion. If this solution is applicable, such pre-conditions would be ’hybrid’ situations requiring the ’pairing’ of two or more related descriptions."))

(DEFRELATION PRECONDITION-OF (?A ?B) :<=> (PRECONDITION ?B ?A))

(DEFRELATION POSTCONDITION ((?A S-DESCRIPTION) (?B SITUATION)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (SATISFIED-BY ?A ?C) (SITUATION ?C) (DIRECT-SUCCESSOR ?C ?B)))) :AXIOMS (DOCUMENTATION POSTCONDITION "A situation is a post-condition of the execution of a method (and of its tasks) when it is a successor (however succession is interpreted, although temporal interpretation is the usual one) of that execution, and is constituted by a subset of the individuals that constitute the execution situation. For example, a surgical guideline describes how to carry out a heart transplant: its (expected) execution situation is constituted by the perdurants, endurants, and regions described by the guideline, while its post-condition situation might be only constituted by the transplanted heart, its anatomical and morphological environment, the physiological functions in which it participates, and some physiological values. But the devices used during the transplantation and the surgeon can be external to the post-condition situation. This definition does not cover the possibility of a post-condition having constituents that are not involved in the description. This is a difficult issue. A possible solution is that such post-conditions are actually referenced by other s-descriptions that -for instance- ’control’ the outcome of a procedure, or ’reconstruct’ a set of events under an independent unity criterion. If this solution is applicable, such post-conditions would be ’hybrid’ situations requiring the ’pairing’ of two or more related descriptions."))

(DEFRELATION POSTCONDITION-OF (?A ?B) :<=> (POSTCONDITION ?B ?A))

(DEFRELATION TASK-PRECONDITION ((?A TASK) (?B SITUATION)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT-OF ?A ?C) (METHOD ?C) (PRECONDITION ?C ?B)))))

(DEFRELATION TASK-PRECONDITION-OF (?A ?B) :<=> (TASK-PRECONDITION ?B ?A))

(DEFRELATION TASK-POSTCONDITION ((?A TASK) (?B SITUATION)) :<=> (AND (MEDIATED-RELATION ?A ?B) (EXISTS (?C) (AND (TEMPORARY-COMPONENT-OF ?A ?C) (METHOD ?C) (POSTCONDITION ?C ?B)))))

(DEFRELATION TASK-POSTCONDITION-OF (?A ?B) :<=> (TASK-POSTCONDITION ?B ?A))

(DEFRELATION EXIT-CONDITION (?A ?B) :=> (TASK-POSTCONDITION ?A ?B))

(DEFRELATION EXIT-CONDITION-OF (?A ?B) :<=> (EXIT-CONDITION ?B ?A))

(DEFRELATION REPETITION-INTERVAL (?A ?B) :<=> (AND (MEDIATED-RELATION ?A ?B) (TASK ?A) (TIME-INTERVAL ?B) (EXISTS (?C) (AND (HAS-REQUISITE ?A ?C) (PARAMETER ?C) (VALUED-BY ?C ?B)))))

238

(DEFRELATION REPETITION-INTERVAL-OF (?A ?B) :<=> (REPETITION-INTERVAL ?B ?A))

(DEFRELATION FIRST-TASK-OF ((?A TASK) (?B PLAN)) :<=> (AND (TEMPORARY-COMPONENT-OF ?A ?B) (NOT (EXISTS ?W (AND (TASK ?W) (TEMPORARY-COMPONENT-OF ?W ?B) (DIRECT-PREDECESSOR ?A ?W))))))

(DEFRELATION FIRST-TASK (?A ?B) :<=> (FIRST-TASK-OF ?B ?A))

(DEFRELATION LAST-TASK-OF ((?A TASK) (?B PLAN)) :<=> (AND (TEMPORARY-COMPONENT-OF ?A ?B) (NOT (EXISTS ?W (AND (TASK ?W) (TEMPORARY-COMPONENT-OF ?W ?B) (DIRECT-SUCCESSOR ?A ?W))))))

(DEFRELATION LAST-TASK (?A ?B) :<=> (LAST-TASK-OF ?B ?A))

(DEFRELATION ITERATED-FOR ((?A TASK) (?B INTEGER)) :<=> (AND (ENTITY-TO-CONSTANT-RELATION ?A ?B) (EXISTS (?C ?D) (AND (HAS-REQUISITE ?A ?C) (PARAMETER ?C) (VALUED-BY ?C ?D) (REGION ?D) (COUNTED-BY ?D ?B)))) :AXIOMS (SINGLE-VALUED ITERATED-FOR))

(DEFRELATION ITERATION-VALUE-OF (?A ?B) :<=> (ITERATED-FOR ?B ?A))

(DEFCONCEPT ELEMENTARY-TASK (?SELF) :<=> (AND (TASK ?SELF) (NOT (EXISTS (?A) (AND (TASK ?A) (COMPONENT ?SELF ?A))))) :AXIOMS (DOCUMENTATION ELEMENTARY-TASK "An atomic task."))

(DEFCONCEPT COMPLEX-TASK (?SELF) :<=> (AND (TASK ?SELF) (EXISTS (?A) (AND (TASK ?A) (COMPONENT ?SELF ?A)))))

(DEFCONCEPT SEQUENTIAL-TASK (?SELF) :<=> (AND (COMPLEX-TASK ?SELF) (NOT (EXISTS (?A) (AND (OR (BRANCHING-TASK ?A) (SYNCHRO-TASK ?A) (CYCLICAL-TASK ?A)) (COMPONENT ?SELF ?A))))) :AXIOMS (DOCUMENTATION SEQUENTIAL-TASK "A task that does not contain branchings nor synchronizations, nor cycles."))

(DEFCONCEPT SYNCHRO-TASK (?SELF) :<=> (AND (ELEMENTARY-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-PREDECESSOR ?SELF ?A))) 2)) :AXIOMS (DOCUMENTATION SYNCHRO-TASK "A task that synchronizes a set of tasks."))

(DEFCONCEPT BRANCHING-TASK (?SELF) :<=> (AND (ELEMENTARY-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 2)) :AXIOMS (DOCUMENTATION BRANCHING-TASK "A task that subdivides in a set of tasks."))

(DEFCONCEPT CASE-TASK (?SELF) :<=> (AND (BRANCHING-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 2) (FORALL (?B ?C)

239

(=> (AND (ACTIVITY ?B) (ACTIVITY ?C) (SEQUENCES ?A ?B) (SEQUENCES ?A ?C))) (PRECEDES ?B ?C))) :AXIOMS (DOCUMENTATION CASE-TASK "A task branched to a set of tasks that are not executable concurrently (at a time)."))

(DEFCONCEPT ALTERNATE-TASK (?SELF) :<=> (AND (CASE-TASK ?SELF) (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A)) 2)) :AXIOMS (DOCUMENTATION ALTERNATE-TASK "A case task branched to exactly 2 tasks not executable in parallel."))

(DEFCONCEPT CONCURRENT-TASK (?SELF) :<=> (AND (BRANCHING-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 2) (FORALL (?B ?C) (=> (AND (ACTIVITY ?B) (ACTIVITY ?C) (SEQUENCES ?A ?B) (SEQUENCES ?A ?C)) (TEMPORAL-INTERSECTION ?B ?C)))) :AXIOMS (DOCUMENTATION CONCURRENT-TASK "A branching task to a set of tasks executable concurrently."))

(DEFCONCEPT PARALLEL-TASK (?SELF) :<=> (AND (BRANCHING-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 2) (FORALL (?B ?C) (=> (AND (ACTIVITY ?B) (ACTIVITY ?C) (SEQUENCES ?A ?B) (SEQUENCES ?A ?C)) (CO-OCCURS ?B ?C)))))

(DEFCONCEPT ANY-ORDER-TASK (?SELF) :<=> (AND (BRANCHING-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 2) (FORALL (?B ?C) (=> (AND (ACTIVITY ?B) (ACTIVITY ?C) (SEQUENCES ?A ?B) (SEQUENCES ?A ?C)) (TEMPORAL-RELATION ?B ?C)))))

(DEFCONCEPT PARTLY-CONCURRENT-TASK (?SELF) :<=> (AND (BRANCHING-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 3) (FORALL (?B ?C) (=> (AND (ACTIVITY ?B) (ACTIVITY ?C) (SEQUENCES ?A ?B) (SEQUENCES ?A ?C)) (AND (TEMPORAL-INTERSECTION ?B ?C) (EXISTS (?D ?E) (AND (ACTIVITY ?D) (ACTIVITY ?E) (SEQUENCES ?A ?D) (SEQUENCES ?A ?E) (PRECEDES ?D ?E))))))) :AXIOMS (DOCUMENTATION PARTLY-CONCURRENT-TASK "A branching task to a set of tasks, some of which are executable concurrently."))

(DEFCONCEPT PARTLY-PARALLEL-TASK (?SELF) :<=> (AND (BRANCHING-TASK ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 3) (FORALL (?B ?C) (=> (AND (ACTIVITY ?B) (ACTIVITY ?C) (SEQUENCES ?A ?B) (SEQUENCES ?A ?C)) (AND (CO-OCCURS ?B ?C) (EXISTS (?D ?E) (AND (ACTIVITY ?D) (ACTIVITY ?E) (SEQUENCES ?A ?D) (SEQUENCES ?A ?E) (NOT (CO-OCCURS ?D ?E)))))))) :AXIOMS (DOCUMENTATION PARTLY-CONCURRENT-TASK "A branching task to a set of tasks, some of which are executable in parallel."))

240

(DEFCONCEPT PARTLY-ANY-ORDER-TASK (?SELF) :<=> (AND (CASE-TASK ?SELF) (NOT (ALTERNATE-TASK ?SELF))) :AXIOMS (DOCUMENTATION PARTLY-CONCURRENT-TASK "A branching task to a set of tasks, some of which are not executable concurrently."))

(DEFCONCEPT CYCLICAL-TASK (?SELF) :<=> (AND (COMPLEX-TASK ?SELF) (EXISTS (?A) (AND (COMPLEX-TASK ?A) (DIRECT-SUCCESSOR ?SELF ?A) (IDENTITY-C ?SELF ?A)))) :AXIOMS (DOCUMENTATION CYCLICAL-TASK "A cyclical task."))

(DEFCONCEPT CYCLE-FOR (?SELF) :<=> (AND (CYCLICAL-TASK ?SELF) (FORALL (?A) (=> (ITERATED-FOR ?SELF ?A) (INTEGER ?A))) (EXISTS (?A) (AND (ITERATED-FOR ?SELF ?A) (INTEGER ?A)))))

(DEFCONCEPT CYCLE-UNTIL (?SELF) :=> (CYCLICAL-TASK ?SELF) :AXIOMS (DOCUMENTATION CYCLE-UNTIL "A cyclical task, which iterates until a certain condition becomes true. It can be repeated after a certain interval."))

(DEFCONCEPT PLANNING-ACTIVITY (?SELF) :=> (ACTIVITY ?SELF))

(DEFCONCEPT INFORMATION-GATHERING (?SELF) :=> (ACTIVITY ?SELF))

(DEFCONCEPT DECISION-ACTIVITY (?SELF) :=> (PLANNING-ACTIVITY ?SELF))

(DEFCONCEPT ASSESSMENT-QUALITY (?SELF) :=> (ABSTRACT-QUALITY ?SELF))

(DEFCONCEPT PLAN-ASSESSMENT-QUALITY (?SELF) :<=> (AND (ASSESSMENT-QUALITY ?SELF) (EXISTS (?A) (AND (INHERENT-IN ?SELF ?A) (PLAN ?A)))))

(DEFCONCEPT PROCEDURAL-QUALITY (?SELF) :<=> (AND (TEMPORAL-QUALITY ?SELF) (EXISTS (?A) (AND (T-INHERENT-IN ?SELF ?A) (ACTIVITY ?A)))))

(DEFCONCEPT DIAGRAM (?SELF) :=> (DIAGRAMMATIC-OBJECT ?SELF))

(DEFCONCEPT DIAGRAM-COMPONENT (?SELF) :<=> (AND (DIAGRAMMATIC-OBJECT ?SELF) (EXISTS (?A) (AND (COMPONENT-OF ?SELF ?A) (DIAGRAM ?A)))))

(DEFCONCEPT FLOW-CHART (?SELF) :=> (DIAGRAM ?SELF))

(DEFCONCEPT FLOW-CHART-COMPONENT (?SELF) :<=> (AND (DIAGRAM-COMPONENT ?SELF) (EXISTS (?A) (AND (COMPONENT-OF ?SELF ?A) (FLOW-CHART ?A)))))

(DEFCONCEPT FLOW-CHART-NODE (?SELF) :=> (FLOW-CHART-COMPONENT ?SELF))

(DEFCONCEPT SIMPLE-NODE (?SELF) :=> (FLOW-CHART-NODE ?SELF))

(DEFCONCEPT FORK-NODE (?SELF) :<=> (AND (FLOW-CHART-NODE ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-SUCCESSOR ?SELF ?A))) 2)))

241

(DEFCONCEPT JOIN-NODE (?SELF) :<=> (AND (FLOW-CHART-NODE ?SELF) (>= (CARDINALITY (SETOFALL ?A (DIRECT-PREDECESSOR ?SELF ?A))) 2)))

(DEFCONCEPT CYCLE-NODE (?SELF) :=> (FLOW-CHART-NODE ?SELF))

(ASSERT (forall (?self) (<= (forall (?a) (<= (PHENOMENON ?a) (SEQUENCES ?self ?a))) (PATH ?self))))

(ASSERT (forall (?self) (<= (and (forall (?a) (<= (ACTIVITY ?a) (SEQUENCES ?self ?a))) (forall (?b) (<= (TASK ?b) (T-SUCCESSOR ?self ?b)))) (TASK ?self))))

(ASSERT (forall (?self) (<= (not (ELEMENTARY-TASK ?self)) (COMPLEX-TASK ?self))))

(ASSERT (forall (?self) (<= (not (COMPLEX-TASK ?self)) (ELEMENTARY-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (TASK ?b) (TEMPORARY-COMPONENT ?self ?b))) (TASK ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (TEMPORARY-COMPONENT ?self ?a) (TASK ?a))) (PLAN ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (and (TEMPORARY-COMPONENT ?self ?b) (FUNCTIONAL-ROLE ?b))) (PLAN ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (PERDURANT ?c) (ENVISAGES ?self ?c))) (PLAN ?self))))

(ASSERT (forall (?self) (<= (forall (?d) (<= (INFORMATION-OBJECT ?d) (REPRESENTED-BY ?self ?d))) (PLAN ?self))))

(ASSERT (forall (?self) (<= (exists (?b) (AUTHORED-BY ?self ?b)) (PLAN-INFORMATION ?self))))

(ASSERT (forall (?self) (<= (forall (?c)

242

(<= (STRING ?c) (TITLE ?self ?c))) (PLAN-INFORMATION ?self))))

(ASSERT (forall (?self) (<= (exists (?d) (and (PRESENT-AT ?self ?d) (TIME-INTERVAL ?d))) (PLAN-INFORMATION ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (STRING ?e) (HAS-INFORMAL-DESCRIPTION ?self ?e))) (PLAN-INFORMATION ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (PLANNING-ACTIVITY ?c) (SEQUENCES ?self ?c))) (SYNCHRO-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (PLANNING-ACTIVITY ?c) (SEQUENCES ?self ?c))) (BRANCHING-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (DECISION-ACTIVITY ?b) (SEQUENCES ?self ?b))) (CASE-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?f) (<= (ACTIVITY ?f) (SEQUENCES ?self ?f))) (CYCLICAL-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?a) (<= (TIME-INTERVAL ?a) (REPETITION-INTERVAL ?self ?a))) (CYCLE-UNTIL ?self))))

(ASSERT (forall (?self) (<= (forall (?c) (<= (TIME-INTERVAL ?c) (REPETITION-INTERVAL ?self ?c))) (CYCLE-FOR ?self))))

(ASSERT (MUTUALLY-DISJOINT-COLLECTION (SETOF CYCLE-NODE SIMPLE-NODE FORK-NODE JOIN-NODE)))

(ASSERT (forall (?self) (<= (exists (?b) (and (INDIRECT-PREDECESSOR ?self ?b) (FORK-NODE ?b))) (JOIN-NODE ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (FLOW-CHART-COMPONENT ?b) (T-SUCCESSOR ?self ?b))) (FLOW-CHART-COMPONENT ?self))))

(ASSERT (forall (?self)

243

(<= (forall (?b) (<= (JOIN-NODE ?b) (REPRESENTED-BY ?self ?b))) (SYNCHRO-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?b) (<= (FORK-NODE ?b) (REPRESENTED-BY ?self ?b))) (BRANCHING-TASK ?self))))

(ASSERT (forall (?self) (<= (forall (?e) (<= (CYCLE-NODE ?e) (REPRESENTED-BY ?self ?e))) (CYCLICAL-TASK ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS/SYSTEMS" :INCLUDES ("PLANS"))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS/SYSTEMS")

(DEFRELATION SYSTEM-AS-ARTIFACT (?SELF) :<=> (AND (NON-AGENTIVE-PHYSICAL-OBJECT ?SELF) (EXISTS (?B) (AND (INVOLVED-IN ?SELF ?B) (OR (PLAN ?B) (PROJECT ?B))))) :AXIOMS (DOCUMENTATION SYSTEM-AS-ARTIFACT "A physical object playing the role of artifact, i.e., produced through an execution of a plan that makes a project materialized. There is a inherent circularity here, since being produced implies executing a plan that contains a functional role for being an artifact. It is the primitive notion of transforming by making that is lacking, but even having that one, how to anchor it to some other notion? The only possibility seems to have descriptions for changing (evolution) scenarios, but how to distinguish between different changes, i.e. between non-artifactual and artifactual changes? Here comes the notion of ’function’: an artifactual change is one that provides a function not available before. But what is such a function? It seems the possibility (a task) for acting in some way, not previously available (plannable). Within non intentional systems, there is no difference btw functional or not (unless imposed by intentionality). But within intentional systems, what are these ways in general is not clear, since they are determined by the interaction btw intentional agents and their environments ... at the end there seems to be a hardcore constituted by agent’s euphoric/disphoric attitude, since any plan satisfaction can only be bounded to agents, and agents have no shared, pre-defined way to be satisfied. The closure of rationalism seems to rely on the standardization of satisfaction (an ontology of satisfaction? quality assessment for one’s or a standard identification life?). Making artefactuality dependent on life models is a hard choice, although practicable. Currently, we simply put an ’artifact-role’ as primitive in the ontology."))

(DEFRELATION MATERIAL-ARTIFACT (?SELF) :<=> (AND (NON-AGENTIVE-PHYSICAL-OBJECT ?SELF) (EXISTS (?B) (AND (INVOLVED-IN ?SELF ?B) (PROJECT ?B)))))

(DEFRELATION MATERIAL-REPRESENTATION-ARTIFACT (?SELF) :<=> (AND (MATERIAL-ARTIFACT ?SELF) (EXISTS (?A) (AND (REALIZES ?SELF ?A) (INFORMATION-OBJECT ?A)))))

(DEFRELATION SYSTEM-AS-DESCRIPTION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (DOCUMENTATION SYSTEM-AS-DESCRIPTION "A description of a system-as-situation.

244

This is provided for cognitive reconstructions of states of affairs: historical, ecological, environmental, sociological, economical, etc."))

(DEFRELATION SYSTEM-AS-SITUATION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (DOCUMENTATION SYSTEM-AS-SITUATION "A system with the intended meaning of a state of affairs described through appropriate intentional constraints. This is provided for some cognitive reconstructions of states of affairs that describe a ’systemic’ context: historical, ecological, environmental, sociological, economical, political, etc."))

(ASSERT (forall (?self) (<= (forall (?a) (<= (SYSTEM-AS-SITUATION ?a) (SATISFIED-BY ?self ?a))) (SYSTEM-AS-DESCRIPTION ?self))))

(ASSERT (forall (?self) (<= (exists (?a) (and (SATISFIES ?self ?a) (SYSTEM-AS-DESCRIPTION ?a))) (SYSTEM-AS-SITUATION ?self))))

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS/SYSTEMS/WNATOP" :INCLUDES ("SYSTEMS"))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS/SYSTEMS/WNATOP")

(DEFCONCEPT PHYSICAL-BODY (?SELF) :=> (NON-AGENTIVE-PHYSICAL-OBJECT ?SELF))

(DEFCONCEPT BIOLOGICAL-OBJECT (?SELF) :=> (PHYSICAL-BODY ?SELF))

(DEFCONCEPT CHEMICAL-OBJECT (?SELF) :=> (PHYSICAL-BODY ?SELF))

(DEFCONCEPT AGENTIVE-GROUP (?SELF) :=> (AGENTIVE-PHYSICAL-OBJECT ?SELF))

(DEFCONCEPT GEOGRAPHICAL-FEATURE (?SELF) :=> (FEATURE ?SELF) :AXIOMS (DOCUMENTATION GEOGRAPHICAL-FEATURE "These can be either dependent places (e.g. bays) or relevant parts (e.g. peaks). In a rigorous geological sense, I suspect that every geographical physical object is a feature. On the other hand, rivers, lakes, mountains, etc. are hardly features for common sense, then -in the spirit of DOLCE- it seems appropriate to follow the common sense in general, and reserve the feature meaning to less mundane entities and domain-oriented geological entries."))

(DEFCONCEPT AGENTIVE-TEMPORAL-ROLE (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT LEGAL-POSSESSION-ENTITY (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT CAUSAL-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT NON-AGENTIVE-TEMPORAL-ROLE (?SELF)

245

:=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT SUBSTANCE-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT COMMERCE-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT FEATURE-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT QUALITATIVE-ROLE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-ROLE ?SELF))

(DEFCONCEPT CREATIVE-OBJECT (?SELF) :=> (INFORMATION-OBJECT ?SELF))

(DEFCONCEPT I-TOPIC (?SELF) :=> (TOPIC ?SELF))

(DEFCONCEPT |WN-Subject| (?SELF) :=> (TOPIC ?SELF))

(DEFCONCEPT |WN-Word| (?SELF) :=> (TERM ?SELF))

(DEFRELATION SUBJECT (?A ?B))

(DEFRELATION SUBJECT-OF (?A ?B) :<=> (SUBJECT ?B ?A))

(DEFRELATION HAS-I-TOPIC (?A ?B))

(DEFRELATION I-TOPIC-OF (?A ?B) :<=> (HAS-I-TOPIC ?B ?A))

(DEFRELATION WORD (?A ?B))

(DEFRELATION SENSE (?A ?B) :<=> (WORD ?B ?A))

(DEFRELATION D-PART-OF (?A ?B) :=> (PART-OF ?A ?B))

(DEFRELATION D-PART (?A ?B) :<=> (D-PART-OF ?B ?A))

(ASSERT (forall (?a ?b) (<= (|WN-Subject| ?b) (SUBJECT ?a ?b))))

(ASSERT (forall (?a ?b) (<= (I-TOPIC ?b) (HAS-I-TOPIC ?a ?b))))

(ASSERT (forall (?a ?b) (<= (|WN-Word| ?b) (WORD ?a ?b))))

(ASSERT (forall (?a ?b) (<= (I-TOPIC ?b) (D-PART-OF ?a ?b))))

(ASSERT (forall (?a ?b) (<= (I-TOPIC ?a) (D-PART-OF ?a ?b))))

246

16 APPENDIX D: WORDNET-DOLCE alignment

(DEFMODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS/SYSTEMS/WNATOP/WNAT" :INCLUDES ("WNATOP") :SHADOW (SETTING ISSUE SUBSTRATE WORLD ATOM))

(IN-MODULE "TOP/DOLCE/DESCRIPTIONS/COMMUNICATION/DOCUMENTS/PLANS/SYSTEMS/WNATOP/WNAT")

(IN-DIALECT :KIF)

(DEFCONCEPT SETTING (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT SETTING LOCATIONS) (DOCUMENTATION SETTING "the physical position of something; ’he changed the setting on the thermostat’") (HAS-I-TOPIC SETTING |Factotum|) (WORD SETTING |setting|))) (DEFCONCEPT ISSUE (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ISSUE COGNITION) (DOCUMENTATION ISSUE "an important question that is in dispute and must be settled; ’the issue could be settled by requiring public education for everyone’; ’politicians never discuss the real issues’") (HAS-I-TOPIC ISSUE |Factotum|) (WORD ISSUE |issue|))) (DEFCONCEPT SUBSTRATE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SUBSTRATE SUBSTANCES) (DOCUMENTATION SUBSTRATE "the substance acted upon by an enzyme or ferment") (HAS-I-TOPIC SUBSTRATE |Chemistry|) (WORD SUBSTRATE |substrate|))) (DEFCONCEPT WORLD (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT WORLD OBJECTS) (DOCUMENTATION WORLD "a part of the earth that can be considered separately; ’the outdoor world’; ’the world of insects’") (HAS-I-TOPIC WORLD |Earth|) (WORD WORLD |world|))) (DEFCONCEPT ATOM (?SELF) :=> (CHEMICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ATOM SUBSTANCES) (DOCUMENTATION ATOM "(physics and chemistry) the smallest component of an element having the chemical properties of the element") (HAS-I-TOPIC ATOM |Chemistry|) (HAS-I-TOPIC ATOM |Physics|) (WORD ATOM |atom|))) (DEFCONCEPT ANTIQUITY_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ANTIQUITY_1 ARTIFACTS) (DOCUMENTATION ANTIQUITY_1 "an artifact surviving from the past") (HAS-I-TOPIC ANTIQUITY_1 |Archaeology|) (WORD ANTIQUITY_1 |antiquity|))) (DEFCONCEPT GRAVE$TOMB (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT GRAVE$TOMB ARTIFACTS) (DOCUMENTATION GRAVE$TOMB "a place for the burial of a corpse (especially beneath the ground and marked by a tombstone); ’he put flowers on his mother’s grave’") (HAS-I-TOPIC GRAVE$TOMB |Archaeology|) (HAS-I-TOPIC GRAVE$TOMB |Religion|) (WORD GRAVE$TOMB |grave|) (WORD GRAVE$TOMB |tomb|))) (DEFCONCEPT SUBJECT$CONTENT$DEPICTED_OBJECT (?SELF) :=> (FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT SUBJECT$CONTENT$DEPICTED_OBJECT ARTIFACTS) (DOCUMENTATION SUBJECT$CONTENT$DEPICTED_OBJECT "something (a person or object or scene) selected by an artist or photographer for graphic representation; ’a moving picture of a train is more dramatic than a still picture of the same subject’") (HAS-I-TOPIC SUBJECT$CONTENT$DEPICTED_OBJECT |Photography|) (WORD SUBJECT$CONTENT$DEPICTED_OBJECT |subject|) (WORD SUBJECT$CONTENT$DEPICTED_OBJECT |content|) (WORD SUBJECT$CONTENT$DEPICTED_OBJECT |depicted object|)))

247

(DEFCONCEPT EXPRESSIVE_STYLE$STYLE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT EXPRESSIVE_STYLE$STYLE COMMUNICATION) (DOCUMENTATION EXPRESSIVE_STYLE$STYLE "a way of expressing something (in language or art or music etc.) that is characteristic of a particular person or group of people or period; ’all the reporters were expected to adopt the style of the newspaper’") (HAS-I-TOPIC EXPRESSIVE_STYLE$STYLE |Art|) (HAS-I-TOPIC EXPRESSIVE_STYLE$STYLE |Linguistics|) (WORD EXPRESSIVE_STYLE$STYLE |expressive style|) (WORD EXPRESSIVE_STYLE$STYLE |style|))) (DEFCONCEPT SHOW_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT SHOW_2 COMMUNICATION) (DOCUMENTATION SHOW_2 "a public exhibition or entertainment; ’they wanted to see some of the shows on Broadway’") (HAS-I-TOPIC SHOW_2 |Art|) (HAS-I-TOPIC SHOW_2 |Telecommunication|) (WORD SHOW_2 |show|))) (DEFCONCEPT ART_COLLECTION (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT ART_COLLECTION GROUPS) (DOCUMENTATION ART_COLLECTION "a collection of art works") (HAS-I-TOPIC ART_COLLECTION |Art|) (WORD ART_COLLECTION |art collection|))) (DEFCONCEPT ENSEMBLE$TOUT_ENSEMBLE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT ENSEMBLE$TOUT_ENSEMBLE GROUPS) (DOCUMENTATION ENSEMBLE$TOUT_ENSEMBLE "an assemblage of parts or details (as in a work of art) considered as forming a whole") (HAS-I-TOPIC ENSEMBLE$TOUT_ENSEMBLE |Art|) (WORD ENSEMBLE$TOUT_ENSEMBLE |ensemble|) (WORD ENSEMBLE$TOUT_ENSEMBLE |tout ensemble|))) (DEFCONCEPT EXHIBITION$EXPOSITION$EXPO (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT EXHIBITION$EXPOSITION$EXPO GROUPS) (DOCUMENTATION EXHIBITION$EXPOSITION$EXPO "a collection of things (goods or works of art etc.) for public display") (HAS-I-TOPIC EXHIBITION$EXPOSITION$EXPO |Art|) (HAS-I-TOPIC EXHIBITION$EXPOSITION$EXPO |Tourism|) (WORD EXHIBITION$EXPOSITION$EXPO |exhibition|) (WORD EXHIBITION$EXPOSITION$EXPO |exposition|) (WORD EXHIBITION$EXPOSITION$EXPO |expo|))) (DEFCONCEPT REPERTOIRE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT REPERTOIRE GROUPS) (DOCUMENTATION REPERTOIRE "a collection of works that an artist or company can perform") (HAS-I-TOPIC REPERTOIRE |Art|) (WORD REPERTOIRE |repertoire|))) (DEFCONCEPT DEEP_SPACE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT DEEP_SPACE LOCATIONS) (DOCUMENTATION DEEP_SPACE "any region in space outside the solar system") (HAS-I-TOPIC DEEP_SPACE |Astrology|) (HAS-I-TOPIC DEEP_SPACE |Astronomy|) (WORD DEEP_SPACE |deep_space|))) (DEFCONCEPT INTERGALACTIC_SPACE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT INTERGALACTIC_SPACE LOCATIONS) (DOCUMENTATION INTERGALACTIC_SPACE "the space between galaxies; ’the Milky Way travels through intergalactic space’") (HAS-I-TOPIC INTERGALACTIC_SPACE |Astrology|) (HAS-I-TOPIC INTERGALACTIC_SPACE |Astronomy|) (WORD INTERGALACTIC_SPACE |intergalactic_space|))) (DEFCONCEPT INTERPLANETARY_SPACE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT INTERPLANETARY_SPACE LOCATIONS) (DOCUMENTATION INTERPLANETARY_SPACE "the part of outer space within the solar system")

248

(HAS-I-TOPIC INTERPLANETARY_SPACE |Astrology|) (HAS-I-TOPIC INTERPLANETARY_SPACE |Astronomy|) (WORD INTERPLANETARY_SPACE |interplanetary_space|))) (DEFCONCEPT INTERSTELLAR_SPACE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT INTERSTELLAR_SPACE LOCATIONS) (DOCUMENTATION INTERSTELLAR_SPACE "the space between stars") (HAS-I-TOPIC INTERSTELLAR_SPACE |Astrology|) (HAS-I-TOPIC INTERSTELLAR_SPACE |Astronomy|) (WORD INTERSTELLAR_SPACE |interstellar_space|))) (DEFCONCEPT OUTER_SPACE$SPACE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT OUTER_SPACE$SPACE LOCATIONS) (DOCUMENTATION OUTER_SPACE$SPACE "any region in space outside the Earth’s atmosphere; ’the astronauts walked in space without a tether’") (HAS-I-TOPIC OUTER_SPACE$SPACE |Astrology|) (WORD OUTER_SPACE$SPACE |outer_space|) (WORD OUTER_SPACE$SPACE |space|))) (DEFCONCEPT SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE LOCATIONS) (DOCUMENTATION SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE "one of 12 equal areas into which the zodiac is divided") (HAS-I-TOPIC SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |Astrology|) (HAS-I-TOPIC SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |Astronomy|) (WORD SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |sign_of_the_zodiac|) (WORD SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |sign|) (WORD SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |mansion|) (WORD SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |house|) (WORD SIGN_OF_THE_ZODIAC$SIGN$MANSION$HOUSE$PLANETARY_HOUSE |planetary_house|))) (DEFCONCEPT MEDIUM_6 (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT MEDIUM_6 SUBSTANCES) (DOCUMENTATION MEDIUM_6 "a liquid with which pigment is mixed by a painter") (HAS-I-TOPIC MEDIUM_6 |Painting|) (WORD MEDIUM_6 |medium|))) (DEFCONCEPT STAMP_COLLECTION (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT STAMP_COLLECTION GROUPS) (DOCUMENTATION STAMP_COLLECTION "a collection of stamps") (HAS-I-TOPIC STAMP_COLLECTION |Philately|) (WORD STAMP_COLLECTION |stamp collection|))) (DEFCONCEPT ANACHRONISM_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ANACHRONISM_1 ARTIFACTS) (DOCUMENTATION ANACHRONISM_1 "an artifact that belongs to another time") (HAS-I-TOPIC ANACHRONISM_1 |History|) (WORD ANACHRONISM_1 |anachronism|))) (DEFCONCEPT HISTORY_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT HISTORY_2 COGNITION) (DOCUMENTATION HISTORY_2 "all that is remembered of the past as preserved in writing; a body of knowledge: ’the dawn of recorded history’; ’from the beginning of history’") (HAS-I-TOPIC HISTORY_2 |History|) (HAS-I-TOPIC HISTORY_2 |Psychology|) (WORD HISTORY_2 |history|))) (DEFCONCEPT VICTORIANA (?SELF) :=> (UNITARY-COLLECTION ?SELF)

249

:AXIOMS (AND (SUBJECT VICTORIANA GROUPS) (DOCUMENTATION VICTORIANA "collection of materials of or characteristic of the Victorian era") (HAS-I-TOPIC VICTORIANA |History|) (WORD VICTORIANA |Victoriana|))) (DEFCONCEPT LANGUAGE$LINGUISTIC_COMMUNICATION (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT LANGUAGE$LINGUISTIC_COMMUNICATION COMMUNICATION) (DOCUMENTATION LANGUAGE$LINGUISTIC_COMMUNICATION "a systematic means of communicating by the use of sounds or conventional symbols; ’he taught foreign languages’; ’the language introduced is standard throughout the text’; ’the speed with which a program can be executed depends on the language in which it is written’") (HAS-I-TOPIC LANGUAGE$LINGUISTIC_COMMUNICATION |Linguistics|) (WORD LANGUAGE$LINGUISTIC_COMMUNICATION |language|) (WORD LANGUAGE$LINGUISTIC_COMMUNICATION |linguistic communication|))) (DEFCONCEPT LANGUAGE_UNIT$LINGUISTIC_UNIT (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT LANGUAGE_UNIT$LINGUISTIC_UNIT COMMUNICATION) (DOCUMENTATION LANGUAGE_UNIT$LINGUISTIC_UNIT "one of the natural units into which linguistic messages can be analyzed") (HAS-I-TOPIC LANGUAGE_UNIT$LINGUISTIC_UNIT |Linguistics|) (WORD LANGUAGE_UNIT$LINGUISTIC_UNIT |language unit|) (WORD LANGUAGE_UNIT$LINGUISTIC_UNIT |linguistic unit|))) (DEFCONCEPT PHYLUM_2 (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT PHYLUM_2 GROUPS) (DOCUMENTATION PHYLUM_2 "(linguistics) a large group of languages that are historically related") (HAS-I-TOPIC PHYLUM_2 |Linguistics|) (WORD PHYLUM_2 |phylum|))) (DEFCONCEPT SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE COGNITION) (DOCUMENTATION SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE "the grammatical arrangement of words in sentences") (HAS-I-TOPIC SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE |Grammar|) (WORD SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE |syntax|) (WORD SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE |sentence structure|) (WORD SYNTAX$SENTENCE_STRUCTURE$PHRASE_STRUCTURE |phrase structure|))) (DEFCONCEPT LEXIS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT LEXIS COGNITION) (DOCUMENTATION LEXIS "all of the words in a language; all word forms having meaning or grammatical function") (HAS-I-TOPIC LEXIS |Linguistics|) (WORD LEXIS |lexis|))) (DEFCONCEPT LINGUISTIC_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT LINGUISTIC_RELATION RELATIONS) (DOCUMENTATION LINGUISTIC_RELATION "a relation between linguistic forms or constituents") (HAS-I-TOPIC LINGUISTIC_RELATION |Linguistics|) (WORD LINGUISTIC_RELATION |linguistic_relation|))) (DEFCONCEPT PARALANGUAGE$PARALINGUISTIC_COMMUNICATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PARALANGUAGE$PARALINGUISTIC_COMMUNICATION COMMUNICATION) (DOCUMENTATION PARALANGUAGE$PARALINGUISTIC_COMMUNICATION "the use of manner of speaking to communicate particular meanings") (HAS-I-TOPIC PARALANGUAGE$PARALINGUISTIC_COMMUNICATION |Linguistics|) (HAS-I-TOPIC PARALANGUAGE$PARALINGUISTIC_COMMUNICATION |Telecommunication|) (WORD PARALANGUAGE$PARALINGUISTIC_COMMUNICATION |paralanguage|) (WORD PARALANGUAGE$PARALINGUISTIC_COMMUNICATION |paralinguistic communication|))) (DEFCONCEPT RULE$LINGUISTIC_RULE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT RULE$LINGUISTIC_RULE COMMUNICATION)

250

(DOCUMENTATION RULE$LINGUISTIC_RULE "a rule describing (or prescribing) a linguistic practice") (HAS-I-TOPIC RULE$LINGUISTIC_RULE |Linguistics|) (WORD RULE$LINGUISTIC_RULE |rule|) (WORD RULE$LINGUISTIC_RULE |linguistic rule|))) (DEFCONCEPT VOCABULARY$LEXICON$MENTAL_LEXICON (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT VOCABULARY$LEXICON$MENTAL_LEXICON COGNITION) (DOCUMENTATION VOCABULARY$LEXICON$MENTAL_LEXICON "a language user’s knowledge of words") (HAS-I-TOPIC VOCABULARY$LEXICON$MENTAL_LEXICON |Linguistics|) (WORD VOCABULARY$LEXICON$MENTAL_LEXICON |vocabulary|) (WORD VOCABULARY$LEXICON$MENTAL_LEXICON |lexicon|) (WORD VOCABULARY$LEXICON$MENTAL_LEXICON |mental lexicon|))) (DEFCONCEPT IMAGINARY_PLACE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT IMAGINARY_PLACE LOCATIONS) (DOCUMENTATION IMAGINARY_PLACE "a place said to exist in religious or fictional writings") (HAS-I-TOPIC IMAGINARY_PLACE |Literature|) (HAS-I-TOPIC IMAGINARY_PLACE |Mythology|) (WORD IMAGINARY_PLACE |imaginary_place|))) (DEFCONCEPT THEME$MOTIF (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT THEME$MOTIF COGNITION) (DOCUMENTATION THEME$MOTIF "a unifying idea that is a recurrent element in a literary or artistic work; ’it was the usual ’boy gets girl’ theme’") (HAS-I-TOPIC THEME$MOTIF |Literature|) (WORD THEME$MOTIF |theme|) (WORD THEME$MOTIF |motif|))) (DEFCONCEPT JUDAICA (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT JUDAICA GROUPS) (DOCUMENTATION JUDAICA "historical and literary materials relating to Judaism") (HAS-I-TOPIC JUDAICA |Literature|) (WORD JUDAICA |Judaica|))) (DEFCONCEPT LIBRARY_3 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT LIBRARY_3 GROUPS) (DOCUMENTATION LIBRARY_3 "a collection of literary documents or records kept for reference or borrowing") (HAS-I-TOPIC LIBRARY_3 |Literature|) (WORD LIBRARY_3 |library|))) (DEFCONCEPT ANTECEDENT_2 (?SELF) :=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ANTECEDENT_2 EVENTS) (DOCUMENTATION ANTECEDENT_2 "a preceding occurrence or cause or event") (HAS-I-TOPIC ANTECEDENT_2 |Philosophy|) (WORD ANTECEDENT_2 |antecedent|))) (DEFCONCEPT ELEMENT_4 (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT ELEMENT_4 SUBSTANCES) (DOCUMENTATION ELEMENT_4 "one of four substances thought in ancient and medieval cosmology to constitute the physical universe; ’the alchemists believed that there were four elements’") (HAS-I-TOPIC ELEMENT_4 |Philosophy|) (WORD ELEMENT_4 |element|))) (DEFCONCEPT ABSOLUTE (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ABSOLUTE COGNITION) (DOCUMENTATION ABSOLUTE "something that is conceived to be absolute; something that does not depends on anything else and is beyond human control; ’no mortal being can influence the absolute’") (HAS-I-TOPIC ABSOLUTE |Philosophy|) (WORD ABSOLUTE |absolute|))) (DEFCONCEPT LOGICAL_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT LOGICAL_RELATION RELATIONS) (DOCUMENTATION LOGICAL_RELATION "a relation between logical propositions")

251

(HAS-I-TOPIC LOGICAL_RELATION |Mathematics|) (HAS-I-TOPIC LOGICAL_RELATION |Philosophy|) (WORD LOGICAL_RELATION |logical_relation|))) (DEFCONCEPT COIN_COLLECTION_2 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT COIN_COLLECTION_2 GROUPS) (DOCUMENTATION COIN_COLLECTION_2 "a collection of coins") (HAS-I-TOPIC COIN_COLLECTION_2 |Numismatics|) (WORD COIN_COLLECTION_2 |coin collection|))) (DEFCONCEPT PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT (?SELF) :=> (COGNITIVE-EVENT ?SELF) :AXIOMS (AND (SUBJECT PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT COGNITION) (DOCUMENTATION PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT "the performance of some composite cognitive activity; an operation that affects mental contents; ’the process of thinking’; ’the act of remembering’") (HAS-I-TOPIC PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT |Psychology|) (WORD PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT |process|) (WORD PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT |cognitive process|) (WORD PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT |operation|) (WORD PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT |cognitive operation|) (WORD PROCESS$COGNITIVE_PROCESS$OPERATION$COGNITIVE_OPERATION$ACT |act|))) (DEFCONCEPT PROCESS$UNCONSCIOUS_PROCESS (?SELF) :=> (COGNITIVE-EVENT ?SELF) :AXIOMS (AND (SUBJECT PROCESS$UNCONSCIOUS_PROCESS COGNITION) (DOCUMENTATION PROCESS$UNCONSCIOUS_PROCESS "a mental process that you are not directly aware of; ’the process of denial’") (HAS-I-TOPIC PROCESS$UNCONSCIOUS_PROCESS |Psychology|) (WORD PROCESS$UNCONSCIOUS_PROCESS |process|) (WORD PROCESS$UNCONSCIOUS_PROCESS |unconscious process|))) (DEFCONCEPT BEHAVIOR$BEHAVIOUR$CONDUCT (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT BEHAVIOR$BEHAVIOUR$CONDUCT ACTS) (DOCUMENTATION BEHAVIOR$BEHAVIOUR$CONDUCT "manner of acting or conducting oneself") (HAS-I-TOPIC BEHAVIOR$BEHAVIOUR$CONDUCT |Psychology|) (WORD BEHAVIOR$BEHAVIOUR$CONDUCT |behavior|) (WORD BEHAVIOR$BEHAVIOUR$CONDUCT |behaviour|) (WORD BEHAVIOR$BEHAVIOUR$CONDUCT |conduct|))) (DEFCONCEPT BEHAVIOR$BEHAVIOUR_1 (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT BEHAVIOR$BEHAVIOUR_1 ACTS) (DOCUMENTATION BEHAVIOR$BEHAVIOUR_1 "(psychology) the aggregate of the responses or reactions or movements made by an organism in any situation") (HAS-I-TOPIC BEHAVIOR$BEHAVIOUR_1 |Psychology|) (WORD BEHAVIOR$BEHAVIOUR_1 |behavior|) (WORD BEHAVIOR$BEHAVIOUR_1 |behaviour|))) (DEFCONCEPT COGNITIVE_FACTOR (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT COGNITIVE_FACTOR COGNITION) (DOCUMENTATION COGNITIVE_FACTOR "something immaterial (as a circumstance or influence) that contributes to producing a result") (HAS-I-TOPIC COGNITIVE_FACTOR |Psychology|) (WORD COGNITIVE_FACTOR |cognitive factor|))) (DEFCONCEPT VOICE_4 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT VOICE_4 COMMUNICATION) (DOCUMENTATION VOICE_4

252

"something suggestive of speech in being a medium of expression; ’the wee small voice of conscience’; ’the voice of experience’; ’he said his voices told him to do it’") (HAS-I-TOPIC VOICE_4 |Psychology|) (WORD VOICE_4 |voice|))) (DEFCONCEPT CLIMATE$MOOD (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT CLIMATE$MOOD STATES) (DOCUMENTATION CLIMATE$MOOD "the prevailing psychological state; ’the climate of opinion’; ’the national mood had changed radically since the last election’") (HAS-I-TOPIC CLIMATE$MOOD |Psychology|) (WORD CLIMATE$MOOD |climate|) (WORD CLIMATE$MOOD |mood|))) (DEFCONCEPT ATTITUDE$MENTAL_ATTITUDE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ATTITUDE$MENTAL_ATTITUDE COGNITION) (DOCUMENTATION ATTITUDE$MENTAL_ATTITUDE "a complex mental orientation involving beliefs and feelings and values and dispositions to act in certain ways; ’he had the attitude that work was fun’") (HAS-I-TOPIC ATTITUDE$MENTAL_ATTITUDE |Psychology|) (WORD ATTITUDE$MENTAL_ATTITUDE |attitude|) (WORD ATTITUDE$MENTAL_ATTITUDE |mental attitude|))) (DEFCONCEPT CHEMISTRY$INTERPERSONAL_CHEMISTRY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CHEMISTRY$INTERPERSONAL_CHEMISTRY RELATIONS) (DOCUMENTATION CHEMISTRY$INTERPERSONAL_CHEMISTRY "the way two individuals relate to each other; ’their chemistry was wrong from the beginning -- they hated each other’") (HAS-I-TOPIC CHEMISTRY$INTERPERSONAL_CHEMISTRY |Psychology|) (WORD CHEMISTRY$INTERPERSONAL_CHEMISTRY |chemistry|) (WORD CHEMISTRY$INTERPERSONAL_CHEMISTRY |interpersonal_chemistry|))) (DEFCONCEPT MIND$HEAD$BRAIN$PSYCHE$NOUS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT MIND$HEAD$BRAIN$PSYCHE$NOUS COGNITION) (DOCUMENTATION MIND$HEAD$BRAIN$PSYCHE$NOUS "that which is responsible for one’s thoughts and feelings; the seat of the faculty of reason; ’his mind wandered’; ’I couldn’t get his words out of my head’") (HAS-I-TOPIC MIND$HEAD$BRAIN$PSYCHE$NOUS |Psychology|) (WORD MIND$HEAD$BRAIN$PSYCHE$NOUS |mind|) (WORD MIND$HEAD$BRAIN$PSYCHE$NOUS |head|) (WORD MIND$HEAD$BRAIN$PSYCHE$NOUS |brain|) (WORD MIND$HEAD$BRAIN$PSYCHE$NOUS |psyche|) (WORD MIND$HEAD$BRAIN$PSYCHE$NOUS |nous|))) (DEFCONCEPT PERCEPTION_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PERCEPTION_2 COGNITION) (DOCUMENTATION PERCEPTION_2 "knowledge gained by perceiving; ’a man admired for the depth of his perception’") (HAS-I-TOPIC PERCEPTION_2 |Psychology|) (WORD PERCEPTION_2 |perception|))) (DEFCONCEPT COGNITIVE_STATE$STATE_OF_MIND (?SELF) :=> (COGNITIVE-STATE ?SELF) :AXIOMS (AND (SUBJECT COGNITIVE_STATE$STATE_OF_MIND COGNITION) (DOCUMENTATION COGNITIVE_STATE$STATE_OF_MIND "the state of a person’s cognitive processes") (HAS-I-TOPIC COGNITIVE_STATE$STATE_OF_MIND |Psychology|) (WORD COGNITIVE_STATE$STATE_OF_MIND |cognitive state|) (WORD COGNITIVE_STATE$STATE_OF_MIND |state of mind|))) (DEFCONCEPT PSYCHOLOGICAL_STATE$MENTAL_STATE (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT PSYCHOLOGICAL_STATE$MENTAL_STATE STATES) (DOCUMENTATION PSYCHOLOGICAL_STATE$MENTAL_STATE "a mental condition in which the qualities of a state are relatively constant even though the state itself may be dynamic; ’a manic state’") (HAS-I-TOPIC PSYCHOLOGICAL_STATE$MENTAL_STATE |Psychology|) (WORD PSYCHOLOGICAL_STATE$MENTAL_STATE |psychological_state|) (WORD PSYCHOLOGICAL_STATE$MENTAL_STATE |mental_state|))) (DEFCONCEPT CONGREGATION$FOLD$FAITHFUL (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT CONGREGATION$FOLD$FAITHFUL GROUPS)

253

(DOCUMENTATION CONGREGATION$FOLD$FAITHFUL "a group of people who adhere to a common faith and habitually attend a given church") (HAS-I-TOPIC CONGREGATION$FOLD$FAITHFUL |Religion|) (WORD CONGREGATION$FOLD$FAITHFUL |congregation|) (WORD CONGREGATION$FOLD$FAITHFUL |fold|) (WORD CONGREGATION$FOLD$FAITHFUL |faithful|))) (DEFCONCEPT SAINTHOOD (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT SAINTHOOD GROUPS) (DOCUMENTATION SAINTHOOD "saints collectively") (HAS-I-TOPIC SAINTHOOD |Religion|) (WORD SAINTHOOD |sainthood|))) (DEFCONCEPT WISE_MEN$MAGI (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT WISE_MEN$MAGI GROUPS) (DOCUMENTATION WISE_MEN$MAGI "(New Testament) the sages who visited Jesus and Mary and Joseph shortly after Jesus was born; according to the Gospel of Matthew they were guided by a star and brought gifts of gold and frankincense and myrrh; because there were three gifts it is usually assumed that there were three of them") (HAS-I-TOPIC WISE_MEN$MAGI |Religion|) (WORD WISE_MEN$MAGI |Wise_Men|) (WORD WISE_MEN$MAGI |Magi|))) (DEFCONCEPT DESTINY$FATE_2 (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT DESTINY$FATE_2 PERSONS) (DOCUMENTATION DESTINY$FATE_2 "the ultimate agency that predetermines the course of events (often personified as a woman); ’we are helpless in the face of Destiny’") (HAS-I-TOPIC DESTINY$FATE_2 |Religion|) (WORD DESTINY$FATE_2 |Destiny|) (WORD DESTINY$FATE_2 |Fate|))) (DEFCONCEPT FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE PERSONS) (DOCUMENTATION FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE "a self-caused agent that is the cause of all things; ’God is the first cause’") (HAS-I-TOPIC FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE |Religion|) (WORD FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE |first_cause|) (WORD FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE |prime_mover|) (WORD FIRST_CAUSE$PRIME_MOVER$PRIMUM_MOBILE |primum_mobile|))) (DEFCONCEPT SUPERNATURAL$OCCULT (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT SUPERNATURAL$OCCULT PERSONS) (DOCUMENTATION SUPERNATURAL$OCCULT "supernatural forces and events and beings collectively; ’She doesn’t believe in the supernatural’") (HAS-I-TOPIC SUPERNATURAL$OCCULT |Religion|) (WORD SUPERNATURAL$OCCULT |supernatural|) (WORD SUPERNATURAL$OCCULT |occult|))) (DEFCONCEPT PHILOSOPHER_S_STONE (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT PHILOSOPHER_S_STONE SUBSTANCES) (DOCUMENTATION PHILOSOPHER_S_STONE "a hypothetical substance that the alchemists believed to be capable of changing other metals into gold") (HAS-I-TOPIC PHILOSOPHER_S_STONE |Mythology|) (WORD PHILOSOPHER_S_STONE |philosopher’s_stone|))) (DEFCONCEPT FALL_3 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT FALL_3 EVENTS) (DOCUMENTATION FALL_3 "the lapse of mankind into sinfulness because of the sin of Adam and Eve; ’women have been blamed ever since the Fall’") (HAS-I-TOPIC FALL_3 |Religion|) (WORD FALL_3 |Fall|))) (DEFCONCEPT MIRACLE_1 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT MIRACLE_1 EVENTS) (DOCUMENTATION MIRACLE_1 "a marvellous event manifesting a supernatural act of God") (HAS-I-TOPIC MIRACLE_1 |Religion|) (WORD MIRACLE_1 |miracle|)))

254

(DEFCONCEPT HOLY_PLACE$SANCTUM$HOLY (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT HOLY_PLACE$SANCTUM$HOLY LOCATIONS) (DOCUMENTATION HOLY_PLACE$SANCTUM$HOLY "a sacred place of pilgrimage") (HAS-I-TOPIC HOLY_PLACE$SANCTUM$HOLY |Religion|) (WORD HOLY_PLACE$SANCTUM$HOLY |holy_place|) (WORD HOLY_PLACE$SANCTUM$HOLY |sanctum|) (WORD HOLY_PLACE$SANCTUM$HOLY |holy|))) (DEFCONCEPT OMNIPOTENCE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT OMNIPOTENCE STATES) (DOCUMENTATION OMNIPOTENCE "the state of being omnipotent; having unlimited power") (HAS-I-TOPIC OMNIPOTENCE |Religion|) (WORD OMNIPOTENCE |omnipotence|))) (DEFCONCEPT OMNISCIENCE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT OMNISCIENCE STATES) (DOCUMENTATION OMNISCIENCE "the state of being omniscient; having infinite knowledge") (HAS-I-TOPIC OMNISCIENCE |Religion|) (WORD OMNISCIENCE |omniscience|))) (DEFCONCEPT PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION COMMUNICATION) (DOCUMENTATION PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION "communication by paranormal means") (HAS-I-TOPIC PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION |Occultism|) (WORD PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION |psychic communication|) (WORD PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION |psychical communication|) (WORD PSYCHIC_COMMUNICATION$PSYCHICAL_COMMUNICATION$ ANOMALOUS_COMMUNICATION |anomalous communication|))) (DEFCONCEPT WORKS$DEEDS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT WORKS$DEEDS ACTS) (DOCUMENTATION WORKS$DEEDS "performance of moral or religious acts; ’salvation by deeds’ or ’the reward for good works’") (HAS-I-TOPIC WORKS$DEEDS |Religion|) (WORD WORKS$DEEDS |works|) (WORD WORKS$DEEDS |deeds|))) (DEFCONCEPT SPIRITUAL_BEING$SUPERNATURAL_BEING (?SELF) :=> (SOCIALLY-CONSTRUCTED-PERSON ?SELF) :AXIOMS (AND (SUBJECT SPIRITUAL_BEING$SUPERNATURAL_BEING PERSONS) (DOCUMENTATION SPIRITUAL_BEING$SUPERNATURAL_BEING "an incorporeal being with powers to affect the course of human events") (HAS-I-TOPIC SPIRITUAL_BEING$SUPERNATURAL_BEING |Religion|) (WORD SPIRITUAL_BEING$SUPERNATURAL_BEING |spiritual_being|) (WORD SPIRITUAL_BEING$SUPERNATURAL_BEING |supernatural_being|))) (DEFCONCEPT DAMNATION$ETERNAL_DAMNATION (?SELF) :=> (STATE ?SELF)

255

:AXIOMS (AND (SUBJECT DAMNATION$ETERNAL_DAMNATION STATES) (DOCUMENTATION DAMNATION$ETERNAL_DAMNATION "the state of being condemned to eternal punishment in Hell") (HAS-I-TOPIC DAMNATION$ETERNAL_DAMNATION |Religion|) (WORD DAMNATION$ETERNAL_DAMNATION |damnation|) (WORD DAMNATION$ETERNAL_DAMNATION |eternal_damnation|))) (DEFCONCEPT GRACE$STATE_OF_GRACE (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT GRACE$STATE_OF_GRACE STATES) (DOCUMENTATION GRACE$STATE_OF_GRACE "a state of sanctification by God") (HAS-I-TOPIC GRACE$STATE_OF_GRACE |Religion|) (WORD GRACE$STATE_OF_GRACE |grace|) (WORD GRACE$STATE_OF_GRACE |state_of_grace|))) (DEFCONCEPT MYTHOLOGY_2 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT MYTHOLOGY_2 GROUPS) (DOCUMENTATION MYTHOLOGY_2 "myths collectively; the body of stories associated with a culture or institution or person") (HAS-I-TOPIC MYTHOLOGY_2 |Mythology|) (WORD MYTHOLOGY_2 |mythology|))) (DEFCONCEPT RATE_2 (?SELF) :=> (PHYSICAL-REGION ?SELF) :AXIOMS (AND (SUBJECT RATE_2 TIME) (DOCUMENTATION RATE_2 "a magnitude or frequency relative to a time unit; ’they traveled at a rate of 55 miles per hour’; ’the rate of change was faster than expected’") (HAS-I-TOPIC RATE_2 |Metrology|) (WORD RATE_2 |rate|))) (DEFCONCEPT MEASURE$QUANTITY$AMOUNT$QUANTUM (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT MEASURE$QUANTITY$AMOUNT$QUANTUM TOPS) (DOCUMENTATION MEASURE$QUANTITY$AMOUNT$QUANTUM "how much there is of something that you can measure") (HAS-I-TOPIC MEASURE$QUANTITY$AMOUNT$QUANTUM |Metrology|) (WORD MEASURE$QUANTITY$AMOUNT$QUANTUM |measure|) (WORD MEASURE$QUANTITY$AMOUNT$QUANTUM |quantity|) (WORD MEASURE$QUANTITY$AMOUNT$QUANTUM |amount|) (WORD MEASURE$QUANTITY$AMOUNT$QUANTUM |quantum|))) (DEFCONCEPT RATIO_WN (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT RATIO_WN RELATIONS) (DOCUMENTATION RATIO_WN "the relative magnitudes of two quantities (usually expressed as a quotient)") (HAS-I-TOPIC RATIO_WN |Metrology|) (WORD RATIO_WN |ratio|))) (DEFCONCEPT SCALE_3 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SCALE_3 RELATIONS) (DOCUMENTATION SCALE_3 "relative magnitude; ’they entertained on a grand scale’") (HAS-I-TOPIC SCALE_3 |Metrology|) (WORD SCALE_3 |scale|))) (DEFCONCEPT TEMPORAL_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT TEMPORAL_RELATION RELATIONS) (DOCUMENTATION TEMPORAL_RELATION "a relation involving time") (HAS-I-TOPIC TEMPORAL_RELATION |Metrology|) (WORD TEMPORAL_RELATION |temporal_relation|))) (DEFCONCEPT HUNK$LUMP (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT HUNK$LUMP OBJECTS) (DOCUMENTATION HUNK$LUMP "a large piece of something without definite shape; ’a hunk of bread’ or ’a lump of coal’") (HAS-I-TOPIC HUNK$LUMP |Metrology|) (WORD HUNK$LUMP |hunk|) (WORD HUNK$LUMP |lump|))) (DEFCONCEPT PEOPLE_1 (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT PEOPLE_1 GROUPS) (DOCUMENTATION PEOPLE_1 "(plural) any group of human beings (men or women or children) collectively; ’old people’; ’there were at least 200 people in the audience’")

256

(HAS-I-TOPIC PEOPLE_1 |Person|) (WORD PEOPLE_1 |people|))) (DEFCONCEPT OPERATOR$MANIPULATOR (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT OPERATOR$MANIPULATOR PERSONS) (DOCUMENTATION OPERATOR$MANIPULATOR "an agent that operates some apparatus or machine; ’the operator of the switchboard’") (HAS-I-TOPIC OPERATOR$MANIPULATOR |Person|) (WORD OPERATOR$MANIPULATOR |operator|) (WORD OPERATOR$MANIPULATOR |manipulator|))) (DEFCONCEPT PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL (?SELF) :=> (SOCIALLY-CONSTRUCTED-PERSON ?SELF) :AXIOMS (AND (SUBJECT PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL TOPS) (DOCUMENTATION PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL "a human being; ’there was too much for one person to do’") (HAS-I-TOPIC PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |Biology|) (HAS-I-TOPIC PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |Person|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |person|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |individual|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |someone|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |somebody|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |mortal|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |human|) (WORD PERSON$INDIVIDUAL$SOMEONE$SOMEBODY$MORTAL$HUMAN$SOUL |soul|))) (DEFCONCEPT TIME_1 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT TIME_1 TOPS) (DOCUMENTATION TIME_1 "the continuum of experience in which events pass from the future through the present to the past") (HAS-I-TOPIC TIME_1 |Time_Period|) (WORD TIME_1 |time|))) (DEFCONCEPT GOAL$END (?SELF) :=> (GOAL ?SELF) :AXIOMS (AND (SUBJECT GOAL$END COGNITION) (DOCUMENTATION GOAL$END "the state of affairs that a plan is intended to achieve and that (when achieved) terminates behavior intended to achieve it; ’the ends justify the means’") (HAS-I-TOPIC GOAL$END |Factotum|) (WORD GOAL$END |goal|) (WORD GOAL$END |end|))) (DEFCONCEPT PLAN$PROGRAM$PROGRAMME (?SELF) :=> (PLAN ?SELF) :AXIOMS (AND (SUBJECT PLAN$PROGRAM$PROGRAMME COGNITION) (DOCUMENTATION PLAN$PROGRAM$PROGRAMME "a series of steps to be carried out or goals to be accomplished; ’they drew up a six-step plan’; ’they discussed plans for a new bond issue’") (HAS-I-TOPIC PLAN$PROGRAM$PROGRAMME |Factotum|) (WORD PLAN$PROGRAM$PROGRAMME |plan|) (WORD PLAN$PROGRAM$PROGRAMME |program|) (WORD PLAN$PROGRAM$PROGRAMME |programme|))) (DEFCONCEPT QUALITY$CHARACTER$LINEAMENT (?SELF) :=> (ABSTRACT-REGION ?SELF) :AXIOMS (AND (SUBJECT QUALITY$CHARACTER$LINEAMENT COGNITION) (DOCUMENTATION QUALITY$CHARACTER$LINEAMENT "a characteristic property that defines the apparent individual nature of something; ’each town has a quality all its own’; ’the radical character of our demands’") (HAS-I-TOPIC QUALITY$CHARACTER$LINEAMENT |Factotum|) (WORD QUALITY$CHARACTER$LINEAMENT |quality|) (WORD QUALITY$CHARACTER$LINEAMENT |character|) (WORD QUALITY$CHARACTER$LINEAMENT |lineament|))) (DEFCONCEPT CONGREGATION (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT CONGREGATION GROUPS) (DOCUMENTATION CONGREGATION "an assemblage of people or animals or things collected together;

257

’a congregation of children pleaded for his autograph’; ’a great congregation of birds flew over’") (HAS-I-TOPIC CONGREGATION |Factotum|) (WORD CONGREGATION |congregation|))) (DEFCONCEPT GATHERING$ASSEMBLAGE (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT GATHERING$ASSEMBLAGE GROUPS) (DOCUMENTATION GATHERING$ASSEMBLAGE "a group of persons together in one place") (HAS-I-TOPIC GATHERING$ASSEMBLAGE |Factotum|) (WORD GATHERING$ASSEMBLAGE |gathering|) (WORD GATHERING$ASSEMBLAGE |assemblage|))) (DEFCONCEPT PROCESSION (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT PROCESSION GROUPS) (DOCUMENTATION PROCESSION "a collection of things moving ahead in an orderly manner") (HAS-I-TOPIC PROCESSION |Factotum|) (WORD PROCESSION |procession|))) (DEFCONCEPT SET$CIRCLE$BAND$LOT (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT SET$CIRCLE$BAND$LOT GROUPS) (DOCUMENTATION SET$CIRCLE$BAND$LOT "an unofficial association of people or groups; ’the smart set goes there’; ’they were an angry lot’") (HAS-I-TOPIC SET$CIRCLE$BAND$LOT |Factotum|) (WORD SET$CIRCLE$BAND$LOT |set|) (WORD SET$CIRCLE$BAND$LOT |circle|) (WORD SET$CIRCLE$BAND$LOT |band|) (WORD SET$CIRCLE$BAND$LOT |lot|))) (DEFCONCEPT TENANTRY (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT TENANTRY GROUPS) (DOCUMENTATION TENANTRY "tenants of an estate considered as a group") (HAS-I-TOPIC TENANTRY |Factotum|) (WORD TENANTRY |tenantry|))) (DEFCONCEPT WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$ HUMAN_BEINGS$HUMANS$MANKIND$MAN (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN GROUPS) (DOCUMENTATION WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN "all of the inhabitants of the earth; ’all the world loves a lover’") (HAS-I-TOPIC WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |Factotum|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |world|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |human race|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |humanity|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |humankind|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |human beings|)

258

(WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |humans|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |mankind|) (WORD WORLD$HUMAN_RACE$HUMANITY$HUMANKIND$HUMAN_BEINGS$ HUMANS$MANKIND$MAN |man|))) (DEFCONCEPT DEUS_EX_MACHINA (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT DEUS_EX_MACHINA PERSONS) (DOCUMENTATION DEUS_EX_MACHINA "any active agent who appears unexpectedly to solve and insoluble difficulty") (HAS-I-TOPIC DEUS_EX_MACHINA |Factotum|) (WORD DEUS_EX_MACHINA |deus_ex_machina|))) (DEFCONCEPT FORCE_2 (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT FORCE_2 GROUPS) (DOCUMENTATION FORCE_2 "a group of people having the power of effective action; ’he joined forces with a band of adventurers’") (HAS-I-TOPIC FORCE_2 |Factotum|) (WORD FORCE_2 |force|))) (DEFCONCEPT NATURE_3 (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT NATURE_3 PERSONS) (DOCUMENTATION NATURE_3 "a causal agent creating and controlling things in the universe; ’nature has seen to it that men are stronger than women’") (HAS-I-TOPIC NATURE_3 |Factotum|) (WORD NATURE_3 |nature|))) (DEFCONCEPT POWER$FORCE (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT POWER$FORCE PERSONS) (DOCUMENTATION POWER$FORCE "one possessing or exercising power or influence or authority: ’the mysterious presence of an evil power’; ’may the force be with you’; ’the forces of evil’") (HAS-I-TOPIC POWER$FORCE |Factotum|) (WORD POWER$FORCE |power|) (WORD POWER$FORCE |force|))) (DEFCONCEPT PRODUCER_1 (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT PRODUCER_1 EVENTS) (DOCUMENTATION PRODUCER_1 "something that produces; ’Maine is a leading producer of potatoes’ or ’this microorganism is a producer of disease’") (HAS-I-TOPIC PRODUCER_1 |Factotum|) (WORD PRODUCER_1 |producer|))) (DEFCONCEPT AEROSPACE (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT AEROSPACE LOCATIONS) (DOCUMENTATION AEROSPACE "the atmosphere and outer space considered as a whole") (HAS-I-TOPIC AEROSPACE |Factotum|) (WORD AEROSPACE |aerospace|))) (DEFCONCEPT IONOSPHERE (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT IONOSPHERE LOCATIONS) (DOCUMENTATION IONOSPHERE "the outer region of the Earth’s atmosphere; contains a high concentration of free electrons") (HAS-I-TOPIC IONOSPHERE |Factotum|) (WORD IONOSPHERE |ionosphere|))) (DEFCONCEPT MASS_5 (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT MASS_5 OBJECTS) (DOCUMENTATION MASS_5 "a large body of matter without definite shape; ’a huge ice mass’") (HAS-I-TOPIC MASS_5 |Factotum|) (WORD MASS_5 |mass|))) (DEFCONCEPT BACKLOG (?SELF) :=> (ARBITRARY-SUM ?SELF)

259

:AXIOMS (AND (SUBJECT BACKLOG GROUPS) (DOCUMENTATION BACKLOG "an accumulation of jobs not done or materials not processed that are yet to be dealt with; ’a large backlog of orders’") (HAS-I-TOPIC BACKLOG |Factotum|) (WORD BACKLOG |backlog|))) (DEFCONCEPT CONTENT_1 (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT CONTENT_1 GROUPS) (DOCUMENTATION CONTENT_1 "everything that is included in a collection; ’he emptied the contents of his pockets’; ’the two groups were similar in content’") (HAS-I-TOPIC CONTENT_1 |Factotum|) (WORD CONTENT_1 |content|))) (DEFCONCEPT DATA$INFORMATION (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT DATA$INFORMATION GROUPS) (DOCUMENTATION DATA$INFORMATION "a collection of facts from which conclusions may be drawn; ’statistical data’") (HAS-I-TOPIC DATA$INFORMATION |Factotum|) (WORD DATA$INFORMATION |data|) (WORD DATA$INFORMATION |information|))) (DEFCONCEPT PILE$HEAP$MOUND (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT PILE$HEAP$MOUND GROUPS) (DOCUMENTATION PILE$HEAP$MOUND "a collection of objects laid on top of each other") (HAS-I-TOPIC PILE$HEAP$MOUND |Factotum|) (WORD PILE$HEAP$MOUND |pile|) (WORD PILE$HEAP$MOUND |heap|) (WORD PILE$HEAP$MOUND |mound|))) (DEFCONCEPT STRAGGLE (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT STRAGGLE GROUPS) (DOCUMENTATION STRAGGLE "a wandering or disorderly grouping (of things or persons); ’a straggle of outbuildings’; ’a straggle of followers’") (HAS-I-TOPIC STRAGGLE |Factotum|) (WORD STRAGGLE |straggle|))) (DEFCONCEPT SUM$SUM_TOTAL (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT SUM$SUM_TOTAL GROUPS) (DOCUMENTATION SUM$SUM_TOTAL "the final aggregate; ’the sum of all our troubles did not equal the misery they suffered’") (HAS-I-TOPIC SUM$SUM_TOTAL |Factotum|) (WORD SUM$SUM_TOTAL |sum|) (WORD SUM$SUM_TOTAL |sum total|))) (DEFCONCEPT AGENT_1 (?SELF) :=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT AGENT_1 OBJECTS) (DOCUMENTATION AGENT_1 "an active and efficient cause; capable of producing a certain effect; ’their research uncovered new disease agents’") (HAS-I-TOPIC AGENT_1 |Factotum|) (WORD AGENT_1 |agent|))) (DEFCONCEPT CATALYST (?SELF) :=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT CATALYST PERSONS) (DOCUMENTATION CATALYST "something that causes an important event to happen; ’the invasion acted as a catalyst to unite the country’") (HAS-I-TOPIC CATALYST |Factotum|) (WORD CATALYST |catalyst|))) (DEFCONCEPT DANGER_3 (?SELF) :=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT DANGER_3 STATES) (DOCUMENTATION DANGER_3 "a cause of pain or injury or loss; ’he feared the dangers of traveling by air’") (HAS-I-TOPIC DANGER_3 |Factotum|) (WORD DANGER_3 |danger|))) (DEFCONCEPT ENGINE_2 (?SELF) :=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ENGINE_2 PHENOMENA) (DOCUMENTATION ENGINE_2 "something used to achieve a purpose: ’an engine of change’") (HAS-I-TOPIC ENGINE_2 |Factotum|) (WORD ENGINE_2 |engine|))) (DEFCONCEPT ETIOLOGY$AETIOLOGY_2 (?SELF)

260

:=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ETIOLOGY$AETIOLOGY_2 EVENTS) (DOCUMENTATION ETIOLOGY$AETIOLOGY_2 "the cause of a disease") (HAS-I-TOPIC ETIOLOGY$AETIOLOGY_2 |Factotum|) (WORD ETIOLOGY$AETIOLOGY_2 |etiology|) (WORD ETIOLOGY$AETIOLOGY_2 |aetiology|))) (DEFCONCEPT FEELING_1 (?SELF) :=> (COGNITIVE-EVENT ?SELF) :AXIOMS (AND (SUBJECT FEELING_1 TOPS) (DOCUMENTATION FEELING_1 "the psychological feature of experiencing affective and emotional states; ’he had a feeling of euphoria’") (HAS-I-TOPIC FEELING_1 |Factotum|) (WORD FEELING_1 |feeling|))) (DEFCONCEPT MOTIVATION$MOTIVE$NEED (?SELF) :=> (COGNITIVE-EVENT ?SELF) :AXIOMS (AND (SUBJECT MOTIVATION$MOTIVE$NEED TOPS) (DOCUMENTATION MOTIVATION$MOTIVE$NEED "the psychological feature that arouses an organism to action; the reason for the action; ’we did not understand his motivation’; ’he acted with the best of motives’") (HAS-I-TOPIC MOTIVATION$MOTIVE$NEED |Factotum|) (WORD MOTIVATION$MOTIVE$NEED |motivation|) (WORD MOTIVATION$MOTIVE$NEED |motive|) (WORD MOTIVATION$MOTIVE$NEED |need|))) (DEFCONCEPT ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY ACTS) (DOCUMENTATION ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY "earnest and conscientious activity intended to do or accomplish something: ’made an effort to cover all the reading material’; ’wished him luck in his endeavor’; ’she gave it a good try’") (HAS-I-TOPIC ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY |Factotum|) (WORD ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY |attempt|) (WORD ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY |effort|) (WORD ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY |endeavor|) (WORD ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY |endeavour|) (WORD ATTEMPT$EFFORT$ENDEAVOR$ENDEAVOUR$TRY |try|))) (DEFCONCEPT CONTINUANCE$CONTINUATION (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT CONTINUANCE$CONTINUATION ACTS) (DOCUMENTATION CONTINUANCE$CONTINUATION "the act of continuing or resuming an activity") (HAS-I-TOPIC CONTINUANCE$CONTINUATION |Factotum|) (WORD CONTINUANCE$CONTINUATION |continuance|) (WORD CONTINUANCE$CONTINUATION |continuation|))) (DEFCONCEPT OCCUPATION (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT OCCUPATION ACTS) (DOCUMENTATION OCCUPATION "any activity that occupies a person’s attention; ’he missed the bell in his occupation with the computer game’") (HAS-I-TOPIC OCCUPATION |Factotum|) (WORD OCCUPATION |occupation|))) (DEFCONCEPT ROUTINE$MODUS_OPERANDI (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT ROUTINE$MODUS_OPERANDI ACTS) (DOCUMENTATION ROUTINE$MODUS_OPERANDI "an unvarying or habitual method of procedure") (HAS-I-TOPIC ROUTINE$MODUS_OPERANDI |Factotum|) (WORD ROUTINE$MODUS_OPERANDI |routine|) (WORD ROUTINE$MODUS_OPERANDI |modus operandi|))) (DEFCONCEPT USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE ACTS) (DOCUMENTATION USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE "the act of using; ’the steps were worn from years of use’") (HAS-I-TOPIC USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |Factotum|) (WORD USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |use|)

261

(WORD USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |usage|) (WORD USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |utilization|) (WORD USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |utilisation|) (WORD USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |employment|) (WORD USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE |exercise|))) (DEFCONCEPT ACCIDENT$FORTUITY$CHANCE_EVENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT ACCIDENT$FORTUITY$CHANCE_EVENT EVENTS) (DOCUMENTATION ACCIDENT$FORTUITY$CHANCE_EVENT "anything that happens by chance without an apparent cause") (HAS-I-TOPIC ACCIDENT$FORTUITY$CHANCE_EVENT |Factotum|) (WORD ACCIDENT$FORTUITY$CHANCE_EVENT |accident|) (WORD ACCIDENT$FORTUITY$CHANCE_EVENT |fortuity|) (WORD ACCIDENT$FORTUITY$CHANCE_EVENT |chance event|))) (DEFCONCEPT ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE EVENTS) (DOCUMENTATION ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE "an event or situation that happens at the same time as or in connection with another") (HAS-I-TOPIC ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE |Factotum|) (WORD ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE |accompaniment|) (WORD ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE |concomitant|) (WORD ACCOMPANIMENT$CONCOMITANT$CO-OCCURRENCE |co-occurrence|))) (DEFCONCEPT ACT$HUMAN_ACTION$HUMAN_ACTIVITY (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT ACT$HUMAN_ACTION$HUMAN_ACTIVITY TOPS) (DOCUMENTATION ACT$HUMAN_ACTION$HUMAN_ACTIVITY "something that people do or cause to happen") (HAS-I-TOPIC ACT$HUMAN_ACTION$HUMAN_ACTIVITY |Factotum|) (WORD ACT$HUMAN_ACTION$HUMAN_ACTIVITY |act|) (WORD ACT$HUMAN_ACTION$HUMAN_ACTIVITY |human action|) (WORD ACT$HUMAN_ACTION$HUMAN_ACTIVITY |human activity|))) (DEFCONCEPT APPEARANCE_3 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT APPEARANCE_3 EVENTS) (DOCUMENTATION APPEARANCE_3 "the event of coming into sight") (HAS-I-TOPIC APPEARANCE_3 |Factotum|) (WORD APPEARANCE_3 |appearance|))) (DEFCONCEPT AVALANCHE_1 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT AVALANCHE_1 EVENTS) (DOCUMENTATION AVALANCHE_1 "a sudden appearance of an overwhelming number of things; ’the program brought an avalanche of mail’") (HAS-I-TOPIC AVALANCHE_1 |Factotum|) (WORD AVALANCHE_1 |avalanche|))) (DEFCONCEPT BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN EVENTS) (DOCUMENTATION BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN "a sudden happening that brings very good fortune") (HAS-I-TOPIC BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN |Factotum|) (WORD BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN |boom|) (WORD BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN |bonanza|) (WORD BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN |goldmine|) (WORD BOOM$BONANZA$GOLDMINE$MANNA_FROM_HEAVEN |manna from heaven|))) (DEFCONCEPT CASE$INSTANCE$EXAMPLE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CASE$INSTANCE$EXAMPLE EVENTS) (DOCUMENTATION CASE$INSTANCE$EXAMPLE "an occurrence of something; ’it was a case of bad judgment’; ’another instance occurred yesterday’; ’but there is always the famous example of the Smiths’") (HAS-I-TOPIC CASE$INSTANCE$EXAMPLE |Factotum|) (WORD CASE$INSTANCE$EXAMPLE |case|) (WORD CASE$INSTANCE$EXAMPLE |instance|)

262

(WORD CASE$INSTANCE$EXAMPLE |example|))) (DEFCONCEPT CASUS_BELLI (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CASUS_BELLI EVENTS) (DOCUMENTATION CASUS_BELLI "an event used to justify starting a war") (HAS-I-TOPIC CASUS_BELLI |Factotum|) (WORD CASUS_BELLI |casus belli|))) (DEFCONCEPT CHANGE$ALTERATION$MODIFICATION (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CHANGE$ALTERATION$MODIFICATION EVENTS) (DOCUMENTATION CHANGE$ALTERATION$MODIFICATION "an event that occurs when something passes from one state or phase to another: ’the change was intended to increase sales’; ’this storm is certainly a change for the worse’") (HAS-I-TOPIC CHANGE$ALTERATION$MODIFICATION |Factotum|) (WORD CHANGE$ALTERATION$MODIFICATION |change|) (WORD CHANGE$ALTERATION$MODIFICATION |alteration|) (WORD CHANGE$ALTERATION$MODIFICATION |modification|))) (DEFCONCEPT CONTACT$IMPINGING$STRIKING (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CONTACT$IMPINGING$STRIKING EVENTS) (DOCUMENTATION CONTACT$IMPINGING$STRIKING "the physical coming together of two or more things; ’contact with the pier scraped paint from the hull’") (HAS-I-TOPIC CONTACT$IMPINGING$STRIKING |Factotum|) (WORD CONTACT$IMPINGING$STRIKING |contact|) (WORD CONTACT$IMPINGING$STRIKING |impinging|) (WORD CONTACT$IMPINGING$STRIKING |striking|))) (DEFCONCEPT CONVERGENCE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CONVERGENCE EVENTS) (DOCUMENTATION CONVERGENCE "the occurrence of two or more things coming together") (HAS-I-TOPIC CONVERGENCE |Factotum|) (WORD CONVERGENCE |convergence|))) (DEFCONCEPT DESTINY$FATE_1 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT DESTINY$FATE_1 EVENTS) (DOCUMENTATION DESTINY$FATE_1 "an event (or course of events) that will inevitably happen in the future") (HAS-I-TOPIC DESTINY$FATE_1 |Factotum|) (WORD DESTINY$FATE_1 |destiny|) (WORD DESTINY$FATE_1 |fate|))) (DEFCONCEPT DISAPPEARANCE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT DISAPPEARANCE EVENTS) (DOCUMENTATION DISAPPEARANCE "the event of passing out of sight") (HAS-I-TOPIC DISAPPEARANCE |Factotum|) (WORD DISAPPEARANCE |disappearance|))) (DEFCONCEPT DISCHARGE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT DISCHARGE EVENTS) (DOCUMENTATION DISCHARGE "the sudden giving off of energy") (HAS-I-TOPIC DISCHARGE |Factotum|) (WORD DISCHARGE |discharge|))) (DEFCONCEPT EMERGENCE$EGRESS$ISSUE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT EMERGENCE$EGRESS$ISSUE EVENTS) (DOCUMENTATION EMERGENCE$EGRESS$ISSUE "the becoming visible; ’not a day’s difference between the emergence of the andrenas and the opening of the willow catkins’") (HAS-I-TOPIC EMERGENCE$EGRESS$ISSUE |Factotum|) (WORD EMERGENCE$EGRESS$ISSUE |emergence|) (WORD EMERGENCE$EGRESS$ISSUE |egress|) (WORD EMERGENCE$EGRESS$ISSUE |issue|))) (DEFCONCEPT EMERGENCE$OUTGROWTH$GROWTH (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT EMERGENCE$OUTGROWTH$GROWTH EVENTS) (DOCUMENTATION EMERGENCE$OUTGROWTH$GROWTH "the gradual beginning or coming forth; ’figurines presage the emergence of sculpture in Greece’")

263

(HAS-I-TOPIC EMERGENCE$OUTGROWTH$GROWTH |Factotum|) (WORD EMERGENCE$OUTGROWTH$GROWTH |emergence|) (WORD EMERGENCE$OUTGROWTH$GROWTH |outgrowth|) (WORD EMERGENCE$OUTGROWTH$GROWTH |growth|))) (DEFCONCEPT ENDING$CONCLUSION (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT ENDING$CONCLUSION EVENTS) (DOCUMENTATION ENDING$CONCLUSION "an event whose occurrence ends something; ’his death marked the ending of an era’") (HAS-I-TOPIC ENDING$CONCLUSION |Factotum|) (WORD ENDING$CONCLUSION |ending|) (WORD ENDING$CONCLUSION |conclusion|))) (DEFCONCEPT EPISODE_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT EPISODE_2 EVENTS) (DOCUMENTATION EPISODE_2 "a happening that is distinctive in a series of related events") (HAS-I-TOPIC EPISODE_2 |Factotum|) (WORD EPISODE_2 |episode|))) (DEFCONCEPT EVENTUALITY$CONTINGENCY (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT EVENTUALITY$CONTINGENCY EVENTS) (DOCUMENTATION EVENTUALITY$CONTINGENCY "a possible event or occurrence or result") (HAS-I-TOPIC EVENTUALITY$CONTINGENCY |Factotum|) (WORD EVENTUALITY$CONTINGENCY |eventuality|) (WORD EVENTUALITY$CONTINGENCY |contingency|))) (DEFCONCEPT EXPERIENCE_3 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT EXPERIENCE_3 EVENTS) (DOCUMENTATION EXPERIENCE_3 "an event as apprehended; ’a surprising experience’; ’that painful experience certainly got our attention’") (HAS-I-TOPIC EXPERIENCE_3 |Factotum|) (WORD EXPERIENCE_3 |experience|))) (DEFCONCEPT FAILURE_3 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT FAILURE_3 EVENTS) (DOCUMENTATION FAILURE_3 "an event that does not accomplish its intended purpose") (HAS-I-TOPIC FAILURE_3 |Factotum|) (WORD FAILURE_3 |failure|))) (DEFCONCEPT FIRE_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT FIRE_2 EVENTS) (DOCUMENTATION FIRE_2 "the event of something burning (often destructive); ’they lost everything in the fire’") (HAS-I-TOPIC FIRE_2 |Factotum|) (WORD FIRE_2 |fire|))) (DEFCONCEPT FLASH_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT FLASH_2 EVENTS) (DOCUMENTATION FLASH_2 "a sudden intense burst of radiant energy") (HAS-I-TOPIC FLASH_2 |Factotum|) (WORD FLASH_2 |flash|))) (DEFCONCEPT INCIDENT_1 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT INCIDENT_1 EVENTS) (DOCUMENTATION INCIDENT_1 "a single distinct event") (HAS-I-TOPIC INCIDENT_1 |Factotum|) (WORD INCIDENT_1 |incident|))) (DEFCONCEPT INTERRUPTION$BREAK$ABRUPT_CHANGE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT INTERRUPTION$BREAK$ABRUPT_CHANGE EVENTS) (DOCUMENTATION INTERRUPTION$BREAK$ABRUPT_CHANGE "some occurrence that interrupts; ’the telephone is an annoying interruption’; ’there was a break in the action when a player was hurt’") (HAS-I-TOPIC INTERRUPTION$BREAK$ABRUPT_CHANGE |Factotum|) (WORD INTERRUPTION$BREAK$ABRUPT_CHANGE |interruption|) (WORD INTERRUPTION$BREAK$ABRUPT_CHANGE |break|) (WORD INTERRUPTION$BREAK$ABRUPT_CHANGE |abrupt change|))) (DEFCONCEPT JUNCTURE$OCCASION (?SELF) :=> (EVENT ?SELF)

264

:AXIOMS (AND (SUBJECT JUNCTURE$OCCASION EVENTS) (DOCUMENTATION JUNCTURE$OCCASION "an event that occurs at a critical time; ’at such junctures he always had an impulse to leave’; ’it was needed only on special occasions’") (HAS-I-TOPIC JUNCTURE$OCCASION |Factotum|) (WORD JUNCTURE$OCCASION |juncture|) (WORD JUNCTURE$OCCASION |occasion|))) (DEFCONCEPT MIGHT-HAVE-BEEN (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT MIGHT-HAVE-BEEN EVENTS) (DOCUMENTATION MIGHT-HAVE-BEEN "an event that could have occurred but never did") (HAS-I-TOPIC MIGHT-HAVE-BEEN |Factotum|) (WORD MIGHT-HAVE-BEEN |might-have-been|))) (DEFCONCEPT MIRACLE_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT MIRACLE_2 EVENTS) (DOCUMENTATION MIRACLE_2 "any amazing or wonderful occurrence") (HAS-I-TOPIC MIRACLE_2 |Factotum|) (WORD MIRACLE_2 |miracle|))) (DEFCONCEPT MOVEMENT$MOTION (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT MOVEMENT$MOTION EVENTS) (DOCUMENTATION MOVEMENT$MOTION "a natural event that involves a change in the position or location of something") (HAS-I-TOPIC MOVEMENT$MOTION |Factotum|) (WORD MOVEMENT$MOTION |movement|) (WORD MOVEMENT$MOTION |motion|))) (DEFCONCEPT NEWS_EVENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT NEWS_EVENT EVENTS) (DOCUMENTATION NEWS_EVENT "a newsworthy event") (HAS-I-TOPIC NEWS_EVENT |Factotum|) (WORD NEWS_EVENT |news event|))) (DEFCONCEPT NONEVENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT NONEVENT EVENTS) (DOCUMENTATION NONEVENT "an anticipated event that turns out to be far less significant than was expected") (HAS-I-TOPIC NONEVENT |Factotum|) (WORD NONEVENT |nonevent|))) (DEFCONCEPT OUTBREAK (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT OUTBREAK EVENTS) (DOCUMENTATION OUTBREAK "a sudden violent spontaneous occurrence of an undesirable condition") (HAS-I-TOPIC OUTBREAK |Factotum|) (WORD OUTBREAK |outbreak|))) (DEFCONCEPT OUTBURST$BURST$FLARE-UP (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT OUTBURST$BURST$FLARE-UP EVENTS) (DOCUMENTATION OUTBURST$BURST$FLARE-UP "a sudden violent happening; ’an outburst of heavy rain’; ’a burst of lightning’") (HAS-I-TOPIC OUTBURST$BURST$FLARE-UP |Factotum|) (WORD OUTBURST$BURST$FLARE-UP |outburst|) (WORD OUTBURST$BURST$FLARE-UP |burst|) (WORD OUTBURST$BURST$FLARE-UP |flare-up|))) (DEFCONCEPT PERIODIC_EVENT$RECURRENT_EVENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT PERIODIC_EVENT$RECURRENT_EVENT EVENTS) (DOCUMENTATION PERIODIC_EVENT$RECURRENT_EVENT "an event that recurs at intervals") (HAS-I-TOPIC PERIODIC_EVENT$RECURRENT_EVENT |Factotum|) (WORD PERIODIC_EVENT$RECURRENT_EVENT |periodic event|) (WORD PERIODIC_EVENT$RECURRENT_EVENT |recurrent event|))) (DEFCONCEPT PHENOMENON_1 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT PHENOMENON_1 TOPS) (DOCUMENTATION PHENOMENON_1 "any state or process known through the senses rather than by intuition or reasoning") (HAS-I-TOPIC PHENOMENON_1 |Factotum|) (WORD PHENOMENON_1 |phenomenon|))) (DEFCONCEPT PRELIMINARY$OVERTURE$PRELUDE (?SELF)

265

:=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT PRELIMINARY$OVERTURE$PRELUDE EVENTS) (DOCUMENTATION PRELIMINARY$OVERTURE$PRELUDE "something that serves as a preceding event or introduces what follows; ’training is a necessary preliminary to employment’; ’drinks were the overture to dinner’") (HAS-I-TOPIC PRELIMINARY$OVERTURE$PRELUDE |Factotum|) (WORD PRELIMINARY$OVERTURE$PRELUDE |preliminary|) (WORD PRELIMINARY$OVERTURE$PRELUDE |overture|) (WORD PRELIMINARY$OVERTURE$PRELUDE |prelude|))) (DEFCONCEPT REVERSE$REVERSAL$SETBACK$BLOW (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT REVERSE$REVERSAL$SETBACK$BLOW EVENTS) (DOCUMENTATION REVERSE$REVERSAL$SETBACK$BLOW "an unfortunate happening that hinders of impedes; something that is thwarting or frustrating") (HAS-I-TOPIC REVERSE$REVERSAL$SETBACK$BLOW |Factotum|) (WORD REVERSE$REVERSAL$SETBACK$BLOW |reverse|) (WORD REVERSE$REVERSAL$SETBACK$BLOW |reversal|) (WORD REVERSE$REVERSAL$SETBACK$BLOW |setback|) (WORD REVERSE$REVERSAL$SETBACK$BLOW |blow|))) (DEFCONCEPT SOUND_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT SOUND_2 EVENTS) (DOCUMENTATION SOUND_2 "the sudden occurrence of an audible event; ’the sound awakened them’") (HAS-I-TOPIC SOUND_2 |Factotum|) (WORD SOUND_2 |sound|))) (DEFCONCEPT START (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT START EVENTS) (DOCUMENTATION START "the beginning of anything; ’it was off to a good start’") (HAS-I-TOPIC START |Factotum|) (WORD START |start|))) (DEFCONCEPT SUCCESS_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT SUCCESS_2 EVENTS) (DOCUMENTATION SUCCESS_2 "an event that accomplishes its intended purpose; ’let’s call heads a success and tails a failure’; ’the election was a remarkable success for Republicans’") (HAS-I-TOPIC SUCCESS_2 |Factotum|) (WORD SUCCESS_2 |success|))) (DEFCONCEPT THING_8 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT THING_8 EVENTS) (DOCUMENTATION THING_8 "an event: ’a funny thing happened on the way to the...’") (HAS-I-TOPIC THING_8 |Factotum|) (WORD THING_8 |thing|))) (DEFCONCEPT TROUBLE_1 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT TROUBLE_1 EVENTS) (DOCUMENTATION TROUBLE_1 "an event causing distress or pain; ’what is the trouble?’; ’heart trouble’") (HAS-I-TOPIC TROUBLE_1 |Factotum|) (WORD TROUBLE_1 |trouble|))) (DEFCONCEPT UNION_2 (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT UNION_2 EVENTS) (DOCUMENTATION UNION_2 "the occurrence of a uniting of separate parts; ’lightning produced an unusual union of the metals’") (HAS-I-TOPIC UNION_2 |Factotum|) (WORD UNION_2 |union|))) (DEFCONCEPT WONDER$MARVEL (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT WONDER$MARVEL EVENTS) (DOCUMENTATION WONDER$MARVEL "something that causes feelings of wonder; ’the wonders of modern science’") (HAS-I-TOPIC WONDER$MARVEL |Factotum|) (WORD WONDER$MARVEL |wonder|) (WORD WONDER$MARVEL |marvel|))) (DEFCONCEPT FEATURE$CHARACTERISTIC (?SELF) :=> (FEATURE-ROLE ?SELF) :AXIOMS (AND (SUBJECT FEATURE$CHARACTERISTIC COGNITION) (DOCUMENTATION FEATURE$CHARACTERISTIC "a prominent aspect of something: ’the map showed roads and other features’;

266

’generosity is one of his best characteristics’") (HAS-I-TOPIC FEATURE$CHARACTERISTIC |Factotum|) (WORD FEATURE$CHARACTERISTIC |feature|) (WORD FEATURE$CHARACTERISTIC |characteristic|))) (DEFCONCEPT PART$SECTION$DIVISION (?SELF) :=> (FEATURE-ROLE ?SELF) :AXIOMS (AND (SUBJECT PART$SECTION$DIVISION COGNITION) (DOCUMENTATION PART$SECTION$DIVISION "one of the portions into which something is regarded as divided and which together constitute a whole: ’the written part of the exam’; ’the finance section of the company’; ’the BBC’s engineering division’") (HAS-I-TOPIC PART$SECTION$DIVISION |Factotum|) (WORD PART$SECTION$DIVISION |part|) (WORD PART$SECTION$DIVISION |section|) (WORD PART$SECTION$DIVISION |division|))) (DEFCONCEPT AIR_3 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT AIR_3 LOCATIONS) (DOCUMENTATION AIR_3 "the region above the ground; ’her hand stopped in mid air’; ’the hanged man danced on air’") (HAS-I-TOPIC AIR_3 |Factotum|) (WORD AIR_3 |air|))) (DEFCONCEPT BELT_3 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT BELT_3 LOCATIONS) (DOCUMENTATION BELT_3 "an elongated region where a specific condition is found; ’a belt of high pressure’") (HAS-I-TOPIC BELT_3 |Factotum|) (WORD BELT_3 |belt|))) (DEFCONCEPT BOTTOM (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT BOTTOM LOCATIONS) (DOCUMENTATION BOTTOM "the lowest part of anything; ’they started at the bottom of the hill’") (HAS-I-TOPIC BOTTOM |Factotum|) (WORD BOTTOM |bottom|))) (DEFCONCEPT BOUNDARY$EDGE$BOUND (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT BOUNDARY$EDGE$BOUND SHAPES) (DOCUMENTATION BOUNDARY$EDGE$BOUND "a line determining the limits of an area") (HAS-I-TOPIC BOUNDARY$EDGE$BOUND |Factotum|) (WORD BOUNDARY$EDGE$BOUND |boundary|) (WORD BOUNDARY$EDGE$BOUND |edge|) (WORD BOUNDARY$EDGE$BOUND |bound|))) (DEFCONCEPT CENTERLINE$CENTER_LINE (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT CENTERLINE$CENTER_LINE SHAPES) (DOCUMENTATION CENTERLINE$CENTER_LINE "a line that bisects a plane figure") (HAS-I-TOPIC CENTERLINE$CENTER_LINE |Factotum|) (WORD CENTERLINE$CENTER_LINE |centerline|) (WORD CENTERLINE$CENTER_LINE |center_line|))) (DEFCONCEPT CONNECTION$CONNEXION$LINK (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT CONNECTION$CONNEXION$LINK SHAPES) (DOCUMENTATION CONNECTION$CONNEXION$LINK "a connecting shape") (HAS-I-TOPIC CONNECTION$CONNEXION$LINK |Factotum|) (WORD CONNECTION$CONNEXION$LINK |connection|) (WORD CONNECTION$CONNEXION$LINK |connexion|) (WORD CONNECTION$CONNEXION$LINK |link|))) (DEFCONCEPT CORNER_5 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT CORNER_5 OBJECTS) (DOCUMENTATION CORNER_5 "a projecting part that is corner-shaped; ’he knocked off the corners’") (HAS-I-TOPIC CORNER_5 |Factotum|) (WORD CORNER_5 |corner|))) (DEFCONCEPT ENCLOSURE (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT ENCLOSURE ARTIFACTS) (DOCUMENTATION ENCLOSURE "a space that has been enclosed for some purpose")

267

(HAS-I-TOPIC ENCLOSURE |Factotum|) (WORD ENCLOSURE |enclosure|))) (DEFCONCEPT EXTREMITY_2 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT EXTREMITY_2 LOCATIONS) (DOCUMENTATION EXTREMITY_2 "the outermost or farthest region or point") (HAS-I-TOPIC EXTREMITY_2 |Factotum|) (WORD EXTREMITY_2 |extremity|))) (DEFCONCEPT FRAGMENT (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT FRAGMENT OBJECTS) (DOCUMENTATION FRAGMENT "a piece broken off of something else; ’a fragment of rock’") (HAS-I-TOPIC FRAGMENT |Factotum|) (WORD FRAGMENT |fragment|))) (DEFCONCEPT HEAD_8 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT HEAD_8 OBJECTS) (DOCUMENTATION HEAD_8 "a rounded compact mass; ’the head of a comet’") (HAS-I-TOPIC HEAD_8 |Factotum|) (WORD HEAD_8 |head|))) (DEFCONCEPT HERE (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT HERE LOCATIONS) (DOCUMENTATION HERE "the present location; this place; ’where do we go from here?’") (HAS-I-TOPIC HERE |Factotum|) (WORD HERE |here|))) (DEFCONCEPT INSIDE$INTERIOR_2 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT INSIDE$INTERIOR_2 LOCATIONS) (DOCUMENTATION INSIDE$INTERIOR_2 "the region that is inside of something") (HAS-I-TOPIC INSIDE$INTERIOR_2 |Factotum|) (WORD INSIDE$INTERIOR_2 |inside|) (WORD INSIDE$INTERIOR_2 |interior|))) (DEFCONCEPT LAYER_3 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT LAYER_3 LOCATIONS) (DOCUMENTATION LAYER_3 "a relatively thin sheetlike expanse or region lying over or under another") (HAS-I-TOPIC LAYER_3 |Factotum|) (WORD LAYER_3 |layer|))) (DEFCONCEPT NUB$STUB (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT NUB$STUB OBJECTS) (DOCUMENTATION NUB$STUB "a small piece; ’a nub of coal’ or ’a stub of a pencil’") (HAS-I-TOPIC NUB$STUB |Factotum|) (WORD NUB$STUB |nub|) (WORD NUB$STUB |stub|))) (DEFCONCEPT OPENING_3 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT OPENING_3 ARTIFACTS) (DOCUMENTATION OPENING_3 "a vacant or unobstructed space; ’they left a small opening for the cat at the bottom of the door’") (HAS-I-TOPIC OPENING_3 |Factotum|) (WORD OPENING_3 |opening|))) (DEFCONCEPT OUTSIDE$EXTERIOR_2 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT OUTSIDE$EXTERIOR_2 LOCATIONS) (DOCUMENTATION OUTSIDE$EXTERIOR_2 "the region that is outside of something") (HAS-I-TOPIC OUTSIDE$EXTERIOR_2 |Factotum|) (WORD OUTSIDE$EXTERIOR_2 |outside|) (WORD OUTSIDE$EXTERIOR_2 |exterior|))) (DEFCONCEPT PART$PORTION (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT PART$PORTION ARTIFACTS) (DOCUMENTATION PART$PORTION "something less than the whole of a human artifact: ’the rear part of the house’; ’glue the two parts together’") (HAS-I-TOPIC PART$PORTION |Factotum|) (WORD PART$PORTION |part|) (WORD PART$PORTION |portion|)))

268

(DEFCONCEPT PERIMETER (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT PERIMETER SHAPES) (DOCUMENTATION PERIMETER "a line enclosing a plane areas") (HAS-I-TOPIC PERIMETER |Factotum|) (WORD PERIMETER |perimeter|))) (DEFCONCEPT RADIUS_2 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT RADIUS_2 LOCATIONS) (DOCUMENTATION RADIUS_2 "a circular region whose area is indicated by the length of its radius; ’they located it within a radius of 2 miles’") (HAS-I-TOPIC RADIUS_2 |Factotum|) (WORD RADIUS_2 |radius|))) (DEFCONCEPT SIDE_7 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT SIDE_7 LOCATIONS) (DOCUMENTATION SIDE_7 "a place within a region identified relative to a center or reference location; ’they always sat on the right side of the church’; ’he never left my side’") (HAS-I-TOPIC SIDE_7 |Factotum|) (WORD SIDE_7 |side|))) (DEFCONCEPT SLICE_2 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT SLICE_2 OBJECTS) (DOCUMENTATION SLICE_2 "a thin flat piece cut off of some object") (HAS-I-TOPIC SLICE_2 |Factotum|) (WORD SLICE_2 |slice|))) (DEFCONCEPT SPACE_4 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT SPACE_4 SHAPES) (DOCUMENTATION SPACE_4 "an empty area (usually bounded in some way between things); ’the architect left space in front of the building’; ’they stopped at an open space in the jungle’; ’the space between his teeth’") (HAS-I-TOPIC SPACE_4 |Factotum|) (WORD SPACE_4 |space|))) (DEFCONCEPT STRIP_2 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT STRIP_2 OBJECTS) (DOCUMENTATION STRIP_2 "a relatively long narrow piece of something; ’he felt a flat strip of muscle’") (HAS-I-TOPIC STRIP_2 |Factotum|) (WORD STRIP_2 |strip|))) (DEFCONCEPT SURFACE_1 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT SURFACE_1 ARTIFACTS) (DOCUMENTATION SURFACE_1 "the outer boundary of an object or a material layer constituting or resembling such a boundary; ’there is a special cleaner for these surfaces’; ’the cloth had a pattern of red dots on a white surface’") (HAS-I-TOPIC SURFACE_1 |Factotum|) (WORD SURFACE_1 |surface|))) (DEFCONCEPT THERE (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT THERE LOCATIONS) (DOCUMENTATION THERE "a location other than here; that place; ’you can take it from there’") (HAS-I-TOPIC THERE |Factotum|) (WORD THERE |there|))) (DEFCONCEPT TOP_4 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT TOP_4 LOCATIONS) (DOCUMENTATION TOP_4 "the upper part of anything; ’the mower cuts off the tops of the grass’; ’the title should be written at the top of the first page’") (HAS-I-TOPIC TOP_4 |Factotum|) (WORD TOP_4 |top|))) (DEFCONCEPT VACUUM$VACUITY_1 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT VACUUM$VACUITY_1 LOCATIONS) (DOCUMENTATION VACUUM$VACUITY_1 "a region empty of matter") (HAS-I-TOPIC VACUUM$VACUITY_1 |Factotum|) (WORD VACUUM$VACUITY_1 |vacuum|) (WORD VACUUM$VACUITY_1 |vacuity|))) (DEFCONCEPT WHEREABOUTS (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT WHEREABOUTS LOCATIONS)

269

(DOCUMENTATION WHEREABOUTS "the general location where something is; ’I questioned him about his whereabouts on the night of the crime’") (HAS-I-TOPIC WHEREABOUTS |Factotum|) (WORD WHEREABOUTS |whereabouts|))) (DEFCONCEPT ARTICLE_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ARTICLE_1 TOPS) (DOCUMENTATION ARTICLE_1 "one of a class of artifacts; ’an article of clothing’") (HAS-I-TOPIC ARTICLE_1 |Factotum|) (WORD ARTICLE_1 |article|))) (DEFCONCEPT BLOCK_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT BLOCK_1 ARTIFACTS) (DOCUMENTATION BLOCK_1 "a solid piece of something (usually having flat rectangular sides); ’the pyramids were built with large stone blocks’") (HAS-I-TOPIC BLOCK_1 |Factotum|) (WORD BLOCK_1 |block|))) (DEFCONCEPT CONE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT CONE ARTIFACTS) (DOCUMENTATION CONE "any cone-shaped artifact") (HAS-I-TOPIC CONE |Factotum|) (WORD CONE |cone|))) (DEFCONCEPT COVERING_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT COVERING_2 ARTIFACTS) (DOCUMENTATION COVERING_2 "an artifact that protects or shelters or conceals") (HAS-I-TOPIC COVERING_2 |Factotum|) (WORD COVERING_2 |covering|))) (DEFCONCEPT CREATION_3 (?SELF) :=> (CREATIVE-OBJECT ?SELF) :AXIOMS (AND (SUBJECT CREATION_3 ARTIFACTS) (DOCUMENTATION CREATION_3 "something that has been brought into existence by someone") (HAS-I-TOPIC CREATION_3 |Factotum|) (WORD CREATION_3 |creation|))) (DEFCONCEPT DECKER (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT DECKER ARTIFACTS) (DOCUMENTATION DECKER "(often used in combination) something constructed with multiple levels; ’they rode in a double-decker bus’") (HAS-I-TOPIC DECKER |Factotum|) (WORD DECKER |decker|))) (DEFCONCEPT DECORATION$ORNAMENT$ORNAMENTATION (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT DECORATION$ORNAMENT$ORNAMENTATION ARTIFACTS) (DOCUMENTATION DECORATION$ORNAMENT$ORNAMENTATION "something used to beautify") (HAS-I-TOPIC DECORATION$ORNAMENT$ORNAMENTATION |Factotum|) (WORD DECORATION$ORNAMENT$ORNAMENTATION |decoration|) (WORD DECORATION$ORNAMENT$ORNAMENTATION |ornament|) (WORD DECORATION$ORNAMENT$ORNAMENTATION |ornamentation|))) (DEFCONCEPT FIXTURE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT FIXTURE ARTIFACTS) (DOCUMENTATION FIXTURE "a object firmly fixed in place (especially in a household)") (HAS-I-TOPIC FIXTURE |Factotum|) (WORD FIXTURE |fixture|))) (DEFCONCEPT FLOAT_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT FLOAT_1 ARTIFACTS) (DOCUMENTATION FLOAT_1 "something that remains on the surface of a liquid") (HAS-I-TOPIC FLOAT_1 |Factotum|) (WORD FLOAT_1 |float|))) (DEFCONCEPT INSERT$INSET (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT INSERT$INSET ARTIFACTS) (DOCUMENTATION INSERT$INSET "something inserted or to be inserted") (HAS-I-TOPIC INSERT$INSET |Factotum|) (WORD INSERT$INSET |insert|)

270

(WORD INSERT$INSET |inset|))) (DEFCONCEPT INSTRUMENTALITY$INSTRUMENTATION (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT INSTRUMENTALITY$INSTRUMENTATION ARTIFACTS) (DOCUMENTATION INSTRUMENTALITY$INSTRUMENTATION "an artifact (or system of artifacts) that is instrumental in accomplishing some end") (HAS-I-TOPIC INSTRUMENTALITY$INSTRUMENTATION |Factotum|) (WORD INSTRUMENTALITY$INSTRUMENTATION |instrumentality|) (WORD INSTRUMENTALITY$INSTRUMENTATION |instrumentation|))) (DEFCONCEPT LINE_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT LINE_2 ARTIFACTS) (DOCUMENTATION LINE_2 "something long and thin and flexible") (HAS-I-TOPIC LINE_2 |Factotum|) (WORD LINE_2 |line|))) (DEFCONCEPT MARKER_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT MARKER_1 ARTIFACTS) (DOCUMENTATION MARKER_1 "some conspicuous object used to distinguish or mark something; ’the buoys were markers for the channel’") (HAS-I-TOPIC MARKER_1 |Factotum|) (WORD MARKER_1 |marker|))) (DEFCONCEPT SHEET$FLAT_SOLID (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT SHEET$FLAT_SOLID ARTIFACTS) (DOCUMENTATION SHEET$FLAT_SOLID "a flat man-made object that is thin relative to its length and width") (HAS-I-TOPIC SHEET$FLAT_SOLID |Factotum|) (WORD SHEET$FLAT_SOLID |sheet|) (WORD SHEET$FLAT_SOLID |flat solid|))) (DEFCONCEPT SPHERE_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT SPHERE_1 ARTIFACTS) (DOCUMENTATION SPHERE_1 "any spherically shaped artifact") (HAS-I-TOPIC SPHERE_1 |Factotum|) (WORD SPHERE_1 |sphere|))) (DEFCONCEPT SQUARE_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT SQUARE_2 ARTIFACTS) (DOCUMENTATION SQUARE_2 "any object having a shape similar to a plane geometric figure with four equal sides and four right angles; ’a chessboard has 64 squares’") (HAS-I-TOPIC SQUARE_2 |Factotum|) (WORD SQUARE_2 |square|))) (DEFCONCEPT STRIP$SLIP (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT STRIP$SLIP ARTIFACTS) (DOCUMENTATION STRIP$SLIP "a narrow flat piece of material") (HAS-I-TOPIC STRIP$SLIP |Factotum|) (WORD STRIP$SLIP |strip|) (WORD STRIP$SLIP |slip|))) (DEFCONCEPT STRUCTURE$CONSTRUCTION (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT STRUCTURE$CONSTRUCTION ARTIFACTS) (DOCUMENTATION STRUCTURE$CONSTRUCTION "a thing constructed; a complex construction or entity; ’the structure consisted of a series of arches’; ’she wore her hair in an amazing construction of whirls and ribbons’") (HAS-I-TOPIC STRUCTURE$CONSTRUCTION |Factotum|) (WORD STRUCTURE$CONSTRUCTION |structure|) (WORD STRUCTURE$CONSTRUCTION |construction|))) (DEFCONCEPT THING_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT THING_2 ARTIFACTS) (DOCUMENTATION THING_2 "an artifact; ’how does this thing work?’") (HAS-I-TOPIC THING_2 |Factotum|) (WORD THING_2 |thing|))) (DEFCONCEPT UNIT$BUILDING_BLOCK (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT UNIT$BUILDING_BLOCK OBJECTS) (DOCUMENTATION UNIT$BUILDING_BLOCK "a single undivided natural entity occurring in the composition of something else; ’units of nucleic acids’") (HAS-I-TOPIC UNIT$BUILDING_BLOCK |Factotum|) (WORD UNIT$BUILDING_BLOCK |unit|)

271

(WORD UNIT$BUILDING_BLOCK |building_block|))) (DEFCONCEPT WEIGHT_1 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT WEIGHT_1 ARTIFACTS) (DOCUMENTATION WEIGHT_1 "an artifact that is heavy") (HAS-I-TOPIC WEIGHT_1 |Factotum|) (WORD WEIGHT_1 |weight|))) (DEFCONCEPT WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES ARTIFACTS) (DOCUMENTATION WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES "miscellaneous unspecified artifacts; ’the trunk was full of stuff’") (HAS-I-TOPIC WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES |Factotum|) (WORD WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES |whatchamacallit|) (WORD WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES |stuff|) (WORD WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES |whatsis|) (WORD WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES |sundry|) (WORD WHATCHAMACALLIT$STUFF$WHATSIS$SUNDRY$SUNDRIES |sundries|))) (DEFCONCEPT IMAGINARY_BEING$IMAGINARY_CREATURE (?SELF) :=> (FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT IMAGINARY_BEING$IMAGINARY_CREATURE PERSONS) (DOCUMENTATION IMAGINARY_BEING$IMAGINARY_CREATURE "a creature of the imagination") (HAS-I-TOPIC IMAGINARY_BEING$IMAGINARY_CREATURE |Factotum|) (WORD IMAGINARY_BEING$IMAGINARY_CREATURE |imaginary_being|) (WORD IMAGINARY_BEING$IMAGINARY_CREATURE |imaginary_creature|))) (DEFCONCEPT AGGLOMERATION (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT AGGLOMERATION GROUPS) (DOCUMENTATION AGGLOMERATION "a jumbled collection or mass") (HAS-I-TOPIC AGGLOMERATION |Factotum|) (WORD AGGLOMERATION |agglomeration|))) (DEFCONCEPT FILM (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT FILM ARTIFACTS) (DOCUMENTATION FILM "a thin coating or layer; ’the table was covered with a film of dust’") (HAS-I-TOPIC FILM |Factotum|) (WORD FILM |film|))) (DEFCONCEPT MATERIAL$STUFF (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT MATERIAL$STUFF SUBSTANCES) (DOCUMENTATION MATERIAL$STUFF "the tangible substance that goes into the makeup of a physical object; ’coal is a hard black material’; ’wheat is the stuff they use to make bread’") (HAS-I-TOPIC MATERIAL$STUFF |Factotum|) (WORD MATERIAL$STUFF |material|) (WORD MATERIAL$STUFF |stuff|))) (DEFCONCEPT SAMPLE_2 (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT SAMPLE_2 OBJECTS) (DOCUMENTATION SAMPLE_2 "all or part of a natural object that is collected and preserved as an example of its class") (HAS-I-TOPIC SAMPLE_2 |Factotum|) (WORD SAMPLE_2 |sample|))) (DEFCONCEPT ABUTMENT_2 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT ABUTMENT_2 LOCATIONS) (DOCUMENTATION ABUTMENT_2 "point of contact between two objects or parts") (HAS-I-TOPIC ABUTMENT_2 |Factotum|) (WORD ABUTMENT_2 |abutment|))) (DEFCONCEPT BACK$REAR (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT BACK$REAR LOCATIONS) (DOCUMENTATION BACK$REAR "the part of something that is furthest from the normal viewer: ’he stood at the back of the stage’; ’it was hidden in the rear of the store’") (HAS-I-TOPIC BACK$REAR |Factotum|) (WORD BACK$REAR |back|) (WORD BACK$REAR |rear|)))

272

(DEFCONCEPT CROSSING_3 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT CROSSING_3 LOCATIONS) (DOCUMENTATION CROSSING_3 "a point where two lines (paths or arcs etc.) intersect") (HAS-I-TOPIC CROSSING_3 |Factotum|) (WORD CROSSING_3 |crossing|))) (DEFCONCEPT DEPTH_3 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT DEPTH_3 LOCATIONS) (DOCUMENTATION DEPTH_3 "(usually plural) the deepest and most remote part; ’from the depths of darkest Africa’; ’signals received from the depths of space’") (HAS-I-TOPIC DEPTH_3 |Factotum|) (WORD DEPTH_3 |depth|))) (DEFCONCEPT END_7 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT END_7 LOCATIONS) (DOCUMENTATION END_7 "one of two places from which people are communicating to each other; ’the phone rang at the other end’ or ’both ends wrote at the same time’") (HAS-I-TOPIC END_7 |Factotum|) (WORD END_7 |end|))) (DEFCONCEPT FOCUS$FOCAL_POINT (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT FOCUS$FOCAL_POINT PHENOMENA) (DOCUMENTATION FOCUS$FOCAL_POINT "a point of convergence of light (or other radiation) or a point from which it diverges") (HAS-I-TOPIC FOCUS$FOCAL_POINT |Factotum|) (WORD FOCUS$FOCAL_POINT |focus|) (WORD FOCUS$FOCAL_POINT |focal_point|))) (DEFCONCEPT FOCUS_3 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT FOCUS_3 LOCATIONS) (DOCUMENTATION FOCUS_3 "a fixed reference point on the concave side of a conic section") (HAS-I-TOPIC FOCUS_3 |Factotum|) (WORD FOCUS_3 |focus|))) (DEFCONCEPT FRONT_3 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT FRONT_3 LOCATIONS) (DOCUMENTATION FRONT_3 "the part of something that is nearest to the normal viewer; ’he walked to the front of the stage’") (HAS-I-TOPIC FRONT_3 |Factotum|) (WORD FRONT_3 |front|))) (DEFCONCEPT HILUM (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT HILUM PLANTS) (DOCUMENTATION HILUM "the scar on certain seeds marking its point of attachment to the funicle") (HAS-I-TOPIC HILUM |Factotum|) (WORD HILUM |hilum|))) (DEFCONCEPT LEFT_2 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT LEFT_2 LOCATIONS) (DOCUMENTATION LEFT_2 "location near or direction toward the left side; i.e. the side to the north when a person or object faces east: ’she stood on the left’") (HAS-I-TOPIC LEFT_2 |Factotum|) (WORD LEFT_2 |left|))) (DEFCONCEPT LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION LOCATIONS) (DOCUMENTATION LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION "a mathematical value toward which a function goes as the independent variable approaches infinity") (HAS-I-TOPIC LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION |Factotum|) (WORD LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION |limit|) (WORD LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION |limit_point|) (WORD LIMIT$LIMIT_POINT$POINT_OF_ACCUMULATION |point_of_accumulation|))) (DEFCONCEPT LINE_8 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT LINE_8 LOCATIONS)

273

(DOCUMENTATION LINE_8 "a spatial location defined by a real or imaginary unidimensional extent") (HAS-I-TOPIC LINE_8 |Factotum|) (WORD LINE_8 |line|))) (DEFCONCEPT MCBURNEY_S_POINT (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT MCBURNEY_S_POINT BODY_AS_SUBJECT) (DOCUMENTATION MCBURNEY_S_POINT "a point one third of the way along a line drawn from the hip to the umbilicus; the point of maximum sensitivity in acute appendicitis") (HAS-I-TOPIC MCBURNEY_S_POINT |Factotum|) (WORD MCBURNEY_S_POINT |McBurney’s point|))) (DEFCONCEPT PARHELION$MOCK_SUN$SUNDOG (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT PARHELION$MOCK_SUN$SUNDOG PHENOMENA) (DOCUMENTATION PARHELION$MOCK_SUN$SUNDOG "a bright spot on the parhelic circle; caused by diffraction by ice crystals") (HAS-I-TOPIC PARHELION$MOCK_SUN$SUNDOG |Factotum|) (WORD PARHELION$MOCK_SUN$SUNDOG |parhelion|) (WORD PARHELION$MOCK_SUN$SUNDOG |mock_sun|) (WORD PARHELION$MOCK_SUN$SUNDOG |sundog|))) (DEFCONCEPT PEAK$CROWN$CREST$TOP$TIP$SUMMIT (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT PEAK$CROWN$CREST$TOP$TIP$SUMMIT LOCATIONS) (DOCUMENTATION PEAK$CROWN$CREST$TOP$TIP$SUMMIT "the top point of a mountain or hill; ’the view from the peak was magnificent’; ’they clambered to the summit of Monadnock’") (HAS-I-TOPIC PEAK$CROWN$CREST$TOP$TIP$SUMMIT |Factotum|) (WORD PEAK$CROWN$CREST$TOP$TIP$SUMMIT |peak|) (WORD PEAK$CROWN$CREST$TOP$TIP$SUMMIT |crown|) (WORD PEAK$CROWN$CREST$TOP$TIP$SUMMIT |crest|) (WORD PEAK$CROWN$CREST$TOP$TIP$SUMMIT |top|) (WORD PEAK$CROWN$CREST$TOP$TIP$SUMMIT |tip|) (WORD PEAK$CROWN$CREST$TOP$TIP$SUMMIT |summit|))) (DEFCONCEPT RIGHT_3 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT RIGHT_3 LOCATIONS) (DOCUMENTATION RIGHT_3 "location near or direction toward the right side; i.e. the side to the south when a person or object faces east: ’he stood on the right’") (HAS-I-TOPIC RIGHT_3 |Factotum|) (WORD RIGHT_3 |right|))) (DEFCONCEPT SCOUR (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT SCOUR LOCATIONS) (DOCUMENTATION SCOUR "a place that is scoured (especially by running water)") (HAS-I-TOPIC SCOUR |Factotum|) (WORD SCOUR |scour|))) (DEFCONCEPT SUNSPOT$MACULA (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT SUNSPOT$MACULA PHENOMENA) (DOCUMENTATION SUNSPOT$MACULA "a cooler darker spot appearing periodically on the surface of the sun; associated with a strong magnetic field") (HAS-I-TOPIC SUNSPOT$MACULA |Factotum|) (WORD SUNSPOT$MACULA |sunspot|) (WORD SUNSPOT$MACULA |macula|))) (DEFCONCEPT MARE$MARIA (?SELF) :=> (GEOGRAPHICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT MARE$MARIA OBJECTS) (DOCUMENTATION MARE$MARIA "a dark region of considerable extent on the surface of the moon") (HAS-I-TOPIC MARE$MARIA |Factotum|) (WORD MARE$MARIA |mare|) (WORD MARE$MARIA |maria|))) (DEFCONCEPT TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$ MANDATE$COLONY (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY POSSESSION)

274

(DOCUMENTATION TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY "a territorial possession controlled by a ruling state") (HAS-I-TOPIC TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |Factotum|) (WORD TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |territory|) (WORD TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |dominion|) (WORD TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |territorial_dominion|) (WORD TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |province|) (WORD TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |mandate|) (WORD TERRITORY$DOMINION$TERRITORIAL_DOMINION$PROVINCE$MANDATE$COLONY |colony|))) (DEFCONCEPT CLASSIFICATION$CATEGORIZATION (?SELF) :=> (INFORMATION-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CLASSIFICATION$CATEGORIZATION GROUPS) (DOCUMENTATION CLASSIFICATION$CATEGORIZATION "a group of people or things arranged by class or category") (HAS-I-TOPIC CLASSIFICATION$CATEGORIZATION |Factotum|) (WORD CLASSIFICATION$CATEGORIZATION |classification|) (WORD CLASSIFICATION$CATEGORIZATION |categorization|))) (DEFCONCEPT AUDITORY_COMMUNICATION (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT AUDITORY_COMMUNICATION COMMUNICATION) (DOCUMENTATION AUDITORY_COMMUNICATION "communication that relies on hearing") (HAS-I-TOPIC AUDITORY_COMMUNICATION |Factotum|) (WORD AUDITORY_COMMUNICATION |auditory communication|))) (DEFCONCEPT SIGN_1 (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT SIGN_1 COMMUNICATION) (DOCUMENTATION SIGN_1 "a public display of a (usually written) message; ’he posted signs in all the shop windows’") (HAS-I-TOPIC SIGN_1 |Factotum|) (WORD SIGN_1 |sign|))) (DEFCONCEPT SIGNAL$SIGNALING$SIGN (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT SIGNAL$SIGNALING$SIGN COMMUNICATION) (DOCUMENTATION SIGNAL$SIGNALING$SIGN "any communication that encodes a message; ’signals from the boat sudddenly stopped’") (HAS-I-TOPIC SIGNAL$SIGNALING$SIGN |Factotum|) (WORD SIGNAL$SIGNALING$SIGN |signal|) (WORD SIGNAL$SIGNALING$SIGN |signaling|) (WORD SIGNAL$SIGNALING$SIGN |sign|))) (DEFCONCEPT VISUAL_COMMUNICATION (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT VISUAL_COMMUNICATION COMMUNICATION) (DOCUMENTATION VISUAL_COMMUNICATION "communication that relies on vision") (HAS-I-TOPIC VISUAL_COMMUNICATION |Factotum|) (WORD VISUAL_COMMUNICATION |visual communication|))) (DEFCONCEPT WRITTEN_COMMUNICATION$WRITTEN_LANGUAGE (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT WRITTEN_COMMUNICATION$WRITTEN_LANGUAGE COMMUNICATION) (DOCUMENTATION WRITTEN_COMMUNICATION$WRITTEN_LANGUAGE "communication by means of written symbols") (HAS-I-TOPIC WRITTEN_COMMUNICATION$WRITTEN_LANGUAGE |Factotum|) (WORD WRITTEN_COMMUNICATION$WRITTEN_LANGUAGE

275

|written communication|) (WORD WRITTEN_COMMUNICATION$WRITTEN_LANGUAGE |written language|))) (DEFCONCEPT OWN_RIGHT (?SELF) :=> (LEGAL-POSSESSION-ENTITY ?SELF) :AXIOMS (AND (SUBJECT OWN_RIGHT POSSESSION) (DOCUMENTATION OWN_RIGHT "by title vested in oneself or by virtue of qualifications one has achieved; ’a peer of the realm in his own right’; ’a leading sports figure in his own right’; ’a fine opera in its own right’") (HAS-I-TOPIC OWN_RIGHT |Factotum|) (WORD OWN_RIGHT |own_right|))) (DEFCONCEPT ADDRESS_3 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT ADDRESS_3 LOCATIONS) (DOCUMENTATION ADDRESS_3 "the place where a person or organization can be found or communicated with") (HAS-I-TOPIC ADDRESS_3 |Factotum|) (WORD ADDRESS_3 |address|))) (DEFCONCEPT BASE$HOME (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT BASE$HOME LOCATIONS) (DOCUMENTATION BASE$HOME "the place where you are stationed and from which missions start and end") (HAS-I-TOPIC BASE$HOME |Factotum|) (WORD BASE$HOME |base|) (WORD BASE$HOME |home|))) (DEFCONCEPT BEGINNING$ORIGIN$ROOT$SOURCE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT BEGINNING$ORIGIN$ROOT$SOURCE LOCATIONS) (DOCUMENTATION BEGINNING$ORIGIN$ROOT$SOURCE "the place where something begins, where it springs into being; ’the Italian beginning of the Renaissance’; ’Jupiter was the origin of the radiation’; ’Pittsburgh is the source of the Ohio River’; ’communism’s Russian root’") (HAS-I-TOPIC BEGINNING$ORIGIN$ROOT$SOURCE |Factotum|) (WORD BEGINNING$ORIGIN$ROOT$SOURCE |beginning|) (WORD BEGINNING$ORIGIN$ROOT$SOURCE |origin|) (WORD BEGINNING$ORIGIN$ROOT$SOURCE |root|) (WORD BEGINNING$ORIGIN$ROOT$SOURCE |source|))) (DEFCONCEPT BIRTHPLACE$PLACE_OF_BIRTH (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT BIRTHPLACE$PLACE_OF_BIRTH LOCATIONS) (DOCUMENTATION BIRTHPLACE$PLACE_OF_BIRTH "the place where someone was born") (HAS-I-TOPIC BIRTHPLACE$PLACE_OF_BIRTH |Factotum|) (WORD BIRTHPLACE$PLACE_OF_BIRTH |birthplace|) (WORD BIRTHPLACE$PLACE_OF_BIRTH |place_of_birth|))) (DEFCONCEPT BLACK_HOLE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT BLACK_HOLE OBJECTS) (DOCUMENTATION BLACK_HOLE "a region of space resulting from the collapse of a star; extremely high gravitational field") (HAS-I-TOPIC BLACK_HOLE |Factotum|) (WORD BLACK_HOLE |black_hole|))) (DEFCONCEPT DESTINATION$GOAL (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT DESTINATION$GOAL LOCATIONS) (DOCUMENTATION DESTINATION$GOAL "place where something (e.g., a journey or race) ends") (HAS-I-TOPIC DESTINATION$GOAL |Factotum|) (WORD DESTINATION$GOAL |destination|) (WORD DESTINATION$GOAL |goal|))) (DEFCONCEPT DISTANCE_2 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT DISTANCE_2 LOCATIONS) (DOCUMENTATION DISTANCE_2 "a distant region; ’I could see it in the distance’") (HAS-I-TOPIC DISTANCE_2 |Factotum|) (WORD DISTANCE_2 |distance|))) (DEFCONCEPT EARTH_1 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT EARTH_1 LOCATIONS) (DOCUMENTATION EARTH_1 "the abode of mortals (as contrasted with heaven or hell); ’it was hell on earth’") (HAS-I-TOPIC EARTH_1 |Factotum|) (WORD EARTH_1 |Earth|)))

276

(DEFCONCEPT EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA LOCATIONS) (DOCUMENTATION EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$ SHANGRI-LA "any place of complete bliss and delight and peace") (HAS-I-TOPIC EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |Factotum|) (WORD EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |eden|) (WORD EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |paradise|) (WORD EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |nirvana|) (WORD EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |heaven|) (WORD EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |promised_land|) (WORD EDEN$PARADISE$NIRVANA$HEAVEN$PROMISED_LAND$SHANGRI-LA |Shangri-la|))) (DEFCONCEPT FIELD_5 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT FIELD_5 LOCATIONS) (DOCUMENTATION FIELD_5 "somewhere (away from a studio or office or library or laboratory) where practical work is done or data is collected; ’anthropologists do much of their work in the field’") (HAS-I-TOPIC FIELD_5 |Factotum|) (WORD FIELD_5 |field|))) (DEFCONCEPT HALF-MAST (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT HALF-MAST LOCATIONS) (DOCUMENTATION HALF-MAST "a position some distance below the top of the mast to which a flag is lowered in mourning or to signal distress") (HAS-I-TOPIC HALF-MAST |Factotum|) (WORD HALF-MAST |half-mast|))) (DEFCONCEPT HELL$HELL_ON_EARTH$THE_PITS$INFERNO (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT HELL$HELL_ON_EARTH$THE_PITS$INFERNO LOCATIONS) (DOCUMENTATION HELL$HELL_ON_EARTH$THE_PITS$INFERNO "any place of pain and turmoil: ’the hell of battle’; ’the inferno of the engine room’; ’when you’re alone Christmas is the pits’;") (HAS-I-TOPIC HELL$HELL_ON_EARTH$THE_PITS$INFERNO |Factotum|) (WORD HELL$HELL_ON_EARTH$THE_PITS$INFERNO |hell|) (WORD HELL$HELL_ON_EARTH$THE_PITS$INFERNO |hell_on_earth|) (WORD HELL$HELL_ON_EARTH$THE_PITS$INFERNO |the_pits|) (WORD HELL$HELL_ON_EARTH$THE_PITS$INFERNO |inferno|))) (DEFCONCEPT HIDING_PLACE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT HIDING_PLACE LOCATIONS) (DOCUMENTATION HIDING_PLACE "a place suitable for hiding something (such as yourself)") (HAS-I-TOPIC HIDING_PLACE |Factotum|) (WORD HIDING_PLACE |hiding_place|))) (DEFCONCEPT HIGH$HEIGHTS (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT HIGH$HEIGHTS LOCATIONS) (DOCUMENTATION HIGH$HEIGHTS "a high place; ’they stood on high and observed the coutryside’ or ’he doesn’t like heights’") (HAS-I-TOPIC HIGH$HEIGHTS |Factotum|) (WORD HIGH$HEIGHTS |high|) (WORD HIGH$HEIGHTS |heights|))) (DEFCONCEPT HOME_1 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT HOME_1 LOCATIONS) (DOCUMENTATION HOME_1 "the country or state or city where you live; ’Canadian tariffs enabled United States lumber companies to raise prices at home’; ’his home is New Jersey’") (HAS-I-TOPIC HOME_1 |Factotum|) (WORD HOME_1 |home|))) (DEFCONCEPT LANDMARK_2 (?SELF)

277

:=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT LANDMARK_2 LOCATIONS) (DOCUMENTATION LANDMARK_2 "the position of a prominent or well-known object in a particular landscape; ’the church steeple provided a convenient landmark’") (HAS-I-TOPIC LANDMARK_2 |Factotum|) (WORD LANDMARK_2 |landmark|))) (DEFCONCEPT LIE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT LIE LOCATIONS) (DOCUMENTATION LIE "position or manner in which something is situated") (HAS-I-TOPIC LIE |Factotum|) (WORD LIE |lie|))) (DEFCONCEPT MECCA_1 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT MECCA_1 LOCATIONS) (DOCUMENTATION MECCA_1 "a place that attracts many visitors; ’New York is a mecca for young artists’") (HAS-I-TOPIC MECCA_1 |Factotum|) (WORD MECCA_1 |mecca|))) (DEFCONCEPT MIDAIR (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT MIDAIR LOCATIONS) (DOCUMENTATION MIDAIR "some point in the air; above ground level; ’the planes collided in midair’") (HAS-I-TOPIC MIDAIR |Factotum|) (WORD MIDAIR |midair|))) (DEFCONCEPT NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE STATES) (DOCUMENTATION NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE "a wild primitive state untouched by civilization; ’he lived in the wild’; ’they tried to preserve nature as they found it’") (HAS-I-TOPIC NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE |Factotum|) (WORD NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE |nature|) (WORD NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE |wild|) (WORD NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE |natural_state|) (WORD NATURE$WILD$NATURAL_STATE$STATE_OF_NATURE |state_of_nature|))) (DEFCONCEPT NEIGHBOR$NEIGHBOUR_1 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT NEIGHBOR$NEIGHBOUR_1 OBJECTS) (DOCUMENTATION NEIGHBOR$NEIGHBOUR_1 "a nearby object of the same kind; ’Fort Worth is a neighbor of Dallas’; ’what is the closest neighbor to the Earth?’") (HAS-I-TOPIC NEIGHBOR$NEIGHBOUR_1 |Factotum|) (WORD NEIGHBOR$NEIGHBOUR_1 |neighbor|) (WORD NEIGHBOR$NEIGHBOUR_1 |neighbour|))) (DEFCONCEPT NESTING_PLACE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT NESTING_PLACE LOCATIONS) (DOCUMENTATION NESTING_PLACE "a place suitable for nesting") (HAS-I-TOPIC NESTING_PLACE |Factotum|) (WORD NESTING_PLACE |nesting_place|))) (DEFCONCEPT OVERLOOK (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT OVERLOOK LOCATIONS) (DOCUMENTATION OVERLOOK "a high place affording a good view") (HAS-I-TOPIC OVERLOOK |Factotum|) (WORD OVERLOOK |overlook|))) (DEFCONCEPT PITCH_3 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT PITCH_3 LOCATIONS) (DOCUMENTATION PITCH_3 "(British) a vendor’s position (especially on the sidewalk); ’he was employed to see that his paper’s news pitches were not trespassed upon by rival vendors’") (HAS-I-TOPIC PITCH_3 |Factotum|) (WORD PITCH_3 |pitch|))) (DEFCONCEPT POLLING_PLACE$POLLING_STATION (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT POLLING_PLACE$POLLING_STATION LOCATIONS) (DOCUMENTATION POLLING_PLACE$POLLING_STATION "a place where voters go to cast their votes in an election") (HAS-I-TOPIC POLLING_PLACE$POLLING_STATION |Factotum|)

278

(WORD POLLING_PLACE$POLLING_STATION |polling_place|) (WORD POLLING_PLACE$POLLING_STATION |polling_station|))) (DEFCONCEPT POOL$PUDDLE_1 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT POOL$PUDDLE_1 LOCATIONS) (DOCUMENTATION POOL$PUDDLE_1 "something resembling a pool of liquid; ’he stood in a pool of light’; ’his chair sat in a puddle of books and magazines’") (HAS-I-TOPIC POOL$PUDDLE_1 |Factotum|) (WORD POOL$PUDDLE_1 |pool|) (WORD POOL$PUDDLE_1 |puddle|))) (DEFCONCEPT POSITION_2 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT POSITION_2 LOCATIONS) (DOCUMENTATION POSITION_2 "the appropriate or customary location; ’the cars were in position’") (HAS-I-TOPIC POSITION_2 |Factotum|) (WORD POSITION_2 |position|))) (DEFCONCEPT POST$STATION (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT POST$STATION LOCATIONS) (DOCUMENTATION POST$STATION "the position where something or someone (as a guard or sentry) stands or is assigned to stand: ’a sentry station’") (HAS-I-TOPIC POST$STATION |Factotum|) (WORD POST$STATION |post|) (WORD POST$STATION |station|))) (DEFCONCEPT RENDEZVOUS_2 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT RENDEZVOUS_2 LOCATIONS) (DOCUMENTATION RENDEZVOUS_2 "a place where people meet; ’he was waiting for them at the rendezvous’") (HAS-I-TOPIC RENDEZVOUS_2 |Factotum|) (WORD RENDEZVOUS_2 |rendezvous|))) (DEFCONCEPT SHOWPLACE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT SHOWPLACE LOCATIONS) (DOCUMENTATION SHOWPLACE "a place that is frequently exhibited and visited for its historical interest or natural beauty") (HAS-I-TOPIC SHOWPLACE |Factotum|) (WORD SHOWPLACE |showplace|))) (DEFCONCEPT SITE$LAND_SITE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT SITE$LAND_SITE LOCATIONS) (DOCUMENTATION SITE$LAND_SITE "the piece of land on which something is located (or is to be located): ’a good site for the school’") (HAS-I-TOPIC SITE$LAND_SITE |Factotum|) (WORD SITE$LAND_SITE |site|) (WORD SITE$LAND_SITE |land_site|))) (DEFCONCEPT SITE$SITUATION (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT SITE$SITUATION LOCATIONS) (DOCUMENTATION SITE$SITUATION "physical position in relation to the surroundings") (HAS-I-TOPIC SITE$SITUATION |Factotum|) (WORD SITE$SITUATION |site|) (WORD SITE$SITUATION |situation|))) (DEFCONCEPT SOLITUDE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT SOLITUDE LOCATIONS) (DOCUMENTATION SOLITUDE "a solitary place") (HAS-I-TOPIC SOLITUDE |Factotum|) (WORD SOLITUDE |solitude|))) (DEFCONCEPT STAND_5 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT STAND_5 LOCATIONS) (DOCUMENTATION STAND_5 "the position where a thing or person stands") (HAS-I-TOPIC STAND_5 |Factotum|) (WORD STAND_5 |stand|))) (DEFCONCEPT STOP_2 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT STOP_2 LOCATIONS) (DOCUMENTATION STOP_2 "a spot where something halts or pauses; ’his next stop is Atlanta’") (HAS-I-TOPIC STOP_2 |Factotum|) (WORD STOP_2 |stop|)))

279

(DEFCONCEPT TARGET$TARGET_AREA (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT TARGET$TARGET_AREA LOCATIONS) (DOCUMENTATION TARGET$TARGET_AREA "the location of the target that is to be hit") (HAS-I-TOPIC TARGET$TARGET_AREA |Factotum|) (WORD TARGET$TARGET_AREA |target|) (WORD TARGET$TARGET_AREA |target_area|))) (DEFCONCEPT VANISHING_POINT_2 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT VANISHING_POINT_2 LOCATIONS) (DOCUMENTATION VANISHING_POINT_2 "the point beyond which something disappears or ceases to exist") (HAS-I-TOPIC VANISHING_POINT_2 |Factotum|) (WORD VANISHING_POINT_2 |vanishing_point|))) (DEFCONCEPT VANTAGE (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT VANTAGE LOCATIONS) (DOCUMENTATION VANTAGE "place or situation affording some advantage (especially a comprehensive view or commanding perspective)") (HAS-I-TOPIC VANTAGE |Factotum|) (WORD VANTAGE |vantage|))) (DEFCONCEPT WORKPLACE$WORK (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT WORKPLACE$WORK ARTIFACTS) (DOCUMENTATION WORKPLACE$WORK "a place where work is done; ’he arrived at work early today’") (HAS-I-TOPIC WORKPLACE$WORK |Factotum|) (WORD WORKPLACE$WORK |workplace|) (WORD WORKPLACE$WORK |work|))) (DEFCONCEPT ZONE_1 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT ZONE_1 LOCATIONS) (DOCUMENTATION ZONE_1 "an area or region distinguished from adjacent parts by a distinctive feature or characteristic") (HAS-I-TOPIC ZONE_1 |Factotum|) (WORD ZONE_1 |zone|))) (DEFCONCEPT OLD_WIVES__TALE (?SELF) :=> (NARRATIVE ?SELF) :AXIOMS (AND (SUBJECT OLD_WIVES__TALE COGNITION) (DOCUMENTATION OLD_WIVES__TALE "a bit of lore passed on by word of mouth") (HAS-I-TOPIC OLD_WIVES__TALE |Factotum|) (WORD OLD_WIVES__TALE |old wives’ tale|))) (DEFCONCEPT COMMON_DENOMINATOR_1 (?SELF) :=> (PARAMETER ?SELF) :AXIOMS (AND (SUBJECT COMMON_DENOMINATOR_1 ATTRIBUTES) (DOCUMENTATION COMMON_DENOMINATOR_1 "an attribute that is common to all members of a category") (HAS-I-TOPIC COMMON_DENOMINATOR_1 |Factotum|) (WORD COMMON_DENOMINATOR_1 |common denominator|))) (DEFCONCEPT PARAMETER_2 (?SELF) :=> (PARAMETER ?SELF) :AXIOMS (AND (SUBJECT PARAMETER_2 EVENTS) (DOCUMENTATION PARAMETER_2 "any factor that defines a system and determines (or limits) its performance") (HAS-I-TOPIC PARAMETER_2 |Factotum|) (WORD PARAMETER_2 |parameter|))) (DEFCONCEPT ANTICIPATION (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ANTICIPATION OBJECTS) (DOCUMENTATION ANTICIPATION "some early entity whose type or style anticipates a later one; ’there were many anticipations of Darwinian theory’; ’the hour glass was an anticipation of the clock’") (HAS-I-TOPIC ANTICIPATION |Factotum|) (WORD ANTICIPATION |anticipation|))) (DEFCONCEPT CATCH_5 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT CATCH_5 OBJECTS) (DOCUMENTATION CATCH_5 "anything that is caught (especially if it is worth catching); ’he shared his catch with the others’")

280

(HAS-I-TOPIC CATCH_5 |Factotum|) (WORD CATCH_5 |catch|))) (DEFCONCEPT COAGULATION_FACTOR (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT COAGULATION_FACTOR SUBSTANCES) (DOCUMENTATION COAGULATION_FACTOR "any of the factors in the blood whose actions are essential for blood coagulation") (HAS-I-TOPIC COAGULATION_FACTOR |Factotum|) (WORD COAGULATION_FACTOR |coagulation_factor|))) (DEFCONCEPT DETAIL$PARTICULAR$ITEM (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT DETAIL$PARTICULAR$ITEM RELATIONS) (DOCUMENTATION DETAIL$PARTICULAR$ITEM "a small part that can be considered separately from the whole; ’it was perfect in all details’") (HAS-I-TOPIC DETAIL$PARTICULAR$ITEM |Factotum|) (WORD DETAIL$PARTICULAR$ITEM |detail|) (WORD DETAIL$PARTICULAR$ITEM |particular|) (WORD DETAIL$PARTICULAR$ITEM |item|))) (DEFCONCEPT DRAW$LOT (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT DRAW$LOT ARTIFACTS) (DOCUMENTATION DRAW$LOT "anything (straws or pebbles etc.) taken or chosen at random; ’the luck of the draw’ or ’they drew lots for it’") (HAS-I-TOPIC DRAW$LOT |Factotum|) (WORD DRAW$LOT |draw|) (WORD DRAW$LOT |lot|))) (DEFCONCEPT EQUIVALENT (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT EQUIVALENT COGNITION) (DOCUMENTATION EQUIVALENT "a person or thing equal to another in value or measure or force or effect or significance etc: ’send two dollars or the equivalent in stamps’") (HAS-I-TOPIC EQUIVALENT |Factotum|) (WORD EQUIVALENT |equivalent|))) (DEFCONCEPT FINDING_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT FINDING_2 OBJECTS) (DOCUMENTATION FINDING_2 "something that is found; ’the findings in the gastrointestinal tract indicate that he died several hours after dinner’; ’an area rich in archaelogical findings’") (HAS-I-TOPIC FINDING_2 |Factotum|) (WORD FINDING_2 |finding|))) (DEFCONCEPT GROWTH_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT GROWTH_2 OBJECTS) (DOCUMENTATION GROWTH_2 "something grown or growing; ’a growth of hair’") (HAS-I-TOPIC GROWTH_2 |Factotum|) (WORD GROWTH_2 |growth|))) (DEFCONCEPT INESSENTIAL$NONESSENTIAL (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT INESSENTIAL$NONESSENTIAL OBJECTS) (DOCUMENTATION INESSENTIAL$NONESSENTIAL "anything that is not essential; ’they discarded all their inessentials’") (HAS-I-TOPIC INESSENTIAL$NONESSENTIAL |Factotum|) (WORD INESSENTIAL$NONESSENTIAL |inessential|) (WORD INESSENTIAL$NONESSENTIAL |nonessential|))) (DEFCONCEPT ITEM (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ITEM ARTIFACTS) (DOCUMENTATION ITEM "an individual unit; especially when included in a list or collection; ’they reduced the price on many items’") (HAS-I-TOPIC ITEM |Factotum|) (WORD ITEM |item|))) (DEFCONCEPT ITEM$POINT (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ITEM$POINT COMMUNICATION) (DOCUMENTATION ITEM$POINT "a distinct part that can be specified separately in a group of things that could be enumerated on a list; ’he noticed an item in the New York Times’; ’she had several items on her shopping list’; ’the main point on the agenda was taken up first’") (HAS-I-TOPIC ITEM$POINT |Factotum|) (WORD ITEM$POINT |item|)

281

(WORD ITEM$POINT |point|))) (DEFCONCEPT KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY COGNITION) (DOCUMENTATION KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY "the choicest or most essential or most vital part of some idea or experience: ’the gist of the prosecutor’s argument’; ’the nub of the story’") (HAS-I-TOPIC KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |Factotum|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |kernel|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |substance|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |core|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |center|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |essence|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |gist|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |heart|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |inwardness|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |marrow|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |meat|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |nub|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |pith|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$

282

MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |sum|) (WORD KERNEL$SUBSTANCE$CORE$CENTER$ESSENCE$GIST$HEART$INWARDNESS$ MARROW$MEAT$NUB$PITH$SUM$NITTY-GRITTY |nitty-gritty|))) (DEFCONCEPT MEMBER_3 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT MEMBER_3 RELATIONS) (DOCUMENTATION MEMBER_3 "anything that belongs to a set or class: ’snakes are members of the class Reptilia’; ’members of the opposite sex’") (HAS-I-TOPIC MEMBER_3 |Factotum|) (WORD MEMBER_3 |member|))) (DEFCONCEPT NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY OBJECTS) (DOCUMENTATION NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY "anything indispensable; ’food and shelter are necessities of life’; ’the essentials of the good life’; ’allow farmers to buy their requirements under favorable conditions’; ’a place where the requisites of water fuel and fodder can be obtained’") (HAS-I-TOPIC NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY |Factotum|) (WORD NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY |necessity|) (WORD NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY |essential|) (WORD NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY |requirement|) (WORD NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY |requisite|) (WORD NECESSITY$ESSENTIAL$REQUIREMENT$REQUISITE$NECESSARY |necessary|))) (DEFCONCEPT OBJECT_1 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT OBJECT_1 COGNITION) (DOCUMENTATION OBJECT_1 "the focus of cognitions or feelings; ’objects of thought’; ’the object of my affection’") (HAS-I-TOPIC OBJECT_1 |Factotum|) (WORD OBJECT_1 |object|))) (DEFCONCEPT PARING$PARINGS (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT PARING$PARINGS FOOD) (DOCUMENTATION PARING$PARINGS "a part that is pared or cut off; especially skin or peel") (HAS-I-TOPIC PARING$PARINGS |Factotum|) (WORD PARING$PARINGS |paring|) (WORD PARING$PARINGS |parings|))) (DEFCONCEPT PLACE_1 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT PLACE_1 COGNITION) (DOCUMENTATION PLACE_1 "an abstract mental location; ’he has a special place in my thoughts’; ’a place in my heart’; ’a political system with no place for the less prominent groups’") (HAS-I-TOPIC PLACE_1 |Factotum|) (WORD PLACE_1 |place|))) (DEFCONCEPT PLACE_5 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT PLACE_5 STATES) (DOCUMENTATION PLACE_5 "proper or appropriate position or location; ’a woman’s place is no longer in the kitchen’") (HAS-I-TOPIC PLACE_5 |Factotum|) (WORD PLACE_5 |place|))) (DEFCONCEPT REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST RELATIONS) (DOCUMENTATION REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST "something left after other parts have been taken away; ’there was no remainder’; ’he threw away the rest’") (HAS-I-TOPIC REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST |Factotum|) (WORD REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST |remainder|)

283

(WORD REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST |residual|) (WORD REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST |residue|) (WORD REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST |residuum|) (WORD REMAINDER$RESIDUAL$RESIDUE$RESIDUUM$REST |rest|))) (DEFCONCEPT REMAINS (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT REMAINS OBJECTS) (DOCUMENTATION REMAINS "any object that is left unused or still extant; ’I threw out the remains of my dinner’") (HAS-I-TOPIC REMAINS |Factotum|) (WORD REMAINS |remains|))) (DEFCONCEPT RIBBON$THREAD (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT RIBBON$THREAD OBJECTS) (DOCUMENTATION RIBBON$THREAD "any long object resembling a thin line; ’a mere ribbon of land’; ’the lighted ribbon of traffic’; ’from the air the road was a gray thread’; ’a thread of smoke climbed upward’") (HAS-I-TOPIC RIBBON$THREAD |Factotum|) (WORD RIBBON$THREAD |ribbon|) (WORD RIBBON$THREAD |thread|))) (DEFCONCEPT SUBPART (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SUBPART RELATIONS) (DOCUMENTATION SUBPART "a part of a part") (HAS-I-TOPIC SUBPART |Factotum|) (WORD SUBPART |subpart|))) (DEFCONCEPT TEACHER (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT TEACHER COGNITION) (DOCUMENTATION TEACHER "a personified abstraction that teaches; ’books were his teachers’ or ’experience is a demanding teacher’") (HAS-I-TOPIC TEACHER |Factotum|) (WORD TEACHER |teacher|))) (DEFCONCEPT THEOREM_1 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT THEOREM_1 COGNITION) (DOCUMENTATION THEOREM_1 "an idea accepted as a demonstrable truth") (HAS-I-TOPIC THEOREM_1 |Factotum|) (WORD THEOREM_1 |theorem|))) (DEFCONCEPT THING_3 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT THING_3 ARTIFACTS) (DOCUMENTATION THING_3 "an entity that is not named specifically; ’I couldn’t tell what the thing was’") (HAS-I-TOPIC THING_3 |Factotum|) (WORD THING_3 |thing|))) (DEFCONCEPT THING_5 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT THING_5 COGNITION) (DOCUMENTATION THING_5 "a special abstraction; ’a thing of the spirit’; ’things of the heart’") (HAS-I-TOPIC THING_5 |Factotum|) (WORD THING_5 |thing|))) (DEFCONCEPT TRANSFERRED_PROPERTY$TRANSFERRED_POSSESSION (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT TRANSFERRED_PROPERTY$ TRANSFERRED_POSSESSION POSSESSION) (DOCUMENTATION TRANSFERRED_PROPERTY$TRANSFERRED_POSSESSION "a possession whose ownership changes or lapses") (HAS-I-TOPIC TRANSFERRED_PROPERTY$TRANSFERRED_POSSESSION |Factotum|) (WORD TRANSFERRED_PROPERTY$TRANSFERRED_POSSESSION |transferred_property|) (WORD TRANSFERRED_PROPERTY$TRANSFERRED_POSSESSION |transferred_possession|))) (DEFCONCEPT TREASURE_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT TREASURE_2 POSSESSION) (DOCUMENTATION TREASURE_2 "any possession that is highly valued by its owner; ’the children returned from the seashore with their shells and other treasures’") (HAS-I-TOPIC TREASURE_2 |Factotum|) (WORD TREASURE_2 |treasure|))) (DEFCONCEPT UNIT_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF)

284

:AXIOMS (AND (SUBJECT UNIT_2 RELATIONS) (DOCUMENTATION UNIT_2 "an individual or group or structure or other entity regarded as a structural or functional constituent of a whole; ’the reduced the number of units and installations’; ’the word is a basic linguistic unit’") (HAS-I-TOPIC UNIT_2 |Factotum|) (WORD UNIT_2 |unit|))) (DEFCONCEPT UNKNOWN_QUANTITY (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT UNKNOWN_QUANTITY EVENTS) (DOCUMENTATION UNKNOWN_QUANTITY "a factor in a given situation whose bearing and importance is not apparent; ’I don’t know what the new man will do; he’s still an unknown quantity’") (HAS-I-TOPIC UNKNOWN_QUANTITY |Factotum|) (WORD UNKNOWN_QUANTITY |unknown quantity|))) (DEFCONCEPT VAGABOND_1 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT VAGABOND_1 OBJECTS) (DOCUMENTATION VAGABOND_1 "anything that resembles a vagabond in having no fixed place; ’pirate ships were vagabonds of the sea’") (HAS-I-TOPIC VAGABOND_1 |Factotum|) (WORD VAGABOND_1 |vagabond|))) (DEFCONCEPT VARIABLE_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT VARIABLE_2 OBJECTS) (DOCUMENTATION VARIABLE_2 "something that is likely to vary; something that is subject to variation; ’the weather is one variable to be considered’") (HAS-I-TOPIC VARIABLE_2 |Factotum|) (WORD VARIABLE_2 |variable|))) (DEFCONCEPT WALL_3 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT WALL_3 OBJECTS) (DOCUMENTATION WALL_3 "anything that suggests a wall in structure or effect; ’a wall of water’; ’a wall of smoke’; ’a wall of prejudice’") (HAS-I-TOPIC WALL_3 |Factotum|) (WORD WALL_3 |wall|))) (DEFCONCEPT WHITE_ELEPHANT_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT WHITE_ELEPHANT_2 POSSESSION) (DOCUMENTATION WHITE_ELEPHANT_2 "a valuable possession whole upkeep is expensive") (HAS-I-TOPIC WHITE_ELEPHANT_2 |Factotum|) (WORD WHITE_ELEPHANT_2 |white_elephant|))) (DEFCONCEPT WHOLE (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT WHOLE COGNITION) (DOCUMENTATION WHOLE "all of something including all its component elements or parts; ’Europe as a whole’; ’the whole of American literature’") (HAS-I-TOPIC WHOLE |Factotum|) (WORD WHOLE |whole|))) (DEFCONCEPT ANGULAR_SHAPE$ANGULARITY (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT ANGULAR_SHAPE$ANGULARITY SHAPES) (DOCUMENTATION ANGULAR_SHAPE$ANGULARITY "a shape having one or more sharp angles") (HAS-I-TOPIC ANGULAR_SHAPE$ANGULARITY |Factotum|) (WORD ANGULAR_SHAPE$ANGULARITY |angular_shape|) (WORD ANGULAR_SHAPE$ANGULARITY |angularity|))) (DEFCONCEPT BLOB (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT BLOB SHAPES) (DOCUMENTATION BLOB "an indistinct shapeless form") (HAS-I-TOPIC BLOB |Factotum|) (WORD BLOB |blob|))) (DEFCONCEPT CIRCLE_2 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT CIRCLE_2 SHAPES) (DOCUMENTATION CIRCLE_2 "something approximating the shape of a circle; ’the chairs were arranged in a circle’") (HAS-I-TOPIC CIRCLE_2 |Factotum|) (WORD CIRCLE_2 |circle|)))

285

(DEFCONCEPT COLUMN$TOWER$PILLAR (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT COLUMN$TOWER$PILLAR SHAPES) (DOCUMENTATION COLUMN$TOWER$PILLAR "anything tall and thin approximating the shape of a column or tower; ’the test tube held a column of white powder’; ’a tower of dust rose above the horizon’; ’a thin pillar of smoke betrayed their campsite’") (HAS-I-TOPIC COLUMN$TOWER$PILLAR |Factotum|) (WORD COLUMN$TOWER$PILLAR |column|) (WORD COLUMN$TOWER$PILLAR |tower|) (WORD COLUMN$TOWER$PILLAR |pillar|))) (DEFCONCEPT CURVE (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT CURVE COMMUNICATION) (DOCUMENTATION CURVE "a line on a graph representing data") (HAS-I-TOPIC CURVE |Factotum|) (WORD CURVE |curve|))) (DEFCONCEPT DISTORTED_SHAPE$DISTORTION (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT DISTORTED_SHAPE$DISTORTION SHAPES) (DOCUMENTATION DISTORTED_SHAPE$DISTORTION "a shape resulting from distortion") (HAS-I-TOPIC DISTORTED_SHAPE$DISTORTION |Factotum|) (WORD DISTORTED_SHAPE$DISTORTION |distorted_shape|) (WORD DISTORTED_SHAPE$DISTORTION |distortion|))) (DEFCONCEPT FIGURE_6 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT FIGURE_6 SHAPES) (DOCUMENTATION FIGURE_6 "a combination of points and lines and planes that form a visible palpable shape") (HAS-I-TOPIC FIGURE_6 |Factotum|) (WORD FIGURE_6 |figure|))) (DEFCONCEPT FLARE_2 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT FLARE_2 SHAPES) (DOCUMENTATION FLARE_2 "a shape that spreads outward; ’the skirt had a wide flare’") (HAS-I-TOPIC FLARE_2 |Factotum|) (WORD FLARE_2 |flare|))) (DEFCONCEPT INHERITANCE$HERITAGE_2 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT INHERITANCE$HERITAGE_2 ATTRIBUTES) (DOCUMENTATION INHERITANCE$HERITAGE_2 "any attribute that passes from parent to offspring") (HAS-I-TOPIC INHERITANCE$HERITAGE_2 |Factotum|) (WORD INHERITANCE$HERITAGE_2 |inheritance|) (WORD INHERITANCE$HERITAGE_2 |heritage|))) (DEFCONCEPT MOON_1 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT MOON_1 OBJECTS) (DOCUMENTATION MOON_1 "any object resembling a moon; ’he made a moon lamp that he used as a night light’; ’the clock had a moon that showed various phases’") (HAS-I-TOPIC MOON_1 |Factotum|) (WORD MOON_1 |moon|))) (DEFCONCEPT PERSONALITY_1 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT PERSONALITY_1 ATTRIBUTES) (DOCUMENTATION PERSONALITY_1 "the complex of all the attributes--behavioral, temperamental, emotional and mental --that characterize a unique individual; ’their different reactions reflected their very different personalities’; ’it is his nature to help others’") (HAS-I-TOPIC PERSONALITY_1 |Factotum|) (WORD PERSONALITY_1 |personality|))) (DEFCONCEPT QUALITY_1 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT QUALITY_1 ATTRIBUTES) (DOCUMENTATION QUALITY_1 "an essential and distinguishing attribute of something or someone; ’the quality of mercy is not strained’--Shakespeare") (HAS-I-TOPIC QUALITY_1 |Factotum|) (WORD QUALITY_1 |quality|))) (DEFCONCEPT ROUND_SHAPE (?SELF)

286

:=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT ROUND_SHAPE SHAPES) (DOCUMENTATION ROUND_SHAPE "a shape that is curved and without sharp angles") (HAS-I-TOPIC ROUND_SHAPE |Factotum|) (WORD ROUND_SHAPE |round_shape|))) (DEFCONCEPT SHAPELESSNESS_2 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT SHAPELESSNESS_2 SHAPES) (DOCUMENTATION SHAPELESSNESS_2 "an amorphous or indefinite shape; ’a shapeless mass’") (HAS-I-TOPIC SHAPELESSNESS_2 |Factotum|) (WORD SHAPELESSNESS_2 |shapelessness|))) (DEFCONCEPT SOLID_1 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT SOLID_1 SHAPES) (DOCUMENTATION SOLID_1 "a three-dimensional shape") (HAS-I-TOPIC SOLID_1 |Factotum|) (WORD SOLID_1 |solid|))) (DEFCONCEPT THING_4 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT THING_4 ATTRIBUTES) (DOCUMENTATION THING_4 "any attribute or quality considered as having its own existence: ’the thing I like about her is ...’") (HAS-I-TOPIC THING_4 |Factotum|) (WORD THING_4 |thing|))) (DEFCONCEPT TRAIT (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT TRAIT ATTRIBUTES) (DOCUMENTATION TRAIT "a distinguishing feature of one’s personal nature") (HAS-I-TOPIC TRAIT |Factotum|) (WORD TRAIT |trait|))) (DEFCONCEPT WEB_3 (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT WEB_3 OBJECTS) (DOCUMENTATION WEB_3 "an intricate network suggesting something that was formed by weaving or interweaving; ’the trees cast a delicate web of shadows over the lawn’") (HAS-I-TOPIC WEB_3 |Factotum|) (WORD WEB_3 |web|))) (DEFCONCEPT BALDNESS$HAIRLESSNESS$PHALACROSIS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT BALDNESS$HAIRLESSNESS$PHALACROSIS STATES) (DOCUMENTATION BALDNESS$HAIRLESSNESS$PHALACROSIS "the condition of having no hair (especially on the top of the head)") (HAS-I-TOPIC BALDNESS$HAIRLESSNESS$PHALACROSIS |Factotum|) (WORD BALDNESS$HAIRLESSNESS$PHALACROSIS |baldness|) (WORD BALDNESS$HAIRLESSNESS$PHALACROSIS |hairlessness|) (WORD BALDNESS$HAIRLESSNESS$PHALACROSIS |phalacrosis|))) (DEFCONCEPT CELIBACY (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT CELIBACY STATES) (DOCUMENTATION CELIBACY "an unmarried status (as because of religious vows)") (HAS-I-TOPIC CELIBACY |Factotum|) (WORD CELIBACY |celibacy|))) (DEFCONCEPT COMFORT$COMFORTABLENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT COMFORT$COMFORTABLENESS STATES) (DOCUMENTATION COMFORT$COMFORTABLENESS "a state of being relaxed and feeling no pain; ’he is a man who enjoys his comfort’; ’she longed for the comfortableness of her armchair’") (HAS-I-TOPIC COMFORT$COMFORTABLENESS |Factotum|) (WORD COMFORT$COMFORTABLENESS |comfort|) (WORD COMFORT$COMFORTABLENESS |comfortableness|))) (DEFCONCEPT CONDITION_WN (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT CONDITION_WN STATES) (DOCUMENTATION CONDITION_WN "a mode of being or form of existence of a person or things: ’the human condition’") (HAS-I-TOPIC CONDITION_WN |Factotum|) (WORD CONDITION_WN |condition|)))

287

(DEFCONCEPT DISCOMFORT$UNCOMFORTABLENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT DISCOMFORT$UNCOMFORTABLENESS STATES) (DOCUMENTATION DISCOMFORT$UNCOMFORTABLENESS "the state of being tense and feeling pain") (HAS-I-TOPIC DISCOMFORT$UNCOMFORTABLENESS |Factotum|) (WORD DISCOMFORT$UNCOMFORTABLENESS |discomfort|) (WORD DISCOMFORT$UNCOMFORTABLENESS |uncomfortableness|))) (DEFCONCEPT DRYNESS$WATERLESSNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT DRYNESS$WATERLESSNESS STATES) (DOCUMENTATION DRYNESS$WATERLESSNESS "the condition of not containing or being covered by a liquid (especially water)") (HAS-I-TOPIC DRYNESS$WATERLESSNESS |Factotum|) (WORD DRYNESS$WATERLESSNESS |dryness|) (WORD DRYNESS$WATERLESSNESS |waterlessness|))) (DEFCONCEPT EMPTINESS_2 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT EMPTINESS_2 STATES) (DOCUMENTATION EMPTINESS_2 "the state of containing nothing") (HAS-I-TOPIC EMPTINESS_2 |Factotum|) (WORD EMPTINESS_2 |emptiness|))) (DEFCONCEPT ENNOBLEMENT_2 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT ENNOBLEMENT_2 STATES) (DOCUMENTATION ENNOBLEMENT_2 "the state of being noble") (HAS-I-TOPIC ENNOBLEMENT_2 |Factotum|) (WORD ENNOBLEMENT_2 |ennoblement|))) (DEFCONCEPT FULLNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT FULLNESS STATES) (DOCUMENTATION FULLNESS "the condition of being filled to capacity") (HAS-I-TOPIC FULLNESS |Factotum|) (WORD FULLNESS |fullness|))) (DEFCONCEPT GUILT$GUILTINESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT GUILT$GUILTINESS STATES) (DOCUMENTATION GUILT$GUILTINESS "the state of having committed an offense") (HAS-I-TOPIC GUILT$GUILTINESS |Factotum|) (WORD GUILT$GUILTINESS |guilt|) (WORD GUILT$GUILTINESS |guiltiness|))) (DEFCONCEPT HOPEFULNESS_2 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT HOPEFULNESS_2 STATES) (DOCUMENTATION HOPEFULNESS_2 "full of hope") (HAS-I-TOPIC HOPEFULNESS_2 |Factotum|) (WORD HOPEFULNESS_2 |hopefulness|))) (DEFCONCEPT ILLUMINATION (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT ILLUMINATION STATES) (DOCUMENTATION ILLUMINATION "the degree of visibility of your environment") (HAS-I-TOPIC ILLUMINATION |Factotum|) (WORD ILLUMINATION |illumination|))) (DEFCONCEPT IMMATURITY$IMMATURENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT IMMATURITY$IMMATURENESS STATES) (DOCUMENTATION IMMATURITY$IMMATURENESS "not having reached maturity") (HAS-I-TOPIC IMMATURITY$IMMATURENESS |Factotum|) (WORD IMMATURITY$IMMATURENESS |immaturity|) (WORD IMMATURITY$IMMATURENESS |immatureness|))) (DEFCONCEPT IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS STATES) (DOCUMENTATION IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS "the state of being imminent and liable to happen soon")

288

(HAS-I-TOPIC IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS |Factotum|) (WORD IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS |imminence|) (WORD IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS |imminency|) (WORD IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS |impendence|) (WORD IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS |impendency|) (WORD IMMINENCE$IMMINENCY$IMPENDENCE$IMPENDENCY$FORTHCOMINGNESS |forthcomingness|))) (DEFCONCEPT IMPERFECTION$IMPERFECTNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT IMPERFECTION$IMPERFECTNESS STATES) (DOCUMENTATION IMPERFECTION$IMPERFECTNESS "the state or an instance of being imperfect") (HAS-I-TOPIC IMPERFECTION$IMPERFECTNESS |Factotum|) (WORD IMPERFECTION$IMPERFECTNESS |imperfection|) (WORD IMPERFECTION$IMPERFECTNESS |imperfectness|))) (DEFCONCEPT IMPURITY$IMPURENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT IMPURITY$IMPURENESS STATES) (DOCUMENTATION IMPURITY$IMPURENESS "the condition of being impure") (HAS-I-TOPIC IMPURITY$IMPURENESS |Factotum|) (WORD IMPURITY$IMPURENESS |impurity|) (WORD IMPURITY$IMPURENESS |impureness|))) (DEFCONCEPT INNOCENCE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT INNOCENCE STATES) (DOCUMENTATION INNOCENCE "a state or condition of being innocent of a specific crime or offense; ’the trial established his innocence’") (HAS-I-TOPIC INNOCENCE |Factotum|) (WORD INNOCENCE |innocence|))) (DEFCONCEPT INTEGRITY$UNITY$WHOLENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT INTEGRITY$UNITY$WHOLENESS STATES) (DOCUMENTATION INTEGRITY$UNITY$WHOLENESS "an unreduced or unbroken completeness or totality") (HAS-I-TOPIC INTEGRITY$UNITY$WHOLENESS |Factotum|) (WORD INTEGRITY$UNITY$WHOLENESS |integrity|) (WORD INTEGRITY$UNITY$WHOLENESS |unity|) (WORD INTEGRITY$UNITY$WHOLENESS |wholeness|))) (DEFCONCEPT MATURITY$MATURENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT MATURITY$MATURENESS STATES) (DOCUMENTATION MATURITY$MATURENESS "state of being mature; full development") (HAS-I-TOPIC MATURITY$MATURENESS |Factotum|) (WORD MATURITY$MATURENESS |maturity|) (WORD MATURITY$MATURENESS |matureness|))) (DEFCONCEPT NOISE_CONDITIONS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT NOISE_CONDITIONS STATES) (DOCUMENTATION NOISE_CONDITIONS "the condition of being noisy (as in a communication channel)") (HAS-I-TOPIC NOISE_CONDITIONS |Factotum|) (WORD NOISE_CONDITIONS |noise_conditions|))) (DEFCONCEPT PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA STATES) (DOCUMENTATION PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA "the state of being without a flaw or defect") (HAS-I-TOPIC PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA |Factotum|) (WORD PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA |perfection|) (WORD PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA |flawlessness|) (WORD PERFECTION$FLAWLESSNESS$NE_PLUS_ULTRA |ne_plus_ultra|)))

289

(DEFCONCEPT POLARIZATION (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT POLARIZATION STATES) (DOCUMENTATION POLARIZATION "the condition of having or giving polarity") (HAS-I-TOPIC POLARIZATION |Factotum|) (WORD POLARIZATION |polarization|))) (DEFCONCEPT PROPERTY_WN (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT PROPERTY_WN ATTRIBUTES) (DOCUMENTATION PROPERTY_WN "a basic or essential attribute shared by all members of a class; ’a study of the physical properties of atomic particles’") (HAS-I-TOPIC PROPERTY_WN |Factotum|) (WORD PROPERTY_WN |property|))) (DEFCONCEPT PURITY$PURENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT PURITY$PURENESS STATES) (DOCUMENTATION PURITY$PURENESS "being undiluted or unmixed with extraneous material") (HAS-I-TOPIC PURITY$PURENESS |Factotum|) (WORD PURITY$PURENESS |purity|) (WORD PURITY$PURENESS |pureness|))) (DEFCONCEPT PURITY$SINLESSNESS$INNOCENCE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT PURITY$SINLESSNESS$INNOCENCE STATES) (DOCUMENTATION PURITY$SINLESSNESS$INNOCENCE "the state of being free from sin or moral wrong; lacking a knowledge of evil") (HAS-I-TOPIC PURITY$SINLESSNESS$INNOCENCE |Factotum|) (WORD PURITY$SINLESSNESS$INNOCENCE |purity|) (WORD PURITY$SINLESSNESS$INNOCENCE |sinlessness|) (WORD PURITY$SINLESSNESS$INNOCENCE |innocence|))) (DEFCONCEPT READING$METER_READING_2 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT READING$METER_READING_2 COGNITION) (DOCUMENTATION READING$METER_READING_2 "the data presented to a user by a meter or similar instrument; ’he could not believe the meter reading’") (HAS-I-TOPIC READING$METER_READING_2 |Factotum|) (WORD READING$METER_READING_2 |reading|) (WORD READING$METER_READING_2 |meter reading|))) (DEFCONCEPT SILENCE (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SILENCE STATES) (DOCUMENTATION SILENCE "the state of being silent (as when no one is speaking); ’there was a shocked silence’: ’he gestured for silence’") (HAS-I-TOPIC SILENCE |Factotum|) (WORD SILENCE |silence|))) (DEFCONCEPT SKILLFULNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SKILLFULNESS COGNITION) (DOCUMENTATION SKILLFULNESS "the state of being cognitively skillful") (HAS-I-TOPIC SKILLFULNESS |Factotum|) (WORD SKILLFULNESS |skillfulness|))) (DEFCONCEPT SPACE_1 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SPACE_1 TOPS) (DOCUMENTATION SPACE_1 "the unlimited 3-dimensional expanse in which everything is located; ’they tested his ability to locate objects in space’") (HAS-I-TOPIC SPACE_1 |Factotum|) (WORD SPACE_1 |space|))) (DEFCONCEPT SUSCEPTIBILITY$SUSCEPTIBLENESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SUSCEPTIBILITY$SUSCEPTIBLENESS STATES) (DOCUMENTATION SUSCEPTIBILITY$SUSCEPTIBLENESS "the state of being susceptible; easily affected") (HAS-I-TOPIC SUSCEPTIBILITY$SUSCEPTIBLENESS |Factotum|) (WORD SUSCEPTIBILITY$SUSCEPTIBLENESS |susceptibility|) (WORD SUSCEPTIBILITY$SUSCEPTIBLENESS |susceptibleness|)))

290

(DEFCONCEPT TENSION$TENSITY$TENSENESS$TAUTNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT TENSION$TENSITY$TENSENESS$TAUTNESS STATES) (DOCUMENTATION TENSION$TENSITY$TENSENESS$TAUTNESS "the physical condition of being stretched or strained; ’it places great tension on the leg muscles’; ’he could feel the tenseness of her body’; ’the violinist adjusted the tension of the strings’") (HAS-I-TOPIC TENSION$TENSITY$TENSENESS$TAUTNESS |Factotum|) (WORD TENSION$TENSITY$TENSENESS$TAUTNESS |tension|) (WORD TENSION$TENSITY$TENSENESS$TAUTNESS |tensity|) (WORD TENSION$TENSITY$TENSENESS$TAUTNESS |tenseness|) (WORD TENSION$TENSITY$TENSENESS$TAUTNESS |tautness|))) (DEFCONCEPT UNSUSCEPTIBILITY$IMMUNITY (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT UNSUSCEPTIBILITY$IMMUNITY STATES) (DOCUMENTATION UNSUSCEPTIBILITY$IMMUNITY "the state of not being susceptible: ’unsusceptibility to rust’; ’immunity to disease’") (HAS-I-TOPIC UNSUSCEPTIBILITY$IMMUNITY |Factotum|) (WORD UNSUSCEPTIBILITY$IMMUNITY |unsusceptibility|) (WORD UNSUSCEPTIBILITY$IMMUNITY |immunity|))) (DEFCONCEPT WETNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT WETNESS STATES) (DOCUMENTATION WETNESS "the condition of containing or being covered by a liquid (especially water); ’he confirmed the wetness of the paint’") (HAS-I-TOPIC WETNESS |Factotum|) (WORD WETNESS |wetness|))) (DEFCONCEPT ABILITY$POWER (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ABILITY$POWER COGNITION) (DOCUMENTATION ABILITY$POWER "possession of the qualities (especially mental qualities) required to do something or get something done; ’danger heightened his powers of discrimination’") (HAS-I-TOPIC ABILITY$POWER |Factotum|) (WORD ABILITY$POWER |ability|) (WORD ABILITY$POWER |power|))) (DEFCONCEPT ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY COGNITION) (DOCUMENTATION ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY "personal knowledge or information about someone or something") (HAS-I-TOPIC ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY |Factotum|) (WORD ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY |acquaintance|) (WORD ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY |familiarity|) (WORD ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY |conversance|) (WORD ACQUAINTANCE$FAMILIARITY$CONVERSANCE$CONVERSANCY |conversancy|))) (DEFCONCEPT AFFINITY$KINSHIP (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT AFFINITY$KINSHIP RELATIONS) (DOCUMENTATION AFFINITY$KINSHIP "a close connection marked by community of interests or similarity in nature or character: ’found a natural affinity with the immigrants’; ’felt a deep kinship with the other students’; ’anthropology’s kinship with the humanities’") (HAS-I-TOPIC AFFINITY$KINSHIP |Factotum|) (WORD AFFINITY$KINSHIP |affinity|) (WORD AFFINITY$KINSHIP |kinship|))) (DEFCONCEPT ANA_1 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ANA_1 GROUPS) (DOCUMENTATION ANA_1 "a collection of anecdotes about a person or place") (HAS-I-TOPIC ANA_1 |Factotum|) (WORD ANA_1 |ana|))) (DEFCONCEPT APOLOGY_1 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT APOLOGY_1 COGNITION)

291

(DOCUMENTATION APOLOGY_1 "a poor example; ’it was an apology for a meal’") (HAS-I-TOPIC APOLOGY_1 |Factotum|) (WORD APOLOGY_1 |apology|))) (DEFCONCEPT ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ARRANGEMENT$ORGANIZATION$ORGANISATION$ SYSTEM COGNITION) (DOCUMENTATION ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM "an organized structure for arranging or classifying; ’he changed the arrangement of the topics’; ’the facts were familiar but it was in the organization of them that he was original’; ’he tried to understand their system of classification’") (HAS-I-TOPIC ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM |Factotum|) (WORD ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM |arrangement|) (WORD ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM |organization|) (WORD ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM |organisation|) (WORD ARRANGEMENT$ORGANIZATION$ORGANISATION$SYSTEM |system|))) (DEFCONCEPT ARRANGEMENT_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ARRANGEMENT_2 GROUPS) (DOCUMENTATION ARRANGEMENT_2 "an orderly grouping (of things or persons)") (HAS-I-TOPIC ARRANGEMENT_2 |Factotum|) (WORD ARRANGEMENT_2 |arrangement|))) (DEFCONCEPT CAUSALITY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CAUSALITY RELATIONS) (DOCUMENTATION CAUSALITY "the relation between causes and effects") (HAS-I-TOPIC CAUSALITY |Factotum|) (WORD CAUSALITY |causality|))) (DEFCONCEPT CHANGE_8 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CHANGE_8 RELATIONS) (DOCUMENTATION CHANGE_8 "a relational difference between states; especially between states before and after some event: ’he attributed the change to their marriage’") (HAS-I-TOPIC CHANGE_8 |Factotum|) (WORD CHANGE_8 |change|))) (DEFCONCEPT CHEERFULNESS$CHEER (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CHEERFULNESS$CHEER ATTRIBUTES) (DOCUMENTATION CHEERFULNESS$CHEER "the quality of being cheerful and dispelling gloom; ’flowers added a note of cheerfulness to the drab room’") (HAS-I-TOPIC CHEERFULNESS$CHEER |Factotum|) (WORD CHEERFULNESS$CHEER |cheerfulness|) (WORD CHEERFULNESS$CHEER |cheer|))) (DEFCONCEPT CLASS$CATEGORY$FAMILY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CLASS$CATEGORY$FAMILY GROUPS) (DOCUMENTATION CLASS$CATEGORY$FAMILY "a collection of things sharing a common attribute; ’there are two classes of detergents’") (HAS-I-TOPIC CLASS$CATEGORY$FAMILY |Factotum|) (WORD CLASS$CATEGORY$FAMILY |class|) (WORD CLASS$CATEGORY$FAMILY |category|) (WORD CLASS$CATEGORY$FAMILY |family|))) (DEFCONCEPT COMPARISON (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT COMPARISON RELATIONS) (DOCUMENTATION COMPARISON "relation based on similarities and differences") (HAS-I-TOPIC COMPARISON |Factotum|) (WORD COMPARISON |comparison|))) (DEFCONCEPT CONNECTION$CONNEXION$CONNECTEDNESS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CONNECTION$CONNEXION$CONNECTEDNESS RELATIONS) (DOCUMENTATION CONNECTION$CONNEXION$CONNECTEDNESS "a relation between things or events (as in the case of one causing the other or sharing features with it); ’there was a connection between eating that pickle and having that nightmare’") (HAS-I-TOPIC CONNECTION$CONNEXION$CONNECTEDNESS |Factotum|)

292

(WORD CONNECTION$CONNEXION$CONNECTEDNESS |connection|) (WORD CONNECTION$CONNEXION$CONNECTEDNESS |connexion|) (WORD CONNECTION$CONNEXION$CONNECTEDNESS |connectedness|))) (DEFCONCEPT CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT COGNITION) (DOCUMENTATION CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT "the sum or range of what has been perceived, discovered, or learned") (HAS-I-TOPIC CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT |Factotum|) (WORD CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT |content|) (WORD CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT |cognitive content|) (WORD CONTENT$COGNITIVE_CONTENT$MENTAL_OBJECT |mental object|))) (DEFCONCEPT CONTROL_5 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT CONTROL_5 RELATIONS) (DOCUMENTATION CONTROL_5 "a relation of constraint of one entity (thing or person or group) by another; ’measures for the control of disease’; ’they instituted controls over drinking on campus’") (HAS-I-TOPIC CONTROL_5 |Factotum|) (WORD CONTROL_5 |control|))) (DEFCONCEPT COURSE_1 (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT COURSE_1 ACTS) (DOCUMENTATION COURSE_1 "a mode of action; ’if you persist in that course you will surely fail’") (HAS-I-TOPIC COURSE_1 |Factotum|) (WORD COURSE_1 |course|))) (DEFCONCEPT ETHOS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT ETHOS ATTRIBUTES) (DOCUMENTATION ETHOS "the distinctive spirit of a people or an era; ’the Greek ethos’") (HAS-I-TOPIC ETHOS |Factotum|) (WORD ETHOS |ethos|))) (DEFCONCEPT EXCEPTION_1 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT EXCEPTION_1 COGNITION) (DOCUMENTATION EXCEPTION_1 "an instance that does not conform to a rule or generalization; ’all her children were brilliant; the only exception was her last child’; ’an exception tests the rule’") (HAS-I-TOPIC EXCEPTION_1 |Factotum|) (WORD EXCEPTION_1 |exception|))) (DEFCONCEPT FOUNDATION_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT FOUNDATION_2 RELATIONS) (DOCUMENTATION FOUNDATION_2 "the basis on which something is grounded; ’there is little foundation for his objections’") (HAS-I-TOPIC FOUNDATION_2 |Factotum|) (WORD FOUNDATION_2 |foundation|))) (DEFCONCEPT FUNCTION_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT FUNCTION_2 RELATIONS) (DOCUMENTATION FUNCTION_2 "a relation such that one thing is dependent on another; ’height is a function of age’; ’price is a function of supply and demand’") (HAS-I-TOPIC FUNCTION_2 |Factotum|) (WORD FUNCTION_2 |function|))) (DEFCONCEPT HYPOTHESIS$POSSIBILITY$THEORY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT HYPOTHESIS$POSSIBILITY$THEORY COGNITION) (DOCUMENTATION HYPOTHESIS$POSSIBILITY$THEORY "a concept that is not yet verified but that if true would explain certain facts or phenomena; ’he proposed a fresh theory of alkalis that later was accepted in chemical practices’") (HAS-I-TOPIC HYPOTHESIS$POSSIBILITY$THEORY |Factotum|) (WORD HYPOTHESIS$POSSIBILITY$THEORY |hypothesis|) (WORD HYPOTHESIS$POSSIBILITY$THEORY |possibility|) (WORD HYPOTHESIS$POSSIBILITY$THEORY |theory|))) (DEFCONCEPT INABILITY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT INABILITY COGNITION) (DOCUMENTATION INABILITY "lack of ability (especially mental ability) to do something") (HAS-I-TOPIC INABILITY |Factotum|) (WORD INABILITY |inability|)))

293

(DEFCONCEPT INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS RELATIONS) (DOCUMENTATION INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS "mutual or reciprocal relation or relatedness: ’interrelationships of animal structure and function’") (HAS-I-TOPIC INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS |Factotum|) (WORD INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS |interrelation|) (WORD INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS |interrelationship|) (WORD INTERRELATION$INTERRELATIONSHIP$INTERRELATEDNESS |interrelatedness|))) (DEFCONCEPT LAW$LAW_OF_NATURE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT LAW$LAW_OF_NATURE COGNITION) (DOCUMENTATION LAW$LAW_OF_NATURE "a generalization based on recurring facts or events (in science or mathematics etc): ’the laws of thermodynamics") (HAS-I-TOPIC LAW$LAW_OF_NATURE |Factotum|) (WORD LAW$LAW_OF_NATURE |law|) (WORD LAW$LAW_OF_NATURE |law of nature|))) (DEFCONCEPT LAW$NATURAL_LAW (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT LAW$NATURAL_LAW COGNITION) (DOCUMENTATION LAW$NATURAL_LAW "a rule or body of rules of conduct inherent in human nature and essential to or binding upon human society") (HAS-I-TOPIC LAW$NATURAL_LAW |Factotum|) (WORD LAW$NATURAL_LAW |law|) (WORD LAW$NATURAL_LAW |natural law|))) (DEFCONCEPT MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT MESSAGE$CONTENT$SUBJECT_MATTER$ SUBSTANCE COMMUNICATION) (DOCUMENTATION MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE "what a communication that is about something is about") (HAS-I-TOPIC MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE |Factotum|) (WORD MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE |message|) (WORD MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE |content|) (WORD MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE |subject matter|) (WORD MESSAGE$CONTENT$SUBJECT_MATTER$SUBSTANCE |substance|))) (DEFCONCEPT MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$ WORD_STRUCTURE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$WORD_STRUCTURE COGNITION) (DOCUMENTATION MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$WORD_STRUCTURE "the admissible arrangement of sounds in words") (HAS-I-TOPIC MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$WORD_STRUCTURE |Factotum|) (WORD MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$ WORD_STRUCTURE |morphology|) (WORD MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$ WORD_STRUCTURE |sound structure|) (WORD MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$ WORD_STRUCTURE |syllable structure|) (WORD MORPHOLOGY$SOUND_STRUCTURE$SYLLABLE_STRUCTURE$ WORD_STRUCTURE |word structure|))) (DEFCONCEPT OPPOSITION$OPPOSITENESS (?SELF)

294

:=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT OPPOSITION$OPPOSITENESS RELATIONS) (DOCUMENTATION OPPOSITION$OPPOSITENESS "the relation between opposed entities") (HAS-I-TOPIC OPPOSITION$OPPOSITENESS |Factotum|) (WORD OPPOSITION$OPPOSITENESS |opposition|) (WORD OPPOSITION$OPPOSITENESS |oppositeness|))) (DEFCONCEPT POSITION$SPATIAL_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT POSITION$SPATIAL_RELATION ATTRIBUTES) (DOCUMENTATION POSITION$SPATIAL_RELATION "the spatial property of a place where or way in which something is situated; ’the position of the hands on the clock’; ’he specified the spatial relations of every piece of furniture on the stage’") (HAS-I-TOPIC POSITION$SPATIAL_RELATION |Factotum|) (WORD POSITION$SPATIAL_RELATION |position|) (WORD POSITION$SPATIAL_RELATION |spatial relation|))) (DEFCONCEPT PRACTICE$PATTERN (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PRACTICE$PATTERN ACTS) (DOCUMENTATION PRACTICE$PATTERN "a customary way of operation or behavior; ’it is their practice to give annual raises’; ’they changed their dietary pattern’") (HAS-I-TOPIC PRACTICE$PATTERN |Factotum|) (WORD PRACTICE$PATTERN |practice|) (WORD PRACTICE$PATTERN |pattern|))) (DEFCONCEPT PROFESSIONAL_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PROFESSIONAL_RELATION RELATIONS) (DOCUMENTATION PROFESSIONAL_RELATION "the relation that exists when one person requests and is granted professional help from a qualified source") (HAS-I-TOPIC PROFESSIONAL_RELATION |Factotum|) (WORD PROFESSIONAL_RELATION |professional_relation|))) (DEFCONCEPT PUBLIC_KNOWLEDGE$GENERAL_KNOWLEDGE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PUBLIC_KNOWLEDGE$GENERAL_KNOWLEDGE COGNITION) (DOCUMENTATION PUBLIC_KNOWLEDGE$GENERAL_KNOWLEDGE "knowledge that is available to anyone") (HAS-I-TOPIC PUBLIC_KNOWLEDGE$GENERAL_KNOWLEDGE |Factotum|) (WORD PUBLIC_KNOWLEDGE$GENERAL_KNOWLEDGE |public knowledge|) (WORD PUBLIC_KNOWLEDGE$GENERAL_KNOWLEDGE |general knowledge|))) (DEFCONCEPT QUINTESSENCE_1 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT QUINTESSENCE_1 COGNITION) (DOCUMENTATION QUINTESSENCE_1 "the most typical example or representative of a type") (HAS-I-TOPIC QUINTESSENCE_1 |Factotum|) (WORD QUINTESSENCE_1 |quintessence|))) (DEFCONCEPT RECIPROCALITY$RECIPROCITY (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT RECIPROCALITY$RECIPROCITY RELATIONS) (DOCUMENTATION RECIPROCALITY$RECIPROCITY "a relation of mutual dependence or action or influence") (HAS-I-TOPIC RECIPROCALITY$RECIPROCITY |Factotum|) (WORD RECIPROCALITY$RECIPROCITY |reciprocality|) (WORD RECIPROCALITY$RECIPROCITY |reciprocity|))) (DEFCONCEPT RELATIONS$DEALINGS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT RELATIONS$DEALINGS RELATIONS) (DOCUMENTATION RELATIONS$DEALINGS "mutual dealings or connections or communications among persons or groups") (HAS-I-TOPIC RELATIONS$DEALINGS |Factotum|) (WORD RELATIONS$DEALINGS |relations|) (WORD RELATIONS$DEALINGS |dealings|))) (DEFCONCEPT RELATIONSHIP$HUMAN_RELATIONSHIP (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT RELATIONSHIP$HUMAN_RELATIONSHIP RELATIONS) (DOCUMENTATION RELATIONSHIP$HUMAN_RELATIONSHIP

295

"(’relationship’ is often used where ’relation’ would serve (as in ’the relationship between inflation and unemployment’) preferred usage of ’relationship’ is for human relations or states of relatedness; ’the relationship between mothers and children’") (HAS-I-TOPIC RELATIONSHIP$HUMAN_RELATIONSHIP |Factotum|) (WORD RELATIONSHIP$HUMAN_RELATIONSHIP |relationship|) (WORD RELATIONSHIP$HUMAN_RELATIONSHIP |human_relationship|))) (DEFCONCEPT RULE$REGULATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT RULE$REGULATION COGNITION) (DOCUMENTATION RULE$REGULATION "a principle or condition that customarily governs behavior; ’it was his rule to take a walk before breakfast’; ’short haircuts were the regulation’") (HAS-I-TOPIC RULE$REGULATION |Factotum|) (WORD RULE$REGULATION |rule|) (WORD RULE$REGULATION |regulation|))) (DEFCONCEPT SPECIMEN_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT SPECIMEN_2 COGNITION) (DOCUMENTATION SPECIMEN_2 "an example regarded as typical of its class") (HAS-I-TOPIC SPECIMEN_2 |Factotum|) (WORD SPECIMEN_2 |specimen|))) (DEFCONCEPT STANDARD_OF_LIVING$STANDARD_OF_LIFE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT STANDARD_OF_LIVING$STANDARD_OF_LIFE STATES) (DOCUMENTATION STANDARD_OF_LIVING$STANDARD_OF_LIFE "a level of material comfort in terms of goods and services available to someone") (HAS-I-TOPIC STANDARD_OF_LIVING$STANDARD_OF_LIFE |Factotum|) (WORD STANDARD_OF_LIVING$STANDARD_OF_LIFE |standard_of_living|) (WORD STANDARD_OF_LIVING$STANDARD_OF_LIFE |standard_of_life|))) (DEFCONCEPT TIP-OFF (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT TIP-OFF COGNITION) (DOCUMENTATION TIP-OFF "inside information that something is going to happen") (HAS-I-TOPIC TIP-OFF |Factotum|) (WORD TIP-OFF |tip-off|))) (DEFCONCEPT UNCHEERFULNESS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT UNCHEERFULNESS ATTRIBUTES) (DOCUMENTATION UNCHEERFULNESS "not conducive to cheer or good spirits") (HAS-I-TOPIC UNCHEERFULNESS |Factotum|) (WORD UNCHEERFULNESS |uncheerfulness|))) (DEFCONCEPT UNCONNECTEDNESS (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT UNCONNECTEDNESS RELATIONS) (DOCUMENTATION UNCONNECTEDNESS "the lack of a connection between things") (HAS-I-TOPIC UNCONNECTEDNESS |Factotum|) (WORD UNCONNECTEDNESS |unconnectedness|))) (DEFCONCEPT ABNORMALITY$ABNORMALCY (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ABNORMALITY$ABNORMALCY STATES) (DOCUMENTATION ABNORMALITY$ABNORMALCY "an abnormal condition") (HAS-I-TOPIC ABNORMALITY$ABNORMALCY |Factotum|) (WORD ABNORMALITY$ABNORMALCY |abnormality|) (WORD ABNORMALITY$ABNORMALCY |abnormalcy|))) (DEFCONCEPT ACTION$ACTIVITY$ACTIVENESS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ACTION$ACTIVITY$ACTIVENESS STATES) (DOCUMENTATION ACTION$ACTIVITY$ACTIVENESS "the state of being active; ’his sphere of activity’; ’he is out of action’") (HAS-I-TOPIC ACTION$ACTIVITY$ACTIVENESS |Factotum|) (WORD ACTION$ACTIVITY$ACTIVENESS |action|) (WORD ACTION$ACTIVITY$ACTIVENESS |activity|) (WORD ACTION$ACTIVITY$ACTIVENESS |activeness|))) (DEFCONCEPT ATMOSPHERE$AMBIANCE$AMBIENCE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ATMOSPHERE$AMBIANCE$AMBIENCE STATES) (DOCUMENTATION ATMOSPHERE$AMBIANCE$AMBIENCE

296

"a particular environment or surrounding influence; ’there was an atmosphere of excitement’") (HAS-I-TOPIC ATMOSPHERE$AMBIANCE$AMBIENCE |Factotum|) (WORD ATMOSPHERE$AMBIANCE$AMBIENCE |atmosphere|) (WORD ATMOSPHERE$AMBIANCE$AMBIENCE |ambiance|) (WORD ATMOSPHERE$AMBIANCE$AMBIENCE |ambience|))) (DEFCONCEPT BACKGROUND$BACKGROUND_KNOWLEDGE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT BACKGROUND$BACKGROUND_KNOWLEDGE COGNITION) (DOCUMENTATION BACKGROUND$BACKGROUND_KNOWLEDGE "information that is essential to understanding a situation or problem; ’the embassy filled him in on the background of the incident’") (HAS-I-TOPIC BACKGROUND$BACKGROUND_KNOWLEDGE |Factotum|) (WORD BACKGROUND$BACKGROUND_KNOWLEDGE |background|) (WORD BACKGROUND$BACKGROUND_KNOWLEDGE |background knowledge|))) (DEFCONCEPT BEING$BEINGNESS$EXISTENCE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT BEING$BEINGNESS$EXISTENCE STATES) (DOCUMENTATION BEING$BEINGNESS$EXISTENCE "the state or fact of existing: ’a point of view gradually coming into being’; ’laws in existence for centuries’") (HAS-I-TOPIC BEING$BEINGNESS$EXISTENCE |Factotum|) (WORD BEING$BEINGNESS$EXISTENCE |being|) (WORD BEING$BEINGNESS$EXISTENCE |beingness|) (WORD BEING$BEINGNESS$EXISTENCE |existence|))) (DEFCONCEPT CHANGE_1 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CHANGE_1 ACTS) (DOCUMENTATION CHANGE_1 "the act of changing something; ’the change of government had no impact on the economy’; ’his change on abortion cost him the election’") (HAS-I-TOPIC CHANGE_1 |Factotum|) (WORD CHANGE_1 |change|))) (DEFCONCEPT CIRCUMSTANCE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CIRCUMSTANCE STATES) (DOCUMENTATION CIRCUMSTANCE "a condition that accompanies or influences some event or activity") (HAS-I-TOPIC CIRCUMSTANCE |Factotum|) (WORD CIRCUMSTANCE |circumstance|))) (DEFCONCEPT CIRCUMSTANCE$CONDITION$CONSIDERATION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CIRCUMSTANCE$CONDITION$CONSIDERATION COGNITION) (DOCUMENTATION CIRCUMSTANCE$CONDITION$CONSIDERATION "information that should be kept in mind when making a decision; ’another consideration is the time it would take’") (HAS-I-TOPIC CIRCUMSTANCE$CONDITION$CONSIDERATION |Factotum|) (WORD CIRCUMSTANCE$CONDITION$CONSIDERATION |circumstance|) (WORD CIRCUMSTANCE$CONDITION$CONSIDERATION |condition|) (WORD CIRCUMSTANCE$CONDITION$CONSIDERATION |consideration|))) (DEFCONCEPT CONDITIONALITY (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CONDITIONALITY STATES) (DOCUMENTATION CONDITIONALITY "the state of being conditional") (HAS-I-TOPIC CONDITIONALITY |Factotum|) (WORD CONDITIONALITY |conditionality|))) (DEFCONCEPT CONFIGURATION$CONSTELLATION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CONFIGURATION$CONSTELLATION COGNITION) (DOCUMENTATION CONFIGURATION$CONSTELLATION "an arrangement of parts or elements; ’the outcome depends on the configuration of influences at the time’") (HAS-I-TOPIC CONFIGURATION$CONSTELLATION |Factotum|) (WORD CONFIGURATION$CONSTELLATION |configuration|) (WORD CONFIGURATION$CONSTELLATION |constellation|))) (DEFCONCEPT CONFLICT_4 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CONFLICT_4 STATES) (DOCUMENTATION CONFLICT_4 "a state of opposition between persons or ideas or interests; ’his conflict of interest

297

made him ineligible for the post’; ’a conflict of loyalties’") (HAS-I-TOPIC CONFLICT_4 |Factotum|) (WORD CONFLICT_4 |conflict|))) (DEFCONCEPT CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT PHENOMENA) (DOCUMENTATION CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT "a phenomenon that follows and is caused by some previous phenomenon; ’the magnetic effect was greater when the rod was lengthwise’; ’his decision had depressing consequences for business’") (HAS-I-TOPIC CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |Factotum|) (WORD CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |consequence|) (WORD CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |effect|) (WORD CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |outcome|) (WORD CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |result|) (WORD CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |issue|) (WORD CONSEQUENCE$EFFECT$OUTCOME$RESULT$ISSUE$UPSHOT |upshot|))) (DEFCONCEPT DANGER_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DANGER_2 STATES) (DOCUMENTATION DANGER_2 "the condition of being susceptible to harm or injury; ’you are in no danger’; ’there was widespread danger of disease’") (HAS-I-TOPIC DANGER_2 |Factotum|) (WORD DANGER_2 |danger|))) (DEFCONCEPT DEAD_LETTER$NON-ISSUE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DEAD_LETTER$NON-ISSUE STATES) (DOCUMENTATION DEAD_LETTER$NON-ISSUE "the state of something that has outlived its relevance") (HAS-I-TOPIC DEAD_LETTER$NON-ISSUE |Factotum|) (WORD DEAD_LETTER$NON-ISSUE |dead_letter|) (WORD DEAD_LETTER$NON-ISSUE |non-issue|))) (DEFCONCEPT DECLINE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DECLINE STATES) (DOCUMENTATION DECLINE "a condition inferior to an earlier condition") (HAS-I-TOPIC DECLINE |Factotum|) (WORD DECLINE |decline|))) (DEFCONCEPT DEGREE$LEVEL$STAGE$POINT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DEGREE$LEVEL$STAGE$POINT STATES) (DOCUMENTATION DEGREE$LEVEL$STAGE$POINT "a specific identifiable position in a continuum or series or especially in a process; ’a remarkable degree of frankness’; ’at what stage are the social sciences?’") (HAS-I-TOPIC DEGREE$LEVEL$STAGE$POINT |Factotum|) (WORD DEGREE$LEVEL$STAGE$POINT |degree|) (WORD DEGREE$LEVEL$STAGE$POINT |level|) (WORD DEGREE$LEVEL$STAGE$POINT |stage|) (WORD DEGREE$LEVEL$STAGE$POINT |point|))) (DEFCONCEPT DEPENDENCE$DEPENDANCE$DEPENDENCY (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DEPENDENCE$DEPENDANCE$DEPENDENCY STATES) (DOCUMENTATION DEPENDENCE$DEPENDANCE$DEPENDENCY "lack of independence or self-sufficiency") (HAS-I-TOPIC DEPENDENCE$DEPENDANCE$DEPENDENCY |Factotum|) (WORD DEPENDENCE$DEPENDANCE$DEPENDENCY |dependence|) (WORD DEPENDENCE$DEPENDANCE$DEPENDENCY |dependance|) (WORD DEPENDENCE$DEPENDANCE$DEPENDENCY |dependency|))) (DEFCONCEPT DESPAIR$DESPERATION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DESPAIR$DESPERATION STATES) (DOCUMENTATION DESPAIR$DESPERATION "a state in which everything seems wrong and will turn out badly; ’they were rescued from despair at the last minute’") (HAS-I-TOPIC DESPAIR$DESPERATION |Factotum|) (WORD DESPAIR$DESPERATION |despair|) (WORD DESPAIR$DESPERATION |desperation|)))

298

(DEFCONCEPT DIFFICULTY_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DIFFICULTY_2 STATES) (DOCUMENTATION DIFFICULTY_2 "a situation or condition almost beyond one’s ability to deal with and requiring great effort to bear or overcome: ’grappling with financial difficulties’") (HAS-I-TOPIC DIFFICULTY_2 |Factotum|) (WORD DIFFICULTY_2 |difficulty|))) (DEFCONCEPT DISORDER (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DISORDER STATES) (DOCUMENTATION DISORDER "a disturbance of the peace or of public order") (HAS-I-TOPIC DISORDER |Factotum|) (WORD DISORDER |disorder|))) (DEFCONCEPT DISORDERLINESS$DISORDER (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DISORDERLINESS$DISORDER STATES) (DOCUMENTATION DISORDERLINESS$DISORDER "a condition in which things are not in their expected places: ’the files are in complete disorder’") (HAS-I-TOPIC DISORDERLINESS$DISORDER |Factotum|) (WORD DISORDERLINESS$DISORDER |disorderliness|) (WORD DISORDERLINESS$DISORDER |disorder|))) (DEFCONCEPT DOMINANCE$ASCENDANCE$ASCENDENCE$ASCENDANCY$ ASCENDENCY$CONTROL (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DOMINANCE$ASCENDANCE$ASCENDENCE$ASCENDANCY$ASCENDENCY$CONTROL STATES) (DOCUMENTATION DOMINANCE$ASCENDANCE$ASCENDENCE$ASCENDANCY$ASCENDENCY$CONTROL "the state that exists when one person or group has power over another; ’her apparent dominance of her husband was really her attempt to make him pay attention to her’") (HAS-I-TOPIC DOMINANCE$ASCENDANCE$ASCENDENCE$ASCENDANCY$ ASCENDENCY$CONTROL |Factotum|) (WORD DOMINANCE$ASCENDANCE$ASCENDENCE$ ASCENDANCY$ASCENDENCY$CONTROL |dominance|) (WORD DOMINANCE$ASCENDANCE$ASCENDENCE$ ASCENDANCY$ASCENDENCY$CONTROL |ascendance|) (WORD DOMINANCE$ASCENDANCE$ASCENDENCE$ ASCENDANCY$ASCENDENCY$CONTROL |ascendence|) (WORD DOMINANCE$ASCENDANCE$ASCENDENCE$ ASCENDANCY$ASCENDENCY$CONTROL |ascendancy|) (WORD DOMINANCE$ASCENDANCE$ASCENDENCE$ ASCENDANCY$ASCENDENCY$CONTROL |ascendency|) (WORD DOMINANCE$ASCENDANCE$ASCENDENCE$ ASCENDANCY$ASCENDENCY$CONTROL |control|))) (DEFCONCEPT DYSTOPIA (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DYSTOPIA STATES) (DOCUMENTATION DYSTOPIA "state in which the condition of life is extremely bad as from deprivation or oppression or terror") (HAS-I-TOPIC DYSTOPIA |Factotum|) (WORD DYSTOPIA |dystopia|))) (DEFCONCEPT END$DESTRUCTION$DEATH (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT END$DESTRUCTION$DEATH STATES) (DOCUMENTATION END$DESTRUCTION$DEATH "a final state; ’he came to a bad end’; ’the so-called glorious experiment came to an inglorious end’") (HAS-I-TOPIC END$DESTRUCTION$DEATH |Factotum|)

299

(WORD END$DESTRUCTION$DEATH |end|) (WORD END$DESTRUCTION$DEATH |destruction|) (WORD END$DESTRUCTION$DEATH |death|))) (DEFCONCEPT ENVIRONMENTAL_CONDITION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ENVIRONMENTAL_CONDITION STATES) (DOCUMENTATION ENVIRONMENTAL_CONDITION "the state of the environment") (HAS-I-TOPIC ENVIRONMENTAL_CONDITION |Factotum|) (WORD ENVIRONMENTAL_CONDITION |environmental_condition|))) (DEFCONCEPT EVIDENCE$GROUNDS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT EVIDENCE$GROUNDS COGNITION) (DOCUMENTATION EVIDENCE$GROUNDS "your basis for belief or disbelief; knowledge on which to base belief; ’the evidence that smoking causes lung cancer is very compelling’") (HAS-I-TOPIC EVIDENCE$GROUNDS |Factotum|) (WORD EVIDENCE$GROUNDS |evidence|) (WORD EVIDENCE$GROUNDS |grounds|))) (DEFCONCEPT FACT_1 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT FACT_1 COGNITION) (DOCUMENTATION FACT_1 "a piece of information about circumstances that exist or events that have occurred; ’first you must collect all the facts of the case’") (HAS-I-TOPIC FACT_1 |Factotum|) (WORD FACT_1 |fact|))) (DEFCONCEPT FACT_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT FACT_2 COGNITION) (DOCUMENTATION FACT_2 "a concept whose truth can be proved; ’scientific hypotheses are not facts’") (HAS-I-TOPIC FACT_2 |Factotum|) (WORD FACT_2 |fact|))) (DEFCONCEPT FORM$SHAPE$PATTERN (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT FORM$SHAPE$PATTERN COGNITION) (DOCUMENTATION FORM$SHAPE$PATTERN "a perceptual structure; ’the composition presents problems for students of musical form’; ’a visual pattern must include not only objects but the spaces between them’") (HAS-I-TOPIC FORM$SHAPE$PATTERN |Factotum|) (WORD FORM$SHAPE$PATTERN |form|) (WORD FORM$SHAPE$PATTERN |shape|) (WORD FORM$SHAPE$PATTERN |pattern|))) (DEFCONCEPT FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION STATES) (DOCUMENTATION FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION "your overall circumstances or condition in life (including everything that happens to you): ’whatever my fortune may be’; ’deserved a better fate’; ’has a happy lot’; ’the luck of the Irish’; ’a victim of circumstances’; ’success that was her portion’") (HAS-I-TOPIC FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |Factotum|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |fortune|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |destiny|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |fate|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |luck|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |lot|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |circumstances|) (WORD FORTUNE$DESTINY$FATE$LUCK$LOT$CIRCUMSTANCES$PORTION |portion|))) (DEFCONCEPT HAPPENING$OCCURRENCE$NATURAL_EVENT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT HAPPENING$OCCURRENCE$NATURAL_EVENT EVENTS) (DOCUMENTATION HAPPENING$OCCURRENCE$NATURAL_EVENT "an event that happens") (HAS-I-TOPIC HAPPENING$OCCURRENCE$NATURAL_EVENT |Factotum|) (WORD HAPPENING$OCCURRENCE$NATURAL_EVENT |happening|) (WORD HAPPENING$OCCURRENCE$NATURAL_EVENT |occurrence|) (WORD HAPPENING$OCCURRENCE$NATURAL_EVENT |natural event|))) (DEFCONCEPT HINDRANCE$INTERFERENCE$INTERFERING (?SELF)

300

:=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT HINDRANCE$INTERFERENCE$INTERFERING ACTS) (DOCUMENTATION HINDRANCE$INTERFERENCE$INTERFERING "the act of hindering or obstructing or impeding") (HAS-I-TOPIC HINDRANCE$INTERFERENCE$INTERFERING |Factotum|) (WORD HINDRANCE$INTERFERENCE$INTERFERING |hindrance|) (WORD HINDRANCE$INTERFERENCE$INTERFERING |interference|) (WORD HINDRANCE$INTERFERENCE$INTERFERING |interfering|))) (DEFCONCEPT HOSTILITY$ENMITY$ANTAGONISM (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT HOSTILITY$ENMITY$ANTAGONISM STATES) (DOCUMENTATION HOSTILITY$ENMITY$ANTAGONISM "a state of deep-seated ill-will") (HAS-I-TOPIC HOSTILITY$ENMITY$ANTAGONISM |Factotum|) (WORD HOSTILITY$ENMITY$ANTAGONISM |hostility|) (WORD HOSTILITY$ENMITY$ANTAGONISM |enmity|) (WORD HOSTILITY$ENMITY$ANTAGONISM |antagonism|))) (DEFCONCEPT IMPROVEMENT_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT IMPROVEMENT_2 STATES) (DOCUMENTATION IMPROVEMENT_2 "a condition superior to an earlier condition: ’the new school represents a great improvement’") (HAS-I-TOPIC IMPROVEMENT_2 |Factotum|) (WORD IMPROVEMENT_2 |improvement|))) (DEFCONCEPT INACTION$INACTIVITY$INACTIVENESS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT INACTION$INACTIVITY$INACTIVENESS STATES) (DOCUMENTATION INACTION$INACTIVITY$INACTIVENESS "the state of being inactive") (HAS-I-TOPIC INACTION$INACTIVITY$INACTIVENESS |Factotum|) (WORD INACTION$INACTIVITY$INACTIVENESS |inaction|) (WORD INACTION$INACTIVITY$INACTIVENESS |inactivity|) (WORD INACTION$INACTIVITY$INACTIVENESS |inactiveness|))) (DEFCONCEPT INACTIVITY (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT INACTIVITY ACTS) (DOCUMENTATION INACTIVITY "being inactive") (HAS-I-TOPIC INACTIVITY |Factotum|) (WORD INACTIVITY |inactivity|))) (DEFCONCEPT MEDIUM_4 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT MEDIUM_4 STATES) (DOCUMENTATION MEDIUM_4 "a state that is intermediate between extremes; a middle position; ’a happy medium’") (HAS-I-TOPIC MEDIUM_4 |Factotum|) (WORD MEDIUM_4 |medium|))) (DEFCONCEPT MODEL$EXAMPLE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT MODEL$EXAMPLE COGNITION) (DOCUMENTATION MODEL$EXAMPLE "a representative form or pattern; ’I profited from his example’") (HAS-I-TOPIC MODEL$EXAMPLE |Factotum|) (WORD MODEL$EXAMPLE |model|) (WORD MODEL$EXAMPLE |example|))) (DEFCONCEPT MOTION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT MOTION STATES) (DOCUMENTATION MOTION "a state of change; ’they were in a state of steady motion’") (HAS-I-TOPIC MOTION |Factotum|) (WORD MOTION |motion|))) (DEFCONCEPT NEED$DEMAND (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT NEED$DEMAND STATES) (DOCUMENTATION NEED$DEMAND "a condition requiring relief; ’she satified his need for affection’; ’God has no need of men to accomplish His work’; ’there is a demand for jobs’") (HAS-I-TOPIC NEED$DEMAND |Factotum|) (WORD NEED$DEMAND |need|) (WORD NEED$DEMAND |demand|))) (DEFCONCEPT NONACCOMPLISHMENT$NONACHIEVEMENT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT NONACCOMPLISHMENT$NONACHIEVEMENT ACTS)

301

(DOCUMENTATION NONACCOMPLISHMENT$NONACHIEVEMENT "an act that does not achieve its intended goal") (HAS-I-TOPIC NONACCOMPLISHMENT$NONACHIEVEMENT |Factotum|) (WORD NONACCOMPLISHMENT$NONACHIEVEMENT |nonaccomplishment|) (WORD NONACCOMPLISHMENT$NONACHIEVEMENT |nonachievement|))) (DEFCONCEPT NONBEING (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT NONBEING STATES) (DOCUMENTATION NONBEING "the state of not being") (HAS-I-TOPIC NONBEING |Factotum|) (WORD NONBEING |nonbeing|))) (DEFCONCEPT NORMALITY$NORMALCY (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT NORMALITY$NORMALCY STATES) (DOCUMENTATION NORMALITY$NORMALCY "conformity with the norm") (HAS-I-TOPIC NORMALITY$NORMALCY |Factotum|) (WORD NORMALITY$NORMALCY |normality|) (WORD NORMALITY$NORMALCY |normalcy|))) (DEFCONCEPT ORDER_3 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ORDER_3 STATES) (DOCUMENTATION ORDER_3 "established customary state esp. of society; ’order ruled in the streets’; ’law and order’") (HAS-I-TOPIC ORDER_3 |Factotum|) (WORD ORDER_3 |order|))) (DEFCONCEPT ORDERLINESS$ORDER (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ORDERLINESS$ORDER STATES) (DOCUMENTATION ORDERLINESS$ORDER "a condition of regular or proper arrangement: ’he put his desk in order’; ’put the chessmen in order’") (HAS-I-TOPIC ORDERLINESS$ORDER |Factotum|) (WORD ORDERLINESS$ORDER |orderliness|) (WORD ORDERLINESS$ORDER |order|))) (DEFCONCEPT ORDINARY_4 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT ORDINARY_4 STATES) (DOCUMENTATION ORDINARY_4 "the expected or commonplace condition or situation: ’not out of the ordinary’") (HAS-I-TOPIC ORDINARY_4 |Factotum|) (WORD ORDINARY_4 |ordinary|))) (DEFCONCEPT PRECEDENT$CASE_IN_POINT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT PRECEDENT$CASE_IN_POINT COGNITION) (DOCUMENTATION PRECEDENT$CASE_IN_POINT "an example that is used to justify similar occurrences at a later time") (HAS-I-TOPIC PRECEDENT$CASE_IN_POINT |Factotum|) (WORD PRECEDENT$CASE_IN_POINT |precedent|) (WORD PRECEDENT$CASE_IN_POINT |case in point|))) (DEFCONCEPT REINSTATEMENT_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT REINSTATEMENT_2 STATES) (DOCUMENTATION REINSTATEMENT_2 "the condition of being reinstated; ’her reinstatement to her former office followed quickly’") (HAS-I-TOPIC REINSTATEMENT_2 |Factotum|) (WORD REINSTATEMENT_2 |reinstatement|))) (DEFCONCEPT RELATIONSHIP_1 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT RELATIONSHIP_1 STATES) (DOCUMENTATION RELATIONSHIP_1 "a state of connectedness between people (especially an emotional connection); ’he didn’t want his wife to know of the relationship’") (HAS-I-TOPIC RELATIONSHIP_1 |Factotum|) (WORD RELATIONSHIP_1 |relationship|))) (DEFCONCEPT RELATIONSHIP_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT RELATIONSHIP_2 STATES) (DOCUMENTATION RELATIONSHIP_2 "a state involving mutual dealings between people or parties or countries") (HAS-I-TOPIC RELATIONSHIP_2 |Factotum|) (WORD RELATIONSHIP_2 |relationship|)))

302

(DEFCONCEPT REPAIR (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT REPAIR STATES) (DOCUMENTATION REPAIR "a formal way of referring to the condition of something; ’the building was in good repair’") (HAS-I-TOPIC REPAIR |Factotum|) (WORD REPAIR |repair|))) (DEFCONCEPT RESISTANCE$OPPOSITION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT RESISTANCE$OPPOSITION ACTS) (DOCUMENTATION RESISTANCE$OPPOSITION "the action of opposing something that you disapprove or disagree with; ’he encountered a general feeling of resistance from many citizens’; ’despite opposition from the newspapers he went ahead’") (HAS-I-TOPIC RESISTANCE$OPPOSITION |Factotum|) (WORD RESISTANCE$OPPOSITION |resistance|) (WORD RESISTANCE$OPPOSITION |opposition|))) (DEFCONCEPT SAFETY_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT SAFETY_2 STATES) (DOCUMENTATION SAFETY_2 "the state of being safe; ’the safety of the children’") (HAS-I-TOPIC SAFETY_2 |Factotum|) (WORD SAFETY_2 |safety|))) (DEFCONCEPT SITUATION$POSITION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT SITUATION$POSITION STATES) (DOCUMENTATION SITUATION$POSITION "a condition or position in which you find yourself: ’the unpleasant situation (or position) of having to choose between two evils’; ’found herself in a very fortunate situation’") (HAS-I-TOPIC SITUATION$POSITION |Factotum|) (WORD SITUATION$POSITION |situation|) (WORD SITUATION$POSITION |position|))) (DEFCONCEPT SITUATION$STATE_OF_AFFAIRS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT SITUATION$STATE_OF_AFFAIRS STATES) (DOCUMENTATION SITUATION$STATE_OF_AFFAIRS "the general state of things; the combination of circumstances at a given time; ’the present international situation is dangerous’; ’wondered how such a state of affairs had come about’; ’eternal truths will be neither true nor eternal unless they have fresh meaning for every new social situation’- Franklin D.Roosevelt") (HAS-I-TOPIC SITUATION$STATE_OF_AFFAIRS |Factotum|) (WORD SITUATION$STATE_OF_AFFAIRS |situation|) (WORD SITUATION$STATE_OF_AFFAIRS |state_of_affairs|))) (DEFCONCEPT SOUNDNESS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT SOUNDNESS STATES) (DOCUMENTATION SOUNDNESS "a state or condition free from damage or decay") (HAS-I-TOPIC SOUNDNESS |Factotum|) (WORD SOUNDNESS |soundness|))) (DEFCONCEPT STIMULATION$STIMULUS$STIMULANT$INPUT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT STIMULATION$STIMULUS$STIMULANT$INPUT COGNITION) (DOCUMENTATION STIMULATION$STIMULUS$STIMULANT$INPUT "any stimulating information or event; acts to arouse action") (HAS-I-TOPIC STIMULATION$STIMULUS$STIMULANT$INPUT |Factotum|) (WORD STIMULATION$STIMULUS$STIMULANT$INPUT |stimulation|) (WORD STIMULATION$STIMULUS$STIMULANT$INPUT |stimulus|) (WORD STIMULATION$STIMULUS$STIMULANT$INPUT |stimulant|) (WORD STIMULATION$STIMULUS$STIMULANT$INPUT |input|))) (DEFCONCEPT SUPPORT_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT SUPPORT_2 ACTS) (DOCUMENTATION SUPPORT_2 "the activity of providing for or maintaining by supplying with money or necessities; ’his support kept the family together’; ’they gave him emotional support during difficult times’") (HAS-I-TOPIC SUPPORT_2 |Factotum|) (WORD SUPPORT_2 |support|))) (DEFCONCEPT TEMPORARY_STATE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT TEMPORARY_STATE STATES)

303

(DOCUMENTATION TEMPORARY_STATE "a state that continues for a limited time") (HAS-I-TOPIC TEMPORARY_STATE |Factotum|) (WORD TEMPORARY_STATE |temporary_state|))) (DEFCONCEPT UNSOUNDNESS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT UNSOUNDNESS STATES) (DOCUMENTATION UNSOUNDNESS "a condition of damage or decay") (HAS-I-TOPIC UNSOUNDNESS |Factotum|) (WORD UNSOUNDNESS |unsoundness|))) (DEFCONCEPT UTOPIA (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT UTOPIA STATES) (DOCUMENTATION UTOPIA "ideally perfect state; especially in its social and political and moral aspects") (HAS-I-TOPIC UTOPIA |Factotum|) (WORD UTOPIA |utopia|))) (DEFCONCEPT VARIATION$VARIANCE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT VARIATION$VARIANCE ACTS) (DOCUMENTATION VARIATION$VARIANCE "an activity that varies from a norm or standard; ’any variation in his routine was immediately reported’") (HAS-I-TOPIC VARIATION$VARIANCE |Factotum|) (WORD VARIATION$VARIANCE |variation|) (WORD VARIATION$VARIANCE |variance|))) (DEFCONCEPT WAY_6 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT WAY_6 STATES) (DOCUMENTATION WAY_6 "the condition of things generally; ’that’s the way it is’ or ’I felt the same way’") (HAS-I-TOPIC WAY_6 |Factotum|) (WORD WAY_6 |way|))) (DEFCONCEPT ORGANIZATION$ORGANISATION_2 (?SELF) :=> (SOCIAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ORGANIZATION$ORGANISATION_2 GROUPS) (DOCUMENTATION ORGANIZATION$ORGANISATION_2 "a group of people who work together") (HAS-I-TOPIC ORGANIZATION$ORGANISATION_2 |Factotum|) (WORD ORGANIZATION$ORGANISATION_2 |organization|) (WORD ORGANIZATION$ORGANISATION_2 |organisation|))) (DEFCONCEPT SUBGROUP_2 (?SELF) :=> (SOCIAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT SUBGROUP_2 GROUPS) (DOCUMENTATION SUBGROUP_2 "a distinct and often subordinate group within a group") (HAS-I-TOPIC SUBGROUP_2 |Factotum|) (WORD SUBGROUP_2 |subgroup|))) (DEFCONCEPT ROLE_WN (?SELF) :=> (SOCIALLY-CONSTRUCTED-PERSON ?SELF) :AXIOMS (AND (SUBJECT ROLE_WN ACTS) (DOCUMENTATION ROLE_WN "normal or customary activity; ’what is your role on the team?’") (HAS-I-TOPIC ROLE_WN |Factotum|) (WORD ROLE_WN |role|))) (DEFCONCEPT DEATH_4 (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT DEATH_4 STATES) (DOCUMENTATION DEATH_4 "the absence of life or state of being dead; ’he seemed more content in death than he had ever been in life’") (HAS-I-TOPIC DEATH_4 |Factotum|) (WORD DEATH_4 |death|))) (DEFCONCEPT DISHABILLE$DESHABILLE (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT DISHABILLE$DESHABILLE STATES) (DOCUMENTATION DISHABILLE$DESHABILLE "the state of being carelessly or partially dressed") (HAS-I-TOPIC DISHABILLE$DESHABILLE |Factotum|) (WORD DISHABILLE$DESHABILLE |dishabille|) (WORD DISHABILLE$DESHABILLE |deshabille|))) (DEFCONCEPT FREEDOM (?SELF) :=> (STATE ?SELF)

304

:AXIOMS (AND (SUBJECT FREEDOM STATES) (DOCUMENTATION FREEDOM "the condition of being free; the power to act or speak or think without externally imposed restraints") (HAS-I-TOPIC FREEDOM |Factotum|) (WORD FREEDOM |freedom|))) (DEFCONCEPT HOMELESSNESS (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT HOMELESSNESS STATES) (DOCUMENTATION HOMELESSNESS "the state or condition of having no home (especially the state of living in the streets)") (HAS-I-TOPIC HOMELESSNESS |Factotum|) (WORD HOMELESSNESS |homelessness|))) (DEFCONCEPT HYALINIZATION (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT HYALINIZATION STATES) (DOCUMENTATION HYALINIZATION "the state of being hyaline or having become hyaline: ’the patient’s arterioles showed marked hyalinization’") (HAS-I-TOPIC HYALINIZATION |Factotum|) (WORD HYALINIZATION |hyalinization|))) (DEFCONCEPT MOTIONLESSNESS$STILLNESS (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT MOTIONLESSNESS$STILLNESS STATES) (DOCUMENTATION MOTIONLESSNESS$STILLNESS "a state of no motion or movement") (HAS-I-TOPIC MOTIONLESSNESS$STILLNESS |Factotum|) (WORD MOTIONLESSNESS$STILLNESS |motionlessness|) (WORD MOTIONLESSNESS$STILLNESS |stillness|))) (DEFCONCEPT NAKEDNESS$NUDITY$NUDENESS (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT NAKEDNESS$NUDITY$NUDENESS STATES) (DOCUMENTATION NAKEDNESS$NUDITY$NUDENESS "the state of being without clothing or covering of any kind") (HAS-I-TOPIC NAKEDNESS$NUDITY$NUDENESS |Factotum|) (WORD NAKEDNESS$NUDITY$NUDENESS |nakedness|) (WORD NAKEDNESS$NUDITY$NUDENESS |nudity|) (WORD NAKEDNESS$NUDITY$NUDENESS |nudeness|))) (DEFCONCEPT REPRESENTATION$DELEGACY$AGENCY (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT REPRESENTATION$DELEGACY$AGENCY STATES) (DOCUMENTATION REPRESENTATION$DELEGACY$AGENCY "the state of serving as an official and authorized delegate or agent") (HAS-I-TOPIC REPRESENTATION$DELEGACY$AGENCY |Factotum|) (WORD REPRESENTATION$DELEGACY$AGENCY |representation|) (WORD REPRESENTATION$DELEGACY$AGENCY |delegacy|) (WORD REPRESENTATION$DELEGACY$AGENCY |agency|))) (DEFCONCEPT SERRATION_3 (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT SERRATION_3 STATES) (DOCUMENTATION SERRATION_3 "the condition of being serrated; ’the serrations of a city skyline’") (HAS-I-TOPIC SERRATION_3 |Factotum|) (WORD SERRATION_3 |serration|))) (DEFCONCEPT TILTH (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT TILTH STATES) (DOCUMENTATION TILTH "the state of aggregation of soil and its condition for supporting plant growth") (HAS-I-TOPIC TILTH |Factotum|) (WORD TILTH |tilth|))) (DEFCONCEPT UNION_4 (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT UNION_4 STATES) (DOCUMENTATION UNION_4 "the state of being united; ’there is strength in union’") (HAS-I-TOPIC UNION_4 |Factotum|) (WORD UNION_4 |union|))) (DEFCONCEPT VACUOLIZATION$VACUOLATION (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT VACUOLIZATION$VACUOLATION STATES) (DOCUMENTATION VACUOLIZATION$VACUOLATION "the state of having become filled with vacuoles")

305

(HAS-I-TOPIC VACUOLIZATION$VACUOLATION |Factotum|) (WORD VACUOLIZATION$VACUOLATION |vacuolization|) (WORD VACUOLIZATION$VACUOLATION |vacuolation|))) (DEFCONCEPT VIRGINITY (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT VIRGINITY STATES) (DOCUMENTATION VIRGINITY "the condition or quality of being a virgin") (HAS-I-TOPIC VIRGINITY |Factotum|) (WORD VIRGINITY |virginity|))) (DEFCONCEPT DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$ FIELD_OF_STUDY$ STUDY$BRANCH_OF_KNOWLEDGE (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$ FIELD_OF_STUDY$STUDY$ BRANCH_OF_KNOWLEDGE COGNITION) (DOCUMENTATION DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$ FIELD_OF_STUDY$STUDY$ BRANCH_OF_KNOWLEDGE "a branch of knowledge; ’in what discipline is his doctorate?’; ’teachers should be well trained in their subject’; ’anthropology is the study of human beings’") (HAS-I-TOPIC DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$STUDY$ BRANCH_OF_KNOWLEDGE |Factotum|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$STUDY$ BRANCH_OF_KNOWLEDGE |discipline|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$STUDY$ BRANCH_OF_KNOWLEDGE |subject|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$STUDY$ BRANCH_OF_KNOWLEDGE |subject area|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$ STUDY$BRANCH_OF_KNOWLEDGE |subject field|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$ STUDY$BRANCH_OF_KNOWLEDGE |field|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$ STUDY$BRANCH_OF_KNOWLEDGE |field of study|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$ STUDY$BRANCH_OF_KNOWLEDGE |study|) (WORD DISCIPLINE$SUBJECT$SUBJECT_AREA$SUBJECT_FIELD$FIELD$FIELD_OF_STUDY$ STUDY$BRANCH_OF_KNOWLEDGE |branch of knowledge|))) (DEFCONCEPT DOMAIN$REGION$REALM (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT DOMAIN$REGION$REALM COGNITION) (DOCUMENTATION DOMAIN$REGION$REALM "a knowledge domain that you are interested in or are communicating about; ’it was a limited domain of discourse’; ’here we enter the region of opinion’;z

306

’the realm of the occult’") (HAS-I-TOPIC DOMAIN$REGION$REALM |Factotum|) (WORD DOMAIN$REGION$REALM |domain|) (WORD DOMAIN$REGION$REALM |region|) (WORD DOMAIN$REGION$REALM |realm|))) (DEFCONCEPT LORE$TRADITIONAL_KNOWLEDGE (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT LORE$TRADITIONAL_KNOWLEDGE COGNITION) (DOCUMENTATION LORE$TRADITIONAL_KNOWLEDGE "knowledge gained through tradition or anecdote: ’early peoples passed on plant and animal lore through legend’") (HAS-I-TOPIC LORE$TRADITIONAL_KNOWLEDGE |Factotum|) (WORD LORE$TRADITIONAL_KNOWLEDGE |lore|) (WORD LORE$TRADITIONAL_KNOWLEDGE |traditional knowledge|))) (DEFCONCEPT METAKNOWLEDGE (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT METAKNOWLEDGE COGNITION) (DOCUMENTATION METAKNOWLEDGE "knowledge about knowledge") (HAS-I-TOPIC METAKNOWLEDGE |Factotum|) (WORD METAKNOWLEDGE |metaknowledge|))) (DEFCONCEPT SCIENCE$SCIENTIFIC_KNOWLEDGE (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT SCIENCE$SCIENTIFIC_KNOWLEDGE COGNITION) (DOCUMENTATION SCIENCE$SCIENTIFIC_KNOWLEDGE "any domain of knowledge accumulated by systematic study and organized by general principles; ’mathematics is important for science’") (HAS-I-TOPIC SCIENCE$SCIENTIFIC_KNOWLEDGE |Factotum|) (WORD SCIENCE$SCIENTIFIC_KNOWLEDGE |science|) (WORD SCIENCE$SCIENTIFIC_KNOWLEDGE |scientific knowledge|))) (DEFCONCEPT TOPIC$SUBJECT$ISSUE$MATTER (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT TOPIC$SUBJECT$ISSUE$MATTER COGNITION) (DOCUMENTATION TOPIC$SUBJECT$ISSUE$MATTER "some situation or event that is thought about; ’he kept drifting off the topic’; ’he had been thinking about the subject for several years’; ’it is a matter for the police’") (HAS-I-TOPIC TOPIC$SUBJECT$ISSUE$MATTER |Factotum|) (WORD TOPIC$SUBJECT$ISSUE$MATTER |topic|) (WORD TOPIC$SUBJECT$ISSUE$MATTER |subject|) (WORD TOPIC$SUBJECT$ISSUE$MATTER |issue|) (WORD TOPIC$SUBJECT$ISSUE$MATTER |matter|))) (DEFCONCEPT UNIVERSE$UNIVERSE_OF_DISCOURSE (?SELF) :=> (TOPIC ?SELF) :AXIOMS (AND (SUBJECT UNIVERSE$UNIVERSE_OF_DISCOURSE COGNITION) (DOCUMENTATION UNIVERSE$UNIVERSE_OF_DISCOURSE "everything stated or assumed in a given discussion") (HAS-I-TOPIC UNIVERSE$UNIVERSE_OF_DISCOURSE |Factotum|) (WORD UNIVERSE$UNIVERSE_OF_DISCOURSE |universe|) (WORD UNIVERSE$UNIVERSE_OF_DISCOURSE |universe of discourse|))) (DEFCONCEPT CUTTING (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT CUTTING OBJECTS) (DOCUMENTATION CUTTING "a piece cut off from the main part of something") (HAS-I-TOPIC CUTTING |Factotum|) (WORD CUTTING |cutting|))) (DEFCONCEPT EMANATION (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT EMANATION SUBSTANCES) (DOCUMENTATION EMANATION "something that is produced by emanation") (HAS-I-TOPIC EMANATION |Factotum|) (WORD EMANATION |emanation|))) (DEFCONCEPT POUNDER (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT POUNDER OBJECTS) (DOCUMENTATION POUNDER "something weighing a given number of pounds; ’the fisherman caught a 10-pounder’ or ’their linemen are all 300-pounders’") (HAS-I-TOPIC POUNDER |Factotum|) (WORD POUNDER |pounder|))) (DEFCONCEPT SAMPLE_1 (?SELF) :=> (SUBSTANCE-ROLE ?SELF)

307

:AXIOMS (AND (SUBJECT SAMPLE_1 COGNITION) (DOCUMENTATION SAMPLE_1 "a small part of something intended as representative of the whole") (HAS-I-TOPIC SAMPLE_1 |Factotum|) (WORD SAMPLE_1 |sample|))) (DEFCONCEPT SHINER_2 (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SHINER_2 OBJECTS) (DOCUMENTATION SHINER_2 "something that shines") (HAS-I-TOPIC SHINER_2 |Factotum|) (WORD SHINER_2 |shiner|))) (DEFCONCEPT SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$ OOZE SUBSTANCES) (DOCUMENTATION SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE "any thick messy substance") (HAS-I-TOPIC SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |Factotum|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |sludge|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |slime|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |goo|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |gook|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |guck|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |gunk|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |muck|) (WORD SLUDGE$SLIME$GOO$GOOK$GUCK$GUNK$MUCK$OOZE |ooze|))) (DEFCONCEPT SUBSTANCE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SUBSTANCE RELATIONS) (DOCUMENTATION SUBSTANCE "the stuff of which an object consists") (HAS-I-TOPIC SUBSTANCE |Factotum|) (WORD SUBSTANCE |substance|))) (DEFCONCEPT THEORY_2 (?SELF) :=> (THEORY ?SELF) :AXIOMS (AND (SUBJECT THEORY_2 COGNITION) (DOCUMENTATION THEORY_2 "an organized system of accepted knowledge that applies in a variety of circumstances to explain a specific set of phenomena; ’true in fact and theory’") (HAS-I-TOPIC THEORY_2 |Factotum|) (WORD THEORY_2 |theory|))) (DEFCONCEPT ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$ POTPOURRI$MOTLEY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY GROUPS) (DOCUMENTATION ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY "a collection containing a variety of sorts of things; ’a great assortment of cars was on display’; ’he had a variety of disorders’") (HAS-I-TOPIC ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |Factotum|) (WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |assortment|) (WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |mixture|) (WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |miscellany|) (WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |miscellanea|) (WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |variety|) (WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |potpourri|)

308

(WORD ASSORTMENT$MIXTURE$MISCELLANY$MISCELLANEA$VARIETY$POTPOURRI$MOTLEY |motley|))) (DEFCONCEPT BATCH (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BATCH GROUPS) (DOCUMENTATION BATCH "all the loaves of bread baked at the same time") (HAS-I-TOPIC BATCH |Factotum|) (WORD BATCH |batch|))) (DEFCONCEPT BATCH$CLUTCH (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BATCH$CLUTCH GROUPS) (DOCUMENTATION BATCH$CLUTCH "a collection of things or persons to be handled together") (HAS-I-TOPIC BATCH$CLUTCH |Factotum|) (WORD BATCH$CLUTCH |batch|) (WORD BATCH$CLUTCH |clutch|))) (DEFCONCEPT BATTERY_1 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BATTERY_1 GROUPS) (DOCUMENTATION BATTERY_1 "a collection of related things intended for use together: ’took a battery of achievement tests’") (HAS-I-TOPIC BATTERY_1 |Factotum|) (WORD BATTERY_1 |battery|))) (DEFCONCEPT BLOCK_3 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BLOCK_3 GROUPS) (DOCUMENTATION BLOCK_3 "a number or quantity of related things dealt with as a unit; ’he reserved a large block of seats’; ’he held a large block of the company’s stock’") (HAS-I-TOPIC BLOCK_3 |Factotum|) (WORD BLOCK_3 |block|))) (DEFCONCEPT BOTTLE_COLLECTION_3 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BOTTLE_COLLECTION_3 GROUPS) (DOCUMENTATION BOTTLE_COLLECTION_3 "a collection of bottles: ’her bottle collection is arranged on glass shelves in the wondow’") (HAS-I-TOPIC BOTTLE_COLLECTION_3 |Factotum|) (WORD BOTTLE_COLLECTION_3 |bottle collection|))) (DEFCONCEPT BUNCH$LOT$CABOODLE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BUNCH$LOT$CABOODLE GROUPS) (DOCUMENTATION BUNCH$LOT$CABOODLE "any collection in its entirety; ’she bought the whole caboodle’") (HAS-I-TOPIC BUNCH$LOT$CABOODLE |Factotum|) (WORD BUNCH$LOT$CABOODLE |bunch|) (WORD BUNCH$LOT$CABOODLE |lot|) (WORD BUNCH$LOT$CABOODLE |caboodle|))) (DEFCONCEPT COMBINATION_2 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT COMBINATION_2 GROUPS) (DOCUMENTATION COMBINATION_2 "a collection of things that have been combined; an assemblage of separate parts or qualities") (HAS-I-TOPIC COMBINATION_2 |Factotum|) (WORD COMBINATION_2 |combination|))) (DEFCONCEPT CORPUS_2 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT CORPUS_2 GROUPS) (DOCUMENTATION CORPUS_2 "a collection of writings; ’he edited the Hemingway corpus’") (HAS-I-TOPIC CORPUS_2 |Factotum|) (WORD CORPUS_2 |corpus|))) (DEFCONCEPT GALAXY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT GALAXY GROUPS) (DOCUMENTATION GALAXY "a splendid assemblage (especially of famous people)") (HAS-I-TOPIC GALAXY |Factotum|) (WORD GALAXY |galaxy|))) (DEFCONCEPT GIMMICKRY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT GIMMICKRY GROUPS) (DOCUMENTATION GIMMICKRY "a collection of gimmicks") (HAS-I-TOPIC GIMMICKRY |Factotum|) (WORD GIMMICKRY |gimmickry|)))

309

(DEFCONCEPT MASS_4 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT MASS_4 GROUPS) (DOCUMENTATION MASS_4 "an ill-structured collection of similar things (objects or people)") (HAS-I-TOPIC MASS_4 |Factotum|) (WORD MASS_4 |mass|))) (DEFCONCEPT PACK_4 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT PACK_4 GROUPS) (DOCUMENTATION PACK_4 "a complete collection of similar things") (HAS-I-TOPIC PACK_4 |Factotum|) (WORD PACK_4 |pack|))) (DEFCONCEPT REPERTORY$REPERTOIRE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT REPERTORY$REPERTOIRE GROUPS) (DOCUMENTATION REPERTORY$REPERTOIRE "the entire range of skills or aptitudes or devices used in a particular field or occupation: ’the repertory of the supposed feats of mesmerism’; ’has a large repertory of dialects and characters’") (HAS-I-TOPIC REPERTORY$REPERTOIRE |Factotum|) (WORD REPERTORY$REPERTOIRE |repertory|) (WORD REPERTORY$REPERTOIRE |repertoire|))) (DEFCONCEPT ROGUE_S_GALLERY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT ROGUE_S_GALLERY GROUPS) (DOCUMENTATION ROGUE_S_GALLERY "a collection of pictures of criminals") (HAS-I-TOPIC ROGUE_S_GALLERY |Factotum|) (WORD ROGUE_S_GALLERY |rogue’s_gallery|))) (DEFCONCEPT SET_4 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT SET_4 GROUPS) (DOCUMENTATION SET_4 "a group of things of the same kind that belong together and are so used: ’a set of books’; ’a set of golf clubs’") (HAS-I-TOPIC SET_4 |Factotum|) (WORD SET_4 |set|))) (DEFCONCEPT STATUARY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT STATUARY GROUPS) (DOCUMENTATION STATUARY "statues collectively") (HAS-I-TOPIC STATUARY |Factotum|) (WORD STATUARY |statuary|))) (DEFCONCEPT STRING_2 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT STRING_2 ARTIFACTS) (DOCUMENTATION STRING_2 "a collection of objects threaded on a single strand") (HAS-I-TOPIC STRING_2 |Factotum|) (WORD STRING_2 |string|))) (DEFCONCEPT SYSTEM_4 (?SELF) :=> (SYSTEM-AS-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT SYSTEM_4 GROUPS) (DOCUMENTATION SYSTEM_4 "a group of independent but interrelated elements comprising a unified whole; ’a vast system of production and distribution and consumption keep the country going’") (HAS-I-TOPIC SYSTEM_4 |Factotum|) (WORD SYSTEM_4 |system|))) (DEFCONCEPT TREASURE_1 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT TREASURE_1 GROUPS) (DOCUMENTATION TREASURE_1 "a collection of precious things; ’the trunk held all her meager treasures’") (HAS-I-TOPIC TREASURE_1 |Factotum|) (WORD TREASURE_1 |treasure|))) (DEFCONCEPT TREASURE_TROVE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT TREASURE_TROVE GROUPS) (DOCUMENTATION TREASURE_TROVE "any collection of valuables that is discovered; ’her book was a treasure trove of new ideas’ or ’mother’s attic was a treasure trove when we were looking for antiques’") (HAS-I-TOPIC TREASURE_TROVE |Factotum|) (WORD TREASURE_TROVE |treasure_trove|))) (DEFCONCEPT UNIVERSE$COSMOS (?SELF) :=> (UNITARY-COLLECTION ?SELF)

310

:AXIOMS (AND (SUBJECT UNIVERSE$COSMOS GROUPS) (DOCUMENTATION UNIVERSE$COSMOS "the whole collection of existing things") (HAS-I-TOPIC UNIVERSE$COSMOS |Factotum|) (WORD UNIVERSE$COSMOS |universe|) (WORD UNIVERSE$COSMOS |cosmos|))) (DEFCONCEPT PLAYTHING$TOY (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT PLAYTHING$TOY ARTIFACTS) (DOCUMENTATION PLAYTHING$TOY "an artifact designed to be played with") (HAS-I-TOPIC PLAYTHING$TOY |Play|) (WORD PLAYTHING$TOY |plaything|) (WORD PLAYTHING$TOY |toy|))) (DEFCONCEPT HAND$DEAL (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT HAND$DEAL GROUPS) (DOCUMENTATION HAND$DEAL "the cards held in a card game by a given player at any given time; ’I didn’t hold a good hand all evening’; ’he kept trying to see my hand’") (HAS-I-TOPIC HAND$DEAL |Card|) (WORD HAND$DEAL |hand|) (WORD HAND$DEAL |deal|))) (DEFCONCEPT TURN$PLAY (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT TURN$PLAY ACTS) (DOCUMENTATION TURN$PLAY "the activity of doing something in an agreed succession; ’it is my turn’ or ’it is still my play’") (HAS-I-TOPIC TURN$PLAY |Sport|) (WORD TURN$PLAY |turn|) (WORD TURN$PLAY |play|))) (DEFCONCEPT LEAD_4 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT LEAD_4 LOCATIONS) (DOCUMENTATION LEAD_4 "(baseball) the position taken by a base runner preparing to advance to the next base; ’he took a long lead off first’") (HAS-I-TOPIC LEAD_4 |Baseball|) (WORD LEAD_4 |lead|))) (DEFCONCEPT HOLE_2 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT HOLE_2 ARTIFACTS) (DOCUMENTATION HOLE_2 "one unit of play from tee to green on a golf course; ’he played 18 holes’") (HAS-I-TOPIC HOLE_2 |Golf|) (WORD HOLE_2 |hole|))) (DEFCONCEPT DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT DEFENSE$DEFENCE$DEFENSE_TEAM$ DEFENSE_LAWYERS GROUPS) (DOCUMENTATION DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS "the defendant and his legal advisors collectively; ’the defense called for a mistrial’") (HAS-I-TOPIC DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS |Law|) (WORD DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS |defense|) (WORD DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS |defence|) (WORD DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS |defense team|) (WORD DEFENSE$DEFENCE$DEFENSE_TEAM$DEFENSE_LAWYERS |defense lawyers|))) (DEFCONCEPT PROSECUTION_2 (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT PROSECUTION_2 GROUPS) (DOCUMENTATION PROSECUTION_2 "the lawyers acting for the state to put the case against the defendant") (HAS-I-TOPIC PROSECUTION_2 |Law|) (WORD PROSECUTION_2 |prosecution|))) (DEFCONCEPT BERTILLON_SYSTEM (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT BERTILLON_SYSTEM ACTS) (DOCUMENTATION BERTILLON_SYSTEM "a system or procedure for identifying persons") (HAS-I-TOPIC BERTILLON_SYSTEM |Law|) (WORD BERTILLON_SYSTEM |Bertillon system|))) (DEFCONCEPT LAW$JURISPRUDENCE (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT LAW$JURISPRUDENCE GROUPS)

311

(DOCUMENTATION LAW$JURISPRUDENCE "the collection of rules imposed by authority; ’civilization presupposes respect for the law’") (HAS-I-TOPIC LAW$JURISPRUDENCE |Law|) (WORD LAW$JURISPRUDENCE |law|) (WORD LAW$JURISPRUDENCE |jurisprudence|))) (DEFCONCEPT RIGHT_2 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT RIGHT_2 ATTRIBUTES) (DOCUMENTATION RIGHT_2 "an abstract idea of that which is due to a person or governmental body by law or tradition or nature: ’they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness’; ’Certain rights can never be granted to the government but must be kept in the hands of the people’- Eleanor Roosevelt; ’it is his right to say what he pleases’") (HAS-I-TOPIC RIGHT_2 |Law|) (WORD RIGHT_2 |right|))) (DEFCONCEPT ORGANIZED_CRIME$GANGLAND$GANGDOM (?SELF) :=> (SOCIAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ORGANIZED_CRIME$GANGLAND$GANGDOM GROUPS) (DOCUMENTATION ORGANIZED_CRIME$GANGLAND$GANGDOM "underworld organizations") (HAS-I-TOPIC ORGANIZED_CRIME$GANGLAND$GANGDOM |Law|) (HAS-I-TOPIC ORGANIZED_CRIME$GANGLAND$GANGDOM |Sociology|) (WORD ORGANIZED_CRIME$GANGLAND$GANGDOM |organized crime|) (WORD ORGANIZED_CRIME$GANGLAND$GANGDOM |gangland|) (WORD ORGANIZED_CRIME$GANGLAND$GANGDOM |gangdom|))) (DEFCONCEPT CIRCUIT (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT CIRCUIT GROUPS) (DOCUMENTATION CIRCUIT "(law) one of the twelve groups of states in the U.S. that is covered by a particular circuit court of appeals") (HAS-I-TOPIC CIRCUIT |Law|) (WORD CIRCUIT |circuit|))) (DEFCONCEPT COMMODITY$GOODS (?SELF) :=> (COMMERCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT COMMODITY$GOODS ARTIFACTS) (DOCUMENTATION COMMODITY$GOODS "articles of commerce") (HAS-I-TOPIC COMMODITY$GOODS |Commerce|) (WORD COMMODITY$GOODS |commodity|) (WORD COMMODITY$GOODS |goods|))) (DEFCONCEPT EXPORT (?SELF) :=> (COMMERCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT EXPORT ARTIFACTS) (DOCUMENTATION EXPORT "goods or services sold to a foreign country") (HAS-I-TOPIC EXPORT |Commerce|) (WORD EXPORT |export|))) (DEFCONCEPT IMPORT_1 (?SELF) :=> (COMMERCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT IMPORT_1 ARTIFACTS) (DOCUMENTATION IMPORT_1 "goods or services bought from a foreign country") (HAS-I-TOPIC IMPORT_1 |Commerce|) (WORD IMPORT_1 |import|))) (DEFCONCEPT LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$ LINE_OF_BUSINESS (?SELF) :=> (COMMERCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS ARTIFACTS) (DOCUMENTATION LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS "a particular kind of product; ’a nice line of shoes’") (HAS-I-TOPIC LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS |Commerce|) (WORD LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS

312

|line|) (WORD LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS |product line|) (WORD LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS |line of products|) (WORD LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS |line of merchandise|) (WORD LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS |business line|) (WORD LINE$PRODUCT_LINE$LINE_OF_PRODUCTS$LINE_OF_MERCHANDISE$ BUSINESS_LINE$LINE_OF_BUSINESS |line of business|))) (DEFCONCEPT MERCHANDISE$WARES$PRODUCT (?SELF) :=> (COMMERCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT MERCHANDISE$WARES$PRODUCT ARTIFACTS) (DOCUMENTATION MERCHANDISE$WARES$PRODUCT "commodities offered for sale; ’good business depends on having good merchandise’; ’that store offers a variety of products’") (HAS-I-TOPIC MERCHANDISE$WARES$PRODUCT |Commerce|) (WORD MERCHANDISE$WARES$PRODUCT |merchandise|) (WORD MERCHANDISE$WARES$PRODUCT |wares|) (WORD MERCHANDISE$WARES$PRODUCT |product|))) (DEFCONCEPT CONSUMER_GOODS (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT CONSUMER_GOODS ARTIFACTS) (DOCUMENTATION CONSUMER_GOODS "goods (as food or clothing) intended for direct use or consumption") (HAS-I-TOPIC CONSUMER_GOODS |Commerce|) (WORD CONSUMER_GOODS |consumer goods|))) (DEFCONCEPT DRYGOODS$SOFT_GOODS (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT DRYGOODS$SOFT_GOODS ARTIFACTS) (DOCUMENTATION DRYGOODS$SOFT_GOODS "textiles or clothing and related merchandise") (HAS-I-TOPIC DRYGOODS$SOFT_GOODS |Commerce|) (WORD DRYGOODS$SOFT_GOODS |drygoods|) (WORD DRYGOODS$SOFT_GOODS |soft goods|))) (DEFCONCEPT BASIC$STAPLE (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT BASIC$STAPLE ARTIFACTS) (DOCUMENTATION BASIC$STAPLE "(usually plural) a necessary commodity for which demand is constant") (HAS-I-TOPIC BASIC$STAPLE |Commerce|) (WORD BASIC$STAPLE |basic|) (WORD BASIC$STAPLE |staple|))) (DEFCONCEPT ENTRANT_1 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ENTRANT_1 ARTIFACTS) (DOCUMENTATION ENTRANT_1 "a commodity that enters competition with established merchandise; ’a well publicized entrant is the pocket computer’") (HAS-I-TOPIC ENTRANT_1 |Commerce|) (WORD ENTRANT_1 |entrant|))) (DEFCONCEPT MIDDLING (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT MIDDLING ARTIFACTS) (DOCUMENTATION MIDDLING "any commodity of intermediate quality or size (especially when coarse particles of ground wheat are mixed with bran)") (HAS-I-TOPIC MIDDLING |Commerce|) (WORD MIDDLING |middling|))) (DEFCONCEPT TOP_OF_THE_LINE (?SELF)

313

:=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT TOP_OF_THE_LINE ARTIFACTS) (DOCUMENTATION TOP_OF_THE_LINE "the best (most expensive) in a given line of merchandise") (HAS-I-TOPIC TOP_OF_THE_LINE |Commerce|) (WORD TOP_OF_THE_LINE |top of the line|))) (DEFCONCEPT SALE_3 (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT SALE_3 STATES) (DOCUMENTATION SALE_3 "the state of being purchasable; offered or exhibited for selling; ’vitamin C is on sale at most pharmacies’; ’the new line of cars will soon be on sale’") (HAS-I-TOPIC SALE_3 |Commerce|) (WORD SALE_3 |sale|))) (DEFCONCEPT JOB_LOT (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT JOB_LOT GROUPS) (DOCUMENTATION JOB_LOT "a miscellaneous collection of things sold together") (HAS-I-TOPIC JOB_LOT |Commerce|) (WORD JOB_LOT |job lot|))) (DEFCONCEPT PACKAGE$BUNDLE$PACKET$PARCEL (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT PACKAGE$BUNDLE$PACKET$PARCEL GROUPS) (DOCUMENTATION PACKAGE$BUNDLE$PACKET$PARCEL "a collection of things wrapped or boxed together") (HAS-I-TOPIC PACKAGE$BUNDLE$PACKET$PARCEL |Commerce|) (WORD PACKAGE$BUNDLE$PACKET$PARCEL |package|) (WORD PACKAGE$BUNDLE$PACKET$PARCEL |bundle|) (WORD PACKAGE$BUNDLE$PACKET$PARCEL |packet|) (WORD PACKAGE$BUNDLE$PACKET$PARCEL |parcel|))) (DEFCONCEPT SUM$TOTAL$TOTALITY$AGGREGATE (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT SUM$TOTAL$TOTALITY$AGGREGATE ARTIFACTS) (DOCUMENTATION SUM$TOTAL$TOTALITY$AGGREGATE "the whole") (HAS-I-TOPIC SUM$TOTAL$TOTALITY$AGGREGATE |Economy|) (WORD SUM$TOTAL$TOTALITY$AGGREGATE |sum|) (WORD SUM$TOTAL$TOTALITY$AGGREGATE |total|) (WORD SUM$TOTAL$TOTALITY$AGGREGATE |totality|) (WORD SUM$TOTAL$TOTALITY$AGGREGATE |aggregate|))) (DEFCONCEPT CRASH$COLLAPSE (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CRASH$COLLAPSE EVENTS) (DOCUMENTATION CRASH$COLLAPSE "a sudden large decline of business or the prices of stocks (especially one that causes additional failures)") (HAS-I-TOPIC CRASH$COLLAPSE |Exchange|) (WORD CRASH$COLLAPSE |crash|) (WORD CRASH$COLLAPSE |collapse|))) (DEFCONCEPT DOCUMENT_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT DOCUMENT_2 POSSESSION) (DOCUMENTATION DOCUMENT_2 "a written account of ownership or obligation") (HAS-I-TOPIC DOCUMENT_2 |Administration|) (HAS-I-TOPIC DOCUMENT_2 |Economy|) (WORD DOCUMENT_2 |document|))) (DEFCONCEPT FACILITY$INSTALLATION (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT FACILITY$INSTALLATION ARTIFACTS) (DOCUMENTATION FACILITY$INSTALLATION "something created to provide a particular service; ’the assembly plant is an enormous facility’") (HAS-I-TOPIC FACILITY$INSTALLATION |Economy|) (WORD FACILITY$INSTALLATION |facility|) (WORD FACILITY$INSTALLATION |installation|))) (DEFCONCEPT ASSET (?SELF) :=> (FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ASSET POSSESSION) (DOCUMENTATION ASSET "anything of material value or usefulness") (HAS-I-TOPIC ASSET |Economy|) (WORD ASSET |asset|))) (DEFCONCEPT LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$ PECUNIARY_OBLIGATION (?SELF)

314

:=> (LEGAL-POSSESSION-ENTITY ?SELF) :AXIOMS (AND (SUBJECT LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION POSSESSION) (DOCUMENTATION LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION "possession that is owed to someone else") (HAS-I-TOPIC LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION |Economy|) (WORD LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION |liability|) (WORD LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION |financial_obligation|) (WORD LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION |indebtedness|) (WORD LIABILITY$FINANCIAL_OBLIGATION$INDEBTEDNESS$PECUNIARY_OBLIGATION |pecuniary_obligation|))) (DEFCONCEPT OWNERSHIP_1 (?SELF) :=> (LEGAL-POSSESSION-ENTITY ?SELF) :AXIOMS (AND (SUBJECT OWNERSHIP_1 POSSESSION) (DOCUMENTATION OWNERSHIP_1 "possession with the right to transfer possession to others") (HAS-I-TOPIC OWNERSHIP_1 |Economy|) (WORD OWNERSHIP_1 |ownership|))) (DEFCONCEPT PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION (?SELF) :=> (LEGAL-POSSESSION-ENTITY ?SELF) :AXIOMS (AND (SUBJECT PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION POSSESSION) (DOCUMENTATION PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION "any tangible possession that is owned by someone; ’that hat is my property’") (HAS-I-TOPIC PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION |Economy|) (WORD PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION |property|) (WORD PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION |belongings|) (WORD PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION |holding|) (WORD PROPERTY$BELONGINGS$HOLDING$MATERIAL_POSSESSION |material_possession|))) (DEFCONCEPT RECEIVERSHIP_3 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT RECEIVERSHIP_3 STATES) (DOCUMENTATION RECEIVERSHIP_3 "the state of property that is in the hands of a receiver; ’the business is in receivership’") (HAS-I-TOPIC RECEIVERSHIP_3 |Economy|) (WORD RECEIVERSHIP_3 |receivership|))) (DEFCONCEPT BUSINESS_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT BUSINESS_RELATION RELATIONS) (DOCUMENTATION BUSINESS_RELATION "a relation between different business enterprises") (HAS-I-TOPIC BUSINESS_RELATION |Economy|) (WORD BUSINESS_RELATION |business_relation|))) (DEFCONCEPT FINANCIAL_CONDITION$ECONOMIC_CONDITION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT FINANCIAL_CONDITION$ECONOMIC_CONDITION STATES) (DOCUMENTATION FINANCIAL_CONDITION$ECONOMIC_CONDITION "the condition of finances") (HAS-I-TOPIC FINANCIAL_CONDITION$ECONOMIC_CONDITION |Economy|) (WORD FINANCIAL_CONDITION$ECONOMIC_CONDITION |financial_condition|) (WORD FINANCIAL_CONDITION$ECONOMIC_CONDITION |economic_condition|))) (DEFCONCEPT OWNERSHIP_2 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT OWNERSHIP_2 STATES) (DOCUMENTATION OWNERSHIP_2 "the state or fact of being an owner")

315

(HAS-I-TOPIC OWNERSHIP_2 |Economy|) (WORD OWNERSHIP_2 |ownership|))) (DEFCONCEPT MARKET$MARKETPLACE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT MARKET$MARKETPLACE ACTS) (DOCUMENTATION MARKET$MARKETPLACE "the world of commercial activity where goods and services are bought and sold; ’without competition there would be no market’; ’they were driven from the marketplace’") (HAS-I-TOPIC MARKET$MARKETPLACE |Exchange|) (WORD MARKET$MARKETPLACE |market|) (WORD MARKET$MARKETPLACE |marketplace|))) (DEFCONCEPT ENTERPRISE (?SELF) :=> (ORGANIZATION$ORGANISATION_2 ?SELF) :AXIOMS (AND (SUBJECT ENTERPRISE GROUPS) (DOCUMENTATION ENTERPRISE "an organization created for business ventures; ’a growing enterprise must have a bold leader’") (HAS-I-TOPIC ENTERPRISE |Enterprise|) (WORD ENTERPRISE |enterprise|))) (DEFCONCEPT EMPLOYMENT$EMPLOY (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT EMPLOYMENT$EMPLOY STATES) (DOCUMENTATION EMPLOYMENT$EMPLOY "the state of being employed or having a job; ’they are looking for employment’; ’he was in the employ of the city’") (HAS-I-TOPIC EMPLOYMENT$EMPLOY |Enterprise|) (WORD EMPLOYMENT$EMPLOY |employment|) (WORD EMPLOYMENT$EMPLOY |employ|))) (DEFCONCEPT UNEMPLOYMENT (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT UNEMPLOYMENT STATES) (DOCUMENTATION UNEMPLOYMENT "the state of being unemployed or not having a job: ’unemployment is a serious social evil’; ’the rate of unemployment is an indicator of the health of an economy’") (HAS-I-TOPIC UNEMPLOYMENT |Enterprise|) (WORD UNEMPLOYMENT |unemployment|))) (DEFCONCEPT FLEET_3 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT FLEET_3 GROUPS) (DOCUMENTATION FLEET_3 "group of motor vehicles operating together under the same ownership") (HAS-I-TOPIC FLEET_3 |Economy|) (HAS-I-TOPIC FLEET_3 |Military|) (HAS-I-TOPIC FLEET_3 |Transport|) (WORD FLEET_3 |fleet|))) (DEFCONCEPT FLEET_4 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT FLEET_4 GROUPS) (DOCUMENTATION FLEET_4 "group of aircraft operating together under the same ownership") (HAS-I-TOPIC FLEET_4 |Economy|) (HAS-I-TOPIC FLEET_4 |Transport|) (WORD FLEET_4 |fleet|))) (DEFCONCEPT AUTOMATON$ROBOT$GOLEM (?SELF) :=> (AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT AUTOMATON$ROBOT$GOLEM ARTIFACTS) (DOCUMENTATION AUTOMATON$ROBOT$GOLEM "a mechanism that can move automatically") (HAS-I-TOPIC AUTOMATON$ROBOT$GOLEM |Industry|) (HAS-I-TOPIC AUTOMATON$ROBOT$GOLEM |Mechanics|) (WORD AUTOMATON$ROBOT$GOLEM |automaton|) (WORD AUTOMATON$ROBOT$GOLEM |robot|) (WORD AUTOMATON$ROBOT$GOLEM |golem|))) (DEFCONCEPT EXCAVATION$HOLE_IN_THE_GROUND (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT EXCAVATION$HOLE_IN_THE_GROUND ARTIFACTS) (DOCUMENTATION EXCAVATION$HOLE_IN_THE_GROUND "a hole made by excavating") (HAS-I-TOPIC EXCAVATION$HOLE_IN_THE_GROUND |Industry|) (WORD EXCAVATION$HOLE_IN_THE_GROUND |excavation|) (WORD EXCAVATION$HOLE_IN_THE_GROUND |hole in the ground|))) (DEFCONCEPT PADDING$CUSHIONING (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT PADDING$CUSHIONING ARTIFACTS)

316

(DOCUMENTATION PADDING$CUSHIONING "soft or resilient material used to fill or give shape or protect or add comfort") (HAS-I-TOPIC PADDING$CUSHIONING |Industry|) (WORD PADDING$CUSHIONING |padding|) (WORD PADDING$CUSHIONING |cushioning|))) (DEFCONCEPT FABRIC$CLOTH$MATERIAL$TEXTILE (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT FABRIC$CLOTH$MATERIAL$TEXTILE ARTIFACTS) (DOCUMENTATION FABRIC$CLOTH$MATERIAL$TEXTILE "something made by weaving or felting or knitting or crocheting natural or synthetic fibers") (HAS-I-TOPIC FABRIC$CLOTH$MATERIAL$TEXTILE |Industry|) (WORD FABRIC$CLOTH$MATERIAL$TEXTILE |fabric|) (WORD FABRIC$CLOTH$MATERIAL$TEXTILE |cloth|) (WORD FABRIC$CLOTH$MATERIAL$TEXTILE |material|) (WORD FABRIC$CLOTH$MATERIAL$TEXTILE |textile|))) (DEFCONCEPT FIELD_4 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT FIELD_4 LOCATIONS) (DOCUMENTATION FIELD_4 "a region in which military operations are in progress; ’the army was in the field awaiting action’") (HAS-I-TOPIC FIELD_4 |Military|) (WORD FIELD_4 |field|))) (DEFCONCEPT MILITARY_POSITION$POSITION (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT MILITARY_POSITION$POSITION LOCATIONS) (DOCUMENTATION MILITARY_POSITION$POSITION "a point occupied by troops for tactical reasons") (HAS-I-TOPIC MILITARY_POSITION$POSITION |Military|) (WORD MILITARY_POSITION$POSITION |military_position|) (WORD MILITARY_POSITION$POSITION |position|))) (DEFCONCEPT READINESS$PREPAREDNESS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT READINESS$PREPAREDNESS STATES) (DOCUMENTATION READINESS$PREPAREDNESS "the state of being ready or prepared for use or action (especially military action); ’putting them in readiness’") (HAS-I-TOPIC READINESS$PREPAREDNESS |Military|) (WORD READINESS$PREPAREDNESS |readiness|) (WORD READINESS$PREPAREDNESS |preparedness|))) (DEFCONCEPT AVIATION$AIR_POWER (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT AVIATION$AIR_POWER GROUPS) (DOCUMENTATION AVIATION$AIR_POWER "the aggregation of a country’s military aircraft") (HAS-I-TOPIC AVIATION$AIR_POWER |Military|) (WORD AVIATION$AIR_POWER |aviation|) (WORD AVIATION$AIR_POWER |air_power|))) (DEFCONCEPT CONVOY_2 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT CONVOY_2 GROUPS) (DOCUMENTATION CONVOY_2 "a collection of merchant ships with an escort of warships") (HAS-I-TOPIC CONVOY_2 |Military|) (WORD CONVOY_2 |convoy|))) (DEFCONCEPT FLEET_1 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT FLEET_1 GROUPS) (DOCUMENTATION FLEET_1 "a group of warships organized as a tactical unit") (HAS-I-TOPIC FLEET_1 |Military|) (WORD FLEET_1 |fleet|))) (DEFCONCEPT CITIZENRY$PEOPLE (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT CITIZENRY$PEOPLE GROUPS) (DOCUMENTATION CITIZENRY$PEOPLE "the body of citizens of a state or country; ’the Spanish people’") (HAS-I-TOPIC CITIZENRY$PEOPLE |Politics|) (WORD CITIZENRY$PEOPLE |citizenry|) (WORD CITIZENRY$PEOPLE |people|))) (DEFCONCEPT MOVEMENT$FRONT (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT MOVEMENT$FRONT GROUPS)

317

(DOCUMENTATION MOVEMENT$FRONT "a group of people with a common ideology who try together to achieve certain general goals; ’he was a charter member of the movement’; ’politicians have to respect a mass movement’; ’he led the national liberation front’") (HAS-I-TOPIC MOVEMENT$FRONT |Politics|) (WORD MOVEMENT$FRONT |movement|) (WORD MOVEMENT$FRONT |front|))) (DEFCONCEPT NONALIGNMENT$NONALINEMENT (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT NONALIGNMENT$NONALINEMENT GROUPS) (DOCUMENTATION NONALIGNMENT$NONALINEMENT "people (or countries) who are not aligned with other people (or countries) in a pact or treaty") (HAS-I-TOPIC NONALIGNMENT$NONALINEMENT |Politics|) (WORD NONALIGNMENT$NONALINEMENT |nonalignment|) (WORD NONALIGNMENT$NONALINEMENT |nonalinement|))) (DEFCONCEPT THIRD_WORLD (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT THIRD_WORLD GROUPS) (DOCUMENTATION THIRD_WORLD "underdeveloped and developing countries of Asia and Africa and Latin America collectively; neutral in the East-West alignment") (HAS-I-TOPIC THIRD_WORLD |Politics|) (WORD THIRD_WORLD |Third World|))) (DEFCONCEPT MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE GROUPS) (DOCUMENTATION MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE "the common people generally; ’separate the warriors from the mass’; ’power to the people’") (HAS-I-TOPIC MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE |Politics|) (WORD MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE |multitude|) (WORD MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE |masses|) (WORD MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE |mass|) (WORD MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE |hoi polloi|) (WORD MULTITUDE$MASSES$MASS$HOI_POLLOI$PEOPLE |people|))) (DEFCONCEPT IRREDENTA$IRRIDENTA (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT IRREDENTA$IRRIDENTA LOCATIONS) (DOCUMENTATION IRREDENTA$IRRIDENTA "a region that is related ethnically or historically to one country but is controlled politically by another") (HAS-I-TOPIC IRREDENTA$IRRIDENTA |Politics|) (WORD IRREDENTA$IRRIDENTA |irredenta|) (WORD IRREDENTA$IRRIDENTA |irridenta|))) (DEFCONCEPT POLLS (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT POLLS LOCATIONS) (DOCUMENTATION POLLS "the place where people vote") (HAS-I-TOPIC POLLS |Politics|) (WORD POLLS |polls|))) (DEFCONCEPT POLITICAL_SYSTEM$FORM_OF_GOVERNMENT (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT POLITICAL_SYSTEM$FORM_OF_GOVERNMENT GROUPS) (DOCUMENTATION POLITICAL_SYSTEM$FORM_OF_GOVERNMENT "the members of a social organization who are in power") (HAS-I-TOPIC POLITICAL_SYSTEM$FORM_OF_GOVERNMENT |Anthropology|) (HAS-I-TOPIC POLITICAL_SYSTEM$FORM_OF_GOVERNMENT |Politics|) (HAS-I-TOPIC POLITICAL_SYSTEM$FORM_OF_GOVERNMENT |Sociology|) (WORD POLITICAL_SYSTEM$FORM_OF_GOVERNMENT |political_system|) (WORD POLITICAL_SYSTEM$FORM_OF_GOVERNMENT |form_of_government|))) (DEFCONCEPT POLITICS$POLITICAL_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT POLITICS$POLITICAL_RELATION RELATIONS) (DOCUMENTATION POLITICS$POLITICAL_RELATION "social relations involving authority or power") (HAS-I-TOPIC POLITICS$POLITICAL_RELATION |Politics|) (WORD POLITICS$POLITICAL_RELATION |politics|) (WORD POLITICS$POLITICAL_RELATION |political_relation|))) (DEFCONCEPT OFFICE$POWER (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT OFFICE$POWER STATES)

318

(DOCUMENTATION OFFICE$POWER "(of a government or government official) holding an office means being in power; ’being in office already gives a candidate a great advantage’; ’during his first year in power’") (HAS-I-TOPIC OFFICE$POWER |Politics|) (WORD OFFICE$POWER |office|) (WORD OFFICE$POWER |power|))) (DEFCONCEPT FREE_WORLD (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT FREE_WORLD GROUPS) (DOCUMENTATION FREE_WORLD "anti-Communist countries collectively") (HAS-I-TOPIC FREE_WORLD |Politics|) (WORD FREE_WORLD |Free World|))) (DEFCONCEPT EDITION_3 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT EDITION_3 GROUPS) (DOCUMENTATION EDITION_3 "all of the identical copies of something offered to the public at the same time; ’the first edition appeared in 1920’ or ’it was too late for the morning edition’ or ’they issued a limited edition of Bach recordings’") (HAS-I-TOPIC EDITION_3 |Publishing|) (WORD EDITION_3 |edition|))) (DEFCONCEPT INTEREST$INTEREST_GROUP (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT INTEREST$INTEREST_GROUP GROUPS) (DOCUMENTATION INTEREST$INTEREST_GROUP "(usually plural) a social group whose members control some field of activity and who have common aims; ’the iron interests stepped up production’") (HAS-I-TOPIC INTEREST$INTEREST_GROUP |Sociology|) (WORD INTEREST$INTEREST_GROUP |interest|) (WORD INTEREST$INTEREST_GROUP |interest group|))) (DEFCONCEPT KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$ TRIBE GROUPS) (DOCUMENTATION KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE "group of people related by blood or marriage") (HAS-I-TOPIC KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |Sociology|) (WORD KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |kin|) (WORD KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |kin group|) (WORD KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |kinship group|) (WORD KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |kindred|) (WORD KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |clan|) (WORD KIN$KIN_GROUP$KINSHIP_GROUP$KINDRED$CLAN$TRIBE |tribe|))) (DEFCONCEPT MINORITY_2 (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT MINORITY_2 GROUPS) (DOCUMENTATION MINORITY_2 "a group of people who differ racially or politically from a larger group of which it is a part") (HAS-I-TOPIC MINORITY_2 |Anthropology|) (HAS-I-TOPIC MINORITY_2 |Sociology|) (WORD MINORITY_2 |minority|))) (DEFCONCEPT SOCIETY (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT SOCIETY GROUPS) (DOCUMENTATION SOCIETY "an extended social group having a distinctive cultural and economic organization") (HAS-I-TOPIC SOCIETY |Anthropology|) (HAS-I-TOPIC SOCIETY |Sociology|) (WORD SOCIETY |society|))) (DEFCONCEPT SOCIAL_EVENT (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT SOCIAL_EVENT EVENTS) (DOCUMENTATION SOCIAL_EVENT "an event characteristic of persons forming groups") (HAS-I-TOPIC SOCIAL_EVENT |Sociology|) (WORD SOCIAL_EVENT |social event|))) (DEFCONCEPT PLATOON_3 (?SELF) :=> (QUALITATIVE-ROLE ?SELF) :AXIOMS (AND (SUBJECT PLATOON_3 GROUPS) (DOCUMENTATION PLATOON_3 "a group of persons who are engaged in a common activity; ’platoons of tourists poured

319

out of the busses’; ’the defensive platoon of the football team’") (HAS-I-TOPIC PLATOON_3 |Sociology|) (WORD PLATOON_3 |platoon|))) (DEFCONCEPT STATUS$POSITION (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT STATUS$POSITION STATES) (DOCUMENTATION STATUS$POSITION "the relative position or standing of things or especially persons in a society: ’he had the status of a minor’; ’the novel attained the status of a classic’; ’atheists do not enjoy a favorable position in American life’") (HAS-I-TOPIC STATUS$POSITION |Sociology|) (WORD STATUS$POSITION |status|) (WORD STATUS$POSITION |position|))) (DEFCONCEPT KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP RELATIONS) (DOCUMENTATION KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP "state of relatedness or connection by blood or marriage or adoption") (HAS-I-TOPIC KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP |Anthropology|) (HAS-I-TOPIC KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP |Sociology|) (WORD KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP |kinship|) (WORD KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP |family_relationship|) (WORD KINSHIP$FAMILY_RELATIONSHIP$RELATIONSHIP |relationship|))) (DEFCONCEPT PRACTICE_3 (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT PRACTICE_3 COGNITION) (DOCUMENTATION PRACTICE_3 "knowledge of how something is customarily done: ’it is not the local practice to wear shorts to dinner’") (HAS-I-TOPIC PRACTICE_3 |Sociology|) (WORD PRACTICE_3 |practice|))) (DEFCONCEPT STRATIFICATION$SOCIAL_STRATIFICATION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT STRATIFICATION$SOCIAL_STRATIFICATION STATES) (DOCUMENTATION STRATIFICATION$SOCIAL_STRATIFICATION "the condition of being arranged in social strata or classes") (HAS-I-TOPIC STRATIFICATION$SOCIAL_STRATIFICATION |Sociology|) (WORD STRATIFICATION$SOCIAL_STRATIFICATION |stratification|) (WORD STRATIFICATION$SOCIAL_STRATIFICATION |social_stratification|))) (DEFCONCEPT WRONGDOING$MISCONDUCT (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT WRONGDOING$MISCONDUCT ACTS) (DOCUMENTATION WRONGDOING$MISCONDUCT "activity that transgresses moral or civil law; ’he denied any wrongdoing’") (HAS-I-TOPIC WRONGDOING$MISCONDUCT |Sociology|) (WORD WRONGDOING$MISCONDUCT |wrongdoing|) (WORD WRONGDOING$MISCONDUCT |misconduct|))) (DEFCONCEPT MESSAGE (?SELF) :=> (INFORMATION-OBJECT ?SELF) :AXIOMS (AND (SUBJECT MESSAGE COMMUNICATION) (DOCUMENTATION MESSAGE "a communication (usually brief) that is written or spoken or signaled; ’he sent a three-word message’") (HAS-I-TOPIC MESSAGE |Telecommunication|) (WORD MESSAGE |message|))) (DEFCONCEPT MAIL_3 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT MAIL_3 GROUPS) (DOCUMENTATION MAIL_3 "any particular collection of letters or packages that is delivered; ’your mail is on the table’") (HAS-I-TOPIC MAIL_3 |Post|) (WORD MAIL_3 |mail|))) (DEFCONCEPT SERVICE_AREA (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT SERVICE_AREA LOCATIONS) (DOCUMENTATION SERVICE_AREA "place on a highway providing garage services and eating and toilet facilities") (HAS-I-TOPIC SERVICE_AREA |Tourism|) (WORD SERVICE_AREA |service_area|))) (DEFCONCEPT TRAFFIC_2 (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT TRAFFIC_2 GROUPS)

320

(DOCUMENTATION TRAFFIC_2 "the aggregation of things (pedestrians or vehicles or messages) coming and going in a particular locality") (HAS-I-TOPIC TRAFFIC_2 |Town_Planning|) (HAS-I-TOPIC TRAFFIC_2 |Transport|) (WORD TRAFFIC_2 |traffic|))) (DEFCONCEPT WAY_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT WAY_2 ARTIFACTS) (DOCUMENTATION WAY_2 "any road or path affording passage from one place to another; ’he said he was looking for the way out’") (HAS-I-TOPIC WAY_2 |Transport|) (WORD WAY_2 |way|))) (DEFCONCEPT JUNCTION (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT JUNCTION ARTIFACTS) (DOCUMENTATION JUNCTION "the place where two things come together") (HAS-I-TOPIC JUNCTION |Transport|) (WORD JUNCTION |junction|))) (DEFCONCEPT PORT (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT PORT LOCATIONS) (DOCUMENTATION PORT "a place (seaport or airport) where people and merchandise can enter or leave a country") (HAS-I-TOPIC PORT |Geography|) (HAS-I-TOPIC PORT |Merchant_Navy|) (WORD PORT |port|))) (DEFCONCEPT STATION_2 (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT STATION_2 LOCATIONS) (DOCUMENTATION STATION_2 "(Navy) the location to which a ship or fleet is assigned for duty") (HAS-I-TOPIC STATION_2 |Merchant_Navy|) (WORD STATION_2 |station|))) (DEFCONCEPT BALLAST (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT BALLAST ARTIFACTS) (DOCUMENTATION BALLAST "used to stabilize a ship or airship") (HAS-I-TOPIC BALLAST |Transport|) (WORD BALLAST |ballast|))) (DEFCONCEPT ATMOSPHERE_1 (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT ATMOSPHERE_1 LOCATIONS) (DOCUMENTATION ATMOSPHERE_1 "the mass of air surrounding the Earth; ’there was great heat as the comet entered the atmosphere’") (HAS-I-TOPIC ATMOSPHERE_1 |Astronomy|) (WORD ATMOSPHERE_1 |atmosphere|))) (DEFCONCEPT HELIOSPHERE (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT HELIOSPHERE LOCATIONS) (DOCUMENTATION HELIOSPHERE "the region inside the heliopause containing the sun and solar system") (HAS-I-TOPIC HELIOSPHERE |Astronomy|) (WORD HELIOSPHERE |heliosphere|))) (DEFCONCEPT CELESTIAL_POINT (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT CELESTIAL_POINT LOCATIONS) (DOCUMENTATION CELESTIAL_POINT "a point in the heavens (on the celestial sphere)") (HAS-I-TOPIC CELESTIAL_POINT |Astronomy|) (WORD CELESTIAL_POINT |celestial_point|))) (DEFCONCEPT ASTERISM_1 (?SELF) :=> (GEOGRAPHICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ASTERISM_1 OBJECTS) (DOCUMENTATION ASTERISM_1 "(astronomy) a cluster of stars (or a small constellation)") (HAS-I-TOPIC ASTERISM_1 |Astronomy|) (WORD ASTERISM_1 |asterism|))) (DEFCONCEPT CONSTELLATION (?SELF) :=> (GEOGRAPHICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT CONSTELLATION OBJECTS) (DOCUMENTATION CONSTELLATION "a configuration of stars as seen from the earth") (HAS-I-TOPIC CONSTELLATION |Astronomy|)

321

(WORD CONSTELLATION |constellation|))) (DEFCONCEPT ZODIAC_2 (?SELF) :=> (GEOGRAPHICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ZODIAC_2 LOCATIONS) (DOCUMENTATION ZODIAC_2 "a belt-shaped region in the heavens on either side to the ecliptic; divided into 12 constellations or signs for astrological purposes") (HAS-I-TOPIC ZODIAC_2 |Astronomy|) (WORD ZODIAC_2 |zodiac|))) (DEFCONCEPT CELESTIAL_BODY$HEAVENLY_BODY (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT CELESTIAL_BODY$HEAVENLY_BODY OBJECTS) (DOCUMENTATION CELESTIAL_BODY$HEAVENLY_BODY "natural objects visible in the sky") (HAS-I-TOPIC CELESTIAL_BODY$HEAVENLY_BODY |Astronomy|) (WORD CELESTIAL_BODY$HEAVENLY_BODY |celestial_body|) (WORD CELESTIAL_BODY$HEAVENLY_BODY |heavenly_body|))) (DEFCONCEPT UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$ MACROCOSM (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$ MACROCOSM OBJECTS) (DOCUMENTATION UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM "everything that exists anywhere; ’they study the evolution of the universe’; ’the biggest tree in existence’") (HAS-I-TOPIC UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |Astronomy|) (HAS-I-TOPIC UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |Physics|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |universe|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |existence|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |nature|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |creation|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |world|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |cosmos|) (WORD UNIVERSE$EXISTENCE$NATURE$CREATION$WORLD$COSMOS$MACROCOSM |macrocosm|))) (DEFCONCEPT ANOMALY (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT ANOMALY LOCATIONS) (DOCUMENTATION ANOMALY "(astronomy) position of a planet as defined by its angular distance from its perihelion (as observed from the sun)") (HAS-I-TOPIC ANOMALY |Astronomy|) (WORD ANOMALY |anomaly|))) (DEFCONCEPT MAGNITUDE_RELATION (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT MAGNITUDE_RELATION RELATIONS) (DOCUMENTATION MAGNITUDE_RELATION "a relation between magnitudes") (HAS-I-TOPIC MAGNITUDE_RELATION |Astronomy|) (WORD MAGNITUDE_RELATION |magnitude_relation|))) (DEFCONCEPT GALAXY$EXTRAGALACTIC_NEBULA (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT GALAXY$EXTRAGALACTIC_NEBULA GROUPS) (DOCUMENTATION GALAXY$EXTRAGALACTIC_NEBULA "(astronomy) a collection of star systems; any of the billions of systems each having many stars and nebulae and dust; ’extragalactic nebula’ is a former name for ’galaxy’’") (HAS-I-TOPIC GALAXY$EXTRAGALACTIC_NEBULA |Astronomy|) (WORD GALAXY$EXTRAGALACTIC_NEBULA |galaxy|)

322

(WORD GALAXY$EXTRAGALACTIC_NEBULA |extragalactic nebula|))) (DEFCONCEPT OORT_CLOUD (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT OORT_CLOUD GROUPS) (DOCUMENTATION OORT_CLOUD "(astronomy) a hypothetical huge collection of comets orbiting the sun far beyond the orbit of Pluto; perturbations (as by other stars) can upset a comet’s orbit and may send it tumbling toward the sun") (HAS-I-TOPIC OORT_CLOUD |Astronomy|) (WORD OORT_CLOUD |Oort cloud|))) (DEFCONCEPT SET_5 (?SELF) :=> (SET ?SELF) :AXIOMS (AND (SUBJECT SET_5 GROUPS) (DOCUMENTATION SET_5 "an abstract collection of numbers or symbols; ’the set of prime numbers is infinite’") (HAS-I-TOPIC SET_5 |Mathematics|) (WORD SET_5 |set|))) (DEFCONCEPT QUANTITY_2 (?SELF) :=> (ABSTRACT-REGION ?SELF) :AXIOMS (AND (SUBJECT QUANTITY_2 COGNITION) (DOCUMENTATION QUANTITY_2 "something that has a magnitude and can be represented in mathematical expressions by a constant or a variable") (HAS-I-TOPIC QUANTITY_2 |Mathematics|) (WORD QUANTITY_2 |quantity|))) (DEFCONCEPT CALCULATION$COMPUTATION (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT CALCULATION$COMPUTATION ACTS) (DOCUMENTATION CALCULATION$COMPUTATION "the procedure of calculating; determining something by mathematical or logical methods") (HAS-I-TOPIC CALCULATION$COMPUTATION |Mathematics|) (WORD CALCULATION$COMPUTATION |calculation|) (WORD CALCULATION$COMPUTATION |computation|))) (DEFCONCEPT RULE$FORMULA (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT RULE$FORMULA COGNITION) (DOCUMENTATION RULE$FORMULA "(mathematics) a standard procedure for solving a class of problems; ’he determined the upper bound with Descartes’ rule of signs’; ’he gave us a general formula for attacking polynomials’") (HAS-I-TOPIC RULE$FORMULA |Mathematics|) (WORD RULE$FORMULA |rule|) (WORD RULE$FORMULA |formula|))) (DEFCONCEPT SEGMENT (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT SEGMENT OBJECTS) (DOCUMENTATION SEGMENT "one of the parts into which something naturally divides: ’a segment of an orange’") (HAS-I-TOPIC SEGMENT |Geometry|) (WORD SEGMENT |segment|))) (DEFCONCEPT GEODESIC$GEODESIC_LINE (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT GEODESIC$GEODESIC_LINE SHAPES) (DOCUMENTATION GEODESIC$GEODESIC_LINE "(mathematics) the shortest line between two points on a mathematically defined surface (as a straight line on a plane or a an arc of a great circle on a sphere)") (HAS-I-TOPIC GEODESIC$GEODESIC_LINE |Mathematics|) (WORD GEODESIC$GEODESIC_LINE |geodesic|) (WORD GEODESIC$GEODESIC_LINE |geodesic_line|))) (DEFCONCEPT CENTER$CENTRE$MIDPOINT (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT CENTER$CENTRE$MIDPOINT LOCATIONS) (DOCUMENTATION CENTER$CENTRE$MIDPOINT "a point equidistant from the ends of a line or the extremities of a figure") (HAS-I-TOPIC CENTER$CENTRE$MIDPOINT |Geometry|) (WORD CENTER$CENTRE$MIDPOINT |center|) (WORD CENTER$CENTRE$MIDPOINT |centre|) (WORD CENTER$CENTRE$MIDPOINT |midpoint|))) (DEFCONCEPT CORNER_1 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT CORNER_1 LOCATIONS) (DOCUMENTATION CORNER_1 "the point where two lines meet or intersect; ’the corners of a rectangle’")

323

(HAS-I-TOPIC CORNER_1 |Geometry|) (WORD CORNER_1 |corner|))) (DEFCONCEPT CORNER_4 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT CORNER_4 LOCATIONS) (DOCUMENTATION CORNER_4 "the point where three areas or surfaces meet or intersect; ’the corners of a cube’") (HAS-I-TOPIC CORNER_4 |Geometry|) (WORD CORNER_4 |corner|))) (DEFCONCEPT CURVE$CURVED_SHAPE (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT CURVE$CURVED_SHAPE SHAPES) (DOCUMENTATION CURVE$CURVED_SHAPE "the trace of a point whose direction of motion changes") (HAS-I-TOPIC CURVE$CURVED_SHAPE |Geometry|) (WORD CURVE$CURVED_SHAPE |curve|) (WORD CURVE$CURVED_SHAPE |curved_shape|))) (DEFCONCEPT STRAIGHT_LINE (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT STRAIGHT_LINE SHAPES) (DOCUMENTATION STRAIGHT_LINE "a line traced by a point traveling in a constant direction; a line of zero curvature; ’the shortest distance between two points is a straight line’") (HAS-I-TOPIC STRAIGHT_LINE |Geometry|) (WORD STRAIGHT_LINE |straight_line|))) (DEFCONCEPT PLANE$SHEET (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT PLANE$SHEET SHAPES) (DOCUMENTATION PLANE$SHEET "(mathematics) an unbounded two-dimensional shape; ’we will refer to the plane of the graph as the X-Y plane’; ’any line joining two points on a plane lies wholly on that plane’") (HAS-I-TOPIC PLANE$SHEET |Mathematics|) (WORD PLANE$SHEET |plane|) (WORD PLANE$SHEET |sheet|))) (DEFCONCEPT MATHEMATICAL_RELATION (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT MATHEMATICAL_RELATION RELATIONS) (DOCUMENTATION MATHEMATICAL_RELATION "a relation between mathematical expressions (such as equality or inequality)") (HAS-I-TOPIC MATHEMATICAL_RELATION |Mathematics|) (WORD MATHEMATICAL_RELATION |mathematical_relation|))) (DEFCONCEPT STATISTIC (?SELF) :=> (S-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT STATISTIC COGNITION) (DOCUMENTATION STATISTIC "a datum that can be represented numerically") (HAS-I-TOPIC STATISTIC |Mathematics|) (WORD STATISTIC |statistic|))) (DEFCONCEPT POPULATION$UNIVERSE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT POPULATION$UNIVERSE COGNITION) (DOCUMENTATION POPULATION$UNIVERSE "(statistics) the entire aggregation of items from which samples can be drawn; ’it is an estimate of the mean of the population’") (HAS-I-TOPIC POPULATION$UNIVERSE |Statistics|) (WORD POPULATION$UNIVERSE |population|) (WORD POPULATION$UNIVERSE |universe|))) (DEFCONCEPT FLUID_1 (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT FLUID_1 SUBSTANCES) (DOCUMENTATION FLUID_1 "a continuous amorphous substance that tends to flow and to conform to the outline of its container: a liquid or a gas") (HAS-I-TOPIC FLUID_1 |Physics|) (WORD FLUID_1 |fluid|))) (DEFCONCEPT MOLECULE (?SELF) :=> (CHEMICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT MOLECULE SUBSTANCES) (DOCUMENTATION MOLECULE "(physics and chemistry) the simplest structural unit of an element or compound") (HAS-I-TOPIC MOLECULE |Chemistry|) (HAS-I-TOPIC MOLECULE |Physics|) (WORD MOLECULE |molecule|))) (DEFCONCEPT VOICE$VOCALIZATION (?SELF)

324

:=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT VOICE$VOCALIZATION COMMUNICATION) (DOCUMENTATION VOICE$VOCALIZATION "the sound made by the vibration of vocal folds modified by the resonance of the vocal tract; ’a singer takes good care of his voice’; ’the giraffe cannot make any vocalizations’") (HAS-I-TOPIC VOICE$VOCALIZATION |Acoustics|) (WORD VOICE$VOCALIZATION |voice|) (WORD VOICE$VOCALIZATION |vocalization|))) (DEFCONCEPT ELECTROPLATE (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT ELECTROPLATE ARTIFACTS) (DOCUMENTATION ELECTROPLATE "any artifact that has been plated with a thin coat of metal by electrolysis") (HAS-I-TOPIC ELECTROPLATE |Physics|) (WORD ELECTROPLATE |electroplate|))) (DEFCONCEPT LIGAND (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT LIGAND SUBSTANCES) (DOCUMENTATION LIGAND "an atom or molecule or radical or ion that forms a complex around a central atom") (HAS-I-TOPIC LIGAND |Physics|) (WORD LIGAND |ligand|))) (DEFCONCEPT BLIND_SPOT$OPTIC_DISC (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT BLIND_SPOT$OPTIC_DISC BODY_AS_SUBJECT) (DOCUMENTATION BLIND_SPOT$OPTIC_DISC "the point where the optic nerve enters the retina; not sensitive to light") (HAS-I-TOPIC BLIND_SPOT$OPTIC_DISC |Anatomy|) (HAS-I-TOPIC BLIND_SPOT$OPTIC_DISC |Optics|) (WORD BLIND_SPOT$OPTIC_DISC |blind spot|) (WORD BLIND_SPOT$OPTIC_DISC |optic disc|))) (DEFCONCEPT BLACKBODY$FULL_RADIATOR (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT BLACKBODY$FULL_RADIATOR OBJECTS) (DOCUMENTATION BLACKBODY$FULL_RADIATOR "a hypothetical object capable of absorbing all the electromagnetic radiation falling on it") (HAS-I-TOPIC BLACKBODY$FULL_RADIATOR |Physics|) (WORD BLACKBODY$FULL_RADIATOR |blackbody|) (WORD BLACKBODY$FULL_RADIATOR |full_radiator|))) (DEFCONCEPT RADIATOR_3 (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT RADIATOR_3 OBJECTS) (DOCUMENTATION RADIATOR_3 "any object that radiates energy") (HAS-I-TOPIC RADIATOR_3 |Physics|) (WORD RADIATOR_3 |radiator|))) (DEFCONCEPT ASTIGMATISM$ASTIGMIA_1 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT ASTIGMATISM$ASTIGMIA_1 STATES) (DOCUMENTATION ASTIGMATISM$ASTIGMIA_1 "(optics) defect in an optical system in which light rays from a single point fail to converge in a single focal point") (HAS-I-TOPIC ASTIGMATISM$ASTIGMIA_1 |Optics|) (WORD ASTIGMATISM$ASTIGMIA_1 |astigmatism|) (WORD ASTIGMATISM$ASTIGMIA_1 |astigmia|))) (DEFCONCEPT STIGMATISM (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT STIGMATISM STATES) (DOCUMENTATION STIGMATISM "(optics) condition of an optical system (as a lens) in which light rays from a single point converge in a single focal point") (HAS-I-TOPIC STIGMATISM |Optics|) (WORD STIGMATISM |stigmatism|))) (DEFCONCEPT EYE_CONDITION (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT EYE_CONDITION STATES) (DOCUMENTATION EYE_CONDITION "the condition of the optical properties of the eye") (HAS-I-TOPIC EYE_CONDITION |Optics|) (WORD EYE_CONDITION |eye_condition|))) (DEFCONCEPT ISOMERISM (?SELF) :=> (STATE ?SELF)

325

:AXIOMS (AND (SUBJECT ISOMERISM STATES) (DOCUMENTATION ISOMERISM "the state of being an isomer; the complex of chemical and physical phenomena characteristic of isomers") (HAS-I-TOPIC ISOMERISM |Chemistry|) (HAS-I-TOPIC ISOMERISM |Physics|) (WORD ISOMERISM |isomerism|))) (DEFCONCEPT BIOLOGICAL_GROUP (?SELF) :=> (AGENTIVE-PHYSICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT BIOLOGICAL_GROUP GROUPS) (DOCUMENTATION BIOLOGICAL_GROUP "a group of plants or animals") (HAS-I-TOPIC BIOLOGICAL_GROUP |Biology|) (WORD BIOLOGICAL_GROUP |biological group|))) (DEFCONCEPT LIFE_FORM$ORGANISM$BEING$LIVING_THING (?SELF) :=> (AGENTIVE-PHYSICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT LIFE_FORM$ORGANISM$BEING$LIVING_THING TOPS) (DOCUMENTATION LIFE_FORM$ORGANISM$BEING$LIVING_THING "any living entity") (HAS-I-TOPIC LIFE_FORM$ORGANISM$BEING$LIVING_THING |Biology|) (WORD LIFE_FORM$ORGANISM$BEING$LIVING_THING |life form|) (WORD LIFE_FORM$ORGANISM$BEING$LIVING_THING |organism|) (WORD LIFE_FORM$ORGANISM$BEING$LIVING_THING |being|) (WORD LIFE_FORM$ORGANISM$BEING$LIVING_THING |living thing|))) (DEFCONCEPT VITAL_PRINCIPLE$LIFE_PRINCIPLE (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT VITAL_PRINCIPLE$LIFE_PRINCIPLE PERSONS) (DOCUMENTATION VITAL_PRINCIPLE$LIFE_PRINCIPLE "a hypothetical force to which the functions and qualities peculiar to living things are sometimes ascribed") (HAS-I-TOPIC VITAL_PRINCIPLE$LIFE_PRINCIPLE |Biology|) (WORD VITAL_PRINCIPLE$LIFE_PRINCIPLE |vital_principle|) (WORD VITAL_PRINCIPLE$LIFE_PRINCIPLE |life_principle|))) (DEFCONCEPT FAUNA (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT FAUNA GROUPS) (DOCUMENTATION FAUNA "all the animal life in a particular region") (HAS-I-TOPIC FAUNA |Botany|) (HAS-I-TOPIC FAUNA |Zoology|) (WORD FAUNA |fauna|))) (DEFCONCEPT VEGETATION$FLORA (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT VEGETATION$FLORA GROUPS) (DOCUMENTATION VEGETATION$FLORA "all the plant life in a particular region") (HAS-I-TOPIC VEGETATION$FLORA |Botany|) (HAS-I-TOPIC VEGETATION$FLORA |Zoology|) (WORD VEGETATION$FLORA |vegetation|) (WORD VEGETATION$FLORA |flora|))) (DEFCONCEPT BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE (?SELF) :=> (BIOLOGICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE BODY_AS_SUBJECT) (DOCUMENTATION BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE "the entire physical structure of an organism (especially an animal or human being); ’he felt as if his whole body were on fire’") (HAS-I-TOPIC BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE |Anatomy|) (WORD BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE |body|) (WORD BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE |organic structure|) (WORD BODY$ORGANIC_STRUCTURE$PHYSICAL_STRUCTURE |physical structure|))) (DEFCONCEPT BODY_PART (?SELF) :=> (BIOLOGICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT BODY_PART BODY_AS_SUBJECT) (DOCUMENTATION BODY_PART "any part of an organism such as an organ or extremity") (HAS-I-TOPIC BODY_PART |Anatomy|) (WORD BODY_PART |body part|))) (DEFCONCEPT CELL_1 (?SELF) :=> (BIOLOGICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT CELL_1 TOPS) (DOCUMENTATION CELL_1 "the basic structural and functional unit of all organisms; cells may exist as independent

326

units of life (as in monads) or may form colonies or tissues as in higher plants and animals") (HAS-I-TOPIC CELL_1 |Biology|) (WORD CELL_1 |cell|))) (DEFCONCEPT CREATION$CONCEPTION (?SELF) :=> (EVENT ?SELF) :AXIOMS (AND (SUBJECT CREATION$CONCEPTION EVENTS) (DOCUMENTATION CREATION$CONCEPTION "the event that occured at the beginning of something; ’from its creation the plan was doomed to failure’") (HAS-I-TOPIC CREATION$CONCEPTION |Biology|) (WORD CREATION$CONCEPTION |creation|) (WORD CREATION$CONCEPTION |conception|))) (DEFCONCEPT CORPUS_1 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT CORPUS_1 BODY_AS_SUBJECT) (DOCUMENTATION CORPUS_1 "the main part of an organ or other bodily structure") (HAS-I-TOPIC CORPUS_1 |Anatomy|) (WORD CORPUS_1 |corpus|))) (DEFCONCEPT COVERING$NATURAL_COVERING$COVER (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT COVERING$NATURAL_COVERING$COVER OBJECTS) (DOCUMENTATION COVERING$NATURAL_COVERING$COVER "a natural object that covers or envelops; ’the fox was flushed from its cover’") (HAS-I-TOPIC COVERING$NATURAL_COVERING$COVER |Anatomy|) (WORD COVERING$NATURAL_COVERING$COVER |covering|) (WORD COVERING$NATURAL_COVERING$COVER |natural_covering|) (WORD COVERING$NATURAL_COVERING$COVER |cover|))) (DEFCONCEPT ACICULA (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT ACICULA OBJECTS) (DOCUMENTATION ACICULA "a needle-like part or structure of a plant or animal or crystal; as a spine or bristle or crystal") (HAS-I-TOPIC ACICULA |Biology|) (HAS-I-TOPIC ACICULA |Geology|) (WORD ACICULA |acicula|))) (DEFCONCEPT PLANT_PART (?SELF) :=> (BIOLOGICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT PLANT_PART PLANTS) (DOCUMENTATION PLANT_PART "any part of a plant or fungus") (HAS-I-TOPIC PLANT_PART |Botany|) (WORD PLANT_PART |plant_part|))) (DEFCONCEPT BODY$DEAD_BODY (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT BODY$DEAD_BODY BODY_AS_SUBJECT) (DOCUMENTATION BODY$DEAD_BODY "body of a dead animal or person; ’they found the body in the lake’") (HAS-I-TOPIC BODY$DEAD_BODY |Anatomy|) (WORD BODY$DEAD_BODY |body|) (WORD BODY$DEAD_BODY |dead body|))) (DEFCONCEPT MECHANISM_2 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT MECHANISM_2 OBJECTS) (DOCUMENTATION MECHANISM_2 "a natural object resembling a machine in structure and function; ’the mechanism of the ear’") (HAS-I-TOPIC MECHANISM_2 |Biology|) (WORD MECHANISM_2 |mechanism|))) (DEFCONCEPT COCOON (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT COCOON ANIMALS) (DOCUMENTATION COCOON "silky envelope spun by the larvae of many insects to protect pupas and by spiders to protect eggs") (HAS-I-TOPIC COCOON |Zoology|) (WORD COCOON |cocoon|))) (DEFCONCEPT NEST_5 (?SELF) :=> (NON-AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT NEST_5 OBJECTS) (DOCUMENTATION NEST_5 "a structure in which animals lay eggs or give birth to their young") (HAS-I-TOPIC NEST_5 |Zoology|) (WORD NEST_5 |nest|))) (DEFCONCEPT BODY_SUBSTANCE (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT BODY_SUBSTANCE BODY_AS_SUBJECT) (DOCUMENTATION BODY_SUBSTANCE "the substance of the body") (HAS-I-TOPIC BODY_SUBSTANCE |Anatomy|)

327

(WORD BODY_SUBSTANCE |body substance|))) (DEFCONCEPT PROTOPLASM$LIVING_SUBSTANCE (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT PROTOPLASM$LIVING_SUBSTANCE BODY_AS_SUBJECT) (DOCUMENTATION PROTOPLASM$LIVING_SUBSTANCE "the living substance of a cell") (HAS-I-TOPIC PROTOPLASM$LIVING_SUBSTANCE |Biology|) (WORD PROTOPLASM$LIVING_SUBSTANCE |protoplasm|) (WORD PROTOPLASM$LIVING_SUBSTANCE |living substance|))) (DEFCONCEPT LEAVEN$LEAVENING_2 (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT LEAVEN$LEAVENING_2 SUBSTANCES) (DOCUMENTATION LEAVEN$LEAVENING_2 "a substance used to produce fermentation in dough or a liquid") (HAS-I-TOPIC LEAVEN$LEAVENING_2 |Botany|) (HAS-I-TOPIC LEAVEN$LEAVENING_2 |Gastronomy|) (WORD LEAVEN$LEAVENING_2 |leaven|) (WORD LEAVEN$LEAVENING_2 |leavening|))) (DEFCONCEPT NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS BODY_AS_SUBJECT) (DOCUMENTATION NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS "scar where the umbilical cord was attached") (HAS-I-TOPIC NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS |Anatomy|) (WORD NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS |navel|) (WORD NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS |umbilicus|) (WORD NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS |bellybutton|) (WORD NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS |omphalos|) (WORD NAVEL$UMBILICUS$BELLYBUTTON$OMPHALOS$OMPHALUS |omphalus|))) (DEFCONCEPT TRICHION$CRINION (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT TRICHION$CRINION LOCATIONS) (DOCUMENTATION TRICHION$CRINION "point where the hairline meets the midpoint of the forehead") (HAS-I-TOPIC TRICHION$CRINION |Anatomy|) (WORD TRICHION$CRINION |trichion|) (WORD TRICHION$CRINION |crinion|))) (DEFCONCEPT BODY_5 (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT BODY_5 OBJECTS) (DOCUMENTATION BODY_5 "an individual 3-dimensional object that has mass and that is distinguishable from other objects; ’heavenly body’") (HAS-I-TOPIC BODY_5 |Anatomy|) (WORD BODY_5 |body|))) (DEFCONCEPT TANGLE (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT TANGLE OBJECTS) (DOCUMENTATION TANGLE "a twisted and tangled mass that is highly interwoven; ’they carved their way through the tangle of vines’") (HAS-I-TOPIC TANGLE |Zoology|) (WORD TANGLE |tangle|))) (DEFCONCEPT NATURAL_SHAPE (?SELF) :=> (QUALITY ?SELF) :AXIOMS (AND (SUBJECT NATURAL_SHAPE SHAPES) (DOCUMENTATION NATURAL_SHAPE "a shape created by natural forces; not man-made") (HAS-I-TOPIC NATURAL_SHAPE |Biology|) (WORD NATURAL_SHAPE |natural_shape|))) (DEFCONCEPT ATONICITY$ATONY$ATONIA$AMYOTONIA (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT ATONICITY$ATONY$ATONIA$AMYOTONIA STATES) (DOCUMENTATION ATONICITY$ATONY$ATONIA$AMYOTONIA "lack of normal muscular tension or tonus") (HAS-I-TOPIC ATONICITY$ATONY$ATONIA$AMYOTONIA |Physiology|) (WORD ATONICITY$ATONY$ATONIA$AMYOTONIA |atonicity|) (WORD ATONICITY$ATONY$ATONIA$AMYOTONIA |atony|)

328

(WORD ATONICITY$ATONY$ATONIA$AMYOTONIA |atonia|) (WORD ATONICITY$ATONY$ATONIA$AMYOTONIA |amyotonia|))) (DEFCONCEPT NICHE_1 (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT NICHE_1 STATES) (DOCUMENTATION NICHE_1 "(ecology) the status of an organism within its environment and community (affecting its survival as a species)") (HAS-I-TOPIC NICHE_1 |Ecology|) (WORD NICHE_1 |niche|))) (DEFCONCEPT TURGOR (?SELF) :=> (STATE ?SELF) :AXIOMS (AND (SUBJECT TURGOR STATES) (DOCUMENTATION TURGOR "(biology) the normal rigid state of fullness of a cell or blood vessel or capillary resulting from pressure of the contents against the wall or membrane") (HAS-I-TOPIC TURGOR |Biology|) (WORD TURGOR |turgor|))) (DEFCONCEPT PHYSIOLOGICAL_STATE (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT PHYSIOLOGICAL_STATE STATES) (DOCUMENTATION PHYSIOLOGICAL_STATE "the condition of the body or bodily functions") (HAS-I-TOPIC PHYSIOLOGICAL_STATE |Physiology|) (WORD PHYSIOLOGICAL_STATE |physiological_state|))) (DEFCONCEPT CULTURE_MEDIUM$MEDIUM (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT CULTURE_MEDIUM$MEDIUM SUBSTANCES) (DOCUMENTATION CULTURE_MEDIUM$MEDIUM "(bacteriology) a nutrient substance (solid or liquid) that is used to cultivate micro-organisms") (HAS-I-TOPIC CULTURE_MEDIUM$MEDIUM |Biology|) (WORD CULTURE_MEDIUM$MEDIUM |culture_medium|) (WORD CULTURE_MEDIUM$MEDIUM |medium|))) (DEFCONCEPT MEDIUM_5 (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT MEDIUM_5 SUBSTANCES) (DOCUMENTATION MEDIUM_5 "(biology) a substance in which specimens are preserved or displayed") (HAS-I-TOPIC MEDIUM_5 |Biology|) (WORD MEDIUM_5 |medium|))) (DEFCONCEPT METABOLITE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT METABOLITE SUBSTANCES) (DOCUMENTATION METABOLITE "any substance involved in metabolism (either as a product of metabolism or as necessary for metabolism)") (HAS-I-TOPIC METABOLITE |Biology|) (WORD METABOLITE |metabolite|))) (DEFCONCEPT BIOTA$BIOLOGY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT BIOTA$BIOLOGY GROUPS) (DOCUMENTATION BIOTA$BIOLOGY "all the plant and animal life of a particular region") (HAS-I-TOPIC BIOTA$BIOLOGY |Biology|) (WORD BIOTA$BIOLOGY |biota|) (WORD BIOTA$BIOLOGY |biology|))) (DEFCONCEPT MENAGERIE (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT MENAGERIE GROUPS) (DOCUMENTATION MENAGERIE "a collection of live animals for study or display") (HAS-I-TOPIC MENAGERIE |Zoology|) (WORD MENAGERIE |menagerie|))) (DEFCONCEPT CHEMICAL_ELEMENT$ELEMENT (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT CHEMICAL_ELEMENT$ELEMENT SUBSTANCES) (DOCUMENTATION CHEMICAL_ELEMENT$ELEMENT "any of the more than 100 known substances (of which 93 occur naturally) that cannot be separated into simpler substances and that singly or in combination constitute all matter") (HAS-I-TOPIC CHEMICAL_ELEMENT$ELEMENT |Chemistry|) (WORD CHEMICAL_ELEMENT$ELEMENT |chemical_element|) (WORD CHEMICAL_ELEMENT$ELEMENT |element|))) (DEFCONCEPT COMPOUND$CHEMICAL_COMPOUND (?SELF) :=> (AMOUNT-OF-MATTER ?SELF)

329

:AXIOMS (AND (SUBJECT COMPOUND$CHEMICAL_COMPOUND SUBSTANCES) (DOCUMENTATION COMPOUND$CHEMICAL_COMPOUND "(chemistry) a substance formed by chemical union of two or more elements or ingredients in definite proportion by weight") (HAS-I-TOPIC COMPOUND$CHEMICAL_COMPOUND |Chemistry|) (WORD COMPOUND$CHEMICAL_COMPOUND |compound|) (WORD COMPOUND$CHEMICAL_COMPOUND |chemical_compound|))) (DEFCONCEPT FLUID_2 (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT FLUID_2 SUBSTANCES) (DOCUMENTATION FLUID_2 "a substance that is fluid at room temperature and pressure") (HAS-I-TOPIC FLUID_2 |Chemistry|) (WORD FLUID_2 |fluid|))) (DEFCONCEPT AGENT_3 (?SELF) :=> (CAUSAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT AGENT_3 SUBSTANCES) (DOCUMENTATION AGENT_3 "a substance that exerts some force or effect") (HAS-I-TOPIC AGENT_3 |Chemistry|) (WORD AGENT_3 |agent|))) (DEFCONCEPT GROUP$RADICAL (?SELF) :=> (CHEMICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT GROUP$RADICAL SUBSTANCES) (DOCUMENTATION GROUP$RADICAL "two or more atoms bound together as a single unit and forming part of a molecule") (HAS-I-TOPIC GROUP$RADICAL |Chemistry|) (WORD GROUP$RADICAL |group|) (WORD GROUP$RADICAL |radical|))) (DEFCONCEPT CHEMICAL_IRRITANT (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT CHEMICAL_IRRITANT SUBSTANCES) (DOCUMENTATION CHEMICAL_IRRITANT "a substance producing irritation") (HAS-I-TOPIC CHEMICAL_IRRITANT |Chemistry|) (WORD CHEMICAL_IRRITANT |chemical_irritant|))) (DEFCONCEPT FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL SUBSTANCES) (DOCUMENTATION FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL "a substance that can be burned to provide heat or power; ’more fuel is needed during the winter months’; ’they developed alternative fuels for aircraft’") (HAS-I-TOPIC FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL |Chemistry|) (WORD FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL |fuel|) (WORD FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL |combustible|) (WORD FUEL$COMBUSTIBLE$COMBUSTIBLE_MATERIAL |combustible_material|))) (DEFCONCEPT POISON_2 (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT POISON_2 SUBSTANCES) (DOCUMENTATION POISON_2 "any substance that causes injury or illness or death of a living organism") (HAS-I-TOPIC POISON_2 |Chemistry|) (HAS-I-TOPIC POISON_2 |Medicine|) (WORD POISON_2 |poison|))) (DEFCONCEPT SOLID_2 (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT SOLID_2 SUBSTANCES) (DOCUMENTATION SOLID_2 "a substance that is a solid at room temperature and pressure") (HAS-I-TOPIC SOLID_2 |Chemistry|) (WORD SOLID_2 |solid|))) (DEFCONCEPT SATURATION_2 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SATURATION_2 STATES) (DOCUMENTATION SATURATION_2 "(chemistry) the state in which a substance contains no multiple bonds and thus is incapable of undergoing additional reactions") (HAS-I-TOPIC SATURATION_2 |Chemistry|) (WORD SATURATION_2 |saturation|))) (DEFCONCEPT ACTIVATOR (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ACTIVATOR SUBSTANCES) (DOCUMENTATION ACTIVATOR "any agency bringing about activation; (biology) a molecule that increases the activity of

330

an enzyme or a protein that increases the production of a gene product in DNA transcription") (HAS-I-TOPIC ACTIVATOR |Chemistry|) (WORD ACTIVATOR |activator|))) (DEFCONCEPT ADULTERANT (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ADULTERANT SUBSTANCES) (DOCUMENTATION ADULTERANT "any substance that adulterates (lessens the purity or effectiveness of a substance); ’it is necessary to remove the adulterants before use’") (HAS-I-TOPIC ADULTERANT |Chemistry|) (WORD ADULTERANT |adulterant|))) (DEFCONCEPT CARCINOGEN (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT CARCINOGEN SUBSTANCES) (DOCUMENTATION CARCINOGEN "any substance that produces cancer") (HAS-I-TOPIC CARCINOGEN |Chemistry|) (WORD CARCINOGEN |carcinogen|))) (DEFCONCEPT DENATURANT (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT DENATURANT SUBSTANCES) (DOCUMENTATION DENATURANT "any substance that serves as a denaturing agent") (HAS-I-TOPIC DENATURANT |Chemistry|) (WORD DENATURANT |denaturant|))) (DEFCONCEPT FERMENT (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT FERMENT SUBSTANCES) (DOCUMENTATION FERMENT "a substance capable of bringing about fermentation") (HAS-I-TOPIC FERMENT |Chemistry|) (WORD FERMENT |ferment|))) (DEFCONCEPT INHIBITOR (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT INHIBITOR SUBSTANCES) (DOCUMENTATION INHIBITOR "a substance that retards or stops an activity") (HAS-I-TOPIC INHIBITOR |Chemistry|) (WORD INHIBITOR |inhibitor|))) (DEFCONCEPT MIXTURE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT MIXTURE SUBSTANCES) (DOCUMENTATION MIXTURE "(chemistry) a substance consisting of two or more substances mixed together (not in fixed proportions and not with chemical bonding)") (HAS-I-TOPIC MIXTURE |Chemistry|) (WORD MIXTURE |mixture|))) (DEFCONCEPT PRECIPITANT (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT PRECIPITANT SUBSTANCES) (DOCUMENTATION PRECIPITANT "a substance that causes a precipitate to form") (HAS-I-TOPIC PRECIPITANT |Chemistry|) (WORD PRECIPITANT |precipitant|))) (DEFCONCEPT REFRIGERANT (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT REFRIGERANT SUBSTANCES) (DOCUMENTATION REFRIGERANT "a substance used to provide cooling (as in a refrigerator)") (HAS-I-TOPIC REFRIGERANT |Chemistry|) (WORD REFRIGERANT |refrigerant|))) (DEFCONCEPT RESIDUE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT RESIDUE SUBSTANCES) (DOCUMENTATION RESIDUE "matter that remains after something has been removed") (HAS-I-TOPIC RESIDUE |Chemistry|) (WORD RESIDUE |residue|))) (DEFCONCEPT SOLUTE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SOLUTE SUBSTANCES) (DOCUMENTATION SOLUTE "the dissolved substance in a solution; the component of a solution that changes its state") (HAS-I-TOPIC SOLUTE |Chemistry|) (WORD SOLUTE |solute|))) (DEFCONCEPT SOLVATE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SOLVATE SUBSTANCES)

331

(DOCUMENTATION SOLVATE "a compound formed by solvation (the combination of solvent molecules with molecules or ions of the solute)") (HAS-I-TOPIC SOLVATE |Chemistry|) (WORD SOLVATE |solvate|))) (DEFCONCEPT SYSTEM_5 (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SYSTEM_5 SUBSTANCES) (DOCUMENTATION SYSTEM_5 "(physical chemistry) a sample of matter in which substances in different phases are in equilibrium; ’in a static system oil cannot be replaced by water on a surface’; ’a system generating hydrogen peroxide’") (HAS-I-TOPIC SYSTEM_5 |Chemistry|) (WORD SYSTEM_5 |system|))) (DEFCONCEPT VOLATILE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT VOLATILE SUBSTANCES) (DOCUMENTATION VOLATILE "a volatile substance; a substance that changes readily from solid or liquid to a vapor; ’it was heated to evaporate the volatiles’") (HAS-I-TOPIC VOLATILE |Chemistry|) (WORD VOLATILE |volatile|))) (DEFCONCEPT KINGDOM_1 (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT KINGDOM_1 GROUPS) (DOCUMENTATION KINGDOM_1 "a basic group of natural objects") (HAS-I-TOPIC KINGDOM_1 |Chemistry|) (WORD KINGDOM_1 |kingdom|))) (DEFCONCEPT POPULATION_1 (?SELF) :=> (AGENTIVE-GROUP ?SELF) :AXIOMS (AND (SUBJECT POPULATION_1 GROUPS) (DOCUMENTATION POPULATION_1 "a group of organisms of the same species populating a given area; ’they hired hunters to keep down the deer population’") (HAS-I-TOPIC POPULATION_1 |Geography|) (WORD POPULATION_1 |population|))) (DEFCONCEPT APPLETON_LAYER$F_LAYER$F_REGION (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT APPLETON_LAYER$F_LAYER$F_REGION LOCATIONS) (DOCUMENTATION APPLETON_LAYER$F_LAYER$F_REGION "the highest region of the ionosphere (from 90 to 600 miles up) that contains the highest concentration of free electrons and is most useful for long-range radio transmission") (HAS-I-TOPIC APPLETON_LAYER$F_LAYER$F_REGION |Geography|) (WORD APPLETON_LAYER$F_LAYER$F_REGION |Appleton_layer|) (WORD APPLETON_LAYER$F_LAYER$F_REGION |F_layer|) (WORD APPLETON_LAYER$F_LAYER$F_REGION |F_region|))) (DEFCONCEPT D-LAYER$D_REGION (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT D-LAYER$D_REGION LOCATIONS) (DOCUMENTATION D-LAYER$D_REGION "the lowest region of the ionosphere (35 to 50 miles up) that reflects low-frequency radio waves") (HAS-I-TOPIC D-LAYER$D_REGION |Geography|) (WORD D-LAYER$D_REGION |D-layer|) (WORD D-LAYER$D_REGION |D_region|))) (DEFCONCEPT HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION LOCATIONS) (DOCUMENTATION HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION "a region of the ionosphere (from 50 to 90 miles up) that reflects radio waves of medium length") (HAS-I-TOPIC HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION |Geography|) (WORD HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION |Heaviside_layer|) (WORD HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION |Kennelly-Heaviside_layer|) (WORD HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION |E_layer|) (WORD HEAVISIDE_LAYER$KENNELLY-HEAVISIDE_LAYER$E_LAYER$E_REGION |E_region|)))

332

(DEFCONCEPT LAND$GROUND$SOIL (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT LAND$GROUND$SOIL OBJECTS) (DOCUMENTATION LAND$GROUND$SOIL "what plants grow in (especially with reference to its quality or use); ’the land had never been plowed’; ’good agricultural soil’") (HAS-I-TOPIC LAND$GROUND$SOIL |Geography|) (WORD LAND$GROUND$SOIL |land|) (WORD LAND$GROUND$SOIL |ground|) (WORD LAND$GROUND$SOIL |soil|))) (DEFCONCEPT ICE_1 (?SELF) :=> (AMOUNT-OF-MATTER ?SELF) :AXIOMS (AND (SUBJECT ICE_1 OBJECTS) (DOCUMENTATION ICE_1 "the frozen part of a body of water") (HAS-I-TOPIC ICE_1 |Oceanography|) (WORD ICE_1 |ice|))) (DEFCONCEPT BASE_5 (?SELF) :=> (FEATURE ?SELF) :AXIOMS (AND (SUBJECT BASE_5 OBJECTS) (DOCUMENTATION BASE_5 "the bottom or lowest part; ’the base of the mountain’") (HAS-I-TOPIC BASE_5 |Geography|) (WORD BASE_5 |base|))) (DEFCONCEPT ENCLOSURE$NATURAL_ENCLOSURE (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT ENCLOSURE$NATURAL_ENCLOSURE OBJECTS) (DOCUMENTATION ENCLOSURE$NATURAL_ENCLOSURE "a naturally enclosed space") (HAS-I-TOPIC ENCLOSURE$NATURAL_ENCLOSURE |Earth|) (WORD ENCLOSURE$NATURAL_ENCLOSURE |enclosure|) (WORD ENCLOSURE$NATURAL_ENCLOSURE |natural_enclosure|))) (DEFCONCEPT ANTIPODES (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT ANTIPODES LOCATIONS) (DOCUMENTATION ANTIPODES "any two places or regions on diametrically opposite sides of the Earth; ’the North Pole and the South Pole are antipodes’") (HAS-I-TOPIC ANTIPODES |Geography|) (WORD ANTIPODES |antipodes|))) (DEFCONCEPT CONFLUENCE$JUNCTION$MEETING (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT CONFLUENCE$JUNCTION$MEETING LOCATIONS) (DOCUMENTATION CONFLUENCE$JUNCTION$MEETING "a place where two things come together; ’Pittsburgh is located at the confluence of the Allegheny and Monongahela rivers’") (HAS-I-TOPIC CONFLUENCE$JUNCTION$MEETING |Geography|) (WORD CONFLUENCE$JUNCTION$MEETING |confluence|) (WORD CONFLUENCE$JUNCTION$MEETING |junction|) (WORD CONFLUENCE$JUNCTION$MEETING |meeting|))) (DEFCONCEPT EPICENTER$EPICENTRE (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT EPICENTER$EPICENTRE LOCATIONS) (DOCUMENTATION EPICENTER$EPICENTRE "the point on the Earth’s surface directly above the focus of an earthquake") (HAS-I-TOPIC EPICENTER$EPICENTRE |Geography|) (WORD EPICENTER$EPICENTRE |epicenter|) (WORD EPICENTER$EPICENTRE |epicentre|))) (DEFCONCEPT MAGNETIC_POLE (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT MAGNETIC_POLE LOCATIONS) (DOCUMENTATION MAGNETIC_POLE "either of two points where the lines of force of the Earth’s magnetic field are vertical") (HAS-I-TOPIC MAGNETIC_POLE |Geography|) (WORD MAGNETIC_POLE |magnetic_pole|))) (DEFCONCEPT NORTH$NORTHLAND$SEPTENTRION (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT NORTH$NORTHLAND$SEPTENTRION LOCATIONS) (DOCUMENTATION NORTH$NORTHLAND$SEPTENTRION "any region lying in or toward the north") (HAS-I-TOPIC NORTH$NORTHLAND$SEPTENTRION |Geography|) (WORD NORTH$NORTHLAND$SEPTENTRION |North|) (WORD NORTH$NORTHLAND$SEPTENTRION |northland|)

333

(WORD NORTH$NORTHLAND$SEPTENTRION |septentrion|))) (DEFCONCEPT POLE_4 (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT POLE_4 LOCATIONS) (DOCUMENTATION POLE_4 "one of two antipodal points where the Earth’s axis of rotation intersects the Earth’s surface") (HAS-I-TOPIC POLE_4 |Geography|) (WORD POLE_4 |pole|))) (DEFCONCEPT SOUTH$SOUTHLAND (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT SOUTH$SOUTHLAND LOCATIONS) (DOCUMENTATION SOUTH$SOUTHLAND "any region lying in or toward the south") (HAS-I-TOPIC SOUTH$SOUTHLAND |Geography|) (WORD SOUTH$SOUTHLAND |South|) (WORD SOUTH$SOUTHLAND |southland|))) (DEFCONCEPT WEST$OCCIDENT (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT WEST$OCCIDENT LOCATIONS) (DOCUMENTATION WEST$OCCIDENT "the countries of (originally) Europe and (now including) North and South America") (HAS-I-TOPIC WEST$OCCIDENT |Geography|) (WORD WEST$OCCIDENT |West|) (WORD WEST$OCCIDENT |occident|))) (DEFCONCEPT GEOLOGICAL_FORMATION$GEOLOGY$FORMATION (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT GEOLOGICAL_FORMATION$GEOLOGY$FORMATION OBJECTS) (DOCUMENTATION GEOLOGICAL_FORMATION$GEOLOGY$FORMATION "the geological features of the earth") (HAS-I-TOPIC GEOLOGICAL_FORMATION$GEOLOGY$FORMATION |Geology|) (WORD GEOLOGICAL_FORMATION$GEOLOGY$FORMATION |geological_formation|) (WORD GEOLOGICAL_FORMATION$GEOLOGY$FORMATION |geology|) (WORD GEOLOGICAL_FORMATION$GEOLOGY$FORMATION |formation|))) (DEFCONCEPT PASS$MOUNTAIN_PASS$NOTCH (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT PASS$MOUNTAIN_PASS$NOTCH OBJECTS) (DOCUMENTATION PASS$MOUNTAIN_PASS$NOTCH "the location in a range of mountains of a geological formation that is lower than the surrounding peaks; ’we got through the pass before it started to snow’") (HAS-I-TOPIC PASS$MOUNTAIN_PASS$NOTCH |Geology|) (WORD PASS$MOUNTAIN_PASS$NOTCH |pass|) (WORD PASS$MOUNTAIN_PASS$NOTCH |mountain_pass|) (WORD PASS$MOUNTAIN_PASS$NOTCH |notch|))) (DEFCONCEPT BODY_OF_WATER$WATER (?SELF) :=> (GEOGRAPHICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT BODY_OF_WATER$WATER OBJECTS) (DOCUMENTATION BODY_OF_WATER$WATER "the part of the earth’s surface covered with water; ’they invaded our territorial waters’") (HAS-I-TOPIC BODY_OF_WATER$WATER |Geography|) (WORD BODY_OF_WATER$WATER |body_of_water|) (WORD BODY_OF_WATER$WATER |water|))) (DEFCONCEPT LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA (?SELF) :=> (GEOGRAPHICAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA OBJECTS) (DOCUMENTATION LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$ TERRA_FIRMA "the solid part of the earth’s surface; ’the plane turned away from the sea and moved back over land’; ’the earth shook for several minutes’; ’he dropped the logs on the ground’") (HAS-I-TOPIC LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |Geography|) (WORD LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |land|) (WORD LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |dry_land|) (WORD LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |earth|) (WORD LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |ground|) (WORD LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |solid_ground|) (WORD LAND$DRY_LAND$EARTH$GROUND$SOLID_GROUND$TERRA_FIRMA |terra_firma|)))

334

(DEFCONCEPT AREA$COUNTRY (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT AREA$COUNTRY LOCATIONS) (DOCUMENTATION AREA$COUNTRY "a particular geographical region of indefinite boundary (usually serving some special purpose or distinguished by its people or culture or geography); ’it was a mountainous area’; ’Bible country’ (HAS-I-TOPIC AREA$COUNTRY |Geography|) (WORD AREA$COUNTRY |area|) (WORD AREA$COUNTRY |country|))) (DEFCONCEPT DOMAIN$DEMESNE$LAND (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT DOMAIN$DEMESNE$LAND LOCATIONS) (DOCUMENTATION DOMAIN$DEMESNE$LAND "territory over which rule or control is exercised; ’his domain extended into Europe’; ’he made it the law of the land’") (HAS-I-TOPIC DOMAIN$DEMESNE$LAND |Administration|) (HAS-I-TOPIC DOMAIN$DEMESNE$LAND |Geography|) (WORD DOMAIN$DEMESNE$LAND |domain|) (WORD DOMAIN$DEMESNE$LAND |demesne|) (WORD DOMAIN$DEMESNE$LAND |land|))) (DEFCONCEPT FAR_EAST (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT FAR_EAST LOCATIONS) (DOCUMENTATION FAR_EAST "a popular expression for the countries of eastern Asia (usually including China and Mongolia and Taiwan and Japan and Korea and Indochina and eastern Siberia)") (HAS-I-TOPIC FAR_EAST |Geography|) (WORD FAR_EAST |Far_East|))) (DEFCONCEPT GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION LOCATIONS) (DOCUMENTATION GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION "a demarcated area of the Earth") (HAS-I-TOPIC GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION |Geography|) (WORD GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION |geographical_area|) (WORD GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION |geographic_area|) (WORD GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION |geographical_region|) (WORD GEOGRAPHICAL_AREA$GEOGRAPHIC_AREA$GEOGRAPHICAL_REGION$ GEOGRAPHIC_REGION |geographic_region|))) (DEFCONCEPT EXPANSE$EXTENT (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT EXPANSE$EXTENT OBJECTS) (DOCUMENTATION EXPANSE$EXTENT "a wide and open space or area as of surface or land or sky") (HAS-I-TOPIC EXPANSE$EXTENT |Earth|) (WORD EXPANSE$EXTENT |expanse|) (WORD EXPANSE$EXTENT |extent|))) (DEFCONCEPT BACKWATER (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT BACKWATER LOCATIONS)

335

(DOCUMENTATION BACKWATER "any backward region that is isolated from the world and resists progress") (HAS-I-TOPIC BACKWATER |Geography|) (WORD BACKWATER |backwater|))) (DEFCONCEPT BIOGEOGRAPHICAL_REGION (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT BIOGEOGRAPHICAL_REGION LOCATIONS) (DOCUMENTATION BIOGEOGRAPHICAL_REGION "an area of the Earth determined by distribution of flora and fauna") (HAS-I-TOPIC BIOGEOGRAPHICAL_REGION |Geography|) (WORD BIOGEOGRAPHICAL_REGION |biogeographical_region|))) (DEFCONCEPT OLD_WORLD (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT OLD_WORLD LOCATIONS) (DOCUMENTATION OLD_WORLD "the regions of the world that were known to Europeans before the discovery of the Americas") (HAS-I-TOPIC OLD_WORLD |Geography|) (WORD OLD_WORLD |Old_World|))) (DEFCONCEPT UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA (?SELF) :=> (NON-PHYSICAL-PLACE ?SELF) :AXIOMS (AND (SUBJECT UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA LOCATIONS) (DOCUMENTATION UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA "an unknown and unexplored region; ’they came like angels out the unknown’") (HAS-I-TOPIC UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA |Geography|) (WORD UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA |unknown|) (WORD UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA |unknown_region|) (WORD UNKNOWN$UNKNOWN_REGION$TERRA_INCOGNITA |terra_incognita|))) (DEFCONCEPT ROCK$STONE_1 (?SELF) :=> (PHYSICAL-BODY ?SELF) :AXIOMS (AND (SUBJECT ROCK$STONE_1 OBJECTS) (DOCUMENTATION ROCK$STONE_1 "a lump of hard consolidated mineral matter; ’he threw a rock at me’") (HAS-I-TOPIC ROCK$STONE_1 |Geology|) (WORD ROCK$STONE_1 |rock|) (WORD ROCK$STONE_1 |stone|))) (DEFCONCEPT SKI_CONDITIONS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SKI_CONDITIONS STATES) (DOCUMENTATION SKI_CONDITIONS "the amount and state of snow for skiing") (HAS-I-TOPIC SKI_CONDITIONS |Meteorology|) (WORD SKI_CONDITIONS |ski_conditions|))) (DEFCONCEPT WEATHER_CONDITIONS (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT WEATHER_CONDITIONS STATES) (DOCUMENTATION WEATHER_CONDITIONS "the condition of the weather") (HAS-I-TOPIC WEATHER_CONDITIONS |Meteorology|) (WORD WEATHER_CONDITIONS |weather_conditions|))) (DEFCONCEPT DRIFT_1 (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT DRIFT_1 OBJECTS) (DOCUMENTATION DRIFT_1 "something heaped up by the wind or current") (HAS-I-TOPIC DRIFT_1 |Geography|) (HAS-I-TOPIC DRIFT_1 |Geology|) (WORD DRIFT_1 |drift|))) (DEFCONCEPT SEDIMENT$DEPOSIT (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT SEDIMENT$DEPOSIT OBJECTS) (DOCUMENTATION SEDIMENT$DEPOSIT "matter deposited by water or ice or wind") (HAS-I-TOPIC SEDIMENT$DEPOSIT |Geology|) (WORD SEDIMENT$DEPOSIT |sediment|) (WORD SEDIMENT$DEPOSIT |deposit|))) (DEFCONCEPT BEDDING_MATERIAL$BEDDING$LITTER (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT BEDDING_MATERIAL$BEDDING$LITTER ARTIFACTS) (DOCUMENTATION BEDDING_MATERIAL$BEDDING$LITTER "material used to provide a bed for animals") (HAS-I-TOPIC BEDDING_MATERIAL$BEDDING$LITTER |Agriculture|) (HAS-I-TOPIC BEDDING_MATERIAL$BEDDING$LITTER |Zootechnics|) (WORD BEDDING_MATERIAL$BEDDING$LITTER |bedding material|) (WORD BEDDING_MATERIAL$BEDDING$LITTER |bedding|) (WORD BEDDING_MATERIAL$BEDDING$LITTER |litter|)))

336

(DEFCONCEPT FOOD$NUTRIENT (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT FOOD$NUTRIENT TOPS) (DOCUMENTATION FOOD$NUTRIENT "any substance that can be metabolized by an organism to give energy and build tissue") (HAS-I-TOPIC FOOD$NUTRIENT |Alimentation|) (WORD FOOD$NUTRIENT |food|) (WORD FOOD$NUTRIENT |nutrient|))) (DEFCONCEPT GRINDING_2 (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT GRINDING_2 OBJECTS) (DOCUMENTATION GRINDING_2 "matter resulting from the process of grinding; ’vegetable grindings clogged the drain’") (HAS-I-TOPIC GRINDING_2 |Gastronomy|) (WORD GRINDING_2 |grinding|))) (DEFCONCEPT MACHINE_1 (?SELF) :=> (AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT MACHINE_1 ARTIFACTS) (DOCUMENTATION MACHINE_1 "any mechanical or electrical device that transmits or modifies energy to perform or assist in the performance of human tasks") (HAS-I-TOPIC MACHINE_1 |Building_Industry|) (WORD MACHINE_1 |machine|))) (DEFCONCEPT BRICKS_AND_MORTAR (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT BRICKS_AND_MORTAR SUBSTANCES) (DOCUMENTATION BRICKS_AND_MORTAR "building material consisting of bricks laid with mortar between then") (HAS-I-TOPIC BRICKS_AND_MORTAR |Building_Industry|) (WORD BRICKS_AND_MORTAR |bricks_and_mortar|))) (DEFCONCEPT LATH_AND_PLASTER (?SELF) :=> (ARBITRARY-SUM ?SELF) :AXIOMS (AND (SUBJECT LATH_AND_PLASTER SUBSTANCES) (DOCUMENTATION LATH_AND_PLASTER "a building material consisting of thin strips of wood that provide a foundation for a coat of plaster") (HAS-I-TOPIC LATH_AND_PLASTER |Building_Industry|) (WORD LATH_AND_PLASTER |lath_and_plaster|))) (DEFCONCEPT BUILDING_MATERIAL (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT BUILDING_MATERIAL SUBSTANCES) (DOCUMENTATION BUILDING_MATERIAL "material used for constructing buildings") (HAS-I-TOPIC BUILDING_MATERIAL |Building_Industry|) (WORD BUILDING_MATERIAL |building_material|))) (DEFCONCEPT PAVING_MATERIAL (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF) :AXIOMS (AND (SUBJECT PAVING_MATERIAL SUBSTANCES) (DOCUMENTATION PAVING_MATERIAL "material used for pavement") (HAS-I-TOPIC PAVING_MATERIAL |Building_Industry|) (WORD PAVING_MATERIAL |paving_material|))) (DEFCONCEPT DISTRICT$TERRITORY (?SELF) :=> (GEOGRAPHICAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT DISTRICT$TERRITORY LOCATIONS) (DOCUMENTATION DISTRICT$TERRITORY "a region marked off for administrative or other purposes") (HAS-I-TOPIC DISTRICT$TERRITORY |Administration|) (HAS-I-TOPIC DISTRICT$TERRITORY |Town_Planning|) (WORD DISTRICT$TERRITORY |district|) (WORD DISTRICT$TERRITORY |territory|))) (DEFCONCEPT LIBRARY$PROGRAM_LIBRARY (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT LIBRARY$PROGRAM_LIBRARY GROUPS) (DOCUMENTATION LIBRARY$PROGRAM_LIBRARY "(computing) a collection of standard programs and subroutines that are stored and available for immediate use") (HAS-I-TOPIC LIBRARY$PROGRAM_LIBRARY |Computer_Science|) (WORD LIBRARY$PROGRAM_LIBRARY |library|) (WORD LIBRARY$PROGRAM_LIBRARY |program library|))) (DEFCONCEPT DRUG (?SELF) :=> (FUNCTIONALLY-VIEWED-MATTER ?SELF)

337

:AXIOMS (AND (SUBJECT DRUG ARTIFACTS) (DOCUMENTATION DRUG "something that is used as a medicine or narcotic") (HAS-I-TOPIC DRUG |Pharmacy|) (WORD DRUG |drug|))) (DEFCONCEPT FOCUS$NIDUS (?SELF) :=> (GEOGRAPHICAL-FEATURE ?SELF) :AXIOMS (AND (SUBJECT FOCUS$NIDUS STATES) (DOCUMENTATION FOCUS$NIDUS "a central point or locus of bacterial growth in an organism; ’the focus of infection’") (HAS-I-TOPIC FOCUS$NIDUS |Medicine|) (WORD FOCUS$NIDUS |focus|) (WORD FOCUS$NIDUS |nidus|))) (DEFCONCEPT CURVATURE_2 (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT CURVATURE_2 STATES) (DOCUMENTATION CURVATURE_2 "(medical) a curving or bending; often abnormal; ’curvature of the spine’") (HAS-I-TOPIC CURVATURE_2 |Medicine|) (WORD CURVATURE_2 |curvature|))) (DEFCONCEPT SANITARY_CONDITION (?SELF) :=> (REGION ?SELF) :AXIOMS (AND (SUBJECT SANITARY_CONDITION STATES) (DOCUMENTATION SANITARY_CONDITION "the state of sanitation (clean or dirty)") (HAS-I-TOPIC SANITARY_CONDITION |Medicine|) (WORD SANITARY_CONDITION |sanitary_condition|))) (DEFCONCEPT DISORDER$UPSET (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT DISORDER$UPSET STATES) (DOCUMENTATION DISORDER$UPSET "a disturbance of normal functioning; ’the doctor prescribed some medicine for the disorder’; ’everyone gets stomach upsets from time to time’") (HAS-I-TOPIC DISORDER$UPSET |Medicine|) (WORD DISORDER$UPSET |disorder|) (WORD DISORDER$UPSET |upset|))) (DEFCONCEPT ALLERGEN (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ALLERGEN SUBSTANCES) (DOCUMENTATION ALLERGEN "any substance that can cause an allergy") (HAS-I-TOPIC ALLERGEN |Medicine|) (WORD ALLERGEN |allergen|))) (DEFCONCEPT ESSENCE (?SELF) :=> (SUBSTANCE-ROLE ?SELF) :AXIOMS (AND (SUBJECT ESSENCE SUBSTANCES) (DOCUMENTATION ESSENCE "any substance possessing to a high degree the predominant properties of a plant or drug or other natural product from which it is extracted") (HAS-I-TOPIC ESSENCE |Pharmacy|) (WORD ESSENCE |essence|))) (DEFCONCEPT ARMAMENTARIUM (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT ARMAMENTARIUM GROUPS) (DOCUMENTATION ARMAMENTARIUM "the collection of equipment and methods used in the practice of medicine") (HAS-I-TOPIC ARMAMENTARIUM |Medicine|) (WORD ARMAMENTARIUM |armamentarium|))) (DEFCONCEPT PHARMACOPOEIA (?SELF) :=> (UNITARY-COLLECTION ?SELF) :AXIOMS (AND (SUBJECT PHARMACOPOEIA ARTIFACTS) (DOCUMENTATION PHARMACOPOEIA "a collection or stock of drugs") (HAS-I-TOPIC PHARMACOPOEIA |Pharmacy|) (WORD PHARMACOPOEIA |pharmacopoeia|))) (DEFCONCEPT TAXONOMIC_GROUP$TAXON (?SELF) :=> (LIFE_FORM$ORGANISM$BEING$LIVING_THING ?SELF) :AXIOMS (AND (SUBJECT TAXONOMIC_GROUP$TAXON GROUPS) (DOCUMENTATION TAXONOMIC_GROUP$TAXON "animal or plant group having natural relations") (HAS-I-TOPIC TAXONOMIC_GROUP$TAXON |Biology|))) (DEFCONCEPT DIVISION_8 (?SELF) :=> (LIFE_FORM$ORGANISM$BEING$LIVING_THING ?SELF)) (DEFCONCEPT ANIMAL_GROUP (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT ANIMAL_GROUP GROUPS)

338

(DOCUMENTATION ANIMAL_GROUP "a group of animals") (HAS-I-TOPIC ANIMAL_GROUP |Zoology|))) (DEFCONCEPT GENERATION_1 (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT GENERATION_1 GROUPS) (DOCUMENTATION GENERATION_1 "group of genetically related organisms constituting a single step in the line of descent") (HAS-I-TOPIC GENERATION_1 |Biology|))) (DEFCONCEPT DESCENDANTS$POSTERITY (?SELF) :=> (AGENTIVE-FUNCTIONAL-ROLE ?SELF) :AXIOMS (AND (SUBJECT DESCENDANTS$POSTERITY GROUPS) (DOCUMENTATION DESCENDANTS$POSTERITY "all of the offspring of a given progenitor; ’we must secure the benefits of freedom for ourselves and our posterity’") (HAS-I-TOPIC DESCENDANTS$POSTERITY |Biology|))) (DEFCONCEPT POWER_TOOL (?SELF) :=> (INSTRUMENTALITY-ROLE ?SELF) :AXIOMS (AND (SUBJECT POWER_TOOL ARTIFACTS) (DOCUMENTATION POWER_TOOL "a motor-driven tool") (HAS-I-TOPIC POWER_TOOL |Building_Industry|))) (DEFCONCEPT HOME_APPLIANCE$HOUSEHOLD_APPLIANCE (?SELF) :=> (INSTRUMENTALITY-ROLE ?SELF) :AXIOMS (AND (SUBJECT HOME_APPLIANCE$HOUSEHOLD_APPLIANCE ARTIFACTS) (DOCUMENTATION HOME_APPLIANCE$HOUSEHOLD_APPLIANCE "an appliance that does a particular job in the home") (HAS-I-TOPIC HOME_APPLIANCE$HOUSEHOLD_APPLIANCE |Furniture|))) (DEFCONCEPT AUTOPILOT$AUTOMATIC_PILOT (?SELF) :=> (AGENTIVE-FUNCTIONAL-OBJECT ?SELF) :AXIOMS (AND (SUBJECT AUTOPILOT$AUTOMATIC_PILOT ARTIFACTS) (DOCUMENTATION AUTOPILOT$AUTOMATIC_PILOT "automatically keeps ships or planes or spacecraft on a steady course") (HAS-I-TOPIC AUTOPILOT$AUTOMATIC_PILOT |Transport|) (WORD AUTOPILOT$AUTOMATIC_PILOT |autopilot|) (WORD AUTOPILOT$AUTOMATIC_PILOT |automatic pilot|))) (DEFCONCEPT TERMINOLOGY$NOMENCLATURE$LANGUAGE (?SELF) :=> (INFORMATION-DESCRIPTION ?SELF) :AXIOMS (AND (SUBJECT TERMINOLOGY$NOMENCLATURE$LANGUAGE COMMUNICATION) (DOCUMENTATION TERMINOLOGY$NOMENCLATURE$LANGUAGE "a system of words used in a particular discipline; ’legal terminology’; ’the language of sociology’") (HAS-I-TOPIC TERMINOLOGY$NOMENCLATURE$LANGUAGE |Linguistics|) (WORD TERMINOLOGY$NOMENCLATURE$LANGUAGE |terminology|) (WORD TERMINOLOGY$NOMENCLATURE$LANGUAGE |nomenclature|) (WORD TERMINOLOGY$NOMENCLATURE$LANGUAGE |language|))) (DEFCONCEPT CONDITION$STATUS (?SELF) :=> (SITUATION ?SELF) :AXIOMS (AND (SUBJECT CONDITION$STATUS STATES) (DOCUMENTATION CONDITION$STATUS "a condition or state at a particular time: ’a condition (or state) of disrepair’; ’the current status of the arms negotiations’") (HAS-I-TOPIC CONDITION$STATUS |Factotum|) (WORD CONDITION$STATUS |condition|) (WORD CONDITION$STATUS |status|))) (DEFCONCEPT PHASE$STAGE (?SELF) :=> (PARAMETER ?SELF) :AXIOMS (AND (SUBJECT PHASE$STAGE TIME) (DOCUMENTATION PHASE$STAGE "any distinct time period in a sequence of events; ’we are in a transitional stage in which many former ideas must be revised or rejected’") (HAS-I-TOPIC PHASE$STAGE |Biology|) (HAS-I-TOPIC PHASE$STAGE |Time_Period|) (WORD PHASE$STAGE |phase|) (WORD PHASE$STAGE |stage|))) (DEFCONCEPT CYCLE$RHYTHM$ROUND (?SELF) :=> (COURSE ?SELF) :AXIOMS (AND (SUBJECT CYCLE$RHYTHM$ROUND TIME) (DOCUMENTATION CYCLE$RHYTHM$ROUND "an interval during which a recurring sequence of events occurs; ’the neverending cycle of the seasons’") (HAS-I-TOPIC CYCLE$RHYTHM$ROUND |Time_Period|) (WORD CYCLE$RHYTHM$ROUND |cycle|) (WORD CYCLE$RHYTHM$ROUND |rhythm|)

339

(WORD CYCLE$RHYTHM$ROUND |round|))) (DEFCONCEPT REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD (?SELF) :=> (PARAMETER ?SELF) :AXIOMS (AND (SUBJECT REACTION_TIME$RESPONSE_TIME$LATENCY$ LATENT_PERIOD TIME) (DOCUMENTATION REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD "the time that elapses between a stimulus and the response to it") (HAS-I-TOPIC REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD |Chemistry|) (HAS-I-TOPIC REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD |Time_Period|) (WORD REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD |reaction_time|) (WORD REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD |response_time|) (WORD REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD |latency|) (WORD REACTION_TIME$RESPONSE_TIME$LATENCY$LATENT_PERIOD |latent_period|))) (DEFCONCEPT CRAFT (?SELF) :=> (VEHICLE_1 ?SELF) :AXIOMS (AND (SUBJECT CRAFT ARTIFACTS) (DOCUMENTATION CRAFT "a vehicle designed for navigation in or on water or air or through outer space") (HAS-I-TOPIC CRAFT |Transport|) (WORD CRAFT |craft|))) (DEFCONCEPT EXPLOITATION$DEVELOPMENT (?SELF) :=> (USE$USAGE$UTILIZATION$UTILISATION$EMPLOYMENT$EXERCISE ?SELF) :AXIOMS (AND (SUBJECT EXPLOITATION$DEVELOPMENT ACTS) (DOCUMENTATION EXPLOITATION$DEVELOPMENT "the act of making some area of land or water more profitable or productive or useful: ’the development of Alaskan resources’; ’the exploitation of copper deposits’") (HAS-I-TOPIC EXPLOITATION$DEVELOPMENT |Factotum|) (WORD EXPLOITATION$DEVELOPMENT |exploitation|) (WORD EXPLOITATION$DEVELOPMENT |development|))) (DEFCONCEPT HARVEST$HARVESTING$HARVEST_HOME (?SELF) :=> (GATHER$GATHERING_1 ?SELF) :AXIOMS (AND (SUBJECT HARVEST$HARVESTING$HARVEST_HOME ACTS) (DOCUMENTATION HARVEST$HARVESTING$HARVEST_HOME "the gathering of a ripened crop") (HAS-I-TOPIC HARVEST$HARVESTING$HARVEST_HOME |Factotum|) (WORD HARVEST$HARVESTING$HARVEST_HOME |harvest|) (WORD HARVEST$HARVESTING$HARVEST_HOME |harvesting|) (WORD HARVEST$HARVESTING$HARVEST_HOME |harvest home|))) (DEFCONCEPT DEVELOPMENT$EVOLUTION (?SELF) :=> (PROCESS ?SELF) :AXIOMS (AND (SUBJECT DEVELOPMENT$EVOLUTION PROCESSES) (DOCUMENTATION DEVELOPMENT$EVOLUTION "a process in which something passes by degrees to a more advanced or mature stage; ’the development of his ideas took many years’; ’the evolution of Greek civilization’; ’the slow development of her skill as a writer’") (HAS-I-TOPIC DEVELOPMENT$EVOLUTION |Factotum|) (WORD DEVELOPMENT$EVOLUTION |development|) (WORD DEVELOPMENT$EVOLUTION |evolution|))) (DEFCONCEPT DEVICE_1 (?SELF) :=> (INSTRUMENTALITY$INSTRUMENTATION ?SELF) :AXIOMS (AND (SUBJECT DEVICE_1 ARTIFACTS) (DOCUMENTATION DEVICE_1 "an instrumentality invented for a particular purpose; ’the device is small enough to wear on your wrist’; ’a device intended to conserve water’") (HAS-I-TOPIC DEVICE_1 |Factotum|) (WORD DEVICE_1 |device|))) (DEFCONCEPT PROVISION$PROVIDING$SUPPLY$SUPPLYING (?SELF) :=> (ACTIVITY_1 ?SELF) :AXIOMS (AND (SUBJECT PROVISION$PROVIDING$SUPPLY$SUPPLYING ACTS) (DOCUMENTATION PROVISION$PROVIDING$SUPPLY$SUPPLYING "the activity of supplying or providing something") (HAS-I-TOPIC PROVISION$PROVIDING$SUPPLY$SUPPLYING |Factotum|) (WORD PROVISION$PROVIDING$SUPPLY$SUPPLYING |provision|) (WORD PROVISION$PROVIDING$SUPPLY$SUPPLYING |providing|) (WORD PROVISION$PROVIDING$SUPPLY$SUPPLYING |supply|)

340

(WORD PROVISION$PROVIDING$SUPPLY$SUPPLYING |supplying|))) (DEFCONCEPT CONVEYANCE$TRANSPORT (?SELF) :=> (INSTRUMENTALITY$INSTRUMENTATION ?SELF) :AXIOMS (AND (SUBJECT CONVEYANCE$TRANSPORT ARTIFACTS) (DOCUMENTATION CONVEYANCE$TRANSPORT "something that serves as a means of transportation") (HAS-I-TOPIC CONVEYANCE$TRANSPORT |Transport|) (WORD CONVEYANCE$TRANSPORT |conveyance|) (WORD CONVEYANCE$TRANSPORT |transport|))) (DEFCONCEPT VEHICLE_1 (?SELF) :=> (CONVEYANCE$TRANSPORT ?SELF) :AXIOMS (AND (SUBJECT VEHICLE_1 ARTIFACTS) (DOCUMENTATION VEHICLE_1 "a conveyance that transports people or objects") (HAS-I-TOPIC VEHICLE_1 |Transport|) (WORD VEHICLE_1 |vehicle|))) (DEFCONCEPT GATHER$GATHERING_1 (?SELF) :=> (COLLECTION$COLLECTING$ASSEMBLING ?SELF) :AXIOMS (AND (SUBJECT GATHER$GATHERING_1 ACTS) (DOCUMENTATION GATHER$GATHERING_1 "the act of gathering something") (HAS-I-TOPIC GATHER$GATHERING_1 |Factotum|) (WORD GATHER$GATHERING_1 |gather|) (WORD GATHER$GATHERING_1 |gathering|))) (DEFCONCEPT EQUIPMENT (?SELF) :=> (INSTRUMENTALITY$INSTRUMENTATION ?SELF) :AXIOMS (AND (SUBJECT EQUIPMENT ARTIFACTS) (DOCUMENTATION EQUIPMENT "an artifact needed for an undertaking or to perform a service") (HAS-I-TOPIC EQUIPMENT |Factotum|) (WORD EQUIPMENT |equipment|))) (DEFCONCEPT TRANSACTION$DEALING$DEALINGS (?SELF) :=> (GROUP_ACTION ?SELF) :AXIOMS (AND (SUBJECT TRANSACTION$DEALING$DEALINGS ACTS) (DOCUMENTATION TRANSACTION$DEALING$DEALINGS "the act of transacting within or between groups (as carrying on commercial activities); ’no transactions are possible without him’; ’he has always been honest is his dealings with me’") (HAS-I-TOPIC TRANSACTION$DEALING$DEALINGS |Economy|) (WORD TRANSACTION$DEALING$DEALINGS |transaction|) (WORD TRANSACTION$DEALING$DEALINGS |dealing|) (WORD TRANSACTION$DEALING$DEALINGS |dealings|))) (DEFCONCEPT DEMAND_3 (?SELF) :=> (ECONOMIC_PROCESS ?SELF) :AXIOMS (AND (SUBJECT DEMAND_3 PROCESSES) (DOCUMENTATION DEMAND_3 "the ability and desire to purchase goods and services; ’the automobile reduced the demand for buggywhips’; ’the demand exceeded the supply’") (HAS-I-TOPIC DEMAND_3 |Economy|) (WORD DEMAND_3 |demand|))) (DEFCONCEPT COMMERCE$COMMERCIALISM$MERCANTILISM (?SELF) :=> (TRANSACTION$DEALING$DEALINGS ?SELF) :AXIOMS (AND (SUBJECT COMMERCE$COMMERCIALISM$MERCANTILISM ACTS) (DOCUMENTATION COMMERCE$COMMERCIALISM$MERCANTILISM "transactions having the objective of supplying commodities") (HAS-I-TOPIC COMMERCE$COMMERCIALISM$MERCANTILISM |Commerce|) (WORD COMMERCE$COMMERCIALISM$MERCANTILISM |commerce|) (WORD COMMERCE$COMMERCIALISM$MERCANTILISM |commercialism|) (WORD COMMERCE$COMMERCIALISM$MERCANTILISM |mercantilism|))) (DEFCONCEPT SUPPLY_1 (?SELF) :=> (ECONOMIC_PROCESS ?SELF) :AXIOMS (AND (SUBJECT SUPPLY_1 PROCESSES) (DOCUMENTATION SUPPLY_1 "offering goods and services for sale") (HAS-I-TOPIC SUPPLY_1 |Economy|) (WORD SUPPLY_1 |supply|))) (DEFCONCEPT ECONOMIC_PROCESS (?SELF) :=> (PROCESS ?SELF) :AXIOMS (AND (SUBJECT ECONOMIC_PROCESS PROCESSES) (DOCUMENTATION ECONOMIC_PROCESS "any process affecting the production and development and management of material wealth") (HAS-I-TOPIC ECONOMIC_PROCESS |Economy|) (WORD ECONOMIC_PROCESS |economic_process|))) (DEFCONCEPT COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS (?SELF) :=> (COMMERCE$COMMERCIALISM$MERCANTILISM ?SELF)

341

:AXIOMS (AND (SUBJECT COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS ACTS) (DOCUMENTATION COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS "the activity of providing goods and services involving financial and commercial and industrial aspects; ’computers are now widely used in business’") (HAS-I-TOPIC COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS |Enterprise|) (HAS-I-TOPIC COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS |Industry|) (WORD COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS |commercial enterprise|) (WORD COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS |business enterprise|) (WORD COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS |business|))) (DEFCONCEPT INDUSTRY$MANUFACTURE$MANUFACTURING (?SELF) :=> (COMMERCIAL_ENTERPRISE$BUSINESS_ENTERPRISE$BUSINESS ?SELF) :AXIOMS (AND (SUBJECT INDUSTRY$MANUFACTURE$MANUFACTURING ACTS) (DOCUMENTATION INDUSTRY$MANUFACTURE$MANUFACTURING "the organized action of making of goods and services for sale; ’American industry i s making increased use of computers to control production’") (HAS-I-TOPIC INDUSTRY$MANUFACTURE$MANUFACTURING |Enterprise|) (HAS-I-TOPIC INDUSTRY$MANUFACTURE$MANUFACTURING |Industry|) (WORD INDUSTRY$MANUFACTURE$MANUFACTURING |industry|) (WORD INDUSTRY$MANUFACTURE$MANUFACTURING |manufacture|) (WORD INDUSTRY$MANUFACTURE$MANUFACTURING |manufacturing|))) (DEFCONCEPT FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY (?SELF) :=> (PLANT$WORKS$INDUSTRIAL_PLANT ?SELF) :AXIOMS (AND (SUBJECT FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY ARTIFACTS) (DOCUMENTATION FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY "buildings with facilities for manufacturing") (HAS-I-TOPIC FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY |Enterprise|) (HAS-I-TOPIC FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY |Industry|) (WORD FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY |factory|) (WORD FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY |mill|) (WORD FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY |manufacturing plant|) (WORD FACTORY$MILL$MANUFACTURING_PLANT$MANUFACTORY |manufactory|))) (DEFCONCEPT CORD_1 (?SELF) :=> (LINE_2 ?SELF) :AXIOMS (AND (SUBJECT CORD_1 ARTIFACTS) (DOCUMENTATION CORD_1 "a line made of twisted fibers or threads") (HAS-I-TOPIC CORD_1 |Factotum|) (WORD CORD_1 |cord|))) (DEFCONCEPT DISAGREEMENT$DISSENSION (?SELF) :=> (CONFLICT_4 ?SELF) :AXIOMS (AND (SUBJECT DISAGREEMENT$DISSENSION STATES) (DOCUMENTATION DISAGREEMENT$DISSENSION "a conflict of people’s opinions or actions or characters") (HAS-I-TOPIC DISAGREEMENT$DISSENSION |Factotum|) (WORD DISAGREEMENT$DISSENSION |disagreement|) (WORD DISAGREEMENT$DISSENSION |dissension|))) (DEFCONCEPT ORGANIC_PROCESS$BIOLOGICAL_PROCESS (?SELF) :=> (NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY ?SELF) :AXIOMS (AND (SUBJECT ORGANIC_PROCESS$BIOLOGICAL_PROCESS PROCESSES) (DOCUMENTATION ORGANIC_PROCESS$BIOLOGICAL_PROCESS "a process occurring in living organisms") (HAS-I-TOPIC ORGANIC_PROCESS$BIOLOGICAL_PROCESS |Biology|) (WORD ORGANIC_PROCESS$BIOLOGICAL_PROCESS |organic_process|) (WORD ORGANIC_PROCESS$BIOLOGICAL_PROCESS |biological_process|))) (DEFCONCEPT GROUP_ACTION (?SELF) :=> (ACT$HUMAN_ACTION$HUMAN_ACTIVITY ?SELF) :AXIOMS (AND (SUBJECT GROUP_ACTION ACTS) (DOCUMENTATION GROUP_ACTION "action taken by a group of people") (HAS-I-TOPIC GROUP_ACTION |Factotum|) (WORD GROUP_ACTION |group action|))) (DEFCONCEPT PLANT$WORKS$INDUSTRIAL_PLANT (?SELF) :=> (BUILDING_COMPLEX$COMPLEX ?SELF)

342

:AXIOMS (AND (SUBJECT PLANT$WORKS$INDUSTRIAL_PLANT ARTIFACTS) (DOCUMENTATION PLANT$WORKS$INDUSTRIAL_PLANT "buildings for carrying on industrial labor; ’they built a large plant to manufacture automobiles’") (HAS-I-TOPIC PLANT$WORKS$INDUSTRIAL_PLANT |Industry|) (WORD PLANT$WORKS$INDUSTRIAL_PLANT |plant|) (WORD PLANT$WORKS$INDUSTRIAL_PLANT |works|) (WORD PLANT$WORKS$INDUSTRIAL_PLANT |industrial plant|))) (DEFCONCEPT ACTIVITY_1 (?SELF) :=> (ACT$HUMAN_ACTION$HUMAN_ACTIVITY ?SELF) :AXIOMS (AND (SUBJECT ACTIVITY_1 ACTS) (DOCUMENTATION ACTIVITY_1 "any specific activity or pursuit; ’they avoided all recreational activity’") (HAS-I-TOPIC ACTIVITY_1 |Factotum|) (WORD ACTIVITY_1 |activity|))) (DEFCONCEPT NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY (?SELF) :=> (PROCESS ?SELF) :AXIOMS (AND (SUBJECT NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY PROCESSES) (DOCUMENTATION NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY "a process existing in or produced by nature (rather than by the intent of human beings); ’the action of natural forces’; ’volcanic activity’") (HAS-I-TOPIC NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY |Factotum|) (WORD NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY |natural_process|) (WORD NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY |natural_action|) (WORD NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY |action|) (WORD NATURAL_PROCESS$NATURAL_ACTION$ACTION$ACTIVITY |activity|))) (DEFCONCEPT COLLECTION$COLLECTING$ASSEMBLING (?SELF) :=> (GROUPING ?SELF) :AXIOMS (AND (SUBJECT COLLECTION$COLLECTING$ASSEMBLING ACTS) (DOCUMENTATION COLLECTION$COLLECTING$ASSEMBLING "the act of gathering something together") (HAS-I-TOPIC COLLECTION$COLLECTING$ASSEMBLING |Factotum|) (WORD COLLECTION$COLLECTING$ASSEMBLING |collection|) (WORD COLLECTION$COLLECTING$ASSEMBLING |collecting|) (WORD COLLECTION$COLLECTING$ASSEMBLING |assembling|))) (DEFCONCEPT GROUPING (?SELF) :=> (ACTIVITY_1 ?SELF) :AXIOMS (AND (SUBJECT GROUPING ACTS) (DOCUMENTATION GROUPING "the activity of putting things together in groups") (HAS-I-TOPIC GROUPING |Factotum|) (WORD GROUPING |grouping|))) (DEFCONCEPT BUILDING_COMPLEX$COMPLEX (?SELF) :=> (STRUCTURE$CONSTRUCTION ?SELF) :AXIOMS (AND (SUBJECT BUILDING_COMPLEX$COMPLEX ARTIFACTS) (DOCUMENTATION BUILDING_COMPLEX$COMPLEX "a whole building made up of interconnected or related structures") (HAS-I-TOPIC BUILDING_COMPLEX$COMPLEX |Factotum|) (WORD BUILDING_COMPLEX$COMPLEX |building complex|) (WORD BUILDING_COMPLEX$COMPLEX |complex|)))

343