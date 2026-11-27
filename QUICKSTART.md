# Quick Start Guide - Windows PowerShell

## Step 1: Navigate to the project folder
```powershell
cd C:\Users\pksma\OneDrive\Desktop\bulidathon\buildathon-support-crew
```

## Step 2: Activate the virtual environment (if not already active)
```powershell
venv\Scripts\Activate.ps1
```

## Step 3: Set your API keys

### Get OpenAI API Key:
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Set it:
```powershell
$env:OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxx"
```

### Get Serper API Key:
1. Go to https://serper.dev
2. Create a free account and get API key
3. Set it:
```powershell
$env:SERPER_API_KEY="xxxxxxxxxxxxx"
```

## Step 4: Run the application
```powershell
streamlit run app.py
```

The app will automatically open in your browser at http://localhost:8501

## Step 5: Stop the app
Press Ctrl + C in the terminal

## Step 6: Deactivate virtual environment
```powershell
deactivate
```

---

## What to expect:
✅ Streamlit interface loads at localhost:8501
✅ Input field for customer queries
✅ Three agents process the query sequentially
✅ Results display in the UI
✅ Answers are saved to answers.txt
✅ Download button to get answers.txt

## Next Steps:
- Customize agent prompts in app.py as needed
- Add more specialized tools beyond web search
- Extend with database integration
- Modify the output format in the Entry Agent
