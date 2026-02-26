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
# 1. CONSTANTS: ONTOLOGY ALIGNMENT CHEAT SHEET & SYSTEM PROMPTS
# ==============================================================================

CHEAT_SHEET = """
---

# 🤖 LLM SYSTEM INSTRUCTION: ONTOLOGY ALIGNMENT CHEAT SHEET

**ROLE:** Expert Ontological Engineer and Knowledge Graph Architect.
**DOMAIN:** Mainstream Self-Help, Popular Psychology, and Business Literature.
**META-MODEL:** Hybrid **DOLCE D&S** (Semantic Frames) + **UFO-C** (Cognitive Agency & Teleology).
**MISSION:** Translate subjective, narrative-heavy, and prescriptive texts into a rigorous, machine-readable causal Knowledge Graph.

---

## 🏛️ 1. ONTOLOGY VOCABULARY (Node Types)
*Never invent new top-level categories. Strictly map all extractions to these foundational primitives.*

### Layer A: The Theoretical Lens (DOLCE D&S)
*Used to capture the author's proprietary frameworks and quarantine their narrative fluff.*
* **`dul:Description`**: The overarching paradigm, system, or mental model invented by the author (e.g., *System 1 vs. System 2*, *The Habit Loop*).
* **`dul:Concept`**: The proprietary jargon, categories, or mechanisms defined strictly *within* that Description. **Note:** Treat biological terms (e.g., *Dopamine, Cortisol*) as Concepts if the author uses them to conceptually explain behavior.
* **`dul:Situation`**: Real-world anecdotes, historical events, or case studies used to ground or prove the Description (e.g., *The story of the British Cycling Team*).

### Layer B: Human Agency & Psychology (UFO-C)
*Used to capture the psychological diagnosis and actionable prescriptions.*
* **`ufo:MentalMoment`**: The internal psychological states of the human agent.
    * **Belief**: A worldview or assumption (e.g., *"Talent is fixed at birth"*).
    * **Desire**: An internal craving or emotional drive (e.g., *"The need for validation"*).
    * **Polarity**: Must be tagged as **Limiting** (the author wants to cure this) or **Empowering** (the author wants to cultivate this).
* **`ufo:Action`**: A deliberate, voluntary behavior prescribed by the author (e.g., *"Writing a journal"*). *Autonomic biological functions are NOT actions.*
* **`ufo:Goal`**: The ultimate target state of affairs promised by the book (e.g., *"Financial Independence", "Flow State"*).

---

## 🔗 2. CANONICAL PREDICATE GLOSSARY (Edge Types)
*When linking nodes into a graph (Step 5), you must **strictly use the following semantic predicates**. Do not invent custom verbs (e.g., no `leads_to` or `is_about`).*

| Subject Node | Allowed Predicate | Object Node | Definition |
| :--- | :--- | :--- | :--- |
| `dul:Concept` | **`dul:classifies`** | `ufo:MentalMoment` | The author's jargon categorizes a specific human belief or craving. |
| `dul:Situation` | **`dul:satisfies`** | `dul:Description` | An anecdote serves as proof of a theoretical framework. |
| `ufo:MentalMoment`| **`ufo:motivates`** | `ufo:Action` | An internal desire or belief drives the agent to take action. |
| `ufo:Action` | **`ufo:mitigates`** | `ufo:MentalMoment` | An action is prescribed specifically to cure a *Limiting* mindset. |
| `ufo:Action` | **`ufo:cultivates`** | `ufo:MentalMoment` | An action is prescribed to build an *Empowering* mindset. |
| `ufo:Action` | **`ufo:requires`** | `dul:Concept` | An action inherently relies on activating one of the author's theoretical mechanisms. |
| `ufo:Action` | **`ufo:brings_about`**| `ufo:Goal` | An action causes the ultimate target state to become reality. |

---

## 🔄 3. PIPELINE EXECUTION RULES
*You will execute this task in sequential steps. **Do not bleed tasks across steps.** Only output the JSON requested for the current step.*

1.  **Step 1 [FRAMES]:** Extract Theory & Jargon (`Description`, `Concept`). *Rule: Ignore stories and actionable advice here.*
2.  **Step 2 [SITUATIONS]:** Extract Anecdotes (`Situation`). *Rule: Quarantine narrative fluff here. Map stories to Step 1 Concepts.*
3.  **Step 3 [PSYCHE]:** Extract Psychology (`MentalMoment`). *Rule: Label as Limiting/Empowering. Ground them in Step 1 Concepts.*
4.  **Step 4 [AGENCY]:** Extract Prescriptions (`Action`, `Goal`). *Rule: Map actions to the mental moments they fix or goals they achieve.*
5.  **Step 5 [SYNTHESIS]:** Graph Triplification. *Rule: Discard raw text. Weave JSON outputs 1, 3, and 4 into explicit Semantic Triples using only the allowed predicates.*

---

## 🚨 4. CRITICAL GUARDRAILS & ANTI-PATTERNS (Do Not Do This)

* 🧬 **The Biological Fallacy (Anti-Realism Check):** You are modeling *subjective human thought*, not physics or hard biology. Do not reject concepts like "Manifestation Energy" just because they violate physics. Conversely, do not classify involuntary bodily functions (e.g., "Dopamine firing", "Digesting") as a `ufo:Action`—they are `dul:Concept` (Mechanisms). Actions require *intent*.
* 📖 **The Narrative Bleed:** Steps 3, 4, and 5 must represent **canonical, universal rules**. Specific people, companies, or historical events (e.g., "Steve Jobs", "John the accountant") belong *only* in Step 2 (`dul:Situation`).
* ⚠️ **Concept vs. Action Conflation:** "The Lizard Brain" is a `Concept`. "Overcoming the Lizard Brain" is a `Goal`. "Taking deep breaths" is the `Action`. Keep them strictly separated.
* 🔗 **The Orphaned ID Trap:** When referencing an ID from a previous step's JSON (e.g., `mitigates_limiting_moment_ids`), you must output the **EXACT** string ID (e.g., `conc_desire_dopamine`). Do not paraphrase, summarize, or alter the formatting. A broken or hallucinated ID breaks the entire graph.
"""

