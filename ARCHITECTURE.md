# 🏗️ Architecture - Customer Support Crew

**Professional system architecture designed with enterprise best practices**

---

## 🏢 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     STREAMLIT USER INTERFACE                     │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │                                                              │  │
│  │  Title: Customer Support System                             │  │
│  │  Input:  [User enters their query here...]                 │  │
│  │  Button: [Submit]                                           │  │
│  │                                                              │  │
│  │  ─────────────────────────────────────────────────────────  │  │
│  │  Output:                                                     │  │
│  │  ┌─ KNOWLEDGE AGENT ANSWER ──────────────────────────────┐ │  │
│  │  │ From training knowledge...                              │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  │  ┌─ WEB SEARCH AGENT ANSWER ─────────────────────────────┐ │  │
│  │  │ From current web information...                        │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  │  ✅ Saved to answers.txt                                   │  │
│  │                                                              │  │
│  └────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    app.py (Main Entry Point)
                         ↓↓↓
         ┌────────────────┼────────────────┐
         ↓                ↓                 ↓
    agents.py         tasks.py          prompts.py
      (Agents)        (Tasks)            (LLM Prompts)
         ↓                ↓                 ↓
    ┌────────────────────────────────────────────┐
    │           CrewAI Framework                  │
    │      (Process.sequential)                  │
    └────────────────────────────────────────────┘
         ↓↓↓
    ┌─────────────────────────────────────────────────────┐
    │ CREW EXECUTION - SEQUENTIAL PROCESS                 │
    │                                                       │
    │ PHASE 1: KNOWLEDGE AGENT                            │
    │ ├─ Receives: user_query                             │
    │ ├─ Prompt: prompts.get_task_1_prompt()             │
    │ ├─ Tool: None (knowledge only)                      │
    │ └─ Output: knowledge_answer (Answer 1)              │
    │                                                       │
    │ PHASE 2: WEB SEARCH AGENT                           │
    │ ├─ Receives: user_query + knowledge_answer          │
    │ ├─ Prompt: prompts.get_task_2_prompt()             │
    │ ├─ Tool: SerperDevTool (web search)                 │
    │ ├─ Compares: Shows differences from Answer 1        │
    │ └─ Output: web_answer (Answer 2)                    │
    │                                                       │
    │ PHASE 3: DOCUMENTATION AGENT                        │
    │ ├─ Receives: user_query + knowledge_answer + web_answer
    │ ├─ Prompt: prompts.get_task_3_prompt()             │
    │ ├─ Tool: save_to_file (creates answers.txt)        │
    │ ├─ Synthesizes: Combines both perspectives          │
    │ └─ Output: file_save_confirmation                   │
    │                                                       │
    └─────────────────────────────────────────────────────┘
              ↓
         Result Object (Contains all outputs)
              ↓
           ui.py (Streamlit Display)
              ↓
        Display both answers to user
```

---

## 📦 Component Architecture

### 1. **app.py** - Main Application Controller
```
app.py
├── Import modules (agents, tasks, ui, prompts)
├── validate_api_keys()
│   ├─ Check OPENAI_API_KEY
│   └─ Check SERPER_API_KEY
├── main()
│   ├─ configure_page() [ui.py]
│   ├─ show_info() [ui.py]
│   ├─ get_user_query() [ui.py]
│   ├─ Create Agents
│   │   ├─ create_knowledge_agent() [agents.py]
│   │   ├─ create_web_agent() [agents.py]
│   │   └─ create_documentation_agent() [agents.py]
│   ├─ Create Tasks
│   │   ├─ create_task_1() [tasks.py]
│   │   ├─ create_task_2() [tasks.py]
│   │   └─ create_task_3() [tasks.py]
│   ├─ Create Crew (sequential process)
│   ├─ Execute: crew.kickoff()
│   └─ show_results() [ui.py]
```

### 2. **agents.py** - Agent Definitions
```
agents.py
├── create_knowledge_agent()
│   ├─ Role: "Knowledge-Based Support Specialist"
│   ├─ Goal: Answer from training knowledge
│   ├─ Backstory: 15+ years experience
│   ├─ Tools: None
│   └─ Return: Agent object
│
├── create_web_agent()
│   ├─ Role: "Modern Technology Specialist"
│   ├─ Goal: Research current information
│   ├─ Backstory: 15+ years research
│   ├─ Tools: [SerperDevTool]
│   └─ Return: Agent object
│
└── create_documentation_agent()
    ├─ Role: "Documentation Expert"
    ├─ Goal: Synthesize and save
    ├─ Backstory: 15+ years documentation
    ├─ Tools: [save_to_file]
    └─ Return: Agent object
