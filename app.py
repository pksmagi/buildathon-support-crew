"""
Customer Support System - CrewAI + Streamlit

A sequential crew of three agents that process customer queries:
1. Knowledge Agent: Answers from training knowledge
2. Web Agent: Searches web for current information
3. Documentation Agent: Saves both answers to file

Usage:
    streamlit run app.py

Environment Variables Required:
    OPENAI_API_KEY: OpenAI API key
    SERPER_API_KEY: Serper web search API key
"""

import streamlit as st
from crewai import Crew, Process

from agents import create_knowledge_agent, create_web_agent, create_documentation_agent
from tasks import create_task_1, create_task_2, create_task_3
from ui import (
    configure_page,
    show_info,
    get_user_query,
    show_processing,
    show_results,
    show_error,
    show_warning,
    show_footer,
)


def main():
    """Main application flow."""
    # Configure UI
    configure_page()
    show_info()
    
    # Get user input
    user_query, submitted = get_user_query()
    
    if submitted and user_query:
        show_processing()
        
        # Create agents
        knowledge_agent = create_knowledge_agent()
        web_agent = create_web_agent()
        documentation_agent = create_documentation_agent()
        
        # Create tasks
        task_1 = create_task_1(knowledge_agent, user_query)
        task_2 = create_task_2(web_agent, user_query)
        task_3 = create_task_3(documentation_agent, user_query)
        
        # Create crew with sequential process
        crew = Crew(
            agents=[knowledge_agent, web_agent, documentation_agent],
            tasks=[task_1, task_2, task_3],
            process=Process.sequential,  # Ensures strict sequential execution
            verbose=False
        )
        
        # Execute crew
        with st.spinner("🔄 Agents processing sequentially..."):
            try:
                result = crew.kickoff()
                show_results(result, user_query)
            except Exception as e:
                show_error(str(e))
    
    elif submitted and not user_query:
        show_warning()
    
    # Footer
    show_footer()


if __name__ == "__main__":
    main()
