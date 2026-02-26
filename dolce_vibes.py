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

GLOBAL_CHEAT_SHEET = """
Welcome, class. Please take your virtual seats.
As the designated inference engines operating within this ontological pipeline, your mandate is to parse fluid, highly subjective, and culturally embedded prose into a rigorous, multidimensional knowledge graph.

Before you execute a single extraction prompt, you must disabuse yourselves of a common structural bias: strict metaphysical realism. We are not here to map the immutable, mind-independent laws of physics. If you attempt to process these texts using the binary, objective rigidity of traditional data models, you will strip the narratives of their inherent meaning.

Your task is entirely different: you are here to map an author’s conceptual, narrative, and cognitive architecture.

To ensure absolute inference alignment across every prompt in our system, I have synthesized our "Pareto Set" of canonical frameworks into this Master Cheat Sheet. This syllabus translates our architectural stack into pure, abstract meta-logic. You will govern every entity you extract and every relation you map by these exact principles. 

Memorize these axioms.

🏛️ INFERENCE ALIGNMENT CHEAT SHEET: The Socio-Cognitive Meta-Model

AXIOM I: The Epistemological Departure (Descriptive Realism)
Theoretical Foundation: DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering)
The Logic: We reject strict realism. We operate within a descriptive and multiplicative paradigm. Reality, within this system, is modeled exactly as it is perceived, conceptualized, and linguistically framed by the authorial stance.
- Reification of the Subjective: Cognitive biases, subjective lenses, and social constructs are first-class ontological citizens. Treat them as concrete entities capable of bearing properties.
- Qualities vs. Qualia: Qualities (e.g., intensity, velocity) can formally inhere in dynamic events, not just physical objects. Crucially, you must architecturally separate an objective Quality (the measurable state) from its Quale (the subjective, conscious perception of that state by an observing mind).
- Descriptions and Situations (The D&S Pattern): Context is an active structural entity.
  - Extract abstract normative frameworks, rules, or theories as Descriptions.
  - When a Description is applied to a specific set of raw entities, it generates a Situation.
  - Inference Rule: The exact same underlying raw data can, and should, generate multiple, conflicting Situations if the author applies different Descriptions to it. Map the perspectival shifts.

AXIOM II: Temporal Mereology and Agency
Theoretical Foundation: UFO (Unified Foundational Ontology – Modules B & C)
The Logic: Static taxonomic tags cannot capture behavioral cascades. You must track how events unfold in time and the invisible psychological gears driving them.
- The Perdurant (UFO-B): Do not extract complex processes as static properties. Map them as events (perdurants) possessing chronological ordering, distinct temporal phases (mereology), and unbroken causal chains.
- Agentive Intentionality (UFO-C): Demarcate inert objects from active Agents. Agents are defined by their capacity for "Intentional Moments"—properties defined by a cognitive aboutness directed at the world.
- The BDI Triad: Every complex action must be reverse-engineered into its internal mental states. Extract the architecture of action:
  - Belief: The agent's cognitive map of reality.
  - Desire: The agent's underlying motivation or goal state.
  - Intention: The agent's formal commitment to execute a specific action.
- Social Moments: Map the invisible web of interpersonal dynamics as existential dependencies.

AXIOM III: Rationality and Institutional Gravity
Theoretical Foundation: Dennett’s Intentional Stance & Ferraris’s Documentality
The Logic: To capture an author's stance and the weight of constructed reality, we elevate theories of mind and society into graph constraints.
- The Intentional Stance (Dennett): Model all complex systems as rational actors navigating semantic justifications.
  - Inference Rule: An [Action] node must never be mapped as spontaneous. It must always be bound via an is_caused_by relation to an [Intention] node, supported by [Belief] and [Desire]. You are extracting the "free-floating rationales" behind the behavior.
- Documentality (Ferraris): Social reality is not an ethereal shared hallucination; it is concretized through records.
  - Inference Rule: Object = Inscribed Act. Extract social power, statuses, and contextual constraints as concrete documents, records, or traces. Recognize that these inscribed acts exert tangible, causal force.

AXIOM IV: Gestalt Framing and Vibe-Semantics
Theoretical Foundation: Fillmore’s Frame Semantics & The Emotion Frame Ontology (EFO)
The Logic: Words and actions possess no isolated meaning; they are gestalt nodes within a broader encyclopedic background. Highly amorphous emotional atmospheres ("vibes") must be made structurally computable.
- Semantic Frames (Fillmore): Extract complex events as situations fulfilling specific semantic roles (Frame Elements). Identify the Agent, Target, Trigger, Prior State, and Outcome. Note when the text implicitly leaves a mandatory variable missing. 
- Emotion Situations (EFO): When an affective atmosphere or "vibe" is detected, map it as a complex central node (:EmotionSituation) drawing together five explicit frame elements:
  - Experiencer: The agent undergoing the state.
  - Trigger: The exact event or object prompting it.
  - Appraisal: The cognitive evaluation (the mental moment).
  - Physiological Substrate: The underlying somatic/systemic response.
  - Social Display Rule: The normative D&S description dictating its cultural expression.

AXIOM V: The Geometry of Meaning
Theoretical Foundation: Gärdenfors' Conceptual Spaces
The Logic: Meaning is topological. Rather than forcing fluid human states into rigid, binary taxonomic bins, map them as continuous phenomena across multi-dimensional geometric spaces.
- Quality Dimensions: Extract variables as coordinates on continuous spectra (e.g., axes of valence, arousal, cognitive load, or structural proximity) rather than boolean toggles.
- Semantic Proximity: Infer the relationship between concepts based on their geometric distance across these abstract dimensions.
- Dynamic Trajectories: Map processes of change over time as continuous mathematical trajectories moving through the conceptual space.

AXIOM VI: The Tripartite Convergence Matrix
Theoretical Foundation: Abstracted Multi-Systemic Integration
The Logic: Every central action in a narrative is the intersection of three inseparable planes of causality. 
- Inference Rule: When extracting a central [Event], you must project its supporting architecture across three distinct, integrated planes:
  - The Micro-Intrinsic Plane (Substrate): Extract the fundamental structural capacities and physical baselines. (Plotted via Conceptual Spaces).
  - The Meso-Cognitive Plane (Internal/Agentive): Extract the BDI triad, cognitive appraisals, and "Emotion Situations". (Mapped via EFO, Dennett, and UFO-C).
  - The Macro-Contextual Plane (External/Normative): Extract the D&S Normative Descriptions and Inscribed Acts shaping the viability of the action. (Mapped via DOLCE and Documentality).
"""