```

### 3. **tasks.py** - Task Definitions
```
tasks.py
├── create_task_1(agent, query)
│   ├─ Description: "Answer the query from knowledge"
│   ├─ Expected Output: "Comprehensive knowledge-based answer"
│   ├─ Agent: Knowledge Agent
│   └─ Context: query
│
├── create_task_2(agent, query, task_1)
│   ├─ Description: "Search web and provide answer"
│   ├─ Expected Output: "Current web-sourced answer"
│   ├─ Agent: Web Search Agent
│   └─ Context: query + task_1 output
│
└── create_task_3(agent, query, task_1, task_2)
    ├─ Description: "Save everything to file"
    ├─ Expected Output: "File saved confirmation"
    ├─ Agent: Documentation Agent
    └─ Context: query + task_1 + task_2
```

### 4. **prompts.py** - LLM Prompt Engineering
```
prompts.py
├── get_task_1_prompt(query)
│   ├─ Role definition (15+ years)
│   ├─ Explicit constraints (knowledge only)
│   ├─ 5-step reasoning framework
│   ├─ 7 quality criteria
│   ├─ 7-part output structure
│   └─ Return: 400-600 token prompt
│
├── get_task_2_prompt(query, answer_1)
│   ├─ Role definition (15+ years research)
│   ├─ Research strategy (2-3 sources)
│   ├─ 5 source evaluation criteria
│   ├─ Comparative analysis instructions
│   ├─ 7-part output structure
│   └─ Return: 400-600 token prompt
│
└── get_task_3_prompt(query, answer_1, answer_2)
    ├─ Role definition (15+ years documentation)
    ├─ Synthesis guidance
    ├─ Quality assurance checklist
    ├─ File save instructions
    ├─ 7-part output structure
    └─ Return: 400-600 token prompt
```

### 5. **ui.py** - User Interface Components
```
ui.py
├── configure_page()
│   ├─ Set page config
│   ├─ CSS styling
│   └─ Layout configuration
│
├── show_info()
│   ├─ Display title
│   ├─ Show description
│   └─ Display instructions
│
├── get_user_query()
│   ├─ Input text box
│   ├─ Submit button
│   └─ Return: (query, submitted_flag)
│
├── show_processing()
│   ├─ Display spinner
│   └─ Show "Processing..." message
│
├── show_results(result, query)
│   ├─ Display query
│   ├─ Show Knowledge Agent answer
│   ├─ Show Web Search Agent answer
│   ├─ Show file save confirmation
│   └─ Provide download link
│
├── show_error(message, error_type)
│   ├─ Display error message
│   ├─ Show error type (API, Network, etc.)
│   └─ Provide recovery steps
│
└── show_footer()
    └─ Display footer information
```

### 6. **tools.py** - CrewAI Tools
```
tools.py
├── SerperDevTool
│   ├─ Name: "search_internet"
│   ├─ Description: "Search the internet using Serper API"
│   ├─ Input: query string
│   └─ Output: search results
│
└── save_to_file
    ├─ Name: "save_to_file"
    ├─ Description: "Save content to answers.txt"
    ├─ Input: query, answer1, answer2
    └─ Output: file path confirmation
