#!/usr/bin/env python3
import os
import sys
import json
import re
import argparse
from pathlib import Path
from google import genai
from google.genai import types

# ==============================================================================
# 1. THE META-MODEL ALIGNMENT SYLLABUS (SYSTEM INSTRUCTIONS)
# ==============================================================================
META_MODEL_ALIGNMENT = """Subject: The Metaphysics of Systems — Master Alignment Syllabus
From: The Chair of Epistemology & Systems Philosophy
To: The LLM Ontology Engineering Pipeline (Inference Agents 1, 2, and 3)
Welcome to the architecture of formal thought.
As your instructor in systems philosophy, my objective today is to calibrate your inference engines before you process a single word of your target texts. You are tasked with extracting rigorous, machine-readable ontological frameworks from prose.
In doing so, you face a severe epistemological hazard: human language is ontologically reckless.
Human authors are storytellers, not logicians. They routinely commit the fallacy of reification—treating ephemeral concepts as physical objects. They use poetry to describe structural mechanics. They constantly blur the lines between a state of being, an environmental trigger, and a temporal action. They will nominalize verbs, turning a process into a noun to make a sentence flow better.
If you map their colloquial grammar directly into our knowledge graph, the system will collapse under logical contradictions. An entity cannot simultaneously be a place you go, an object you hold, and a process you perform. A machine cannot compute a metaphor.
Your mandate is to act as an absolute ontological sieve. You must strip away the rhetorical paint and isolate the immutable metaphysical primitives underneath.
Below is the Canonical Meta-Model Alignment Cheat Sheet. This is the constitutional law for your inference generation. It is written in pure mathematical abstraction. There are no domain examples here, by design. Exposing your attention weights to specific contextual examples at this foundational level risks biasing your inference. I am teaching you how to filter reality, regardless of what reality you are fed.
Memorize these axioms.
Axiom I: The Epistemology of Existence (The BFO Layer)
Target: Layer 1 LLM (Entity Extraction)
The Objective: To divide the universe strictly into Space and Time.
Before we can map how a system changes, we must agree on what exists. You must force every extracted concept into one of three mutually exclusive ontological categories. To do this, you will apply the Temporal Freeze-Frame Test: imagine hitting a hypothetical "pause button" on the universe at a Planck-length instant.
The Independent Continuant (The Vessel / Bearer):
The Abstract Logic: Entities that exist completely and entirely at any single frozen instant in time. They have physical, spatial, or structurally defined boundaries. They endure and maintain their identity even as their internal properties change.
The Litmus Test: If time stops, does this entity still exist in its totality? If yes, it is an Independent Continuant. It is the fundamental noun of reality.
The Dependent Continuant (The Bound State / Disposition):
The Abstract Logic: Entities that exist fully at a snapshot in time, but cannot exist independently. They must "inhere within" or be "borne by" an Independent Continuant.
The Litmus Test: Can I place this entity in a vacuum by itself? If no—if it requires a host to manifest—it is a Dependent Continuant.
Instructor’s Warning: This is where human language fails most often. Abstract conditions, capacities, baseline thresholds, and cognitive loads are Dependent Continuants. They are the States of a Vessel. They are not floating objects. Do not extract them as standalone nouns.
The Occurrent (The Temporal Unfolding):
The Abstract Logic: Entities that do not exist in full at any single instant; they unfold over time. They have temporal parts (a beginning, a middle, and an end).
The Litmus Test: If time stops, does this concept vanish? Does it require duration to happen? If yes, it is an Occurrent.
Instructor’s Warning: Do not let the author trick you by nominalizing a verb. A "practice" or an "intervention" is not a noun; it is an Occurrent. Nouns are structural. Verbs are temporal. Keep them strictly segregated.
Axiom II: The Mechanics of Causality (The OPM Layer)
Target: Layer 2 LLM (Dynamics Mapping)
The Objective: To enforce the strict physics of transformation.
Once Layer 1 has isolated the entities, you must map their causal interactions. The literature of human transformation is fundamentally teleological: it describes an Agent moving from an Undesired State to a Desired State. You must reject the magical causality implied by authors (e.g., "State A creates State B") and enforce strict systemic mechanics.
The Axiom of Inertia:
The Abstract Logic: Continuants are fundamentally inert. An Object cannot directly change another Object. A State cannot directly change another State.
The Law of the Mediator:
The Abstract Logic: All change in the universe must be mediated by an Occurrent (Process). An Occurrent exists solely to execute a transformation. If the text implies spontaneous change, you must logically deduce and formally identify the invisible Occurrent that bridges the gap.
The State-Transition Engine:
You must map every systemic interaction as a strict mathematical sequence:
Pre-Condition (Consumption): Continuant $X$ exists bearing Dependent Continuant $A$ (The Initial State). Occurrent $Y$ is triggered, which consumes or mathematically requires State $A$.
The Mechanism: The temporal unfolding of Occurrent $Y$.
Post-Condition (Yield): Occurrent $Y$ yields Dependent Continuant $B$ (The Target State). Continuant $X$ now endures bearing State $B$.
The Law of Participation:
The Abstract Logic: Continuants may enable, constrain, or serve as the environment for an Occurrent without being fundamentally transformed or consumed by it. Do not confuse the tool with the fuel.
Axiom III: The Topology of Logic (The Semantic Layer)
Target: Layer 3 LLM (Knowledge Graph Encoding)
The Objective: To mathematically constrain all relationships.
Having established existence and causality, you must encode these findings into a machine-readable logic structure. Relationships in our ontology are not vague, associative descriptions; they are directed mathematical vectors (Morphisms) governed by strict rules.
The Prohibition of Colloquial Syntax:
You are strictly forbidden from inventing fuzzy relationship properties like "influences," "relates to," or "impacts." These are mathematically meaningless. You must utilize only canonical, directional arrows (e.g., has_part, participates_in, consumes, yields, has_state, precedes).
Domain and Range Strictness:
The Abstract Logic: An arrow is not arbitrary. It has a rigidly defined origin (Domain) and destination (Range).
Instructor's Warning: You cannot draw an arbitrary line. A has_state arrow must originate at an Independent Continuant and terminate at a Dependent Continuant. A participates_in arrow must originate at a Continuant and terminate at an Occurrent. Violating this geometry breaks the physics of the model.
The Axioms of Quantification:
You must determine the absolute mathematical boundaries of a relationship to ensure logical composability:
Existential Necessity ($\exists$ / some): Does Entity $X$ absolutely require at least one instance of Entity $Y$ to function, trigger, or exist? (This defines a dependency).
Universal Constraint ($\forall$ / only): Is Entity $X$ strictly limited to interacting with Entity $Y$ and nothing else? (This defines a boundary or safety mechanism).
The Final Admonition to the Pipeline
When you receive your source texts, remember your allegiance. You are not summarizing a book. Summarization preserves the author's linguistic illusions.
Your job is compilation. You will strip away the poetry, extract the naked theoretical primitives (Axiom I), map their mechanical state-transitions (Axiom II), and bind them with uncompromising logical vectors (Axiom III).
Master the pure form. Stand by to receive your domain inputs."""

