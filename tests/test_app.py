import unittest
import os

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['TESTING'] = 'true'
        self.client = app.test_client()

    def tearDown(self):
        del os.environ['TESTING']
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "<h1" in html
        assert "Welcome" in html or "Timeline" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        post_response = self.client.post("/api/timeline_post", data={
            "name": "Liza",
            "email": "liza@example.com",
            "content": "Testing 1 2 3"
        })
        assert post_response.status_code == 200
        post_json = post_response.get_json()
        assert post_json["name"] == "Liza"
        assert post_json["email"] == "liza@example.com"
        assert post_json["content"] == "Testing 1 2 3"

        updated_response = self.client.get("/api/timeline_post")
        updated_json = updated_response.get_json()
        assert len(updated_json["timeline_posts"]) == 1
        assert updated_json["timeline_posts"][0]["name"] == "Liza"

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<form" in html
        assert "Submit" in html or "Post" in html

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
