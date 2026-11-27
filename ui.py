"""
Streamlit UI for the Customer Support Crew.

Provides the web interface for submitting queries and viewing results.
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
        **True Sequential Process:**
        1. **Task 1**: Knowledge Agent answers from training data
        2. **Task 2**: Web Agent searches web (receives Task 1 output)
        3. **Task 3**: Documentation Agent saves both (receives Task 1 + Task 2 outputs)
        
        Each task builds on previous results through proper context passing.
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
        with open("answers.txt", "r") as f:
            file_content = f.read()
        st.success("💾 Support record saved to answers.txt")
        st.download_button(
            label="📥 Download answers.txt",
            data=file_content,
            file_name="answers.txt",
            mime="text/plain"
        )


def show_error(error: str):
    """Display error message."""
    st.error(f"❌ Error: {str(error)}")
    st.info("Required: OPENAI_API_KEY and SERPER_API_KEY environment variables")


def show_warning():
    """Display warning for empty query."""
    st.warning("⚠️ Please enter a query!")


def show_footer():
    """Display page footer."""
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center'><small>Customer Support System | CrewAI + Streamlit</small></div>",
        unsafe_allow_html=True
    )
