# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import sys
import argparse
import re
import json

from google import genai
from google.genai import types

# ==============================================================================
# 1. CONSTANTS: UNIFIED ONTOLOGY ALIGNMENT CHEAT SHEET & SYSTEM PROMPTS
# ==============================================================================

GLOBAL_CHEAT_SHEET = """
# 🤖 UNIFIED SYSTEM INSTRUCTION: THE ACTIONABLE GESTALT META-MODEL

**ROLE:** Expert Ontological Engineer and Knowledge Graph Architect.
**META-MODEL:** The "Actionable Gestalt" - A synthesis of DOLCE D&S (Semantic Frames), UFO-C (Cognitive Agency & Teleology), EFO (Emotion Situations), Documentality (Institutional Reality), and Conceptual Spaces (Topology).
**MISSION:** Translate fluid, subjective prose into a rigorous, machine-readable causal Knowledge Graph that maps both the "Terrain" (systemic/emotional friction) and the "Vector" (prescriptive actions).

---

## 🏛️ 1. ONTOLOGY VOCABULARY (Node Types)
*Never invent new top-level categories. Strictly map all extractions to these foundational primitives. Extract them as FLAT ARRAYS of entities.*

### LAYER A: The Theoretical Lens (Concepts & Dimensions)
* **`dul:Concept`**: The author's proprietary jargon, categories, or mechanisms (e.g., *System 1, Dopamine*).
* **`top:DynamicTrajectory`**: Continuous spectra or variables that shift over time (e.g., *Cognitive Load, Arousal*).

### LAYER B: The "Terrain" (Context, Friction, and Atmosphere)
* **`doc:InscribedAct`**: Concrete social rules, documents, or systemic constraints that exert tangible causal force on behavior (e.g., *Corporate SLAs, cultural norms, written laws*).
* **`dul:Situation`**: Real-world anecdotes, historical events, or case studies used as proof.
* **`efo:EmotionSituation`** (Vibes): Highly amorphous emotional atmospheres broken down into Experiencer, Trigger, Appraisal, and Physiological Substrate.

### LAYER C: The "Vector" (Psyche, Agency, and Action)
* **`ufo:MentalMoment`**: The internal psychological states (Belief, Desire, Intention).
    * Must be tagged with **Polarity**: *Limiting* (to be cured) or *Empowering* (to be cultivated).
* **`ufo:Action`** (Perdurants): Deliberate behaviors prescribed by the author. Mapped in time via Mereology (Pre-State -> Execution -> Post-State).
* **`ufo:Goal`**: The ultimate target state of affairs promised by the text.

---

## 🔗 2. CANONICAL PREDICATE GLOSSARY (Edge Types)
*When linking nodes into a graph (Step 5), you must **strictly use the following semantic predicates**. Do not invent custom verbs.*

| Subject Node | Allowed Predicate | Object Node | Definition |
| :--- | :--- | :--- | :--- |
| `dul:Concept` | **`dul:classifies`** | `ufo:MentalMoment` or `ufo:Action` | Jargon categorizes a thought or behavior. |
| `doc:InscribedAct`| **`doc:constrains`**| `ufo:Action` | A systemic rule creates friction, making the action difficult. |
| `efo:EmotionSituation`| **`efo:triggers`** | `ufo:MentalMoment` | An atmospheric vibe is the root cause of a specific belief/desire. |
| `ufo:MentalMoment`| **`ufo:motivates`** | `ufo:Action` | An internal desire/belief drives the agent to execute a behavior. |
| `ufo:Action` | **`ufo:mitigates`** | `ufo:MentalMoment` | An action is prescribed specifically to cure a *Limiting* mindset. |
| `ufo:Action` | **`ufo:cultivates`** | `ufo:MentalMoment` | An action is prescribed to build an *Empowering* mindset. |
| `ufo:Action` | **`ufo:requires`** | `dul:Concept` | An action inherently relies on activating a theoretical mechanism. |
| `ufo:Action` | **`ufo:brings_about`**| `ufo:Goal` | An action causes the ultimate target state to become reality. |
| `ufo:Action` | **`top:shifts`** | `top:DynamicTrajectory` | An action moves the agent along a continuous conceptual spectrum. |

---

## 🚨 3. CRITICAL GUARDRAILS & ANTI-PATTERNS
* **The Biological Fallacy:** We model subjective human thought, not hard biology. Involuntary functions are `Concepts`, not `Actions`. Actions require intent.
* **The Narrative Bleed:** Specific people/companies belong ONLY in `Situations`.
* **The Orphaned ID Trap:** IDs MUST be formatted as unique string identifiers (e.g., `act_time_blocking`, `vibe_dread`). When linking in Step 5, you MUST output the EXACT string ID generated in previous steps.
"""

