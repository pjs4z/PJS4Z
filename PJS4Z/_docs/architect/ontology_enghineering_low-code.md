# Ontology engineering for ADHD recovery: a low-code architecture guide

**The fastest path to a working ontology demo combines Claude's structured outputs with Obsidian's plugin ecosystem and an n8n automation bridge to Notion — achievable in 1–2 days for under $20.** No formal ontology of a 12-step-style recovery program exists in the literature, which means the founder has greenfield opportunity but must build the schema from scratch. The good news: LLM-powered ontology extraction has matured dramatically since 2024, with tools like OntoGPT and KGGen reducing what once required months of knowledge engineering to hours of prompt-guided extraction. Four viable architectures emerge, ranked from a weekend hack to a production system.

The core insight driving every architecture below is that **Obsidian markdown with YAML frontmatter is itself a lightweight ontology format** — no OWL or RDF required. Combined with plugins like Dataview, Breadcrumbs, and Metadata Menu, an Obsidian vault becomes a human-readable, AI-editable knowledge graph where the founder can curate concepts by simply editing text files.

---

## The ontology schema: what the recovery program knowledge graph looks like

Before choosing architecture, the founder needs a clear picture of what the ontology contains. No published formal ontology exists for AA-style 12-step programs, but the closest analog is the **Behaviour Change Intervention Ontology (BCIO)** from UCL's Human Behaviour-Change Project, which models 42 upper-level entities organized around intervention content, mechanisms of action, context, engagement, and behavioral outcomes. The **Addiction Ontology (AddictO)** extends BCIO with addiction-specific concepts. Both are open-source on GitHub and provide structural templates worth adapting.

For an ADHD recovery program integrating intentional stance theory and dopamine science, the ontology needs six interconnected domains:

**Problem definition (intentional stance layer).** Daniel Dennett's intentional stance framework offers three levels for understanding ADHD behavior: the physical stance (dopamine transporter density, prefrontal hypoactivity), the design stance (how the brain's reward system was "designed" to function), and the intentional stance (attributing beliefs, desires, and rationality to the person with ADHD). The ontology should model the person as a rational agent whose dopamine-driven urges are understood mechanistically at the design level while recovery operates at the intentional level — beliefs about self, desires for change, and intentions for behavior modification.

**Neuroscience layer.** Key entities include dopamine (DA) and norepinephrine (NE) as neurotransmitters; the dopamine transporter (DAT/SLC6A3), D1/D2/D4 receptors, and COMT enzyme as proteins; fronto-striatal circuits, prefrontal cortex, and the default mode network as brain structures; and the **inverted-U model** of optimal dopamine levels as the central theoretical framework. The phasic/tonic dopamine imbalance model and the dual pathway model (executive function + reward processing) provide the mechanistic backbone.

**Recovery methodology layer.** Modeled after SMART Recovery's four-point structure (which is more CBT-aligned than AA and maps more cleanly to an ontology): building motivation, coping with urges, managing thoughts/feelings/behaviors, and living a balanced life. Each point contains tools, practices, and measurable outcomes. The BCIO pattern of `Intervention_Content → works_through → Mechanism_of_Action → targets → Neurobiological_Process` provides the bridge between recovery practices and neuroscience.

**Values and principles layer.** Values-based recovery frameworks are modeled as: `Value → motivates → Goal → guides → Behavior_Plan → implements → Coping_Strategy`. The 2024 ADHD ontology by Alsaedi et al. defines 8 top-level classes (Subtypes, Symptoms, Behaviors, Diagnostic Criteria, Treatment, Risk Factors, Comorbidities, Patient Profile) with 13 relationships — a useful structural starting point.

**Program structure layer.** Steps/stages, milestones, community elements, sponsor/mentee relationships, meeting types, and literature references.

**Source provenance layer.** Each concept note links back to its source documents (academic papers, books) with extraction metadata, enabling the founder to trace every claim to its origin.

In Obsidian, each domain becomes a folder or tag namespace, each concept becomes a note with YAML frontmatter defining its type and properties, and relationships between concepts are expressed as `[[wikilinks]]` with typed Dataview inline fields like `parent:: [[Neuroscience]]` or `mechanism_of_action:: [[Dopamine Regulation]]`.

---

## Architecture 1: the weekend demo (complexity: minimal)

