from agents.base_helper import call_llm
from utils.prompts import INSIGHTS_PROMPT

def insights_agent(state):
    state["insights"] = call_llm(INSIGHTS_PROMPT, state["paper_text"])
    return state