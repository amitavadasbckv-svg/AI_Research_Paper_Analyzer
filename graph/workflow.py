from langgraph.graph import StateGraph, END
from agents.analyzer import analyzer_agent
from agents.summarizer import summarizer_agent
from agents.citation import citation_agent
from agents.insights import insights_agent
from agents.reviewer import review_output
from agents.metadata import metadata_agent

MAX_RETRIES = 2

def review_and_retry(agent_func, key):
    def wrapper(state):
        for i in range(MAX_RETRIES):
            state = agent_func(state)
            review = review_output(str(state.get(key)))

            if review["score"] >= 7:
                return state

        return state
    return wrapper


def build_graph():
    builder = StateGraph(dict)

    builder.add_node("metadata", review_and_retry(metadata_agent, "metadata"))
    builder.add_node("analyzer", review_and_retry(analyzer_agent, "analysis"))
    builder.add_node("summarizer", review_and_retry(summarizer_agent, "summary"))
    builder.add_node("citation", review_and_retry(citation_agent, "citations"))
    builder.add_node("insights", review_and_retry(insights_agent, "insights"))

    builder.set_entry_point("metadata")

    builder.add_edge("metadata", "analyzer")
    builder.add_edge("analyzer", "summarizer")
    builder.add_edge("summarizer", "citation")
    builder.add_edge("citation", "insights")
    builder.add_edge("insights", END)

    return builder.compile()
