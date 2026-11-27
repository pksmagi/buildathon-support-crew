# 🤖 Customer Support System - CrewAI + Streamlit

A sequential crew of three AI agents that process customer support queries using the CrewAI framework with a Streamlit user interface.

## ✨ Features

- **Three Sequential Agents:**
  1. **Knowledge Agent** - Answers from training knowledge (no tools)
  2. **Web Agent** - Searches web for current information (SerperDevTool)
  3. **Documentation Agent** - Saves both answers to file (custom @tool)

- **True Sequential Processing** - Each task receives outputs from previous tasks
- **Modular Architecture** - Agents, tasks, tools, and UI in separate modules
- **File Saving** - Automatic record creation with both answers
- **Download Feature** - Users can download generated answers.txt
- **Secure API Handling** - API keys from environment variables only

## 🏗️ Project Structure

```
buildathon-support-crew/
├── app.py              # Main application entry point
├── agents.py           # Agent definitions (3 specialized agents)
├── tasks.py            # Task definitions (3 sequential tasks)
├── tools.py            # Custom CrewAI tools (@tool decorator)
├── ui.py               # Streamlit UI components
├── tests/
│   ├── __init__.py
│   └── test_app.py     # pytest test suite (20+ tests)
├── answers.txt         # Sample output file (auto-generated)
├── requirements.txt    # Python dependencies (includes pytest)
├── .env.example        # API key template
├── .gitignore          # Git ignore patterns
└── README.md          # This file
```

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API Keys

```bash
# macOS / Linux
export OPENAI_API_KEY="your-openai-key"
export SERPER_API_KEY="your-serper-key"

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
```

**Get API Keys:**
- OpenAI: https://platform.openai.com
- Serper: https://serper.dev

### 4. Run Application

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test class
pytest tests/test_app.py::TestAgentConfiguration -v

# Run with coverage
pytest tests/ --cov=.
```

**Test Coverage:**
- ✅ Agent configuration (distinct roles and tools)
- ✅ Task definitions (sequential context passing)
- ✅ File saving functionality (@tool decorator)
- ✅ Tool registration and execution

## 🔧 Architecture Details

### Agents (agents.py)

| Agent | Role | Tools |
|-------|------|-------|
| Knowledge Agent | Knowledge-Based Support Specialist | None (knowledge-only) |
| Web Agent | Web Research Specialist | SerperDevTool (web search) |
| Documentation Agent | Documentation Specialist | save_to_file (@tool) |

**Key Design:**
- Each agent has distinct specialization
- Tools are non-overlapping (no duplicate capabilities)
- Agents are created with `allow_delegation=False` for clarity

### Tasks (tasks.py)

| Task | Input | Agent | Output |
|------|-------|-------|--------|
| Task 1 | User query | Knowledge Agent | Knowledge-based answer |
| Task 2 | Task 1 output | Web Agent | Web-based answer |
| Task 3 | Task 1 + Task 2 | Documentation Agent | Saved file + confirmation |

**Context Passing:**
- Task 2 description explicitly states: "You will receive the knowledge-based answer from the previous task"
- Task 3 description explicitly states: "You will receive outputs from both previous tasks"
- Sequential process ensures strict execution order: Task 1 → Task 2 → Task 3

### Tools (tools.py)

**save_to_file @tool:**
- Proper CrewAI @tool decorator (not plain Python I/O)
- Takes: query, assistant_answer, web_answer
- Returns: Confirmation message with timestamp
- Saves to: `answers.txt`

### UI (ui.py)

Modular Streamlit components:
- `configure_page()` - Page settings
- `show_info()` - How-it-works section
- `get_user_query()` - Form input
- `show_processing()` - Processing status
- `show_results()` - Query results and download
- `show_error()` - Error handling
- `show_warning()` - Input validation
- `show_footer()` - Page footer

## 📋 Example Usage

**Input:**
```
How do I reset my password?
```

**Output:** `answers.txt` contains:
```
=====================================
CUSTOMER SUPPORT RECORD
=====================================

TIMESTAMP: 2024-11-27 11:15:30

CUSTOMER QUERY:
How do I reset my password?

---

KNOWLEDGE-BASED ANSWER:
To reset your password, follow these steps...

---

WEB RESEARCH ANSWER:
Based on current web information, password reset best practices...

=====================================
```

## 🛠️ Technologies

- **CrewAI** - Multi-agent framework with sequential processes
- **Streamlit** - Web UI framework
- **OpenAI** - LLM for agent reasoning
- **Serper** - Web search API
- **pytest** - Testing framework
- **Python 3.8+** - Runtime

## ✅ What Makes This Work

1. **True Sequential Execution** - `Process.sequential` ensures strict order
2. **Explicit Context Passing** - Task descriptions clearly reference previous outputs
3. **Proper Tool Usage** - CrewAI @tool decorator, not plain Python code
4. **Modular Design** - Agents, tasks, tools, and UI separated into modules
5. **Real Tests** - pytest suite verifies all critical functionality
6. **Sample Output** - `answers.txt` demonstrates expected output format

## 🔒 Security

- ✅ API keys from environment variables only
- ✅ No hardcoded secrets in code
- ✅ No personal paths or sensitive data in git
- ✅ `.gitignore` excludes venv/ and local files
- ✅ `.env.example` shows required keys

## 📝 Environment Variables

Required:
```
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key
```

## 🎓 Buildathon

Built for the **Weekly Buildathon** - Customer Support System Challenge

**Difficulty:** Medium | **Tools:** Python, CrewAI, Streamlit | **Status:** ✅ Complete
