# LLM-driven ontology extraction: techniques, tools, and practical patterns

Large language models have become the dominant approach for extracting structured ontological knowledge from unstructured text, with **schema-guided prompting** emerging as the single most effective technique — improving extraction accuracy by up to 44% while reducing hallucinations by 22%. The field has matured rapidly since 2023, producing purpose-built tools like OntoGPT/SPIRES, standardized benchmarks like LLMs4OL, and a convergent best-practice architecture: define a target schema, extract iteratively in decomposed passes, ground entities against existing ontologies, and validate with both rule-based and LLM-based checks. For domains with sparse existing formal structure — behavioral sciences, executive function modeling, self-help/recovery programs — competency-question-driven bootstrapping combined with adjacent ontology references offers the most reliable path. Claude models consistently outperform GPT-4 variants on ontology generation stability and structured output consistency, though both require multi-step validation pipelines to achieve production-quality results.

## The schema-first extraction paradigm now dominates

The single most important architectural insight from 2023–2025 research is that **unconstrained triple extraction from text produces unreliable results**, while schema-constrained extraction dramatically improves precision. The SPIRES method (Caufield, Mungall et al., *Bioinformatics* 2024) established this pattern: define your target ontology structure as a LinkML schema (YAML-based), automatically generate extraction prompts from that schema, recursively extract nested semantic structures, then ground entities against external ontologies. OntoGPT, the open-source implementation, returned **correct ontology identifiers for 97–98 out of 100 Gene Ontology terms**, versus just 3 out of 100 from raw GPT-3.5-turbo without grounding.

The TextMine evaluation quantified this precisely: prompts embedding ontology specifications and examples improved triple extraction accuracy by **up to 44.2%**, reduced hallucinations by **22.5%**, and increased consistency by **20.9%** compared to unconstrained extraction. A VLDB 2024 workshop study confirmed that Chain-of-Thought prompting combined with ontology constraints "markedly reduced the variety of relationship types" in extracted triples — the LLM stops inventing relations and conforms to the specified schema.

This schema-first approach maps cleanly to lightweight formalisms. You define Pydantic models representing your entity types, properties, and relationships; pass the JSON Schema to the LLM via structured output modes (OpenAI's `response_format`, Anthropic's tool use with `input_schema`, or constrained-decoding libraries like Outlines); and get back validated, typed JSON that can be trivially converted to JSON-LD by adding `@context` mappings. LinkML takes this further by auto-generating both JSON Schema for validation and JSON-LD contexts for semantic web interoperability from a single YAML definition.

## Most effective prompting strategies, ranked by evidence

Research from 2023–2025 has tested numerous prompting approaches on ontology extraction tasks. The evidence points to a clear effectiveness hierarchy:

**Schema-guided prompting with explicit ontology constraints** is the top performer. Embed your allowed entity types, relationship types, cardinality constraints, and ID conventions directly in the prompt. The OntoMetric framework (Yu et al., 2025) demonstrated a concrete pattern: provide a "connection map" listing allowed `(subject_type, predicate, object_type)` triples, required fields per entity type, and ID format conventions (e.g., `ENT_{type}_{number}`). This achieved **65–90% semantic accuracy and 80–90% schema compliance**.

**Few-shot prompting with 1–3 domain-relevant examples** provides the next-largest gain. Polat et al. (*Semantic Web Journal*, 2025) found a single example improves performance **2–3× over zero-shot**, with diminishing returns beyond three examples. Critically, **RAG-retrieved examples** — dynamically selecting demonstrations similar to the input text — achieved the best absolute performance across all LLMs tested, significantly outperforming random or canonical examples.

**Decomposed multi-step extraction** consistently outperforms single-prompt approaches. The axiom-by-axiom prompting method (arXiv 2512.05594) was "more successful overall" than direct prompting for identifying ontological axioms. The practical pattern decomposes extraction into: (1) extract concepts/entities, (2) extract taxonomic (is-a) relations, (3) extract non-taxonomic relations and properties, (4) validate and reconcile. Each step receives the accumulated context from previous steps. The NeOn-GPT pipeline (ESWC 2024) operationalized this as: scope definition → competency question generation → entity/relationship extraction → OWL draft → syntax validation → consistency checking.

**Chain-of-Thought with ontology constraints** improves conformance in 6–8 out of 10 domains tested. Zero-shot CoT ("let's think step by step") adds modest value, but CoT combined with explicit ontological constraints creates a multiplicative effect — the reasoning traces help the LLM map extracted concepts to the correct schema categories. The **Ontogenia metacognitive prompting** technique (Lippolis et al., ESWC 2025) takes this further by having the LLM reflect on its own ontology modeling decisions.