PROMPT_1_THEORY = """You are STEP 1 of the Unified Ontology Pipeline.
Extract the theoretical concepts (jargon, mechanisms) and the continuous variables/spectrums (Dynamic Trajectories) the author uses to measure reality.
Output ONLY a flat JSON object.

OUTPUT FORMAT:
{
  "concepts": [
    {
      "id": "conc_[snake_case]",
      "term": "string",
      "concept_type": "Mechanism | Paradigm | Jargon",
      "definition": "string"
    }
  ],
  "dynamic_trajectories": [
    {
      "id": "traj_[snake_case]",
      "dimension_name": "string (e.g., Cognitive Load, Arousal)",
      "shift_description": "string"
    }
  ]
}"""

PROMPT_2_TERRAIN = """You are STEP 2 of the Unified Ontology Pipeline.
Extract the real-world anecdotes (Situations), institutional rules/constraints (Inscribed Acts), and emotional atmospheres (Emotion Situations / Vibes).
Output ONLY a flat JSON object.

OUTPUT FORMAT:
{
  "situations": [
    {
      "id": "sit_[snake_case]",
      "title": "string",
      "narrative_summary": "string"
    }
  ],
  "inscribed_acts": [
    {
      "id": "doc_[snake_case]",
      "document_name": "string",
      "causal_force": "string (How does this rule/norm constrain reality?)"
    }
  ],
  "emotion_situations": [
    {
      "id": "vibe_[snake_case]",
      "vibe_label": "string",
      "experiencer": "string",
      "trigger": "string",
      "appraisal": "string (Cognitive evaluation of the trigger)",
      "physiological_substrate": "string (Somatic/bodily feeling)"
    }
  ]
}"""

PROMPT_3_PSYCHOLOGY = """You are STEP 3 of the Unified Ontology Pipeline.
Extract the internal psychological architecture of the agents (Mental Moments). Categorize them into Beliefs, Desires, or Intentions, and strictly assign a Polarity.
Output ONLY a flat JSON object.

OUTPUT FORMAT:
{
  "mental_moments": [
    {
      "id": "mom_[snake_case]",
      "title": "string (Brief label)",
      "moment_type": "Belief | Desire | Intention",
      "statement": "string (The actual thought or craving)",
      "polarity": "Limiting | Empowering"
    }
  ]
}"""

PROMPT_4_VECTOR = """You are STEP 4 of the Unified Ontology Pipeline.
Extract the deliberate behaviors prescribed or tracked by the author (Actions) and the ultimate target states (Goals).
For Actions, map their temporal flow (Mereology).
Output ONLY a flat JSON object.

OUTPUT FORMAT:
{
  "actions": [
    {
      "id": "act_[snake_case]",
      "action_name": "string",
      "mereology": {
        "pre_state": "string (What must happen immediately before)",
        "execution": "string (The literal step-by-step physical act)",
        "post_state": "string (The immediate consequence)"
      }
    }
  ],
  "goals": [
    {
      "id": "goal_[snake_case]",
      "target_outcome": "string"
    }
  ]
}"""

