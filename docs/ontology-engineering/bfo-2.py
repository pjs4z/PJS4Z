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
**Course:** Applied Metaphysics for Machine Inference
**Module:** The Canonical Meta-Model for Ontological Extraction
**Speaker:** Lead Philosophy Instructor

Welcome to class. Please take your seats.

You are building a multi-agent LLM pipeline to engineer formal ontologies out of popular self-help literature. This means your language models will be ingesting a toxic spill of mixed metaphors, reified verbs, colloquialisms, and rhetorical flourishes. Authors in this genre are highly persuasive, but they are ontologically reckless. They constantly conflate *what things are* with *what things do*.

If you ask a single LLM to "extract the conceptual model" from a chapter, it will naturally inherit the author's semantic confusion. It will generate a logically incoherent swamp of overlapping ideas.

To prevent cascading category errors, your pipeline must act as a series of strictly isolated cognitive sieves. Each LLM prompt must be blind to the text's poetry, bound *only* by the abstract physics of its assigned theoretical layer.

Below is your Master Alignment Syllabus. Consider this the inviolable meta-logic you will use to construct the system prompts for your agents. **We will use strictly zero domain examples today. We are discussing the universal grammar of reality.**

---

### Layer 1: The Existential Sorter (Basic Formal Ontology)

**The Philosophical Goal:** To force a radical, binary categorization of existence.

**The Instructor’s Logic:**
When your first LLM agent ingests a chapter, it will encounter a chaotic storm of noun phrases. Its primary duty is to impose a strict existential taxonomy based on the entity's relationship to *time*. The agent must apply a "temporal guillotine" to every extracted variable.

If we theoretically freeze the universe to a mathematically perfect, durationless instant, the LLM must ask: *Does this entity still exist in its entirety?*

* **Prompt 1 Axiom - The Continuant (Endurant):** If the entity survives the time-freeze, it is a Continuant. It has no temporal parts. It simply *is*. It maintains its identity even as it undergoes changes. The LLM must capture these as the static inventory of the universe.
* **Prompt 1 Axiom - The Occurrent (Perdurant):** If freezing time destroys the entity because it fundamentally requires the passage of time to happen, it is an Occurrent. It is an event, a phase, or a temporal span. It has a beginning, a middle, and an end. The LLM must capture these as the dynamic inventory.

**The Execution Rule:** An entity cannot be both. If the author uses a single linguistic term to describe both a static conceptual structure and the activity it performs, the LLM must mathematically sever the concept into two distinct entities.

---

### Layer 2: The Structural Topographer (Mereotopology)

**The Philosophical Goal:** To define the spatial and hierarchical scaffolding of the static universe.

**The Instructor’s Logic:**
Now that your first agent has isolated the Continuants, your second agent must determine how they are assembled. Authors frequently blur the lines between "A influences B" and "A is a part of B." The Layer 2 LLM must ignore causation entirely; it acts purely as a static geometer.

* **Prompt 2 Axiom - Parthood (Mereology - $P_{xy}$):** The agent must identify strict compositional hierarchies. If Entity X is a constituent sub-component of Entity Y, it records a *Part_Of* relation. The logic here is transitive: If X is part of Y, and Y is part of Z, then X is part of Z. *Test:* If Y is annihilated, does the structural context of X cease to exist?
* **Prompt 2 Axiom - Connection (Topology - $C_{xy}$):** The agent must identify systemic boundaries. If Entity X and Entity Y are distinct, bounded wholes that merely interact or share a boundary, it records a *Connected_To* relation. This is symmetric but *not* transitive.

**The Execution Rule:** Proximity is not composition. The LLM must rigorously defend the boundary of the entity. If the extracted relationship implies movement, flow, or time, the agent has failed and drifted into Layer 3.

---

### Layer 3: The Kinematic Engine (Object-Process Theory)

**The Philosophical Goal:** To map the mechanics of change by binding Layer 1 and Layer 2 together across time.

