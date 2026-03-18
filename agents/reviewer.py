from utils.prompts import REVIEW_PROMPT
from agents.base_helper import call_llm
import json

def review_output(output):
    response = call_llm(REVIEW_PROMPT, output)
    try:
        return json.loads(response)
    except:
        return {"score": 6, "feedback": "Parsing failed"}