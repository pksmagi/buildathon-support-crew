# 🚀 Quick Start Guide - Customer Support Crew

**Get running in 5 minutes** ⚡

---

## ✅ Prerequisites

- Python 3.8+ installed
- OpenAI API key (from https://platform.openai.com)
- Serper API key (from https://serper.dev)
- Git

---

## 1️⃣ Clone & Navigate

```bash
git clone https://github.com/pksmagi/buildathon-support-crew.git
cd buildathon-support-crew
```

---

## 2️⃣ Create Virtual Environment

```bash
# Create
python -m venv venv

# Activate - Windows PowerShell
venv\Scripts\Activate.ps1

# Activate - Windows Command Prompt
venv\Scripts\activate.bat

# Activate - macOS/Linux
source venv/bin/activate
```

You'll see `(venv)` at your prompt when activated.

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Takes ~2 minutes** ⏱️

---

## 4️⃣ Set Environment Variables

### Windows PowerShell
```powershell
$env:OPENAI_API_KEY="sk-your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
```

### Windows Command Prompt
```cmd
set OPENAI_API_KEY=sk-your-openai-key
set SERPER_API_KEY=your-serper-key
```

### macOS/Linux
```bash
export OPENAI_API_KEY="sk-your-openai-key"
export SERPER_API_KEY="your-serper-key"
```

---

## 5️⃣ Run the App

```bash
streamlit run app.py
```

🎉 **Opens automatically in your browser at http://localhost:8501**

---

## 6️⃣ Use the App

1. **Type a question** (e.g., "How do I reset my password?")
2. **Click "Submit"**
3. **See two answers**:
   - Knowledge Agent: From training data
   - Web Search Agent: Current web info
4. **Answers saved** to `answers.txt`

---

## ⛔ Stop the App

```bash
# Press Ctrl + C in terminal
# Then deactivate:
deactivate
```

---

## 🆘 Troubleshooting

### "API keys not found"
- **Windows PowerShell**: Did you set environment variables?
  ```powershell
  $env:OPENAI_API_KEY="your-key"
  ```
- **Make sure to restart Streamlit** after setting environment variables

### "No module named 'crewai'"
```bash
pip install -r requirements.txt
```

### "Connection timeout"
- Check internet connection
- Verify API keys are valid
- Increase timeout if network is slow

### "Streamlit not found"
```bash
pip install streamlit
```

---

## 📁 Project Structure

```
buildathon-support-crew/
├── app.py                    # Main application
├── agents.py                 # 3 agents definition
├── tasks.py                  # 3 tasks definition
├── prompts.py                # LLM prompts
├── ui.py                     # Streamlit UI
├── requirements.txt          # Dependencies
└── answers.txt               # Saved answers (auto-created)
```

---

## 📚 Documentation

- **[VERIFICATION_REPORT.md](./VERIFICATION_REPORT.md)** - Complete requirements checklist
- **[README.md](./README.md)** - Full setup guide
- **[PROMPTS_DOCUMENTATION.md](./PROMPTS_DOCUMENTATION.md)** - Prompt engineering details
- **[SAMPLE_OUTPUT.md](./SAMPLE_OUTPUT.md)** - Example outputs

---

## 🎯 What It Does

| Step | Agent | Does | Output |
|------|-------|------|--------|
| 1 | Knowledge Agent | Answers from training | Answer 1 |
| 2 | Web Search Agent | Searches web + answers | Answer 2 |
| 3 | Entry Agent | Saves both to file | answers.txt |

**All sequential** = Agent 2 sees Agent 1's output = Agent 3 sees both = Perfect context!

---

## ✨ Example Queries

Try these:
- "How do I reset my password?"
- "What are the latest features in Python?"
- "How do I implement OAuth in a web app?"
- "What's the best database for my startup?"
- "How do I optimize my code for performance?"

---

## 🔧 Configuration

Edit [app.py](./app.py) to change:
- Model (GPT-4, GPT-3.5-turbo, etc.)
- Temperature/creativity
- File output location
- UI styling

---

## 🚀 Deploy to Production

This app is ready for:
- **Local development** ✅
- **Team collaboration** ✅
- **Cloud deployment** (Streamlit Cloud, Heroku, AWS)

For deployment, store API keys in secret management (never in .env):
- **Streamlit Cloud**: Store in Secrets
- **AWS**: Use Parameter Store
- **Heroku**: Use Config Vars

---

**Happy building! 🎉**

Questions? See the full [README.md](./README.md) or check [PROMPTS_DOCUMENTATION.md](./PROMPTS_DOCUMENTATION.md)