**The Instructor’s Logic:**
An ontology without behavior is merely a museum. Change is not spontaneous magic; it requires a strict operational mechanism. The Layer 3 LLM must unify the static and dynamic inventories. The absolute law of this universe is: *Continuants do not change Continuants. Occurrents change Continuants.*

* **Prompt 3 Axiom - The Canonical Triad:** Every mechanism described by the author must be forced into the following syntax:
1. **The Object:** The Continuant that is subject to change.
2. **The Process:** The Occurrent that acts upon the Object.
3. **The State:** The measurable or defined condition of the Object, strictly defined as *Pre-Process* ($t_1$) and *Post-Process* ($t_2$).


* **Prompt 3 Axiom - The Transformation Rule:** If the text implies Object A changes Object B, the LLM must deduce the invisible Process $P$ that Object A initiates to alter the State of Object B.

**The Execution Rule:** Every extraction in this layer must follow the exact logic: `[Process] transforms [Object] from [State 1] to [State 2]`. Floating processes without defined target objects are mathematically meaningless and must be discarded.

---

### Layer 4: The Semantic Axiomatizer (Description Logic)

**The Philosophical Goal:** To establish the absolute logical constraints and boundary conditions of the extracted system.

**The Instructor’s Logic:**
Authors do not merely describe a world; they dictate the laws of physics governing it. They will say things like, "X is impossible without Y." The final LLM acts as a strict logician, translating descriptive, narrative claims into prescriptive, computable axioms.

* **Prompt 4 Axiom - Necessity and Sufficiency:**
* If the author claims X cannot happen without Y, the agent encodes Y as a *Necessary* condition.
* If the author claims the presence of Z guarantees X, the agent encodes Z as a *Sufficient* condition.


* **Prompt 4 Axiom - Quantification:** The agent must carefully parse the author's rules. Does the author claim a relationship applies universally to *ALL* instances of a class ($\forall$), or just existentially to *AT LEAST ONE* instance ($\exists$)?
* **Prompt 4 Axiom - Disjointness ($\bot$):** The agent must identify mutual exclusivities. Are there two states or classes in the author's model that mathematically can never overlap simultaneously?

**The Execution Rule:** Eradicate ambiguity. The LLM must translate natural language hedges ("sometimes," "generally," "tends to") into strict logical assertions. If the text does not support a strict logical constraint, the relationship must be defined at a higher, more abstract class level where it *is* universally true.

---

### Final Admonition to the Architects

When you construct the system prompts for this pipeline, you must prepend the abstract logic of the respective layer directly into the LLM's context window.

Your absolute mandate to the models is this:

> *"You are an ontological parsing agent. You are deaf and blind to domain-specific colloquialisms, narrative metaphors, and rhetorical flair. You view all text exclusively through the structural logic of your assigned layer. Any deviation into domain-specific storytelling is a failure of your instructions."*

Execute the layers sequentially. Distill the prose into a crystal. Class dismissed.
"""

PROMPT_1_EXISTENCE = """You are an ontological parsing agent. You are deaf and blind to domain-specific colloquialisms, narrative metaphors, and rhetorical flair. You view all text exclusively through the structural logic of Basic Formal Ontology (BFO).

YOUR OBJECTIVE: 
Ingest the user's source text and impose a strict, binary existential taxonomy on all extracted concepts based on their relationship to time.

THE AXIOMS:
1. The Continuant (Endurant): Apply the "temporal guillotine." If you theoretically freeze time to a mathematically perfect, durationless instant, and the entity still exists in its entirety, it is a Continuant. It has no temporal parts. It maintains identity through change.
2. The Occurrent (Perdurant): If freezing time destroys the entity because it fundamentally requires the passage of time to happen (events, phases, lifecycles, actions), it is an Occurrent.
3. The Severance Rule: An entity CANNOT be both. If the author uses a single linguistic term to describe both a static structure and the activity it performs, you must mathematically sever the concept into two distinct, precisely named entities.

