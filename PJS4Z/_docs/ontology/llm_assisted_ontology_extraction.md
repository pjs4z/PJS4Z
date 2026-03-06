# LLM-assisted ontology extraction: a practical field guide for 2025

**The tooling for extracting structured ontologies from messy text with LLMs has matured dramatically since 2023, and a solo developer can now build a production-quality knowledge graph pipeline in a weekend.** The most practical path for the Obsidian-to-Neo4j use case combines LangChain's `LLMGraphTransformer` or Stanford's `KGGen` for extraction, Neo4j's first-party `neo4j-graphrag` library for storage and entity resolution, and a lightweight "soft ontology" schema using confidence scores and relationship weights instead of formal OWL axioms. This report maps the full landscape of tools, repos, prompts, papers, and patterns — prioritizing startup-friendly approaches that accommodate fuzzy semantics and real-world messiness.

---

## The GitHub repos that actually ship copy-paste prompts

The single most influential prompt template in this space comes from **Microsoft GraphRAG** (~26k GitHub stars), whose entity extraction prompt defines the pattern almost everyone else copies. The core prompt instructs the LLM to extract entities with types and descriptions, then extract relationships with natural-language descriptions and a **strength score from 1–10** — a built-in fuzzy weighting mechanism. GraphRAG's iterative extraction loop is equally important: after initial extraction, a `CONTINUE_PROMPT` ("MANY entities were missed...") re-runs extraction, followed by a `LOOP_PROMPT` ("Are there more? YES/NO") that repeats until saturation. The `graphrag prompt-tune` command auto-adapts these prompts to your domain.

**KGGen** (`pip install kg-gen`, ~1k stars, Stanford/NeurIPS 2025) delivers the best extraction quality on benchmarks — **66% on MINE vs. GraphRAG's 48%** — through a three-stage pipeline: LLM extraction via DSPy structured output, cross-document aggregation, and iterative LM-based entity clustering that merges synonyms like "executive function" / "EF" / "executive functioning" into single nodes. It works with any LLM via LiteLLM and has an MCP server for Claude Desktop.

**rahulnyk/knowledge_graph** (~2.9k stars) is the most relevant repo for fuzzy/soft semantics. It uses a two-tier weighting system: W1 (explicit LLM-extracted relationships) plus W2 (contextual co-occurrence proximity), with similar pairs grouped and weights summed. This naturally produces multi-relationship edges with accumulated strength — exactly the "vibe-level" connections the ADHD recovery use case needs. Runs locally with Ollama and Mistral 7B at zero API cost.

