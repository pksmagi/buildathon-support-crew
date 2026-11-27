# 🚀 GitHub Setup Guide

## Push Your Project to GitHub

Follow these steps to upload your project to GitHub for the Buildathon submission.

### Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: `buildathon-support-crew`
3. Add description: "Customer Support System with CrewAI and Streamlit"
4. Choose visibility: Public (for Buildathon)
5. **Don't** initialize with README (we have one)
6. Click "Create repository"

### Step 2: Copy the Repository URL

After creation, you'll see your repo URL:
```
https://github.com/YOUR_USERNAME/buildathon-support-crew.git
```

### Step 3: Set Up Git Locally (Windows PowerShell)

Navigate to your project:
```powershell
cd C:\Users\pksma\OneDrive\Desktop\bulidathon\buildathon-support-crew
```

Initialize git:
```powershell
git init
```

Add all files:
```powershell
git add .
```

Create initial commit:
```powershell
git commit -m "Initial commit: Customer Support Crew - CrewAI and Streamlit integration"
```

Add remote repository (replace with your URL):
```powershell
git remote add origin https://github.com/YOUR_USERNAME/buildathon-support-crew.git
```

Rename branch to main (if needed):
```powershell
git branch -M main
```

Push to GitHub:
```powershell
git push -u origin main
```

### Step 4: Verify on GitHub

Go to your repository URL and confirm:
- ✅ All files are uploaded
- ✅ app.py is visible
- ✅ README.md displays properly
- ✅ .gitignore is in place (venv/ not shown)

---

## Useful Git Commands

### Check Status
```powershell
git status
```

### View Commit History
```powershell
git log --oneline
```

### Add Updates After Initial Push
```powershell
git add .
git commit -m "Your message here"
git push
```

### Create a New Branch for Development
```powershell
git checkout -b develop
git push -u origin develop
```

---

## GitHub README Tips

Your README.md will automatically display on the repository main page. Make sure it includes:

✅ Project title and description
✅ Features list
✅ Setup instructions
✅ How to run
✅ Example usage
✅ Technologies used
✅ Troubleshooting

All of these are already in your README.md!

---

## Repository Structure Verification

When pushed, your repository should look like:
```
buildathon-support-crew/
├── app.py                    ✅ Main application
├── README.md                 ✅ Setup guide
├── QUICKSTART.md            ✅ Quick reference
├── PROJECT_SUMMARY.md       ✅ Project overview
├── DELIVERABLES.md          ✅ Deliverables list
├── TEST_SCENARIOS.md        ✅ Testing guide
├── requirements.txt         ✅ Dependencies
├── .env.example             ✅ API key template
├── .gitignore               ✅ Ignore patterns
└── [Other files...]
```

**Note:** `venv/` and `answers.txt` will NOT appear (correctly ignored by .gitignore)

---

## Buildathon Submission Checklist

Before submitting, verify:

- [ ] Repository is public
- [ ] All source code is committed
- [ ] README.md has clear instructions
- [ ] No API keys in any committed files
- [ ] `.env.example` shows what keys are needed
- [ ] `.gitignore` excludes `venv/`
- [ ] app.py is complete and runnable
- [ ] All 3 agents are implemented
- [ ] Streamlit UI is functional
- [ ] File saving works
- [ ] Code is well-commented
- [ ] Documentation is complete

---

## If You Need to Update

After pushing to GitHub, you can still make changes:

```powershell
# Make your changes to app.py or other files

# Stage changes
git add app.py

# Commit with message
git commit -m "Fix: description of what changed"

# Push updates
git push
```

---

## Troubleshooting Git

### "fatal: not a git repository"
Solution:
```powershell
git init
```

### "rejected... [pre-receive hook declined]"
Solution:
```powershell
git pull origin main
git push
```

### "Permission denied" on push
Solution:
1. Check if you're logged into GitHub on your machine
2. Use GitHub CLI: `gh auth login`
3. Or generate SSH key (see GitHub docs)

### "fatal: The current branch main has no upstream tracking"
Solution:
```powershell
git branch -M main
git push -u origin main
```

---

## Share Your Repository

Once pushed, share these links with your team:

1. **Repository:** `https://github.com/YOUR_USERNAME/buildathon-support-crew`
2. **Raw app.py:** `https://github.com/YOUR_USERNAME/buildathon-support-crew/blob/main/app.py`
3. **Full README:** `https://github.com/YOUR_USERNAME/buildathon-support-crew#readme`

---

## Example Commit Messages

Good commit messages for future updates:

```
git commit -m "Add: Sentiment analysis to agent responses"
git commit -m "Fix: Web search timeout issue"
git commit -m "Refactor: Extract agent creation to separate function"
git commit -m "Docs: Update README with deployment instructions"
git commit -m "Chore: Update dependencies in requirements.txt"
```

---

## 🎉 You're Ready to Submit!

Your project is complete and ready for the Weekly Buildathon. Push it to GitHub and you're all set!

**Next:** Follow the instructions in this file to push to GitHub, then submit your repository link to the Buildathon platform.

---

**Need Help?** Check GitHub's documentation: https://docs.github.com/en/get-started
