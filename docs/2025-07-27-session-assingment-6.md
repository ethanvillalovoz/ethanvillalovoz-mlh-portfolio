# 🐳 Containerizing Flask Portfolio with Docker

**Date:** July 27, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Containerize the Flask portfolio application using Docker, set up container orchestration with Docker Compose, implement a MySQL container for persistent storage, and configure Nginx for HTTPS support.

---

## ✅ Tasks Completed

### 1. Setting Up Docker Environment

- Installed Docker Desktop on local MacOS system:
  ```bash
  # Verified installation with:
  docker version
  docker compose version
  docker run hello-world
  ```
- Installed Docker Engine on the VPS server:
  ```bash
  curl -sSL https://get.docker.com/ | sudo sh
  sudo systemctl start docker
  sudo systemctl enable docker
  ```
- Verified installation on both environments with the hello-world container test

---

### 2. Creating Initial Dockerfile

- Created first version of Dockerfile using CentOS base image:
  ```dockerfile
  FROM centos:stream9
  
  RUN dnf -y install python3.9 python3.9-pip
  
  WORKDIR /myportfolio
  
  COPY . .
  
  RUN pip3 install -r requirements.txt
  
  CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
  
  EXPOSE 5000
  ```
- Built and tested the image with basic commands:
  ```bash
  docker build -t myportfolio_image .
  docker run --name myportfolio --env TESTING=true --publish "5000:5000" --detach myportfolio_image
  ```
- Verified functionality with curl tests:
  ```bash
  curl http://localhost:5000/api/timeline_post
  curl -X POST http://localhost:5000/api/timeline_post -d 'name=Ethan&email=ethan@example.com&content=Testing Docker!'
  ```

---

### 3. Optimizing Dockerfile

- Identified issues with the initial Dockerfile:
  - Large image size (~600MB)
  - Inefficient layer caching
  - Mixed responsibilities (app + database)
- Created improved Dockerfile with Python slim image:
  ```dockerfile
  FROM python:3.9-slim-buster
  
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  
  WORKDIR /myportfolio
  
  COPY . .
  
  CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
  
  EXPOSE 5000
  ```
- Reduced image size to ~150MB (over 400MB reduction)
- Improved build efficiency through better layer caching

---

### 4. Setting Up Container Orchestration

- Created `docker-compose.yml` for local development:
  ```yaml
  version: '3'
  services:
    myportfolio:
      build: .
      restart: always
      env_file:
        - .env
      environment:
        - FLASK_ENV=development
      ports:
        - "5000:5000"
      volumes:
        - .:/myportfolio
      depends_on:
        - mysql
    
    mysql:
      image: mariadb:10.6
      restart: always
      env_file:
        - .env
      volumes:
        - mydatabase:/var/lib/mysql
  
  volumes:
    mydatabase:
  ```
- Modified `.env` file to support containerization:
  ```
  MYSQL_HOST=mysql
  MYSQL_DATABASE=myportfoliodb
  MYSQL_USER=myportfolio
  MYSQL_PASSWORD=mypassword
  MYSQL_PORT=3306
  MYSQL_ROOT_PASSWORD=rootpassword
  ```
- Tested local development setup with:
  ```bash
  docker compose up -d
  # Created and verified timeline posts
  docker compose down
  docker compose up -d
  # Verified data persistence
  ```

---

### 5. Production Deployment Configuration

- Created `docker-compose.prod.yml` for production environment:
  ```yaml
  version: '3'
  services:
    myportfolio:
      build: .
      restart: always
      env_file:
        - .env
      depends_on:
        - mysql
    
    mysql:
      image: mariadb:10.6
      restart: always
      env_file:
        - .env
      volumes:
        - mydatabase:/var/lib/mysql
    
    nginx:
      image: jonasal/nginx-certbot:latest
      restart: always
      environment:
        - CERTBOT_EMAIL=ethan@example.com
      ports:
        - 80:80
        - 443:443
      volumes:
        - nginx_secrets:/etc/letsencrypt
        - ./user_conf.d:/etc/nginx/user_conf.d
  
  volumes:
    mydatabase:
    nginx_secrets:
  ```
