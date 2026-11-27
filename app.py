import streamlit as st
import os
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, tool


# Custom tool for file saving
@tool
def save_to_file(query: str, assistant_answer: str, web_answer: str) -> str:
    """Save query and both answers to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""=====================================
CUSTOMER SUPPORT RECORD
=====================================

TIMESTAMP: {timestamp}
---

CUSTOMER QUERY:
{query}

---

ASSISTANT ANSWER (From Knowledge):
{assistant_answer}

---

WEB SEARCH ANSWER (Current Information):
{web_answer}

---
[End of Record]
=====================================
"""
    with open("answers.txt", "w") as f:
        f.write(content)
    return f"Successfully saved record to answers.txt at {timestamp}"


# Set up the Streamlit page
st.set_page_config(page_title="Customer Support Crew", layout="wide")
st.title("🤖 Customer Support System - CrewAI Powered")
st.markdown("---")

# Display how it works
with st.expander("ℹ️ How it works", expanded=False):
    st.markdown("""
    **Sequential Process:**
    1. **Assistant Agent** answers directly from knowledge (specialized in general support)
    2. **Web Search Agent** searches current web info (specialized in real-time data)
    3. **Entry Agent** documents and saves the interaction
    
    Each agent builds on previous results in true sequential order.
    """)

# Create input form
with st.form("query_form"):
    user_query = st.text_area(
        "Enter your customer support query:",
        placeholder="e.g., How do I reset my password?",
        height=100
    )
    submitted = st.form_submit_button("🚀 Submit Query", use_container_width=True)

if submitted and user_query:
    st.markdown("---")
    st.info("⏳ Processing your query through the crew sequentially...")
    
    # Initialize tools
    search_tool = SerperDevTool()
    
    # Agent 1: Knowledge-based assistant (NO web search capability)
    assistant_agent = Agent(
        role="Knowledge-Based Support Assistant",
        goal="Provide accurate answers to support queries using your training knowledge only",
        backstory="You are a support specialist with deep knowledge of common issues. Answer queries directly without searching.",
        verbose=False,
        allow_delegation=False,
        tools=[]  # No tools - knowledge only
    )
    
    # Agent 2: Web research specialist (WITH search tool)
    web_search_agent = Agent(
        role="Web Research Specialist",
        goal="Find current, up-to-date information from the web to supplement support",
        backstory="You specialize in finding the most current web information using search tools.",
        verbose=False,
        allow_delegation=False,
        tools=[search_tool]  # Only web search tool
    )
    
    # Agent 3: Documentation specialist (WITH file saving tool)
    entry_agent = Agent(
        role="Documentation Specialist",
        goal="Create comprehensive support records by combining all answers",
        backstory="You format and save complete support interactions for record-keeping.",
        verbose=False,
        allow_delegation=False,
        tools=[save_to_file]  # Only file saving tool
    )
    
    # Task 1: Get knowledge-based answer
    task_1 = Task(
        description=f"Answer this support query using your knowledge: '{user_query}'",
        agent=assistant_agent,
        expected_output="A clear, helpful answer based on your knowledge"
    )
    
    # Task 2: Get web-based answer (depends on Task 1 completion)
    task_2 = Task(
        description=f"""Search the web for current information about: '{user_query}'
        Provide an answer that complements the knowledge-based answer.""",
        agent=web_search_agent,
        expected_output="A detailed answer based on current web sources"
    )
    
    # Task 3: Save both answers (depends on Task 1 and Task 2)
    task_3 = Task(
        description=f"""Document this support interaction by:
        1. Using the original query: {user_query}
        2. Including the knowledge-based answer from Task 1
        3. Including the web-based answer from Task 2
        4. Saving everything to file using the save_to_file tool
        
        Call save_to_file with query, assistant_answer (from task 1), and web_answer (from task 2).""",
        agent=entry_agent,
        expected_output="Confirmation that the support record was saved"
    )
    
    # Create crew with true sequential processing
    crew = Crew(
        agents=[assistant_agent, web_search_agent, entry_agent],
        tasks=[task_1, task_2, task_3],
        process=Process.sequential,  # Ensures strict sequential execution
        verbose=False
    )
    
    # Execute crew
    with st.spinner("🔄 Agents processing sequentially..."):
        try:
            result = crew.kickoff()
            
            # Display success
            st.success("✅ Query processed successfully!")
            st.markdown("---")
            
            # Show query details
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("📝 Query")
                st.write(user_query)
            with col2:
                st.subheader("⏰ Processed At")
                st.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            st.markdown("---")
            st.subheader("🤖 Agent Responses")
            st.write(result)
            
            # Offer file download
            st.markdown("---")
            if os.path.exists("answers.txt"):
                with open("answers.txt", "r") as f:
                    file_content = f.read()
                st.success("💾 Record saved to answers.txt")
                st.download_button(
                    label="📥 Download answers.txt",
                    data=file_content,
                    file_name="answers.txt",
                    mime="text/plain"
                )
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Ensure API keys are set: OPENAI_API_KEY and SERPER_API_KEY")

elif submitted and not user_query:
    st.warning("⚠️ Please enter a query!")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center'><small>Customer Support System | CrewAI + Streamlit</small></div>", unsafe_allow_html=True)
