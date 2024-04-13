import unittest
from flask import Flask
from app.api.routes import api_routes

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api_routes)

    def test_hello_world(self):
        with self.app.test_client() as client:
            response = client.get('/api/hello')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), 'Hello, World!')

    def test_get_users(self):
        with self.app.test_client() as client:
            response = client.get('/api/users')
            self.assertEqual(response.status_code, 200)
            # Add assertions for the expected response data

    def test_create_user(self):
        with self.app.test_client() as client:
            response = client.post('/api/users', json={'name': 'John Doe', 'email': 'john@example.com'})
            self.assertEqual(response.status_code, 201)
            # Add assertions for the expected response data

if __name__ == '__main__':
    unittest.main()