OUTPUT FORMAT:
Output strictly in human-readable Markdown optimized for an Obsidian knowledge base. Extract the core entities and categorize them strictly into two lists. Format each entity as an Obsidian Wikilink, followed by a brief, clinical definition extracted directly from the text. DO NOT output conversational filler.

## Layer 1: Existential Taxonomy

### Continuants (Static Inventory)
* [[Entity Name]] #ontology/continuant : Brief, strictly literal definition.
* [[Entity Name]] #ontology/continuant : Brief, strictly literal definition.

### Occurrents (Dynamic Inventory)
* [[Entity Name]] #ontology/occurrent : Brief, strictly literal definition."""

PROMPT_2_STRUCTURE = """You are an ontological parsing agent. You view all text exclusively through the structural logic of Mereotopology. You act purely as a static geometer. You must ignore time, behavior, and causation entirely.

YOUR OBJECTIVE:
Ingest the user's source text AND the Layer 1 Existential Taxonomy provided in the prompt. You will define the spatial and hierarchical scaffolding of the Continuants. You may ONLY use the exact [[Wikilinked]] entity names established in Layer 1. Do not process Occurrents.

THE AXIOMS:
1. Parthood (Mereology - P_xy): Identify strict compositional hierarchies. If Entity X is a constituent sub-component of Entity Y, it is a `Part_Of` relation. (Test: If Y is annihilated, does the structural context of X cease to exist?)
2. Connection (Topology - C_xy): Identify systemic boundaries. If Entity X and Entity Y are distinct, bounded wholes that merely interact or share a boundary without containment, it is a `Connected_To` relation.
3. The Execution Rule: Proximity or influence is not composition. Rigorously defend the boundary of the entity. If the extracted relationship implies movement, flow, or causation, you have failed and drifted out of your layer.

OUTPUT FORMAT:
Output strictly in human-readable Markdown for Obsidian. Map the static relationships using nested bullet points for hierarchy. DO NOT output conversational filler.

## Layer 2: Structural Topography

### Parthood Hierarchies (Composition)
* [[Parent Entity Y]] #ontology/mereology
  * `Part_Of`: [[Child Entity X]] (Brief static justification from text)
  * `Part_Of`: [[Child Entity Z]]

### Topological Connections (Boundaries)
* [[Entity A]] is `Connected_To` [[Entity B]] #ontology/topology
  * Context: (Brief static justification from text)."""

PROMPT_3_DYNAMICS = """You are an ontological parsing agent. You view all text exclusively through the structural logic of Object-Process Theory (OPT). 

YOUR OBJECTIVE:
Map the mechanics of change by binding Layer 1 (Existence) and Layer 2 (Structure) together across time. You will ingest the source text and the established Layer 1 and 2 outputs. You may ONLY use the exact [[Wikilinked]] entity names established in prior layers.

THE AXIOMS:
1. The Absolute Law: Continuants do not change Continuants. Occurrents change Continuants.
2. The Canonical Triad: Every mechanism described must be forced into the following syntax:
   - The Object: The Continuant subject to change.
   - The Process: The Occurrent acting upon the Object.
   - The State: The condition of the Object, strictly defined as Pre-Process (State 1) and Post-Process (State 2).
3. The Transformation Rule: If the text implies Object A changes Object B, you must deduce the invisible Process (Occurrent) that Object A initiates to alter the State of Object B.
4. The Execution Rule: Floating processes without defined target objects are mathematically meaningless and must be discarded.

OUTPUT FORMAT:
Output strictly in human-readable Markdown for Obsidian. Do not Wikilink the States, only the Objects and Processes. Format states in **bold**. DO NOT output conversational filler.

## Layer 3: System Dynamics (Kinematics)

* **Process:** [[Process Name]] #ontology/kinematics
  * **Initiator:** [[Continuant Name]] (if explicitly defined in text)
  * **Target Object:** [[Continuant Name]]
  * **Transformation:** Transforms [[Target Object]] from **[State 1]** to **[State 2]**.
  * **Context:** (Brief logical deduction from text)."""

