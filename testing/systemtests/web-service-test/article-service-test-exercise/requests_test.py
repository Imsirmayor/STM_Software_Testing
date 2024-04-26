import unittest
import requests


class ArticleServiceTest(unittest.TestCase):
    def test_find_all(self):
        # Setup
        url = 'http://localhost:8080/articles'
        # Exercise
        response = requests.get(url)
        # Verify
        content = response.text
        print(f"Response content: {content}")
        status = response.status_code
        self.assertEqual(200, status)

    def test_find_by_id(self):
        # Setup
        url = 'http://localhost:8080/articles/1'
        # Exercise
        response = requests.get(url)
        # Verify
        content = response.text
        print(f"Response content: {content}")
        status = response.status_code
        self.assertEqual(200, status)

if __name__ == '__main__':
    unittest.main()
