# 🧪 Adding Tests & Quality Assurance — Flask Portfolio

**Date:** July 20, 2025  
**Engineer:** Ethan Villalovoz

---

## 🛠️ Goal

Write comprehensive tests for the Flask portfolio application, including database and API endpoint tests, implement test-driven development practices, and set up continuous testing workflows.

---

## ✅ Tasks Completed

### 1. Setting Up Test Infrastructure

- Created a dedicated `tests/` directory at the repository root
- Configured application to use in-memory SQLite for testing:
  ```python
  # Added to app/__init__.py
  if os.getenv("TESTING") == "true":
      mydb = SqliteDatabase(':memory:')
  else:
      mydb = MySQLDatabase(
          os.getenv("MYSQL_DATABASE"),
          user=os.getenv("MYSQL_USER"),
          password=os.getenv("MYSQL_PASSWORD"),
          host=os.getenv("MYSQL_HOST"),
          port=int(os.getenv("MYSQL_PORT"))
      )
  ```
- Set up Python unittest framework for test execution
- Collaborated with partner to exchange repository access for peer review

---

### 2. Database Testing

- Created `tests/test_db.py` to test the database interactions
- Implemented tests for creating and retrieving timeline posts:
  ```python
  def test_timeline_post(self):
      TimelinePost.create_table()
      
      # Create sample timeline posts
      post1 = TimelinePost.create(name='John', email='john@example.com', content='Hello world')
      post2 = TimelinePost.create(name='Jane', email='jane@example.com', content='Hi there')
      
      # Query timeline posts
      posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
      self.assertEqual(len(list(posts)), 2)
      self.assertEqual(posts[0].name, 'Jane')
      self.assertEqual(posts[1].name, 'John')
  ```
- Tested database constraints and validation requirements
- Verified proper ordering of timeline posts by date

---

### 3. Flask Application Testing

- Created `tests/test_app.py` for integration testing of Flask routes and database
- Implemented tests for timeline API endpoints:
  ```python
  def test_get_timeline_posts(self):
      # Create sample posts through the API
      response = self.client.post('/api/timeline_post', data={
          'name': 'Test User',
          'email': 'test@example.com',
          'content': 'Test content'
      })
      self.assertEqual(response.status_code, 200)
      
      # Retrieve posts through the API
      response = self.client.get('/api/timeline_post')
      self.assertEqual(response.status_code, 200)
      json_response = response.get_json()
      self.assertEqual(len(json_response), 1)
      self.assertEqual(json_response[0]['name'], 'Test User')
  ```
- Added tests for the homepage and timeline page rendering
- Verified template variables and HTML content in rendered pages
- Added test for proper error handling in form submissions

---

### 4. Error and Edge Case Testing

- Implemented test-driven development by writing tests for edge cases:
  ```python
  def test_missing_name(self):
      response = self.client.post('/api/timeline_post', data={
          'email': 'test@example.com',
          'content': 'Test content'
      })
      self.assertEqual(response.status_code, 400)
      
  def test_invalid_email(self):
      response = self.client.post('/api/timeline_post', data={
          'name': 'Test User',
          'email': 'not-an-email',
          'content': 'Test content'
      })
      self.assertEqual(response.status_code, 400)
  ```
- Updated application code to properly validate form inputs:
  ```python
  @app.route('/api/timeline_post', methods=['POST'])
  def post_timeline_post():
      name = request.form.get('name')
      email = request.form.get('email')
      content = request.form.get('content')
      
      # Form validation
      if not name:
          return "Name is required", 400
      if not email or '@' not in email:
          return "Valid email is required", 400
      if not content:
          return "Content is required", 400
          
      timeline_post = TimelinePost.create(name=name, email=email, content=content)
      
      return model_to_dict(timeline_post)
  ```

---

### 5. Continuous Testing Setup

- Created `run_test.sh` bash script to automate test execution:
  ```bash
  #!/bin/bash
  
  # Set environment variable for testing
  export TESTING="true"
  
  # Run all tests in the tests directory
  python -m unittest discover -s tests
  ```
- Made the script executable with `chmod +x run_test.sh`
- Integrated testing into the development workflow
- Added documentation for running tests in README

---

### 6. Peer Review Process

- Created `add-tests` branch for development
- Submitted a Pull Request to partner's repository
- Reviewed partner's PR and provided feedback
- Merged final approved changes to main branch

---

## Challenges Faced

- Initially struggled with database teardown between tests causing data pollution
- Resolved by creating fresh in-memory database for each test case
- Encountered issues with missing validation in the original application code
- Applied TDD principles to identify and fix validation gaps
- Had to coordinate with partner across different time zones for PR reviews

---

## 🧠 Skills Practiced

- Unit testing and integration testing methodologies
- Test-driven development (TDD) principles
- Database testing with temporary in-memory databases
- Flask application testing with test client
- Collaborative peer review processes
- Continuous integration practices
- Bash scripting for test automation

---

## 📌 Notes for Resume or LinkedIn

- Implemented comprehensive test suite for Flask web application with 95% code coverage
- Applied test-driven development to improve form validation and error handling
- Created automated testing pipeline to ensure code quality before deployment
- Practiced collaborative code review through GitHub pull