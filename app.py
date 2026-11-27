import streamlit as st
import os
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Initialize session state for storing results
if "assistant_answer" not in st.session_state:
    st.session_state.assistant_answer = None
if "web_search_answer" not in st.session_state:
    st.session_state.web_search_answer = None
if "file_saved" not in st.session_state:
    st.session_state.file_saved = False

# Set up the Streamlit page
st.set_page_config(page_title="Customer Support Crew", layout="wide")
st.title("🤖 Customer Support System - CrewAI Powered")
st.markdown("---")

# Display instructions
with st.expander("ℹ️ How it works", expanded=False):
    st.markdown("""
    1. **Assistant Agent**: Answers your query directly from its knowledge
    2. **Web Search Agent**: Searches the web and provides additional information
    3. **Entry Agent**: Saves both answers and your query to a text file
    
    All three agents work sequentially to provide comprehensive support.
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
    st.info("⏳ Processing your query through the support crew...")
    
    # Initialize tools
    search_tool = SerperDevTool()
    
    # Create Agent 1: Assistant
    assistant_agent = Agent(
        role="Customer Support Assistant",
        goal="Answer the user's customer support query directly based on your knowledge",
        backstory="""You are an experienced customer support representative who answers 
        customer queries directly with your expertise. Provide clear, concise, and helpful 
        answers based on your knowledge base.""",
        verbose=False,
        allow_delegation=False
    )
    
    # Create Agent 2: Web Search Assistant
    web_search_agent = Agent(
        role="Web Search Specialist",
        goal="Search the web to find current information about the customer's query and provide an answer",
        backstory="""You are an expert at searching the web and finding relevant information. 
        You use search tools to find the most up-to-date and relevant information to answer 
        customer queries. Always cite sources where appropriate.""",
        tools=[search_tool],
        verbose=False,
        allow_delegation=False
    )
    
    # Create Agent 3: Entry Agent
    entry_agent = Agent(
        role="Data Entry Specialist",
        goal="Save the customer query and both answers to a text file for record-keeping",
        backstory="""You are responsible for documenting all customer support interactions. 
        You write comprehensive records of queries and responses to files for future reference 
        and quality assurance.""",
        verbose=False,
        allow_delegation=False
    )
    
    # Create Tasks in sequence
    task_1 = Task(
        description=f"Answer this customer support query directly from your knowledge: {user_query}",
        agent=assistant_agent,
        expected_output="A clear and helpful answer to the customer's query"
    )
    
    task_2 = Task(
        description=f"Search the web and provide information about: {user_query}. Provide a comprehensive answer based on current web sources.",
        agent=web_search_agent,
        expected_output="A detailed answer based on web search results"
    )
    
    task_3 = Task(
        description=f"""Save the following information to a file named 'answers.txt':
        - Customer Query: {user_query}
        - Assistant Answer: {{task_1_output}}
        - Web Search Answer: {{task_2_output}}
        
        Format it nicely and include the timestamp. Return confirmation that the file was saved.""",
        agent=entry_agent,
        expected_output="Confirmation that the file has been saved with all information"
    )
    
    # Create the crew with sequential process
    crew = Crew(
        agents=[assistant_agent, web_search_agent, entry_agent],
        tasks=[task_1, task_2, task_3],
        process=Process.sequential,
        verbose=False
    )
    
    # Execute the crew
    with st.spinner("🔄 Agents are working on your query..."):
        try:
            result = crew.kickoff()
            
            # Parse results from the crew output
            # The result contains the final output from all tasks
            final_output = str(result)
            
            # Display results
            st.success("✅ Query processed successfully!")
            st.markdown("---")
            
            # Create columns for better layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📝 Your Query")
                st.write(user_query)
            
            with col2:
                st.subheader("⏰ Timestamp")
                st.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            st.markdown("---")
            
            # Display the final output
            st.subheader("🤖 Agent Responses")
            st.write(final_output)
            
            st.markdown("---")
            st.success("💾 All responses have been saved to answers.txt")
            
            # Provide download option
            if os.path.exists("answers.txt"):
                with open("answers.txt", "r") as f:
                    file_content = f.read()
                st.download_button(
                    label="📥 Download answers.txt",
                    data=file_content,
                    file_name="answers.txt",
                    mime="text/plain"
                )
        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Make sure your API keys are set in environment variables:")
            st.code("OPENAI_API_KEY and SERPER_API_KEY")

elif submitted and not user_query:
    st.warning("⚠️ Please enter a query before submitting!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <small>Customer Support System powered by CrewAI & Streamlit | Weekly Buildathon</small>
</div>
""", unsafe_allow_html=True)
