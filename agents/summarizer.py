from agents.base_helper import call_llm
from utils.prompts import SUMMARY_PROMPT

def summarizer_agent(state):
    state["summary"] = call_llm(SUMMARY_PROMPT, state["paper_text"])
    return state