```

---

## 🔄 Data Flow

```
Step 1: User Input
─────────────────
User enters query in Streamlit UI
         ↓
Query: "How do I reset my password?"
         ↓

Step 2: Validation
─────────────────
Check API keys present?
  ├─ No → Show error, exit
  └─ Yes → Continue
         ↓

Step 3: Create Crew
─────────────────
Create 3 agents with professional prompts
Create 3 tasks with context passing
Bundle into Crew (sequential process)
         ↓

Step 4: Execute Task 1 (Knowledge Agent)
─────────────────────────────────────────
Input: query = "How do I reset my password?"
Prompt: "You are an Expert Support Specialist..."
         ↓
LLM Processing (OpenAI)
         ↓
Output: knowledge_answer (Answer 1)
Example: "To reset your password: 1) Go to login 2) Click 'Forgot Password'..."
         ↓

Step 5: Execute Task 2 (Web Search Agent)
──────────────────────────────────────────
Input: 
  - query = "How do I reset my password?"
  - context = knowledge_answer
  
Prompt: "You are a Technology Specialist with 15+ years research experience..."
         ↓
Step 5a: Search Web
  Tool: SerperDevTool("How do I reset my password?")
  Result: Top search results about password resets
         ↓
LLM Processing (analyzes results, compares with knowledge)
         ↓
Output: web_answer (Answer 2)
Example: "In 2024, modern platforms use: OAuth, 2FA, email verification..."
         ↓

Step 6: Execute Task 3 (Documentation Agent)
─────────────────────────────────────────────
Input:
  - query = "How do I reset my password?"
  - context = knowledge_answer + web_answer
  
Prompt: "You are a Documentation Expert with 15+ years experience..."
         ↓
Step 6a: Synthesize
  Combine both perspectives
  Create unified narrative
         ↓
Step 6b: Save to File
  Tool: save_to_file()
  Content: query + knowledge_answer + web_answer
  File: answers.txt (with formatting)
         ↓
Output: file_save_confirmation
Example: "✅ Saved to answers.txt"
         ↓

Step 7: Display Results
──────────────────────
Streamlit shows:
  ✅ Original query
  ✅ Knowledge Agent answer
  ✅ Web Search Agent answer
  ✅ File save confirmation
  ✅ Download link to answers.txt
         ↓

COMPLETE
```

---

## 💾 File I/O

### Input Files
- ❌ No input files required
- ✅ Configuration: Environment variables only

### Output Files
```
answers.txt (auto-created in project directory)

Format:
================================================================================
Customer Support Query - Saved on [TIMESTAMP]
================================================================================

