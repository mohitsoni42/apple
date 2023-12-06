from django.test import TestCase


# Create your tests here.
class HomeTest(TestCase):
    def test_page_running(self):
        res = self.client.get("http://127.0.0.1:8123/tech-blog/")

        self.assertEqual(res.content ,b"heyyyy o")

        