"""
Task definitions for the Customer Support Crew.

Three sequential tasks with proper context passing:
1. Task 1: Knowledge agent answers from training data
2. Task 2: Web agent searches and answers (receives Task 1 output via context)
3. Task 3: Documentation agent saves both (receives Task 1 + Task 2 outputs via context)
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


def create_task_2(agent: Agent, user_query: str, task_1: Task) -> Task:
    """Create Task 2: Web search answer (receives Task 1 output via context parameter)."""
    return Task(
        description=f"""Now search the web for current information about: '{user_query}'
        
        Provide a web-based answer that complements the knowledge answer.
        This answer will be used along with the previous answer in the final record.""",
        agent=agent,
        expected_output="A detailed web-based answer with current information",
        context=[task_1]  # Proper CrewAI context passing - receives Task 1 output
    )


def create_task_3(agent: Agent, user_query: str, task_1: Task, task_2: Task) -> Task:
    """Create Task 3: Document both answers (receives Task 1 + Task 2 outputs via context)."""
    return Task(
        description=f"""Use the save_to_file tool to create a support record with:
        
        Original query: {user_query}
        Knowledge answer: (from first task)
        Web answer: (from second task)
        
        Call the save_to_file tool with all three pieces of information.""",
        agent=agent,
        expected_output="Confirmation that the support record was saved successfully",
        context=[task_1, task_2]  # Proper CrewAI context passing - receives Task 1 + Task 2 outputs
    )
