# 🧠 VPS & Flask Deployment Log — DigitalOcean + DuckDNS

**Date:** June 28, 2025  
**Engineer:** Ethan Villalovoz

---

## 🌐 VPS Setup and Initialization (DigitalOcean)

### ✅ Exercise 1: Create and Configure VPS
- Created a new VPS (Droplet) on [DigitalOcean](https://digitalocean.com) with the following specifications:
  - **Image:** CentOS 9 Stream x64
  - **Plan:** 1GB RAM / 1 CPU / 25GB SSD / 1000GB Transfer
  - **Region:** Closest available to user
  - **Authentication:** SSH key-based authentication using ED25519 keys
  - **Hostname:** `ethanvillalovoz`
- Generated a new SSH key pair:
  ```bash
  ssh-keygen -t ed25519 -C "ethanvillalovoz@Mac"
  ```
- Deployed Droplet and accessed IPv4 address: 128.199.6.17

### 🔐 Exercise 2: Connect to VPS via SSH
- Connected to VPS using SSH and private key:
  ```bash
  ssh -i ~/.ssh/id_ed25519 root@128.199.6.17
  ```
- Verified OS:
  ```bash
  cat /etc/centos-release
  # Output: CentOS Stream release 9
  ```

### 🔧 Exercise 3: Update Packages and Install Python/Git
- Updated system:
  ```bash
  dnf update -y
  ```
- Installed required packages:
  ```bash
  dnf install git python3
  ```
- Verified Python setup:
  ```bash
  python --version
  which python
  # Output: /usr/bin/python
  ```

---

## 🚀 Flask Portfolio Deployment

### ✅ Part 1: Clone Git Repository
- SSH’d into VPS and cloned personal Flask portfolio repository from GitHub:
  ```bash
  git clone https://github.com/ethanvillalovoz/my-flask-portfolio.git
  cd my-flask-portfolio
  ```

### ✅ Part 2: Set Up Virtual Environment and Run Flask
- Created virtual environment and installed dependencies:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
- Launched Flask app on all interfaces:
  ```bash
  python app.py --host=0.0.0.0 --port=5000
  ```
- Accessed live app at:
  ```
  http://128.199.6.17:5000
  ```

---

## 🦆 DuckDNS Subdomain Setup

### ✅ Part 3: Create Public Domain Name
- Registered free DuckDNS subdomain: ethanvillalovoz.duckdns.org
- Pointed domain to VPS IP 128.199.6.17
- Verified public access to app via:
  ```
  http://ethanvillalovoz.duckdns.org:5000
  ```

---

## 🖥️ Persistent Server Hosting

### ✅ Part 4: Keep Flask Running with tmux
- Installed and used tmux to run Flask server in a background session:
  ```bash
  tmux
  python app.py --host=0.0.0.0 --port=5000
  # Detach: Ctrl + B then D
  ```
- Verified that the Flask app remained live after SSH logout:
  ```bash
  exit
  # Re-access app from browser via DuckDNS domain
  ```

---

### ✅ Final Output

📡 Live site:
``` 
http://ethanvillalovoz.duckdns.org:5000
```

🧠 Skills Practiced:
- Linux system administration (CentOS)
- SSH key authentication and secure login
- Terminal tools (tmux, chmod, mkdir, etc.)
- Python virtual environments & dependency management
- Flask web deployment on a cloud VPS
- Dynamic DNS setup with DuckDNS
- Remote process management and persistent hosting

📌 Notes for Resume or LinkedIn:
- Deployed Flask portfolio app on a self-hosted CentOS VPS using DigitalOcean and DuckDNS
- Configured secure SSH key authentication and automated public IP routing via dynamic DNS
- Enabled persistent background server processes using tmux to maintain 24/7 site availability
