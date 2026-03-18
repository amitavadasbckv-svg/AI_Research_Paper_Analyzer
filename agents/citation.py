from agents.base_helper import call_llm
from utils.prompts import CITATION_PROMPT

def citation_agent(state):
    state["citations"] = call_llm(CITATION_PROMPT, state["paper_text"])
    return state