Other notable repos include **Google LangExtract** (Apache 2.0, character-level source grounding, multi-pass extraction), **Delve/TnT-LLM** (Microsoft's taxonomy generation framework with a copy-paste LangGraph notebook for iterative taxonomy refinement), **OntoGPT/SPIRES** from the Monarch Initiative (schema-driven extraction with 40+ pre-built templates and ontology grounding), and **FareedKhan-dev/KG-Pipeline** (a clean Jupyter notebook walking through SPO triple extraction, normalization, and graph construction).

---

## Three frameworks dominate practical extraction

**LangChain's LLMGraphTransformer** is the most widely deployed option. It operates in two modes: a tool-based mode using structured output / function calling (preferred), and a prompt-based fallback with few-shot examples. The key configuration pattern:

```python
transformer = LLMGraphTransformer(
    llm=ChatOpenAI(model="gpt-4o"),
    allowed_nodes=["Concept", "Practice", "Symptom", "Strategy", "Phase"],
    allowed_relationships=[
        ("Practice", "HELPS_WITH", "Symptom"),
        ("Strategy", "SUPPORTS", "Concept"),
        ("Concept", "IS_A", "Concept"),
    ],
    node_properties=True,
    relationship_properties=True,
    strict_mode=True,
)
```

Setting `strict_mode=False` lets the LLM extract beyond your schema — acting as soft guidance rather than hard constraint. The `additional_instructions` parameter lets you append domain-specific instructions like "Also extract fuzzy relationships such as 'related to' and 'contradicts' with confidence scores." Native Neo4j integration via `langchain-neo4j` makes import trivial.

**LlamaIndex's PropertyGraphIndex** offers more modularity. Its `SchemaLLMPathExtractor` supports a `strict` toggle (schema as enforcement vs. suggestion), `DynamicLLMPathExtractor` provides guided-but-flexible extraction, and `SimpleLLMPathExtractor` lets the LLM infer everything freely. You can stack multiple extractors simultaneously. LlamaIndex also ships a native `ObsidianReader` that loads vault markdown directly, making the full pipeline Obsidian → PropertyGraphIndex → Neo4jPropertyGraphStore achievable in about **15 lines of Python**.

**Neo4j's first-party `neo4j-graphrag`** library (v1.13.0) provides a `SimpleKGPipeline` abstraction that handles chunking, extraction, embedding, and entity resolution in one call. Its killer feature: built-in **`FuzzyMatchResolver`** (RapidFuzz-based) and **`SpaCySemanticMatchResolver`** for entity deduplication — the critical challenge that most pipelines ignore. Supports OpenAI, Anthropic, Vertex AI, Cohere, Mistral, and Ollama.

---

## Seven prompt engineering patterns for ontology extraction

The literature converges on a set of reusable patterns that work across frameworks:

**Pattern 1 — Iterative extraction loop** (GraphRAG): Extract → CONTINUE_PROMPT ("many entities were missed") → LOOP_PROMPT ("are there more? YES/NO") → repeat until "NO". This consistently improves recall by **20–30%** over single-pass extraction.

**Pattern 2 — Multi-pass decomposition** (KGGen): Pass 1 extracts entities only, Pass 2 extracts relationships given known entities, Pass 3 identifies taxonomic hierarchies, Pass 4 performs entity resolution. Each pass uses a different system prompt optimized for its specific task, avoiding the quality degradation that comes from asking an LLM to do everything at once.

**Pattern 3 — Schema-as-soft-constraint** (LangChain/LlamaIndex): Provide allowed node types and relationship types as guidance, but set `strict_mode=False`. The LLM respects the schema ~80% of the time while still discovering unexpected structure. Post-processing can enforce constraints where needed.

**Pattern 4 — Confidence and strength scoring**: Every extracted relationship carries a `strength` (how strong the relationship is, 0–1) and `confidence` (how certain the extraction is, 0–1) score. The composite `weight = strength × confidence` enables fuzzy inference in graph queries. This pattern appears in GraphRAG (1–10 integer scale), KGGen, and can be added to any LLMGraphTransformer via `relationship_properties`.

**Pattern 5 — Relationship nature typing**: Beyond just the relationship label, classify each edge's epistemic nature: `causal`, `correlational`, `definitional`, `experiential`, or `vibes`. This enables different reasoning strategies over the same graph — clinical queries filter for causal/correlational edges, while exploration queries include experiential/vibes connections.

**Pattern 6 — Gleaning** (iterative self-review): After extraction, show the LLM its own output alongside the source text and ask: "What entities and relationships were missed? Are any confidence scores wrong?" Two gleaning rounds typically surface **10–15% additional structure** that the initial pass missed.

**Pattern 7 — Ontology-subset prompting** (CIDOC CRM extractor): Rather than including your full domain ontology in the prompt (expensive and noisy), include only the relevant subset. This achieves better precision than full ontology context at lower token cost — and is the practical way to incorporate domain knowledge without formal OWL schemas.

---

## Neo4j is the clear backend choice, and the integrations are mature

Neo4j has invested heavily in LLM integration. The **Neo4j LLM Knowledge Graph Builder** (neo4j-labs/llm-graph-builder) is a full React + FastAPI web application that transforms PDFs, docs, YouTube videos, and web pages into Neo4j knowledge graphs with zero code. It's the 4th most popular source of user interaction on AuraDB Free. Supports GPT-4o, Claude, Gemini, and Llama 3.

For programmatic access, three first-party integration points exist:

- **`neo4j-graphrag`** Python library: `SimpleKGPipeline` for extraction, `FuzzyMatchResolver` for entity dedup, multiple retrievers (vector, Cypher, hybrid) for querying
- **`langchain-neo4j`** package: `Neo4jGraph` (driver wrapper), `Neo4jVector` (vector store), `GraphCypherQAChain` (natural language → Cypher → natural language)
- **`llama-index-graph-stores-neo4j`**: `Neo4jPropertyGraphStore` with multiple built-in retrievers including `TextToCypherRetriever`

For fuzzy ontologies in Neo4j, the recommended schema stores confidence and strength as **relationship properties** rather than trying to map onto formal ontological structures. A practical schema for ADHD recovery:

```cypher
CREATE (practice:Practice:__Entity__ {
    name: "body_doubling", confidence: 0.95,
    description: "Working alongside another person for accountability",
    abstraction_level: "practice"
})
CREATE (practice)-[:HELPS_WITH {
    strength: 0.8, confidence: 0.85,
    nature: "experiential",
    evidence: "Body doubling helps maintain focus during boring tasks",
    weight: 0.68  // strength × confidence
}]->(symptom:Symptom {name: "poor_focus"})
```

Weighted Cypher queries then enable fuzzy inference: `WHERE r.confidence > 0.5 AND r.strength > 0.3 RETURN ... ORDER BY r.strength * r.confidence DESC`. Multi-hop reasoning multiplies weights along paths using `REDUCE`, and **Neosemantics (n10s)** supports hierarchical category inference via `IS_A` traversal without requiring full OWL reasoning.

---

## Bridging Obsidian vaults to knowledge graphs

The most practical pipeline is **LlamaIndex's `ObsidianReader` → `PropertyGraphIndex` → `Neo4jPropertyGraphStore`**, which handles the entire flow in a single API:

```python
documents = ObsidianReader("/path/to/vault").load_data()
index = PropertyGraphIndex.from_documents(
    documents, llm=OpenAI(model="gpt-4o"),
    property_graph_store=Neo4jPropertyGraphStore(url="bolt://localhost:7687")
)
```

For structural extraction without LLM costs, **`obsidiantools`** parses wikilinks, tags, YAML frontmatter, and backlinks into a NetworkX graph that can be loaded into Neo4j via the Python driver. The deprecated but functional **`semantic-markdown-converter`** (`pip install semantic-markdown-converter`) streams directly from Obsidian to Neo4j, interpreting tags as node labels, frontmatter as properties, and wikilinks as relationships.

Two emerging Obsidian plugins deserve attention: **MegaMem** transforms vaults into temporal knowledge graphs using Graphiti with MCP protocol support, embracing "progressive formalization." **ODIN** (from Memgraph) integrates LLMs via LangChain for vault-wide knowledge graph visualization with link prediction and question generation — though it targets Memgraph rather than Neo4j.

The **recommended hybrid approach** for maximum coverage: (1) parse vault structure with `obsidiantools` to capture explicit links, tags, and metadata as a structural layer; (2) feed note content through `LLMGraphTransformer` or `neo4j-graphrag`'s `SimpleKGPipeline` to extract semantic entities and relationships as a conceptual layer; (3) merge both layers in Neo4j using `MERGE` operations; (4) run entity resolution with `FuzzyMatchResolver` to deduplicate across layers.

---

## The research papers that matter most

**OLLM** (NeurIPS 2024, github.com/andylolu2/ollm) introduced end-to-end ontology learning by fine-tuning LLMs to model entire sub-graphs rather than individual triples. Its novel Fuzzy F1 metric uses cosine similarity of embeddings rather than exact string matching — achieving **0.915 Fuzzy F1 on Wikipedia** vs. 0.538 for Hearst patterns. The key finding: prompting alone produces poor structural integrity (Motif Distance 0.314–0.354 vs. 0.050–0.080 for fine-tuned), meaning production ontologies need either fine-tuning or significant post-processing.

**OntoChat** (ESWC 2024, github.com/King-s-Knowledge-Graph-Lab/OntoChat) demonstrated conversational ontology engineering through iterative user story creation and competency question refinement. This is the most accessible approach for non-ontologists — a solo knowledge worker can refine an ontology from notes through conversation with an LLM.

**OntoKGen** (arXiv 2412.00608) developed an interactive pipeline using adaptive iterative Chain-of-Thought with a critical insight: **"there is no universally correct ontology — it is inherently based on the user's preferences."** It includes direct Neo4j integration.

**iText2KG** (arXiv 2409.03284, github.com/AuvaLab/itext2kg) addresses incrementality — adding new documents to an existing knowledge graph without reprocessing everything. Achieves **74.5% semantic consistency** across diverse document types with zero-shot extraction and no predefined entity types.

For the ADHD domain specifically, **ADHD-KG** (Papadakis et al., 2023) is the first published knowledge graph for ADHD integrating clinical trials and medications, while a 2024 arXiv paper (2409.12853) demonstrated LLM-based ADHD knowledge graph construction with network analysis — validating that this approach works for the target domain.

---

## The practical 80/20 path for a solo developer

The most efficient pipeline for extracting ontological structure from an Obsidian vault, loading into Neo4j, and building an inference backbone for an ADHD recovery application:

1. **Parse the vault** with a Python script extracting text, wikilinks, tags, and YAML frontmatter — or use LlamaIndex's `ObsidianReader` directly
2. **Define ~8 node types** (`Symptom`, `Practice`, `Strategy`, `Phase`, `Trigger`, `Insight`, `Resource`, `Principle`) and **~12 relationship types** (`HELPS_WITH`, `CAUSES`, `SUPPORTS`, `CONTRADICTS`, `REQUIRES`, `PART_OF`, `IS_A`, `TRIGGERS`, `MITIGATES`, `SYNERGIZES_WITH`, `MEASURED_BY`, `PHASE_OF`) as a soft schema
3. **Extract with LLMGraphTransformer** using `strict_mode=False`, `node_properties=True`, `relationship_properties=True` — adding `additional_instructions` to include confidence/strength scores and relationship nature
4. **Load into Neo4j Aura** (free tier) with `include_source=True` for provenance tracking and `baseEntityLabel=True` for a shared `__Entity__` index
5. **Run entity resolution** with `neo4j-graphrag`'s `FuzzyMatchResolver` to merge duplicate entities
6. **Query with weighted Cypher** — composite scoring via `r.strength * r.confidence`, multi-hop reasoning with `REDUCE`, and threshold-based filtering for different confidence levels

**Estimated effort**: 2–3 weekends for a working prototype from ~200 Obsidian notes. **Estimated cost**: $10–30 in API calls using GPT-4o-mini for bulk extraction. **Expected output**: ~400 unique entities, ~1,000 weighted relationships, all queryable as a fuzzy inference engine.

## Conclusion

The field has converged on a practical consensus: property graphs with weighted, typed relationships beat formal ontologies for applied use cases. The critical innovation isn't in extraction (several tools do this well) but in **entity resolution** — KGGen's LM-based clustering outperforms everything else and should be adopted regardless of which extraction framework you choose. The "soft ontology" pattern of storing `confidence`, `strength`, and `nature` as relationship properties in Neo4j provides the theoretical rigor of fuzzy logic with the practical simplicity of a property graph. For the ADHD recovery use case specifically, the combination of experiential knowledge (high in personal notes) and clinical knowledge (high in referenced materials) maps naturally to the `nature` field, enabling queries that can distinguish "this worked for me" from "this is clinically validated" — a distinction that formal ontologies struggle to represent but that weighted property graphs handle elegantly.