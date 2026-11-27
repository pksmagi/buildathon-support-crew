"""
Agent definitions for the Customer Support Crew.

Each agent has a distinct role with specific tools:
- knowledge_agent: Knowledge-only, NO tools
- web_agent: Web search with SerperDevTool
- documentation_agent: File saving with custom @tool
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from tools import save_to_file


def create_knowledge_agent() -> Agent:
    """Create knowledge-based support specialist (no tools)."""
    return Agent(
        role="Knowledge-Based Support Specialist",
        goal="Answer support queries using your training knowledge without external tools",
        backstory="You are a support expert with deep knowledge. Answer directly from what you know.",
        verbose=False,
        allow_delegation=False,
        tools=[]  # NO tools - knowledge only
    )


def create_web_agent() -> Agent:
    """Create web research specialist (search tool only)."""
    search_tool = SerperDevTool()
    return Agent(
        role="Web Research Specialist",
        goal="Search the web for current information related to the support query",
        backstory="You find up-to-date web information using search tools.",
        verbose=False,
        allow_delegation=False,
        tools=[search_tool]  # Only web search tool
    )


def create_documentation_agent() -> Agent:
    """Create documentation specialist (file saving tool only)."""
    return Agent(
        role="Documentation Specialist",
        goal="Create and save support records using the provided information",
        backstory="You format and save support interactions properly.",
        verbose=False,
        allow_delegation=False,
        tools=[save_to_file]  # Only file saving tool
    )
