import re

def heuristic_metadata(first_page_text):
    lines = [l.strip() for l in first_page_text.split("\n") if l.strip()]

    title = lines[0] if len(lines) > 0 else "Unknown"

    # Authors: line with commas or multiple words
    authors = "Unknown"
    for line in lines[:5]:
        if "," in line or " and " in line:
            authors = line
            break

    # Year detection
    year_match = re.search(r"(19|20)\d{2}", first_page_text)
    year = year_match.group() if year_match else "Unknown"

    # Venue keywords
    venue = "Unknown"
    for line in lines:
        if any(k in line.lower() for k in ["conference", "journal", "ieee", "acm"]):
            venue = line
            break

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue
    }