This architecture requires **no orchestration tools, no databases, and no server infrastructure**. It uses Claude directly as the ontology co-builder, outputting Obsidian-compatible markdown files that the founder manually places in a vault. Notion sync is handled by the "Share to NotionNext" Obsidian plugin.

**How it works.** The founder creates a LinkML-style YAML schema defining the ontology's entity types (Concept, Principle, Practice, Mechanism, Value, Source) and their properties. This schema is included in a system prompt to Claude. The founder then feeds source documents — academic papers on dopamine dysregulation in ADHD, chapters from books on recovery methodology, Dennett's intentional stance writings — into Claude conversations. Claude extracts structured concepts and outputs them as individual markdown files with YAML frontmatter and `[[wikilinks]]` to related concepts.

**The prompt pattern** follows the SPIRES approach from OntoGPT: provide the schema, provide the text, ask for extraction conforming to the schema. A single demonstration example in the prompt improves extraction quality by **2–3x** according to Polat et al. (2024). The key is decomposed extraction: first extract entity names and types, then relationships, then properties — rather than asking for everything at once.

**Example output for a single concept note:**

```yaml
---
type: mechanism
label: Dopamine Transporter Dysregulation
domain: neuroscience
superclass: "[[Dopamine System]]"
related: ["[[ADHD Pathophysiology]]", "[[Methylphenidate]]"]
mechanism_of_action: "[[Synaptic Dopamine Clearance]]"
confidence: high
source: "[[Volkow2009]]"
tags: [ontology/mechanism, domain/neuroscience]
---
# Dopamine Transporter Dysregulation

## Definition
Elevated DAT density in the striatum leads to excessive dopamine reuptake...

## Relationship to ADHD
parent:: [[ADHD Pathophysiology]]
affects:: [[Reward Processing]]
modulated_by:: [[Methylphenidate]]

## Evidence
Key finding from Volkow et al. (2009): PET imaging shows...
```

**Obsidian setup.** Install five plugins: **Dataview** (query structured metadata across all notes), **Breadcrumbs** (typed hierarchical relationships between notes), **Metadata Menu** (define FileClasses with property schemas for each entity type), **Templater** (auto-populate note templates when creating new concepts), and **ExcaliBrain** (interactive visual graph navigation showing typed relationships). The combination creates a functional lightweight ontology editor where the Graph View shows the full knowledge graph and Dataview queries can list all mechanisms, all values, all practices, or any cross-cutting view.

**Notion sync.** The "Share to NotionNext" plugin (v2.8.0, actively maintained) pushes individual notes to a Notion database with auto-sync on content changes. One-way push, low maintenance, reliable.

**Cost: ~$5–15 in Claude API credits for processing 50–100 source documents.** Zero infrastructure cost. **Time to demo: 1–2 days.** The founder spends most time curating and editing the AI-generated notes for alignment with their vision, which is exactly the intended workflow.

---

## Architecture 2: the automated pipeline (complexity: low-medium)

This architecture adds **n8n as a visual workflow orchestrator** to automate the document-to-ontology pipeline, eliminating the manual copy-paste step from Architecture 1. The founder drops PDFs into a watched folder; n8n processes them through Claude's API with structured output schemas; formatted markdown files appear in the Obsidian vault automatically.

**Pipeline flow:** PDF upload → n8n webhook trigger → PDF text extraction node → text chunking (recursive character splitter, ~1,024 tokens with 100-token overlap for academic papers) → Claude API node with ontology extraction prompt and JSON schema → markdown template engine → file write to Obsidian vault folder → optional Notion push via Notion API node.

**n8n provides the glue** with 422+ integrations, native LLM chain support, and a visual drag-and-drop interface. The critical bridge to Obsidian is the **Post Webhook Plugin** (by masterb12345), which sends full note content plus YAML frontmatter to any webhook endpoint and can receive AI-processed responses back into the vault. Self-hosted n8n is free; cloud starts at $20/month.

**Claude's structured outputs** (beta feature using `output_config.format` with JSON schema) guarantee schema-compliant extraction. The founder defines Pydantic-like models for each ontology entity type, and Claude's constrained decoding ensures every extraction conforms. Claude also handles PDFs natively up to ~32MB, eliminating the need for separate PDF parsing in many cases.