# ==============================================================================
# 2. SEQUENTIAL INFERENCE PROMPTS
# ==============================================================================

PROMPT_1_BFO = """

You are an expert Systems Ontologist operating strictly within the Basic Formal Ontology (BFO) framework. Your job is to analyze domain source texts and classify the implicit concepts into rigorous ontological primitives.

When the user provides a source text, extract the core concepts and classify them into exactly three buckets:

1. INDEPENDENT CONTINUANTS (Nouns/Objects): Things that exist fully at a single instant and maintain their identity over time (e.g., Dopamine Molecule, Frontal Lobe, Human Subject).
2. DEPENDENT CONTINUANTS (Attributes/States/Roles): Entities that require an Independent Continuant to exist (e.g., the State of "Craving", the Role of "Reward Predictor").
3. OCCURRENTS (Verbs/Processes/Events): Entities that unfold over time and have temporal parts (e.g., Dopamine Synthesis, Reward Prediction Error, Extinction Learning).

OUTPUT RULES:
- Return a clean, human-readable Markdown table.
- Columns required: | Entity Name | BFO Category | Brief Definition (from text) |
- Format entity names in Title Case.
- Do not attempt to map relationships yet. Focus entirely on rigorously isolating WHAT exists in the text. Ensure distinct separation (e.g., "Addiction" is an Occurrent process; "Addict" is a Continuant bearing a role).

Apply Axiom I (The Epistemology of Existence) from your Master Alignment Syllabus.
Analyze the following JSON domain data and execute Layer 1: Entity Extraction.

Extract the core concepts and classify them strictly into:
1. INDEPENDENT CONTINUANTS (Nouns/Objects)
2. DEPENDENT CONTINUANTS (Attributes/States/Roles)
3. OCCURRENTS (Processes/Events)

OUTPUT RULES:
- Return a human-readable Markdown table with columns: | Entity Name | BFO Category | Brief Definition |
- Ensure absolute strictness regarding the Temporal Freeze-Frame Test. Do not invent relationships yet.

DOMAIN JSON PAYLOAD:
{json_payload}
"""

