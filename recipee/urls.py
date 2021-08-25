from django.urls import path

from .views import (
    recipe_create_view,
    recipe_list_view,
    recipe_detail_view,
    recipe_update_view,
    recipe_search_view
)


app_name="recipes" # recipes:list / recipes:create

urlpatterns = [
    path('create/', recipe_create_view, name="create"),
    path('search/', recipe_search_view, name="search"),
    path('<int:id>/edit/', recipe_update_view, name="update"),
    path('<int:id>/', recipe_detail_view, name="detail"),
    path('', recipe_list_view, name="list"),
]