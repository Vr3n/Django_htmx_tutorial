from django.urls import path
from .views import home, article_search_view,article_detail, article_create_view

urlpatterns = [
    path('', home, name="home"),
    path('articles/create', article_create_view, name="article_create"),
    path('articles/', article_search_view, name="article_search"),
    path('articles/<slug:slug>/', article_detail, name="article_detail"),
]
