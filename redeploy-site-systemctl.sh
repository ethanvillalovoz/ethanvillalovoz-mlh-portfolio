#!/bin/bash

set -e  # Exit immediately if any command fails

# Navigate to your project folder
cd /opt/ethanvillalovoz-mlh-portfolio

# Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# Activate Python venv
source /opt/ethanvillalovoz-mlh-portfolio/python3-virtualenv/bin/activate

# (Optional) Reinstall dependencies in case of updates
pip install -r /opt/ethanvillalovoz-mlh-portfolio/requirements.txt

# Start Flask server and enable for reboot via systemd service
systemctl start myportfolio
systemctl enable myportfolio