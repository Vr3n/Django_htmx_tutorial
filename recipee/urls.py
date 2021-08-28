from django.urls import path

from .views import (
    recipe_create_view,
    recipe_list_view,
    recipe_detail_view,
    recipe_detail_hx_view,
    recipe_ingredient_detail_hx_view,
    recipe_update_view,
    recipe_search_view
)


app_name = "recipes"  # recipes:list / recipes:create

urlpatterns = [
    path('create/', recipe_create_view, name="create"),
    path('search/', recipe_search_view, name="search"),
    path('<int:id>/edit/', recipe_update_view, name="update"),
    path('hx/<int:id>/', recipe_detail_hx_view, name="hx-detail"),
    path('hx/<int:parent_id>/ingredient/<int:id>/',
         recipe_ingredient_detail_hx_view, name="hx-ingredient-detail"),
    path('hx/<int:parent_id>/ingredient/',
         recipe_ingredient_detail_hx_view, name="hx-ingredient-new"),
    path('<int:id>/', recipe_detail_view, name="detail"),
    path('', recipe_list_view, name="list"),
]
