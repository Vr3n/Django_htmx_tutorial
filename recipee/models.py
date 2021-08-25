import pint
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import reverse

from .utils import number_str_to_float
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

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={"id": self.id})

    def get_update_url(self):
        return reverse('recipes:update', kwargs={ 'id': self.id })

    def get_ingredients_children(self):
        return self.recipeingredient_set.all()


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=10)
    quantity_in_float = models.FloatField(blank=True, null=True)
    # valid unit measurements -> [ "pounds", 'lbs', 'oz', 'gram']
    unit = models.CharField(max_length=10, validators=[
                            validate_unit_of_measure])
    direction = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    updated_on = models.DateTimeField(auto_now=timezone.now)

    def convert_to_system(self, system: str = "mks") -> str:
        if self.quantity_in_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_in_float * ureg[self.unit]
        return measurement

    def as_mks(self):
        measurement = self.convert_to_system(system="mks")
        print("mks: ", measurement)
        return measurement.to_base_units()

    def as_imperial(self):
        measurement = self.convert_to_system(system="imperial")
        print("imperial: ", measurement)
        return measurement.to_base_units()

    def __str__(self):
        return f"{self.name} - {self.recipe}"

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)

        if qty_as_float_success:
            self.quantity_in_float = qty_as_float
        else:
            self.quantity_in_float = None

        super().save(*args, **kwargs)
