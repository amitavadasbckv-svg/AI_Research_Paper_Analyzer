from pydantic import BaseModel
from typing import List, Dict

class Analysis(BaseModel):
    problem: str
    methodology: str
    experiments: str
    findings: str

class Review(BaseModel):
    score: int
    feedback: str

class State(dict):
    pass