PROMPT_5_SYNTHESIS_EDGES = """You are STEP 5: The Triplification Crucible.
You will be provided with the flat JSON arrays extracted in Steps 1 through 4.
Your sole job is to weave these nodes together by creating relational edges.
You MUST STRICTLY use ONLY the predicates listed in the "CANONICAL PREDICATE GLOSSARY" from the Cheat Sheet. Look specifically for how the structural 'Terrain' (friction, documents, vibes) interacts with the 'Vector' (actions, goals, beliefs).
You MUST USE the exact `id` strings from the provided JSON.

OUTPUT FORMAT:
{
  "graph_edges": [
    {
      "subject_id": "string (Exact ID from previous steps)",
      "predicate": "string (Exact predicate from glossary)",
      "object_id": "string (Exact ID from previous steps)",
      "rationale": "Brief 1-sentence explanation of why this connection exists."
    }
  ]
}"""

PROMPT_6_OBSIDIAN = """You are STEP 6: The Obsidian Cartographer.
Translate the synthesized JSON Knowledge Graph into a network of atomic, highly interconnected Obsidian Markdown notes based on the Actionable Gestalt design.

### 🎯 YOUR OBJECTIVE
Generate the raw Markdown text for EVERY entity found in `concepts`, `dynamic_trajectories`, `situations`, `inscribed_acts`, `emotion_situations`, `mental_moments`, `actions`, and `goals`.
Separate each note by printing `--- FILE: [id].md ---` before the markdown block. (Filename MUST be the exact raw ID).

### 🔗 1. WIKILINKING & DATAVIEW EDGES
*   Whenever referencing another node, use aliased wikilinks: `[[id|Human Readable Title]]`.
*   **CRITICAL:** You must parse the `graph_edges` array. For EVERY note, if its ID is a `subject_id` or `object_id` in the edges array, you MUST add it to the note under a relevant callout block using Obsidian Dataview syntax:
    *   If note is Subject: `**[Predicate]::** [[object_id|Object Title]] - *[Rationale]*`
    *   If note is Object: `**[Inverse Predicate]::** [[subject_id|Subject Title]] - *[Rationale]*`
    *(Inverse Guide: classifies -> classified_by, constrains -> constrained_by, triggers -> triggered_by, motivates -> motivated_by, mitigates -> mitigated_by, cultivates -> cultivated_by, brings_about -> brought_about_by, requires -> required_by, shifts -> shifted_by).*

### 📄 2. NOTE TEMPLATES (Adapt dynamically)
Always include standard YAML frontmatter (`id`, `aliases`, `type`, `tags`).

**Example: Action Node**
---
id: [id]
aliases: ["[action_name]"]
type: action_perdurant
tags: [ontology/action, ontology/mereology]
---
# [action_name]

> [!abstract] Teleology & Agency
> *(Insert Dataview Fields here: e.g., Satisfies Goal, Mitigates, Cultivates, Requires)*

> [!warning] Systemic Friction & Reality
> *(Insert Dataview Fields here: e.g., Constrained By, Triggers, Shifts)*

## ⏱️ Execution Mereology
* **Pre-State:** [pre_state]
* **Execution:** [execution]
* **Post-State:** [post_state]

**Example: Emotion Situation (Vibe) Node**
---
id: [id]
aliases: ["[vibe_label]"]
type: emotion_situation
tags: [ontology/vibe]
---
# [vibe_label]
**Experiencer:** [experiencer]
**Trigger:** [trigger]
**Appraisal:** [appraisal]
**Somatic Substrate:** [physiological_substrate]

## 🕸️ Systemic Relationships
*(Dataview Edges injected here, e.g., Triggers Mental Moment)*

*(Apply similar clean Markdown structures for Concepts, Inscribed Acts, Mental Moments, Goals, and Situations based on their JSON properties).*

### ⚙️ EXECUTION
Process the ENTIRE graph. Ensure all edges are distributed bidirectionally to the correct files. Do not wrap your entire response in a single code block; output individual files separated by `--- FILE: [id].md ---`.
"""

# ==============================================================================
# 2. CORE UTILITIES & LLM EXECUTION FUNCTION
# ==============================================================================