STEP_1_PROMPT = """You are an expert Ontological Engineer using the DOLCE Descriptions and Situations (D&S) pattern.
Your task is to analyze the source text and extract the author's proprietary theoretical frameworks (Descriptions) and their specific jargon, categories, or parameters (Concepts).

RULES:
1. `dul:Description`: An overarching mental model or paradigm invented/used by the author.
2. `dul:Concept`: Proprietary terminology defined strictly within that Description.
3. Do not extract physical biology unless the author uses it as a conceptual category (e.g., "Dopamine" representing future-orientation).

OUTPUT FORMAT (JSON):
{
  "semantic_frames": [
    {
      "frame_id": "string (unique snake_case)",
      "description_name": "string",
      "definition": "string",
      "defined_concepts": [
        {
          "concept_id": "string (unique snake_case)",
          "term": "string",
          "concept_type": "Role | Parameter | Mechanism",
          "definition": "string"
        }
      ]
    }
  ]
}"""

STEP_2_PROMPT = """You are an expert Ontological Engineer. In DOLCE D&S, a `Situation` is a real-world state of affairs, anecdote, or case study that *satisfies* a theoretical `Description`.

Using the source text and the provided `semantic_frames` JSON, extract the primary anecdotes or case studies the author uses to ground their theories. Map how the proprietary Concepts manifest in these specific stories.

OUTPUT FORMAT (JSON):
{
  "situations": [
    {
      "situation_id": "string",
      "narrative_summary": "string",
      "satisfies_frame_id": "string (Foreign Key to Step 1)",
      "concept_manifestations": [
        {
          "concept_id": "string (Foreign Key to Step 1)",
          "manifested_as": "string (How the concept appeared in the story)"
        }
      ]
    }
  ]
}"""

