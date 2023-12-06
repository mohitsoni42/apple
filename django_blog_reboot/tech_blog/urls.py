from django.urls import path
from .views import Home, Article, ArticleDetail

urlpatterns =[
    path('', Home.as_view()),
    path('articles', Article.as_view()),
    path('articles/<int:id>', ArticleDetail.as_view())
]