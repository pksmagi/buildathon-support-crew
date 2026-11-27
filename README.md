# 🤖 Customer Support System - CrewAI Powered

A customer support system built with **CrewAI** and **Streamlit** that uses three sequential agents to answer customer queries.

## Features

✨ **Three Sequential Agents:**
1. **Assistant Agent** - Answers queries directly from knowledge
2. **Web Search Agent** - Searches the web for current information
3. **Entry Agent** - Saves all interactions to a text file

🎨 **User-Friendly Interface** - Built with Streamlit for easy interaction
💾 **Persistent Records** - All queries and answers saved to `answers.txt`
🔐 **Secure** - API keys loaded from environment variables only

## Setup Instructions

### 1. Prerequisites
- Python 3.8+ installed
- OpenAI API key from [platform.openai.com](https://platform.openai.com/api-keys)
- Serper API key from [serper.dev](https://serper.dev) for web search

### 2. Create Virtual Environment (Windows PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install crewai crewai-tools streamlit
```

### 4. Set Environment Variables (Windows PowerShell)
```powershell
$env:OPENAI_API_KEY="your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
```

**On macOS/Linux:**
```bash
export OPENAI_API_KEY="your-openai-key"
export SERPER_API_KEY="your-serper-key"
```

### 5. Run the Application
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

## How It Works

1. **User enters a query** in the Streamlit interface
2. **Assistant Agent** (Agent 1) answers directly from its knowledge
3. **Web Search Agent** (Agent 2) searches the web and provides additional information
4. **Entry Agent** (Agent 3) saves the query and both answers to `answers.txt`
5. **Results displayed** in the UI with download option for the saved file

## File Structure

```
buildathon-support-crew/
├── app.py                 # Main application file
├── .env.example          # Example environment variables
├── answers.txt           # Generated file with query and responses
├── venv/                 # Virtual environment
└── README.md             # This file
```

## Example Usage

**Input:** "How do I reset my password?"

**Output:**
- Direct answer from Assistant Agent
- Web search results and answer from Web Search Agent
- Both answers saved to `answers.txt`

## Troubleshooting

### "API key not found" error
Make sure you've set both environment variables correctly before running the app.

### "SerperDevTool" error
Ensure you have a valid Serper API key set in the `SERPER_API_KEY` environment variable.

### Agents not responding
Check that your OpenAI API key is valid and has available credits.

## Deactivate Virtual Environment
When finished, deactivate the virtual environment:
```bash
deactivate
```

## Technologies Used

- **CrewAI** - AI agent framework for creating autonomous agents
- **Streamlit** - Web app framework for data apps
- **OpenAI GPT** - Language model for agent intelligence
- **SerperDev** - Web search API integration

## Author
Built for Weekly Buildathon - Customer Support Challenge

---

For more information, visit:
- [CrewAI Documentation](https://docs.crewai.com)
- [Streamlit Documentation](https://docs.streamlit.io)
