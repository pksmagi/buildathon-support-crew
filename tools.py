"""
Custom tools for the Customer Support Crew.

Implements the file-saving tool as a proper CrewAI @tool decorator,
not as plain Python file I/O.
"""

from datetime import datetime
from crewai_tools import tool


@tool
def save_to_file(query: str, assistant_answer: str, web_answer: str) -> str:
    """Save query and both answers to a text file. Use this tool to document support interactions.
    
    Args:
        query: The original customer query
        assistant_answer: Answer from knowledge-based assistant
        web_answer: Answer from web research
    
    Returns:
        Confirmation message with file path and timestamp
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""=====================================
CUSTOMER SUPPORT RECORD
=====================================

TIMESTAMP: {timestamp}

CUSTOMER QUERY:
{query}

---

KNOWLEDGE-BASED ANSWER:
{assistant_answer}

---

WEB RESEARCH ANSWER:
{web_answer}

=====================================
"""
    filepath = "answers.txt"
    with open(filepath, "w") as f:
        f.write(content)
    return f"Record saved to {filepath} at {timestamp}"
