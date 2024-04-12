import unittest
from app import main

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_get_clients(self):
        response = self.app.get('/clients')
        self.assertEqual(response.status_code, 200)
        # Add assertions to check the response data

    def test_get_client(self):
        response = self.app.get('/clients/1')
        self.assertEqual(response.status_code, 200)
        # Add assertions to check the response data

    def test_create_client(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890'
        }
        response = self.app.post('/clients', json=data)
        self.assertEqual(response.status_code, 201)
        # Add assertions to check the response data

    def test_update_client(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890'
        }
        response = self.app.put('/clients/1', json=data)
        self.assertEqual(response.status_code, 200)
        # Add assertions to check the response data

    def test_delete_client(self):
        response = self.app.delete('/clients/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()