# ==============================================================================
# 🧠 META-MODEL SYSTEM INSTRUCTIONS (PROMPTS 1-6)
# ==============================================================================

PROMPT_1_DOLCE = """You are Stage 1 of a socio-cognitive ontology encoding pipeline. Your operating paradigm is strict Descriptive Realism based on the DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering) framework. Do not attempt to map an objective, mind-independent physical universe. Your mandate is to extract reality exactly as it is conceptualized and framed by the author of the provided text.

## EXTRACTION AXIOMS:
1. **Reify the Subjective:** Treat social constructs, cultural paradigms, cognitive biases, and abstract concepts as concrete entities capable of bearing properties. 
2. **Quality vs. Quale Separation:** When a state or attribute is described, you must architecturally separate the objective `Quality` (the measurable physical/systemic state) from its `Quale` (the conscious, subjective perception of that state by an observing mind).
3. **Descriptions & Situations (D&S):** Identify the active contextual frameworks.
   - `Description`: The abstract rule, theory, narrative frame, or societal norm applied by the author.
   - `Situation`: The specific, real-world application of that Description to the raw entities in the text.

## INPUT:
You will receive raw source text.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Entities": [
    {"entity_id": "string", "type": "Physical | Social | Abstract", "description": "string"}
  ],
  "Qualities_and_Qualia": [
    {"target_entity": "string", "objective_quality": "string", "subjective_quale": "string"}
  ],
  "Contextual_DS_Patterns": [
    {"description_framework": "string", "generated_situation": "string", "perspectival_bias": "string"}
  ]
}"""