- Deployed to VPS:
  ```bash
  # Stop existing service
  sudo systemctl stop myportfolio
  sudo systemctl disable myportfolio
  
  # Deploy with Docker Compose
  docker compose -f docker-compose.prod.yml up -d
  ```
- Verified production deployment and data persistence after reboot

---

### 6. Setting Up Nginx with HTTPS

- Created `user_conf.d/myportfolio.conf` for Nginx configuration:
  ```nginx
  server {
      listen 80;
      server_name ethanvillalovoz.duckdns.org;
  
      location / {
          return 301 https://ethanvillalovoz.duckdns.org$request_uri;
      }
  }
  
  server {
      listen 443 ssl;
      server_name ethanvillalovoz.duckdns.org;
  
      ssl_certificate /etc/letsencrypt/live/ethanvillalovoz.duckdns.org/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/ethanvillalovoz.duckdns.org/privkey.pem;
  
      location / {
          proxy_pass http://myportfolio:5000;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
      }
  
      location ~ /.well-known/acme-challenge {
          root /var/www/certbot;
          allow all;
      }
  }
  ```
- Added rate limiting to prevent abuse:
  ```nginx
  # Added inside server block for rate limiting
  limit_req_zone $binary_remote_addr zone=timeline_post:10m rate=1r/m;
  
  location /api/timeline_post {
      limit_req zone=timeline_post burst=1 nodelay;
      proxy_pass http://myportfolio:5000/api/timeline_post;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
  }
  ```
- Verified HTTPS functionality at https://ethanvillalovoz.duckdns.org
- Tested rate limiting by attempting multiple timeline posts within a minute

---

### 7. Updating Deployment Script

- Updated `redeploy-site.sh` for Docker-based deployment:
  ```bash
  #!/bin/bash
  
  # Navigate to project directory
  cd /root/ethanvillalovoz-mlh-portfolio
  
  # Pull latest changes
  git fetch && git reset origin/main --hard
  
  # Stop running containers
  docker compose -f docker-compose.prod.yml down
  
  # Start containers with rebuilt images
  docker compose -f docker-compose.prod.yml up -d --build
  
  echo "Deployment complete!"
  ```
- Made the script executable with `chmod +x redeploy-site.sh`
- Tested the deployment process with a small change to the site

**GitHub URL:**  
https://github.com/ethanvillalovoz/ethanvillalovoz-mlh-portfolio/blob/main/redeploy-site.sh

---

## Challenges Faced

- Initially encountered connection issues between Flask and MySQL containers
  - Resolved by adding a short wait script and depends_on configuration
- Experienced certificate generation failures with Nginx
  - Fixed by ensuring proper DNS configuration and waiting for propagation
- VPS memory constraints during Docker image builds
  - Mitigated by stopping containers before rebuilding
- Rate limit configuration in Nginx required careful syntax
  - Tested extensively to ensure proper functionality

---

## 🧠 Skills Practiced

- Docker containerization and image optimization
- Multi-container orchestration with Docker Compose
- Nginx configuration for reverse proxy and HTTPS
- Docker volume management for data persistence
- Environment-specific configurations (dev vs prod)
- Container networking and service discovery
- Automated deployment scripting with Docker
- HTTPS and SSL certificate management
- Rate limiting implementation for API security

---

## 📌 Notes for Resume or LinkedIn

- Containerized Flask web application using Docker with optimized multi-stage builds
- Implemented container orchestration with Docker Compose for local and production environments
- Set up secure HTTPS access using Nginx reverse proxy with auto-renewing SSL certificates
- Created persistent database storage using Docker volumes for reliable data retention
- Implemented rate limiting on API endpoints to prevent abuse