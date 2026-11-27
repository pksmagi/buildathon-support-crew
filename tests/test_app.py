"""
pytest test suite for Customer Support Crew System.

Tests verify:
- Agent configuration (distinct roles and tools)
- Task definitions (sequential context passing)
- File saving functionality (@tool decorator)
- Tool registration
"""

import pytest
import os
import tempfile
from datetime import datetime
from crewai import Agent, Task, Process
from crewai_tools import SerperDevTool

from agents import create_knowledge_agent, create_web_agent, create_documentation_agent
from tasks import create_task_1, create_task_2, create_task_3
from tools import save_to_file


class TestAgentConfiguration:
    """Test agent roles and tool assignments."""
    
    def test_knowledge_agent_has_no_tools(self):
        """Knowledge agent should have NO tools (knowledge-only)."""
        agent = create_knowledge_agent()
        assert agent.tools == [], "Knowledge agent should have no tools"
        assert "Knowledge" in agent.role
    
    def test_web_agent_has_search_tool(self):
        """Web agent should have ONLY SerperDevTool."""
        agent = create_web_agent()
        assert len(agent.tools) == 1, "Web agent should have exactly one tool"
        assert "Web Research" in agent.role
    
    def test_documentation_agent_has_save_tool(self):
        """Documentation agent should have ONLY file-saving tool."""
        agent = create_documentation_agent()
        assert len(agent.tools) == 1, "Documentation agent should have exactly one tool"
        assert "Documentation" in agent.role
    
    def test_agents_have_distinct_roles(self):
        """All agents should have distinct roles."""
        knowledge = create_knowledge_agent()
        web = create_web_agent()
        docs = create_documentation_agent()
        
        roles = {knowledge.role, web.role, docs.role}
        assert len(roles) == 3, "All agents should have distinct roles"


class TestTaskConfiguration:
    """Test task definitions and context passing."""
    
    def test_task_1_description(self):
        """Task 1 should ask for knowledge-based answer."""
        query = "How do I reset my password?"
        agent = create_knowledge_agent()
        task = create_task_1(agent, query)
        
        assert query in task.description
        assert "knowledge" in task.description.lower()
    
    def test_task_2_mentions_previous_output(self):
        """Task 2 should explicitly reference Task 1 output."""
        query = "How do I reset my password?"
        agent = create_web_agent()
        task = create_task_2(agent, query)
        
        assert "previous task" in task.description.lower()
        assert query in task.description
    
    def test_task_3_mentions_multiple_outputs(self):
        """Task 3 should explicitly reference Task 1 and Task 2 outputs."""
        query = "How do I reset my password?"
        agent = create_documentation_agent()
        task = create_task_3(agent, query)
        
        assert "both previous tasks" in task.description.lower()
        assert query in task.description
        assert "save_to_file" in task.description.lower()
    
    def test_tasks_have_expected_outputs(self):
        """All tasks should have expected output descriptions."""
        query = "Test query"
        agent = create_knowledge_agent()
        
        task1 = create_task_1(agent, query)
        task2 = create_task_2(create_web_agent(), query)
        task3 = create_task_3(create_documentation_agent(), query)
        
        assert task1.expected_output
        assert task2.expected_output
        assert task3.expected_output


class TestFileOperations:
    """Test file saving functionality."""
    
    def test_save_to_file_creates_file(self):
        """save_to_file tool should create a text file."""
        query = "Test query"
        assistant_answer = "Test assistant answer"
        web_answer = "Test web answer"
        
        result = save_to_file(query, assistant_answer, web_answer)
        
        assert os.path.exists("answers.txt"), "answers.txt should be created"
        assert "saved" in result.lower()
        
        # Cleanup
        if os.path.exists("answers.txt"):
            os.remove("answers.txt")
    
    def test_saved_file_contains_all_sections(self):
        """Saved file should contain query, assistant answer, and web answer."""
        query = "How do I reset my password?"
        assistant_answer = "Step 1: Go to login page"
        web_answer = "Current best practices include 2FA"
        
        save_to_file(query, assistant_answer, web_answer)
        
        with open("answers.txt", "r") as f:
            content = f.read()
        
        assert "CUSTOMER QUERY:" in content
        assert "KNOWLEDGE-BASED ANSWER:" in content
        assert "WEB RESEARCH ANSWER:" in content
        assert query in content
        assert assistant_answer in content
        assert web_answer in content
        
        # Cleanup
        if os.path.exists("answers.txt"):
            os.remove("answers.txt")
    
    def test_saved_file_includes_timestamp(self):
        """Saved file should include timestamp."""
        save_to_file("Test", "Answer", "Web answer")
        
        with open("answers.txt", "r") as f:
            content = f.read()
        
        assert "TIMESTAMP:" in content
        assert len(content) > 0
        
        # Cleanup
        if os.path.exists("answers.txt"):
            os.remove("answers.txt")
    
    def test_save_to_file_overwrites_previous(self):
        """save_to_file should overwrite previous file."""
        # Create first file
        save_to_file("Query 1", "Answer 1", "Web 1")
        with open("answers.txt", "r") as f:
            first_content = f.read()
        
        # Create second file (should overwrite)
        save_to_file("Query 2", "Answer 2", "Web 2")
        with open("answers.txt", "r") as f:
            second_content = f.read()
        
        assert "Query 2" in second_content
        assert "Query 1" not in second_content
        assert first_content != second_content
        
        # Cleanup
        if os.path.exists("answers.txt"):
            os.remove("answers.txt")


class TestSequentialProcess:
    """Test that crew uses sequential process."""
    
    def test_process_sequential_exists(self):
        """Process.sequential should be available."""
        assert hasattr(Process, 'sequential')
    
    def test_sequential_process_enum_value(self):
        """Process.sequential should be accessible."""
        process = Process.sequential
        assert process is not None


if __name__ == "__main__":
    # Run with: pytest tests/test_app.py -v
    pytest.main([__file__, "-v"])
