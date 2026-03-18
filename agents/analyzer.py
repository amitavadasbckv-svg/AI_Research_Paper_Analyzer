from agents.base_helper import call_llm
from utils.prompts import ANALYZER_PROMPT
import json

def analyzer_agent(state):
    output = call_llm(ANALYZER_PROMPT, state["paper_text"])
    try:
        state["analysis"] = json.loads(output)
    except:
        state["analysis"] = {"raw": output}
    return state