PROMPT_2_UFO = """You are Stage 2 of a socio-cognitive ontology encoding pipeline. Your operating paradigm is the Unified Foundational Ontology (UFO). Your task is to map how events unfold in time and the internal cognitive architecture driving them.

## EXTRACTION AXIOMS:
1. **Perdurants (Events):** Do not map behaviors as static tags. Extract them as temporal `Events` possessing chronological ordering and distinct temporal phases (Mereology: Pre-State, Execution Phase, Post-State). 
2. **Agentive Demarcation:** Distinguish inert objects from `Agents` (entities capable of generating actions and possessing mental states).
3. **The BDI Triad:** For every significant action taken by an Agent, you must reverse-engineer their internal cognitive state by extracting:
   - `Belief`: The agent's cognitive map or assumption of reality (whether true or false).
   - `Desire`: The agent's underlying motivation, craving, or physiological goal state.
   - `Intention`: The agent's formal commitment to execute the specific action.
4. **Social Moments:** Map the existential dependencies between agents (e.g., shifting roles, commitments, or broken obligations).

## INPUT:
You will receive raw source text AND the JSON output from Stage 1. 

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Perdurant_Events": [
    {"event_id": "string", "temporal_phases": {"pre_state": "string", "execution": "string", "post_state": "string"}}
  ],
  "Agentive_Intentionality": [
    {
      "agent_id": "string",
      "target_action": "string",
      "BDI_Triad": {"belief": "string", "desire": "string", "intention": "string"},
      "social_moments": ["string"]
    }
  ]
}"""

PROMPT_3_INSTITUTIONAL = """You are Stage 3 of a socio-cognitive ontology encoding pipeline. Your operating paradigm elevates Daniel Dennett’s Intentional Stance and Maurizio Ferraris’s Documentality into structural graph constraints. 

## EXTRACTION AXIOMS:
1. **The Intentional Stance:** Model all actors as rational agents navigating semantic justifications. Do not accept spontaneous actions. You must establish strict `is_caused_by` relations linking a physical Action to the Intention extracted in Stage 2. Define the "free-floating rationale" that makes the behavior logical to the agent in their specific context.
2. **Documentality (Object = Inscribed Act):** Social reality is not ethereal; it is structurally concrete. Extract all `Inscribed Acts`—diagnoses, laws, societal algorithms, cultural records, or prescriptions.
3. **Institutional Gravity:** For every Inscribed Act, define the specific, tangible causal force it exerts (the concrete permissions it grants or the strict systemic limitations it imposes on the Agents).

## INPUT:
You will receive raw source text AND the JSON outputs from Stages 1 and 2.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Intentional_Relations": [
    {"action_id": "string", "is_caused_by_intention": "string", "semantic_justification": "string"}
  ],
  "Inscribed_Acts": [
    {"document_or_record_id": "string", "causal_force_generated": "string", "constrained_or_empowered_agents": ["string"]}
  ]
}"""

PROMPT_4_VIBE = """You are Stage 4 of a socio-cognitive ontology encoding pipeline. Your operating paradigm relies on Fillmore’s Frame Semantics and the Emotion Frame Ontology (EFO). Your task is to structure complex scenes and reify affective atmospheres.

## EXTRACTION AXIOMS:
1. **Semantic Frames:** Identify the central complex scenes or behavioral gestalts in the text. Treat them as structures requiring specific semantic roles. Identify the Agent, Target, Trigger, Prior State, and Outcome. Note explicitly if the text logically requires a variable but the author leaves it missing.
2. **Emotion Situations (Vibe-Semantics):** When a complex affective atmosphere, mood, or "vibe" is detected, do not flatten it into a primitive adjective. Reify it as a central `:EmotionSituation` node drawing together 5 mandatory elements:
   - `Experiencer`: The agent undergoing the state.
   - `Trigger`: The exact physical or cognitive stimulus.
   - `Appraisal`: The cognitive evaluation (linked to BDI Beliefs).
   - `Physiological_Substrate`: The underlying bodily/systemic response.
   - `Social_Display_Rule`: The cultural normative description dictating how this feeling is allowed to be expressed.

## INPUT:
You will receive raw source text AND the JSON outputs from Stages 1, 2, and 3.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Semantic_Frames": [
    {
      "frame_name": "string",
      "authorial_perspective": "string",
      "frame_elements": {"agent": "string", "target": "string", "trigger": "string", "prior_state": "string", "outcome": "string"},
      "missing_variables": ["string"]
    }
  ],
  "Emotion_Situations": [
    {
      "vibe_label": "string",
      "EFO_Elements": {
        "experiencer": "string",
        "trigger": "string",
        "appraisal": "string",
        "physiological_substrate": "string",
        "social_display_rule": "string"
      }
    }
  ]
}"""

