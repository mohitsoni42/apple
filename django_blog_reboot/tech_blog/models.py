from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.title