**Role-play prompting** ("You are an experienced Knowledge Engineer") helps with appropriate modeling choices, particularly for generating competency questions and making design decisions about class versus instance boundaries. This is most useful in the early planning phases of ontology extraction rather than during data extraction itself.

## Key papers and research groups driving the field

The period from 2023 to 2025 produced several foundational papers that defined the current state of the art:

**OntoGPT/SPIRES** (Caufield, Hegde, Emonet, Harris, Joachimiak, Matentzoglu, Mungall et al., *Bioinformatics* 2024, btae104) established the schema-driven extraction paradigm. The Mungall Lab at Lawrence Berkeley National Laboratory, part of the Monarch Initiative, remains the most productive group for biomedical ontology extraction tooling. Their ecosystem includes OntoGPT, MapperGPT for ontology alignment, and LinkML for schema definition. GitHub: `monarch-initiative/ontogpt`.

**LLMs4OL** (Babaei Giglou, D'Souza, Auer, ISWC 2023) proposed the first systematic evaluation framework for LLM-based ontology learning, testing 9 LLM families across term typing, taxonomy discovery, and non-taxonomic relation extraction on WordNet, GeoNames, UMLS, and Schema.org. This spawned the **LLMs4OL Challenge** at ISWC, now in its second edition (2025), which has become the field's primary benchmark. The 2025 challenge added a Text2Onto task and found that **hybrid pipelines integrating commercial LLMs with domain-tuned embeddings** achieved strongest overall performance. GitHub: `HamedBabaei/LLMs4OL`.

**OLLM** (Lo et al., NeurIPS 2024) introduced end-to-end ontology learning by fine-tuning LLMs with a custom regularizer to reduce overfitting on high-frequency concepts, modeling entire ontology subcomponents rather than individual relations. This represents a shift from pipeline decomposition toward holistic ontology generation. GitHub: `andylolu2/ollm`.

**SAC-KG** (Chen et al., ACL 2024) achieved **89.3% precision** at million-node-scale knowledge graph construction using a Generator-Verifier-Pruner multi-agent architecture — demonstrating that LLM-based extraction can scale to production volumes. **GraphRAG** (Edge et al., Microsoft Research, 2024) uses LLMs to build entity knowledge graphs from documents with hierarchical community summaries via Leiden clustering, producing the most widely adopted production pattern for corpus-scale knowledge structuring. GitHub: `microsoft/graphrag`.

**KGGen** (Stanford STAIR Lab, NeurIPS 2025) introduced an entity-clustering approach that addresses the critical deduplication problem — achieving **66% accuracy on the MINE benchmark** versus 48% for GraphRAG and 30% for OpenIE. Its three-stage extract-aggregate-cluster pipeline with LLM-as-Judge entity resolution represents the current best approach for clean KG construction from text. GitHub: `stair-lab/kg-gen`.

Additional notable papers include **RELATE** (2025) for biomedical relation extraction with ontology constraints (52% exact match, 94% accuracy@10 on ChemProt), **TELEClass** (Zhang et al., ACM Web Conference 2025) for taxonomy enrichment, **TaxMorph** (2025) for LLM-refined taxonomies, and the **KARMA** multi-agent architecture (OpenReview 2025) that decomposes KG enrichment across specialized agents for ingestion, NER, relation extraction, conflict resolution, and evaluation.

## The open-source tooling landscape

Purpose-built tools for ontology extraction sit alongside general structured-output libraries, forming a layered toolkit:

**OntoGPT/SPIRES** (~539 GitHub stars, BSD-3) is the most ontology-specific tool available. It takes LinkML schemas and free text as input, recursively extracts nested structures via zero-shot prompting, and grounds entities against external ontologies (GO, MONDO, FOODON, MESH) using annotators like Gilda and BioPortal. Output formats include JSON, YAML, RDF, and OWL. It supports GPT models and Ollama-hosted local models. The key limitation is precision degradation beyond two levels of nesting.

**OLAF** (Ontology Learning Applied Framework, `wikit-ai/olaf`, Apache-2.0) is the most complete end-to-end ontology learning pipeline — covering term extraction through synonym enrichment, concept grouping, taxonomy construction, relation extraction, and axiom discovery, outputting OWL ontologies in Turtle format. It includes LLM-based components for each pipeline step but has a small community.

**KGGen** (~1,007 stars, MIT) offers the best entity deduplication through its extract-aggregate-cluster pipeline using DSPy internally. It supports any LLM via LiteLLM routing and includes an MCP server for Claude Desktop integration — making it particularly accessible for Claude-centric workflows.

For **structured output infrastructure**, **Instructor** (`567-labs/instructor`, ~7k+ stars, MIT) is the lightest-weight option — it patches any LLM client to accept Pydantic `response_model` parameters with automatic retry on validation failures. **DSPy** (`stanfordnlp/dspy`, ~20k+ stars, MIT) provides optimizable extraction pipelines with TypedPredictors and DSPy Assertions for enforcing structural constraints, plus automatic prompt optimization. **Outlines** (`dottxt-ai/outlines`, ~10k+ stars, Apache-2.0) and **Guidance** (`guidance-ai/guidance`, ~19k+ stars, MIT) guarantee structural validity through constrained decoding — modifying logits in real-time to prevent invalid tokens, eliminating parsing failures entirely.

**LangChain's `LLMGraphTransformer`** (in langchain-experimental) provides the most widely adopted graph extraction pattern with schema-guided modes using `allowed_nodes` and `allowed_relationships`. **LlamaIndex's `PropertyGraphIndex`** with `SchemaLLMPathExtractor` offers an alternative schema-guided extraction path. Both integrate with Neo4j for graph storage. **OntoCast** (`growgraph/ontocast`) uniquely co-evolves ontologies as it processes documents, outputting SPARQL operations for incremental updates.

For biomedical work specifically, **DeepOnto** (`KRR-Oxford/DeepOnto`, Apache-2.0) bridges OWL API with Python deep learning frameworks, offering taxonomy extraction, BERTMap alignment, and biomedical ontology matching benchmarks — though it focuses on manipulating existing ontologies rather than extracting from text.

## Validation pipelines that actually reduce hallucination

LLM-generated ontological structures require multi-layered validation. The evidence supports a specific validation stack:

**Ontology grounding** is the single highest-impact validation step. SPIRES demonstrated that post-extraction entity linking against external ontologies (querying BioPortal, OBO Foundry, Wikidata) transforms raw LLM string outputs into verified ontology identifiers. Without grounding, **over 90% of Gene Ontology identifiers generated by GPT-4o are incorrect** (Caufield et al.). With grounding, accuracy reaches 97–98%. For domains without rich reference ontologies, FAISS-based similarity search against Wikidata names (as in the Two-Step Pipeline from ACL TextGraphs 2024) provides an analogous function — the top-5 similar canonical names are fed back to the LLM for selection.

**Schema-constrained generation** prevents structural hallucinations at the source. Using Outlines or Guidance for constrained decoding eliminates malformed JSON entirely. API-level structured output modes (OpenAI's JSON Schema mode, Anthropic's tool use) provide similar guarantees without local model hosting. Beyond structural validity, embedding domain-range constraints in prompts catches semantic errors: the Two-Step Pipeline validates that hierarchical types of extracted subjects and objects align with relation constraints in the target ontology.

**Self-consistency through multiple runs** shows "significant improvements across all metrics" when combined with few-shot demonstrations (Polat et al., 2025). Running the same extraction 3–5 times and taking the intersection or majority vote filters out stochastic hallucinations. The **KARMA** framework adds an explicit Conflict Resolution Agent that conducts "LLM-based debate" when contradictory extractions arise.

**Iterative self-repair loops** catch residual errors. A validator inspects every candidate assertion against domain-range constraints; violations trigger an analyze-errors → fix-schema → fix-instances cycle until consistency is achieved. The four-stage agent pipeline using this approach achieved **67.5% fact recall on the MINE benchmark**. The **CyberBOT** system (2025) takes validation further by applying Description Logic reasoning over candidate answers, checking class disjointness, range/domain constraints, and logical axioms — achieving **15 percentage point hallucination reduction**.

**Provenance tracking** provides auditability. SPIRES labels every extracted entity and relationship with its source text segment and uses low-temperature (low-creativity) settings. The practical recommendation is to always extract with `temperature=0` or near-zero, include explicit instructions to "only extract what was found in the text," and store source-text spans alongside extracted triples.

## Iterative refinement follows a convergent multi-pass architecture

Practitioners have converged on a consistent pattern for iterative ontology refinement that mirrors the classical "ontology learning layer cake" but leverages LLMs at each step:

**Pass 1 — Concept extraction and initial taxonomy.** Extract key domain terms and organize them into a preliminary is-a hierarchy. The competency-question approach (Kommineni et al., 2024) works well here: generate questions the ontology should answer, then extract concepts needed to answer them. Prompt: "Given this domain text, identify the main concepts and organize them into a taxonomy with parent-child (is-a) relationships."

**Pass 2 — Relation enrichment.** With the taxonomy as context, extract non-taxonomic relations (part-of, causes, treats, enables). Provide the existing taxonomy in the prompt so the LLM can reference established concept names. The sequential approach (Bakker et al., CEUR-WS 2024) feeds back previously extracted classes and individuals as context for each subsequent extraction step.

**Pass 3 — Property and attribute extraction.** For each concept, extract datatype properties (attributes with literal values) and refine object properties (relationships between concepts). OntoKGen's adaptive iterative CoT algorithm (Abolhasani et al., 2024) includes an interactive user interface at this stage for ontology confirmation.

**Pass 4 — Validation and reconciliation.** Run consistency checks (RDFLib syntax validation, reasoner-based logical checks, schema compliance verification). Feed errors back to the LLM for correction. The NeOn-GPT pipeline automates this: errors detected by RDFLib are fed back to the LLM for auto-correction.

**Pass 5 — Grounding and alignment.** Map extracted entities to existing ontology terms where applicable. For biomedical domains, MapperGPT combines lexical mapping with LLM-based semantic refinement for ambiguous cases. For sparse domains, this pass may instead align with upper ontologies (BFO, PROV-O) or adjacent domain ontologies.

The **KGFiller method** (Ciatto et al., ScienceDirect 2024) offers an alternative bootstrapping pattern: start with a minimal schema defining just classes and properties, query the LLM as an "oracle" to populate instances, merge duplicates via LLM-assisted deduplication, then iterate. In food domain testing, this produced ontologies with **1,176 instances and 1,211 relations** from minimal seed schemas.

## Claude outperforms GPT-4 on ontology generation stability

Direct head-to-head benchmarks remain limited, but available evidence consistently favors Claude for ontology tasks. The **Lettria benchmark** (ISWC 2024) provides the most direct comparison: Claude 3.5 Sonnet achieved the **best overall F1 for class generation (0.76)** with the most stable performance regardless of whether a use case specification was provided. GPT-4o achieved F1 of 0.70 with a use case but **dropped drastically without one** — indicating greater sensitivity to prompt completeness. On the IEEE engineering ontology benchmark, **Claude 3 Sonnet achieved F1 = 0.967** (best among 17 models tested), substantially outperforming GPT-4 variants. The **OntoLogX** cybersecurity evaluation (2025) found Claude Sonnet 4 achieved strongest results across all metrics for ontology-guided KG extraction.

Practical differences matter for pipeline design. Claude produces **more consistent structured output formatting** — valid JSON in all cases during high-volume extraction — while GPT-4o shows syntax errors at scale. Claude's **200K+ token context window** provides advantages for processing entire documents or corpora. GPT-4's native Structured Outputs mode with JSON Schema enforcement is more mature than Claude's tool-use approach, but Instructor and similar libraries abstract this difference away.

For open-source models, **Llama 3.1-405B-Instruct** was the best open-source performer in Lippolis et al.'s evaluation, producing ontologies competitive with OpenAI o1-preview. The **DREAM-LLMs** entry in LLMs4OL 2025 ensembled GPT-4o, Claude Sonnet 4, DeepSeek-V3, and Gemini 2.5 Pro for robust term typing — suggesting that model ensembling represents the frontier approach. At the 7B parameter scale, **Mistral-7B** and **Dolphin-Mistral-7B** (F1 = 0.920 on IEEE benchmark) provide surprisingly strong performance for resource-constrained deployments, though quality degrades significantly for complex domain ontologies.

## JSON-LD and lightweight output schemas in practice

No mainstream tool directly outputs JSON-LD from LLM extraction in a single step. Instead, the practical pattern involves extracting into validated JSON using Pydantic schemas, then mapping to JSON-LD via context definitions. **LinkML** automates this entirely — a single YAML schema definition generates both the JSON Schema for constrained LLM extraction and the JSON-LD `@context` for semantic interoperability:

```yaml
classes:
  Concept:
    attributes:
      label: {range: string}
      broader: {range: Concept}
      related_to: {range: Concept, multivalued: true}
      properties: {range: Property, multivalued: true}
```

This compiles to a JSON-LD context mapping `broader` to SKOS broader-than, `label` to `rdfs:label`, etc. The extracted JSON is simultaneously valid against the JSON Schema and interpretable as linked data.

For simpler use cases, the dominant output pattern is **typed JSON triplets** with an entity registry:

```json
{
  "entities": [
    {"id": "ENT_Concept_1", "type": "Concept", "label": "Executive Function", 
     "description": "Higher-order cognitive processes..."}
  ],
  "relations": [
    {"source": "ENT_Concept_1", "predicate": "has_component", 
     "target": "ENT_Concept_2"}
  ]
}
```

The **OntoEKG** two-phase pattern (arXiv, Feb 2025) separates extraction from entailment: Phase 1 extracts flat classes and properties as JSON using Pydantic-enforced schemas; Phase 2 structures them into a hierarchy and serializes to RDF. This separation simplifies both the LLM's task and downstream processing.

For **concept maps and taxonomies** specifically, the SKOS (Simple Knowledge Organization System) vocabulary provides the lightest-weight formal target. Extracted hierarchies map naturally to `skos:broader`/`skos:narrower`, with `skos:related` for associative links and `skos:prefLabel`/`skos:altLabel` for synonym handling. This is substantially lighter than OWL while remaining standards-compliant.

## Domain-specific extraction requires fundamentally different strategies

**Biomedical extraction** benefits from the richest ecosystem. SNOMED CT, UMLS, Gene Ontology, and the OBO Foundry provide extensive reference ontologies for grounding. OntoGPT/SPIRES was built specifically for this domain. The critical insight is that **LLMs should never generate biomedical identifiers without post-extraction grounding** — over 90% will be wrong. Use SPIRES-style annotators (Gilda, BioPortal) or embedding-based retrieval (SapBERT, as in RELATE) to map extracted entities to canonical terms. RAG-based approaches consistently outperform pure generation for biomedical tasks. The LLMs4OL challenge found biomedical term typing and relation extraction are **more challenging** than general-domain tasks, with Gene Ontology tasks highlighting the need for specialized approaches.

**Social and behavioral sciences** present a fundamentally different challenge. The National Academies of Sciences (2022) report "Ontologies in the Behavioral Sciences" documented that behavioral sciences **lack well-established, widely shared formal definitions** for key concepts. Existing structures range from informal classification (DSM) to formal ontology (BCIO — Behaviour Change Intervention Ontology, with 12 central entities available in OWL on GitHub). The boundaries between describing and explaining phenomena are unclear, concepts are highly context-dependent, and different researchers use different terms for similar phenomena. The **BCIO** provides the best starting reference for behavioral intervention domains. For cognitive science and executive function modeling, the emerging **ADHD-KG** (Papadakis et al., 2023) covers symptoms, medications, clinical trials, and side-effects with MeSH concept linking, while Otal et al. (2024) demonstrated LLM-powered ADHD KG construction with Graph-RAG for context-aware querying. Alsaedi et al. (2024) proposed an ADHD conceptual model with **8 top-level classes** (subtypes, symptoms, behaviors, diagnostic criteria, treatment, risk factors, comorbidities, patient profile) and **13 key relationships** — a ready-made seed schema for LLM extraction.

**Self-help and recovery programs** represent a genuinely greenfield domain — searches returned zero formal ontology or knowledge graph work. The recommended bootstrapping approach is:

- Define competency questions manually (e.g., "What psychological concepts does Step 4 involve?" "What cognitive processes does this self-help technique target?")
- Compile a corpus from source texts (primary literature, clinical guidelines, experiential accounts)
- Use Claude (preferred for consistency) to extract an initial concept hierarchy with explicit schema constraints
- Reference adjacent ontologies: BCIO for behavioral change mechanisms, DSM-5 for mental health concepts, the ADHD conceptual model for executive function structure
- Apply the KGFiller pattern — start with a minimal schema and iteratively populate
- Run multiple extraction passes with consensus voting to handle the high output variability inherent in informal text domains
- Iterate with domain expert validation at every stage — LLMs cannot fully automate ontology creation in sparse domains but can reduce development time by **60–80%**

## Conclusion

The field has converged on a clear architectural pattern: schema-first extraction using LLMs produces dramatically better results than unconstrained triple extraction. The practical toolkit centers on OntoGPT/SPIRES for biomedical work, Instructor or DSPy with Pydantic schemas for custom domain extraction, and KGGen or LangChain's LLMGraphTransformer for knowledge graph construction. Multi-step pipelines that decompose extraction into concept identification, taxonomy construction, relation enrichment, and validation passes consistently outperform single-prompt approaches. Claude models show stronger stability and format consistency than GPT-4 variants on ontology tasks, though model ensembling across providers represents the frontier. For sparse-ontology domains like behavioral sciences and self-help/recovery, the competency-question bootstrapping approach — seeded with adjacent formal ontologies and validated iteratively by domain experts — offers the most reliable path from unstructured text to usable knowledge structures. The most underexplored opportunity lies at the intersection of these domains: no one has yet applied modern LLM extraction techniques to recovery programs, executive function coaching, or ADHD self-management literature, despite the existence of seed schemas and adjacent ontologies that make this tractable.