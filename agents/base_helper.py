from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def call_llm(prompt, content):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"{prompt}\n\n{content}"
    )
    return response.output_text