from agents.base_helper import call_llm
from utils.prompts import METADATA_PROMPT
from utils.metadata_extractor import heuristic_metadata
import json

def metadata_agent(state):
    # Step 1: Heuristic
    heuristic = heuristic_metadata(state["first_page"])

    # Step 2: LLM refinement
    output = call_llm(METADATA_PROMPT, state["paper_text"][:3000])

    try:
        llm_data = json.loads(output)
    except:
        llm_data = {}

    # Step 3: Merge (LLM overrides only if valid)
    metadata = {}
    for key in ["title", "authors", "year", "venue"]:
        metadata[key] = llm_data.get(key) or heuristic.get(key) or "Unknown"

    state["metadata"] = metadata
    return state