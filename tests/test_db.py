import unittest
from peewee import Model, CharField, TextField, SqliteDatabase

test_db = SqliteDatabase(':memory:')

from app.models import TimelinePost  # Import the model from the main application module
MODELS = [TimelinePost]

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_create_and_retrieve_timeline_posts(self):
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content='Hello world, I\'m John!'
        )
        self.assertEqual(first_post.id, 1)

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world, I\'m Jane!'
        )
        self.assertEqual(second_post.id, 2)

        posts = TimelinePost.select().order_by(TimelinePost.id)
        self.assertEqual(posts.count(), 2)
        self.assertEqual(posts[0].name, 'John Doe')
        self.assertEqual(posts[1].email, 'jane@example.com')

if __name__ == '__main__':
    unittest.main()
