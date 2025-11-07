from django.test import TestCase, Client

class SimpleTest(TestCase):
    def test_homepage_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
