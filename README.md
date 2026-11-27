# 🤖 Customer Support System - CrewAI Powered

A production-ready customer support system using **CrewAI** and **Streamlit** with three sequential agents:
1. **Knowledge-Based Assistant** - Answers from training data only
2. **Web Research Specialist** - Searches current web information
3. **Documentation Specialist** - Saves interactions using CrewAI tools

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set API Keys
```powershell
# Windows PowerShell
$env:OPENAI_API_KEY="your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
```

### 3. Run
```bash
streamlit run app.py
```

Opens at: `http://localhost:8501`

## Architecture

**True Sequential Process:**
- Task 1: Knowledge-based agent answers query (no tools)
- Task 2: Web agent searches for current info (Serper tool)
- Task 3: Documentation agent saves both answers (Custom file tool)

Each agent has distinct specialized roles and capabilities.

## Features

✅ **Distinct Agent Roles** - Each agent specialized with unique tools
✅ **True Sequential Processing** - Tasks run one after another
✅ **Custom CrewAI Tool** - File saving via tool, not plain Python
✅ **Web Search Integration** - Serper API for current information
✅ **Streamlit UI** - Clean interface for queries
✅ **Automatic Documentation** - Results saved to `answers.txt`
✅ **Environment Security** - API keys from environment only

## API Keys Required

- **OpenAI**: https://platform.openai.com/api-keys (free trial)
- **Serper**: https://serper.dev (free tier)

## Project Structure
```
buildathon-support-crew/
├── app.py                    # Main application
├── requirements.txt          # Dependencies
├── .env.example             # API key template
├── README.md                # This file
└── answers.txt              # Generated (git-ignored)
```

## Technologies

- **CrewAI** - Multi-agent orchestration with sequential processing
- **Streamlit** - Web application interface  
- **OpenAI GPT** - Language model
- **SerperDev** - Web search API
- **Python 3.8+**
