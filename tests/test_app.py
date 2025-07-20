import sys
import os
import unittest

# Ensure the app module can be imported by adding the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import *  # Import the Flask app and TimelinePost model

class AppTestCase(unittest.TestCase):
    """Integration tests for the Flask application endpoints and TimelinePost API."""

    def setUp(self):
        """Set up the test client and clear the TimelinePost table before each test."""
        os.environ['TESTING'] = 'true'  # Set environment variable to indicate testing mode
        self.client = app.test_client()  # Create a test client for the Flask app
        TimelinePost.delete().execute()  # Remove all timeline posts to ensure a clean slate

    def tearDown(self):
        """Clean up after each test by removing the TESTING environment variable."""
        os.environ.pop('TESTING', None)

    def test_home(self):
        """Test that the home page loads successfully and contains expected content."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>MLH Fellow</title>", html)
        self.assertIn("<h1", html)
        # Check for either "Welcome" or "Timeline" in the page content
        self.assertTrue("Welcome" in html or "Timeline" in html)

    def test_timeline(self):
        """Test the timeline API: GET should return empty, POST should add, GET should return one."""
        # Ensure timeline is empty at the start
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 0)

        # Add a new timeline post via POST
        post_response = self.client.post("/api/timeline_post", data={
            "name": "Liza",
            "email": "liza@example.com",
            "content": "Testing 1 2 3"
        })
        self.assertEqual(post_response.status_code, 200)
        post_json = post_response.get_json()
        self.assertEqual(post_json["name"], "Liza")
        self.assertEqual(post_json["email"], "liza@example.com")
        self.assertEqual(post_json["content"], "Testing 1 2 3")

        # Ensure the timeline now contains the new post
        updated_response = self.client.get("/api/timeline_post")
        updated_json = updated_response.get_json()
        self.assertEqual(len(updated_json["timeline_posts"]), 1)
        self.assertEqual(updated_json["timeline_posts"][0]["name"], "Liza")

    def test_timeline_page(self):
        """Test that the timeline page loads and contains a form for posting."""
        response = self.client.get("/timeline")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<form", html)
        # Check for either "Submit" or "Post" button in the form
        self.assertTrue("Submit" in html or "Post" in html)

    def test_malformed_timeline_post(self):
        """Test that malformed timeline posts are rejected with appropriate error messages."""
        # Missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid name", html)

        # Empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid content", html)

        # Invalid email format
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid email", html)
