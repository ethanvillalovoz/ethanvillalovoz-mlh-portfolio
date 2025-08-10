# 🚀 Automating Deployment with GitHub Actions

**Date:** August 10, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Implement a comprehensive CI/CD (Continuous Integration/Continuous Deployment) pipeline using GitHub Actions to automate testing and deployment of the portfolio site to a DigitalOcean VPS, ensuring code quality and reducing manual deployment overhead.

---

## ✅ Tasks Completed

### 1. Automated Testing with GitHub Actions

- Created a GitHub Actions workflow for automated testing:
  ```yaml
  # Key components of test.yml
  name: Run Tests
  on:
    push:
      branches:
        - main
    pull_request:
      branches:
        - main
  jobs:
    test:
      runs-on: ubuntu-latest
      name: Run Tests
      env:
        TESTING: true
      steps:
        - name: Checkout Repository
          uses: actions/checkout@v2
        
        - name: Setup Python
          uses: actions/setup-python@v4
          with:
            python-version: '3.13.3'
        
        - name: Setup Python Virtual Environment
          run: python -m venv venv
        
        - name: Install Dependencies
          run: venv/bin/pip install -r requirements.txt

        - name: Run Tests
          run: ./run_test.sh
  ```
- Verified test workflow execution on the GitHub Actions dashboard
- Debugged environment issues to ensure tests pass in the CI environment
- Made necessary changes to ensure test compatibility with Python 3.13.3
- Successfully triggered test execution on both push and pull request events

---

### 2. Automated Deployment Workflow

- Created a deployment workflow that runs after successful testing:
  ```yaml
  # Key components of deploy.yml
  name: Deploy
  on:
    push:
      branches:
        - main
    workflow_dispatch:

  jobs:
    test:
      name: "Run Tests"
      runs-on: ubuntu-latest
      env:
        TESTING: true
      steps:
        # Test steps similar to test.yml
        
    deploy:
      needs: test
      name: "Deploy to VPS"
      runs-on: ubuntu-latest
      steps:
        - name: Configure SSH
          run: |
            mkdir -p ~/.ssh/
            echo "$SSH_PRIVATE_KEY" > ~/.ssh/deploy-key.pem
            chmod 600 ~/.ssh/deploy-key.pem
            cat >> ~/.ssh/config <<END
            Host my-vps
              HostName $SSH_IP
              User $SSH_USER
              IdentityFile ~/.ssh/deploy-key.pem
              StrictHostKeyChecking no
            END
          env:
            SSH_USER: ${{ secrets.SSH_USER }}
            SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
            SSH_IP: ${{ secrets.SSH_IP }}

        - name: Deploy site
          id: deploy
          run: ssh my-vps '~/redeploy-site.sh'
  ```
- Set up GitHub Secrets for secure SSH connection:
  - `SSH_PRIVATE_KEY`: The private SSH key
  - `SSH_IP`: Server IP address
  - `SSH_USER`: SSH username
  - `PROJECT_ROOT`: Project directory path on the server
- Created a dedicated SSH key pair specifically for deployments
- Successfully triggered the deployment process on push to main
- Verified that the deployment script (`~/redeploy-site.sh`) executes properly

---

### 3. Enhanced Deployment Features

- Added container status reporting after deployment:
  ```yaml
  - name: Print Container Status
    run: ssh my-vps 'cd /opt/ethanvillalovoz-mlh-portfolio && sudo docker ps || echo "Unable to get container status"'
  ```
- Debugged path issues to correctly navigate to the project directory
- Addressed docker command permissions by using sudo where necessary
- Set up Discord notification webhooks for deployment status:
  ```yaml
  - name: Send Success Notification to Discord
    if: success()
    run: |
      curl -s -X POST "${{ secrets.DISCORD_WEBHOOK }}" \
        -H "Content-Type: application/json" \
        -d '{
          "content": "🚀 Deployment Successful",
          "embeds": [{
            "title": "Portfolio Site Deployed",
            "description": "The portfolio site has been successfully deployed to the VPS",
            "color": 5814783
          }]
        }'
  ```
- Implemented failure notifications for comprehensive monitoring:
  ```yaml
  notify-failure:
    needs: [test, deploy]
    if: failure()
    name: "Notify Deployment Failure"
    runs-on: ubuntu-latest
    steps:
      - name: Send Failure Notification to Discord
        run: |
          curl -s -X POST "${{ secrets.DISCORD_WEBHOOK }}" \
            -H "Content-Type: application/json" \
            -d '{
              "content": "🚨 Deployment Failed",
              "embeds": [{
                "title": "Deployment Failure",
                "description": "There was an error during the deployment process. Please check the GitHub Actions logs.",
                "color": 15158332
              }]
            }'
  ```
- Established job dependency structure to ensure deployment occurs only after successful tests
- Used conditional job execution with `needs` and `if` clauses

---

## Challenges Faced

- **SSH Connection Issues**: Initial SSH connection attempts failed due to permission and key format problems
  - Resolved by properly formatting the private key and setting correct permissions (`chmod 600`)
  - Created dedicated deployment keys to follow security best practices
  
- **Path Discrepancies**: The project path on the VPS was different than expected
  - Initial attempt used `/ethanvillalovoz-mlh-portfolio` but actual path was `/opt/ethanvillalovoz-mlh-portfolio`
  - Fixed by using `pwd` command to determine the correct path
  
- **Docker Command Availability**: The `docker-compose` command was not available in the SSH session
  - Switched to using `docker ps` with `sudo` to ensure proper privileges
  - Added fallback messages to improve error handling
  
- **Test Environment Configuration**: Tests initially failed due to database connection issues
  - The `TESTING` environment variable was essential to make tests pass in CI environment
  - Aligned environment variables between test and deploy workflows
  
- **Notification Workflow Logic**: Needed to ensure failure notifications would run even if previous jobs failed
  - Implemented a separate job with appropriate conditions to catch failures
  - Used job dependencies to properly sequence the workflow

---

## 🧠 Skills Practiced

- GitHub Actions workflow configuration and debugging
- CI/CD pipeline design and implementation
- Secure credential management using GitHub Secrets
- SSH key management and configuration
- Conditional job execution in CI/CD workflows
- Webhook integration with Discord for notifications
- Docker container management and monitoring
- Environment-specific configuration for tests
- Shell scripting in workflow contexts

---

## 📌 Notes for Resume or LinkedIn

- Implemented end-to-end CI/CD pipeline using GitHub Actions for automated testing and deployment
- Designed secure deployment process using SSH keys and secrets management
- Created multi-stage workflow with test verification, deployment, and status reporting
- Integrated real-time deployment notifications via Discord webhooks for success and failure scenarios
- Improved development workflow with automated testing on pull requests and pushes
- Implemented container status monitoring to track deployment health
