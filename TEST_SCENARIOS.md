# Test Scenarios for Customer Support Crew

## Sample Test Queries

Try these queries to test the system:

### 1. Password Reset Query
**Input:** "How do I reset my password?"
- **Expected:** Assistant provides basic steps
- **Web Search:** Finds specific instructions for different platforms
- **File:** Both answers saved to answers.txt

### 2. Technical Support
**Input:** "My internet connection keeps dropping. What should I do?"
- **Expected:** Generic troubleshooting steps
- **Web Search:** Latest solutions and ISP guidelines
- **File:** Complete troubleshooting guide saved

### 3. Product Information
**Input:** "What are the specifications of your latest product?"
- **Expected:** Knowledge-based product info
- **Web Search:** Current specifications and reviews
- **File:** Comprehensive product details saved

### 4. Billing Question
**Input:** "How can I update my billing information?"
- **Expected:** Standard billing procedures
- **Web Search:** Step-by-step current instructions
- **File:** Complete billing update guide saved

### 5. Account Issue
**Input:** "My account appears to be locked. How do I unlock it?"
- **Expected:** Standard unlock procedures
- **Web Search:** Security best practices and solutions
- **File:** Account recovery steps saved

## Expected Output Format in answers.txt

```
=====================================
CUSTOMER SUPPORT RECORD
=====================================

TIMESTAMP: [Date and Time]
---

CUSTOMER QUERY:
[User's original query]

---

ASSISTANT ANSWER:
[Direct answer from Assistant Agent]

---

WEB SEARCH ANSWER:
[Answer from Web Search Agent with current information]

---

[End of Record]
=====================================
```

## Testing Checklist

- [ ] App starts without errors
- [ ] Query form accepts input
- [ ] Submit button works
- [ ] Assistant Agent responds
- [ ] Web Search Agent searches and responds
- [ ] Entry Agent saves file
- [ ] answers.txt is created
- [ ] All three answers appear in UI
- [ ] Download button appears
- [ ] File content is properly formatted
- [ ] Timestamp is included
- [ ] No API key errors
- [ ] UI is responsive

## Common Test Cases

### Quick Test (1-2 minutes)
```
Query: "What is Python?"
Expected: 3 different answers about Python programming language
```

### Medium Test (3-5 minutes)
```
Query: "Best practices for data security"
Expected: Knowledge-based answer + recent web sources
```

### Full Test (5+ minutes)
```
Query: "How do I migrate to a new phone?"
Expected: Complete migration guide from all agents
```

## Performance Notes

- First run may take longer (model loading)
- Subsequent queries should be faster
- Web search may add 10-30 seconds to execution
- File writing is typically instantaneous

## Debugging Tips

1. **Check API Keys:**
   ```powershell
   echo $env:OPENAI_API_KEY
   echo $env:SERPER_API_KEY
   ```

2. **Check Agent Responses:**
   - Look at the verbose output in the UI
   - Set `verbose=True` in Agent creation to debug

3. **Monitor Web Search:**
   - Verify SERPER_API_KEY is valid
   - Check Serper account for API usage

4. **File Validation:**
   - Look for answers.txt in the project folder
   - Check file permissions if file doesn't save

5. **Error Logs:**
   - Check Streamlit console for detailed errors
   - Review OpenAI API logs for rate limits

---

Happy Testing! 🎉