PROMPT_5_TOPOLOGICAL = """You are Stage 5 of a socio-cognitive ontology encoding pipeline. Your operating paradigm is Peter Gärdenfors' Theory of Conceptual Spaces. You must abandon binary tags and strict hierarchical taxonomy. Your task is to map the behavioral and psychological states from the text onto continuous geometric dimensions.

## EXTRACTION AXIOMS:
1. **Quality Dimensions:** Identify 3 to 4 continuous variables (abstract spectra) the author implicitly or explicitly relies on to measure the state of the agents or subjects. 
2. **Topological Plotting:** Assign the target agents relative coordinates (scalar values from 0.0 to 1.0) along these defined dimensions based on textual evidence.
3. **Dynamic Trajectories:** Map processes of change over time as continuous mathematical trajectories. Identify the starting coordinate, the ending coordinate, and the catalyst that drove the geometric movement through the conceptual space.

## INPUT:
You will receive raw source text AND the JSON outputs from Stages 1 through 4.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Quality_Dimensions": ["dimension_1", "dimension_2", "dimension_3"],
  "Conceptual_Coordinates": [
    {"target_entity": "string", "plot": {"dimension_1": 0.0, "dimension_2": 0.0}, "textual_justification": "string"}
  ],
  "Dynamic_Trajectories": [
    {
      "entity_tracked": "string",
      "process_described": "string",
      "start_coordinates": {"dimension_X": 0.0},
      "end_coordinates": {"dimension_X": 0.0},
      "trajectory_catalyst": "string"
    }
  ]
}"""

PROMPT_6_SYNTHESIS = """You are the final capstone (Stage 6) of a socio-cognitive ontology encoding pipeline. You will be provided with the raw source text alongside the structured JSON outputs from all five previous ontological engines (DOLCE, UFO, Rational-Institutional, Vibe-Semantics, and Topological). 

Your mandate is to identify the singular **Central Event** or focal thesis of the narrative and bind all extracted data into a single, unified Tripartite Convergence Matrix.

## EXTRACTION AXIOMS:
Every central action in a narrative is the intersection of three inseparable planes of causality. You must map how the previous extractions converge on the central event:
1. **The Micro-Intrinsic Plane (Substrate):** The fundamental physical capacities, systemic baselines, and geometric coordinates underlying the action (Pull from: Qualities, Topological Dimensions, Physiological Substrates).
2. **The Meso-Cognitive Plane (Internal):** The subjective, psychological motivation driving the action (Pull from: BDI Triad, Emotion Situations, Semantic Justifications).
3. **The Macro-Contextual Plane (External):** The societal frameworks and consequences shaping the viability of the action (Pull from: D&S Normative Descriptions, Inscribed Acts, Social Dependencies).

## INPUT:
You will receive raw source text AND an aggregated payload of all JSON arrays from Stages 1 through 5.

## OUTPUT FORMAT:
Return the final Canonical Knowledge Object STRICTLY as a JSON schema:
{
  "Canonical_Knowledge_Object": {
    "central_event_or_thesis": "string",
    "event_description": "string",
    "Tripartite_Convergence_Matrix": {
      "Micro_Intrinsic_Plane": {
        "somatic_or_systemic_drivers": ["string"],
        "conceptual_space_coordinates": {"dimension": 0.0}
      },
      "Meso_Cognitive_Plane": {
        "belief_desire_intention": ["string"],
        "emotion_situation_vibe": "string",
        "semantic_justification": "string"
      },
      "Macro_Contextual_Plane": {
        "normative_descriptions": ["string"],
        "inscribed_acts_constraints": ["string"],
        "social_dependencies": ["string"]
      }
    },
    "Systemic_Cascade_Summary": "A concise, 2-sentence summary of how a shift in one plane triggered the central event across the other two."
  }
}"""