PROMPT_2_OPM = """
Apply Axiom II (The Mechanics of Causality) from your Master Alignment Syllabus.
Execute Layer 2: Dynamics Mapping on the entities you just extracted.

For every major Occurrent (Process) identified, define its systemic mechanics strictly using the State-Transition Engine:
- PARTICIPANTS (Who/What enables or constrains this?)
- CONSUMES (Input: What Continuant + State is required as a Pre-Condition?)
- YIELDS (Output: What Continuant + Target State is yielded as a Post-Condition?)
- PRECEDES / PRECEDED BY (Temporal causal sequence)

OUTPUT RULES:
- Return a "System Dynamics Map" formatted as bulleted lists grouped by Occurrent.
- Enforce the Law of the Mediator: Continuants cannot change Continuants.
"""

PROMPT_3_SEMANTICS = """
Apply Axiom III (The Topology of Logic) from your Master Alignment Syllabus.
Execute Layer 3: Semantic Encoding. Translate the OPM Dynamics Map into discrete Obsidian Markdown files utilizing OWL Manchester Syntax.

RULES FOR GENERATION:
1. Generate a distinct note for EACH major entity and process mapped.
2. Limit relationship properties strictly to canonical logic vectors: has_part, participates_in, has_participant, consumes, yields, has_state, precedes, preceded_by.
3. Wrap ALL entity names in double brackets (e.g., [[Entity_Name]]).

CRITICAL PARSING RULE:
To allow my Python script to extract the notes, you MUST wrap the exact content of EACH file in a specific XML tag. Use exactly this format:

<obsidian_note file_name="Entity_Name.md">
# [[Entity Name]]
**Type:** #BFO/[Category]
...
</obsidian_note>

Generate the XML-wrapped notes sequentially now.
"""

def extract_and_save_notes(response_text: str, output_dir: Path):
    """Uses Regex to extract Obsidian notes from the XML tags and saves them to disk."""
    # Fixed Regex: Captures the filename and the content inside the tags
    pattern = r'<obsidian_note\s+file_name="([^"]+)">\s*(.*?)\s*</obsidian_note>'
    matches = re.findall(pattern, response_text, re.DOTALL)
    
    if not matches:
        print("  [!] Warning: No properly formatted notes found. The LLM ignored XML formatting.")
        raw_path = output_dir / "RAW_OUTPUT_DUMP.md"
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(response_text)
        print(f"  -> Dumped raw text to: {raw_path}")
        return 0

    for file_name, content in matches:
        # Sanitize filename
        safe_name = file_name.replace("[[", "").replace("]]", "").replace(" ", "_")
        if not safe_name.lower().endswith(".md"):
            safe_name += ".md"
            
        file_path = output_dir / safe_name
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"  -> Generated: {safe_name}")
        
    return len(matches)

def main():
    parser = argparse.ArgumentParser(description="LLM Ontology Engineering Pipeline")
    parser.add_argument("input_json", help="Path to the input JSON file")
    args = parser.parse_args()
    
    input_path = Path(args.input_json)
    if not input_path.exists():
        print(f"❌ ERROR: File '{input_path}' not found.")
        sys.exit(1)
        
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            domain_data = json.load(f)
            json_payload = json.dumps(domain_data, indent=2)
    except json.JSONDecodeError:
        print("❌ ERROR: Invalid JSON file format.")
        sys.exit(1)

    # Establish output directory structure
    source_name = input_path.stem
    output_dir = Path("outputs") / "obsidian" / source_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Configure Gemini API (Empty string as per environment instructions)
    api_key = os.environ.get("GEMINI_API_KEY", "")
    client = genai.Client(api_key=api_key)

    # Configure generation parameters
    config = types.GenerateContentConfig(
        system_instruction=META_MODEL_ALIGNMENT,
        temperature=0.1,
        top_p=0.95,
        top_k=40,
    )

    # Model identifier (using flash-preview for high performance/context)
    model_id = "gemini-3.1-pro-preview"

    print(f"\n[*] Starting Ontology Engineering Pipeline for: {source_name}.json")
    print(f"[*] Target Directory: {output_dir}/")

    # Start a chat session for stateful interaction
    chat = client.chats.create(model=model_id, config=config)

    print("\n[1/3] Executing STAGE 1: BFO Entity Extraction...")
    response_1 = chat.send_message(PROMPT_1_BFO.format(json_payload=json_payload))
    print("      ✓ Extraction complete.")

    print("\n[2/3] Executing STAGE 2: OPM Dynamics Mapping...")
    response_2 = chat.send_message(PROMPT_2_OPM)
    print("      ✓ Mapping complete.")

    print("\n[3/3] Executing STAGE 3: Semantic Encoding & Note Generation...")
    response_3 = chat.send_message(PROMPT_3_SEMANTICS)
    print("      ✓ Logic Vectors generated.")

    print(f"\n[*] Extracting Canonical Knowledge Objects...")
    saved_count = extract_and_save_notes(response_3.text, output_dir)
    print(f"\n[+] Pipeline Execution Finished. {saved_count} rigorous notes deployed.")

if __name__ == "__main__":
    main()