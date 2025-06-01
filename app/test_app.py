import unittest
from app import app as flask_app  # Rename to avoid confusion

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        flask_app.testing = True
        self.client = flask_app.test_client()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get('/')
        self.assertEqual(response.data.decode(), "Hello from Flask!")

    def test_invalid_route(self):
        response = self.client.get('/invalid')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
