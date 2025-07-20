import unittest
from peewee import SqliteDatabase

# Use an in-memory SQLite database for isolated testing
test_db = SqliteDatabase(':memory:')

# Import the TimelinePost model from the main application
from app import TimelinePost

# List of models to bind to the test database
MODELS = [TimelinePost]

class TestTimelinePost(unittest.TestCase):
    """Unit tests for the TimelinePost model using an in-memory SQLite database."""

    def setUp(self):
        """Set up a fresh database before each test."""
        # Bind models to the test database and create tables
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        """Clean up the database after each test."""
        # Drop tables and close the database connection
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_create_and_retrieve_timeline_posts(self):
        """Test creating and retrieving TimelinePost records."""
        # Create the first timeline post
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content='Hello world, I\'m John!'
        )
        self.assertEqual(first_post.id, 1)

        # Create the second timeline post
        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world, I\'m Jane!'
        )
        self.assertEqual(second_post.id, 2)

        # Retrieve all posts, ordered by ID
        posts = TimelinePost.select().order_by(TimelinePost.id)
        self.assertEqual(posts.count(), 2)
        self.assertEqual(posts[0].name, 'John Doe')
        self.assertEqual(posts[1].email, 'jane@example.com')

if __name__ == '__main__':
    unittest.main()