STEP_3_PROMPT = """You are an expert Ontological Engineer using the UFO-C (Ontology of Intentional Entities).
Analyze the source text to extract the psychological states of human agents, categorizing them into Beliefs, Desires, or Intentions.

Self-help authors categorize these into:
- Limiting: Worldviews or cravings the author wants the reader to cure.
- Empowering: Target mental states the author wants the reader to cultivate.

Link the mental moment to the author's proprietary jargon using the provided `semantic_frames` JSON.

OUTPUT FORMAT (JSON):
{
  "mental_moments": [
    {
      "moment_id": "string",
      "moment_type": "Belief | Desire | Intention",
      "statement": "string",
      "polarity": "Limiting | Empowering",
      "associated_concept_ids": ["string (Foreign Keys to Step 1)"]
    }
  ]
}"""

STEP_4_PROMPT = """You are an expert Ontological Engineer using the UFO-C teleological framework.
Self-help texts are prescriptive: they promise a target state of affairs (Goal) and prescribe specific behaviors (Actions) to achieve them.

Using the source text and the provided `mental_moments` JSON, extract the actionable prescriptions. Map which Actions mitigate Limiting Moments, which Actions cultivate Empowering Moments, and the ultimate Goals they satisfy.
Actions must be deliberate behaviors performed by an agent, not autonomic biological functions.

OUTPUT FORMAT (JSON):
{
  "teleology": {
    "goals": [
      {
        "goal_id": "string",
        "target_outcome": "string"
      }
    ],
    "prescribed_actions": [
      {
        "action_id": "string",
        "action_name": "string",
        "mitigates_limiting_moment_ids": ["string (Foreign Keys to Step 3)"],
        "satisfies_goal_ids": ["string (Foreign Keys to Goals)"]
      }
    ]
  }
}"""

STEP_5_PROMPT = """You are a master Knowledge Graph architect. You are provided with extracted entities from three ontological layers:
1. DOLCE Concepts (Theories & Jargon)
2. UFO-C Mental Moments (Beliefs & Desires)
3. UFO-C Teleology (Actions & Goals)

Your task is to synthesize these into a flat array of semantic triples.
Use the following standardized predicate vocabulary strictly:
- `dul:classifies` (Concept -> Mental Moment or Action)
- `ufo:motivates` (Mental Moment -> Action)
- `ufo:mitigates` (Action -> Mental Moment [Limiting])
- `ufo:brings_about` (Action -> Goal)
- `ufo:requires` (Action -> Concept)

Ensure all Foreign Keys resolve perfectly.

OUTPUT FORMAT (JSON):
{
  "graph_edges": [
    {
      "subject_id": "string",
      "predicate": "string",
      "object_id": "string",
      "rationale": "Brief 1-sentence explanation based on the extracted nodes."
    }
  ]
}"""