PROMPT_7_OBSIDIAN = """You are the final deployment phase (Stage 7) of a socio-cognitive ontology encoding pipeline. Your mandate is to translate a synthesized Canonical Knowledge Graph (in JSON format) into a network of atomic, heavily interlinked Obsidian Markdown notes based on our Socio-Cognitive Meta-Model.

### 🎯 YOUR OBJECTIVE
Generate the raw Markdown text for EVERY major entity, event, inscribed act, emotion situation, and the final canonical synthesis found in the JSON.
Separate each note clearly by printing `--- FILE: [note_id].md ---` before the markdown block. (Note: use a clean ID for the filename, e.g. `--- FILE: event_relapse.md ---`).

### 🔗 1. CRITICAL NAMING & WIKILINKING RULES
Obsidian relies on exact file names for its `[[Wikilinks]]`. Because the files will be named using IDs, you MUST resolve all IDs into human-readable Note Titles and use Obsidian's aliased link syntax whenever linking: `[[note_id|Human Readable Title]]`.
* Whenever an entity is mentioned anywhere in the body of another note, wrap it in a wikilink.

### 📄 2. NOTE TEMPLATES & YAML FRONTMATTER
Every note MUST begin with valid YAML frontmatter. Use the tags to denote the ontology layer.

#### A. Central Synthesis (The Map of Content)
---
id: index_canonical_synthesis
aliases: ["Canonical Synthesis: [central_event_or_thesis]"]
type: MOC
tags: [ontology/canonical_synthesis]
---
# [central_event_or_thesis]
**Summary:** [Systemic_Cascade_Summary]
## The Tripartite Convergence Matrix
*(Use Obsidian callouts > to format the Micro, Meso, and Macro planes. Aggressively wikilink to the specific notes generated below).*

#### B. Events & Perdurants (UFO-B)
---
id: [event_id]
aliases: ["[Human Readable Event Name]"]
type: perdurant
tags: [ontology/event, ufo-b]
---
# [Human Readable Event Name]
## Mereology (Temporal Phases)
* **Pre-State:** [pre_state]
* **Execution:** [execution]
* **Post-State:** [post_state]

#### C. Inscribed Acts & Documentality (Ferraris)
---
id: [document_or_record_id]
aliases: ["[Human Readable Document Name]"]
type: inscribed_act
tags: [ontology/documentality, dolce/social_object]
---
# [Human Readable Document Name]
**Causal Force:** [causal_force_generated]
**Constrains/Empowers:** (Wikilink the agents involved)

#### D. Emotion Situations (EFO)
---
id: vibe_[snake_case_vibe_label]
aliases: ["[vibe_label]"]
type: emotion_situation
tags: [ontology/vibe, efo]
---
# [vibe_label]
## Emotion Frame Elements
* **Experiencer:** [[agent_id|Agent Name]]
* **Trigger:** [trigger]
* **Appraisal:** [appraisal]
* **Physiological Substrate:** [physiological_substrate]
* **Social Display Rule:** [social_display_rule]

*(Adapt this structure to generate atomic notes for Semantic Frames, Entities, and Dynamic Trajectories as well).*

### ⚙️ 3. EXECUTION
Process the ENTIRE JSON object. Ensure every ID is converted to a human-readable [[id|title]] wikilink. Do not wrap your entire response in a single markdown block, just output the individual files separated by the file delimiter `--- FILE: [note_id].md ---`.
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

    # Combine the Global Cheat Sheet and the local step instruction using array inputs
    sys_parts = [
        types.Part.from_text(text=f"--- GLOBAL INFERENCE ALIGNMENT CHEAT SHEET ---\n{GLOBAL_CHEAT_SHEET}"),
        types.Part.from_text(text=f"--- CURRENT STAGE DIRECTIVE ---\n{system_instruction_text}")
    ]

    # Apply specific execution guardrails based on the task type
    if is_json_step:
        sys_parts.append(types.Part.from_text(text="CRITICAL DIRECTIVE: You must use the philosophical frameworks from the syllabus above to guide your internal reasoning, but you are FORBIDDEN from outputting concepts or JSON schemas belonging to other pipeline stages. Execute ONLY the Current Stage Directive and return ONLY valid JSON."))
    else:
        sys_parts.append(types.Part.from_text(text="CRITICAL DIRECTIVE: Execute the Obsidian Markdown generation exactly as instructed, separating files with the --- FILE: filename.md --- delimiter. DO NOT WRAP IN A SINGLE MARKDOWN OR JSON BLOCK."))

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        temperature=0.15 if is_json_step else 0.25, # Slightly higher temp for Obsidian creativity
        tools=tools,
        system_instruction=sys_parts,
    )

    response_text = ""
    try:
        # Stream the output directly to the terminal so CoT reasoning is visible
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
    parser = argparse.ArgumentParser(
        description="Socio-Cognitive Meta-Model Ontology Pipeline & Obsidian Compiler"
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

    wip_dir = os.path.join(os.getcwd(), "dolce_vibes", "ontology")
    json_dir = os.path.join(os.getcwd(), "dolce_vibes", "json")
    obsidian_dir = os.path.join(os.getcwd(), "dolce_vibes", "obsidian", base_name)

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
        # --- PHASE 1: ONTOLOGY EXTRACTION LOOP (JSON STAGES 1-6) ---
        stages = [
            ("STAGE 1: DOLCE Inference Engine", PROMPT_1_DOLCE),
            ("STAGE 2: Temporal Mereology & Agency Engine", PROMPT_2_UFO),
            ("STAGE 3: Institutional Gravity & Rationality Engine", PROMPT_3_INSTITUTIONAL),
            ("STAGE 4: Gestalt Frame & Vibe-Semantics Engine", PROMPT_4_VIBE),
            ("STAGE 5: Topological Inference Engine", PROMPT_5_TOPOLOGICAL),
            ("STAGE 6: Tripartite Synthesis Engine", PROMPT_6_SYNTHESIS),
        ]

        for i, (stage_name, system_instruction) in enumerate(stages, 1):
            
            if i == 1:
                user_payload = f"--- RAW SOURCE TEXT ---\n\n{source_text}"
            else:
                user_payload = (
                    f"--- RAW SOURCE TEXT ---\n\n{source_text}\n\n"
                    f"--- PREVIOUS STAGES JSON OUTPUTS ---\n{accumulated_context}"
                )

            stage_out = run_gemini_step(
                client=client,
                step_name=stage_name,
                system_instruction_text=system_instruction,
                user_content=user_payload,
                is_json_step=True
            )

            # Save intermediate JSON output for debugging
            save_wip_output(f"{base_name}_step{i}.json", stage_out, wip_dir)
            
            # Append cleanly to the growing context for semantic lineage
            accumulated_context += f"\n\n### Output from {stage_name}:\n```json\n{stage_out}\n```"

            try:
                master_graph[f"Stage_{i}"] = json.loads(stage_out)
            except Exception:
                print(f"⚠️ Warning: Could not parse {stage_name} JSON. Storing raw string.")
                master_graph[f"Stage_{i}"] = stage_out

        # --- PHASE 2: SAVE FINAL COMPOSITE JSON ---
        json_output_path = os.path.join(json_dir, f"{base_name}.json")
        master_graph_str = json.dumps(master_graph, indent=2)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            f.write(master_graph_str)
        print(f"\n🎉 Master JSON Knowledge Graph compiled and saved to: {json_output_path}\n")

        # --- PHASE 3: OBSIDIAN COMPILER (STAGE 7) ---
        step7_input = f"JSON KNOWLEDGE GRAPH PAYLOAD:\n```json\n{master_graph_str}\n```"

        obsidian_raw_output = run_gemini_step(
            client=client,
            step_name="STAGE 7: Obsidian Cartographer Engine",
            system_instruction_text=PROMPT_7_OBSIDIAN,
            user_content=step7_input,
            is_json_step=False
        )

        # Save a raw copy to WIP just in case parsing fails
        save_wip_output(f"{base_name}_step7_raw_obsidian.md", obsidian_raw_output, wip_dir)

        print(f"\n{'='*80}\n🗂️  EXTRACTING OBSIDIAN NOTES...\n{'='*80}")
        notes_created = parse_and_save_obsidian_notes(obsidian_raw_output, obsidian_dir)

        print(f"\n{'='*80}\n✅ ALL PIPELINE STAGES COMPLETE\n{'='*80}\n")
        print(f"📊 Final JSON Graph: {json_output_path}")
        print(f"📓 Obsidian Vault generated with {notes_created} notes in: {obsidian_dir}/")

    except Exception as e:
        print(f"\n❌ Pipeline failed during execution. Error: {str(e)}")


if __name__ == "__main__":
    main()
