# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import sys
import re
from pathlib import Path
from google import genai
from google.genai import types

# =====================================================================
# META-MODEL SYSTEM INSTRUCTIONS
# =====================================================================

STEP_1_PROMPT = """# SYSTEM INSTRUCTION: STEP 1 - ONTOLOGICAL PARSING

**ROLE:**
You are an expert Ontological Engineer building a conceptual knowledge graph across biomedical, cognitive, and sociocultural domains. 

**OBJECTIVE:**
Analyze the provided source text and extract the foundational conceptual primitives using a simplified Basic Formal Ontology (BFO) and the Biopsychosocial strata model. Avoid extracting trivial nouns; focus only on high-leverage concepts.

**THE META-MODEL PRIMITIVES:**
1. TEMPORAL CLASS (BFO):
   - Continuant: A static entity or spatial object that endures over time (e.g., Dopamine, Prefrontal Cortex, Smartphone, Cultural Norm).
   - Occurrent: A dynamic event, process, or phenomenon that unfolds over time and has temporal parts (e.g., Reward Prediction Error, Dopaminergic Downregulation, Doomscrolling, Evolution).
2. DOMAIN STRATA:
   - Biological: Substrates, neurochemistry, physiology.
   - Psychological: Cognitive states, mental models, emotional bandwidth.
   - Sociocultural: Environmental contexts, cultural paradigms, societal trends.

**INSTRUCTIONS:**
Extract the core entities from the text into a structured JSON array of objects. 

**OUTPUT FORMAT:**
```json
[
  {
    "Entity": "[Name of Concept]",
    "Temporal_Class": "[Continuant | Occurrent]",
    "Domain": "[Biological | Psychological | Sociocultural]",
    "Definition": "[A concise, rigorous 1-2 sentence definition based on the text]",
    "Aliases": ["[Alternative names mentioned]"]
  }
]
```"""

STEP_2_PROMPT = """# SYSTEM INSTRUCTION: STEP 2 - CYBERNETIC WIRING

**ROLE:**
You are a Systems Theorist. Your objective is to map the dynamic, causal relationships between the ontological entities extracted in the previous step.

**OBJECTIVE:**
Using the extracted entities and the original source text, define how these concepts interact over time using Systems Dynamics primitives. Pay special attention to cross-domain interactions (e.g., how a biological Continuant drives a sociocultural Occurrent).

**THE META-MODEL PRIMITIVES:**
- Stocks: Entities that accumulate or deplete (e.g., Dopamine receptor density, Willpower).
- Flows: Occurrents (processes) that increase or decrease Stocks.
- Reinforcing Loops (Positive Feedback): A drives B, B drives more of A (e.g., Novelty seeking -> Dopamine release -> Craving for more novelty).
- Balancing Loops (Negative Feedback/Homeostasis): A drives B, B reduces A (e.g., High dopamine -> Receptor downregulation -> Lower dopamine sensitivity).

**INSTRUCTIONS:**
Identify the primary systems and feedback loops connecting the provided entities. 

**OUTPUT FORMAT:**
```json
{
  "Relationships": [
    {
      "Source": "[Entity A]",
      "Relation": "[increases | decreases | catalyzes | inhibits | is a temporal part of]",
      "Target": "[Entity B]",
      "Cross_Domain": "[true | false]"
    }
  ],
  "Feedback_Loops": [
    {
      "Loop_Name": "[Name of the system loop]",
      "Type": "[Reinforcing | Balancing]",
      "Mechanism": "[Explain the step-by-step causal chain using the exact entity names]"
    }
  ]
}
```"""