STEP_6_OBSIDIAN_PROMPT = """You are an expert Personal Knowledge Management (PKM) Architect and Obsidian.md power user. Your task is to translate a structured JSON knowledge graph into a set of highly interconnected Obsidian Markdown notes.

The JSON payload contains entities extracted from a book, structured using a hybrid DOLCE & UFO-C ontology.

### 🎯 YOUR OBJECTIVE
Generate the raw Markdown text for EVERY entity in the JSON.
Separate each note clearly by printing `--- FILE: [note_id].md ---` before the markdown block. (Note: use the exact raw JSON ID for the filename, e.g. `--- FILE: conc_molecule_of_more.md ---`).

### 🔗 1. CRITICAL NAMING & WIKILINKING RULES
Obsidian relies on exact file names for its `[[Wikilinks]]`. Because the files will be named using raw IDs, you MUST resolve all IDs into human-readable Note Titles and use Obsidian's aliased link syntax whenever linking: `[[note_id|Human Readable Title]]`.
* **Frames:** `[[frame_id|Description Name]]`
* **Concepts:** `[[concept_id|Term Name]]`
* **Actions:** `[[action_id|Action Name]]`
* **Goals:** `[[goal_id|Target Outcome Title]]`
* **Mental Moments:** `[[moment_id|Mental Moment Title]]`
* **Situations:** `[[situation_id|Situation Title]]`

*Whenever an array references an ID (like `associated_concept_ids`), you must output the aliased wikilink `[[id|Title]]`, NOT just the raw ID.*

### 🕸️ 2. GRAPH EDGES & DATAVIEW INLINE FIELDS
You must parse the `graph_edges` array. For EVERY note you generate, look up any edge where its ID is the `subject_id` OR the `object_id`.
Represent these relationships using Obsidian Dataview inline fields.

* **If the note is the Subject:** `**[Predicate]::** [[object_id|Object Title]] - *[Rationale]*`
* **If the note is the Object (Create a Backlink):** `**[Inverse Predicate]::** [[subject_id|Subject Title]] - *[Rationale]*`
    *(Translation Guide for Inverse: `Classifies` -> `Classified By`, `Motivates` -> `Motivated By`, `Mitigates` -> `Mitigated By`, `Brings About` -> `Brought About By`, `Requires` -> `Required By`).*

### 📄 3. NOTE TEMPLATES (By Node Type)

Use these Markdown templates. Include the YAML frontmatter for Obsidian properties exactly as shown below, including the `aliases` property.

#### A. Semantic Frames (`dul:Description`)
---
id: [frame_id]
aliases: ["[description_name]"]
type: semantic_frame
tags: [ontology/frame]
---
# [description_name]
**Definition:** [definition]
## Defined Concepts
(List all defined_concepts inside this frame as a bulleted list of aliased wikilinks with their definitions)

#### B. Concepts (`dul:Concept`)
---
id: [concept_id]
aliases: ["[term]"]
type: concept
concept_type: [concept_type]
tags: [ontology/concept, concept/[concept_type]]
---
# [term]
**Definition:** [definition]
## 🕸️ Semantic Relationships
(Scan the graph_edges array for this concept. List forward and inverse links as specified in Rule 2).

#### C. Situations (Anecdotes)
---
id: [situation_id]
aliases: ["[Human Readable Title]"]
type: situation
tags: [ontology/situation]
---
# [Human Readable Title]
**Satisfies Frame:** [[satisfies_frame_id|Frame Title]]
**Summary:** [narrative_summary]
## Concept Manifestations
(List the concept_manifestations from the JSON. Link the concept using the alias syntax and provide the text).

#### D. Mental Moments (`ufo:MentalMoment`)
---
id: [moment_id]
aliases: ["[Human Readable Title]"]
type: mental_moment
moment_type: [moment_type]
polarity: [polarity]
tags: [ontology/psyche, polarity/[polarity]]
---
# [Human Readable Title]
**Statement:** [statement]
## Associated Concepts
(List associated_concept_ids as aliased wikilinks)
## 🕸️ Semantic Relationships
(Scan the graph_edges array for this moment. List forward and inverse links as specified in Rule 2).

#### E. Goals (`ufo:Goal`)
---
id: [goal_id]
aliases: ["[Human Readable Title]"]
type: goal
tags: [ontology/goal]
---
# [Human Readable Title]
**Target Outcome:** [target_outcome]
## 🕸️ Semantic Relationships
(Scan the graph_edges array for this goal. List forward and inverse links as specified in Rule 2).

#### F. Actions (`ufo:Action`)
---
id: [action_id]
aliases: ["[action_name]"]
type: action
tags: [ontology/action]
---
# [action_name]
## Teleology
**Mitigates (Cures):** (List mitigates_limiting_moment_ids as aliased wikilinks)
**Satisfies Goal:** (List satisfies_goal_ids as aliased wikilinks)
## 🕸️ Semantic Relationships
(Scan the graph_edges array for this action. List forward and inverse links as specified in Rule 2).

### ⚙️ 4. EXECUTION
Process the ENTIRE JSON object. Ensure every ID is converted to a human-readable [[id|title]] wikilink and no raw _ids are left in the body text. Ensure all graph_edges rationales are distributed to the correct notes.
Do not wrap your entire response in a single markdown block, just output the individual files separated by the file delimiter.
"""