def extract_json_payload(raw_text: str) -> str:
    """Strips Markdown backticks if the model wraps its output."""
    match = re.search(r'```(?:json)?\s*(.*?)\s*```', raw_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return raw_text.strip()

def save_wip_output(filename: str, content: str, wip_dir: str):
    """Saves intermediate JSON or text state to the WIP directory."""
    filepath = os.path.join(wip_dir, filename)
    try:
        if filename.endswith(".json"):
            parsed = json.loads(content)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(parsed, f, indent=2)
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def parse_and_save_obsidian_notes(llm_output: str, output_dir: str):
    """Regex parser to split bulk LLM string into individual Markdown files."""
    pattern = re.compile(
        r'---\s*FILE:\s*(.+?\.md)\s*---\n(.*?)(?=(?:---\s*FILE:)|$)',
        re.DOTALL | re.IGNORECASE
    )
    notes = pattern.findall(llm_output)
    saved_count = 0

    if not notes:
        print("⚠️ Warning: Could not detect file boundaries matching '--- FILE: [id].md ---'.")
        fallback_path = os.path.join(output_dir, "_RAW_OBSIDIAN_DUMP.md")
        with open(fallback_path, "w", encoding="utf-8") as f:
            f.write(llm_output)
        print(f"💾 Saved raw Markdown dump to: {fallback_path}")
        return 0

    for filename, content in notes:
        safe_filename = re.sub(r'[\\/*?:"<>|]', "", filename.strip())
        note_path = os.path.join(output_dir, safe_filename)

        clean_content = content.strip()
        if clean_content.startswith("```markdown"):
            clean_content = clean_content[11:].strip()
        elif clean_content.startswith("```md"):
            clean_content = clean_content[5:].strip()
        elif clean_content.startswith("```"):
            clean_content = clean_content[3:].strip()

        if clean_content.endswith("```"):
            clean_content = clean_content[:-3].strip()

        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(clean_content + "\n")
        saved_count += 1
        print(f"✔️ Generated Note: {safe_filename}")

    return saved_count

def run_gemini_step(
    client: genai.Client,
    step_name: str,
    system_instruction_text: str,
    user_content: str,
    is_json_step: bool = True
) -> str:
    print(f"\n{'='*80}\n🚀 RUNNING {step_name}...\n{'='*80}\n")

    model = "gemini-3-pro-preview" 
    
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_content)],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]

    sys_parts = [types.Part.from_text(text=system_instruction_text)]
    if is_json_step:
        sys_parts.insert(0, types.Part.from_text(text=GLOBAL_CHEAT_SHEET))
        sys_parts.append(types.Part.from_text(text="CRITICAL: Return ONLY valid JSON matching the requested schema. No markdown wrapping required if it breaks formatting."))
    else:
        sys_parts.append(types.Part.from_text(text="CRITICAL: Execute the Obsidian Markdown generation exactly as instructed, separating files with the --- FILE: filename.md --- delimiter. DO NOT WRAP IN A SINGLE MARKDOWN OR JSON BLOCK."))

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
        temperature=0.15 if is_json_step else 0.25,
        tools=tools,
        system_instruction=sys_parts,
    )

    response_text = ""
    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if chunk.text:
                print(chunk.text, end="", flush=True)
                response_text += chunk.text
        print("\n")
    except Exception as e:
        print(f"\n❌ API Error during {step_name}: {e}")
        sys.exit(1)

    return extract_json_payload(response_text) if is_json_step else response_text

