"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from search.views import search_view
from books.views import create_book, create_book_form, book_detail_view, update_book, book_delete_view

urlpatterns = [
    path('', include('articles.urls')),
    path('search/', search_view, name="search"),
    path("pantry/recipes/", include('recipee.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('<int:pk>/', create_book, name="create-book"),
    path('book/<int:pk>/', book_detail_view, name="detail-book"),
    path('book/<int:pk>/update/', update_book, name="update-book"),
    path('book/<int:pk>/delete/', book_delete_view, name="delete-book"),
    path('htmx/create-book-form/', create_book_form, name="create-book-form"),
]