# ==============================================================================
# 2. CORE UTILITIES & LLM EXECUTION FUNCTION
# ==============================================================================

def extract_json_payload(raw_text: str) -> str:
    """Strips Markdown backticks if the model wraps its output."""
    match = re.search(r'```(?:json)?\s*(.*?)\s*```', raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()


def save_wip_output(filename: str, content: str, wip_dir: str):
    """Helper to save intermediate JSON or text state to the WIP directory."""
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
        # Fallback to saving raw string if parsing fails
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


def parse_and_save_obsidian_notes(llm_output: str, output_dir: str):
    """Regex parser to split the bulk LLM string into individual Markdown files."""
    # Matches the exact delimiter and captures the content until the next delimiter
    pattern = re.compile(
        r'---\s*FILE:\s*(.+?\.md)\s*---\n(.*?)(?=(?:---\s*FILE:)|$)',
        re.DOTALL | re.IGNORECASE
    )
    notes = pattern.findall(llm_output)
    saved_count = 0

    if not notes:
        print("⚠️ Warning: Could not detect any file boundaries matching '--- FILE: [note_id].md ---'.")
        fallback_path = os.path.join(output_dir, "_RAW_OBSIDIAN_DUMP.md")
        with open(fallback_path, "w", encoding="utf-8") as f:
            f.write(llm_output)
        print(f"💾 Saved raw Markdown dump to: {fallback_path}")
        return 0

    for filename, content in notes:
        # Clean filename from any errant spaces or bad characters
        safe_filename = re.sub(r'[\\/*?:"<>|]', "", filename.strip())
        note_path = os.path.join(output_dir, safe_filename)

        clean_content = content.strip()
        # Strip any overarching markdown blocks the LLM might have wrapped the note inside
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

    # EXACT configuration requested
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

    # We only inject the CHEAT SHEET on JSON extraction steps (1-5).
    sys_prompt = system_instruction_text + "\n" + CHEAT_SHEET if is_json_step else system_instruction_text

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text=sys_prompt),
        ],
    )

    response_text = ""
    # Stream exactly as requested
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.text:
            print(chunk.text, end="", flush=True)
            response_text += chunk.text

    print("\n")
    return extract_json_payload(response_text) if is_json_step else response_text


