# 📊 Project Architecture & File Flow

## Application Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                   USER OPENS BROWSER                        │
│              http://localhost:8501                           │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
        ┌────────────────────────────────┐
        │   STREAMLIT UI                 │
        │  (Rendered by app.py)          │
        │                                │
        │  📝 Input Area                 │
        │  🔘 Submit Button              │
        │  ℹ️  Help Section               │
        └────────────────┬───────────────┘
                         │ User submits query
                         ↓
        ┌────────────────────────────────┐
        │   CREWAI SEQUENTIAL CREW       │
        │                                │
        │  Process Type: Sequential      │
        │  Total Agents: 3               │
        │  Total Tasks: 3                │
        └────────────────┬───────────────┘
                         │
                ┌────────┴────────┐
                │                 │
                ↓                 ↓
    ┌───────────────────┐  ┌──────────────────────┐
    │   TASK 1          │  │   TASK 2             │
    │   ASSISTANT       │  │   WEB SEARCH         │
    │   AGENT           │  │   AGENT              │
    │                   │  │                      │
    │ Direct Answer     │  │ Web Search Answer    │
    │ (No Tools)        │  │ (SerperDev Tool)     │
    │                   │  │                      │
    │ Output: Answer 1  │  │ Output: Answer 2     │
    └────────┬──────────┘  └──────────┬───────────┘
             │                        │
             └────────────┬───────────┘
                          │
                          ↓
            ┌──────────────────────────┐
            │   TASK 3                 │
            │   ENTRY AGENT            │
            │                          │
            │ Receives:                │
            │ - Original Query         │
            │ - Answer 1 (from Task 1) │
            │ - Answer 2 (from Task 2) │
            │                          │
            │ Saves to: answers.txt    │
            │ Returns: Confirmation    │
            └────────────┬─────────────┘
                         │
                         ↓
        ┌────────────────────────────────┐
        │   STREAMLIT UI DISPLAYS         │
        │   RESULTS                       │
        │                                │
        │  ✅ Query Summary              │
        │  ✅ Assistant Answer           │
        │  ✅ Web Search Answer          │
        │  ✅ Timestamp                  │
        │  📥 Download Button            │
        └────────────────────────────────┘
                         │
                         ↓
            ┌──────────────────────────┐
            │  answers.txt Created      │
            │  (In project folder)      │
            └──────────────────────────┘
```

---

## File Structure & Dependencies

```
buildathon-support-crew/
│
├── 🎯 MAIN APPLICATION
│   └── app.py ................................................ (6.4 KB)
│       ├── Imports CrewAI framework
│       ├── Imports Streamlit
│       ├── Imports SerperDevTool
│       ├── Defines 3 Agents
│       ├── Defines 3 Tasks
│       ├── Creates Crew (Sequential)
│       ├── Renders UI
│       └── Handles execution & file I/O
│
├── 📚 DOCUMENTATION (Read in this order)
│   ├── INDEX.md ................ Complete navigation guide (START HERE)
│   ├── QUICKSTART.md ........... 60-second setup guide
│   ├── README.md ............... Complete setup & usage
│   ├── PROJECT_SUMMARY.md ...... Detailed project overview
│   ├── DELIVERABLES.md ......... What's included checklist
│   ├── TEST_SCENARIOS.md ....... Testing guide with examples
│   └── GITHUB_SETUP.md ......... How to push to GitHub
│
├── ⚙️  CONFIGURATION
│   ├── requirements.txt ........ Python dependencies (5 packages)
│   ├── .env.example ............ API key template
│   └── .gitignore .............. Git ignore patterns
│
├── 🐍 PYTHON ENVIRONMENT
│   └── venv/ ................... Virtual environment (created)
│
└── 📝 GENERATED DURING RUN (Git-ignored)
    └── answers.txt ............ Query + answers saved here
```

---

## Dependency Graph

```
app.py
│
├─→ crewai
│   ├─→ Agent class
│   ├─→ Task class
│   ├─→ Crew class
│   └─→ Process.sequential
│
├─→ crewai_tools
│   └─→ SerperDevTool (Web Search)
│
├─→ streamlit
│   ├─→ UI Components (st.*)
│   ├─→ Forms & Buttons
│   └─→ File Download
│
├─→ openai (via crewai)
│   └─→ GPT Model Integration
│
└─→ Environment Variables
    ├─→ OPENAI_API_KEY
    └─→ SERPER_API_KEY
```

---

## Agent Communication Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     USER QUERY                              │
│         "How do I reset my password?"                       │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ↓
        ┌─────────────────────────────────────┐
        │  AGENT 1: ASSISTANT                 │
        │  Role: Customer Support Assistant   │
        │  Tools: None (Knowledge only)       │
        └─────────────────┬───────────────────┘
                          │
                          │ Processes Task 1
                          │
                          ↓
        ┌─────────────────────────────────────┐
        │  OUTPUT 1: ASSISTANT ANSWER         │
        │  "Most password resets require..."  │
        └─────────────────┬───────────────────┘
                          │
                          │ Passed to next task
                          │
                          ↓
        ┌─────────────────────────────────────┐
        │  AGENT 2: WEB SEARCH SPECIALIST     │
        │  Role: Web Search Specialist        │
        │  Tools: SerperDevTool               │
        │                                     │
        │  Receives:                          │
        │  - Original query                   │
        │  - Assistant's output               │
        └─────────────────┬───────────────────┘
                          │
                          │ Performs web search
                          │
                          ↓
        ┌─────────────────────────────────────┐
        │  OUTPUT 2: WEB SEARCH ANSWER        │
        │  "Current methods include: 1..."    │
        └─────────────────┬───────────────────┘
                          │
                          │ Passed to next task
                          │
                          ↓
        ┌─────────────────────────────────────┐
        │  AGENT 3: ENTRY SPECIALIST          │
        │  Role: Data Entry Specialist        │
        │  Tools: File I/O                    │
        │                                     │
        │  Receives:                          │
        │  - Original query                   │
        │  - Output 1 (Assistant)             │
        │  - Output 2 (Web Search)            │
        └─────────────────┬───────────────────┘
                          │
                          │ Writes to file
                          │
                          ↓
        ┌─────────────────────────────────────┐
        │  OUTPUT 3: FILE SAVED               │
        │  "answers.txt has been saved"       │
        └─────────────────┬───────────────────┘
                          │
                          │ Returned to UI
                          │
                          ↓
        ┌─────────────────────────────────────┐
        │  STREAMLIT DISPLAYS                 │
        │  - Query                            │
        │  - Answer 1                         │
        │  - Answer 2                         │
        │  - Download Button                  │
        └─────────────────────────────────────┘
```

