# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a knowledge extraction and ontology engineering pipeline for converting academic PDFs and domain literature into structured knowledge graphs. The system uses LLM-assisted extraction to transform unstructured text into interconnected Obsidian vault notes using formal ontology frameworks (BFO, DOLCE, UFO-C).

## Core Architecture

### Three-Stage Pipeline

1. **PDF Processing** (`pdf_parser.py`, `main.py`)
   - Extracts text from PDFs using PyMuPDF with TOC-aware header detection
   - Applies CropBox logic to remove headers/footers
   - Outputs clean hierarchical Markdown with header shifting (Level 1 → H2, Level 2 → H3)
   - Optional RAG chunking using LangChain's `MarkdownHeaderTextSplitter`

2. **Ontology Extraction** (BFO/DOLCE/UFO scripts in `docs/ontology-engineering/`)
   - Multi-step LLM prompting using Google Gemini API
   - Extracts domain concepts into formal ontological primitives
   - Frameworks supported:
     - **BFO** (Basic Formal Ontology): Continuants vs Occurrents, biopsychosocial strata
     - **DOLCE D&S**: Semantic frames (Descriptions, Concepts, Situations)
     - **UFO-C**: Cognitive agency (Mental Moments, Actions, Goals, COM-B model)

3. **Obsidian Vault Generation** (`obsidian_pipeline.py`, `dolce_code.py`)
   - Converts structured JSON to atomic, interlinked Markdown notes
   - Uses YAML frontmatter with Obsidian properties (aliases, tags, types)
   - Generates `[[wikilinks]]` with aliased syntax for graph navigation
   - Outputs to `PJS4Z/bfo/` or `PJS4Z/dolce/` subdirectories

### Key Workflow Scripts

- **`main.py`**: CLI for PDF-to-Markdown conversion (single file or batch)
- **`dolce_vita.py`**: Orchestrator that runs BFO extraction on all files in `source/inputs/`
- **`obsidian_pipeline.py`**: 4-step BFO extraction pipeline with Zettelkasten output
- **`dolce_code.py`**: 6-step DOLCE/UFO-C extraction with graph triplification

## Common Commands

### Environment Setup
```bash
# Install dependencies using uv
uv sync

# Set required API keys
export GEMINI_API_KEY="your_key_here"
```

### PDF Processing
```bash
# Convert single PDF to Markdown
python main.py -f path/to/document.pdf

# Batch process directory of PDFs
python main.py -d source/pdf-parse -o source/pdf2markdown

# Include RAG chunking demonstration
python main.py -f document.pdf --chunk

# Adjust margin cropping (default 8%)
python main.py -f document.pdf --top-margin 0.10 --bottom-margin 0.10
```

### Ontology Extraction

```bash
# Run BFO extraction on single document
python obsidian_pipeline.py path/to/document.md

# Run DOLCE extraction on single document
python dolce_code.py path/to/document.md

# Batch process all files in source/inputs/
python dolce_vita.py
```

### Output Locations

- **Markdown PDFs**: `source/pdf2markdown/`
- **BFO Obsidian notes**: `PJS4Z/bfo/{document_name}/`
- **DOLCE Obsidian notes**: `PJS4Z/dolce/{document_name}/`
- **JSON intermediates**: `outputs/dolce/{document_name}/json/`

## Ontology Framework Details

### BFO Pipeline (obsidian_pipeline.py)

**4-step extraction:**
1. **Ontological Parsing**: Extract Continuants (enduring entities) and Occurrents (processes) with biopsychosocial domain classification
2. **Cybernetic Wiring**: Map stocks, flows, and feedback loops (reinforcing/balancing)
3. **Behavioral Engineering**: Apply COM-B model (Capability/Opportunity/Motivation) to identify behavioral leverage points
4. **Zettelkasten Generation**: Create atomic Obsidian notes with heavy interlinking

### DOLCE Pipeline (dolce_code.py)

**6-step extraction:**
1. **Semantic Frames**: Extract Descriptions (theoretical frameworks) and Concepts (proprietary jargon)
2. **Situations**: Map anecdotes/case studies that satisfy theoretical frames
3. **Mental Moments**: Extract Beliefs/Desires/Intentions with Limiting/Empowering polarity
4. **Teleology**: Extract Actions and Goals with causal relationships
5. **Graph Triplification**: Create semantic triples with standardized predicates (classifies, motivates, mitigates, brings_about, requires)
6. **Obsidian Vault Generation**: Convert JSON graph to Markdown with Dataview inline fields for relationships

### Gemini API Configuration

All extraction scripts use:
- Model: `gemini-3.1-pro-preview`
- Thinking level: `HIGH` (extended reasoning mode)
- Streaming enabled for live progress
- Google Search tool enabled

## Important Implementation Details

### PDF Parser Strategy

The `SOTADocumentParser` uses a TOC-first injection approach:
- Extracts internal PDF bookmarks as ground truth taxonomy
- Matches text blocks to TOC entries using fuzzy matching
- Deterministic failsafe inserts missed headers at page boundaries
- Watermark filtering (e.g., removes "OceanofPDF.com")

### Ontology Extraction Anti-Patterns

**Do not:**
- Conflate biological mechanisms (Concepts) with intentional Actions
- Include specific people/companies in universal rules (belong in Situations only)
- Use custom predicates in graph edges (stick to canonical vocabulary)
- Hallucinate entity IDs when creating relationships
- Extract trivial nouns (focus on high-leverage concepts only)

### Obsidian Wikilink Format

Generated notes use aliased wikilinks to resolve raw IDs:
```markdown
[[concept_id|Human Readable Title]]
```

This allows filenames to use machine-readable IDs while displaying clean titles in the graph view.

## Development Notes

- **Python Version**: Requires Python >=3.13
- **Primary Dependencies**: google-genai, pymupdf, pydantic, langchain-text-splitters, ontogpt
- **Environment Variables**: `GEMINI_API_KEY` must be set for LLM extraction
- **Output Format**: All generated notes use YAML frontmatter with Obsidian properties