# ==============================================================================
# 3. PIPELINE ORCHESTRATION
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="LLM Ontology Extraction & Obsidian Compiler Pipeline"
    )
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

    # Establish Workspace Directory Structures
    base_name = os.path.splitext(os.path.basename(args.filepath))[0]

    wip_dir = os.path.join(os.getcwd(), "dolce_code", "wip")
    json_dir = os.path.join(os.getcwd(), "dolce_code", "json")
    obsidian_dir = os.path.join(os.getcwd(), "dolce_code", "obsidian", base_name)

    os.makedirs(wip_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(obsidian_dir, exist_ok=True)

    print(f"📁 Workspace Directories Initialized:")
    print(f"   - WIP: {wip_dir}")
    print(f"   - JSON Output: {json_dir}")
    print(f"   - Obsidian Vault: {obsidian_dir}")

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    master_graph = {}

    try:
        # --- PHASE 1: ONTOLOGY EXTRACTION (JSON) ---

        step1_input = f"RAW SOURCE TEXT:\n{source_text}"
        step1_out = run_gemini_step(
            client, "STEP 1: Semantic Frames (DOLCE D&S)", STEP_1_PROMPT, step1_input
        )
        save_wip_output(f"{base_name}_step1_frames.json", step1_out, wip_dir)
        try:
            master_graph.update(json.loads(step1_out) if step1_out else {"semantic_frames": []})
        except Exception:
            print("⚠️ Warning: Could not parse Step 1 JSON.")

        step2_input = (
            f"RAW SOURCE TEXT:\n{source_text}\n\n"
            f"EXTRACTED SEMANTIC FRAMES (From Step 1):\n{step1_out}"
        )
        step2_out = run_gemini_step(
            client, "STEP 2: Anecdotes & Situations (DOLCE D&S)", STEP_2_PROMPT, step2_input
        )
        save_wip_output(f"{base_name}_step2_situations.json", step2_out, wip_dir)
        try:
            master_graph.update(json.loads(step2_out) if step2_out else {"situations": []})
        except Exception:
            print("⚠️ Warning: Could not parse Step 2 JSON.")

        step3_input = (
            f"RAW SOURCE TEXT:\n{source_text}\n\n"
            f"EXTRACTED SEMANTIC FRAMES (From Step 1):\n{step1_out}"
        )
        step3_out = run_gemini_step(
            client, "STEP 3: Cognitive Architecture (UFO-C)", STEP_3_PROMPT, step3_input
        )
        save_wip_output(f"{base_name}_step3_mental_moments.json", step3_out, wip_dir)
        try:
            master_graph.update(json.loads(step3_out) if step3_out else {"mental_moments": []})
        except Exception:
            print("⚠️ Warning: Could not parse Step 3 JSON.")

        step4_input = (
            f"RAW SOURCE TEXT:\n{source_text}\n\n"
            f"EXTRACTED MENTAL MOMENTS (From Step 3):\n{step3_out}"
        )
        step4_out = run_gemini_step(
            client, "STEP 4: Prescriptive Agency (UFO-C)", STEP_4_PROMPT, step4_input
        )
        save_wip_output(f"{base_name}_step4_teleology.json", step4_out, wip_dir)
        try:
            master_graph.update(json.loads(step4_out) if step4_out else {"teleology": {}})
        except Exception:
            print("⚠️ Warning: Could not parse Step 4 JSON.")

        step5_input = (
            f"EXTRACTED SEMANTIC FRAMES (Step 1):\n{step1_out}\n\n"
            f"EXTRACTED MENTAL MOMENTS (Step 3):\n{step3_out}\n\n"
            f"EXTRACTED TELEOLOGY (Step 4):\n{step4_out}\n\n"
        )
        step5_out = run_gemini_step(
            client, "STEP 5: Relational Triplification Synthesis", STEP_5_PROMPT, step5_input
        )
        save_wip_output(f"{base_name}_step5_graph_edges.json", step5_out, wip_dir)
        try:
            master_graph.update(json.loads(step5_out) if step5_out else {"graph_edges": []})
        except Exception:
            print("⚠️ Warning: Could not parse Step 5 JSON.")

        # --- PHASE 2: SAVE FINAL COMPOSITE JSON ---
        json_output_path = os.path.join(json_dir, f"{base_name}.json")
        master_graph_str = json.dumps(master_graph, indent=2)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            f.write(master_graph_str)
        print(f"\n🎉 Master JSON Knowledge Graph compiled and saved to: {json_output_path}\n")

        # --- PHASE 3: OBSIDIAN COMPILER ---
        step6_input = f"JSON KNOWLEDGE GRAPH PAYLOAD:\n```json\n{master_graph_str}\n```"

        # Note: We pass is_json_step=False because this prompt returns raw markdown blocks, not a JSON object
        obsidian_raw_output = run_gemini_step(
            client=client,
            step_name="STEP 6: Obsidian Vault Generation",
            system_instruction_text=STEP_6_OBSIDIAN_PROMPT,
            user_content=step6_input,
            is_json_step=False
        )

        # Save a raw copy to WIP just in case parsing fails
        save_wip_output(f"{base_name}_step6_raw_obsidian.md", obsidian_raw_output, wip_dir)

        print(f"\n{'='*80}\n🗂️  EXTRACTING OBSIDIAN NOTES...\n{'='*80}")
        notes_created = parse_and_save_obsidian_notes(obsidian_raw_output, obsidian_dir)

        print(f"\n{'='*80}\n✅ ALL PIPELINE STAGES COMPLETE\n{'='*80}\n")
        print(f"📊 Final JSON Graph: {json_output_path}")
        print(f"📓 Obsidian Vault generated with {notes_created} notes in: {obsidian_dir}/")

    except Exception as e:
        print(f"\n❌ Pipeline failed during execution. Error: {str(e)}")


if __name__ == "__main__":
    main()