---

## Code Organization in app.py

```python
# SECTION 1: Imports & Configuration (Lines 1-15)
import streamlit as st
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# SECTION 2: Streamlit Setup (Lines 17-45)
st.set_page_config(...)
st.title(...)
# UI Components: title, expander, form

# SECTION 3: Query Submission (Lines 47-55)
with st.form("query_form"):
    user_query = st.text_area(...)
    submitted = st.form_submit_button(...)

# SECTION 4: Processing Logic (Lines 57-170)
if submitted and user_query:
    # 4.1: Tool Initialization (Line 60)
    search_tool = SerperDevTool()
    
    # 4.2: Agent Definition (Lines 63-96)
    assistant_agent = Agent(...)      # Agent 1
    web_search_agent = Agent(...)     # Agent 2
    entry_agent = Agent(...)          # Agent 3
    
    # 4.3: Task Definition (Lines 98-121)
    task_1 = Task(...)  # For Agent 1
    task_2 = Task(...)  # For Agent 2
    task_3 = Task(...)  # For Agent 3
    
    # 4.4: Crew Creation (Lines 123-128)
    crew = Crew(
        agents=[...],
        tasks=[...],
        process=Process.sequential  # KEY: Sequential!
    )
    
    # 4.5: Execution (Lines 130-160)
    result = crew.kickoff()
    
    # 4.6: Display Results (Lines 150-170)
    st.success(...)
    st.write(...)

# SECTION 5: Footer (Lines 172+)
st.markdown(...)
```

---

## Environment Variables Flow

```
┌─────────────────────────────────────┐
│  System Environment                 │
│  Windows PowerShell / macOS bash    │
├─────────────────────────────────────┤
│ $env:OPENAI_API_KEY = "sk-..."      │
│ $env:SERPER_API_KEY = "..."         │
└──────────────┬──────────────────────┘
               │
               ↓
        ┌──────────────────┐
        │  Python os       │
        │  os.getenv()     │
        └──────────┬───────┘
                   │
                   ↓
        ┌──────────────────────────┐
        │  CrewAI Framework        │
        │  (Auto-detects from env) │
        │                          │
        │  Uses for:               │
        │  - OpenAI LLM calls      │
        │  - Serper API calls      │
        └──────────────────────────┘
```

---

## Testing & Validation Flow

```
START TEST
    ↓
STEP 1: Activate venv
    ├─ Check: (venv) in prompt
    └─ Continue
        ↓
STEP 2: Set API Keys
    ├─ Check: $env:OPENAI_API_KEY set
    ├─ Check: $env:SERPER_API_KEY set
    └─ Continue
        ↓
STEP 3: Run streamlit run app.py
    ├─ Check: Browser opens
    ├─ Check: Streamlit UI loads
    └─ Continue
        ↓
STEP 4: Enter test query
    ├─ Check: Text enters successfully
    └─ Continue
        ↓
STEP 5: Click Submit
    ├─ Check: Spinner appears
    ├─ Check: "Processing..." message shown
    └─ Wait 10-30 seconds
        ↓
STEP 6: Verify Results
    ├─ Check: Query displayed
    ├─ Check: Answer 1 (Assistant) shown
    ├─ Check: Answer 2 (Web Search) shown
    └─ Continue
        ↓
STEP 7: Check File
    ├─ Check: answers.txt created
    ├─ Check: File contains all 3 items
    ├─ Check: Timestamp included
    └─ Continue
        ↓
STEP 8: Download & Verify
    ├─ Click: Download button
    ├─ Check: File downloads
    ├─ Check: File content correct
    └─ Success!
        ↓
TEST COMPLETE ✅
```

---

## Deployment to GitHub

```
Local Project Folder
        │
        ├─→ git init
        │   └─→ Initialize git repository
        │
        ├─→ git add .
        │   └─→ Stage all files except .gitignore
        │
        ├─→ git commit -m "..."
        │   └─→ Create initial commit
        │
        ├─→ git remote add origin <URL>
        │   └─→ Connect to GitHub
        │
        └─→ git push -u origin main
            └─→ Upload to GitHub
                    │
                    ↓
            GitHub Repository
                    │
                    ├─ app.py
                    ├─ README.md
                    ├─ All Documentation
                    ├─ .gitignore
                    └─ requirements.txt
                    
                    (venv/ and answers.txt NOT uploaded)
```

---

## Project Complete! 🎉

This architecture represents a production-ready customer support system built with industry-standard tools and best practices.

**All components are ready. Ready to run. Ready to submit.**
