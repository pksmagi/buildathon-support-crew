"""
Agent definitions for the Customer Support Crew.

Each agent has a distinct role with specific tools:
- knowledge_agent: Knowledge-only, NO tools (established practices expert)
- web_agent: Web search with SerperDevTool (current info research expert)
- documentation_agent: File saving with custom @tool (documentation expert)

Agent Backstories provide deep context and reasoning framework for each agent.
See prompts.py for detailed LLM prompts that guide agent reasoning.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from tools import save_to_file
from prompts import get_agent_backstories


def create_knowledge_agent() -> Agent:
    """
    Create knowledge-based support specialist (no tools).
    
    This agent draws from established, proven support practices.
    It answers questions based on deep expertise without external research.
    
    Tool: None (knowledge-only)
    Role: Expert knowledge provider
    Experience: 15+ years in support operations
    """
    backstories = get_agent_backstories()
    return Agent(
        role="Knowledge-Based Support Specialist",
        goal="Provide reliable, proven answers to support queries using established best practices and deep expertise",
        backstory=backstories["knowledge_agent"],
        verbose=False,
        allow_delegation=False,
        tools=[]  # NO tools - knowledge only
    )


def create_web_agent() -> Agent:
    """
    Create web research specialist (search tool only).
    
    This agent searches for current, up-to-date information from authoritative sources.
    It complements the knowledge-based answers with modern best practices and recent changes.
    
    Tool: SerperDevTool (web search only)
    Role: Current information research expert
    Experience: 15+ years finding and evaluating information
    """
    backstories = get_agent_backstories()
    search_tool = SerperDevTool()
    return Agent(
        role="Web Research Specialist",
        goal="Research current information, emerging best practices, and recent developments related to support queries",
        backstory=backstories["web_agent"],
        verbose=False,
        allow_delegation=False,
        tools=[search_tool]  # Only web search tool
    )


def create_documentation_agent() -> Agent:
    """
    Create documentation specialist (file saving tool only).
    
    This agent synthesizes both knowledge-based and web-researched answers
    into a comprehensive, well-organized support document.
    
    Tool: save_to_file @tool (documentation creation only)
    Role: Documentation and synthesis expert
    Experience: 15+ years in technical writing and support documentation
    """
    backstories = get_agent_backstories()
    return Agent(
        role="Documentation Specialist",
        goal="Create comprehensive, well-organized support records that combine established knowledge with current research",
        backstory=backstories["documentation_agent"],
        verbose=False,
        allow_delegation=False,
        tools=[save_to_file]  # Only file saving tool
    )

