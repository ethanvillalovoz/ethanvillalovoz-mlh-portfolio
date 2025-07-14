#!/bin/bash

set -e  # Exit immediately if any command fails

# Kill any existing Flask server running in tmux
tmux kill-server || true

# Navigate to your project folder
cd /opt/ethanvillalovoz-mlh-portfolio

# Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# Activate Python venv
source /opt/ethanvillalovoz-mlh-portfolio/python3-virtualenv/bin/activate

# (Optional) Reinstall dependencies in case of updates
pip install -r /opt/ethanvillalovoz-mlh-portfolio/requirements.txt

# Start Flask server in a detached tmux session
tmux new-session -d -s flask "cd /opt/ethanvillalovoz-mlh-portfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"