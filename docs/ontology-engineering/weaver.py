from typing import List, Optional, Literal
from pydantic import BaseModel, Field

# --- 1. Define the Strict Ontology Schema (Based on your Document) ---

# Allowable Node Categories per your document
UFO_A_Types = Literal["Kind", "Phase", "Role", "Quality", "Disposition", "Relator"]
UFO_B_Types = Literal["Situation", "Event"]
UFO_C_Types = Literal["Agent", "Object", "Belief", "Desire", "Intention", "Happening", "Action", "Commitment", "Claim"]

class OntologyNode(BaseModel):
    id: str = Field(..., description="Unique ID (e.g., 'event_boiling_1')")
    label: str = Field(..., description="The text found in source (e.g., 'Boiling')")
    category: str = Field(..., description="The specific UFO category")

class OntologyEdge(BaseModel):
    source_id: str
    target_id: str
    relation: Literal[
        "inheresIn", "mediates", "triggers", "manifests", 
        "bringsAbout", "motivatedBy", "fulfills", "violates"
    ]

class ExtractionResult(BaseModel):
    nodes: List[OntologyNode]
    edges: List[OntologyEdge] = []

# --- 2. The Specialist Prompts ---

PROMPT_UFO_A = """
You are a specialist in UFO-A (Endurants). Your job is to extract STATIC entities from text.
Strictly adhere to these definitions:
- Kind: Rigid identity (e.g., Human, Star).
- Phase: Intrinsic state change (e.g., Caterpillar).
- Role: Context-dependent identity (e.g., Student).
- Quality: Measurable property (e.g., Temperature).
- Disposition: Latent potential (e.g., Flammability).
- Relator: Object binding relationships (e.g., Marriage).

Do NOT extract events, time, or mental states. Return JSON only.
"""

PROMPT_UFO_B = """
You are a specialist in UFO-B (Perdurants). Your job is to extract TEMPORAL entities.
Strictly adhere to these definitions:
- Situation: A frozen snapshot of reality at time t.
- Event: A dynamic process changing Situation T1 to T2.

Do NOT extract people, objects, or intentions. Return JSON only.
"""

PROMPT_UFO_C = """
You are a specialist in UFO-C (Intentionality). Your job is to extract COGNITIVE and NORMATIVE entities.
Definitions:
- Agent: Entity with intentionality (Person).
- Object: Mechanistic entity (Gear).
- Mental States: Belief, Desire, Intention.
- Normative: Commitment, Claim.
- Special Events: Happening (passive experience), Action (deliberate authoring).

Return JSON only.
"""

PROMPT_WEAVER = """
You are the Relational Weaver. You will be given a list of extracted Nodes.
Your job is to connect them using ONLY these Valid Edges:
- inheresIn (Moment -> Substantial)
- mediates (Relator -> Role)
- triggers (Situation -> Disposition)
- manifests (Event -> Disposition)
- bringsAbout (Event -> Situation)
- motivatedBy (Action -> Intention)
- fulfills/violates (Action -> Commitment)

CRITICAL RULES:
1. Never cross Domain/Range improperly.
2. Do not invent new nodes.
3. Output a list of edges.
"""

# --- 3. The Orchestration Logic ---

def extract_ontology(source_text: str):
    print(f"--- Processing: {source_text[:50]}... ---\n")
    
    all_nodes = []

    # [Step 1] Run Specialist Agents in parallel or sequence
    # Note: In a real implementation, 'simulate_llm_call' would be 'client.chat.completions.create'
    
    print("🤖 Agent A (Structure) working...")
    nodes_a = simulate_llm_call(PROMPT_UFO_A, source_text, ["Kind", "Quality"])
    all_nodes.extend(nodes_a)

    print("🤖 Agent B (Time) working...")
    nodes_b = simulate_llm_call(PROMPT_UFO_B, source_text, ["Event", "Situation"])
    all_nodes.extend(nodes_b)

    print("🤖 Agent C (Mind) working...")
    nodes_c = simulate_llm_call(PROMPT_UFO_C, source_text, ["Agent", "Intention", "Action"])
    all_nodes.extend(nodes_c)

    # [Step 2] Run The Weaver
    print("🕸️ Agent D (Weaver) connecting the graph...")
    edges = simulate_weaver_call(PROMPT_WEAVER, all_nodes)

    # [Step 3] Validation (The Axioms Check)
    print("⚖️ Agent E (Validator) checking axioms...")
    valid, errors = validate_axioms(all_nodes, edges)

    if not valid:
        print(f"⚠️ LOGICAL ERRORS FOUND: {errors}")
    else:
        print("✅ Graph is valid.")

    return ExtractionResult(nodes=all_nodes, edges=edges)

# --- 4. Helpers & Simulation (For Demonstration) ---

def simulate_llm_call(system_prompt, text, likely_types):
    """
    Simulates an LLM response. In production, replace this with your API call 
    that asks for JSON output matching the 'OntologyNode' schema.
    """
    # This is dummy data to demonstrate the output structure
    mock_nodes = []
    if "UFO-A" in system_prompt:
        mock_nodes.append(OntologyNode(id="p1", label="John", category="Kind"))
        mock_nodes.append(OntologyNode(id="d1", label="Fragility", category="Disposition"))
    elif "UFO-B" in system_prompt:
        mock_nodes.append(OntologyNode(id="s1", label="Glass on edge", category="Situation"))
    elif "UFO-C" in system_prompt:
        mock_nodes.append(OntologyNode(id="a1", label="Knocking over", category="Action"))
        mock_nodes.append(OntologyNode(id="i1", label="Harm the owner", category="Intention"))
    return mock_nodes

def simulate_weaver_call(system_prompt, nodes):
    """
    Simulates the Edge extraction agent.
    """
    # Dummy edges connecting the mock nodes above
    return [
        OntologyEdge(source_id="d1", target_id="p1", relation="inheresIn"), # Fragility inheres in John (Example error)
        OntologyEdge(source_id="a1", target_id="i1", relation="motivatedBy")
    ]

def validate_axioms(nodes, edges):
    """
    Implements Section IV: Axioms of Inference
    """
    node_map = {n.id: n for n in nodes}
    errors = []
    
    for edge in edges:
        source = node_map.get(edge.source_id)
        target = node_map.get(edge.target_id)
        
        # 1. The Parasite Error Check
        # Moments (Quality, Disposition, Intention, Commitment) MUST inhere in a Substantial
        moments = ["Quality", "Disposition", "Intention", "Commitment"]
        if source.category in moments and edge.relation != "inheresIn":
             # This is a simplification; in reality, we check if the moment LACKS an inheresIn edge entirely
             pass 

        # 2. Authorship Error Check
        if source.category == "Happening" and edge.relation == "motivatedBy":
            errors.append(f"Authorship Error: Happening '{source.label}' cannot be motivatedBy Intention.")

        # 3. Mechanistic Intent Error Check
        if source.category == "Object" and edge.relation == "inheresIn" and target.category == "Intention":
             errors.append(f"Mechanistic Error: Object '{source.label}' cannot possess Intention.")

    return (len(errors) == 0), errors

# --- Run the Pipeline ---
if __name__ == "__main__":
    sample_text = "John decided to break the vase. The fragility of the vase led to it shattering."
    result = extract_ontology(sample_text)
    
    print("\n--- Final Graph ---")
    for n in result.nodes:
        print(f"[{n.category}] {n.label} ({n.id})")
    for e in result.edges:
        print(f"({e.source_id}) --{e.relation}--> ({e.target_id})")