"""
Streamlit UI for the Customer Support Crew.

Provides the web interface for submitting queries and viewing results.
Includes comprehensive error handling for API failures and missing configuration.
"""

import streamlit as st
import os
from datetime import datetime


def configure_page():
    """Configure Streamlit page settings."""
    st.set_page_config(page_title="Customer Support Crew", layout="wide")
    st.title("🤖 Customer Support System - CrewAI Powered")
    st.markdown("---")


def show_info():
    """Show how the system works."""
    with st.expander("ℹ️ How it works", expanded=False):
        st.markdown("""
        **Sequential Task Execution with Context Passing:**
        
        1. **Task 1 (Knowledge Agent)**: Answers from training knowledge
           - Input: User query
           - Output: Knowledge-based answer
        
        2. **Task 2 (Web Agent)**: Searches web with context from Task 1
           - Input: User query + Task 1 output (via context parameter)
           - Output: Web-based answer
        
        3. **Task 3 (Documentation Agent)**: Saves with context from Tasks 1 & 2
           - Input: User query + Task 1 output + Task 2 output (via context parameters)
           - Output: Saved file + confirmation
        
        **Implementation Details:**
        - Tasks use CrewAI `context=[previous_tasks]` parameter for proper context injection
        - Each agent has distinct tools (no overlap)
        - Sequential process ensures strict execution order
        """)


def get_user_query() -> tuple[str, bool]:
    """Get query from user via form. Returns (query, submitted)."""
    with st.form("query_form"):
        user_query = st.text_area(
            "Enter your customer support query:",
            placeholder="e.g., How do I reset my password?",
            height=100
        )
        submitted = st.form_submit_button("🚀 Submit Query", use_container_width=True)
    
    return user_query, submitted


def show_processing():
    """Show processing status."""
    st.markdown("---")
    st.info("⏳ Processing your query through the crew sequentially...")
    st.info("Task 1: Knowledge Agent processing → Task 2: Web Agent processing → Task 3: Documentation Agent saving...")


def show_results(result: str, user_query: str):
    """Display crew results."""
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
        try:
            with open("answers.txt", "r") as f:
                file_content = f.read()
            st.success("💾 Support record saved to answers.txt")
            st.download_button(
                label="📥 Download answers.txt",
                data=file_content,
                file_name="answers.txt",
                mime="text/plain"
            )
        except IOError as e:
            st.error(f"❌ Failed to read answers.txt: {str(e)}")
    else:
        st.warning("⚠️ answers.txt was not created by the documentation agent")


def show_error(error_message: str, error_type: str = "General"):
    """Display error message with context."""
    st.error(f"❌ {error_type} Error: {error_message}")
    
    if "API" in error_type or "key" in error_message.lower():
        st.error("🔑 **Missing API Keys**")
        st.code("""
# Set environment variables before running:

# macOS / Linux:
export OPENAI_API_KEY="your-openai-key"
export SERPER_API_KEY="your-serper-key"
streamlit run app.py

# Windows (PowerShell):
$env:OPENAI_API_KEY="your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
streamlit run app.py
        """)
        st.info("Get API keys:")
        st.markdown("- **OpenAI**: https://platform.openai.com/api-keys")
        st.markdown("- **Serper**: https://serper.dev/api")
    
    elif "web search" in error_message.lower() or "serper" in error_message.lower():
        st.error("🌐 **Web Search Failed**")
        st.markdown("The web search API (Serper) encountered an error:")
        st.markdown(f"- Verify SERPER_API_KEY is set correctly")
        st.markdown(f"- Check if Serper API quota is exceeded")
        st.markdown(f"- Error details: {error_message}")
    
    elif "timeout" in error_message.lower():
        st.error("⏱️ **Request Timeout**")
        st.markdown("The API request took too long:")
        st.markdown(f"- Try a shorter query")
        st.markdown(f"- Check your internet connection")
        st.markdown(f"- Error details: {error_message}")
    
    else:
        st.markdown(f"**Details**: {error_message}")


def show_warning():
    """Display warning for empty query."""
    st.warning("⚠️ Please enter a query before submitting!")


def show_footer():
    """Display page footer."""
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center'><small>Customer Support System | CrewAI + Streamlit | Sequential Multi-Agent Architecture</small></div>",
        unsafe_allow_html=True
    )