**Entity disambiguation** is the critical post-processing step most pipelines miss. After extracting entities from multiple documents, the pipeline needs a deduplication pass where Claude merges "DA," "dopamine," and "3,4-dihydroxyphenethylamine" into a single canonical entity. KGGen (from Stanford/U of Toronto, NeurIPS 2025) handles this automatically with its three-stage pipeline: generate triples → aggregate across sources → cluster entities. It achieves **66% accuracy on benchmarks versus 48% for Microsoft GraphRAG** and installs with `pip install kg-gen`.

**Notion integration** at this level uses n8n's native Notion node for programmatic page creation. The workflow parses each markdown note's frontmatter, maps properties to Notion database columns (concept type → Select property, related concepts → Relation property, domain → Multi-select), and creates structured database entries. Rate limit: **3 requests per second** to the Notion API, with n8n handling queuing and retry logic.

**Cost: ~$30–80/month** (n8n hosting $10–20, API costs $10–30 for ongoing document processing, Notion free tier). **Time to demo: 1–2 weeks.** The n8n workflow itself takes 2–4 hours to build; most time goes to prompt engineering and testing extraction quality.

---

## Architecture 3: the knowledge graph engine (complexity: medium)

This architecture adds a **proper graph database** (Neo4j or FalkorDB) as the ontology's canonical store, with Obsidian and Notion serving as human-facing views. The AI agent builds and maintains the graph; Obsidian provides the editing interface; Notion provides the curation dashboard.

**The fastest zero-code entry point** is the **Neo4j LLM Knowledge Graph Builder** (llm-graph-builder.neo4jlabs.com), a hosted web application where the founder uploads PDFs and the system automatically extracts entities and relationships into a Neo4j graph, complete with visual exploration in Neo4j Bloom and a RAG chatbot for querying the knowledge. Supports Claude, GPT-4o, Gemini, and Llama 3. Free tier available via Neo4j AuraDB. Time to first graph: **~5 minutes with zero code**.

For deeper integration, **FalkorDB's GraphRAG-SDK** generates ontologies from unstructured text with `Ontology.from_sources()` in approximately 10 lines of Python. It claims **90% hallucination reduction** versus traditional RAG and provides sub-50ms query latency — relevant if the founder wants to build a chatbot that answers questions about the recovery program's methodology.

**The Obsidian-graph sync** works through n8n or a Python script that exports graph nodes as markdown files with computed properties (e.g., centrality scores, cluster membership, relationship counts) embedded in YAML frontmatter. The **ODIN plugin** provides a more direct integration, connecting Obsidian to a Memgraph database backend and providing vault-wide knowledge graph visualization with LLM-powered Q&A.

**Microsoft GraphRAG** deserves mention for its unique capability: community detection using the Leiden algorithm. It automatically identifies clusters of related concepts and generates hierarchical summaries — essentially discovering the ontology's natural structure from the raw text. For processing an entire "knowledge canon" of ADHD and recovery literature, this community detection could reveal unexpected connections between dopamine science and recovery principles. However, indexing costs are **3–5x higher** than simpler approaches due to the multi-pass summarization.

**LightRAG** (from HKU) offers a compelling alternative: comparable accuracy to Microsoft GraphRAG at **10x fewer tokens**, with dual-level retrieval (local entity-focused + global theme-focused). For a cost-sensitive startup processing a growing corpus, LightRAG provides the best quality-per-dollar ratio.

**Notion at this level** becomes a proper relational dashboard. Databases for Concepts, Mechanisms, Practices, Values, and Sources are linked via Notion Relations, with Rollups computing aggregate views (e.g., "how many practices target dopamine regulation?" or "which values are most connected to which steps?"). The **Notion MCP server** (official, from Notion) enables Claude Desktop to read from and write to Notion directly — the founder could instruct Claude to "update the Notion ontology dashboard with the latest extracted concepts from this paper" in natural language.

**Cost: ~$100–200/month** (Neo4j AuraDB $65, n8n $20, API costs $30–50, Notion free). **Time to demo: 2–4 weeks.** Significant time goes to schema design, entity disambiguation tuning, and building the sync infrastructure.

---

## Architecture 4: the agentic system (complexity: high)

