"""
Task definitions for the Customer Support Crew.

Three sequential tasks ensuring context passing:
1. Task 1: Knowledge agent answers from training data
2. Task 2: Web agent searches and answers (receives Task 1 output)
3. Task 3: Documentation agent saves both (receives Task 1 + Task 2 outputs)
"""

from crewai import Task, Agent


def create_task_1(agent: Agent, user_query: str) -> Task:
    """Create Task 1: Knowledge-based answer (no previous context)."""
    return Task(
        description=f"""Answer this support query using only your knowledge: '{user_query}'
        
        Provide a clear, helpful answer based on what you know.""",
        agent=agent,
        expected_output="A clear support answer from your knowledge base"
    )


def create_task_2(agent: Agent, user_query: str) -> Task:
    """Create Task 2: Web search answer (receives Task 1 output)."""
    return Task(
        description=f"""You will receive the knowledge-based answer from the previous task.
        Now search the web for current information about: '{user_query}'
        
        Provide a web-based answer that complements the knowledge answer.
        This answer will be used along with the previous answer in the final record.""",
        agent=agent,
        expected_output="A detailed web-based answer with current information"
    )


def create_task_3(agent: Agent, user_query: str) -> Task:
    """Create Task 3: Document both answers (receives Task 1 + Task 2 outputs)."""
    return Task(
        description=f"""You will receive outputs from both previous tasks.
        Use the save_to_file tool to create a support record with:
        
        Original query: {user_query}
        Knowledge answer: (from Task 1)
        Web answer: (from Task 2)
        
        Call the save_to_file tool with all three pieces of information.""",
        agent=agent,
        expected_output="Confirmation that the support record was saved successfully"
    )
