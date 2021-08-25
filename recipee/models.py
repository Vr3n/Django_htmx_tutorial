from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from .validators import validate_unit_of_measure


# Create your models here.


"""
- User
    - Ingredients
    - Recipes
        - Ingredients.
        - Directions for Ingredients.
"""
User = get_user_model()


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    updated_on = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=10)
    # valid unit measurements -> [ "pounds", 'lbs', 'oz', 'gram']
    unit = models.CharField(max_length=10, validators=[validate_unit_of_measure])
    direction = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    updated_on = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.recipe}"