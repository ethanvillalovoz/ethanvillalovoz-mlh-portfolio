# 🗄️ Adding Database & Persistent Service — Flask Portfolio

**Date:** July 14, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Integrate a MySQL database into my Flask portfolio site to support a public timeline, test endpoints with Postman and curl, build a timeline page, and deploy persistently using a systemd service.

---

## ✅ Tasks Completed

### 1. Install MySQL Database Locally

- Installed MySQL server on macOS using the official installer.
- Started MySQL service and connected as root:
  ```bash
  sudo mysql -u root
  ```
- Created a new MySQL user and database:
  ```sql
  CREATE USER 'myportfolio'@'localhost' IDENTIFIED BY 'mypassword';
  CREATE DATABASE myportfoliodb;
  GRANT ALL PRIVILEGES ON *.* TO 'myportfolio'@'localhost';
  FLUSH PRIVILEGES;
  ```
- Verified connection with:
  ```bash
  mysql -u myportfolio -p
  ```
- Added credentials to `.env` (copied from `example.env`).
- Used `load_dotenv()` in `__init__.py` to load environment variables.
- Connected to MySQL in Flask using Peewee ORM:
  ```python
  from peewee import *
  mydb = MySQLDatabase(
      os.getenv("MYSQL_DATABASE"),
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"),
      host=os.getenv("MYSQL_HOST"),
      port=int(os.getenv("MYSQL_PORT"))
  )
  ```
- Verified connection with Flask (`<peewee.MySQLDatabase object at ...>`).

---

### 2. Create Database Table & Endpoints

- Defined `TimelinePost` model in `__init__.py`:
  ```python
  from datetime import datetime
  class TimelinePost(Model):
      name = CharField()
      email = CharField()
      content = TextField()
      created_at = DateTimeField(default=datetime.now)
      class Meta:
          database = mydb
  ```
- Created table:
  ```python
  mydb.connect()
  mydb.create_tables([TimelinePost])
  ```
- Added endpoints:
  - **POST /api/timeline_post** to create posts
  - **GET /api/timeline_post** to retrieve posts (ordered by newest)
  - Imported `model_to_dict` from `playhouse.shortcuts`
- Tested endpoints with Postman (GET/POST).
- Wrote `curl-test.sh` to automate endpoint testing:
  - POSTs a random timeline post
  - GETs all posts to verify addition
  - Bonus: DELETE endpoint to remove test posts

**GitHub URL:**  
https://github.com/ethanvillalovoz/ethanvillalovoz-mlh-portfolio/blob/main/curl-test.sh

---

### 3. Create Timeline Page

- Created `app/templates/timeline.html` with a form for new posts and a section to display posts.
- Used fetch API to POST new timeline entries and update the page dynamically.
- Displayed posts in descending order.
- Bonus: Used Gravatar for user avatars based on email.
- Committed and pushed changes.
- Deployed to VPS using `redeploy-site.sh`.

**GitHub URL to app/__init__.py:**  
https://github.com/ethanvillalovoz/ethanvillalovoz-mlh-portfolio/blob/main/app/__init__.py

**Live Timeline Page:**  
http://ethanvillalovoz.duckdns.org:5000/timeline

---

### 4. Approach for Moving Portfolio Data to Database

To move experiences, education, and hobbies into the database:
- Define new models (e.g., `Experience`, `Education`, `Hobby`) in Peewee.
- Add fields for each data type (e.g., title, description, dates).
- Create tables with `mydb.create_tables([...])`.
- Update Flask routes to query these tables and pass data to templates.
- Add admin forms or scripts to populate/update data.
- Remove hardcoded lists from `data.py` and migrate to database queries.

---

### 5. Create Persistent Service with systemd

- Created `/etc/systemd/system/myportfolio.service` unit file:
  ```ini
  [Unit]
  Description=Flask Portfolio Service
  After=network.target

  [Service]
  User=root
  Group=root
  WorkingDirectory=/root/ethanvillalovoz-mlh-portfolio
  Environment="PATH=/root/miniconda3/envs/myenv/bin"
  ExecStart=/root/miniconda3/envs/myenv/bin/flask run --host=0.0.0.0

  [Install]
  WantedBy=multi-user.target
  ```
- Enabled and started service:
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl start myportfolio
  sudo systemctl enable myportfolio
  sudo systemctl status myportfolio
  ```
- Verified site is running after reboot.

**Live Site URL:**  
http://ethanvillalovoz.duckdns.org:5000

**Note:**  
SELinux may block Flask if installed in `/root`. Either disable SELinux or use `/opt` for deployment.

---

### 6. Update redeploy-site.sh for Service Deployment

- Updated `redeploy-site.sh` to:
  - Pull latest code
  - Activate Python environment
  - Install dependencies
  - Restart `myportfolio` service:
    ```bash
    sudo systemctl restart myportfolio
    ```
- Committed and pushed updated script.

**GitHub URL:**  
https://github.com/ethanvillalovoz/ethanvillalovoz-mlh-portfolio/blob/main/redeploy-site.sh

---

## Challenges Faced

Note: One issue encountered during "Creating a Service - Part 1" was that SELinux prevented the Flask service from starting when installed in the root user's home directory.

You have two options to resolve this:

Disable SELinux to allow the Flask service to run from the root directory.

Install Flask in a different directory, such as /opt, which is not restricted by SELinux.

The module instructions indicate that the service should be run from the root directory, which suggests that either SELinux was not installed on the instructor's VM or it was set to permissive mode. However, this was not clarified in the module documentation.

---

## 🧠 Skills Practiced

- MySQL installation and user management
- ORM modeling and migrations with Peewee
- REST API endpoint creation and testing (Postman, curl)
- Bash scripting for automated API tests
- Flask template and frontend integration
- Systemd service setup for persistent deployment
- Linux server administration and SELinux troubleshooting

---

## 📌 Notes for Resume or LinkedIn

- Integrated MySQL database and ORM into Flask portfolio site for dynamic timeline feature.
- Automated API testing with bash scripts and curl.
- Deployed Flask app as a persistent systemd service for high availability.
- Practiced full-stack development, Linux server management, and secure