import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True

    def test_index_data(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<h1>Hello, World!</h1>')
        
        
        
if __name__ == '__main__':
    unittest.main()