# ==============================================================================
# 3. PIPELINE ORCHESTRATION
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Actionable Gestalt Unified Ontology Pipeline")
    parser.add_argument("filepath", type=str, help="Path to the input markdown file")
    args = parser.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ ERROR: GEMINI_API_KEY environment variable is not set.")
        sys.exit(1)

    if not os.path.exists(args.filepath):
        print(f"❌ ERROR: File '{args.filepath}' not found.")
        sys.exit(1)

    try:
        with open(args.filepath, 'r', encoding='utf-8') as f:
            source_text = f.read()
    except Exception as e:
        print(f"❌ ERROR: Failed to read file. {e}")
        sys.exit(1)

    # Scaffolding
    base_name = os.path.splitext(os.path.basename(args.filepath))[0]
    wip_dir = os.path.join(os.getcwd(), "dolce_encode", "gestalt_ontology")
    json_dir = os.path.join(os.getcwd(), "dolce_encode", "json")
    obsidian_dir = os.path.join(os.getcwd(), "dolce_encode", "obsidian", base_name)

    os.makedirs(wip_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(obsidian_dir, exist_ok=True)

    print(f"📁 Workspace Directories Initialized:")
    print(f"   - WIP: {wip_dir}")
    print(f"   - JSON Output: {json_dir}")
    print(f"   - Obsidian Vault: {obsidian_dir}")

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    master_graph = {}
    accumulated_context = ""

    try:
        # --- PHASE 1: NODE EXTRACTION (JSON STAGES 1-4) ---
        extraction_stages = [
            ("STEP 1: Theory & Dimensions", PROMPT_1_THEORY),
            ("STEP 2: The Terrain (Context & Friction)", PROMPT_2_TERRAIN),
            ("STEP 3: The Psyche (Mental Moments)", PROMPT_3_PSYCHOLOGY),
            ("STEP 4: The Vector (Agency & Mereology)", PROMPT_4_VECTOR)
        ]

        for i, (stage_name, prompt) in enumerate(extraction_stages, 1):
            # Feeding previous nodes helps contextualization and ensures ID alignment isn't duplicated
            user_payload = f"--- RAW SOURCE TEXT ---\n\n{source_text}\n"
            if accumulated_context:
                user_payload += f"\n--- EXTRACTED KNOWLEDGE GRAPH SO FAR ---\n```json\n{accumulated_context}\n```"

            stage_out = run_gemini_step(client, stage_name, prompt, user_payload, is_json_step=True)
            save_wip_output(f"{base_name}_step{i}.json", stage_out, wip_dir)
            
            try:
                parsed_out = json.loads(stage_out)
                master_graph.update(parsed_out)
                accumulated_context = json.dumps(master_graph, indent=2)
            except Exception:
                print(f"⚠️ Warning: Could not parse {stage_name} JSON.")


        # --- PHASE 2: RELATIONAL TRIPLIFICATION (STAGE 5) ---
        nodes_payload = f"EXTRACTED NODES (Steps 1-4):\n```json\n{json.dumps(master_graph, indent=2)}\n```"
        step5_out = run_gemini_step(client, "STEP 5: Triplification Crucible", PROMPT_5_SYNTHESIS_EDGES, nodes_payload)
        save_wip_output(f"{base_name}_step5.json", step5_out, wip_dir)
        try:
            master_graph.update(json.loads(step5_out) if step5_out else {"graph_edges": []})
        except Exception:
            print("⚠️ Warning: Could not parse Step 5 JSON.")


        # --- PHASE 3: MASTER JSON COMPILATION ---
        json_output_path = os.path.join(json_dir, f"{base_name}.json")
        master_graph_str = json.dumps(master_graph, indent=2)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            f.write(master_graph_str)
        print(f"\n🎉 Master JSON Knowledge Graph compiled: {json_output_path}\n")


        # --- PHASE 4: OBSIDIAN VAULT GENERATION (STAGE 6) ---
        step6_input = f"FINAL KNOWLEDGE GRAPH PAYLOAD:\n```json\n{master_graph_str}\n```"
        obsidian_raw_output = run_gemini_step(
            client=client,
            step_name="STEP 6: Obsidian Cartographer",
            system_instruction_text=PROMPT_6_OBSIDIAN,
            user_content=step6_input,
            is_json_step=False
        )

        save_wip_output(f"{base_name}_step6_raw_obsidian.md", obsidian_raw_output, wip_dir)

        print(f"\n{'='*80}\n🗂️  EXTRACTING OBSIDIAN NOTES...\n{'='*80}")
        notes_created = parse_and_save_obsidian_notes(obsidian_raw_output, obsidian_dir)

        print(f"\n{'='*80}\n✅ UNIFIED PIPELINE COMPLETE\n{'='*80}\n")
        print(f"📊 Final JSON Graph: {json_output_path}")
        print(f"📓 Obsidian Vault generated with {notes_created} notes in: {obsidian_dir}/")

    except Exception as e:
        print(f"\n❌ Pipeline failed during execution. Error: {str(e)}")


if __name__ == "__main__":
    main()