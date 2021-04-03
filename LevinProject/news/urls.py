from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from news.models import News

urlpatterns = [
    path('', ListView.as_view(queryset=News.objects.all().order_by("-date"), template_name="news/news.html")),
    path('<int:pk>', DetailView.as_view(model = News, template_name="news/one.html")),
]