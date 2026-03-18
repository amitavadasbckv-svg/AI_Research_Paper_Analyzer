ANALYZER_PROMPT = """
Extract:
- Problem
- Methodology
- Experiments
- Findings

Return JSON.
"""

SUMMARY_PROMPT = """
Generate a 150-200 word executive summary.
"""

CITATION_PROMPT = """
Extract all citations and references.
Return as a list.
"""

INSIGHTS_PROMPT = """
Generate key insights and practical takeaways.
"""

REVIEW_PROMPT = """
Evaluate output on:
- Accuracy
- Completeness
- Clarity

Return JSON:
{
  "score": 1-10,
  "feedback": ""
}
"""

METADATA_PROMPT = """
Extract the following metadata from the research paper:

- Title
- Authors
- Publication Year
- Venue (journal/conference)

Return JSON:
{
  "title": "",
  "authors": "",
  "year": "",
  "venue": ""
}
"""
