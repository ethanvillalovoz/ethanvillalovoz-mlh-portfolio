# 🔍 Midway Check-In and Project Verification

**Date:** August 1, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Ensure that the portfolio project is properly set up, with all components working correctly, and verify that the deployment process is functioning as expected. Fix any issues with Git repository structure, test execution, and deployment scripts.

---

## ✅ Tasks Completed

### 1. Repository Structure Verification

- Verified that the GitHub repository contains the correct files and structure:
  ```bash
  # Key project components
  app/                 # Flask application code
  tests/               # Test suite for the application
  user_conf.d/         # Nginx configuration files
  .gitignore           # Git ignore rules
  Dockerfile           # Container definition
  docker-compose.yml   # Local development orchestration
  docker-compose.prod.yml  # Production container orchestration
  requirements.txt     # Python dependencies
  ```
- Fixed .gitignore configuration to properly exclude virtual environment:
  ```bash
  # Added both patterns to ensure comprehensive exclusion
  python3-virtualenv/
  .python3-virtualenv/
  ```
- Created a backup and cleaned up requirements.txt to remove incompatible dependencies:
  ```bash
  # Updated requirements to include only necessary packages
  click==8.0.1
  Flask==2.0.1
  itsdangerous==2.0.1
  Jinja2==3.0.1
  MarkupSafe==2.0.1
  peewee==3.14.10
  PyMySQL==1.0.2
  python-dotenv==0.17.1
  Werkzeug==2.0.1
  ```
- Committed changes with appropriate messages:
  ```bash
  git add .gitignore requirements.txt
  git commit -m "Remove virtual environment from tracking and update requirements"
  git push origin main
  ```

---

### 2. Test Suite Verification

- Recreated the Python virtual environment with compatible dependencies:
  ```bash
  python3 -m venv python3-virtualenv
  source python3-virtualenv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
- Successfully executed the test suite with no failures:
  ```bash
  ./run_test.sh
  ```
- Verified all tests are passing:
  - `test_home`: Home page loads with expected content
  - `test_malformed_timeline_post`: Malformed posts are rejected
  - `test_timeline`: API GET and POST operations work correctly
  - `test_timeline_page`: Timeline page loads with form
  - `test_create_and_retrieve_timeline_posts`: Database operations are functioning

- Created a curl-based API test script for quick manual testing:
  ```bash
  ./curl-test.sh
  # Successfully tested POST and GET operations on the timeline API
  ```

---

### 3. Deployment Script Verification

- Inspected the current `redeploy-site.sh` script on the VPS:
  ```bash
  cat /root/redeploy-site.sh
  ```
- Verified that the script properly uses Docker Compose for deployment:
  ```bash
  # Script correctly includes:
  git fetch && git reset origin/main --hard  # Get latest code
  docker compose -f docker-compose.prod.yml down  # Stop containers
  docker compose -f docker-compose.prod.yml up -d --build  # Rebuild and restart
  ```
- Tested the deployment process with a minor change to the site:
  ```bash
  # Made a change to a template file locally
  git commit -am "Update homepage greeting for midway check-in"
  git push origin main
  
  # On the VPS:
  cd /root
  ./redeploy-site.sh
  
  # Verified deployment completed successfully
  ```
- Confirmed that changes are visible at the public URL:
  https://ethanvillalovoz.duckdns.org

---

### 4. Container Status Verification

- Checked running containers on the VPS:
  ```bash
  docker ps
  ```
- Verified all required containers are running:
  - `myportfolio`: Flask application container
  - `mysql`: Database container
  - `nginx`: Web server/proxy container
- All containers showing healthy status with proper uptime
- Confirmed container networking is configured correctly
- Verified that data persistence is working through volume mounts

---

## Challenges Faced

- Virtual environment tracking issues in Git
  - Resolved by updating .gitignore and using `git reset` to restore proper tracking state
- Python dependency compatibility problems with Python 3.13
  - Fixed by simplifying requirements.txt to include only essential packages
  - Removed problematic cffi and cryptography packages that weren't needed
- Test execution environment issues
  - Resolved by recreating the virtual environment with compatible packages
  - Updated run_test.sh to properly use the virtual environment

---

## 🧠 Skills Practiced

- Git repository management and .gitignore configuration
- Python virtual environment setup and dependency management
- Docker container orchestration and status monitoring
- Automated testing and verification
- Continuous deployment workflows
- Environment-specific configurations
- Shell scripting for automation
- Project structure organization

---

## 📌 Notes for Resume or LinkedIn

- Implemented comprehensive automated test suite for Flask web application
- Created CI/CD pipeline with automated deployment using Git and Docker
- Maintained clean repository structure with proper dependency management
- Utilized containerization for consistent development and production environments