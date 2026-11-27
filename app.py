import streamlit as st
import os
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, tool


# Custom tool for file saving
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


# Set up the Streamlit page
st.set_page_config(page_title="Customer Support Crew", layout="wide")
st.title("🤖 Customer Support System - CrewAI Powered")
st.markdown("---")

# Display how it works
with st.expander("ℹ️ How it works", expanded=False):
    st.markdown("""
    **True Sequential Process:**
    1. **Task 1**: Knowledge Agent answers from training data
    2. **Task 2**: Web Agent searches web (receives Task 1 output)
    3. **Task 3**: Documentation Agent saves both (receives Task 1 + Task 2 outputs)
    
    Each task builds on previous results through proper context passing.
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
    knowledge_agent = Agent(
        role="Knowledge-Based Support Specialist",
        goal="Answer support queries using your training knowledge without external tools",
        backstory="You are a support expert with deep knowledge. Answer directly from what you know.",
        verbose=False,
        allow_delegation=False,
        tools=[]  # No tools - knowledge only
    )
    
    # Agent 2: Web research specialist (WITH search tool)
    web_agent = Agent(
        role="Web Research Specialist",
        goal="Search the web for current information related to the support query",
        backstory="You find up-to-date web information using search tools.",
        verbose=False,
        allow_delegation=False,
        tools=[search_tool]  # Only web search tool
    )
    
    # Agent 3: Documentation specialist (WITH file saving tool)
    documentation_agent = Agent(
        role="Documentation Specialist",
        goal="Create and save support records using the provided information",
        backstory="You format and save support interactions properly.",
        verbose=False,
        allow_delegation=False,
        tools=[save_to_file]  # Only file saving tool
    )
    
    # Task 1: Get knowledge-based answer
    task_1 = Task(
        description=f"""Answer this support query using only your knowledge: '{user_query}'
        
        Provide a clear, helpful answer based on what you know.""",
        agent=knowledge_agent,
        expected_output="A clear support answer from your knowledge base"
    )
    
    # Task 2: Web search (explicitly receives Task 1 output)
    task_2 = Task(
        description=f"""You will receive the knowledge-based answer from the previous task.
        Now search the web for current information about: '{user_query}'
        
        Provide a web-based answer that complements the knowledge answer.
        This answer will be used along with the previous answer in the final record.""",
        agent=web_agent,
        expected_output="A detailed web-based answer with current information"
    )
    
    # Task 3: Document both answers (explicitly uses Task 1 and Task 2 outputs)
    task_3 = Task(
        description=f"""You will receive outputs from both previous tasks.
        Use the save_to_file tool to create a support record with:
        
        Original query: {user_query}
        Knowledge answer: (from Task 1)
        Web answer: (from Task 2)
        
        Call the save_to_file tool with all three pieces of information.""",
        agent=documentation_agent,
        expected_output="Confirmation that the support record was saved successfully"
    )
    
    # Create crew with sequential process
    crew = Crew(
        agents=[knowledge_agent, web_agent, documentation_agent],
        tasks=[task_1, task_2, task_3],
        process=Process.sequential,  # Ensures strict sequential execution
        verbose=False
    )
    
    # Execute
    with st.spinner("🔄 Agents processing sequentially..."):
        try:
            result = crew.kickoff()
            
            st.success("✅ Query processed successfully!")
            st.markdown("---")
            
            # Display query and timestamp
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
            
            # File download
            st.markdown("---")
            if os.path.exists("answers.txt"):
                with open("answers.txt", "r") as f:
                    file_content = f.read()
                st.success("💾 Support record saved to answers.txt")
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