This architecture deploys an **autonomous AI agent** that continuously ingests documents, builds and refines the ontology, identifies gaps in coverage, and suggests new sources to the founder. It uses the Model Context Protocol (MCP) to bridge multiple tools, with Claude as the reasoning engine.

**MCP is the key enabling technology.** Released in 2025 and rapidly adopted, MCP gives AI assistants secure, standardized access to external tools. The architecture uses three MCP servers simultaneously: **Notion MCP** (official, one-click OAuth) for reading/writing the curation dashboard, **Graphthulhu MCP** (37 tools for Obsidian/Logseq knowledge graph access) for reading/writing the Obsidian vault, and a **filesystem MCP** for accessing source documents. Claude Desktop or a custom agent orchestrator chains these together.

**The agent workflow:** (1) Founder adds a new source document to the "canon" folder. (2) Agent detects the new file, reads it via filesystem MCP. (3) Agent extracts ontology entities using OntoGPT's SPIRES method with a LinkML schema defining the recovery program's entity types. (4) Agent checks extracted entities against the existing knowledge graph (via Graphthulhu MCP reading the Obsidian vault) for duplicates and conflicts. (5) Agent creates or updates Obsidian notes with proper frontmatter and wikilinks. (6) Agent updates the Notion dashboard with new entries and flags items for founder review. (7) Agent generates a "gap analysis" showing which areas of the ontology are underdeveloped and suggests specific papers or concepts to investigate.

**OntoGPT** is particularly powerful here because it grounds extracted entities against over 1,000 existing ontologies via OAK/Gilda. For ADHD-related extraction, it can automatically map concepts to SNOMED CT clinical terms, the Mental Functioning Ontology (MFO), or the ADHD ontology by Alsaedi et al. (2024). This grounding dramatically reduces hallucination and ensures the founder's ontology is interoperable with established biomedical knowledge.

**The Cannoli plugin** for Obsidian enables building no-code LLM scripts using the Canvas editor — the founder could create visual agent workflows directly within Obsidian, chaining extraction, validation, and note creation steps without writing code.

**Cost: ~$200–500/month** (higher API costs from continuous agent operation, multiple MCP servers, graph database). **Time to demo: 1–2 months.** This is a real product, not just a demo.

---

## Choosing the right Obsidian plugin stack

Regardless of architecture, the Obsidian setup is consistent. Five plugins form the core ontology editing environment, each solving a specific gap:

**Metadata Menu** defines FileClasses — essentially ontology class definitions with property constraints. A "Concept" FileClass might require fields for type (select: mechanism/value/practice/principle), domain (select: neuroscience/recovery/values), superclass (file link), and confidence (number). When the founder creates a new note of that type, structured editing UI enforces the schema. This is the closest Obsidian gets to OWL class restrictions without leaving markdown.

**Breadcrumbs** solves Obsidian's biggest ontology limitation: **untyped links**. Native `[[wikilinks]]` show that two concepts are connected but not how. Breadcrumbs adds directional, typed relationships via Dataview inline fields (`parent:: [[Animal]]`, `mechanism_of_action:: [[Dopamine Regulation]]`). Its V4 rewrite uses a Rust/WASM graph engine for high-performance traversal across large vaults.

**Dataview** turns the vault into a queryable database. DQL (Dataview Query Language) enables SQL-like queries across all notes: `TABLE superclass, domain FROM #ontology/class WHERE domain = "neuroscience" SORT file.name`. DataviewJS provides full JavaScript API for complex cross-cutting analyses.

**ExcaliBrain** generates interactive mind-map visualizations from the vault's link structure, distinguishing parent/child/friend relationships based on configured Dataview field mappings. Its dedicated "Ontology" settings section lets the founder configure which fields map to which relationship types — making the graph view semantically meaningful rather than just showing raw connections.

**Templater** auto-populates standardized note structures for each entity type. When the founder creates a new note in `/Ontology/Mechanisms/`, Templater automatically applies the mechanism template with the correct frontmatter schema, prompting for domain, superclass, and related concepts.