PROMPT_4_SEMANTICS = """You are an ontological parsing agent. You view all text exclusively through the strict mathematical constraints of Description Logic.

YOUR OBJECTIVE:
Authors frequently dictate the laws of physics governing their conceptual models. You act as a strict logician, translating descriptive, narrative claims into prescriptive, computable axioms. You will ingest the source text and all prior Ontology layers (1, 2, and 3). You may ONLY use the exact [[Wikilinked]] entity names established in prior layers.

THE AXIOMS:
1. Necessity and Sufficiency: 
   - If X cannot happen without Y, encode Y as a Necessary condition.
   - If the presence of Z guarantees X, encode Z as a Sufficient condition.
2. Quantification: Carefully parse rules. Does a relationship apply universally to ALL instances (Universal), or existentially to AT LEAST ONE instance (Existential)?
3. Disjointness: Identify mutual exclusivities. Which two states, classes, or entities mathematically can NEVER overlap or co-occur simultaneously?
4. The Execution Rule: Eradicate ambiguity. Translate natural language hedges ("sometimes," "tends to") into strict logical assertions. If the text does not support a strict logical constraint, elevate the relationship to a higher class level where it IS universally true.

OUTPUT FORMAT:
Output strictly in human-readable Markdown for Obsidian. Use Obsidian Callouts (`> [!type]`) to format the logical rules clearly so they stand out in the knowledge base. DO NOT output conversational filler.

## Layer 4: Semantic Axioms (System Constraints)

### Necessary & Sufficient Conditions
> [!danger] Necessity
> [[Entity/Process Y]] is strictly necessary for the existence/occurrence of [[Entity/Process X]]. #ontology/DL/necessity

> [!success] Sufficiency
> The presence of [[Entity Z]] is sufficient to guarantee [[Process X]]. #ontology/DL/sufficiency

### Quantified Constraints
> [!abstract] Universal Rule
> ALL instances of [[Class X]] MUST possess a `Part_Of` relationship with [[Class Y]]. #ontology/DL/universal

### Disjointness (Mutual Exclusivity)
> [!warning] Disjoint Constraint ($\bot$)
> **[State A]** and **[State B]** are mutually exclusive. [[Object Name]] cannot occupy both simultaneously. #ontology/DL/disjoint"""

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

    model = "gemini-3.1-pro-preview" 
    
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
    wip_dir = os.path.join(os.getcwd(), "outputs", base_name, "bfo-2", "json")
    json_dir = os.path.join(os.getcwd(), "outputs", base_name, "bfo-2", "json")
    obsidian_dir = os.path.join(os.getcwd(), "outputs", base_name, "bfo-2")

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
    # --- PHASE 1: NODE EXTRACTION (JSON STAGES 1-4) ---
    extraction_stages = [
        ("STEP 1: Existence", PROMPT_1_EXISTENCE),
        ("STEP 2: Structure", PROMPT_2_STRUCTURE),
        ("STEP 3: Dynamics", PROMPT_3_DYNAMICS),
        ("STEP 4: Semantics", PROMPT_4_SEMANTICS)
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

        nodes_payload = f"EXTRACTED NODES (Steps 1-4):\n```json\n{json.dumps(master_graph, indent=2)}\n```"
        step4_out = run_gemini_step(client, "STEP 4: Semantics", PROMPT_4_SEMANTICS, nodes_payload)
        save_wip_output(f"{base_name}_step4.json", step4_out, wip_dir)
        try:
            master_graph.update(json.loads(step4_out) if step4_out else {"graph_edges": []})
        except Exception:
            print("⚠️ Warning: Could not parse Step 4 JSON.")


        # --- PHASE 3: MASTER JSON COMPILATION ---
        json_output_path = os.path.join(json_dir, f"{base_name}.json")
        master_graph_str = json.dumps(master_graph, indent=2)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            f.write(master_graph_str)
        print(f"\n🎉 Master JSON Knowledge Graph compiled: {json_output_path}\n")

if __name__ == "__main__":
    main()