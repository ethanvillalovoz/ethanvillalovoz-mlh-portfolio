# 🚀 Automated Flask Deployment Script Log

**Date:** July 6, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Automate the process of redeploying my Flask portfolio site on my VPS whenever I push changes to the GitHub repository. This reduces manual steps and ensures the live site always reflects the latest code.

---

## 📝 Steps Automated

1. **Kill all existing tmux sessions**  
   Ensures no old Flask servers are running in the background.

2. **Navigate to project folder**  
   Changes directory to the portfolio project.

3. **Pull latest changes from GitHub**  
   Uses `git fetch && git reset origin/main --hard` to sync the VPS repo with the main branch.

4. **Activate Python environment and install dependencies**  
   Activates the Conda environment and installs any updated requirements.

5. **Start Flask server in a new detached tmux session**  
   Launches Flask in the background so it keeps running after logout.

---

## 🖥️ Bash Script: `~/redeploy-site.sh`

```bash
#!/bin/bash

set -e  # Exit immediately if any command fails

# Kill any existing Flask server running in tmux
tmux kill-server || true

# Navigate to your project folder
cd ~/ethanvillalovoz-mlh-portfolio

# Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# Activate conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate myenv

# (Optional) Reinstall dependencies in case of updates
pip install -r requirements.txt

# Start Flask server in a detached tmux session
tmux new-session -d -s flask "cd ~/ethanvillalovoz-mlh-portfolio && source ~/miniconda3/etc/profile.d/conda.sh && conda activate myenv && flask run --host=0.0.0.0"
```

---

## ✅ Testing

1. Made a text change in the GitHub repository's main branch.
2. SSH’d into VPS and ran:
   ```bash
   ~/redeploy-site.sh
   ```
3. Visited [http://ethanvillalovoz.duckdns.org:5000](http://ethanvillalovoz.duckdns.org:5000) and confirmed the change appeared.

---

## 📦 Script Committed

- Added `redeploy-site.sh` to the root of the repository.
- Committed and pushed to GitHub.

**GitHub URL:**  
https://github.com/ethanvillalovoz/ethanvillalovoz-mlh-portfolio/blob/main/redeploy-site.sh

---

## 🧠 Skills Practiced

- Bash scripting for automation
- Process management with tmux
- Git operations for deployment
- Python virtual environment management
- Flask server deployment on a VPS

---

## 📌 Notes for Resume or LinkedIn

- Automated Flask web app deployment using a custom Bash script and tmux for persistent background processes.
- Reduced manual deployment steps by integrating Git operations, Python environment management, and server restarts into a single script.
- Improved site reliability and update speed by ensuring the VPS always runs the latest code from GitHub.
- Demonstrated skills in Linux server administration, process automation, and cloud-based deployment solutions.