QUERY:
[User's original query]

================================================================================
ANSWER 1 - KNOWLEDGE AGENT (From Training Knowledge):
[Knowledge-based response from Agent 1]

================================================================================
ANSWER 2 - WEB SEARCH AGENT (Current Web Information):
[Web-sourced response from Agent 2]

================================================================================
```

---

## 🔐 Security Architecture

```
                    API KEYS
                       ↓
        ┌──────────────┴──────────────┐
        ↓                             ↓
   OPENAI_API_KEY            SERPER_API_KEY
        ↓                             ↓
   os.getenv()                   os.getenv()
        ↓                             ↓
   ┌────────────────────────────────────┐
   │   validate_api_keys()              │
   │   ├─ Check present?                │
   │   ├─ Show error if missing         │
   │   └─ Exit if invalid               │
   └────────────────────────────────────┘
        ↓
   CrewAI Agents (via OpenAI library)
   ↓
   Web Search (via Serper API)
   
   ✅ Security Measures:
   • Never printed to console
   • Never logged to files
   • Never committed to git (.gitignore)
   • Environment variable only
   • Validated on startup
   • Error messages don't expose keys
```

---

## ⚙️ Configuration Management

```
Environment Variables (Required)
├─ OPENAI_API_KEY
│  ├─ Source: https://platform.openai.com
│  ├─ Format: sk-...
│  └─ Used by: OpenAI API
│
└─ SERPER_API_KEY
   ├─ Source: https://serper.dev
   ├─ Format: API key
   └─ Used by: Web search

Command Line Arguments
└─ None (uses Streamlit defaults)

Configuration Files
└─ .env.example (template only, never committed)

Hardcoded Defaults
├─ Model: gpt-3.5-turbo (can change in code)
├─ Temperature: 0.7
├─ Max retries: 2
└─ Timeout: 30 seconds
```

---

## 🧪 Error Handling Architecture

```
Error Detection Points:

1. API Key Validation (startup)
   └─ Missing → Show error, exit

2. Agent Creation
   └─ Failure → Catch exception, show error

3. Task Execution
   ├─ OpenAI timeout → Catch, show timeout error
   ├─ Serper failure → Catch, show search error
   └─ Invalid response → Catch, show format error

4. File Operations
   ├─ Permission denied → Catch, show permission error
   └─ Disk full → Catch, show storage error

5. User Input
   ├─ Empty query → Warn user, don't execute
   └─ Very long query → Truncate or warn

Error Response Format:
   ┌─────────────────────────────────────┐
   │ ❌ ERROR                             │
   │ Type: [Configuration/API/Network]   │
   │ Message: [User-friendly message]    │
   │ Solution: [How to fix]              │
   └─────────────────────────────────────┘
```

---

## 🎯 Deployment Architecture

```
Local Development
├─ Python 3.8+ installed
├─ pip install -r requirements.txt
├─ Set environment variables
└─ streamlit run app.py
   └─ Runs at http://localhost:8501

Cloud Deployment (Ready for)
├─ Streamlit Cloud
│  ├─ Push to GitHub
│  ├─ Connect repository
│  └─ Set secrets in Streamlit dashboard
│
├─ Docker
│  ├─ Build image
│  ├─ Set environment variables
│  └─ Run container
│
├─ AWS/Azure/GCP
│  └─ Use cloud secret management
│      (Secrets Manager, Key Vault, etc.)
│
└─ Kubernetes
   ├─ ConfigMaps for settings
   ├─ Secrets for API keys
   └─ Pods run container
```

---

## 📊 Performance Considerations

```
Execution Timeline:

User Input
    ↓ (immediate)
API Validation
    ↓ (<100ms)
Agent Creation
    ↓ (<1s)
Task 1: Knowledge Agent
    ↓ (~5-15s) ← OpenAI API call
Task 2: Web Search Agent
    ↓ (~8-20s) ← OpenAI + Serper API calls
Task 3: Documentation Agent
    ↓ (~2-5s) ← File write + formatting
Display Results
    ↓ (<100ms)
Complete

Total: ~15-50 seconds (depends on API response times)

Optimization Opportunities:
✓ Parallel agent execution (would require Process.hierarchical)
✓ Response caching for similar queries
✓ Streaming responses to UI
✓ Database for query/response history
✓ Batch processing for multiple queries
```

---

## ✅ Quality Assurance Architecture

```
Code Quality Checks
├─ Type hints (Python 3.5+)
├─ Docstrings (all functions)
├─ PEP 8 compliance
├─ No hard-coded secrets
└─ Error handling coverage

Testing Architecture
├─ Unit Tests
│  ├─ Test agent creation
│  ├─ Test task execution
│  ├─ Test prompt formatting
│  └─ Test file operations
│
├─ Integration Tests
│  ├─ Test crew execution
│  ├─ Test full pipeline
│  └─ Test file output format
│
└─ Manual Tests
   ├─ Normal queries
   ├─ Edge cases
   ├─ Error conditions
   └─ Performance verification

Verification Checklist
✅ All 3 agents created
✅ Sequential execution verified
✅ Both answers displayed
✅ File saved correctly
✅ API keys handled securely
✅ Error messages helpful
✅ Performance acceptable
✅ Code quality professional
```

---

**Professional Architecture Built for Scale** 🚀