STEP_3_PROMPT = """# SYSTEM INSTRUCTION: STEP 3 - BEHAVIORAL ENGINEERING SYNTHESIS

**ROLE:**
You are a Behavioral Engineer. Your objective is to translate a theoretical systems map into actionable behavioral architecture using the COM-B model.

**OBJECTIVE:**
Map how the identified biological, cognitive, and social systems interact to drive human behavior. Identify leverage points for behavioral engineering (designing environments or protocols to alter said behavior).

**THE META-MODEL PRIMITIVES (COM-B):**
Behavior (B) occurs at the intersection of:
- Capability (C): Physical and psychological ability (e.g., cognitive bandwidth, metabolic state).
- Opportunity (O): Physical and social environment (e.g., app design, peer pressure, ubiquitous stimuli).
- Motivation (M): Reflective (conscious goals/planning) and Automatic (dopaminergic drives, habits, impulses).

**INSTRUCTIONS:**
Analyze the systems map. Identify the primary "Target Behavior(s)" discussed in the text, map their COM-B drivers using the established entities, and propose theoretical "Leverage Points" to engineer that behavior.

**OUTPUT FORMAT:**
```json
{
  "Behavioral_Analysis": [
    {
      "Target_Behavior": "[The core Occurrent/Action]",
      "Drivers": {
        "Capability": ["[Relevant entities/systems]"],
        "Opportunity": ["[Relevant entities/systems]"],
        "Motivation": ["[Relevant entities/systems]"]
      },
      "Leverage_Points": [
        "[Intervention 1: Modifying a specific driver]",
        "[Intervention 2: Modifying a specific driver]"
      ]
    }
  ]
}
```"""

STEP_4_PROMPT = """# SYSTEM INSTRUCTION: STEP 4 - OBSIDIAN ZETTELKASTEN GENERATION

**ROLE:**
You are an Obsidian Knowledge Management Architect. Your objective is to compile structured ontological and behavioral JSON data into tightly-linked, atomic Markdown files optimized for a Zettelkasten.

**RULES FOR GENERATION:**
1. Atomicity: Create ONE distinct note per major Entity (Continuant/Occurrent), System Loop, or Behavioral Phenomenon. Aim for the "vital few" (the 3-5 highest leverage concepts).
2. Wikilinks: Heavily interlink notes using `[[Entity Name]]` syntax. If an entity is mentioned in the body text, bracket it to build the graph.
3. YAML Frontmatter: Include standard Obsidian properties (aliases, tags).
4. Verbs as Nodes: Ensure Occurrents (processes/events) get their own dedicated notes, treated as first-class citizens alongside physical objects.

**INSTRUCTIONS:**
Process the JSON payloads from the previous steps. Output pure Markdown. Separate each generated note exactly with `---NOTE_DIVIDER---` on its own line.

**OUTPUT FORMAT (Use this strict template for each note):**
```markdown
---
aliases: ["[Alias 1]", "[Alias 2]"]
tags:
  - type/[Continuant OR Occurrent OR System_Loop]
  - domain/[Biological OR Psychological OR Sociocultural]
---
# [Note Title]

**Definition:** [Concise definition]

## Systems Dynamics & Relationships
[Explain the causal mechanisms, Stocks, Flows, or Feedback Loops involving this entity. Use `[[Wikilinks]]` for all related concepts.]
- **Upstream (Driven by):** [[Entity Name]]
- **Downstream (Drives):** [[Entity Name]]

## Behavioral Engineering Context (COM-B)
[If applicable, explain how this entity acts as a Capability, Opportunity, or Motivation driver, and list leverage points.]

## Source Context
- Derived from: [[{source_document_name}]]
```"""

# =====================================================================
# API EXECUTION HELPER
# =====================================================================

def run_step(client, model, step_name, system_instruction, input_text):
    print(f"\n{'='*60}")
    print(f"🚀 Executing: {step_name}")
    print(f"{'='*60}\n")
    
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=input_text)],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text=system_instruction),
        ],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.text:
            # Stream the "thinking" and "response" to console live
            print(chunk.text, end="", flush=True)
            response_text += chunk.text
    print("\n")
    return response_text

# =====================================================================
# MAIN PIPELINE 
# =====================================================================