Two additional plugins add significant value: **Smart Connections** for AI-powered semantic note discovery (finding related concepts the founder didn't explicitly link), and **Simple Graph Builder** for LLM-powered entity extraction directly within Obsidian using Claude, GPT-4, or local models via Ollama.

---

## Practical prompt engineering for ontology extraction

The most effective prompt pattern for extracting ontology-aligned concepts from academic papers follows the **SPIRES method** developed by the Monarch Initiative, refined with findings from Polat et al. (2024):

**Step 1: Define the schema.** Provide a YAML or JSON schema describing the exact output structure — entity types, allowed relationship types, required properties. LinkML is the gold standard format for this, and OntoGPT uses it natively.

**Step 2: Provide one demonstration example.** A single domain-specific example of correct extraction improves quality 2–3x. Beyond one example, returns diminish sharply. The example should show a realistic input passage and the corresponding structured output.

**Step 3: Decompose the extraction.** Rather than asking the LLM to extract everything at once, run three sequential passes: (a) extract entity names and types, (b) extract relationships between identified entities, (c) extract properties and definitions. This "axiom-by-axiom" approach consistently outperforms direct all-at-once prompting.

**Step 4: Ground against existing knowledge.** After extraction, map entities to canonical forms using either OntoGPT's OAK integration (for biomedical concepts) or a simpler LLM-based deduplication pass. This prevents the ontology from accumulating duplicate concepts with different surface names.

For the ADHD recovery use case specifically, the founder should create separate extraction prompts for each domain — one tuned for neuroscience papers (extracting mechanisms, pathways, molecules), another for recovery methodology literature (extracting practices, principles, outcomes), and a third for values/philosophy sources (extracting concepts, stances, frameworks). Each prompt includes the relevant subset of the ontology schema and a domain-appropriate example.

---

## Head-to-head comparison of all four architectures

| Dimension | Arch 1: Weekend Demo | Arch 2: Automated Pipeline | Arch 3: Knowledge Graph Engine | Arch 4: Agentic System |
|---|---|---|---|---|
| **Time to working demo** | 1–2 days | 1–2 weeks | 2–4 weeks | 1–2 months |
| **Code required** | Zero | ~50 lines (n8n config) | ~100–200 lines Python | ~500+ lines or no-code via MCP |
| **Monthly cost** | $5–15 | $30–80 | $100–200 | $200–500 |
| **Document processing** | Manual paste into Claude | Automated via n8n | Automated + graph storage | Autonomous agent |
| **Ontology storage** | Obsidian vault only | Obsidian vault + Notion | Neo4j/FalkorDB + Obsidian + Notion | Multi-store with MCP bridge |
| **Notion integration** | Share to NotionNext plugin | n8n Notion node | Notion MCP + Relations | Full MCP agentic access |
| **Query capability** | Dataview in Obsidian | Dataview + Notion filters | Cypher/graph queries + RAG chatbot | Natural language over full graph |
| **Scalability** | ~200 concepts | ~1,000 concepts | ~10,000+ concepts | ~50,000+ concepts |
| **Best for** | Validating the concept | Investor demo / MVP | Beta product | Production system |

---

## Conclusion: start with Architecture 1, graduate to Architecture 2

The founder should **start with Architecture 1 this weekend** — create the ontology schema as a set of Obsidian templates, use Claude to extract concepts from the first 10–20 canonical sources, manually curate and edit the notes for alignment, and install ExcaliBrain to visualize the emerging knowledge graph. This produces a tangible, navigable, visually impressive artifact within 48 hours that demonstrates the ontology's structure and the AI-assisted curation workflow.

Once the schema stabilizes (typically after processing 30–50 sources), **graduate to Architecture 2** by adding n8n to automate ingestion. The key insight is that ontology schema design is inherently a human-judgment task — the AI extracts, the founder curates — and Architecture 1 maximizes the founder's direct engagement with schema decisions before automating them.

Three non-obvious findings from this research: First, **LinkML in YAML is the ideal intermediate format** — human-readable enough for manual editing, formal enough for OntoGPT and other tools to consume, and auto-convertible to OWL/JSON-LD if formal semantics are ever needed. Second, **the BCIO ontology from UCL is the best structural template** for a recovery program ontology, with its clean separation of intervention content, mechanisms of action, and behavioral outcomes mapping directly to the ADHD recovery use case. Third, **Notion MCP represents a paradigm shift** from sync-based integration to agent-based integration — rather than building fragile pipelines to keep Obsidian and Notion in sync, the founder can instruct Claude to read from one and write to the other in natural language, making Architecture 2's n8n bridge potentially unnecessary within 6–12 months as MCP tooling matures.