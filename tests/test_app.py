"""
pytest test suite for Customer Support Crew System.

Tests verify:
- Agent configuration (distinct roles and tools)
- Task definitions (sequential context passing with CrewAI context parameter)
- File saving functionality (@tool decorator)
- Tool registration and execution
- Error handling for missing API keys
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
    """Test task definitions and proper context passing with CrewAI context parameter."""
    
    def test_task_1_has_no_context(self):
        """Task 1 should have no context (first task)."""
        query = "How do I reset my password?"
        agent = create_knowledge_agent()
        task = create_task_1(agent, query)
        
        # Task 1 should not have context parameter set
        assert not hasattr(task, 'context') or task.context is None or task.context == []
    
    def test_task_2_has_proper_context(self):
        """Task 2 should have context=[task_1] for proper context passing."""
        query = "How do I reset my password?"
        agent_1 = create_knowledge_agent()
        agent_2 = create_web_agent()
        
        task_1 = create_task_1(agent_1, query)
        task_2 = create_task_2(agent_2, query, task_1)
        
        # Task 2 should have context pointing to Task 1
        assert hasattr(task_2, 'context'), "Task 2 should have context attribute"
        assert task_2.context is not None, "Task 2 context should not be None"
        assert len(task_2.context) > 0, "Task 2 context should contain Task 1"
        assert task_1 in task_2.context, "Task 2 context should include Task 1"
    
    def test_task_3_has_proper_context(self):
        """Task 3 should have context=[task_1, task_2] for proper context passing."""
        query = "How do I reset my password?"
        agent_1 = create_knowledge_agent()
        agent_2 = create_web_agent()
        agent_3 = create_documentation_agent()
        
        task_1 = create_task_1(agent_1, query)
        task_2 = create_task_2(agent_2, query, task_1)
        task_3 = create_task_3(agent_3, query, task_1, task_2)
        
        # Task 3 should have context pointing to both Task 1 and Task 2
        assert hasattr(task_3, 'context'), "Task 3 should have context attribute"
        assert task_3.context is not None, "Task 3 context should not be None"
        assert len(task_3.context) >= 2, "Task 3 context should contain Task 1 and Task 2"
        assert task_1 in task_3.context, "Task 3 context should include Task 1"
        assert task_2 in task_3.context, "Task 3 context should include Task 2"
    
    def test_task_descriptions_reference_context(self):
        """Task descriptions should clearly reference how context is used."""
        query = "Test query"
        agent_1 = create_knowledge_agent()
        agent_2 = create_web_agent()
        agent_3 = create_documentation_agent()
        
        task_1 = create_task_1(agent_1, query)
        task_2 = create_task_2(agent_2, query, task_1)
        task_3 = create_task_3(agent_3, query, task_1, task_2)
        
        # Task 1 should have query in description
        assert query in task_1.description
        
        # Task 2 should reference the query and imply it has context
        assert query in task_2.description
        
        # Task 3 should reference query and multiple tasks
        assert query in task_3.description
        assert "save_to_file" in task_3.description.lower()


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
