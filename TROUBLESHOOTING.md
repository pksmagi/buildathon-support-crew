# 🔧 Troubleshooting Quick Reference

## Common Issues & Solutions

### ❌ "Command not found: streamlit"

**Cause:** Virtual environment not activated

**Solution:**
```powershell
# Windows PowerShell
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

Check if activated: You should see `(venv)` at start of prompt

---

### ❌ "OPENAI_API_KEY not found" or "API key error"

**Cause:** Environment variable not set

**Solution:**
```powershell
# Check if set
echo $env:OPENAI_API_KEY

# If empty, set it
$env:OPENAI_API_KEY="sk-proj-your-actual-key"

# Verify it was set
echo $env:OPENAI_API_KEY
```

**Note:** Environment variables must be set BEFORE running `streamlit run`

---

### ❌ "SERPER_API_KEY not found"

**Cause:** Web search API key not set

**Solution:**
```powershell
# Check if set
echo $env:SERPER_API_KEY

# If empty, set it
$env:SERPER_API_KEY="your-actual-serper-key"

# Verify
echo $env:SERPER_API_KEY
```

**Note:** Get key from https://serper.dev

---

### ❌ App crashes immediately

**Cause:** Missing imports or dependency issue

**Solution:**
1. Check if venv is activated
2. Reinstall dependencies:
```powershell
pip install crewai crewai-tools streamlit
```
3. Check Python version: `python --version` (should be 3.8+)

---

### ❌ "Port 8501 already in use"

**Cause:** Streamlit already running on that port

**Solution:**
```powershell
# Option 1: Stop the other instance with Ctrl+C

# Option 2: Use different port
streamlit run app.py --server.port 8502
```

---

### ❌ Web search not working

**Cause:** Invalid Serper API key or rate limit exceeded

**Solution:**
1. Verify key: Go to https://serper.dev and check account
2. Check API usage/limits in Serper dashboard
3. Try again in a few minutes if rate limited
4. Create new Serper account if key is invalid

---

### ❌ OpenAI API error (429, 401, 500)

**Cause:** Invalid key, rate limit, or service issue

**Solution:**
| Error | Meaning | Fix |
|-------|---------|-----|
| 401 | Invalid key | Check key at openai.com |
| 429 | Rate limited | Wait and try again |
| 500 | OpenAI down | Check status.openai.com |

---

### ❌ Agents not responding / Timeout

**Cause:** Slow API or network issue

**Solution:**
1. Check internet connection
2. Try simpler query first
3. Wait 30+ seconds (first run is slower)
4. Check OpenAI API status: https://status.openai.com
5. Verify API key has credits

---

### ❌ "File not found" for answers.txt

**Cause:** File saved to different location or permissions issue

**Solution:**
1. Check project folder: `C:\Users\pksma\OneDrive\Desktop\bulidathon\buildathon-support-crew\`
2. Use file explorer to look for `answers.txt`
3. Try running app as Administrator
4. Check file permissions

---

### ❌ Streamlit page blank or not loading

**Cause:** App hasn't fully loaded

**Solution:**
1. Wait 10 seconds for initial load
2. Refresh browser (F5)
3. Check terminal for error messages
4. Try different port: `streamlit run app.py --server.port 8502`

---

### ❌ Python "ModuleNotFoundError: No module named 'crewai'"

**Cause:** Package not installed or venv not activated

**Solution:**
```powershell
# 1. Verify venv is active (check for (venv) in prompt)
# 2. Reinstall
pip install crewai crewai-tools streamlit

# 3. Verify installation
python -c "import crewai; print('OK')"
```

---

### ❌ Character encoding issues in answers.txt

**Cause:** Special characters not saved properly

**Solution:**
1. The app handles UTF-8 encoding automatically
2. If still issues, open answers.txt with Notepad++
3. Use File → Encoding → UTF-8

---

### ❌ "Git: command not found"

**Cause:** Git not installed

**Solution:**
1. Download from https://git-scm.com/download/win
2. Install with default options
3. Restart PowerShell/Command Prompt
4. Try again: `git --version`

---

## Performance Checklist

If the app runs slow:

- [ ] First run? (Always slower - models load)
- [ ] Internet connection stable? (Ping 8.8.8.8)
- [ ] API services responding? (Check status pages)
- [ ] Simple query? (Complex queries take longer)
- [ ] Free API tier? (May have rate limits)
- [ ] System resources available? (RAM, CPU)

---

## Verification Checklist

Before submitting to Buildathon:

- [ ] App runs without errors
- [ ] All 3 agents respond
- [ ] File saves correctly
- [ ] Download button works
- [ ] No API keys in code
- [ ] Environment variables work
- [ ] README.md is complete
- [ ] GitHub push successful

---

## Quick Diagnostic Commands

```powershell
# Check Python
python --version

# Check venv is active
Get-Command python

# List installed packages
pip list

# Check environment variables
echo $env:OPENAI_API_KEY
echo $env:SERPER_API_KEY

# Test imports
python -c "import crewai; import streamlit; print('OK')"

# Check if streamlit works
streamlit --version

# Kill streamlit process (if stuck)
Get-Process python | Where-Object {$_.ProcessName -like "*stream*"} | Stop-Process
```

---

## Still Having Issues?

### Check These Files for Help:
1. **README.md** - Full setup guide
2. **PROJECT_SUMMARY.md** - Detailed overview
3. **QUICKSTART.md** - Quick reference
4. **ARCHITECTURE.md** - System design

### Online Resources:
- CrewAI Docs: https://docs.crewai.com
- Streamlit Docs: https://docs.streamlit.io
- OpenAI Help: https://help.openai.com
- Serper Support: https://serper.dev/support

---

## Need More Help?

### Error Not Listed?
1. Write down the full error message
2. Check the documentation files above
3. Review ARCHITECTURE.md for system flow
4. Try the solution from similar issue above

### Still Stuck?
1. Check all environment variables are set
2. Verify API keys are correct (not truncated)
3. Try with a simpler query
4. Restart Streamlit app
5. Restart PowerShell/Terminal

---

## Common Success Indicators

✅ You'll know it's working when:
- Streamlit opens in browser at localhost:8501
- You can type a query in the text area
- Submit button is clickable
- Spinner appears while processing
- Results appear after 10-30 seconds
- answers.txt appears in project folder
- Download button is active
- No red error messages in browser

---

**Still need help?** Check INDEX.md for complete documentation navigation!
