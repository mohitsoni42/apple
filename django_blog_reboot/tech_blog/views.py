from django.shortcuts import render, redirect
from datetime import datetime
from django.views import View
from django.http import HttpResponse
from .models import ArticleModel
from django.utils import timezone
from .forms import ArticleForm


# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("heyyyy o")
    
    def post(self, request):
        return HttpResponse("postttoo")
    
class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return  render (request, "articles.html", {"articles": articles, "form": ArticleForm() })
    
    def post(self, request):
        form = ArticleForm(request.POST)
        form.instance.created_at = datetime.now(tz=timezone.utc)
        form.save()

        return redirect("/tech-blog/articles")
    
 
class ArticleDetail(View):
    def get(self, request, id):
        article = ArticleModel.objects.get(id=id)

        return  render(request, "article_details.html", {"article": article })