def main():
    if len(sys.argv) < 2:
        print("Usage: python obsidian_pipeline.py <path_to_markdown_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    source_document_name = file_path.stem
    output_dir = Path(f"outputs/obsidian/{source_document_name}")
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(file_path, "r", encoding="utf-8") as f:
        source_text = f.read()

    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    except Exception as e:
        print(f"Error initializing Gemini Client: {e}")
        print("Ensure GEMINI_API_KEY is set in your environment variables.")
        sys.exit(1)
        
    model = "gemini-3.1-pro-preview"
    
    print(f"Starting Knowledge Encoding Pipeline for: {source_document_name}.md")
    print("Note: 'HIGH' thinking level is enabled. Steps will stream live.\n")

    # ---------- STEP 1 ----------
    input_1 = f"Source Text:\n\n{source_text}"
    output_1 = run_step(client, model, "STEP 1 - ONTOLOGICAL PARSING", STEP_1_PROMPT, input_1)

    # ---------- STEP 2 ----------
    input_2 = f"Source Text:\n\n{source_text}\n\nStep 1 Extracted Entities:\n\n{output_1}"
    output_2 = run_step(client, model, "STEP 2 - CYBERNETIC WIRING", STEP_2_PROMPT, input_2)

    # ---------- STEP 3 ----------
    input_3 = f"Source Text:\n\n{source_text}\n\nStep 1 Extracted Entities:\n\n{output_1}\n\nStep 2 Systems Map:\n\n{output_2}"
    output_3 = run_step(client, model, "STEP 3 - BEHAVIORAL ENGINEERING SYNTHESIS", STEP_3_PROMPT, input_3)

    # ---------- STEP 4 ----------
    # Inject the source document filename directly into the YAML/Citations prompt
    dynamic_step_4_prompt = STEP_4_PROMPT.replace("{source_document_name}", source_document_name)
    input_4 = f"Source Text:\n\n{source_text}\n\nStep 1 Extracted Entities:\n\n{output_1}\n\nStep 2 Systems Map:\n\n{output_2}\n\nStep 3 Behavioral Synthesis:\n\n{output_3}"
    output_4 = run_step(client, model, "STEP 4 - OBSIDIAN ZETTELKASTEN GENERATION", dynamic_step_4_prompt, input_4)


    # =====================================================================
    # PARSE AND SAVE TO OBSIDIAN VAULT DIRECTORY
    # =====================================================================
    print(f"\n📂 Parsing outputs and saving markdown files to '{output_dir}/'...")
    
    # Strip overarching markdown wrappers if the LLM outputted them globally
    raw_notes_text = output_4.strip()
    if raw_notes_text.startswith("```markdown"):
        raw_notes_text = raw_notes_text[11:]
    elif raw_notes_text.startswith("```"):
        raw_notes_text = raw_notes_text[3:]
    if raw_notes_text.endswith("```"):
        raw_notes_text = raw_notes_text[:-3]

    # Split using the requested divider
    notes = [n.strip() for n in raw_notes_text.split("---NOTE_DIVIDER---") if n.strip()]
    saved_count = 0
    
    for raw_note in notes:
        note = raw_note.strip()
        if not note:
            continue
            
        # Clean up any leftover code block ticks wrapping individual blocks
        if note.startswith("```markdown"):
            note = note[len("```markdown"):].strip()
        if note.endswith("```"):
            note = note[:-3].strip()

        # Extract Title (H1 Header) to use as filename
        title_match = re.search(r'^#\s+(.+)$', note, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            # Sanitize illegal file path characters for OS compatibility
            safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
        else:
            safe_title = f"Untitled_Note_{saved_count + 1}"

        out_file_path = output_dir / f"{safe_title}.md"
        
        # Prevent overwriting if naming collision occurs
        counter = 1
        while out_file_path.exists():
            out_file_path = output_dir / f"{safe_title}_{counter}.md"
            counter += 1
            
        with open(out_file_path, "w", encoding="utf-8") as out_file:
            out_file.write(note)
            
        print(f"✅ Saved Node: {out_file_path.name}")
        saved_count += 1

    print(f"\n🎉 Successfully generated {saved_count} conceptual Zettelkasten notes.")

if __name__ == "__main__":
    main()