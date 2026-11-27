"""
Task definitions for the Customer Support Crew.

Three sequential tasks with proper context passing and enterprise-grade LLM prompts.

Design:
1. Task 1: Knowledge agent answers from established practices
2. Task 2: Web agent researches current best practices (receives Task 1 output via context)
3. Task 3: Documentation agent synthesizes both (receives Task 1 + Task 2 outputs via context)

LLM Prompts are designed with:
- Role clarity and expertise framing
- Explicit quality criteria
- Reasoning framework guidance
- Output structure specifications
- Professional standards for 15+ year experts

See prompts.py for detailed prompt engineering.
"""

from crewai import Task, Agent
from prompts import get_task_1_prompt, get_task_2_prompt, get_task_3_prompt


def create_task_1(agent: Agent, user_query: str) -> Task:
    """
    Create Task 1: Knowledge-based answer (no previous context).
    
    This is the foundation task. The knowledge agent provides reliable,
    established answers from proven best practices and deep expertise.
    
    LLM Prompt:
    - Guides agent to provide comprehensive knowledge-based answer
    - Includes reasoning framework (what, how, why)
    - Specifies quality criteria for the response
    - Defines output structure for clarity
    
    Output: Used by Task 2 and Task 3 via context parameter
    """
    return Task(
        description=get_task_1_prompt(user_query),
        agent=agent,
        expected_output="""A comprehensive knowledge-based support answer with:
        - Clear summary of the solution
        - Step-by-step instructions
        - Best practices and security considerations
        - Common pitfalls and fallback options
        - Professional, helpful tone
        - Ready to be combined with web research findings"""
    )


def create_task_2(agent: Agent, user_query: str, task_1: Task) -> Task:
    """
    Create Task 2: Web research answer (receives Task 1 output via context).
    
    The web agent researches current, up-to-date information from authoritative sources.
    It complements the knowledge-based answer with modern best practices and recent changes.
    
    Context Passing:
    - Receives Task 1 output via context=[task_1]
    - Can reference established practices from Task 1
    - Provides comparative analysis (what's new/different)
    
    LLM Prompt:
    - Guides research strategy and source evaluation
    - Specifies quality criteria for web sources
    - Requests comparative analysis vs Task 1
    - Emphasizes current best practices and security updates
    - Defines output structure matching Task 1
    
    Output: Used by Task 3 via context parameter
    """
    return Task(
        description=get_task_2_prompt(user_query),
        agent=agent,
        expected_output="""A current, research-backed support answer including:
        - What's new or changed from traditional knowledge
        - Current recommended approaches with dates/versions
        - Modern alternatives and emerging technologies
        - Current security standards (NIST, OWASP)
        - What to avoid (deprecated methods)
        - Authoritative sources and references
        - Ready to be combined with knowledge-based findings""",
        context=[task_1]  # Proper CrewAI context passing - receives Task 1 output
    )


def create_task_3(agent: Agent, user_query: str, task_1: Task, task_2: Task) -> Task:
    """
    Create Task 3: Synthesize and document both answers (receives Task 1 + Task 2 outputs).
    
    The documentation agent creates a comprehensive support record that combines
    established knowledge with current research into a valuable document.
    
    Context Passing:
    - Receives Task 1 output (knowledge-based answer) via context=[task_1]
    - Receives Task 2 output (web research answer) via context=[task_2]
    - Synthesizes both into a cohesive support record
    
    LLM Prompt:
    - Guides synthesis of both answers
    - Specifies documentation quality criteria
    - Provides tool usage instructions (save_to_file)
    - Emphasizes completeness and accuracy
    - Defines file format and structure
    
    Output: Saved to answers.txt via save_to_file tool
    """
    return Task(
        description=get_task_3_prompt(user_query),
        agent=agent,
        expected_output="""Confirmation that the support record was created successfully:
        - File saved to answers.txt
        - Timestamp recorded
        - Both answers properly preserved
        - Customer query documented
        - Professional format maintained
        - Ready for user download and future reference""",
        context=[task_1, task_2]  # Proper CrewAI context passing - receives Task 1 + Task 2 outputs
    )

