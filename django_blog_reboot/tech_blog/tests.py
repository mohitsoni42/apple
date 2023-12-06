from django.test import TestCase
from .models import ArticleModel


# Create your tests here.
class HomeTest(TestCase):
    def test_page_running(self):
        res = self.client.get("http://127.0.0.1:8123/tech-blog/")

        self.assertEqual(res.content ,b"heyyyy o")

        
class ArticleTest(TestCase):
    def test_article_created_success(self):
        ArticleModel.objects.create(title="Test Title", author="Test Author", category="Test Category", content="Test Content", created_at=datetime.now(tz=timezone.utc))
        article = ArticleModel.objects.get(title="Test Title")

        self.assertEqual(article.category,"Test Category")
