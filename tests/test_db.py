import unittest
from peewee import SqliteDatabase, Model, CharField, TextField

test_db = SqliteDatabase(':memory:')

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()

    class Meta:
        database = test_db

class TestTimelinePostModel(unittest.TestCase):
    def setUp(self):
        test_db.connect()
        test_db.create_tables([TimelinePost])

    def tearDown(self):
        test_db.drop_tables([TimelinePost])
        test_db.close()

    def test_create_post(self):
        post = TimelinePost.create(
            name='Ryan',
            email='ryan@example.com',
            content='Test post content'
        )
        self.assertEqual(post.name, 'Ryan')
        self.assertEqual(post.email, 'Ryan@example.com')
        self.assertEqual(post.content, 'Test post content')

if __name__ == '__main__':
    unittest.main()
