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

