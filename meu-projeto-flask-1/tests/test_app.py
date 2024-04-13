import unittest
from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_api_route(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"API endpoint")

if __name__ == '__main__':
    unittest.main()